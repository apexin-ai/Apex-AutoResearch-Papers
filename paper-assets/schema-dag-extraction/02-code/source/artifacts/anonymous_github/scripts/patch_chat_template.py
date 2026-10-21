"""Show diff for adding chat template to run_extraction.py.

Does NOT modify run_extraction.py — only prints the proposed patch to stdout.
"""
import difflib
from pathlib import Path

SRC = Path("./src/run_extraction.py")

original = SRC.read_text()
lines = original.splitlines(keepends=True)

# Find the line: "            outputs = llm.generate(prompts, sampling_params)"
insert_idx = None
for i, line in enumerate(lines):
    if "outputs = llm.generate(prompts, sampling_params)" in line:
        insert_idx = i
        break

if insert_idx is None:
    print("ERROR: Could not find 'llm.generate(prompts, sampling_params)' in run_extraction.py")
    raise SystemExit(1)

# Build the chat template block to insert before llm.generate
chat_template_block = [
    "\n",
    "            # Apply chat template for instruct models (e.g. LLaMA-3.1-Instruct)\n",
    "            tokenizer = llm.get_tokenizer()\n",
    "            if hasattr(tokenizer, 'chat_template') and tokenizer.chat_template:\n",
    "                prompts = [\n",
    "                    tokenizer.apply_chat_template(\n",
    '                        [{"role": "user", "content": p}],\n',
    "                        tokenize=False,\n",
    "                        add_generation_prompt=True,\n",
    "                    )\n",
    "                    for p in prompts\n",
    "                ]\n",
    "\n",
]

modified_lines = lines[:insert_idx] + chat_template_block + lines[insert_idx:]
modified = "".join(modified_lines)

diff = difflib.unified_diff(
    original.splitlines(keepends=True),
    modified.splitlines(keepends=True),
    fromfile="src/run_extraction.py (original)",
    tofile="src/run_extraction.py (patched)",
    n=3,
)

print("".join(diff))
print(f"\nInsert point: line {insert_idx + 1}")
print("Status: DIFF ONLY — run_extraction.py NOT modified")
