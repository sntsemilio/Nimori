"""Contratos de navegación del primer módulo visual."""

import asyncio
import unittest

from textual.widgets import TabbedContent

from nimori.tui.app import NimoriApp, Region


class WorkspaceTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        # Textual procesa el montaje completo en un solo callback durante estas pruebas.
        asyncio.get_running_loop().slow_callback_duration = 1.0

    async def test_wide_workspace_exposes_four_regions_and_reference_tabs(self):
        app = NimoriApp()
        async with app.run_test(size=(140, 42)) as pilot:
            regions = list(app.query(Region))
            self.assertEqual([region.id for region in regions], list(app.REGION_IDS))
            self.assertTrue(all(region.display for region in regions))
            tabs = app.query_one("#reference-tabs", TabbedContent)
            self.assertEqual(tabs.tab_count, 3)
            await pilot.press("3", "tab", "right")
            self.assertEqual(tabs.active, "formula-tab")

    async def test_region_can_be_expanded_and_restored(self):
        app = NimoriApp()
        async with app.run_test(size=(140, 42)) as pilot:
            await pilot.press("3", "z")
            self.assertEqual(app.selected_region, "reference-panel")
            visible = [region.id for region in app.query(Region) if region.display]
            self.assertEqual(visible, ["reference-panel"])
            await pilot.press("z")
            self.assertTrue(all(region.display for region in app.query(Region)))

    async def test_compact_workspace_switches_one_region_at_a_time(self):
        app = NimoriApp()
        async with app.run_test(size=(80, 24)) as pilot:
            self.assertTrue(app.compact)
            self.assertEqual(
                [region.id for region in app.query(Region) if region.display],
                ["guide-panel"],
            )
            await pilot.press("2")
            self.assertEqual(
                [region.id for region in app.query(Region) if region.display],
                ["code-panel"],
            )

    async def test_resize_enters_and_leaves_compact_mode(self):
        app = NimoriApp()
        async with app.run_test(size=(140, 42)) as pilot:
            await pilot.resize_terminal(80, 24)
            self.assertTrue(app.compact)
            self.assertEqual(sum(region.display for region in app.query(Region)), 1)
            await pilot.resize_terminal(140, 42)
            self.assertFalse(app.compact)
            self.assertTrue(all(region.display for region in app.query(Region)))


if __name__ == "__main__":
    unittest.main()
