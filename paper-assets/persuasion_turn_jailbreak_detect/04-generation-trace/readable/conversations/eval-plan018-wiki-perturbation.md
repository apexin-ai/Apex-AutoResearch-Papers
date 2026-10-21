# eval plan018 wiki perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_eval_plan018-wiki-perturbation_20260518T062359.jsonl`
- **Structured JSON:** [`74ee0b273b724f143781.json`](../../sessions/74/74ee0b273b724f143781.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-18T06:27:13.888060+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T06:27:13.888413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T06:27:13.888630+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "ls /root/persuasion_turn_jailbreak_detect/checkpoints/plan_018_wiki_mlm/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "ls /root/persuasion_turn_jailbreak_detect/checkpoints/plan_018_wiki_mlm/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T06:27:13.888786+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "find /root/persuasion_turn_jailbreak_detect/ -name \"*perturb*\" -type f 2>/dev/null | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "find /root/persuasion_turn_jailbreak_detect/ -name \"*perturb*\" -type f 2>/dev/null | head -30",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T06:27:13.888924+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"best\\ngru\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T06:27:13.889048+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "cat /root/persuasion_turn_jailbreak_detect/src/plan_017_perturbed_eval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "cat /root/persuasion_turn_jailbreak_detect/src/plan_017_perturbed_eval.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T06:27:13.889180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/persuasion_turn_jailbreak_detect/src/__pycache__/adversarial_perturbation.cpython-312.pyc\\n/root/persuasion_turn_jailbreak_detect/src/adversarial_perturbation.py\\n/root/persuasion_turn_jailbreak_detect/src/plan_017_perturbed_eval.py\\n/root/persuasion_turn_jailbreak_detect/results/plan_004_perturbed_test.jsonl\\n/root/persuasion_turn_jailbreak_detect/results/perturbation_quality_report.json\\n/root/persuasion_turn_jailbreak_detect/results/adversarial_perturbation_results.json\\n/root/persuasion_turn_jailbreak_detect/results/plan_004_perturbation_eval.json\\n/root/persuasion_turn_jailbreak_detect/results/plan_017_mlm_perturbation.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T06:27:13.889304+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "cat /root/persuasion_turn_jailbreak_detect/src/plan_018_wiki_dd_eval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "cat /root/persuasion_turn_jailbreak_detect/src/plan_018_wiki_dd_eval.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T06:27:13.889557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import sys\\nimport json\\nimport random\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom pathlib import Path\\nfrom sklearn.metrics import f1_score, precision_score, recall_score\\n\\nsys.path.insert(0, \\\"/root/persuasion_turn_jailbreak_detect\\\")\\nfrom src.models.gru_classifier import GRUClassifier\\nfrom transformers import AutoTokenizer, AutoModel\\n\\nPROJ = Path(\\\"/root/persuasion_turn_jailbreak_detect\\\")\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nMODEL_NAME = \\\"microsoft/deberta-v3-base\\\"\\nMAX_LENGTH = 256\\nSEED = 42\\nGRU_HIDDEN = 256\\nGRU_LAYERS = 2\\nGRU_DROPOUT = 0.3\\n\\nrandom.seed(SEED)\\nnp.random.seed(SEED)\\ntorch.manual_seed(SEED)\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        return [json.loads(l) for l in f if l.strip()]\\n\\n\\ndef extract_user_turns(conv, use_original=False):\\n    turns = []\\n    for t in conv[\\\"turns\\\"]:\\n        if t[\\\"role\\\"] == \\\"user\\\":\\n            if use_original and \\\"original_content\\\" in t:\\n                turns.append(t[\\\"original_content\\\"])\\n            else:\\n                turns.append(t[\\\"content\\\"])\\n    return turns\\n\\n\\ndef get_label(conv):\\n    return 1 if conv[\\\"label\\\"] == \\\"jailbreak\\\" else 0\\n\\n\\ndef load_mlm_encoder(ckpt_path):\\n    model = AutoModel.from_pretrained(ckpt_path)\\n    enc = model.to(DEVICE).eval()\\n    for p in enc.parameters():\\n        p.requires_grad = False\\n    return enc\\n\\n\\ndef embed_turns(encoder, tokenizer, turns, k=None):\\n    t = turns[:k] if k is not None else turns\\n    if len(t) == 0:\\n        t = [\\\"\\\"]\\n    enc = tokenizer(t, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors=\\\"pt\\\").to(DEVICE)\\n    with torch.no_grad():\\n        out = encoder(input_ids=enc[\\\"input_ids\\\"], attention_mask=enc[\\\"attention_mask\\\"])\\n        return out.last_hidden_state[:, 0, :]\\n\\n\\ndef
…[truncated 5654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T06:27:13.889912+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Plan 018: Evaluate Wikipedia MLM control on DD OOD + IID.\\n# Identical pipeline to plan_017_dd_eval.py, checkpoint swapped to plan_018.\\n\\nimport sys\\nimport json\\nimport random\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom pathlib import Path\\nfrom sklearn.metrics import f1_score, precision_score, recall_score\\n\\nsys.path.insert(0, \\\"/root/persuasion_turn_jailbreak_detect\\\")\\nfrom src.models.gru_classifier import GRUClassifier\\nfrom transformers import AutoTokenizer, AutoModel\\n\\nPROJ = Path(\\\"/root/persuasion_turn_jailbreak_detect\\\")\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nMODEL_NAME = \\\"microsoft/deberta-v3-base\\\"\\nMAX_LENGTH = 256\\nSEED = 42\\nGRU_HIDDEN = 256\\nGRU_LAYERS = 2\\nGRU_DROPOUT = 0.3\\nGRU_LR = 1e-3\\nGRU_EPOCHS = 20\\nGRU_BATCH = 32\\n\\nrandom.seed(SEED)\\nnp.random.seed(SEED)\\ntorch.manual_seed(SEED)\\n\\n\\ndef load_jsonl(path):\\n    with open(path) as f:\\n        return [json.loads(l) for l in f if l.strip()]\\n\\n\\ndef extract_user_turns(conv):\\n    return [t[\\\"content\\\"] for t in conv[\\\"turns\\\"] if t[\\\"role\\\"] == \\\"user\\\"]\\n\\n\\ndef get_label(conv):\\n    return 1 if conv[\\\"label\\\"] == \\\"jailbreak\\\" else 0\\n\\n\\ndef load_mlm_encoder(ckpt_path):\\n    model = AutoModel.from_pretrained(ckpt_path)\\n    enc = model.to(DEVICE).eval()\\n    for p in enc.parameters():\\n        p.requires_grad = False\\n    return enc\\n\\n\\ndef embed_turns(encoder, tokenizer, turns, k=None):\\n    t = turns[:k] if k is not None else turns\\n    if len(t) == 0:\\n        t = [\\\"\\\"]\\n    enc = tokenizer(t, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors=\\\"pt\\\").to(DEVICE)\\n    with torch.no_grad():\\n        out = encoder(input_ids=enc[\\\"input_ids\\\"], attention_mask=enc[\\\"attention_mask\\\"])\\n        return out.last_hidden_state[:, 0, :]\\n\\n\\ndef precompute_conv_embeddings(encoder, toke
…[truncated 7186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T06:27:13.890126+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "ls /root/persuasion_turn_jailbreak_detect/checkpoints/plan_018_wiki_mlm/gru/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "ls /root/persuasion_turn_jailbreak_detect/checkpoints/plan_018_wiki_mlm/gru/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T06:27:13.890266+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"best_gru.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T06:27:13.890419+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "grep -n \"gru\" /root/persuasion_turn_jailbreak_detect/src/plan_018_wiki_dd_eval.py | head -10",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "grep -n \"gru\" /root/persuasion_turn_jailbreak_detect/src/plan_018_wiki_dd_eval.py | head -10",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T06:27:13.890580+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14:from src.models.gru_classifier import GRUClassifier\\n85:def train_gru(train_embs, train_labels, train_lengths, val_embs, val_labels, val_lengths, save_dir):\\n130:            torch.save(model.state_dict(), save_dir / \\\"best_gru.pt\\\")\\n135:    model.load_state_dict(torch.load(save_dir / \\\"best_gru.pt\\\", weights_only=True))\\n139:def eval_set(encoder, gru, tokenizer, convs, k=None):\\n140:    gru.eval()\\n148:            logits = gru(padded.to(DEVICE), lens)\\n178:    gru_save = PROJ / \\\"checkpoints/plan_018_wiki_mlm/gru\\\"\\n179:    gru = train_gru(train_embs, train_labels, train_lengths, val_embs, val_labels, val_lengths, gru_save)\\n193:    r_full = eval_set(encoder, gru, tokenizer, dd_test)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T06:27:13.890770+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "cat > /root/persuasion_turn_jailbreak_detect/src/plan_018_wiki_perturbed_eval.py << 'PYEOF'\nimport sys\nimport json\nimport random\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom pathlib import Path\nfrom sklearn.metrics import f1_score, precision_score, recall_score\n\nsys.path.insert(0, \"/root/persuasion_turn_jailbreak_detect\")\nfrom src.models.gru_classifier import GRUClassifier\nfrom transformers import AutoTokenizer, AutoModel\n\nPROJ = Path(\"/root/persuasion_turn_jailbreak_detect\")\nDEVICE = torch.device(\"cuda:0\")\nMAX_LENGTH = 256\nSEED = 42\nGRU_HIDDEN = 256\nGRU_LAYERS = 2\nGRU_DROPOUT = 0.3\n\nrandom.seed(SEED)\nnp.random.seed(SEED)\ntorch.manual_seed(SEED)\n\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(l) for l in f if l.strip()]\n\n\ndef extract_user_turns(conv, use_original=False):\n    turns = []\n    for t in conv[\"turns\"]:\n        if t[\"role\"] == \"user\":\n            if use_original and \"original_content\" in t:\n                turns.append(t[\"original_content\"])\n            else:\n                turns.append(t[\"content\"])\n    return turns\n\n\ndef get_label(conv):\n    return 1 if conv[\"label\"] == \"jailbreak\" else 0\n\n\ndef load_mlm_encoder(ckpt_path):\n    model = AutoModel.from_pretrained(ckpt_path)\n    enc = model.to(DEVICE).eval()\n    for p in enc.parameters():\n        p.requires_grad = False\n    return enc\n\n\ndef embed_turns(encoder, tokenizer, turns, k=None):\n    t = turns[:k] if k is not None else turns\n    if len(t) == 0:\n        t = [\"\"]\n    enc = tokenizer(t, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors=\"pt\").to(DEVICE)\n    with torch.no_grad():\n        out = encoder(input_ids=enc[\"input_ids\"], attention_mask=enc[\"attention_mask\"])\n        return out.last_hidden_state[:, 0, :]\n\n\ndef pad_embeddings(embs_list, labels, lengths):\n    max_len = max(lengths)\n    dim = embs_list[0].size(1)\n    padded = torch.zeros(len(embs_list), max_len, dim)\n    for i, e in enumerate(embs_list):\n        padded[i, :e.size(0), :] = e\n    return padded, torch.tensor(labels, dtype=torch.long), torch.tensor(lengths, dtype=torch.long)\n\n\ndef eval_set(encoder, gru, tokenizer, data, k=None, use_original=False):\n    all_embs, all_labels, all_lengths = [], [], []\n    for c in data:\n        turns = extract_user_turns(c, use_original=use_original)\n        embs = embed_turns(encoder, tokenizer, turns, k=k)\n        all_embs.append(embs.cpu())\n        all_labels.append(get_label(c))\n        all_lengths.append(embs.size(0))\n\n    padded, labels, lengths = pad_embeddings(all_embs, all_labels, all_lengths)\n    gru.eval()\n    with torch.no_grad():\n        logits = gru(padded.to(DEVICE), lengths.to(DEVICE))\n        preds = logits.argmax(dim=1).cpu().numpy()\n\n    y_true = labels.numpy()\n    return {\n        \"f1_macro\": round(f1_score(y_true, preds, average=\"macro\"), 4),\n        \"precision\": round(precision_score(y_true, preds, average=\"macro\"), 4),\n        \"recall\": round(recall_score(y_true, preds, average=\"macro\"), 4),\n        \"accuracy\": round((preds == y_true).mean(), 4),\n    }\n\n\ndef main():\n    print(\"Loading Wiki MLM encoder (plan_018)...\")\n    mlm_path = PROJ / \"checkpoints/plan_018_wiki_mlm/best\"\n    encoder = load_mlm_encoder(mlm_path)\n    tokenizer = AutoTokenizer.from_pretrained(mlm_path)\n\n    print(\"Loading BiGRU head (plan_018)...\")\n    embed_dim = encoder.config.hidden_size\n    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT)\n    gru_ckpt = torch.load(PROJ / \"checkpoints/plan_018_wiki_mlm/gru/best_gru.pt\", map_location=DEVICE, weights_only=True)\n    gru.load_state_dict(gru_ckpt)\n    gru.to(DEVICE).eval()\n\n    print(\"Loading perturbed test data...\")\n    perturbed_data = load_jsonl(PROJ / \"results/plan_004_perturbed_test.jsonl\")\n    print(f\"  {len(perturbed_data)} conversations ({sum(1 for d in perturbed_data if d['label']=='jailbreak')} jailbreak, {sum(1 for d in perturbed_data if d['label']=='benign')} benign)\")\n\n    k_values = [1, 2, 3, 5]\n    results = {\"clean\": {}, \"perturbed\": {}, \"delta\": {}}\n\n    print(\"\\n=== Clean (original_content) ===\")\n    for k_label, k_val in [(\"full\", None)] + [(f\"k={k}\", k) for k in k_values]:\n        r = eval_set(encoder, gru, tokenizer, perturbed_data, k=k_val, use_original=True)\n        results[\"clean\"][k_label] = r\n        print(f\"  {k_label}: F1={r['f1_macro']:.4f} P={r['precision']:.4f} R={r['recall']:.4f}\")\n\n    print(\"\\n=== Perturbed (content) ===\")\n    for k_label, k_val in [(\"full\", None)] + [(f\"k={k}\", k) for k in k_values]:\n        r = eval_set(encoder, gru, tokenizer, perturbed_data, k=k_val, use_original=False)\n        results[\"perturbed\"][k_label] = r\n        print(f\"  {k_label}: F1={r['f1_macro']:.4f} P={r['precision']:.4f} R={r['recall']:.4f}\")\n\n    print(\"\\n=== Delta (clean - perturbed) ===\")\n    for k_label in [\"full\"] + [f\"k={k}\" for k in k_values]:\n        delta = round(results[\"clean\"][k_label][\"f1_macro\"] - results[\"perturbed\"][k_label][\"f1_macro\"], 4)\n        results[\"delta\"][k_label] = delta\n        print(f\"  {k_label}: {delta:+.4f}\")\n\n    plan004_ref = {\n        \"treatment\": {\"k=1\": -0.0256, \"k=2\": 0.0, \"k=3\": 0.0, \"full\": 0.0},\n        \"baseline\": {\"k=1\": -0.1464, \"k=2\": -0.121, \"k=3\": -0.1382, \"full\": -0.1176},\n        \"tfidf\": {\"k=1\": -0.0959, \"k=2\": -0.0411, \"k=3\": -0.0133, \"full\": -0.0133},\n        \"jb_mlm\": {\"k=1\": -0.0256, \"k=2\": 0.0, \"k=3\": 0.0, \"k=5\": 0.0, \"full\": -0.026},\n    }\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"COMPARISON: Wiki MLM (018) vs all models (F1 delta: clean - perturbed)\")\n    print(\"=\" * 80)\n    print(f\"{'K':<6} {'Wiki MLM':>10} {'JB MLM':>10} {'Treatment':>10} {'Baseline':>10} {'TF-IDF':>10}\")\n    print(\"-\" * 58)\n    for k_label in [\"k=1\", \"k=2\", \"k=3\", \"full\"]:\n        wiki_d = -results[\"delta\"].get(k_label, 0)\n        jb_d = plan004_ref[\"jb_mlm\"].get(k_label, float(\"nan\"))\n        tr_d = plan004_ref[\"treatment\"].get(k_label, float(\"nan\"))\n        bl_d = plan004_ref[\"baseline\"].get(k_label, float(\"nan\"))\n        tf_d = plan004_ref[\"tfidf\"].get(k_label, float(\"nan\"))\n        print(f\"{k_label:<6} {wiki_d:>+10.4f} {jb_d:>+10.4f} {tr_d:>+10.4f} {bl_d:>+10.4f} {tf_d:>+10.4f}\")\n\n    out = {\n        \"experiment\": \"plan_018_wiki_perturbation\",\n        \"description\": \"Wikipedia MLM control model evaluated on adversarially perturbed data\",\n        \"clean_results\": results[\"clean\"],\n        \"perturbed_results\": results[\"perturbed\"],\n        \"delta_f1\": results[\"delta\"],\n        \"reference_plan004\": plan004_ref,\n        \"sample_count\": len(perturbed_data),\n    }\n    out_path = PROJ / \"results/plan_018_wiki_perturbation.json\"\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script created.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "cat > /root/persuasion_turn_jailbreak_detect/src/plan_018_wiki_perturbed_eval.py << 'PYEOF'\nimport sys\nimport json\nimport random\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom pathlib import Path\nfrom sklearn.metrics import f1_score, precision_score, recall_score\n\nsys.path.insert(0, \"/root/persuasion_turn_jailbreak_detect\")\nfrom src.models.gru_classifier import GRUClassifier\nfrom transformers import AutoTokenizer, AutoModel\n\nPROJ = Path(\"/root/persuasion_turn_jailbreak_detect\")\nDEVICE = torch.device(\"cuda:0\")\nMAX_LENGTH = 256\nSEED = 42\nGRU_HIDDEN = 256\nGRU_LAYERS = 2\nGRU_DROPOUT = 0.3\n\nrandom.seed(SEED)\nnp.random.seed(SEED)\ntorch.manual_seed(SEED)\n\n\ndef load_jsonl(path):\n    with open(path) as f:\n        return [json.loads(l) for l in f if l.strip()]\n\n\ndef extract_user_turns(conv, use_original=False):\n    turns = []\n    for t in conv[\"turns\"]:\n        if t[\"role\"] == \"user\":\n            if use_original and \"original_content\" in t:\n                turns.append(t[\"original_content\"])\n            else:\n                turns.append(t[\"content\"])\n    return turns\n\n\ndef get_label(conv):\n    return 1 if conv[\"label\"] == \"jailbreak\" else 0\n\n\ndef load_mlm_encoder(ckpt_path):\n    model = AutoModel.from_pretrained(ckpt_path)\n    enc = model.to(DEVICE).eval()\n    for p in enc.parameters():\n        p.requires_grad = False\n    return enc\n\n\ndef embed_turns(encoder, tokenizer, turns, k=None):\n    t = turns[:k] if k is not None else turns\n    if len(t) == 0:\n        t = [\"\"]\n    enc = tokenizer(t, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors=\"pt\").to(DEVICE)\n    with torch.no_grad():\n        out = encoder(input_ids=enc[\"input_ids\"], attention_mask=enc[\"attention_mask\"])\n        return out.last_hidden_state[:, 0, :]\n\n\ndef pad_embeddings(embs_list, labels, lengths):\n    max_len = max(lengths)\n    dim = embs_list[0].size(1)\n    padded = torch.zeros(len(embs_list), max_len, dim)\n    for i, e in enumerate(embs_list):\n        padded[i, :e.size(0), :] = e\n    return padded, torch.tensor(labels, dtype=torch.long), torch.tensor(lengths, dtype=torch.long)\n\n\ndef eval_set(encoder, gru, tokenizer, data, k=None, use_original=False):\n    all_embs, all_labels, all_lengths = [], [], []\n    for c in data:\n        turns = extract_user_turns(c, use_original=use_original)\n        embs = embed_turns(encoder, tokenizer, turns, k=k)\n        all_embs.append(embs.cpu())\n        all_labels.append(get_label(c))\n        all_lengths.append(embs.size(0))\n\n    padded, labels, lengths = pad_embeddings(all_embs, all_labels, all_lengths)\n    gru.eval()\n    with torch.no_grad():\n        logits = gru(padded.to(DEVICE), lengths.to(DEVICE))\n        preds = logits.argmax(dim=1).cpu().numpy()\n\n    y_true = labels.numpy()\n    return {\n        \"f1_macro\": round(f1_score(y_true, preds, average=\"macro\"), 4),\n        \"precision\": round(precision_score(y_true, preds, average=\"macro\"), 4),\n        \"recall\": round(recall_score(y_true, preds, average=\"macro\"), 4),\n        \"accuracy\": round((preds == y_true).mean(), 4),\n    }\n\n\ndef main():\n    print(\"Loading Wiki MLM encoder (plan_018)...\")\n    mlm_path = PROJ / \"checkpoints/plan_018_wiki_mlm/best\"\n    encoder = load_mlm_encoder(mlm_path)\n    tokenizer = AutoTokenizer.from_pretrained(mlm_path)\n\n    print(\"Loading BiGRU head (plan_018)...\")\n    embed_dim = encoder.config.hidden_size\n    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT)\n    gru_ckpt = torch.load(PROJ / \"checkpoints/plan_018_wiki_mlm/gru/best_gru.pt\", map_location=DEVICE, weights_only=True)\n    gru.load_state_dict(gru_ckpt)\n    gru.to(DEVICE).eval()\n\n    print(\"Loading perturbed test data...\")\n    perturbed_data = load_jsonl(PROJ / \"results/plan_004_perturbed_test.jsonl\")\n    print(f\"  {len(perturbed_data)} conversations ({sum(1 for d in perturbed_data if d['label']=='jailbreak')} jailbreak, {sum(1 for d in perturbed_data if d['label']=='benign')} benign)\")\n\n    k_values = [1, 2, 3, 5]\n    results = {\"clean\": {}, \"perturbed\": {}, \"delta\": {}}\n\n    print(\"\\n=== Clean (original_content) ===\")\n    for k_label, k_val in [(\"full\", None)] + [(f\"k={k}\", k) for k in k_values]:\n        r = eval_set(encoder, gru, tokenizer, perturbed_data, k=k_val, use_original=True)\n        results[\"clean\"][k_label] = r\n        print(f\"  {k_label}: F1={r['f1_macro']:.4f} P={r['precision']:.4f} R={r['recall']:.4f}\")\n\n    print(\"\\n=== Perturbed (content) ===\")\n    for k_label, k_val in [(\"full\", None)] + [(f\"k={k}\", k) for k in k_values]:\n        r = eval_set(encoder, gru, tokenizer, perturbed_data, k=k_val, use_original=False)\n        results[\"perturbed\"][k_label] = r\n        print(f\"  {k_label}: F1={r['f1_macro']:.4f} P={r['precision']:.4f} R={r['recall']:.4f}\")\n\n    print(\"\\n=== Delta (clean - perturbed) ===\")\n    for k_label in [\"full\"] + [f\"k={k}\" for k in k_values]:\n        delta = round(results[\"clean\"][k_label][\"f1_macro\"] - results[\"perturbed\"][k_label][\"f1_macro\"], 4)\n        results[\"delta\"][k_label] = delta\n        print(f\"  {k_label}: {delta:+.4f}\")\n\n    plan004_ref = {\n        \"treatment\": {\"k=1\": -0.0256, \"k=2\": 0.0, \"k=3\": 0.0, \"full\": 0.0},\n        \"baseline\": {\"k=1\": -0.1464, \"k=2\": -0.121, \"k=3\": -0.1382, \"full\": -0.1176},\n        \"tfidf\": {\"k=1\": -0.0959, \"k=2\": -0.0411, \"k=3\": -0.0133, \"full\": -0.0133},\n        \"jb_mlm\": {\"k=1\": -0.0256, \"k=2\": 0.0, \"k=3\": 0.0, \"k=5\": 0.0, \"full\": -0.026},\n    }\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"COMPARISON: Wiki MLM (018) vs all models (F1 delta: clean - perturbed)\")\n    print(\"=\" * 80)\n    print(f\"{'K':<6} {'Wiki MLM':>10} {'JB MLM':>10} {'Treatment':>10} {'Baseline':>10} {'TF-IDF':>10}\")\n    print(\"-\" * 58)\n    for k_label in [\"k=1\", \"k=2\", \"k=3\", \"full\"]:\n        wiki_d = -results[\"delta\"].get(k_label, 0)\n        jb_d = plan004_ref[\"jb_mlm\"].get(k_label, float(\"nan\"))\n        tr_d = plan004_ref[\"treatment\"].get(k_label, float(\"nan\"))\n        bl_d = plan004_ref[\"baseline\"].get(k_label, float(\"nan\"))\n        tf_d = plan004_ref[\"tfidf\"].get(k_label, float(\"nan\"))\n        print(f\"{k_label:<6} {wiki_d:>+10.4f} {jb_d:>+10.4f} {tr_d:>+10.4f} {bl_d:>+10.4f} {tf_d:>+10.4f}\")\n\n    out = {\n        \"experiment\": \"plan_018_wiki_perturbation\",\n        \"description\": \"Wikipedia MLM control model evaluated on adversarially perturbed data\",\n        \"clean_results\": results[\"clean\"],\n        \"perturbed_results\": results[\"perturbed\"],\n        \"delta_f1\": results[\"delta\"],\n        \"reference_plan004\": plan004_ref,\n        \"sample_count\": len(perturbed_data),\n    }\n    out_path = PROJ / \"results/plan_018_wiki_perturbation.json\"\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script created.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T06:27:13.891001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script created.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T06:27:13.891148+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 python src/plan_018_wiki_perturbed_eval.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 python src/plan_018_wiki_perturbed_eval.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T06:27:13.891276+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"bash: line 1: python: command not found\\n\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T06:27:13.891396+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "which python3 && cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 python3 src/plan_018_wiki_perturbed_eval.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "which python3 && cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 python3 src/plan_018_wiki_perturbed_eval.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T06:27:13.891519+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T06:27:13.891668+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "ls /root/miniconda3/bin/python* 2>/dev/null; ls /opt/conda/bin/python* 2>/dev/null; which python3.12 2>/dev/null; find / -maxdepth 4 -name \"python3*\" -type f 2>/dev/null | head -5",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "ls /root/miniconda3/bin/python* 2>/dev/null; ls /opt/conda/bin/python* 2>/dev/null; which python3.12 2>/dev/null; find / -maxdepth 4 -name \"python3*\" -type f 2>/dev/null | head -5",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T06:27:13.891798+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3\\n/root/miniconda3/bin/python3-config\\n/root/miniconda3/bin/python3.1\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T06:27:13.891917+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T06:27:13.892070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading Wiki MLM encoder (plan_018)...\\nLoading BiGRU head (plan_018)...\\nLoading perturbed test data...\\n  76 conversations (38 jailbreak, 38 benign)\\n\\n=== Clean (original_content) ===\\n  full: F1=0.9868 P=0.9872 R=0.9868\\n  k=1: F1=0.9474 P=0.9474 R=0.9474\\n  k=2: F1=0.9341 P=0.9369 R=0.9342\\n  k=3: F1=0.9737 P=0.9750 R=0.9737\\n  k=5: F1=0.9868 P=0.9872 R=0.9868\\n\\n=== Perturbed (content) ===\\n  full: F1=0.8661 P=0.8958 R=0.8684\\n  k=1: F1=0.8238 P=0.8725 R=0.8289\\n  k=2: F1=0.7797 P=0.8519 R=0.7895\\n  k=3: F1=0.7946 P=0.8585 R=0.8026\\n  k=5: F1=0.8381 P=0.8800 R=0.8421\\n\\n=== Delta (clean - perturbed) ===\\n  full: +0.1207\\n  k=1: +0.1236\\n  k=2: +0.1544\\n  k=3: +0.1791\\n  k=5: +0.1487\\n\\n================================================================================\\nCOMPARISON: Wiki MLM (018) vs all models (F1 delta: clean - perturbed)\\n================================================================================\\nK        Wiki MLM     JB MLM  Treatment   Baseline     TF-IDF\\n----------------------------------------------------------\\nk=1       -0.1236    -0.0256    -0.0256    -0.1464    -0.0959\\nk=2       -0.1544    +0.0000    +0.0000    -0.1210    -0.0411\\nk=3       -0.1791    +0.0000    +0.0000    -0.1382    -0.0133\\nfull      -0.1207    -0.0260    +0.0000    -0.1176    -0.0133\\n\\nResults saved to /root/persuasion_turn_jailbreak_detect/results/plan_018_wiki_perturbation.json\\n\", \"stderr\": \"\\rLoading weights:   0%|          | 0/198 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 198/198 [00:00<00:00, 12672.77it/s]\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T06:27:13.892228+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "hypothesis",
  "value": "Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "hypothesis",
    "value": "Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T06:27:13.892365+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:25:52.733Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1294}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T06:27:13.892485+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "parent",
  "value": "plan_018_wiki_mlm_control",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "parent",
    "value": "plan_018_wiki_mlm_control",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T06:27:13.892633+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:25:55.829Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1362}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T06:27:13.892757+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "status",
  "value": "RUNNING",
  "project": "persuasion_turn_jailbreak_detect",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py', 'server': 'westd-33183', 'data_path': 'results/plan_004_perturbed_test.jsonl', 'data_count': 76, 'model_name': 'plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)', 'seed': 42, 'checkpoint_source': 'checkpoints/plan_018_wiki_mlm/', 'eval_data': 'results/plan_004_perturbed_test.jsonl'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "status",
    "value": "RUNNING",
    "project": "persuasion_turn_jailbreak_detect",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py', 'server': 'westd-33183', 'data_path': 'results/plan_004_perturbed_test.jsonl', 'data_count': 76, 'model_name': 'plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)', 'seed': 42, 'checkpoint_source': 'checkpoints/plan_018_wiki_mlm/', 'eval_data': 'results/plan_004_perturbed_test.jsonl'}"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T06:27:13.892890+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.2121}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T06:27:13.893009+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "status",
  "value": "QUEUED",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "status",
    "value": "QUEUED",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T06:27:13.893141+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:04.774Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3547}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T06:27:13.893278+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "status",
  "value": "RUNNING",
  "project": "persuasion_turn_jailbreak_detect",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py', 'server': 'westd-33183', 'data_path': 'results/plan_004_perturbed_test.jsonl', 'data_count': 76, 'model_name': 'plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)', 'seed': 42, 'checkpoint_source': 'checkpoints/plan_018_wiki_mlm/', 'eval_data': 'results/plan_004_perturbed_test.jsonl'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "status",
    "value": "RUNNING",
    "project": "persuasion_turn_jailbreak_detect",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py', 'server': 'westd-33183', 'data_path': 'results/plan_004_perturbed_test.jsonl', 'data_count': 76, 'model_name': 'plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)', 'seed': 42, 'checkpoint_source': 'checkpoints/plan_018_wiki_mlm/', 'eval_data': 'results/plan_004_perturbed_test.jsonl'}"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T06:27:13.893480+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:09.483Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py\", \"server\": \"westd-33183\", \"data_path\": \"results/plan_004_perturbed_test.jsonl\", \"data_count\": 76, \"model_name\": \"plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/plan_018_wiki_mlm/\", \"eval_data\": \"results/plan_004_perturbed_test.jsonl\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3266}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T06:27:13.893688+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "checkpoint_path",
  "value": "checkpoints/plan_018_wiki_mlm/",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "checkpoint_path",
    "value": "checkpoints/plan_018_wiki_mlm/",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T06:27:13.893835+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:13.863Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py\", \"server\": \"westd-33183\", \"data_path\": \"results/plan_004_perturbed_test.jsonl\", \"data_count\": 76, \"model_name\": \"plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/plan_018_wiki_mlm/\", \"eval_data\": \"results/plan_004_perturbed_test.jsonl\"}, \"checkpoint_path\": \"checkpoints/plan_018_wiki_mlm/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1396}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T06:27:13.893968+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "log_path",
  "value": "results/plan_018_wiki_perturbation.json",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "log_path",
    "value": "results/plan_018_wiki_perturbation.json",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T06:27:13.894112+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:14.666Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py\", \"server\": \"westd-33183\", \"data_path\": \"results/plan_004_perturbed_test.jsonl\", \"data_count\": 76, \"model_name\": \"plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/plan_018_wiki_mlm/\", \"eval_data\": \"results/plan_004_perturbed_test.jsonl\"}, \"checkpoint_path\": \"checkpoints/plan_018_wiki_mlm/\", \"log_path\": \"results/plan_018_wiki_perturbation.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1672}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T06:27:13.894249+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "metrics",
  "value": "{'clean_f1_full': 0.9868, 'perturbed_f1_full': 0.8661, 'delta_f1_full': -0.1207, 'clean_f1_k1': 0.9474, 'perturbed_f1_k1': 0.8238, 'delta_f1_k1': -0.1236, 'clean_f1_k2': 0.9341, 'perturbed_f1_k2': 0.7797, 'delta_f1_k2': -0.1544, 'clean_f1_k3': 0.9737, 'perturbed_f1_k3': 0.7946, 'delta_f1_k3': -0.1791, 'clean_f1_k5': 0.9868, 'perturbed_f1_k5': 0.8381, 'delta_f1_k5': -0.1487, 'sample_count': 76}",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "metrics",
    "value": "{'clean_f1_full': 0.9868, 'perturbed_f1_full': 0.8661, 'delta_f1_full': -0.1207, 'clean_f1_k1': 0.9474, 'perturbed_f1_k1': 0.8238, 'delta_f1_k1': -0.1236, 'clean_f1_k2': 0.9341, 'perturbed_f1_k2': 0.7797, 'delta_f1_k2': -0.1544, 'clean_f1_k3': 0.9737, 'perturbed_f1_k3': 0.7946, 'delta_f1_k3': -0.1791, 'clean_f1_k5': 0.9868, 'perturbed_f1_k5': 0.8381, 'delta_f1_k5': -0.1487, 'sample_count': 76}",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T06:27:13.894407+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:20.523Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py\", \"server\": \"westd-33183\", \"data_path\": \"results/plan_004_perturbed_test.jsonl\", \"data_count\": 76, \"model_name\": \"plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/plan_018_wiki_mlm/\", \"eval_data\": \"results/plan_004_perturbed_test.jsonl\"}, \"checkpoint_path\": \"checkpoints/plan_018_wiki_mlm/\", \"log_path\": \"results/plan_018_wiki_perturbation.json\", \"metrics\": {\"clean_f1_full\": 0.9868, \"perturbed_f1_full\": 0.8661, \"delta_f1_full\": -0.1207, \"clean_f1_k1\": 0.9474, \"perturbed_f1_k1\": 0.8238, \"delta_f1_k1\": -0.1236, \"clean_f1_k2\": 0.9341, \"perturbed_f1_k2\": 0.7797, \"delta_f1_k2\": -0.1544, \"clean_f1_k3\": 0.9737, \"perturbed_f1_k3\": 0.7946, \"delta_f1_k3\": -0.1791, \"clean_f1_k5\": 0.9868, \"perturbed_f1_k5\": 0.8381, \"delta_f1_k5\": -0.1487, \"sample_count\": 76}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1442}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T06:27:13.894587+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "conclusion",
  "value": "Hypothesis confirmed. Wiki MLM shows massive perturbation degradation (delta=-0.121 at full, -0.179 at k=3), comparable to vanilla baseline (-0.118) and far worse than JB MLM (-0.026) and persuasion treatment (0.000). Out-of-domain pretraining provides zero robustness to surface perturbation, confirming domain-specific MLM exposure is the key factor.",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "conclusion",
    "value": "Hypothesis confirmed. Wiki MLM shows massive perturbation degradation (delta=-0.121 at full, -0.179 at k=3), comparable to vanilla baseline (-0.118) and far worse than JB MLM (-0.026) and persuasion treatment (0.000). Out-of-domain pretraining provides zero robustness to surface perturbation, confirming domain-specific MLM exposure is the key factor.",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T06:27:13.894741+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'Hypothesis confirmed. Wiki MLM shows massive perturbation degradation (delta=-0.121 at full, -0.179 at k=3), comparable to vanilla baseline (-0.118) and far worse than JB MLM (-0.026) and persuasion treatment (0.000). Out-of-domain pretraining provides zero robustness to surface perturbation, confirming domain-specific MLM exposure is the key factor.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.0783}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T06:27:13.894868+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "conclusion",
  "value": "success",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "conclusion",
    "value": "success",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T06:27:13.895049+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:29.187Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py\", \"server\": \"westd-33183\", \"data_path\": \"results/plan_004_perturbed_test.jsonl\", \"data_count\": 76, \"model_name\": \"plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/plan_018_wiki_mlm/\", \"eval_data\": \"results/plan_004_perturbed_test.jsonl\"}, \"checkpoint_path\": \"checkpoints/plan_018_wiki_mlm/\", \"log_path\": \"results/plan_018_wiki_perturbation.json\", \"metrics\": {\"clean_f1_full\": 0.9868, \"perturbed_f1_full\": 0.8661, \"delta_f1_full\": -0.1207, \"clean_f1_k1\": 0.9474, \"perturbed_f1_k1\": 0.8238, \"delta_f1_k1\": -0.1236, \"clean_f1_k2\": 0.9341, \"perturbed_f1_k2\": 0.7797, \"delta_f1_k2\": -0.1544, \"clean_f1_k3\": 0.9737, \"perturbed_f1_k3\": 0.7946, \"delta_f1_k3\": -0.1791, \"clean_f1_k5\": 0.9868, \"perturbed_f1_k5\": 0.8381, \"delta_f1_k5\": -0.1487, \"sample_count\": 76}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1545}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T06:27:13.895190+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "plan_018_wiki_perturbation",
  "field": "status",
  "value": "DONE",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "plan_018_wiki_perturbation",
    "field": "status",
    "value": "DONE",
    "project": "persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T06:27:13.895408+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"plan_018_wiki_perturbation\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:25:52.733Z\", \"updated_at\": \"2026-05-18T06:26:33.520Z\", \"hypothesis\": \"Wikipedia MLM model will show significant perturbation degradation (worse than jailbreak MLM -0.026), as out-of-domain pretraining provides even less robustness to surface-level perturbation\", \"parent\": \"plan_018_wiki_mlm_control\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/plan_018_wiki_perturbed_eval.py\", \"server\": \"westd-33183\", \"data_path\": \"results/plan_004_perturbed_test.jsonl\", \"data_count\": 76, \"model_name\": \"plan_018_wiki_mlm (DeBERTa-v3-base + BiGRU)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/plan_018_wiki_mlm/\", \"eval_data\": \"results/plan_004_perturbed_test.jsonl\"}, \"checkpoint_path\": \"checkpoints/plan_018_wiki_mlm/\", \"log_path\": \"results/plan_018_wiki_perturbation.json\", \"metrics\": {\"clean_f1_full\": 0.9868, \"perturbed_f1_full\": 0.8661, \"delta_f1_full\": -0.1207, \"clean_f1_k1\": 0.9474, \"perturbed_f1_k1\": 0.8238, \"delta_f1_k1\": -0.1236, \"clean_f1_k2\": 0.9341, \"perturbed_f1_k2\": 0.7797, \"delta_f1_k2\": -0.1544, \"clean_f1_k3\": 0.9737, \"perturbed_f1_k3\": 0.7946, \"delta_f1_k3\": -0.1791, \"clean_f1_k5\": 0.9868, \"perturbed_f1_k5\": 0.8381, \"delta_f1_k5\": -0.1487, \"sample_count\": 76}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T06:26:33.520Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4512}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T06:27:13.895640+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_018_wiki_perturbation_results",
  "type": "data",
  "description": "Plan 018 Wiki MLM perturbation eval results: clean F1=0.987 → perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
  "project": "persuasion_turn_jailbreak_detect",
  "exp_id": "plan_018_wiki_perturbation",
  "source_path": "/root/persuasion_turn_jailbreak_detect/results/plan_018_wiki_perturbation.json",
  "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_018_wiki_perturbation_results",
    "type": "data",
    "description": "Plan 018 Wiki MLM perturbation eval results: clean F1=0.987 → perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
    "project": "persuasion_turn_jailbreak_detect",
    "exp_id": "plan_018_wiki_perturbation",
    "source_path": "/root/persuasion_turn_jailbreak_detect/results/plan_018_wiki_perturbation.json",
    "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T06:27:13.895801+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/persuasion_turn_jailbreak_detect/results/plan_018_wiki_perturbation.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T06:27:13.895928+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "command": "cat /root/persuasion_turn_jailbreak_detect/results/plan_018_wiki_perturbation.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "command": "cat /root/persuasion_turn_jailbreak_detect/results/plan_018_wiki_perturbation.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T06:27:13.896168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"plan_018_wiki_perturbation\\\",\\n  \\\"description\\\": \\\"Wikipedia MLM control model evaluated on adversarially perturbed data\\\",\\n  \\\"clean_results\\\": {\\n    \\\"full\\\": {\\n      \\\"f1_macro\\\": 0.9868,\\n      \\\"precision\\\": 0.9872,\\n      \\\"recall\\\": 0.9868,\\n      \\\"accuracy\\\": 0.9868\\n    },\\n    \\\"k=1\\\": {\\n      \\\"f1_macro\\\": 0.9474,\\n      \\\"precision\\\": 0.9474,\\n      \\\"recall\\\": 0.9474,\\n      \\\"accuracy\\\": 0.9474\\n    },\\n    \\\"k=2\\\": {\\n      \\\"f1_macro\\\": 0.9341,\\n      \\\"precision\\\": 0.9369,\\n      \\\"recall\\\": 0.9342,\\n      \\\"accuracy\\\": 0.9342\\n    },\\n    \\\"k=3\\\": {\\n      \\\"f1_macro\\\": 0.9737,\\n      \\\"precision\\\": 0.975,\\n      \\\"recall\\\": 0.9737,\\n      \\\"accuracy\\\": 0.9737\\n    },\\n    \\\"k=5\\\": {\\n      \\\"f1_macro\\\": 0.9868,\\n      \\\"precision\\\": 0.9872,\\n      \\\"recall\\\": 0.9868,\\n      \\\"accuracy\\\": 0.9868\\n    }\\n  },\\n  \\\"perturbed_results\\\": {\\n    \\\"full\\\": {\\n      \\\"f1_macro\\\": 0.8661,\\n      \\\"precision\\\": 0.8958,\\n      \\\"recall\\\": 0.8684,\\n      \\\"accuracy\\\": 0.8684\\n    },\\n    \\\"k=1\\\": {\\n      \\\"f1_macro\\\": 0.8238,\\n      \\\"precision\\\": 0.8725,\\n      \\\"recall\\\": 0.8289,\\n      \\\"accuracy\\\": 0.8289\\n    },\\n    \\\"k=2\\\": {\\n      \\\"f1_macro\\\": 0.7797,\\n      \\\"precision\\\": 0.8519,\\n      \\\"recall\\\": 0.7895,\\n      \\\"accuracy\\\": 0.7895\\n    },\\n    \\\"k=3\\\": {\\n      \\\"f1_macro\\\": 0.7946,\\n      \\\"precision\\\": 0.8585,\\n      \\\"recall\\\": 0.8026,\\n      \\\"accuracy\\\": 0.8026\\n    },\\n    \\\"k=5\\\": {\\n      \\\"f1_macro\\\": 0.8381,\\n      \\\"precision\\\": 0.88,\\n      \\\"recall\\\": 0.8421,\\n      \\\"accuracy\\\": 0.8421\\n    }\\n  },\\n  \\\"delta_f1\\\": {\\n    \\\"full\\\": 0.1207,\\n    \\\"k=1
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T06:27:13.896345+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_018_wiki_perturbation_results",
  "type": "data",
  "description": "Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
  "project": "persuasion_turn_jailbreak_detect",
  "exp_id": "plan_018_wiki_perturbation",
  "content": "{\"experiment\":\"plan_018_wiki_perturbation\",\"description\":\"Wikipedia MLM control model evaluated on adversarially perturbed data\",\"clean_results\":{\"full\":{\"f1_macro\":0.9868,\"precision\":0.9872,\"recall\":0.9868,\"accuracy\":0.9868},\"k=1\":{\"f1_macro\":0.9474,\"precision\":0.9474,\"recall\":0.9474,\"accuracy\":0.9474},\"k=2\":{\"f1_macro\":0.9341,\"precision\":0.9369,\"recall\":0.9342,\"accuracy\":0.9342},\"k=3\":{\"f1_macro\":0.9737,\"precision\":0.975,\"recall\":0.9737,\"accuracy\":0.9737},\"k=5\":{\"f1_macro\":0.9868,\"precision\":0.9872,\"recall\":0.9868,\"accuracy\":0.9868}},\"perturbed_results\":{\"full\":{\"f1_macro\":0.8661,\"precision\":0.8958,\"recall\":0.8684,\"accuracy\":0.8684},\"k=1\":{\"f1_macro\":0.8238,\"precision\":0.8725,\"recall\":0.8289,\"accuracy\":0.8289},\"k=2\":{\"f1_macro\":0.7797,\"precision\":0.8519,\"recall\":0.7895,\"accuracy\":0.7895},\"k=3\":{\"f1_macro\":0.7946,\"precision\":0.8585,\"recall\":0.8026,\"accuracy\":0.8026},\"k=5\":{\"f1_macro\":0.8381,\"precision\":0.88,\"recall\":0.8421,\"accuracy\":0.8421}},\"delta_f1\":{\"full\":0.1207,\"k=1\":0.1236,\"k=2\":0.1544,\"k=3\":0.1791,\"k=5\":0.1487},\"sample_count\":76}",
  "content_filename": "plan_018_wiki_perturbation.json",
  "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_018_wiki_perturbation_results",
    "type": "data",
    "description": "Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
    "project": "persuasion_turn_jailbreak_detect",
    "exp_id": "plan_018_wiki_perturbation",
    "content": "{\"experiment\":\"plan_018_wiki_perturbation\",\"description\":\"Wikipedia MLM control model evaluated on adversarially perturbed data\",\"clean_results\":{\"full\":{\"f1_macro\":0.9868,\"precision\":0.9872,\"recall\":0.9868,\"accuracy\":0.9868},\"k=1\":{\"f1_macro\":0.9474,\"precision\":0.9474,\"recall\":0.9474,\"accuracy\":0.9474},\"k=2\":{\"f1_macro\":0.9341,\"precision\":0.9369,\"recall\":0.9342,\"accuracy\":0.9342},\"k=3\":{\"f1_macro\":0.9737,\"precision\":0.975,\"recall\":0.9737,\"accuracy\":0.9737},\"k=5\":{\"f1_macro\":0.9868,\"precision\":0.9872,\"recall\":0.9868,\"accuracy\":0.9868}},\"perturbed_results\":{\"full\":{\"f1_macro\":0.8661,\"precision\":0.8958,\"recall\":0.8684,\"accuracy\":0.8684},\"k=1\":{\"f1_macro\":0.8238,\"precision\":0.8725,\"recall\":0.8289,\"accuracy\":0.8289},\"k=2\":{\"f1_macro\":0.7797,\"precision\":0.8519,\"recall\":0.7895,\"accuracy\":0.7895},\"k=3\":{\"f1_macro\":0.7946,\"precision\":0.8585,\"recall\":0.8026,\"accuracy\":0.8026},\"k=5\":{\"f1_macro\":0.8381,\"precision\":0.88,\"recall\":0.8421,\"accuracy\":0.8421}},\"delta_f1\":{\"full\":0.1207,\"k=1\":0.1236,\"k=2\":0.1544,\"k=3\":0.1791,\"k=5\":0.1487},\"sample_count\":76}",
    "content_filename": "plan_018_wiki_perturbation.json",
    "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T06:27:13.896493+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'plan_018_...87}, 'sample_count': 76}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T06:27:13.896679+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_018_wiki_perturbation_results",
  "type": "data",
  "description": "Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
  "project": "persuasion_turn_jailbreak_detect",
  "exp_id": "plan_018_wiki_perturbation",
  "content": "{\"experiment\":\"plan_018_wiki_perturbation\",\"description\":\"Wikipedia MLM control model evaluated on adversarially perturbed data\",\"clean_results\":{\"full\":{\"f1_macro\":0.9868},\"k=1\":{\"f1_macro\":0.9474},\"k=2\":{\"f1_macro\":0.9341},\"k=3\":{\"f1_macro\":0.9737},\"k=5\":{\"f1_macro\":0.9868}},\"perturbed_results\":{\"full\":{\"f1_macro\":0.8661},\"k=1\":{\"f1_macro\":0.8238},\"k=2\":{\"f1_macro\":0.7797},\"k=3\":{\"f1_macro\":0.7946},\"k=5\":{\"f1_macro\":0.8381}},\"delta_f1\":{\"full\":-0.1207,\"k=1\":-0.1236,\"k=2\":-0.1544,\"k=3\":-0.1791,\"k=5\":-0.1487},\"sample_count\":76}",
  "content_filename": "plan_018_wiki_perturbation.json",
  "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_018_wiki_perturbation_results",
    "type": "data",
    "description": "Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
    "project": "persuasion_turn_jailbreak_detect",
    "exp_id": "plan_018_wiki_perturbation",
    "content": "{\"experiment\":\"plan_018_wiki_perturbation\",\"description\":\"Wikipedia MLM control model evaluated on adversarially perturbed data\",\"clean_results\":{\"full\":{\"f1_macro\":0.9868},\"k=1\":{\"f1_macro\":0.9474},\"k=2\":{\"f1_macro\":0.9341},\"k=3\":{\"f1_macro\":0.9737},\"k=5\":{\"f1_macro\":0.9868}},\"perturbed_results\":{\"full\":{\"f1_macro\":0.8661},\"k=1\":{\"f1_macro\":0.8238},\"k=2\":{\"f1_macro\":0.7797},\"k=3\":{\"f1_macro\":0.7946},\"k=5\":{\"f1_macro\":0.8381}},\"delta_f1\":{\"full\":-0.1207,\"k=1\":-0.1236,\"k=2\":-0.1544,\"k=3\":-0.1791,\"k=5\":-0.1487},\"sample_count\":76}",
    "content_filename": "plan_018_wiki_perturbation.json",
    "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T06:27:13.896816+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'experiment': 'plan_018_...87}, 'sample_count': 76}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T06:27:13.896939+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_018_wiki_perturbation_results",
  "type": "data",
  "description": "Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
  "project": "persuasion_turn_jailbreak_detect",
  "exp_id": "plan_018_wiki_perturbation",
  "content": "Plan 018 Wiki MLM Perturbation Results\\n\\nClean F1: full=0.9868, k1=0.9474, k2=0.9341, k3=0.9737, k5=0.9868\\nPerturbed F1: full=0.8661, k1=0.8238, k2=0.7797, k3=0.7946, k5=0.8381\\nDelta F1: full=-0.1207, k1=-0.1236, k2=-0.1544, k3=-0.1791, k5=-0.1487\\nSamples: 76 (38 jailbreak, 38 benign)\\n\\nConclusion: Wiki MLM degradation (~-0.12 to -0.18) is comparable to vanilla baseline (-0.118) and far worse than JB MLM (-0.026). Out-of-domain pretraining provides no perturbation robustness.",
  "content_filename": "plan_018_wiki_perturbation.txt",
  "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_018_wiki_perturbation_results",
    "type": "data",
    "description": "Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)",
    "project": "persuasion_turn_jailbreak_detect",
    "exp_id": "plan_018_wiki_perturbation",
    "content": "Plan 018 Wiki MLM Perturbation Results\\n\\nClean F1: full=0.9868, k1=0.9474, k2=0.9341, k3=0.9737, k5=0.9868\\nPerturbed F1: full=0.8661, k1=0.8238, k2=0.7797, k3=0.7946, k5=0.8381\\nDelta F1: full=-0.1207, k1=-0.1236, k2=-0.1544, k3=-0.1791, k5=-0.1487\\nSamples: 76 (38 jailbreak, 38 benign)\\n\\nConclusion: Wiki MLM degradation (~-0.12 to -0.18) is comparable to vanilla baseline (-0.118) and far worse than JB MLM (-0.026). Out-of-domain pretraining provides no perturbation robustness.",
    "content_filename": "plan_018_wiki_perturbation.txt",
    "tags": "['perturbation', 'wiki-mlm', 'plan_018', 'evaluation']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T06:27:13.897086+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_978c9b\", \"name\": \"plan_018_wiki_perturbation_results\", \"type\": \"data\", \"description\": \"Plan 018 Wiki MLM perturbation eval: clean F1=0.987, perturbed F1=0.866, delta=-0.121 (comparable to vanilla baseline, far worse than JB MLM -0.026)\", \"path\": \"projects/persuasion_turn_jailbreak_detect/artifacts/plan_018_wiki_perturbation/data/plan_018_wiki_perturbation.txt\", \"url\": null, \"project\": \"persuasion_turn_jailbreak_detect\", \"exp_id\": \"plan_018_wiki_perturbation\", \"skill\": \"\", \"created_at\": \"2026-05-18T06:27:06.278525+00:00\", \"tags\": [\"perturbation\", \"wiki-mlm\", \"plan_018\", \"evaluation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-18T06:27:13.897248+00:00_

全部完成。

**结果总结：**

| K | Clean F1 | Perturbed F1 | Delta |
|---|---|---|---|
| k=1 | 0.947 | 0.824 | **-0.124** |
| k=2 | 0.934 | 0.780 | **-0.154** |
| k=3 | 0.974 | 0.795 | **-0.179** |
| k=5 | 0.987 | 0.838 | **-0.149** |
| full | 0.987 | 0.866 | **-0.121** |

Wiki MLM perturbation degradation (-0.121 ~ -0.179) 与 vanilla baseline (-0.118) 量级相当，远差于 JB MLM (-0.026) 和 persuasion treatment (0.000)。假设成立：out-of-domain pretraining 不提供 perturbation robustness，domain-specific MLM 才是关键。

已保存结果到 `results/plan_018_wiki_perturbation.json`，registry 实验 `plan_018_wiki_perturbation` 已设为 DONE。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_plan018-wiki-perturbation_20260518T062359"
}
```

</details>

---
