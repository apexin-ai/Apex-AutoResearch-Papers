# code exp015 rerun script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_code_exp015-rerun-script_20260514T030213.jsonl`
- **Structured JSON:** [`7be3173b2a34f3310b03.json`](../../sessions/7b/7be3173b2a34f3310b03.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-14T03:07:59.821401+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T03:07:59.821747+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T03:07:59.821946+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T03:07:59.822211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-015: Neural Probe for Generational Depth Classification\\n\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import DataLoader, TensorDataset\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\n# ── Data loading ──────────────────────────────────────────────────────\\n\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\n    \\\"\\\"\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\"\\\"\\\"\\n    texts, depths, doc_ids = [], [], []\\n    for d in range(max_depth + 1):\\n        path = data_dir / f\\\"depth_{d}.jsonl\\\"\\n        if not path.exists():\\n            log.warning(f\\\"Missing {path}, skipping depth {d}\\\")\\n            continue\\n        count = 0\\n        with open(path) as f:\\n            for line in f:\\n                if num_samples is not None and count >= num_samples:\\n                    break\\n                rec = json.loads(line)\\n                texts.append(rec[\\\"text\\\"])\\n                depths.append(d)\\n                doc_ids.append(rec[\\\"doc_id\\\"])\\n                count += 1\\n        log.info(f\\\"  depth {d}: {count} samples\\\")\\n    return texts, np.array(depths), np.array(doc_ids)\\n\\n\\n# ── Embedding extraction ────────────────────────────────────────
…[truncated 7128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T03:07:59.822406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "wc -l /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "wc -l /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T03:07:59.822538+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "head -200 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "head -200 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T03:07:59.822676+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"400 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T03:07:59.822909+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-015: Neural Probe for Generational Depth Classification\\n\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import DataLoader, TensorDataset\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\n# ── Data loading ──────────────────────────────────────────────────────\\n\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\n    \\\"\\\"\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\"\\\"\\\"\\n    texts, depths, doc_ids = [], [], []\\n    for d in range(max_depth + 1):\\n        path = data_dir / f\\\"depth_{d}.jsonl\\\"\\n        if not path.exists():\\n            log.warning(f\\\"Missing {path}, skipping depth {d}\\\")\\n            continue\\n        count = 0\\n        with open(path) as f:\\n            for line in f:\\n                if num_samples is not None and count >= num_samples:\\n                    break\\n                rec = json.loads(line)\\n                texts.append(rec[\\\"text\\\"])\\n                depths.append(d)\\n                doc_ids.append(rec[\\\"doc_id\\\"])\\n                count += 1\\n        log.info(f\\\"  depth {d}: {count} samples\\\")\\n    return texts, np.array(depths), np.array(doc_ids)\\n\\n\\n# ── Embedding extraction ────────────────────────────────────────
…[truncated 5307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T03:07:59.823072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "tail -n +200 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "tail -n +200 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T03:07:59.823334+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    fold_adj_aucs = {f\\\"{k-1}v{k}\\\": [] for k in range(1, num_classes)}\\n\\n    for fold, (tr_idx, te_idx) in enumerate(\\n        gkf.split(embeddings, depths, groups=doc_ids)\\n    ):\\n        log.info(f\\\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\\\")\\n        mlp = train_mlp(\\n            embeddings[tr_idx], depths[tr_idx],\\n            embeddings[te_idx], depths[te_idx],\\n            input_dim=input_dim, num_classes=num_classes,\\n            epochs=args.epochs, lr=args.lr,\\n            batch_size=args.mlp_batch_size,\\n            patience=args.patience, device=device,\\n        )\\n\\n        with torch.no_grad():\\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\\n\\n        all_probas[te_idx] = probas\\n\\n        # Per-fold adjacent AUC\\n        td = depths[te_idx]\\n        for k in range(1, num_classes):\\n            m = (td == k - 1) | (td == k)\\n            y = (td[m] == k).astype(int)\\n            if len(np.unique(y)) < 2 or m.sum() < 4:\\n                continue\\n            p0 = probas[m, k - 1]\\n            p1 = probas[m, k]\\n            s = p1 / (p0 + p1 + 1e-12)\\n            fold_adj_aucs[f\\\"{k-1}v{k}\\\"].append(round(float(roc_auc_score(y, s)), 4))\\n\\n        del mlp\\n        torch.cuda.empty_cache()\\n\\n    # Overall pairwise AUC\\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\\n\\n    # K*\\n    k_star = 0\\n    for k in range(1, num_classes):\\n        if adj_auc.get(f\\\"{k-1}v{k}\\\", 0) > 0.60:\\n            k_star = k\\n\\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\\n\\n    # Per-fold stats\\n    fold_stats = {}\\n    for key, aucs in fold_adj_aucs.items():\\n        if aucs:\\n            fold_stats[key] = {\\n                \\\"mean\\\": round(float(np.mean(aucs)), 4),\\n 
…[truncated 6475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T03:07:59.823529+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "grep -rn \"bootstrap\\|permutation\\|resample\" /root/autodl-tmp/gen-depth-contamination/scripts/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "grep -rn \"bootstrap\\|permutation\\|resample\" /root/autodl-tmp/gen-depth-contamination/scripts/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T03:07:59.823664+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T03:07:59.823804+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "grep -rn \"bootstrap\" /root/autodl-tmp/gen-depth-contamination/scripts/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "grep -rn \"bootstrap\" /root/autodl-tmp/gen-depth-contamination/scripts/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T03:07:59.823936+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci_exp017.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T03:07:59.824052+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T03:07:59.824259+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Bootstrap 95% CI and permutation test for pairwise AUC.\\n\\nMethod:\\n  1. Compute out-of-fold predictions via GroupKFold(5) + LGBMClassifier (matching original pipeline)\\n  2. Bootstrap CI: resample doc_ids with replacement, compute AUC from OOF predictions (1000x)\\n  3. Permutation test: shuffle labels on OOF predictions, compute AUC (500x)\\n\\\"\\\"\\\"\\n\\nimport csv, json, time\\nimport numpy as np\\nfrom pathlib import Path\\nimport lightgbm as lgb\\nfrom sklearn.model_selection import GroupKFold\\nfrom sklearn.metrics import roc_auc_score\\n\\nFEAT_COLS = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\", \\\"freq_entropy\\\", \\\"low_freq_ratio\\\",\\n]\\n\\nEXPERIMENTS = {\\n    \\\"mvp_001_qwen_rewrite\\\": \\\"data/features.csv\\\",\\n    \\\"exp_001_pythia\\\": \\\"data_exp001_pythia/features.csv\\\",\\n    \\\"exp_002_olmo\\\": \\\"data_exp002_olmo/features.csv\\\",\\n}\\n\\nN_BOOTSTRAP = 1000\\nN_PERMUTATION = 500\\nMAX_DEPTH = 5\\nSEED = 42\\n\\n\\ndef load_features(path):\\n    with open(path) as f:\\n        rows = list(csv.DictReader(f))\\n    depths = np.array([int(r[\\\"depth\\\"]) for r in rows])\\n    doc_ids = np.array([int(r[\\\"doc_id\\\"]) for r in rows])\\n    X = np.array([\\n        [float(r[c]) if r[c] not in (\\\"\\\", \\\"nan\\\") else np.nan for c in FEAT_COLS]\\n        for r in rows\\n    ])\\n    col_means = np.nanmean(X, axis=0)\\n    for j in range(X.shape[1]):\\n        mask = np.isnan(X[:, j])\\n        X[mask, j] = col_means[j]\\n    return depths, doc_ids, X\\n\\n\\ndef oof_predictions(X, y, groups):\\n    preds = np.zeros(len(y))\\n    for tr, te in GroupKFold(5).split(X, y, groups):\\n      
…[truncated 5302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T03:07:59.824512+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    \"\"\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\"\"\"\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Frozen LLM last hidden state -> average pool -> (N, hidden_dim).\n    Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for pairwise AUC via doc-level resampling.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Permutation test: shuffle binary labels, compare AUC distribution.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        # Per-fold adjacent AUC\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline (hand-crafted features + LightGBM)\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all data first (text only, cheap)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    # Log peak VRAM during embedding extraction\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM completely before MLP training\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if torch.cuda.is_available() else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        # Bootstrap CI summary for adjacent pairs\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    \"\"\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\"\"\"\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Frozen LLM last hidden state -> average pool -> (N, hidden_dim).\n    Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Bootstrap 95% CI for pairwise AUC via doc-level resampling.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Permutation test: shuffle binary labels, compare AUC distribution.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        # Per-fold adjacent AUC\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline (hand-crafted features + LightGBM)\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all data first (text only, cheap)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    # Log peak VRAM during embedding extraction\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM completely before MLP training\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if torch.cuda.is_available() else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        # Bootstrap CI summary for adjacent pairs\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T03:07:59.825014+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T03:07:59.825165+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T03:07:59.825289+00:00_

plot_exp003_decoding_ablation.py
run_cross_transfer.py
run_exp003_ablation.sh
run_exp009_dose_response.py
run_exp013_cross_transfer.py
run_exp015_neural_probe.py
run_pipeline.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T03:07:59.825405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T03:07:59.825635+00:00_

1	"""
2	exp-015: Neural Probe for Generational Depth Classification
3	
4	Validates that K*=2 (found with 15D hand-crafted features + LightGBM) is
5	data-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B
6	embeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.
7	"""
8	
9	import argparse
10	import json
11	import logging
12	import os
13	import sys
14	from pathlib import Path
15	
16	import numpy as np
17	import torch
18	import torch.nn as nn
19	from torch.utils.data import DataLoader, TensorDataset
20	from sklearn.metrics import roc_auc_score
21	from sklearn.model_selection import GroupKFold
22	from tqdm import tqdm
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	    datefmt="%H:%M:%S",
28	)
29	log = logging.getLogger(__name__)
30	
31	
32	# ── Data loading ──────────────────────────────────────────────────────
33	
34	def load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):
35	    """Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids."""
36	    texts, depths, doc_ids = [], [], []
37	    for d in range(max_depth + 1):
38	        path = data_dir / f"depth_{d}.jsonl"
39	        if not path.exists():
40	            log.warning(f"Missing {path}, skipping depth {d}")
41	            continue
42	        count = 0
43	        with open(path) as f:
44	            for line in f:
45	                if num_samples is not None and count >= num_samples:
46	                    break
47	                rec = json.loads(line)
48	                texts.append(rec["text"])
49	                depths.append(d)
50	                doc_ids.append(rec["doc_id"])
51	                count += 1
52	        log.info(f"  depth {d}: {count} samples")
53	    return texts, np.array(depths), np.array(doc_ids)
54	
55	
56	# ── Embedding extraction ─────────────────────────────────────────────
57	
58	@torch.no_grad()
59	def extract_embeddings(model, tokenizer, texts, batc
…[truncated 13304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T03:07:59.825971+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all text data (cheap, CPU only)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    embed_peak = None\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM before MLP training — this is the key memory optimization\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all text data (cheap, CPU only)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    embed_peak = None\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM before MLP training — this is the key memory optimization\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T03:07:59.826690+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T03:07:59.826938+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py | wc -l"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T03:07:59.827088+00:00_

570

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T03:07:59.827211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T03:07:59.827556+00:00_

1	"""
2	exp-015: Neural Probe for Generational Depth Classification
3	
4	Validates that K*=2 (found with 15D hand-crafted features + LightGBM) is
5	data-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B
6	embeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.
7	
8	v2 changes: memory-optimized (extract all embeddings then free LLM),
9	bootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.
10	"""
11	
12	import argparse
13	import gc
14	import json
15	import logging
16	import sys
17	import time
18	from pathlib import Path
19	
20	import numpy as np
21	import torch
22	import torch.nn as nn
23	from torch.utils.data import DataLoader, TensorDataset
24	from sklearn.metrics import roc_auc_score
25	from sklearn.model_selection import GroupKFold
26	from tqdm import tqdm
27	
28	logging.basicConfig(
29	    level=logging.INFO,
30	    format="%(asctime)s [%(levelname)s] %(message)s",
31	    datefmt="%H:%M:%S",
32	)
33	log = logging.getLogger(__name__)
34	
35	
36	# -- Data loading ------------------------------------------------------
37	
38	def load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):
39	    texts, depths, doc_ids = [], [], []
40	    for d in range(max_depth + 1):
41	        path = data_dir / f"depth_{d}.jsonl"
42	        if not path.exists():
43	            log.warning(f"Missing {path}, skipping depth {d}")
44	            continue
45	        count = 0
46	        with open(path) as f:
47	            for line in f:
48	                if num_samples is not None and count >= num_samples:
49	                    break
50	                rec = json.loads(line)
51	                texts.append(rec["text"])
52	                depths.append(d)
53	                doc_ids.append(rec["doc_id"])
54	                count += 1
55	        log.info(f"  depth {d}: {count} samples")
56	    return texts, np.array(depths), np.array(doc_ids)
57	
58	
59	# -- Embedding extraction with OOM retry ------------------------
…[truncated 20652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T03:07:59.827854+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westc-26893",
  "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py << 'SCRIPT_EOF'\n\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all text data (cheap, CPU only)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    embed_peak = None\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM before MLP training — this is the key memory optimization\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westc-26893",
    "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py << 'SCRIPT_EOF'\n\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all text data (cheap, CPU only)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    embed_peak = None\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM before MLP training — this is the key memory optimization\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T03:07:59.828222+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T03:07:59.828360+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westc-26893",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_exp015_neural_probe.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westc-26893",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_exp015_neural_probe.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T03:07:59.828505+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: run_exp015_neural_probe.py [-h] [--model_path MODEL_PATH]\\n                                  [--data_dir DATA_DIR [DATA_DIR ...]]\\n                                  [--label LABEL [LABEL ...]]\\n                                  [--output OUTPUT]\\n                                  [--num_samples NUM_SAMPLES]\\n                                  [--max_depth MAX_DEPTH]\\n                                  [--embed_batch_size EMBED_BATCH_SIZE]\\n                                  [--max_length MAX_LENGTH]\\n                                  [--mlp_batch_size MLP_BATCH_SIZE]\\n                                  [--epochs EPOCHS] [--lr LR]\\n                                  [--patience PATIENCE] [--device DEVICE]\\n                                  [--bootstrap_resamples BOOTSTRAP_RESAMPLES]\\n                                  [--permutation_resamples PERMUTATION_RESAMPLES]\\n\\nexp-015: Neural Probe for depth classification (frozen LLM + MLP)\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_path MODEL_PATH\\n  --data_dir DATA_DIR [DATA_DIR ...]\\n  --label LABEL [LABEL ...]\\n  --output OUTPUT\\n  --num_samples NUM_SAMPLES\\n                        Max samples per depth (default: all)\\n  --max_depth MAX_DEPTH\\n  --embed_batch_size EMBED_BATCH_SIZE\\n  --max_length MAX_LENGTH\\n  --mlp_batch_size MLP_BATCH_SIZE\\n  --epochs EPOCHS\\n  --lr LR\\n  --patience PATIENCE\\n  --device DEVICE\\n  --bootstrap_resamples BOOTSTRAP_RESAMPLES\\n  --permutation_resamples PERMUTATION_RESAMPLES\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.81}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T03:07:59.828661+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westc-26893",
  "command": "wc -l /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westc-26893",
    "command": "wc -l /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T03:07:59.828817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"570 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp015-rerun-script_20260514T030213",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T03:07:59.829011+00:00_

dry-run 通过，参数解析正确。汇报：

**脚本路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py` (570行，本地+服务器同步)

**新增功能**:

| # | 功能 | 实现方式 |
|---|------|---------|
| 1 | 内存优化 | 三阶段流水线：Phase 1 加载文本 → Phase 2 加载 LLM 提取全部 embeddings → `del llm; gc.collect(); torch.cuda.empty_cache()` → Phase 3 训练 MLP（LLM 已释放） |
| 2 | OOM 自适应 batch | `extract_embeddings` 捕获 `torch.cuda.OutOfMemoryError`，自动减半 batch_size（最小=1），记录实际使用的 batch size |
| 3 | Bootstrap 95% CI | doc-level percentile bootstrap（1000 resamples），对所有 adjacent pairs 计算，输出 `{auc, ci_lower, ci_upper, boot_std}` |
| 4 | Permutation test | 500 permutations，shuffle binary labels，报告 p-value，覆盖全部 adjacent pairs |
| 5 | Peak VRAM logging | 每个 fold 前 `reset_peak_memory_stats()`，fold 后 `max_memory_allocated()` 记录；另外记录 embedding extraction 阶段的 peak VRAM |

**新增参数**: `--bootstrap_resamples 1000` `--permutation_resamples 500`

**命令行兼容**:
```bash
python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 16 \
  --data_dir data_exp001_pythia data_exp002_olmo data_exp017_qwen_cont \
  --label Pythia OLMo Qwen-cont
```

**预估 Peak VRAM**:
- Embedding extraction: Qwen2.5-1.5B fp16 ~3GB model + batch_size=16×max_length=512 的 KV cache/activations ≈ **5-7 GB**
- MLP training (LLM 已释放): MLP <10MB + embeddings in CPU numpy，GPU 仅放 MLP 参数+mini-batch ≈ **<500 MB**
- 总计 peak ≈ **5-7 GB**，24GB RTX 4090D 独占时绰绰有余

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp015-rerun-script_20260514T030213"
}
```

</details>

---
