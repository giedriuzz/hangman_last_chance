"""

An implementation of a classic calculator, with a layout inspired by macOS calculator.


"""
import logging
import logging.config
from textual.logging import TextualHandler
from pathlib import Path
from decimal import Decimal

from textual import events, on
from textual.screen import Screen
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.css.query import NoMatches
from textual.reactive import var
from textual.widgets import (
    Button,
    Static,
    Header,
    Footer,
    Input,
    Markdown,
    Label,
    Tabs,
    Tab,
    TabbedContent,
    TabPane,
)

# logging.basicConfig(
#     level="NOTSET",
#     handlers=[TextualHandler()],
# )

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger("sLogger")

TAB_NAMES = ["User", "Help"]


class Welcome(Static):
    """A welcome screen."""

    def compose(self) -> ComposeResult:
        yield Container(Label("Čia yra puslapis", id="Welcome"))


class Game(Static):
    def compose(self) -> ComposeResult:
        yield Container(Label("Čia yra Game puslapis", id="Welcome"))


class User(Static):
    """A widget for registering a new user."""

    def compose(self) -> ComposeResult:
        yield Container(Label("Čia yra User puslapis", id="Welcome"))


class Help(Static):
    """The help screen for the application."""

    BINDINGS = [("escape,space,q,question_mark", "pop_screen", "Close")]
    """Bindings for the help screen."""

    def compose(self) -> ComposeResult:
        """Compose the game's help.

        Returns:
            ComposeResult: The result of composing the help screen.
        """

        yield Markdown(Path(__file__).with_suffix(".md").read_text())


class Hangman(App):
    """A working 'Hangman' game."""

    TITLE = "Hangman game"
    BINDINGS = [
        ("ctrl+d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        logger.info("Creating child widgets")
        yield Header(show_clock=True)
        with TabbedContent():
            with TabPane("Game", id="game"):
                yield Game()
            with TabPane("User", id="user"):
                yield User()
            with TabPane("Help", id="help"):
                yield Help()

        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.dark = not self.dark

    # def action_open_help(self) -> None:
    #     """An action to open the help screen"""
    #     self.open_help(Help())

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        """Handle TabActivated message sent by Tabs."""
        tab_event = event
        logger.debug(event.tab.id)
        if tab_event == "help":
            # When the tabs are cleared, event.tab will be None
            logger.debug(tab_event)
            yield Help()


if __name__ == "__main__":
    app = Hangman()
    app.run()
