# code adapt training script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_code_adapt-training-script_20260516T045559.jsonl`
- **Structured JSON:** [`4c7e3441811a9d151d04.json`](../../sessions/4c/4c7e3441811a9d151d04.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-16T04:58:29.442948+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:58:29.443328+00:00_

build_data.py
mvp_a_total_sim.py
build_cwm_data.py
train_cwm_baseline.py
eval_cwm_baseline.py
llm_judge_zeroshot.py
eval_majority_voting.py
artifacts/block_correlation_analysis.py
artifacts/_project/intermediate/analysis_5paired_bootstrap.py
artifacts/analysis_5paired_bootstrap.py
artifacts/_project/intermediate/extract_predictions_generic.py
artifacts/extract_predictions_generic.py
.venv/lib/python3.14/site-packages/pip/__init__.py
.venv/lib/python3.14/site-packages/pip/__main__.py
.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
.venv/lib/python3.14/site-packages/pip/_internal/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
.venv/lib/python3.14/site-packages/pip/_inter
…[truncated 4520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:58:29.443523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/train_cwm_baseline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/train_cwm_baseline.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:58:29.443753+00:00_

1	# train_cwm_baseline.py — Qwen3 LoRA fine-tuning for CWM (Code World Model) generation baseline
2	# Input: data_dir/ with {cwm_train,cwm_val}.jsonl (fields: code, test, target)
3	# Output: LoRA adapter in output_dir/best/
4	# Key difference from train_verifier.py (classification):
5	#   - Prompt asks for execution result instead of pass/fail
6	#   - Target is execution output string (e.g. "PASS: ..." or "FAIL: AssertionError: ...")
7	#   - Standard causal LM loss on target tokens (no classification head)
8	#   - Loss masked on system+user tokens, only computed on assistant response
9	# Same: LoRA config, batch_size, grad_accumulation, lr, epochs, seed, max_seq_len
10	
11	import argparse
12	import json
13	import logging
14	import os
15	
16	import torch
17	from datasets import Dataset
18	from peft import LoraConfig, TaskType, get_peft_model
19	from transformers import (
20	    AutoModelForCausalLM,
21	    AutoTokenizer,
22	    DataCollatorForSeq2Seq,
23	    Trainer,
24	    TrainingArguments,
25	)
26	
27	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
28	log = logging.getLogger(__name__)
29	
30	SYSTEM_PROMPT = (
31	    "You are a code execution simulator. Given a code snippet and a test case, "
32	    "predict the execution result."
33	)
34	
35	
36	def load_jsonl(path):
37	    with open(path) as f:
38	        return [json.loads(line) for line in f]
39	
40	
41	def detect_thinking_support(tokenizer):
42	    """Qwen3 tokenizers support enable_thinking; older ones don't."""
43	    try:
44	        tokenizer.apply_chat_template(
45	            [{"role": "user", "content": "hi"}],
46	            tokenize=False,
47	            enable_thinking=False,
48	        )
49	        return {"enable_thinking": False}
50	    except TypeError:
51	        return {}
52	
53	
54	def build_messages(code, test, target=None):
55	    user_msg = f"## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
56	    msgs = [
57	        {"role": "syste
…[truncated 6558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:58:29.443970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/build_cwm_data.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/build_cwm_data.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:58:29.444179+00:00_

1	# build_cwm_data.py — Convert (code, test, label) data to CWM generation format
2	# Input: data/{train,val,test}.jsonl with fields: code, test, label, source, problem_id, mutation_type
3	# Output: data/{cwm_train,cwm_val,cwm_test}.jsonl with target = execution output string
4	# Key difference from classification: label 0/1 → target string with actual error messages
5	# For fail samples, re-executes code+test to capture stderr; pass samples get fixed string.
6	
7	import argparse
8	import json
9	import logging
10	import os
11	import re
12	import subprocess
13	import sys
14	from collections import Counter
15	
16	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
17	log = logging.getLogger(__name__)
18	
19	PASS_TARGET = "PASS: test completed successfully"
20	DEFAULT_TIMEOUT = 5
21	
22	
23	def load_jsonl(path):
24	    with open(path) as f:
25	        return [json.loads(line) for line in f]
26	
27	
28	def save_jsonl(data, path):
29	    with open(path, "w") as f:
30	        for item in data:
31	            f.write(json.dumps(item) + "\n")
32	
33	
34	def execute_and_capture(code: str, test: str, timeout: int) -> str:
35	    """Execute code + test, return formatted error string for failures."""
36	    full_code = code + "\n" + test
37	    try:
38	        result = subprocess.run(
39	            [sys.executable, "-c", full_code],
40	            capture_output=True, text=True, timeout=timeout,
41	        )
42	        if result.returncode == 0:
43	            return PASS_TARGET
44	
45	        stderr = result.stderr.strip()
46	        if not stderr:
47	            stdout = result.stdout.strip()
48	            if stdout:
49	                return f"FAIL: Error: {stdout.splitlines()[-1]}"
50	            return "FAIL: Error: non-zero exit code"
51	
52	        # Extract the last exception line from traceback
53	        lines = stderr.strip().splitlines()
54	        # Find the last line that looks like an exception
55	        error_line = None
56
…[truncated 5027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:58:29.444333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/build_data.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/build_data.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:58:29.444591+00:00_

1	# Build (code, test) -> pass/fail training data from HumanEval + MBPP
2	# Mutations on canonical solutions generate fail examples; actual execution verifies labels.
3	
4	import argparse
5	import ast
6	import json
7	import os
8	import random
9	import re
10	import subprocess
11	import sys
12	import textwrap
13	import time
14	from collections import Counter, defaultdict
15	from pathlib import Path
16	
17	TIMEOUT = 5  # seconds per test execution
18	MUTANTS_PER_SOLUTION = 4
19	SEED = 42
20	
21	
22	# ── Mutation strategies ──────────────────────────────────────────────
23	
24	def mutate_operators(code: str) -> list[str]:
25	    """Swap arithmetic/comparison operators."""
26	    swaps = [
27	        ('+', '-'), ('-', '+'), ('*', '/'), ('/', '*'),
28	        ('==', '!='), ('!=', '=='),
29	        ('<=', '<'), ('>=', '>'), ('<', '<='), ('>', '>='),
30	        (' and ', ' or '), (' or ', ' and '),
31	    ]
32	    results = []
33	    for old, new in swaps:
34	        if old in code:
35	            mutated = code.replace(old, new, 1)
36	            if mutated != code:
37	                results.append(mutated)
38	    return results
39	
40	
41	def mutate_off_by_one(code: str) -> list[str]:
42	    """Shift integer literals by ±1."""
43	    results = []
44	    # Find integer literals (not inside strings ideally, but good enough)
45	    for match in re.finditer(r'(?&lt;![a-zA-Z_"\'])(\d+)(?![a-zA-Z_"\'])', code):
46	        val = int(match.group(1))
47	        for delta in [1, -1]:
48	            new_val = val + delta
49	            if new_val < 0:
50	                continue
51	            mutated = code[:match.start(1)] + str(new_val) + code[match.end(1):]
52	            if mutated != code:
53	                results.append(mutated)
54	    return results
55	
56	
57	def mutate_return_value(code: str) -> list[str]:
58	    """Modify return statements."""
59	    results = []
60	    lines = code.split('\n')
61	    for i, line in enumerate(lines):
62	        stripped = line.lstrip()
63
…[truncated 19079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T04:58:29.444784+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "train_cls|train_verifier",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "output_mode": "files_with_matches",
  "glob": "*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Grep",
  "tool_args": {
    "pattern": "train_cls|train_verifier",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
    "output_mode": "files_with_matches",
    "glob": "*.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T04:58:29.444957+00:00_

Found 1 file
train_cwm_baseline.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T04:58:29.445081+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/eval_cwm_baseline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/eval_cwm_baseline.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T04:58:29.445314+00:00_

1	# eval_cwm_baseline.py — Evaluate CWM generation baseline on pass/fail classification
2	# Input: data_dir/cwm_test.jsonl + LoRA checkpoint (generation model)
3	# Output: Formatted report to stdout + JSON to --output
4	# Key difference from eval_verifier.py:
5	#   - Generates execution output string instead of "pass"/"fail"
6	#   - Extracts pass/fail from generated output via keyword matching
7	#   - Additional metrics: exact match rate, per-error-type match, generation length stats
8	# Same metrics: class balance, majority baseline, per-class P/R/F1, accuracy, confusion matrix
9	
10	import argparse
11	import json
12	import logging
13	import os
14	import re
15	from collections import Counter, defaultdict
16	
17	import torch
18	from peft import PeftModel
19	from sklearn.metrics import (
20	    accuracy_score,
21	    confusion_matrix,
22	    f1_score,
23	    precision_score,
24	    recall_score,
25	)
26	from transformers import AutoModelForCausalLM, AutoTokenizer
27	
28	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
29	log = logging.getLogger(__name__)
30	
31	SYSTEM_PROMPT = (
32	    "You are a code execution simulator. Given a code snippet and a test case, "
33	    "predict the execution result."
34	)
35	
36	
37	def load_jsonl(path):
38	    with open(path) as f:
39	        return [json.loads(line) for line in f]
40	
41	
42	def detect_thinking_support(tokenizer):
43	    try:
44	        tokenizer.apply_chat_template(
45	            [{"role": "user", "content": "hi"}],
46	            tokenize=False,
47	            enable_thinking=False,
48	        )
49	        return {"enable_thinking": False}
50	    except TypeError:
51	        return {}
52	
53	
54	def build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):
55	    user_msg = f"## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
56	    msgs = [
57	        {"role": "system", "content": SYSTEM_PROMPT},
58	        {"role": "user", "content": user_msg},
59	    ]

…[truncated 11785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T04:58:29.445594+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/train_unified.py",
  "content": "\"\"\"Unified LoRA fine-tuning for CWM (Code World Model) generation — supports multiple model families.\n\nSupported model families:\n  - Qwen3 (e.g. Qwen/Qwen3-4B, Qwen/Qwen3-8B)\n  - DeepSeek-Coder (e.g. deepseek-ai/deepseek-coder-6.7b-instruct)\n\nUsage:\n  # Qwen3-8B\n  python train_unified.py --data_dir data/ --model_name_or_path Qwen/Qwen3-8B \\\n      --output_dir checkpoints_cwm_qwen3_8b/ --run_name cwm-qwen3-8b-lora\n\n  # DeepSeek-Coder-6.7B-Instruct\n  python train_unified.py --data_dir data/ --model_name_or_path deepseek-ai/deepseek-coder-6.7b-instruct \\\n      --output_dir checkpoints_cwm_deepseek/ --run_name cwm-deepseek-6.7b-lora\n\nHyperparams are identical across families: LoRA rank=16, alpha=32, 3 epochs, bf16.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    DataCollatorForSeq2Seq,\n    Trainer,\n    TrainingArguments,\n)\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlog = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are a code execution simulator. Given a code snippet and a test case, \"\n    \"predict the execution result.\"\n)\n\n# ---------------------------------------------------------------------------\n# Model family detection & configuration\n# ---------------------------------------------------------------------------\n\nFAMILY_CONFIG = {\n    \"qwen\": {\n        # Qwen3 uses ChatML-style template; needs enable_thinking=False to suppress &lt;think> tags\n        \"lora_target_modules\": [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\"],\n    },\n    \"deepseek\": {\n        # DeepSeek-Coder-Instruct uses \"### Instruction / ### Response\" template\n        # No special chat template kwargs needed\n        \"lora_target_modules\": [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\"],\n    },\n}\n\n\ndef detect_model_family(model_name: str) -> str:\n    name_lower = model_name.lower()\n    if \"qwen\" in name_lower:\n        return \"qwen\"\n    if \"deepseek\" in name_lower:\n        return \"deepseek\"\n    return \"auto\"\n\n\ndef get_chat_template_kwargs(family: str, tokenizer) -> dict:\n    \"\"\"Return extra kwargs for tokenizer.apply_chat_template(), per model family.\"\"\"\n    if family == \"qwen\":\n        # Qwen3 tokenizers accept enable_thinking; older Qwen2 ones don't\n        try:\n            tokenizer.apply_chat_template(\n                [{\"role\": \"user\", \"content\": \"hi\"}],\n                tokenize=False,\n                enable_thinking=False,\n            )\n            return {\"enable_thinking\": False}\n        except TypeError:\n            return {}\n    # DeepSeek and auto: no special kwargs\n    return {}\n\n\ndef setup_tokenizer(tokenizer, family: str):\n    \"\"\"Ensure pad_token is set; handle family-specific token quirks.\"\"\"\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        log.info(f\"Set pad_token = eos_token ({tokenizer.eos_token!r})\")\n\n    if family == \"deepseek\" and tokenizer.pad_token_id == tokenizer.eos_token_id:\n        # DeepSeek-Coder uses <|EOT|> as eos. Using it as pad is fine for training\n        # with DataCollatorForSeq2Seq (labels are masked), but log it for awareness.\n        log.info(\n            f\"DeepSeek: pad_token_id == eos_token_id == {tokenizer.eos_token_id} \"\n            f\"({tokenizer.eos_token!r})\"\n        )\n\n\ndef get_lora_target_modules(family: str) -> list[str]:\n    cfg = FAMILY_CONFIG.get(family, FAMILY_CONFIG[\"qwen\"])\n    return cfg[\"lora_target_modules\"]\n\n\n# ---------------------------------------------------------------------------\n# Prompt / tokenization (family-agnostic via apply_chat_template)\n# ---------------------------------------------------------------------------\n\ndef build_messages(code, test, target=None):\n    user_msg = f\"## Code\\n{code}\\n\\n## Test\\n{test}\\n\\nWhat is the execution result?\"\n    msgs = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_msg},\n    ]\n    if target is not None:\n        msgs.append({\"role\": \"assistant\", \"content\": target})\n    return msgs\n\n\ndef _try_apply_chat_template(tokenizer, messages, tmpl_kw, **kwargs):\n    \"\"\"apply_chat_template with graceful fallback if system role is unsupported.\"\"\"\n    try:\n        return tokenizer.apply_chat_template(messages, **tmpl_kw, **kwargs)\n    except Exception:\n        # Some models don't support system role — merge system into first user message\n        merged = []\n        sys_content = \"\"\n        for m in messages:\n            if m[\"role\"] == \"system\":\n                sys_content = m[\"content\"]\n            elif m[\"role\"] == \"user\" and sys_content:\n                merged.append({\"role\": \"user\", \"content\": sys_content + \"\\n\\n\" + m[\"content\"]})\n                sys_content = \"\"\n            else:\n                merged.append(m)\n        return tokenizer.apply_chat_template(merged, **tmpl_kw, **kwargs)\n\n\ndef tokenize_example(tokenizer, code, test, target, max_len, tmpl_kw):\n    prompt_ids = _try_apply_chat_template(\n        tokenizer,\n        build_messages(code, test),\n        tmpl_kw,\n        tokenize=True,\n        add_generation_prompt=True,\n    )\n    full_ids = _try_apply_chat_template(\n        tokenizer,\n        build_messages(code, test, target),\n        tmpl_kw,\n        tokenize=True,\n        add_generation_prompt=False,\n    )\n\n    truncated = len(full_ids) > max_len\n    if truncated:\n        full_ids = full_ids[:max_len]\n\n    prompt_len = min(len(prompt_ids), len(full_ids))\n    labels = [-100] * prompt_len + full_ids[prompt_len:]\n\n    return {\n        \"input_ids\": full_ids,\n        \"labels\": labels,\n        \"attention_mask\": [1] * len(full_ids),\n    }, truncated\n\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef preprocess_split(tokenizer, data, max_len, name, tmpl_kw):\n    out = {\"input_ids\": [], \"labels\": [], \"attention_mask\": []}\n    n_trunc = 0\n    for ex in data:\n        tok, trunc = tokenize_example(\n            tokenizer, ex[\"code\"], ex[\"test\"], ex[\"target\"], max_len, tmpl_kw,\n        )\n        for k in out:\n            out[k].append(tok[k])\n        n_trunc += int(trunc)\n    pct = n_trunc / len(data) * 100 if data else 0\n    log.info(f\"{name}: {n_trunc}/{len(data)} truncated ({pct:.1f}%)\")\n    return Dataset.from_dict(out)\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    p = argparse.ArgumentParser(description=\"Unified LoRA CWM training (Qwen / DeepSeek / auto)\")\n    p.add_argument(\"--data_dir\", required=True)\n    p.add_argument(\"--model_name_or_path\", required=True, help=\"HF model id or local path\")\n    p.add_argument(\"--output_dir\", default=\"checkpoints_cwm/\")\n    p.add_argument(\"--wandb_project\", default=\"exec-sim-repair-verifier\")\n    p.add_argument(\"--run_name\", default=None, help=\"W&B run name (auto-generated if omitted)\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_seq_length\", type=int, default=2048)\n    p.add_argument(\"--batch_size\", type=int, default=2)\n    p.add_argument(\"--grad_accumulation\", type=int, default=16)\n    p.add_argument(\"--lr\", type=float, default=2e-4)\n    p.add_argument(\"--epochs\", type=int, default=3)\n    p.add_argument(\"--warmup_ratio\", type=float, default=0.1)\n    p.add_argument(\"--lora_rank\", type=int, default=16)\n    p.add_argument(\"--lora_alpha\", type=int, default=32)\n    p.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    p.add_argument(\"--max_steps\", type=int, default=-1)\n    p.add_argument(\"--no_wandb\", action=\"store_true\")\n    args = p.parse_args()\n\n    family = detect_model_family(args.model_name_or_path)\n    log.info(f\"Model: {args.model_name_or_path} → family={family}\")\n\n    if args.run_name is None:\n        # e.g. \"Qwen/Qwen3-8B\" → \"cwm-qwen3-8b-lora\"\n        short = args.model_name_or_path.split(\"/\")[-1].lower().replace(\"_\", \"-\")\n        args.run_name = f\"cwm-{short}-lora\"\n    log.info(f\"Run name: {args.run_name}\")\n\n    if args.no_wandb:\n        os.environ[\"WANDB_DISABLED\"] = \"true\"\n    else:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n\n    # ── Tokenizer ──\n    log.info(f\"Loading tokenizer: {args.model_name_or_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name_or_path, trust_remote_code=True, padding_side=\"right\",\n    )\n    setup_tokenizer(tokenizer, family)\n    tmpl_kw = get_chat_template_kwargs(family, tokenizer)\n    log.info(f\"Chat template kwargs: {tmpl_kw}\")\n\n    # Sanity check: render one example to verify template works\n    sample_text = _try_apply_chat_template(\n        tokenizer,\n        build_messages(\"def f(): return 1\", \"assert f() == 1\", \"PASS: test completed successfully\"),\n        tmpl_kw,\n        tokenize=False,\n        add_generation_prompt=False,\n    )\n    log.info(f\"Sample formatted prompt (first 300 chars):\\n{sample_text[:300]}\")\n\n    # ── Data ──\n    train_raw = load_jsonl(os.path.join(args.data_dir, \"cwm_train.jsonl\"))\n    val_raw = load_jsonl(os.path.join(args.data_dir, \"cwm_val.jsonl\"))\n    log.info(f\"Loaded train={len(train_raw)}, val={len(val_raw)}\")\n\n    train_ds = preprocess_split(tokenizer, train_raw, args.max_seq_length, \"train\", tmpl_kw)\n    val_ds = preprocess_split(tokenizer, val_raw, args.max_seq_length, \"val\", tmpl_kw)\n\n    # ── Model ──\n    log.info(f\"Loading model: {args.model_name_or_path}\")\n    try:\n        import flash_attn  # noqa: F401\n        attn_impl = \"flash_attention_2\"\n    except ImportError:\n        attn_impl = \"sdpa\"\n    log.info(f\"Attention: {attn_impl}\")\n\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name_or_path,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        attn_implementation=attn_impl,\n    )\n    model.config.use_cache = False\n\n    # ── LoRA ──\n    target_modules = get_lora_target_modules(family)\n    log.info(f\"LoRA target modules: {target_modules}\")\n\n    lora_cfg = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=args.lora_dropout,\n        target_modules=target_modules,\n    )\n    model = get_peft_model(model, lora_cfg)\n    model.enable_input_require_grads()\n    model.print_trainable_parameters()\n\n    # ── Training ──\n    collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)\n\n    is_dryrun = args.max_steps > 0\n    ta = {\n        \"output_dir\": args.output_dir,\n        \"num_train_epochs\": args.epochs,\n        \"max_steps\": args.max_steps,\n        \"per_device_train_batch_size\": args.batch_size,\n        \"per_device_eval_batch_size\": args.batch_size,\n        \"gradient_accumulation_steps\": args.grad_accumulation,\n        \"learning_rate\": args.lr,\n        \"warmup_ratio\": args.warmup_ratio,\n        \"bf16\": True,\n        \"logging_steps\": 1 if is_dryrun else 50,\n        \"eval_strategy\": \"no\" if is_dryrun else \"epoch\",\n        \"save_strategy\": \"no\" if is_dryrun else \"epoch\",\n        \"load_best_model_at_end\": not is_dryrun,\n        \"save_total_limit\": 2,\n        \"seed\": args.seed,\n        \"run_name\": args.run_name,\n        \"report_to\": \"none\" if args.no_wandb else \"wandb\",\n        \"gradient_checkpointing\": True,\n        \"dataloader_num_workers\": 4,\n    }\n    if not is_dryrun:\n        ta[\"metric_for_best_model\"] = \"eval_loss\"\n        ta[\"greater_is_better\"] = False\n    training_args = TrainingArguments(**ta)\n\n    trainer = Trainer(\n        model=model,\n        args=training_args,\n        train_dataset=train_ds,\n        eval_dataset=val_ds,\n        data_collator=collator,\n    )\n\n    log.info(\"Starting training...\")\n    trainer.train()\n\n    if not is_dryrun:\n        best_dir = os.path.join(args.output_dir, \"best\")\n        trainer.save_model(best_dir)\n        tokenizer.save_pretrained(best_dir)\n        log.info(f\"Best model saved to {best_dir}\")\n    else:\n        log.info(\"Dry-run complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/train_unified.py",
    "content": "\"\"\"Unified LoRA fine-tuning for CWM (Code World Model) generation — supports multiple model families.\n\nSupported model families:\n  - Qwen3 (e.g. Qwen/Qwen3-4B, Qwen/Qwen3-8B)\n  - DeepSeek-Coder (e.g. deepseek-ai/deepseek-coder-6.7b-instruct)\n\nUsage:\n  # Qwen3-8B\n  python train_unified.py --data_dir data/ --model_name_or_path Qwen/Qwen3-8B \\\n      --output_dir checkpoints_cwm_qwen3_8b/ --run_name cwm-qwen3-8b-lora\n\n  # DeepSeek-Coder-6.7B-Instruct\n  python train_unified.py --data_dir data/ --model_name_or_path deepseek-ai/deepseek-coder-6.7b-instruct \\\n      --output_dir checkpoints_cwm_deepseek/ --run_name cwm-deepseek-6.7b-lora\n\nHyperparams are identical across families: LoRA rank=16, alpha=32, 3 epochs, bf16.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\n\nimport torch\nfrom datasets import Dataset\nfrom peft import LoraConfig, TaskType, get_peft_model\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    DataCollatorForSeq2Seq,\n    Trainer,\n    TrainingArguments,\n)\n\nlogging.basicConfig(level=logging.INFO, format=\"%(asctime)s %(levelname)s %(message)s\")\nlog = logging.getLogger(__name__)\n\nSYSTEM_PROMPT = (\n    \"You are a code execution simulator. Given a code snippet and a test case, \"\n    \"predict the execution result.\"\n)\n\n# ---------------------------------------------------------------------------\n# Model family detection & configuration\n# ---------------------------------------------------------------------------\n\nFAMILY_CONFIG = {\n    \"qwen\": {\n        # Qwen3 uses ChatML-style template; needs enable_thinking=False to suppress &lt;think> tags\n        \"lora_target_modules\": [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\"],\n    },\n    \"deepseek\": {\n        # DeepSeek-Coder-Instruct uses \"### Instruction / ### Response\" template\n        # No special chat template kwargs needed\n        \"lora_target_modules\": [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\"],\n    },\n}\n\n\ndef detect_model_family(model_name: str) -> str:\n    name_lower = model_name.lower()\n    if \"qwen\" in name_lower:\n        return \"qwen\"\n    if \"deepseek\" in name_lower:\n        return \"deepseek\"\n    return \"auto\"\n\n\ndef get_chat_template_kwargs(family: str, tokenizer) -> dict:\n    \"\"\"Return extra kwargs for tokenizer.apply_chat_template(), per model family.\"\"\"\n    if family == \"qwen\":\n        # Qwen3 tokenizers accept enable_thinking; older Qwen2 ones don't\n        try:\n            tokenizer.apply_chat_template(\n                [{\"role\": \"user\", \"content\": \"hi\"}],\n                tokenize=False,\n                enable_thinking=False,\n            )\n            return {\"enable_thinking\": False}\n        except TypeError:\n            return {}\n    # DeepSeek and auto: no special kwargs\n    return {}\n\n\ndef setup_tokenizer(tokenizer, family: str):\n    \"\"\"Ensure pad_token is set; handle family-specific token quirks.\"\"\"\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        log.info(f\"Set pad_token = eos_token ({tokenizer.eos_token!r})\")\n\n    if family == \"deepseek\" and tokenizer.pad_token_id == tokenizer.eos_token_id:\n        # DeepSeek-Coder uses <|EOT|> as eos. Using it as pad is fine for training\n        # with DataCollatorForSeq2Seq (labels are masked), but log it for awareness.\n        log.info(\n            f\"DeepSeek: pad_token_id == eos_token_id == {tokenizer.eos_token_id} \"\n            f\"({tokenizer.eos_token!r})\"\n        )\n\n\ndef get_lora_target_modules(family: str) -> list[str]:\n    cfg = FAMILY_CONFIG.get(family, FAMILY_CONFIG[\"qwen\"])\n    return cfg[\"lora_target_modules\"]\n\n\n# ---------------------------------------------------------------------------\n# Prompt / tokenization (family-agnostic via apply_chat_template)\n# ---------------------------------------------------------------------------\n\ndef build_messages(code, test, target=None):\n    user_msg = f\"## Code\\n{code}\\n\\n## Test\\n{test}\\n\\nWhat is the execution result?\"\n    msgs = [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_msg},\n    ]\n    if target is not None:\n        msgs.append({\"role\": \"assistant\", \"content\": target})\n    return msgs\n\n\ndef _try_apply_chat_template(tokenizer, messages, tmpl_kw, **kwargs):\n    \"\"\"apply_chat_template with graceful fallback if system role is unsupported.\"\"\"\n    try:\n        return tokenizer.apply_chat_template(messages, **tmpl_kw, **kwargs)\n    except Exception:\n        # Some models don't support system role — merge system into first user message\n        merged = []\n        sys_content = \"\"\n        for m in messages:\n            if m[\"role\"] == \"system\":\n                sys_content = m[\"content\"]\n            elif m[\"role\"] == \"user\" and sys_content:\n                merged.append({\"role\": \"user\", \"content\": sys_content + \"\\n\\n\" + m[\"content\"]})\n                sys_content = \"\"\n            else:\n                merged.append(m)\n        return tokenizer.apply_chat_template(merged, **tmpl_kw, **kwargs)\n\n\ndef tokenize_example(tokenizer, code, test, target, max_len, tmpl_kw):\n    prompt_ids = _try_apply_chat_template(\n        tokenizer,\n        build_messages(code, test),\n        tmpl_kw,\n        tokenize=True,\n        add_generation_prompt=True,\n    )\n    full_ids = _try_apply_chat_template(\n        tokenizer,\n        build_messages(code, test, target),\n        tmpl_kw,\n        tokenize=True,\n        add_generation_prompt=False,\n    )\n\n    truncated = len(full_ids) > max_len\n    if truncated:\n        full_ids = full_ids[:max_len]\n\n    prompt_len = min(len(prompt_ids), len(full_ids))\n    labels = [-100] * prompt_len + full_ids[prompt_len:]\n\n    return {\n        \"input_ids\": full_ids,\n        \"labels\": labels,\n        \"attention_mask\": [1] * len(full_ids),\n    }, truncated\n\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef preprocess_split(tokenizer, data, max_len, name, tmpl_kw):\n    out = {\"input_ids\": [], \"labels\": [], \"attention_mask\": []}\n    n_trunc = 0\n    for ex in data:\n        tok, trunc = tokenize_example(\n            tokenizer, ex[\"code\"], ex[\"test\"], ex[\"target\"], max_len, tmpl_kw,\n        )\n        for k in out:\n            out[k].append(tok[k])\n        n_trunc += int(trunc)\n    pct = n_trunc / len(data) * 100 if data else 0\n    log.info(f\"{name}: {n_trunc}/{len(data)} truncated ({pct:.1f}%)\")\n    return Dataset.from_dict(out)\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    p = argparse.ArgumentParser(description=\"Unified LoRA CWM training (Qwen / DeepSeek / auto)\")\n    p.add_argument(\"--data_dir\", required=True)\n    p.add_argument(\"--model_name_or_path\", required=True, help=\"HF model id or local path\")\n    p.add_argument(\"--output_dir\", default=\"checkpoints_cwm/\")\n    p.add_argument(\"--wandb_project\", default=\"exec-sim-repair-verifier\")\n    p.add_argument(\"--run_name\", default=None, help=\"W&B run name (auto-generated if omitted)\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--max_seq_length\", type=int, default=2048)\n    p.add_argument(\"--batch_size\", type=int, default=2)\n    p.add_argument(\"--grad_accumulation\", type=int, default=16)\n    p.add_argument(\"--lr\", type=float, default=2e-4)\n    p.add_argument(\"--epochs\", type=int, default=3)\n    p.add_argument(\"--warmup_ratio\", type=float, default=0.1)\n    p.add_argument(\"--lora_rank\", type=int, default=16)\n    p.add_argument(\"--lora_alpha\", type=int, default=32)\n    p.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    p.add_argument(\"--max_steps\", type=int, default=-1)\n    p.add_argument(\"--no_wandb\", action=\"store_true\")\n    args = p.parse_args()\n\n    family = detect_model_family(args.model_name_or_path)\n    log.info(f\"Model: {args.model_name_or_path} → family={family}\")\n\n    if args.run_name is None:\n        # e.g. \"Qwen/Qwen3-8B\" → \"cwm-qwen3-8b-lora\"\n        short = args.model_name_or_path.split(\"/\")[-1].lower().replace(\"_\", \"-\")\n        args.run_name = f\"cwm-{short}-lora\"\n    log.info(f\"Run name: {args.run_name}\")\n\n    if args.no_wandb:\n        os.environ[\"WANDB_DISABLED\"] = \"true\"\n    else:\n        os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n\n    # ── Tokenizer ──\n    log.info(f\"Loading tokenizer: {args.model_name_or_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(\n        args.model_name_or_path, trust_remote_code=True, padding_side=\"right\",\n    )\n    setup_tokenizer(tokenizer, family)\n    tmpl_kw = get_chat_template_kwargs(family, tokenizer)\n    log.info(f\"Chat template kwargs: {tmpl_kw}\")\n\n    # Sanity check: render one example to verify template works\n    sample_text = _try_apply_chat_template(\n        tokenizer,\n        build_messages(\"def f(): return 1\", \"assert f() == 1\", \"PASS: test completed successfully\"),\n        tmpl_kw,\n        tokenize=False,\n        add_generation_prompt=False,\n    )\n    log.info(f\"Sample formatted prompt (first 300 chars):\\n{sample_text[:300]}\")\n\n    # ── Data ──\n    train_raw = load_jsonl(os.path.join(args.data_dir, \"cwm_train.jsonl\"))\n    val_raw = load_jsonl(os.path.join(args.data_dir, \"cwm_val.jsonl\"))\n    log.info(f\"Loaded train={len(train_raw)}, val={len(val_raw)}\")\n\n    train_ds = preprocess_split(tokenizer, train_raw, args.max_seq_length, \"train\", tmpl_kw)\n    val_ds = preprocess_split(tokenizer, val_raw, args.max_seq_length, \"val\", tmpl_kw)\n\n    # ── Model ──\n    log.info(f\"Loading model: {args.model_name_or_path}\")\n    try:\n        import flash_attn  # noqa: F401\n        attn_impl = \"flash_attention_2\"\n    except ImportError:\n        attn_impl = \"sdpa\"\n    log.info(f\"Attention: {attn_impl}\")\n\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name_or_path,\n        torch_dtype=torch.bfloat16,\n        trust_remote_code=True,\n        attn_implementation=attn_impl,\n    )\n    model.config.use_cache = False\n\n    # ── LoRA ──\n    target_modules = get_lora_target_modules(family)\n    log.info(f\"LoRA target modules: {target_modules}\")\n\n    lora_cfg = LoraConfig(\n        task_type=TaskType.CAUSAL_LM,\n        r=args.lora_rank,\n        lora_alpha=args.lora_alpha,\n        lora_dropout=args.lora_dropout,\n        target_modules=target_modules,\n    )\n    model = get_peft_model(model, lora_cfg)\n    model.enable_input_require_grads()\n    model.print_trainable_parameters()\n\n    # ── Training ──\n    collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)\n\n    is_dryrun = args.max_steps > 0\n    ta = {\n        \"output_dir\": args.output_dir,\n        \"num_train_epochs\": args.epochs,\n        \"max_steps\": args.max_steps,\n        \"per_device_train_batch_size\": args.batch_size,\n        \"per_device_eval_batch_size\": args.batch_size,\n        \"gradient_accumulation_steps\": args.grad_accumulation,\n        \"learning_rate\": args.lr,\n        \"warmup_ratio\": args.warmup_ratio,\n        \"bf16\": True,\n        \"logging_steps\": 1 if is_dryrun else 50,\n        \"eval_strategy\": \"no\" if is_dryrun else \"epoch\",\n        \"save_strategy\": \"no\" if is_dryrun else \"epoch\",\n        \"load_best_model_at_end\": not is_dryrun,\n        \"save_total_limit\": 2,\n        \"seed\": args.seed,\n        \"run_name\": args.run_name,\n        \"report_to\": \"none\" if args.no_wandb else \"wandb\",\n        \"gradient_checkpointing\": True,\n        \"dataloader_num_workers\": 4,\n    }\n    if not is_dryrun:\n        ta[\"metric_for_best_model\"] = \"eval_loss\"\n        ta[\"greater_is_better\"] = False\n    training_args = TrainingArguments(**ta)\n\n    trainer = Trainer(\n        model=model,\n        args=training_args,\n        train_dataset=train_ds,\n        eval_dataset=val_ds,\n        data_collator=collator,\n    )\n\n    log.info(\"Starting training...\")\n    trainer.train()\n\n    if not is_dryrun:\n        best_dir = os.path.join(args.output_dir, \"best\")\n        trainer.save_model(best_dir)\n        tokenizer.save_pretrained(best_dir)\n        log.info(f\"Best model saved to {best_dir}\")\n    else:\n        log.info(\"Dry-run complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T04:58:29.445937+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/train_unified.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_adapt-training-script_20260516T045559",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T04:58:29.446120+00:00_

文件写好了：`train_unified.py`

**新模型 DeepSeek-Coder-6.7B-Instruct 的关键差异和注意事项：**

| 差异点 | Qwen3 | DeepSeek-Coder-6.7B-Instruct |
|--------|-------|------|
| Chat template 格式 | ChatML (`<\|im_start\|>...<\|im_end\|>`) | `### Instruction:\n...\n### Response:\n` |
| 特殊参数 | `enable_thinking=False` | 无 |
| EOS token | `<\|im_end\|>` / `<\|endoftext\|>` | `<\|EOT\|>` |
| LoRA target modules | q/k/v/o_proj | 同（LLaMA架构） |
| context length | 32K | 16K |

**脚本设计要点：**
1. `detect_model_family()` 根据模型名自动选择配置
2. `get_chat_template_kwargs()` 只给 Qwen3 传 `enable_thinking=False`
3. `_try_apply_chat_template()` 兼容不支持 system role 的模型（自动 merge 到 user message）
4. tokenizer/pad_token 处理对两者都安全
5. 训练启动时打印一条格式化后的 sample prompt 用于人工验证模板是否正确

**eval 脚本（`eval_cwm_baseline.py`）也有 Qwen 特有逻辑**（`<|im_end|>` 作为 stop token），如果要用 DeepSeek 评估需要同样适配。需要的话我可以接着改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_adapt-training-script_20260516T045559"
}
```

</details>

---
