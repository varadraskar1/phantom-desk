import pytest

from core.plugin_manager import PluginManager
from plugins.plugin import Plugin


class MockPlugin(Plugin):
    @property
    def name(self) -> str:
        return "mock"

    def execute(self, input_data: dict) -> dict:
        return {
            "plugin": self.name,
            "input": input_data,
        }


def test_register_and_get_plugin():
    manager = PluginManager()
    plugin = MockPlugin()

    manager.register(plugin)

    assert manager.get("mock") is plugin


def test_list_plugins():
    manager = PluginManager()

    manager.register(MockPlugin())

    assert manager.list_plugins() == ["mock"]


def test_execute_plugin():
    manager = PluginManager()

    manager.register(MockPlugin())

    result = manager.execute("mock", {"message": "hello"})

    assert result["plugin"] == "mock"
    assert result["input"]["message"] == "hello"


def test_duplicate_plugin_rejected():
    manager = PluginManager()

    manager.register(MockPlugin())

    with pytest.raises(ValueError):
        manager.register(MockPlugin())


def test_unknown_plugin_rejected():
    manager = PluginManager()

    with pytest.raises(KeyError):
        manager.get("does-not-exist")