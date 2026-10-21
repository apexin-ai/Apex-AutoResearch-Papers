# research first token masking

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_research_first_token_masking_20260513T193339.jsonl`
- **Structured JSON:** [`be83a63fb023f32ab9f6.json`](../../sessions/be/be83a63fb023f32ab9f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-13T19:34:58.259245+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T19:34:58.259735+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T19:34:58.259962+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== SciERC Entity Types ===')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\nfirst_tokens = {}\nfor t in scierc_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\\"{first_decoded}\\\"')\n    if first_id in first_tokens:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\\"{first_decoded}\\\") with {first_tokens[first_id]}')\n    first_tokens[first_id] = t\n\nprint()\nif len(first_tokens) == len(scierc_types):\n    print('SciERC: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('SciERC: First token COLLISIONS detected -- need trie-based approach')\n\nprint()\nprint('=== DocRED Entity Types ===')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfirst_tokens_docred = {}\nfor t in docred_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\\"{first_decoded}\\\"')\n    if first_id in first_tokens_docred:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\\"{first_decoded}\\\") with {first_tokens_docred[first_id]}')\n    first_tokens_docred[first_id] = t\n\nprint()\nif len(first_tokens_docred) == len(docred_types):\n    print('DocRED: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('DocRED: First token COLLISIONS detected -- need trie-based approach')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "account": "root",
    "command": "python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== SciERC Entity Types ===')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\nfirst_tokens = {}\nfor t in scierc_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\\"{first_decoded}\\\"')\n    if first_id in first_tokens:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\\"{first_decoded}\\\") with {first_tokens[first_id]}')\n    first_tokens[first_id] = t\n\nprint()\nif len(first_tokens) == len(scierc_types):\n    print('SciERC: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('SciERC: First token COLLISIONS detected -- need trie-based approach')\n\nprint()\nprint('=== DocRED Entity Types ===')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfirst_tokens_docred = {}\nfor t in docred_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\\"{first_decoded}\\\"')\n    if first_id in first_tokens_docred:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\\"{first_decoded}\\\") with {first_tokens_docred[first_id]}')\n    first_tokens_docred[first_id] = t\n\nprint()\nif len(first_tokens_docred) == len(docred_types):\n    print('DocRED: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('DocRED: First token COLLISIONS detected -- need trie-based approach')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T19:34:58.260121+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python3: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T19:34:58.260284+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "ls /root/miniconda3/bin/python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "account": "root",
    "command": "ls /root/miniconda3/bin/python3"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T19:34:58.260432+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T19:34:58.260596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "/root/miniconda3/bin/python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== SciERC Entity Types ===')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\nfirst_tokens = {}\nfor t in scierc_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\x22{first_decoded}\\x22')\n    if first_id in first_tokens:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\x22{first_decoded}\\x22) with {first_tokens[first_id]}')\n    first_tokens[first_id] = t\n\nprint()\nif len(first_tokens) == len(scierc_types):\n    print('SciERC: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('SciERC: First token COLLISIONS detected -- need trie-based approach')\n\nprint()\nprint('=== DocRED Entity Types ===')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfirst_tokens_docred = {}\nfor t in docred_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\x22{first_decoded}\\x22')\n    if first_id in first_tokens_docred:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\x22{first_decoded}\\x22) with {first_tokens_docred[first_id]}')\n    first_tokens_docred[first_id] = t\n\nprint()\nif len(first_tokens_docred) == len(docred_types):\n    print('DocRED: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('DocRED: First token COLLISIONS detected -- need trie-based approach')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "account": "root",
    "command": "/root/miniconda3/bin/python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== SciERC Entity Types ===')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\nfirst_tokens = {}\nfor t in scierc_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\x22{first_decoded}\\x22')\n    if first_id in first_tokens:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\x22{first_decoded}\\x22) with {first_tokens[first_id]}')\n    first_tokens[first_id] = t\n\nprint()\nif len(first_tokens) == len(scierc_types):\n    print('SciERC: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('SciERC: First token COLLISIONS detected -- need trie-based approach')\n\nprint()\nprint('=== DocRED Entity Types ===')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfirst_tokens_docred = {}\nfor t in docred_types:\n    ids = tokenizer.encode(t, add_special_tokens=False)\n    decoded = [tokenizer.decode([i]) for i in ids]\n    first_id = ids[0]\n    first_decoded = decoded[0]\n    print(f'{t}: ids={ids}, decoded={decoded}, first_token_id={first_id}, first_token=\\x22{first_decoded}\\x22')\n    if first_id in first_tokens_docred:\n        print(f'  COLLISION: {t} shares first token {first_id} (\\x22{first_decoded}\\x22) with {first_tokens_docred[first_id]}')\n    first_tokens_docred[first_id] = t\n\nprint()\nif len(first_tokens_docred) == len(docred_types):\n    print('DocRED: All first tokens unique -- first-token masking is SAFE')\nelse:\n    print('DocRED: First token COLLISIONS detected -- need trie-based approach')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T19:34:58.260793+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== SciERC Entity Types ===\\nTask: ids=[6262], decoded=['Task'], first_token_id=6262, first_token=\\\"Task\\\"\\nMethod: ids=[3523], decoded=['Method'], first_token_id=3523, first_token=\\\"Method\\\"\\nMaterial: ids=[13415], decoded=['Material'], first_token_id=13415, first_token=\\\"Material\\\"\\nMetric: ids=[54310], decoded=['Metric'], first_token_id=54310, first_token=\\\"Metric\\\"\\nOtherScientificTerm: ids=[11409, 50565, 1086, 17249], decoded=['Other', 'Scient', 'ific', 'Term'], first_token_id=11409, first_token=\\\"Other\\\"\\nGeneric: ids=[19964], decoded=['Generic'], first_token_id=19964, first_token=\\\"Generic\\\"\\n\\nSciERC: All first tokens unique -- first-token masking is SAFE\\n\\n=== DocRED Entity Types ===\\nPER: ids=[9654], decoded=['PER'], first_token_id=9654, first_token=\\\"PER\\\"\\nORG: ids=[44927], decoded=['ORG'], first_token_id=44927, first_token=\\\"ORG\\\"\\nLOC: ids=[12052], decoded=['LOC'], first_token_id=12052, first_token=\\\"LOC\\\"\\nTIME: ids=[18129], decoded=['TIME'], first_token_id=18129, first_token=\\\"TIME\\\"\\nNUM: ids=[17488], decoded=['NUM'], first_token_id=17488, first_token=\\\"NUM\\\"\\nMISC: ids=[44, 27629], decoded=['M', 'ISC'], first_token_id=44, first_token=\\\"M\\\"\\n\\nDocRED: All first tokens unique -- first-token masking is SAFE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T19:34:58.260971+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "/root/miniconda3/bin/python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== Context-dependent tokenization test ===')\nprint('Testing tokenization in JSON context (after quote):')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\ncontext = '\\x22type\\x22: \\x22'\ncontext_ids = tokenizer.encode(context, add_special_tokens=False)\nprint(f'Context \\x22{context}\\x22 -> ids={context_ids}')\nprint()\n\nfor t in scierc_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print(f'  {t}: bare={bare_ids}, in_context={type_ids}, {match}')\n\nprint()\nprint('DocRED types:')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfor t in docred_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print(f'  {t}: bare={bare_ids}, in_context={type_ids}, {match}')\n\nprint()\nprint('=== Testing with closing quote ===')\nfor t in scierc_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t + '\\x22'\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):-1]\n    first_bare = bare_ids[0]\n    first_ctx = type_ids[0] if type_ids else -1\n    match = 'SAME' if first_bare == first_ctx else 'DIFFERENT'\n    print(f'  {t}: bare_first={first_bare}, ctx_first={first_ctx}, {match}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "account": "root",
    "command": "/root/miniconda3/bin/python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== Context-dependent tokenization test ===')\nprint('Testing tokenization in JSON context (after quote):')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\ncontext = '\\x22type\\x22: \\x22'\ncontext_ids = tokenizer.encode(context, add_special_tokens=False)\nprint(f'Context \\x22{context}\\x22 -> ids={context_ids}')\nprint()\n\nfor t in scierc_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print(f'  {t}: bare={bare_ids}, in_context={type_ids}, {match}')\n\nprint()\nprint('DocRED types:')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfor t in docred_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print(f'  {t}: bare={bare_ids}, in_context={type_ids}, {match}')\n\nprint()\nprint('=== Testing with closing quote ===')\nfor t in scierc_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t + '\\x22'\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):-1]\n    first_bare = bare_ids[0]\n    first_ctx = type_ids[0] if type_ids else -1\n    match = 'SAME' if first_bare == first_ctx else 'DIFFERENT'\n    print(f'  {t}: bare_first={first_bare}, ctx_first={first_ctx}, {match}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T19:34:58.261121+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T19:34:58.261281+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16980",
  "account": "root",
  "command": "/root/miniconda3/bin/python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== Context-dependent tokenization test ===')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\ncontext = chr(34) + 'type' + chr(34) + ': ' + chr(34)\ncontext_ids = tokenizer.encode(context, add_special_tokens=False)\nprint('Context ids: ' + str(context_ids))\n\nfor t in scierc_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print('  ' + t + ': bare=' + str(bare_ids) + ', in_context=' + str(type_ids) + ', ' + match)\n\nprint()\nprint('DocRED types:')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfor t in docred_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print('  ' + t + ': bare=' + str(bare_ids) + ', in_context=' + str(type_ids) + ', ' + match)\n\nprint()\nprint('=== First token stability check ===')\nall_types = scierc_types + docred_types\nstable = 0\nunstable = 0\nfor t in all_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    if type_ids and type_ids[0] == bare_ids[0]:\n        stable += 1\n    else:\n        unstable += 1\n        print('  UNSTABLE first token: ' + t + ' bare_first=' + str(bare_ids[0]) + ' ctx_first=' + str(type_ids[0] if type_ids else -1))\n\nprint('Stable: ' + str(stable) + '/' + str(len(all_types)))\nif unstable == 0:\n    print('All first tokens stable across contexts -- masking is SAFE')\nelse:\n    print(str(unstable) + ' types have unstable first tokens -- NEEDS FIX')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16980",
    "account": "root",
    "command": "/root/miniconda3/bin/python3 -c \"\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B', trust_remote_code=True)\n\nprint('=== Context-dependent tokenization test ===')\nscierc_types = ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\ncontext = chr(34) + 'type' + chr(34) + ': ' + chr(34)\ncontext_ids = tokenizer.encode(context, add_special_tokens=False)\nprint('Context ids: ' + str(context_ids))\n\nfor t in scierc_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print('  ' + t + ': bare=' + str(bare_ids) + ', in_context=' + str(type_ids) + ', ' + match)\n\nprint()\nprint('DocRED types:')\ndocred_types = ['PER', 'ORG', 'LOC', 'TIME', 'NUM', 'MISC']\nfor t in docred_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    match = 'SAME' if type_ids == bare_ids else 'DIFFERENT'\n    print('  ' + t + ': bare=' + str(bare_ids) + ', in_context=' + str(type_ids) + ', ' + match)\n\nprint()\nprint('=== First token stability check ===')\nall_types = scierc_types + docred_types\nstable = 0\nunstable = 0\nfor t in all_types:\n    bare_ids = tokenizer.encode(t, add_special_tokens=False)\n    full = context + t\n    full_ids = tokenizer.encode(full, add_special_tokens=False)\n    type_ids = full_ids[len(context_ids):]\n    if type_ids and type_ids[0] == bare_ids[0]:\n        stable += 1\n    else:\n        unstable += 1\n        print('  UNSTABLE first token: ' + t + ' bare_first=' + str(bare_ids[0]) + ' ctx_first=' + str(type_ids[0] if type_ids else -1))\n\nprint('Stable: ' + str(stable) + '/' + str(len(all_types)))\nif unstable == 0:\n    print('All first tokens stable across contexts -- masking is SAFE')\nelse:\n    print(str(unstable) + ' types have unstable first tokens -- NEEDS FIX')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:34:58.261442+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Context-dependent tokenization test ===\\nContext ids: [44470, 788, 330]\\n  Task: bare=[6262], in_context=[6262], SAME\\n  Method: bare=[3523], in_context=[3523], SAME\\n  Material: bare=[13415], in_context=[13415], SAME\\n  Metric: bare=[54310], in_context=[54310], SAME\\n  OtherScientificTerm: bare=[11409, 50565, 1086, 17249], in_context=[11409, 50565, 1086, 17249], SAME\\n  Generic: bare=[19964], in_context=[19964], SAME\\n\\nDocRED types:\\n  PER: bare=[9654], in_context=[9654], SAME\\n  ORG: bare=[44927], in_context=[44927], SAME\\n  LOC: bare=[12052], in_context=[12052], SAME\\n  TIME: bare=[18129], in_context=[18129], SAME\\n  NUM: bare=[17488], in_context=[17488], SAME\\n  MISC: bare=[44, 27629], in_context=[44, 27629], SAME\\n\\n=== First token stability check ===\\nStable: 12/12\\nAll first tokens stable across contexts -- masking is SAFE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_first_token_masking_20260513T193339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T19:34:58.261620+00:00_

## 验证结果

### SciERC Entity Types (Qwen3-8B tokenizer)

| Type | Token IDs | Decoded | First Token ID |
|------|-----------|---------|---------------|
| Task | [6262] | ['Task'] | 6262 |
| Method | [3523] | ['Method'] | 3523 |
| Material | [13415] | ['Material'] | 13415 |
| Metric | [54310] | ['Metric'] | 54310 |
| OtherScientificTerm | [11409, 50565, 1086, 17249] | ['Other', 'Scient', 'ific', 'Term'] | 11409 |
| Generic | [19964] | ['Generic'] | 19964 |

**SciERC: 6 个 type 的 first token 全部唯一，SAFE。** Reviewer 担心的 Method/Material/Metric 首字母都是 "M"，但 Qwen3 tokenizer 把它们各自编码为完整单词 token，不存在冲突。

### DocRED Entity Types

| Type | Token IDs | Decoded | First Token ID |
|------|-----------|---------|---------------|
| PER | [9654] | ['PER'] | 9654 |
| ORG | [44927] | ['ORG'] | 44927 |
| LOC | [12052] | ['LOC'] | 12052 |
| TIME | [18129] | ['TIME'] | 18129 |
| NUM | [17488] | ['NUM'] | 17488 |
| MISC | [44, 27629] | ['M', 'ISC'] | 44 |

**DocRED: 6 个 type 的 first token 全部唯一，SAFE。** MISC 被拆为 ['M', 'ISC']，但 first token id=44 ('M') 与其他 type 无冲突。

### Context-dependent Tokenization

所有 12 个 type 在 JSON 上下文（`"type": "` 之后）的 tokenization 与独立 tokenization **完全一致**。First-token masking 在实际生成场景中不会因上下文改变而失效。

### 结论

First-token masking 对 SciERC 和 DocRED 两个数据集均安全，无需 trie-based 方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_first_token_masking_20260513T193339"
}
```

</details>

---
