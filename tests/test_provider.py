from core.provider import AIProvider


class MockProvider(AIProvider):
    def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"


def test_provider_generates_response():
    provider = MockProvider()

    response = provider.generate("Hello Phantom Desk")

    assert response == "Mock response: Hello Phantom Desk"