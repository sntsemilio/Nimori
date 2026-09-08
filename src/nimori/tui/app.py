"""Estructura navegable del espacio de trabajo Nimori."""

from __future__ import annotations

from textual import events
from textual.app import App, ComposeResult
from textual.containers import Grid, Vertical
from textual.widget import Widget
from textual.widgets import Footer, Header, Markdown, RichLog, Static, TabbedContent, TabPane, TextArea

from nimori.tui.content import (
    CHART_PLACEHOLDER,
    CODE_SAMPLE,
    FORMULA_PLACEHOLDER,
    GUIDE,
    PAPER_PLACEHOLDER,
)


class Region(Vertical):
    """Una región que puede recibir foco y ampliarse."""

    can_focus = True


class NimoriApp(App[None]):
    """Base visual para conectar los próximos módulos de Nimori."""

    TITLE = "Nimori"
    SUB_TITLE = "Pequeños modelos. Grandes preguntas."
    COMPACT_WIDTH = 100
    REGION_IDS = ("guide-panel", "code-panel", "reference-panel", "log-panel")

    CSS = """
    Screen {
        background: #121722;
        color: #E7ECF4;
    }

    Header {
        background: #1A2231;
        color: #FFD88A;
    }

    #workspace {
        layout: grid;
        grid-size: 3 2;
        grid-columns: 1fr 2fr 1fr;
        grid-rows: 1fr 11;
        grid-gutter: 1;
        padding: 1;
    }

    #workspace.solo {
        grid-size: 1;
        grid-columns: 1fr;
        grid-rows: 1fr;
    }

    .region {
        height: 100%;
        border: round #39465D;
        background: #171E2A;
    }

    .region:focus-within, .region:focus {
        border: round #A8E6CF;
    }

    #log-panel {
        column-span: 3;
    }

    #workspace.solo #log-panel {
        column-span: 1;
    }

    .region-title {
        height: 1;
        padding: 0 1;
        background: #202A3A;
        color: #FFD88A;
        text-style: bold;
    }

    Markdown, .placeholder {
        padding: 1 2;
    }

    TextArea, RichLog, TabbedContent {
        height: 1fr;
    }

    TextArea {
        border: none;
        background: #10151E;
    }

    TabbedContent {
        background: #171E2A;
    }

    TabPane {
        padding: 0;
    }

    RichLog {
        padding: 1 2;
        background: #10151E;
    }

    Footer {
        background: #1A2231;
    }
    """

    BINDINGS = [
        ("1", "show_region('guide-panel')", "Guía"),
        ("2", "show_region('code-panel')", "Código"),
        ("3", "show_region('reference-panel')", "Referencias"),
        ("4", "show_region('log-panel')", "Logs"),
        ("z", "toggle_solo", "Ampliar"),
        ("q", "quit", "Salir"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.selected_region = "guide-panel"
        self.compact = False
        self.manual_solo = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with Grid(id="workspace"):
            with Region(id="guide-panel", classes="region"):
                yield Static("GUÍA", classes="region-title")
                yield Markdown(GUIDE, id="guide-content")
            with Region(id="code-panel", classes="region"):
                yield Static("CÓDIGO · referencia didáctica", classes="region-title")
                yield TextArea(
                    CODE_SAMPLE,
                    language="python",
                    read_only=True,
                    show_line_numbers=True,
                    tab_behavior="focus",
                    id="code-view",
                )
            with Region(id="reference-panel", classes="region"):
                yield Static("REFERENCIAS", classes="region-title")
                with TabbedContent(initial="paper-tab", id="reference-tabs"):
                    with TabPane("Paper", id="paper-tab"):
                        yield Static(PAPER_PLACEHOLDER, classes="placeholder", id="paper-content")
                    with TabPane("Fórmulas", id="formula-tab"):
                        yield Static(FORMULA_PLACEHOLDER, classes="placeholder", id="formula-content")
                    with TabPane("Gráficos", id="chart-tab"):
                        yield Static(CHART_PLACEHOLDER, classes="placeholder", id="chart-content")
            with Region(id="log-panel", classes="region"):
                yield Static("EJECUCIÓN / LOGS", classes="region-title")
                yield RichLog(id="event-log", wrap=True, highlight=True)
        yield Footer()

    def on_mount(self) -> None:
        log = self.query_one("#event-log", RichLog)
        log.write("[scripted] Espacio de trabajo listo; no hay una ejecución activa.")
        log.write("El worker cancelable se incorporará en NIM-103.")
        self.compact = self.size.width < self.COMPACT_WIDTH
        self._refresh_regions()
        self.query_one("#guide-panel", Region).focus()

    def on_resize(self, event: events.Resize) -> None:
        compact = event.size.width < self.COMPACT_WIDTH
        if compact != self.compact:
            self.compact = compact
            self._refresh_regions()

    def action_show_region(self, region_id: str) -> None:
        if region_id not in self.REGION_IDS:
            return
        self.selected_region = region_id
        if self.compact or self.manual_solo:
            self._refresh_regions()
        self.query_one(f"#{region_id}", Region).focus()

    def action_toggle_solo(self) -> None:
        self.selected_region = self._focused_region() or self.selected_region
        self.manual_solo = not self.manual_solo
        self._refresh_regions()

    def _focused_region(self) -> str | None:
        node: Widget | None = self.focused
        while node is not None:
            if node.id in self.REGION_IDS:
                return node.id
            parent = node.parent
            node = parent if isinstance(parent, Widget) else None
        return None

    def _refresh_regions(self) -> None:
        solo = self.compact or self.manual_solo
        workspace = self.query_one("#workspace", Grid)
        workspace.set_class(solo, "solo")
        for region_id in self.REGION_IDS:
            self.query_one(f"#{region_id}", Region).display = not solo or region_id == self.selected_region


def run() -> None:
    """Abre la TUI; se mantiene separado del comando principal hasta NIM-106."""

    NimoriApp().run()
