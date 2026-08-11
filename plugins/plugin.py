from abc import ABC, abstractmethod


class Plugin(ABC):
    """Base interface for Phantom Desk plugins."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the unique plugin name."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, input_data: dict) -> dict:
        """Execute the plugin with the supplied input."""
        raise NotImplementedError