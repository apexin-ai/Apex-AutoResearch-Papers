"""Smoke test: AIDE's LLM layer against Apexin with the parity patch."""
import os
import sys

sys.path.insert(0, "/root/fml-bench")

from agents.llm import create_client, get_response_from_llm  # noqa: E402

print("FML_REASONING_EFFORT =", os.environ.get("FML_REASONING_EFFORT", "(unset->high)"))
client, model = create_client("gpt-5.6-sol", "OpenAI")
print("client base_url =", str(client.base_url))
print("model =", model)
out = get_response_from_llm(
    "Reply with exactly: AIDE-OK",
    client,
    model,
    "You are a smoke test.",
    print_debug=False,
)
print("response tail:", str(out)[-160:])
