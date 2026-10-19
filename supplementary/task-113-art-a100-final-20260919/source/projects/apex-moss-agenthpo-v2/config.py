"""Load gateway credentials from .env.local and expose them as Anthropic SDK env vars.

The Anthropic SDK appends /v1/messages to the base URL, so a trailing /v1 in
TOKENROUTER_BASE_URL must be stripped.
"""

import os
from pathlib import Path

EXECUTOR_MODEL = "claude-haiku-4-5"
PROPOSER_MODEL = os.environ.get("PROPOSER_MODEL", "claude-sonnet-4-6")


def find_env_file(start: Path | None = None) -> Path | None:
    d = (start or Path(__file__).resolve().parent)
    for p in [d, *d.parents]:
        f = p / ".env.local"
        if f.exists():
            return f
    return None


def load_env() -> dict:
    env_file = find_env_file()
    values = {}
    if env_file:
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            values[k.strip()] = v.strip()

    base = values.get("TOKENROUTER_BASE_URL", "").rstrip("/")
    if base.endswith("/v1"):
        base = base[: -len("/v1")]
    key = values.get("TOKENROUTER_API_KEY", "")

    # The session may inherit credentials for Claude Code's own gateway. This
    # experiment's local file is authoritative for its SDK subprocesses.
    if base:
        os.environ["ANTHROPIC_BASE_URL"] = base
    if key:
        os.environ["ANTHROPIC_API_KEY"] = key
    return values


if __name__ == "__main__":
    load_env()
    print("ANTHROPIC_BASE_URL:", os.environ.get("ANTHROPIC_BASE_URL"))
    print("ANTHROPIC_API_KEY set:", bool(os.environ.get("ANTHROPIC_API_KEY")))
