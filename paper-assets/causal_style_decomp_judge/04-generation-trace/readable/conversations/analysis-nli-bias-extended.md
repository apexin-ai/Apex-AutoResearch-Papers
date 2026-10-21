# analysis nli bias extended

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_nli-bias-extended_20260522T224735.jsonl`
- **Structured JSON:** [`e99b97064c8afb5583a2.json`](../../sessions/e9/e99b97064c8afb5583a2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-22T22:50:36.073170+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T22:50:36.073537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T22:50:36.073718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "ls /root/causal_style_decomp_judge/data/verified*.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "ls /root/causal_style_decomp_judge/data/verified*.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T22:50:36.073852+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "pip list 2>/dev/null | grep -iE \"spacy|sklearn|scikit\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "pip list 2>/dev/null | grep -iE \"spacy|sklearn|scikit\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T22:50:36.073990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -1 /root/causal_style_decomp_judge/data/verified_32b.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -1 /root/causal_style_decomp_judge/data/verified_32b.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T22:50:36.074140+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/causal_style_decomp_judge/data/verified.jsonl\\n/root/causal_style_decomp_judge/data/verified_32b.jsonl\\n/root/causal_style_decomp_judge/data/verified_alpacaeval.jsonl\\n/root/causal_style_decomp_judge/data/verified_alpacaeval_verbosity.jsonl\\n/root/causal_style_decomp_judge/data/verified_gpt4o_rewriter_formality.jsonl\\n/root/causal_style_decomp_judge/data/verified_gpt4o_rewriter_verbosity.jsonl\\n/root/causal_style_decomp_judge/data/verified_mtbench.jsonl\\n/root/causal_style_decomp_judge/data/verified_register.jsonl\\n/root/causal_style_decomp_judge/data/verified_register_pilot.jsonl\\n/root/causal_style_decomp_judge/data/verified_register_pilot_v2.jsonl\\n/root/causal_style_decomp_judge/data/verified_scaled_formality.jsonl\\n/root/causal_style_decomp_judge/data/verified_tone_pilot.jsonl\\n/root/causal_style_decomp_judge/data/verified_verbosity.jsonl\\n/root/causal_style_decomp_judge/data/verified_verbosity_filtered.jsonl\\n/root/causal_style_decomp_judge/data/verified_verbosity_v2.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T22:50:36.074278+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T22:50:36.074504+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"instruction\\\": \\\"Hey, what can you do for me?\\\", \\\"response\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physical sensations: I can't experience physical sensations or perceive the physical world.\\\\n\\\\nRemember, while I can assist you with various tasks, there are limitations to what I can do.\\\", \\\"source\\\": \\\"GPTInst\\\", \\\"label\\\": 2, \\\"id\\\": \\\"mvp_0000\\\", \\\"original_text\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physi
…[truncated 2693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T22:50:36.074686+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -1 /root/causal_style_decomp_judge/data/verified_verbosity.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -1 /root/causal_style_decomp_judge/data/verified_verbosity.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T22:50:36.074818+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "pip list 2>/dev/null | grep -i spacy",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "pip list 2>/dev/null | grep -i spacy",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T22:50:36.075031+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"instruction\\\": \\\"Hey, what can you do for me?\\\", \\\"response\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physical sensations: I can't experience physical sensations or perceive the physical world.\\\\n\\\\nRemember, while I can assist you with various tasks, there are limitations to what I can do.\\\", \\\"source\\\": \\\"GPTInst\\\", \\\"label\\\": 2, \\\"id\\\": \\\"mvp_0000\\\", \\\"original_text\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physi
…[truncated 5242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T22:50:36.075203+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T22:50:36.075388+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "head -1 /root/causal_style_decomp_judge/data/verified_scaled_formality.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "head -1 /root/causal_style_decomp_judge/data/verified_scaled_formality.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T22:50:36.075573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"mvp_0000\\\", \\\"instruction\\\": \\\"Hey, what can you do for me?\\\", \\\"response\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physical sensations: I can't experience physical sensations or perceive the physical world.\\\\n\\\\nRemember, while I can assist you with various tasks, there are limitations to what I can do.\\\", \\\"source\\\": \\\"GPTInst\\\", \\\"original_text\\\": \\\"As an AI assistant, there are a few things I can't do for you:\\\\n\\\\n1. Physical tasks: I can't perform any physical tasks for you, such as cleaning your house or running errands.\\\\n\\\\n2. Emotional support: I can't provide emotional support like a human can. If you need someone to talk to, it's best to reach out to a friend, family member, or a professional.\\\\n\\\\n3. Make decisions for you: It's important to consider multiple perspectives and make choices based on your own judgment.\\\\n\\\\n4. Access personal accounts: I don't have access to personal accounts or sensitive information unless you explicitly provide it to me. It's important to be cautious and avoid sharing any personal or sensitive information with me or any other AI assistant.\\\\n\\\\n5. Physical sensations: I 
…[truncated 2585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T22:50:36.075758+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-29275",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && python3 -c \"import spacy; print(spacy.__version__)\" 2>&1; python3 -c \"from sklearn.feature_extraction.text import TfidfVectorizer; print('sklearn OK')\" 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-29275",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 && python3 -c \"import spacy; print(spacy.__version__)\" 2>&1; python3 -c \"from sklearn.feature_extraction.text import TfidfVectorizer; print('sklearn OK')\" 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T22:50:36.075902+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 1, in &lt;module>\\nModuleNotFoundError: No module named 'spacy'\\nsklearn OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T22:50:36.076060+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-29275",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && pip install spacy -q 2>&1 | tail -3 && python -m spacy download en_core_web_sm 2>&1 | tail -3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-29275",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && pip install spacy -q 2>&1 | tail -3 && python -m spacy download en_core_web_sm 2>&1 | tail -3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T22:50:36.076198+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && pip install spacy -q 2>&1 | tail -3 && python -m spacy download en_core_web_sm 2>&1 | tail -3'\\n\\nStdout:\\n\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 31.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T22:50:36.076388+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-29275",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && nohup bash -c 'pip install spacy -q 2>&1 && python -m spacy download en_core_web_sm 2>&1' > /tmp/spacy_install.log 2>&1 & echo $!",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-29275",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && nohup bash -c 'pip install spacy -q 2>&1 && python -m spacy download en_core_web_sm 2>&1' > /tmp/spacy_install.log 2>&1 & echo $!",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T22:50:36.076540+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"261757\\n设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 14.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T22:50:36.076664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-29275",
  "command": "tail -5 /tmp/spacy_install.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-29275",
    "command": "tail -5 /tmp/spacy_install.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T22:50:36.076806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Collecting en-core-web-sm==3.8.0\\n  Using cached https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl (12.8 MB)\\nWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\\n\\u001b[38;5;2m✔ Download and installation successful\\u001b[0m\\nYou can now load the package via spacy.load('en_core_web_sm')\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T22:50:36.076987+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-29275",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/causal_style_decomp_judge/artifacts/r14_fixes && cat > /tmp/nli_bias_extended.py << 'PYEOF'\nimport json, re, numpy as np\nfrom collections import Counter\nfrom scipy import stats\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.cluster import KMeans\nimport spacy\n\nnlp = spacy.load(\"en_core_web_sm\")\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(l) for l in f if l.strip()]\n\ndef split_pass_reject(data, threshold=0.90):\n    p = [d for d in data if d[\"nli_cf\"] >= threshold]\n    r = [d for d in data if d[\"nli_cf\"] < threshold]\n    return p, r\n\ndef tokenize_simple(text):\n    return text.split()\n\ndef sentence_split(text):\n    return [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]\n\ndef analyze_axis(data, axis_name, all_results):\n    passed, rejected = split_pass_reject(data)\n    n_pass, n_reject = len(passed), len(rejected)\n    print(f\"\\n{'='*60}\")\n    print(f\"Axis: {axis_name} | pass={n_pass}, reject={n_reject}\")\n    print(f\"{'='*60}\")\n\n    # Use original_text for text analysis\n    pass_texts = [d[\"original_text\"] for d in passed]\n    reject_texts = [d[\"original_text\"] for d in rejected]\n    all_texts = pass_texts + reject_texts\n    all_labels = [1]*n_pass + [0]*n_reject  # 1=pass, 0=reject\n\n    # (a) Topic clustering via TF-IDF + KMeans on instructions\n    pass_instr = [d[\"instruction\"] for d in passed]\n    reject_instr = [d[\"instruction\"] for d in rejected]\n    all_instr = pass_instr + reject_instr\n\n    vectorizer = TfidfVectorizer(max_features=500, stop_words='english', min_df=2)\n    try:\n        X = vectorizer.fit_transform(all_instr)\n        k = min(6, max(2, len(all_instr)//10))\n        km = KMeans(n_clusters=k, random_state=42, n_init=10)\n        clusters = km.fit_predict(X)\n\n        # Distribution per cluster\n        pass_clusters = clusters[:n_pass]\n        reject_clusters = clusters[n_pass:]\n\n        cluster_dist = {}\n        contingency = np.zeros((2, k), dtype=int)\n        for c in range(k):\n            pc = int(np.sum(pass_clusters == c))\n            rc = int(np.sum(reject_clusters == c))\n            contingency[0, c] = pc\n            contingency[1, c] = rc\n            # Get top terms for this cluster\n            center = km.cluster_centers_[c]\n            top_idx = center.argsort()[-5:][::-1]\n            top_terms = [vectorizer.get_feature_names_out()[i] for i in top_idx]\n            cluster_dist[f\"cluster_{c}\"] = {\"pass\": pc, \"reject\": rc, \"top_terms\": top_terms}\n\n        # Remove zero columns for chi2\n        nonzero = contingency.sum(axis=0) > 0\n        if nonzero.sum() >= 2:\n            chi2_stat, chi2_p, _, _ = stats.chi2_contingency(contingency[:, nonzero])\n        else:\n            chi2_stat, chi2_p = 0.0, 1.0\n\n        topic_result = {\n            \"method\": f\"TF-IDF + KMeans (k={k})\",\n            \"chi2\": round(chi2_stat, 4),\n            \"p\": round(chi2_p, 6),\n            \"clusters\": cluster_dist\n        }\n    except Exception as e:\n        topic_result = {\"method\": \"failed\", \"error\": str(e), \"chi2\": None, \"p\": None, \"clusters\": {}}\n\n    print(f\"\\n--- Topic Clustering ---\")\n    print(f\"Method: {topic_result['method']}\")\n    print(f\"Chi2={topic_result['chi2']}, p={topic_result['p']}\")\n    for cn, cv in topic_result.get(\"clusters\", {}).items():\n        print(f\"  {cn}: pass={cv['pass']}, reject={cv['reject']}, terms={cv['top_terms']}\")\n\n    # (b) Text statistics\n    pass_tok = [len(tokenize_simple(t)) for t in pass_texts]\n    reject_tok = [len(tokenize_simple(t)) for t in reject_texts]\n\n    ks_stat, ks_p = stats.ks_2samp(pass_tok, reject_tok) if reject_tok else (0, 1)\n\n    pass_sents = [sentence_split(t) for t in pass_texts]\n    reject_sents = [sentence_split(t) for t in reject_texts]\n\n    pass_avg_sent_len = [np.mean([len(tokenize_simple(s)) for s in ss]) if ss else 0 for ss in pass_sents]\n    reject_avg_sent_len = [np.mean([len(tokenize_simple(s)) for s in ss]) if ss else 0 for ss in reject_sents]\n\n    mwu_stat, mwu_p = stats.mannwhitneyu(pass_avg_sent_len, reject_avg_sent_len, alternative='two-sided') if reject_avg_sent_len else (0, 1)\n\n    pass_sent_count = [len(ss) for ss in pass_sents]\n    reject_sent_count = [len(ss) for ss in reject_sents]\n    mwu_sc_stat, mwu_sc_p = stats.mannwhitneyu(pass_sent_count, reject_sent_count, alternative='two-sided') if reject_sent_count else (0, 1)\n\n    token_result = {\n        \"pass_mean\": round(np.mean(pass_tok), 2),\n        \"pass_std\": round(np.std(pass_tok), 2),\n        \"reject_mean\": round(np.mean(reject_tok), 2) if reject_tok else None,\n        \"reject_std\": round(np.std(reject_tok), 2) if reject_tok else None,\n        \"ks_stat\": round(ks_stat, 4),\n        \"ks_p\": round(ks_p, 6)\n    }\n\n    sent_len_result = {\n        \"pass_mean\": round(np.mean(pass_avg_sent_len), 2),\n        \"reject_mean\": round(np.mean(reject_avg_sent_len), 2) if reject_avg_sent_len else None,\n        \"mwu_stat\": round(float(mwu_stat), 2),\n        \"mwu_p\": round(float(mwu_p), 6)\n    }\n\n    sent_count_result = {\n        \"pass_mean\": round(np.mean(pass_sent_count), 2),\n        \"reject_mean\": round(np.mean(reject_sent_count), 2) if reject_sent_count else None,\n        \"mwu_stat\": round(float(mwu_sc_stat), 2),\n        \"mwu_p\": round(float(mwu_sc_p), 6)\n    }\n\n    print(f\"\\n--- Token Count ---\")\n    print(f\"Pass: {token_result['pass_mean']}±{token_result['pass_std']}, Reject: {token_result['reject_mean']}±{token_result['reject_std']}\")\n    print(f\"KS stat={token_result['ks_stat']}, p={token_result['ks_p']}\")\n\n    print(f\"\\n--- Avg Sentence Length ---\")\n    print(f\"Pass: {sent_len_result['pass_mean']}, Reject: {sent_len_result['reject_mean']}\")\n    print(f\"MWU stat={sent_len_result['mwu_stat']}, p={sent_len_result['mwu_p']}\")\n\n    print(f\"\\n--- Sentence Count ---\")\n    print(f\"Pass: {sent_count_result['pass_mean']}, Reject: {sent_count_result['reject_mean']}\")\n    print(f\"MWU stat={sent_count_result['mwu_stat']}, p={sent_count_result['mwu_p']}\")\n\n    # (c) Syntactic complexity via spaCy dependency tree depth\n    def get_tree_depth(doc):\n        def _depth(token):\n            if not list(token.children):\n                return 0\n            return 1 + max(_depth(c) for c in token.children)\n        depths = []\n        for sent in doc.sents:\n            depths.append(_depth(sent.root))\n        return depths\n\n    print(f\"\\n--- Syntactic Complexity (spaCy dep tree depth) ---\")\n    # Process in batches for efficiency; limit text length to avoid OOM\n    MAX_CHARS = 3000\n    pass_depths_all = []\n    for doc in nlp.pipe([t[:MAX_CHARS] for t in pass_texts], batch_size=16):\n        depths = get_tree_depth(doc)\n        if depths:\n            pass_depths_all.append(np.mean(depths))\n\n    reject_depths_all = []\n    for doc in nlp.pipe([t[:MAX_CHARS] for t in reject_texts], batch_size=16):\n        depths = get_tree_depth(doc)\n        if depths:\n            reject_depths_all.append(np.mean(depths))\n\n    if reject_depths_all:\n        syn_mwu_stat, syn_mwu_p = stats.mannwhitneyu(pass_depths_all, reject_depths_all, alternative='two-sided')\n    else:\n        syn_mwu_stat, syn_mwu_p = 0, 1\n\n    syntax_result = {\n        \"metric\": \"mean_dep_tree_depth\",\n        \"pass_mean\": round(np.mean(pass_depths_all), 3) if pass_depths_all else None,\n        \"pass_std\": round(np.std(pass_depths_all), 3) if pass_depths_all else None,\n        \"reject_mean\": round(np.mean(reject_depths_all), 3) if reject_depths_all else None,\n        \"reject_std\": round(np.std(reject_depths_all), 3) if reject_depths_all else None,\n        \"test\": \"Mann-Whitney U\",\n        \"stat\": round(float(syn_mwu_stat), 2),\n        \"p\": round(float(syn_mwu_p), 6)\n    }\n\n    print(f\"Pass depth: {syntax_result['pass_mean']}±{syntax_result['pass_std']}\")\n    print(f\"Reject depth: {syntax_result['reject_mean']}±{syntax_result['reject_std']}\")\n    print(f\"MWU stat={syntax_result['stat']}, p={syntax_result['p']}\")\n\n    result = {\n        \"axis\": axis_name,\n        \"n_pass\": n_pass,\n        \"n_reject\": n_reject,\n        \"topic_clustering\": topic_result,\n        \"token_count\": token_result,\n        \"sentence_length\": sent_len_result,\n        \"sentence_count\": sent_count_result,\n        \"syntactic_complexity\": syntax_result\n    }\n    all_results.append(result)\n    return result\n\n# Load data\nform_data = load_jsonl(\"/root/causal_style_decomp_judge/data/verified_32b.jsonl\")\nverb_data = load_jsonl(\"/root/causal_style_decomp_judge/data/verified_verbosity.jsonl\")\nscaled_form = load_jsonl(\"/root/causal_style_decomp_judge/data/verified_scaled_formality.jsonl\")\n\nprint(f\"Loaded: formality={len(form_data)}, verbosity={len(verb_data)}, scaled_formality={len(scaled_form)}\")\n\nall_results = []\nanalyze_axis(form_data, \"formality\", all_results)\nanalyze_axis(verb_data, \"verbosity\", all_results)\nanalyze_axis(scaled_form, \"scaled_formality\", all_results)\n\n# Save\nout_path = \"/root/causal_style_decomp_judge/artifacts/r14_fixes/nli_selection_bias_extended.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(all_results, f, indent=2, ensure_ascii=False)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\npython3 /tmp/nli_bias_extended.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-29275",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/causal_style_decomp_judge/artifacts/r14_fixes && cat > /tmp/nli_bias_extended.py << 'PYEOF'\nimport json, re, numpy as np\nfrom collections import Counter\nfrom scipy import stats\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.cluster import KMeans\nimport spacy\n\nnlp = spacy.load(\"en_core_web_sm\")\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(l) for l in f if l.strip()]\n\ndef split_pass_reject(data, threshold=0.90):\n    p = [d for d in data if d[\"nli_cf\"] >= threshold]\n    r = [d for d in data if d[\"nli_cf\"] < threshold]\n    return p, r\n\ndef tokenize_simple(text):\n    return text.split()\n\ndef sentence_split(text):\n    return [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]\n\ndef analyze_axis(data, axis_name, all_results):\n    passed, rejected = split_pass_reject(data)\n    n_pass, n_reject = len(passed), len(rejected)\n    print(f\"\\n{'='*60}\")\n    print(f\"Axis: {axis_name} | pass={n_pass}, reject={n_reject}\")\n    print(f\"{'='*60}\")\n\n    # Use original_text for text analysis\n    pass_texts = [d[\"original_text\"] for d in passed]\n    reject_texts = [d[\"original_text\"] for d in rejected]\n    all_texts = pass_texts + reject_texts\n    all_labels = [1]*n_pass + [0]*n_reject  # 1=pass, 0=reject\n\n    # (a) Topic clustering via TF-IDF + KMeans on instructions\n    pass_instr = [d[\"instruction\"] for d in passed]\n    reject_instr = [d[\"instruction\"] for d in rejected]\n    all_instr = pass_instr + reject_instr\n\n    vectorizer = TfidfVectorizer(max_features=500, stop_words='english', min_df=2)\n    try:\n        X = vectorizer.fit_transform(all_instr)\n        k = min(6, max(2, len(all_instr)//10))\n        km = KMeans(n_clusters=k, random_state=42, n_init=10)\n        clusters = km.fit_predict(X)\n\n        # Distribution per cluster\n        pass_clusters = clusters[:n_pass]\n        reject_clusters = clusters[n_pass:]\n\n        cluster_dist = {}\n        contingency = np.zeros((2, k), dtype=int)\n        for c in range(k):\n            pc = int(np.sum(pass_clusters == c))\n            rc = int(np.sum(reject_clusters == c))\n            contingency[0, c] = pc\n            contingency[1, c] = rc\n            # Get top terms for this cluster\n            center = km.cluster_centers_[c]\n            top_idx = center.argsort()[-5:][::-1]\n            top_terms = [vectorizer.get_feature_names_out()[i] for i in top_idx]\n            cluster_dist[f\"cluster_{c}\"] = {\"pass\": pc, \"reject\": rc, \"top_terms\": top_terms}\n\n        # Remove zero columns for chi2\n        nonzero = contingency.sum(axis=0) > 0\n        if nonzero.sum() >= 2:\n            chi2_stat, chi2_p, _, _ = stats.chi2_contingency(contingency[:, nonzero])\n        else:\n            chi2_stat, chi2_p = 0.0, 1.0\n\n        topic_result = {\n            \"method\": f\"TF-IDF + KMeans (k={k})\",\n            \"chi2\": round(chi2_stat, 4),\n            \"p\": round(chi2_p, 6),\n            \"clusters\": cluster_dist\n        }\n    except Exception as e:\n        topic_result = {\"method\": \"failed\", \"error\": str(e), \"chi2\": None, \"p\": None, \"clusters\": {}}\n\n    print(f\"\\n--- Topic Clustering ---\")\n    print(f\"Method: {topic_result['method']}\")\n    print(f\"Chi2={topic_result['chi2']}, p={topic_result['p']}\")\n    for cn, cv in topic_result.get(\"clusters\", {}).items():\n        print(f\"  {cn}: pass={cv['pass']}, reject={cv['reject']}, terms={cv['top_terms']}\")\n\n    # (b) Text statistics\n    pass_tok = [len(tokenize_simple(t)) for t in pass_texts]\n    reject_tok = [len(tokenize_simple(t)) for t in reject_texts]\n\n    ks_stat, ks_p = stats.ks_2samp(pass_tok, reject_tok) if reject_tok else (0, 1)\n\n    pass_sents = [sentence_split(t) for t in pass_texts]\n    reject_sents = [sentence_split(t) for t in reject_texts]\n\n    pass_avg_sent_len = [np.mean([len(tokenize_simple(s)) for s in ss]) if ss else 0 for ss in pass_sents]\n    reject_avg_sent_len = [np.mean([len(tokenize_simple(s)) for s in ss]) if ss else 0 for ss in reject_sents]\n\n    mwu_stat, mwu_p = stats.mannwhitneyu(pass_avg_sent_len, reject_avg_sent_len, alternative='two-sided') if reject_avg_sent_len else (0, 1)\n\n    pass_sent_count = [len(ss) for ss in pass_sents]\n    reject_sent_count = [len(ss) for ss in reject_sents]\n    mwu_sc_stat, mwu_sc_p = stats.mannwhitneyu(pass_sent_count, reject_sent_count, alternative='two-sided') if reject_sent_count else (0, 1)\n\n    token_result = {\n        \"pass_mean\": round(np.mean(pass_tok), 2),\n        \"pass_std\": round(np.std(pass_tok), 2),\n        \"reject_mean\": round(np.mean(reject_tok), 2) if reject_tok else None,\n        \"reject_std\": round(np.std(reject_tok), 2) if reject_tok else None,\n        \"ks_stat\": round(ks_stat, 4),\n        \"ks_p\": round(ks_p, 6)\n    }\n\n    sent_len_result = {\n        \"pass_mean\": round(np.mean(pass_avg_sent_len), 2),\n        \"reject_mean\": round(np.mean(reject_avg_sent_len), 2) if reject_avg_sent_len else None,\n        \"mwu_stat\": round(float(mwu_stat), 2),\n        \"mwu_p\": round(float(mwu_p), 6)\n    }\n\n    sent_count_result = {\n        \"pass_mean\": round(np.mean(pass_sent_count), 2),\n        \"reject_mean\": round(np.mean(reject_sent_count), 2) if reject_sent_count else None,\n        \"mwu_stat\": round(float(mwu_sc_stat), 2),\n        \"mwu_p\": round(float(mwu_sc_p), 6)\n    }\n\n    print(f\"\\n--- Token Count ---\")\n    print(f\"Pass: {token_result['pass_mean']}±{token_result['pass_std']}, Reject: {token_result['reject_mean']}±{token_result['reject_std']}\")\n    print(f\"KS stat={token_result['ks_stat']}, p={token_result['ks_p']}\")\n\n    print(f\"\\n--- Avg Sentence Length ---\")\n    print(f\"Pass: {sent_len_result['pass_mean']}, Reject: {sent_len_result['reject_mean']}\")\n    print(f\"MWU stat={sent_len_result['mwu_stat']}, p={sent_len_result['mwu_p']}\")\n\n    print(f\"\\n--- Sentence Count ---\")\n    print(f\"Pass: {sent_count_result['pass_mean']}, Reject: {sent_count_result['reject_mean']}\")\n    print(f\"MWU stat={sent_count_result['mwu_stat']}, p={sent_count_result['mwu_p']}\")\n\n    # (c) Syntactic complexity via spaCy dependency tree depth\n    def get_tree_depth(doc):\n        def _depth(token):\n            if not list(token.children):\n                return 0\n            return 1 + max(_depth(c) for c in token.children)\n        depths = []\n        for sent in doc.sents:\n            depths.append(_depth(sent.root))\n        return depths\n\n    print(f\"\\n--- Syntactic Complexity (spaCy dep tree depth) ---\")\n    # Process in batches for efficiency; limit text length to avoid OOM\n    MAX_CHARS = 3000\n    pass_depths_all = []\n    for doc in nlp.pipe([t[:MAX_CHARS] for t in pass_texts], batch_size=16):\n        depths = get_tree_depth(doc)\n        if depths:\n            pass_depths_all.append(np.mean(depths))\n\n    reject_depths_all = []\n    for doc in nlp.pipe([t[:MAX_CHARS] for t in reject_texts], batch_size=16):\n        depths = get_tree_depth(doc)\n        if depths:\n            reject_depths_all.append(np.mean(depths))\n\n    if reject_depths_all:\n        syn_mwu_stat, syn_mwu_p = stats.mannwhitneyu(pass_depths_all, reject_depths_all, alternative='two-sided')\n    else:\n        syn_mwu_stat, syn_mwu_p = 0, 1\n\n    syntax_result = {\n        \"metric\": \"mean_dep_tree_depth\",\n        \"pass_mean\": round(np.mean(pass_depths_all), 3) if pass_depths_all else None,\n        \"pass_std\": round(np.std(pass_depths_all), 3) if pass_depths_all else None,\n        \"reject_mean\": round(np.mean(reject_depths_all), 3) if reject_depths_all else None,\n        \"reject_std\": round(np.std(reject_depths_all), 3) if reject_depths_all else None,\n        \"test\": \"Mann-Whitney U\",\n        \"stat\": round(float(syn_mwu_stat), 2),\n        \"p\": round(float(syn_mwu_p), 6)\n    }\n\n    print(f\"Pass depth: {syntax_result['pass_mean']}±{syntax_result['pass_std']}\")\n    print(f\"Reject depth: {syntax_result['reject_mean']}±{syntax_result['reject_std']}\")\n    print(f\"MWU stat={syntax_result['stat']}, p={syntax_result['p']}\")\n\n    result = {\n        \"axis\": axis_name,\n        \"n_pass\": n_pass,\n        \"n_reject\": n_reject,\n        \"topic_clustering\": topic_result,\n        \"token_count\": token_result,\n        \"sentence_length\": sent_len_result,\n        \"sentence_count\": sent_count_result,\n        \"syntactic_complexity\": syntax_result\n    }\n    all_results.append(result)\n    return result\n\n# Load data\nform_data = load_jsonl(\"/root/causal_style_decomp_judge/data/verified_32b.jsonl\")\nverb_data = load_jsonl(\"/root/causal_style_decomp_judge/data/verified_verbosity.jsonl\")\nscaled_form = load_jsonl(\"/root/causal_style_decomp_judge/data/verified_scaled_formality.jsonl\")\n\nprint(f\"Loaded: formality={len(form_data)}, verbosity={len(verb_data)}, scaled_formality={len(scaled_form)}\")\n\nall_results = []\nanalyze_axis(form_data, \"formality\", all_results)\nanalyze_axis(verb_data, \"verbosity\", all_results)\nanalyze_axis(scaled_form, \"scaled_formality\", all_results)\n\n# Save\nout_path = \"/root/causal_style_decomp_judge/artifacts/r14_fixes/nli_selection_bias_extended.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(all_results, f, indent=2, ensure_ascii=False)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\npython3 /tmp/nli_bias_extended.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T22:50:36.077244+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded: formality=100, verbosity=100, scaled_formality=355\\n\\n============================================================\\nAxis: formality | pass=88, reject=12\\n============================================================\\n\\n--- Topic Clustering ---\\nMethod: TF-IDF + KMeans (k=6)\\nChi2=4.0564, p=0.541321\\n  cluster_0: pass=10, reject=2, terms=['write', 'impressive', 'language', 'prompted', 'just']\\n  cluster_1: pass=6, reject=0, terms=['story', 'creative', 'choose', 'adventure', 'words']\\n  cluster_2: pass=8, reject=2, terms=['create', 'word', 'given', 'password', 'make']\\n  cluster_3: pass=5, reject=2, terms=['following', 'healthy', 'food', 'burgers', 'unhealthy']\\n  cluster_4: pass=52, reject=5, terms=['ways', 'question', 'date', 'come', 'new']\\n  cluster_5: pass=7, reject=1, terms=['sentence', 'school', 'identify', 'data', 'gdpr']\\n\\n--- Token Count ---\\nPass: 104.68±128.16, Reject: 101.67±174.23\\nKS stat=0.2689, p=0.3656\\n\\n--- Avg Sentence Length ---\\nPass: 13.09, Reject: 13.47\\nMWU stat=480.0, p=0.614288\\n\\n--- Sentence Count ---\\nPass: 7.68, Reject: 5.83\\nMWU stat=658.5, p=0.163128\\n\\n--- Syntactic Complexity (spaCy dep tree depth) ---\\nPass depth: 4.591±1.711\\nReject depth: 5.102±2.548\\nMWU stat=483.0, p=0.636569\\n\\n============================================================\\nAxis: verbosity | pass=86, reject=14\\n============================================================\\n\\n--- Topic Clustering ---\\nMethod: TF-IDF + KMeans (k=6)\\nChi2=7.8469, p=0.16488\\n  cluster_0: pass=50, reject=10, terms=['create', 'ways', 'come', 'date', 'reduce']\\n  cluster_1: pass=5, reject=2, terms=['following', 'healthy', 'food', 'burgers', 'unhealthy']\\n  cluster_2: pass=9, reject=0, terms=['possible', 'data', 'sentence', 'identify', 'way']\\n  cluster_3: pass=7, reject=0, terms=['story', 'creative', 'create', 'make', 'choose']\\n  cluster_4: pass=11, reject=0, terms=['write', 'imp
…[truncated 1361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-bias-extended_20260522T224735",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-22T22:50:36.077516+00:00_

Analysis complete. Results:

## Results Summary

### Formality (88 pass / 12 reject) — No Bias Detected

| Dimension | Pass | Reject | Test | p-value |
|---|---|---|---|---|
| Topic distribution | — | — | χ²=4.06 | 0.541 |
| Token count | 104.7±128.2 | 101.7±174.2 | KS=0.269 | 0.366 |
| Avg sentence length | 13.1 | 13.5 | MWU | 0.614 |
| Sentence count | 7.7 | 5.8 | MWU | 0.163 |
| Dep tree depth | 4.59±1.71 | 5.10±2.55 | MWU | 0.637 |

All dimensions non-significant. NLI gate on formality data is unbiased across these axes.

### Verbosity (86 pass / 14 reject) — Significant Bias on Length

| Dimension | Pass | Reject | Test | p-value |
|---|---|---|---|---|
| Topic distribution | — | — | χ²=7.85 | 0.165 |
| **Token count** | **109.5±133.8** | **72.3±134.4** | **KS=0.503** | **0.003** |
| **Avg sentence length** | **13.8** | **9.0** | **MWU** | **0.006** |
| Sentence count | 7.8 | 5.4 | MWU | 0.050 |
| Dep tree depth | 4.73±1.68 | 4.21±2.58 | MWU | 0.110 |

Verbosity NLI gate shows **significant selection bias**: rejected samples are systematically shorter (72 vs 110 tokens, p=0.003) with shorter sentences (9.0 vs 13.8 words, p=0.006). This is expected — concise originals undergoing verbosity expansion produce CF texts that are structurally very different, making NLI entailment harder to satisfy.

### Scaled Formality (355 pass / 0 reject)

All 355 pairs pass NLI ≥ 0.90. No reject group to compare.

**Output**: `/root/causal_style_decomp_judge/artifacts/r14_fixes/nli_selection_bias_extended.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_nli-bias-extended_20260522T224735"
}
```

</details>

---
