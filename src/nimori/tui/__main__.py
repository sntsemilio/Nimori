"""Permite probar el espacio de trabajo con ``python -m nimori.tui``."""

from nimori.tui.app import NimoriApp


def main() -> None:
    NimoriApp().run()


if __name__ == "__main__":
    main()
