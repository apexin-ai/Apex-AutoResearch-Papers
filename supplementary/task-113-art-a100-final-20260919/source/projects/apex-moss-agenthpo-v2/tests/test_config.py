"""Gateway environment precedence (no API calls)."""

import config


def test_local_env_overrides_inherited_gateway(tmp_path, monkeypatch):
    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "TOKENROUTER_BASE_URL=https://task-gateway.example/v1\n"
        "TOKENROUTER_API_KEY=[REDACTED]"
    )
    monkeypatch.setattr(config, "find_env_file", lambda: env_file)
    monkeypatch.setenv("ANTHROPIC_BASE_URL", "https://inherited.example")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "inherited-key")

    config.load_env()

    assert config.os.environ["ANTHROPIC_BASE_URL"] == (
        "https://task-gateway.example"
    )
    assert config.os.environ["ANTHROPIC_API_KEY"] == "task-key"
