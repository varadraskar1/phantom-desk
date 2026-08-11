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


def test_plugin_execution():
    plugin = MockPlugin()

    result = plugin.execute({"message": "hello"})

    assert result["plugin"] == "mock"
    assert result["input"]["message"] == "hello"