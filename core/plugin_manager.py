from plugins.plugin import Plugin


class PluginManager:
    """Manage registered Phantom Desk plugins."""

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin) -> None:
        """Register a plugin by its unique name."""
        if plugin.name in self._plugins:
            raise ValueError(f"Plugin already registered: {plugin.name}")

        self._plugins[plugin.name] = plugin

    def get(self, name: str) -> Plugin:
        """Return a registered plugin."""
        try:
            return self._plugins[name]
        except KeyError:
            raise KeyError(f"Plugin not found: {name}")

    def list_plugins(self) -> list[str]:
        """Return the names of all registered plugins."""
        return list(self._plugins)

    def execute(self, name: str, input_data: dict) -> dict:
        """Execute a registered plugin."""
        plugin = self.get(name)
        return plugin.execute(input_data)