# code exp015 rerun script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_code_exp015-rerun-script_20260514T030213.log`
- **Structured JSON:** [`e3a889c2ea2b3b88a4b8.json`](../../sessions/e3/e3a889c2ea2b3b88a4b8.json)

## Before a recorded user message

50 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "5f246225-14a2-41ab-b6d0-4769b733a9af",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778745000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aaef34a3-3c25-4299-b7ff-7169cd3fcc3d",
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing script on the server, then modify it locally and push it back.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "6e2a8e14-943b-4f36-b41f-4ff84a9cd82c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6Cpgo1F88SaRXNT5U5GvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11855
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

先读取服务器上的现有脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "772f4720-7a8a-4a96-80cf-a8c446041e30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6Cpgo1F88SaRXNT5U5GvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11855
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MNBLycPDHZPPBFDuejR8SN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "6c41ff68-827a-4de5-9159-d206d25dcafa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6Cpgo1F88SaRXNT5U5GvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11855,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11855
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T03:02:27.569Z_

<details><summary>↩ Tool result · `toolu_01MNBLycPDHZPPBFDuejR8SN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "5587b2be-a8d6-4d6a-b173-4e92060aad05",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NcsqzsptmnHUDZVBnFfWfG`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "dff12687-d0ec-4b5a-b329-498472fc1ab8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uhNpYrrUmsxh8n4rdeaen",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 23696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 923
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T03:02:33.066Z_

<details><summary>↩ Tool result · `toolu_01NcsqzsptmnHUDZVBnFfWfG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-015: Neural Probe for Generational Depth Classification\\n\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import DataLoader, TensorDataset\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\n# ── Data loading ──────────────────────────────────────────────────────\\n\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\n    \\\"\\\"\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\"\\\"\\\"\\n    texts, depths, doc_ids = [], [], []\\n    for d in range(max_depth + 1):\\n        path = data_dir / f\\\"depth_{d}.jsonl\\\"\\n        if not path.exists():\\n            log.warning(f\\\"Missing {path}, skipping depth {d}\\\")\\n            continue\\n        count = 0\\n        with open(path) as f:\\n            for line in f:\\n                if num_samples is not None and count >= num_samples:\\n                    break\\n                rec = json.loads(line)\\n                texts.append(rec[\\\"text\\\"])\\n                depths.append(d)\\n                doc_ids.append(rec[\\\"doc_id\\\"])\\n                count += 1\\n        log.info(f\\\"  depth {d}: {count} samples\\\")\\n    return texts, np.array(depths), np.array(doc_ids)\\n\\n\\n# ── Embedding extraction ─────────────────────────────────────────────\\n\\n@torch.no_grad()\\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\\n    \\\"\\\"\\\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\\\"\\\"\\\"\\n    all_emb = []\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\"Embedding\\\"):\\n        batch = texts[i : i + batch_size]\\n        inputs = tokenizer(\\n            batch,\\n            return_tensors=\\\"pt\\\",\\n            padding=True,\\n            truncation=True,\\n            max_length=max_length,\\n        ).to(model.device)\\n\\n        out = model(**inputs, output_hidden_states=True)\\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\\n        mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1).float()\\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\\n        all_emb.append(pooled.cpu().float().numpy())\\n\\n    return np.concatenate(all_emb, axis=0)\\n\\n\\n# ── MLP ───────────────────────────────────────────────────────────────\\n\\nclass DepthMLP(nn.Module):\\n    def __init__(self, input_dim=1536, num_classes=6):\\n        super().__init__()\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, 512),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(512, 256),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(256, num_classes),\\n        )\\n\\n    def forward(self, x):\\n        return self.net(x)\\n\\n\\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\\\"cuda\\\"):\\n    \\\"\\\"\\\"Train MLP with early stopping. Returns best model in eval mode.\\\"\\\"\\\"\\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\\n    criterion = nn.CrossEntropyLoss()\\n\\n    ds = TensorDataset(\\n        torch.tensor(X_train, dtype=torch.float32),\\n        torch.tensor(y_train, dtype=torch.long),\\n    )\\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\\n\\n    best_loss = float(\\\"inf\\\")\\n    best_state = None\\n    wait = 0\\n\\n    for epoch in range(epochs):\\n        model.train()\\n        for xb, yb in loade\\n\\n... [截断: 输出过长，省略 5810 字符] ...\\n\\nv{k}\\\"\\n        a = adj_auc.get(key, \\\"N/A\\\")\\n        fs = fold_stats.get(key, {})\\n        std = fs.get(\\\"std\\\", 0)\\n        base = baseline[\\\"mean\\\"].get(key, \\\"—\\\") if baseline else \\\"—\\\"\\n        log.info(f\\\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\\\")\\n\\n    return result\\n\\n\\n# ── Main ──────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\",\\n    )\\n    parser.add_argument(\\n        \\\"--model_path\\\", type=str,\\n        default=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\\\",\\n    )\\n    parser.add_argument(\\\"--data_dir\\\", type=str, nargs=\\\"+\\\",\\n                        default=[\\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\"])\\n    parser.add_argument(\\\"--label\\\", type=str, nargs=\\\"+\\\", default=[\\\"Qwen-cont\\\"])\\n    parser.add_argument(\\n        \\\"--output\\\", type=str,\\n        default=\\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\",\\n    )\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=None,\\n                        help=\\\"Max samples per depth (default: all)\\\")\\n    parser.add_argument(\\\"--max_depth\\\", type=int, default=5)\\n    parser.add_argument(\\\"--embed_batch_size\\\", type=int, default=24)\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512)\\n    parser.add_argument(\\\"--mlp_batch_size\\\", type=int, default=256)\\n    parser.add_argument(\\\"--epochs\\\", type=int, default=20)\\n    parser.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    parser.add_argument(\\\"--patience\\\", type=int, default=5)\\n    parser.add_argument(\\\"--device\\\", type=str, default=\\\"cuda:0\\\")\\n    args = parser.parse_args()\\n\\n    if len(args.data_dir) != len(args.label):\\n        log.error(\\\"--data_dir and --label must have the same number of entries\\\")\\n        sys.exit(1)\\n\\n    device = args.device if torch.cuda.is_available() else \\\"cpu\\\"\\n    log.info(f\\\"Device: {device}\\\")\\n    if torch.cuda.is_available():\\n        props = torch.cuda.get_device_properties(0)\\n        log.info(f\\\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\\\")\\n\\n    # Load LLM once for all datasets\\n    from transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n    log.info(f\\\"Loading model from {args.model_path} ...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n        tokenizer.pad_token_id = tokenizer.eos_token_id\\n    tokenizer.padding_side = \\\"right\\\"\\n\\n    llm = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch.float16,\\n        device_map=\\\"auto\\\",\\n        trust_remote_code=True,\\n    )\\n    llm.eval()\\n    log.info(\\\"Model loaded.\\\")\\n\\n    # Run per-dataset\\n    all_results = []\\n    for dd, lab in zip(args.data_dir, args.label):\\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\\n        if r:\\n            all_results.append(r)\\n\\n    # Free LLM\\n    del llm\\n    torch.cuda.empty_cache()\\n\\n    # Save\\n    out = Path(args.output)\\n    out.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\\n    log.info(f\\\"\\\\nResults → {out}\\\")\\n\\n    # Final summary\\n    log.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    log.info(\\\"SUMMARY\\\")\\n    log.info(\\\"=\\\" * 60)\\n    for r in all_results:\\n        np_ks = r[\\\"neural_probe\\\"][\\\"k_star\\\"]\\n        base_ks = r.get(\\\"lgbm_baseline\\\", {}).get(\\\"k_star\\\", \\\"—\\\")\\n        log.info(f\\\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\\\")\\n\\n    k_stars = [r[\\\"neural_probe\\\"][\\\"k_star\\\"] for r in all_results]\\n    if len(k_stars) > 1:\\n        if all(k == k_stars[0] for k in k_stars):\\n            log.info(f\\\"\\\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\\\")\\n        else:\\n            log.info(f\\\"\\\\n  K* varies: {k_stars}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.16}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "2c0ab62f-b737-4599-9312-8838143fecc5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nexp-015: Neural Probe for Generational Depth Classification\\\\n\\\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nfrom pathlib import Path\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn as nn\\\\nfrom torch.utils.data import DataLoader, TensorDataset\\\\nfrom sklearn.metrics import roc_auc_score\\\\nfrom sklearn.model_selection import GroupKFold\\\\nfrom tqdm import tqdm\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\n\\\\n# ── Data loading ──────────────────────────────────────────────────────\\\\n\\\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    texts, depths, doc_ids = [], [], []\\\\n    for d in range(max_depth + 1):\\\\n        path = data_dir / f\\\\\\\"depth_{d}.jsonl\\\\\\\"\\\\n        if not path.exists():\\\\n            log.warning(f\\\\\\\"Missing {path}, skipping depth {d}\\\\\\\")\\\\n            continue\\\\n        count = 0\\\\n        with open(path) as f:\\\\n            for line in f:\\\\n                if num_samples is not None and count >= num_samples:\\\\n                    break\\\\n                rec = json.loads(line)\\\\n                texts.append(rec[\\\\\\\"text\\\\\\\"])\\\\n                depths.append(d)\\\\n                doc_ids.append(rec[\\\\\\\"doc_id\\\\\\\"])\\\\n                count += 1\\\\n        log.info(f\\\\\\\"  depth {d}: {count} samples\\\\\\\")\\\\n    return texts, np.array(depths), np.array(doc_ids)\\\\n\\\\n\\\\n# ── Embedding extraction ─────────────────────────────────────────────\\\\n\\\\n@torch.no_grad()\\\\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    all_emb = []\\\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\\\\\"Embedding\\\\\\\"):\\\\n        batch = texts[i : i + batch_size]\\\\n        inputs = tokenizer(\\\\n            batch,\\\\n            return_tensors=\\\\\\\"pt\\\\\\\",\\\\n            padding=True,\\\\n            truncation=True,\\\\n            max_length=max_length,\\\\n        ).to(model.device)\\\\n\\\\n        out = model(**inputs, output_hidden_states=True)\\\\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\\\\n        mask = inputs[\\\\\\\"attention_mask\\\\\\\"].unsqueeze(-1).float()\\\\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\\\\n        all_emb.append(pooled.cpu().float().numpy())\\\\n\\\\n    return np.concatenate(all_emb, axis=0)\\\\n\\\\n\\\\n# ── MLP ───────────────────────────────────────────────────────────────\\\\n\\\\nclass DepthMLP(nn.Module):\\\\n    def __init__(self, input_dim=1536, num_classes=6):\\\\n        super().__init__()\\\\n        self.net = nn.Sequential(\\\\n            nn.Linear(input_dim, 512),\\\\n            nn.ReLU(),\\\\n            nn.Dropout(0.1),\\\\n            nn.Linear(512, 256),\\\\n            nn.ReLU(),\\\\n            nn.Dropout(0.1),\\\\n            nn.Linear(256, num_classes),\\\\n        )\\\\n\\\\n    def forward(self, x):\\\\n        return self.net(x)\\\\n\\\\n\\\\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\\\\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\\\\\\\"cuda\\\\\\\"):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Train MLP with early stopping. Returns best model in eval mode.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\\\\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\\\\n    criterion = nn.CrossEntropyLoss()\\\\n\\\\n    ds = TensorDataset(\\\\n        torch.tensor(X_train, dtype=torch.float32),\\\\n        torch.tensor(y_train, dtype=torch.long),\\\\n    )\\\\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\\\\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\\\\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\\\\n\\\\n    best_loss = float(\\\\\\\"inf\\\\\\\")\\\\n    best_state = None\\\\n    wait = 0\\\\n\\\\n    for epoch in range(epochs):\\\\n        model.train()\\\\n        for xb, yb in loade\\\\n\\\\n... [截断: 输出过长，省略 5810 字符] ...\\\\n\\\\nv{k}\\\\\\\"\\\\n        a = adj_auc.get(key, \\\\\\\"N/A\\\\\\\")\\\\n        fs = fold_stats.get(key, {})\\\\n        std = fs.get(\\\\\\\"std\\\\\\\", 0)\\\\n        base = baseline[\\\\\\\"mean\\\\\\\"].get(key, \\\\\\\"—\\\\\\\") if baseline else \\\\\\\"—\\\\\\\"\\\\n        log.info(f\\\\\\\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\\\\\\\")\\\\n\\\\n    return result\\\\n\\\\n\\\\n# ── Main ──────────────────────────────────────────────────────────────\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\\\\\",\\\\n    )\\\\n    parser.add_argument(\\\\n        \\\\\\\"--model_path\\\\\\\", type=str,\\\\n        default=\\\\\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\\\\\\\",\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--data_dir\\\\\\\", type=str, nargs=\\\\\\\"+\\\\\\\",\\\\n                        default=[\\\\\\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\\\\\"])\\\\n    parser.add_argument(\\\\\\\"--label\\\\\\\", type=str, nargs=\\\\\\\"+\\\\\\\", default=[\\\\\\\"Qwen-cont\\\\\\\"])\\\\n    parser.add_argument(\\\\n        \\\\\\\"--output\\\\\\\", type=str,\\\\n        default=\\\\\\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\\\\\",\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--num_samples\\\\\\\", type=int, default=None,\\\\n                        help=\\\\\\\"Max samples per depth (default: all)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_depth\\\\\\\", type=int, default=5)\\\\n    parser.add_argument(\\\\\\\"--embed_batch_size\\\\\\\", type=int, default=24)\\\\n    parser.add_argument(\\\\\\\"--max_length\\\\\\\", type=int, default=512)\\\\n    parser.add_argument(\\\\\\\"--mlp_batch_size\\\\\\\", type=int, default=256)\\\\n    parser.add_argument(\\\\\\\"--epochs\\\\\\\", type=int, default=20)\\\\n    parser.add_argument(\\\\\\\"--lr\\\\\\\", type=float, default=1e-3)\\\\n    parser.add_argument(\\\\\\\"--patience\\\\\\\", type=int, default=5)\\\\n    parser.add_argument(\\\\\\\"--device\\\\\\\", type=str, default=\\\\\\\"cuda:0\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    if len(args.data_dir) != len(args.label):\\\\n        log.error(\\\\\\\"--data_dir and --label must have the same number of entries\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = args.device if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\"\\\\n    log.info(f\\\\\\\"Device: {device}\\\\\\\")\\\\n    if torch.cuda.is_available():\\\\n        props = torch.cuda.get_device_properties(0)\\\\n        log.info(f\\\\\\\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\\\\\\\")\\\\n\\\\n    # Load LLM once for all datasets\\\\n    from transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\n    log.info(f\\\\\\\"Loading model from {args.model_path} ...\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\\\n    if tokenizer.pad_token is None:\\\\n        tokenizer.pad_token = tokenizer.eos_token\\\\n        tokenizer.pad_token_id = tokenizer.eos_token_id\\\\n    tokenizer.padding_side = \\\\\\\"right\\\\\\\"\\\\n\\\\n    llm = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_path,\\\\n        torch_dtype=torch.float16,\\\\n        device_map=\\\\\\\"auto\\\\\\\",\\\\n        trust_remote_code=True,\\\\n    )\\\\n    llm.eval()\\\\n    log.info(\\\\\\\"Model loaded.\\\\\\\")\\\\n\\\\n    # Run per-dataset\\\\n    all_results = []\\\\n    for dd, lab in zip(args.data_dir, args.label):\\\\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\\\\n        if r:\\\\n            all_results.append(r)\\\\n\\\\n    # Free LLM\\\\n    del llm\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    # Save\\\\n    out = Path(args.output)\\\\n    out.parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(out, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\\\\n    log.info(f\\\\\\\"\\\\\\\\nResults → {out}\\\\\\\")\\\\n\\\\n    # Final summary\\\\n    log.info(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 60)\\\\n    log.info(\\\\\\\"SUMMARY\\\\\\\")\\\\n    log.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    for r in all_results:\\\\n        np_ks = r[\\\\\\\"neural_probe\\\\\\\"][\\\\\\\"k_star\\\\\\\"]\\\\n        base_ks = r.get(\\\\\\\"lgbm_baseline\\\\\\\", {}).get(\\\\\\\"k_star\\\\\\\", \\\\\\\"—\\\\\\\")\\\\n        log.info(f\\\\\\\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\\\\\\\")\\\\n\\\\n    k_stars = [r[\\\\\\\"neural_probe\\\\\\\"][\\\\\\\"k_star\\\\\\\"] for r in all_results]\\\\n    if len(k_stars) > 1:\\\\n        if all(k == k_stars[0] for k in k_stars):\\\\n            log.info(f\\\\\\\"\\\\\\\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\\\\\\\")\\\\n        else:\\\\n            log.info(f\\\\\\\"\\\\\\\\n  K* varies: {k_stars}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.16}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-015: Neural Probe for Generational Depth Classification\\n\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import DataLoader, TensorDataset\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\n# ── Data loading ──────────────────────────────────────────────────────\\n\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\n    \\\"\\\"\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\"\\\"\\\"\\n    texts, depths, doc_ids = [], [], []\\n    for d in range(max_depth + 1):\\n        path = data_dir / f\\\"depth_{d}.jsonl\\\"\\n        if not path.exists():\\n            log.warning(f\\\"Missing {path}, skipping depth {d}\\\")\\n            continue\\n        count = 0\\n        with open(path) as f:\\n            for line in f:\\n                if num_samples is not None and count >= num_samples:\\n                    break\\n                rec = json.loads(line)\\n                texts.append(rec[\\\"text\\\"])\\n                depths.append(d)\\n                doc_ids.append(rec[\\\"doc_id\\\"])\\n                count += 1\\n        log.info(f\\\"  depth {d}: {count} samples\\\")\\n    return texts, np.array(depths), np.array(doc_ids)\\n\\n\\n# ── Embedding extraction ─────────────────────────────────────────────\\n\\n@torch.no_grad()\\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\\n    \\\"\\\"\\\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\\\"\\\"\\\"\\n    all_emb = []\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\"Embedding\\\"):\\n        batch = texts[i : i + batch_size]\\n        inputs = tokenizer(\\n            batch,\\n            return_tensors=\\\"pt\\\",\\n            padding=True,\\n            truncation=True,\\n            max_length=max_length,\\n        ).to(model.device)\\n\\n        out = model(**inputs, output_hidden_states=True)\\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\\n        mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1).float()\\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\\n        all_emb.append(pooled.cpu().float().numpy())\\n\\n    return np.concatenate(all_emb, axis=0)\\n\\n\\n# ── MLP ───────────────────────────────────────────────────────────────\\n\\nclass DepthMLP(nn.Module):\\n    def __init__(self, input_dim=1536, num_classes=6):\\n        super().__init__()\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, 512),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(512, 256),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(256, num_classes),\\n        )\\n\\n    def forward(self, x):\\n        return self.net(x)\\n\\n\\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\\\"cuda\\\"):\\n    \\\"\\\"\\\"Train MLP with early stopping. Returns best model in eval mode.\\\"\\\"\\\"\\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\\n    criterion = nn.CrossEntropyLoss()\\n\\n    ds = TensorDataset(\\n        torch.tensor(X_train, dtype=torch.float32),\\n        torch.tensor(y_train, dtype=torch.long),\\n    )\\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\\n\\n    best_loss = float(\\\"inf\\\")\\n    best_state = None\\n    wait = 0\\n\\n    for epoch in range(epochs):\\n        model.train()\\n        for xb, yb in loade\\n\\n... [截断: 输出过长，省略 5810 字符] ...\\n\\nv{k}\\\"\\n        a = adj_auc.get(key, \\\"N/A\\\")\\n        fs = fold_stats.get(key, {})\\n        std = fs.get(\\\"std\\\", 0)\\n        base = baseline[\\\"mean\\\"].get(key, \\\"—\\\") if baseline else \\\"—\\\"\\n        log.info(f\\\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\\\")\\n\\n    return result\\n\\n\\n# ── Main ──────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\",\\n    )\\n    parser.add_argument(\\n        \\\"--model_path\\\", type=str,\\n        default=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\\\",\\n    )\\n    parser.add_argument(\\\"--data_dir\\\", type=str, nargs=\\\"+\\\",\\n                        default=[\\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\"])\\n    parser.add_argument(\\\"--label\\\", type=str, nargs=\\\"+\\\", default=[\\\"Qwen-cont\\\"])\\n    parser.add_argument(\\n        \\\"--output\\\", type=str,\\n        default=\\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\",\\n    )\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=None,\\n                        help=\\\"Max samples per depth (default: all)\\\")\\n    parser.add_argument(\\\"--max_depth\\\", type=int, default=5)\\n    parser.add_argument(\\\"--embed_batch_size\\\", type=int, default=24)\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512)\\n    parser.add_argument(\\\"--mlp_batch_size\\\", type=int, default=256)\\n    parser.add_argument(\\\"--epochs\\\", type=int, default=20)\\n    parser.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    parser.add_argument(\\\"--patience\\\", type=int, default=5)\\n    parser.add_argument(\\\"--device\\\", type=str, default=\\\"cuda:0\\\")\\n    args = parser.parse_args()\\n\\n    if len(args.data_dir) != len(args.label):\\n        log.error(\\\"--data_dir and --label must have the same number of entries\\\")\\n        sys.exit(1)\\n\\n    device = args.device if torch.cuda.is_available() else \\\"cpu\\\"\\n    log.info(f\\\"Device: {device}\\\")\\n    if torch.cuda.is_available():\\n        props = torch.cuda.get_device_properties(0)\\n        log.info(f\\\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\\\")\\n\\n    # Load LLM once for all datasets\\n    from transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n    log.info(f\\\"Loading model from {args.model_path} ...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n        tokenizer.pad_token_id = tokenizer.eos_token_id\\n    tokenizer.padding_side = \\\"right\\\"\\n\\n    llm = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch.float16,\\n        device_map=\\\"auto\\\",\\n        trust_remote_code=True,\\n    )\\n    llm.eval()\\n    log.info(\\\"Model loaded.\\\")\\n\\n    # Run per-dataset\\n    all_results = []\\n    for dd, lab in zip(args.data_dir, args.label):\\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\\n        if r:\\n            all_results.append(r)\\n\\n    # Free LLM\\n    del llm\\n    torch.cuda.empty_cache()\\n\\n    # Save\\n    out = Path(args.output)\\n    out.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\\n    log.info(f\\\"\\\\nResults → {out}\\\")\\n\\n    # Final summary\\n    log.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    log.info(\\\"SUMMARY\\\")\\n    log.info(\\\"=\\\" * 60)\\n    for r in all_results:\\n        np_ks = r[\\\"neural_probe\\\"][\\\"k_star\\\"]\\n        base_ks = r.get(\\\"lgbm_baseline\\\", {}).get(\\\"k_star\\\", \\\"—\\\")\\n        log.info(f\\\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\\\")\\n\\n    k_stars = [r[\\\"neural_probe\\\"][\\\"k_star\\\"] for r in all_results]\\n    if len(k_stars) > 1:\\n        if all(k == k_stars[0] for k in k_stars):\\n            log.info(f\\\"\\\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\\\")\\n        else:\\n            log.info(f\\\"\\\\n  K* varies: {k_stars}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.16}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. Let me get the full file by reading it in sections, particularly the middle part that was cut off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "8082df09-6e07-4515-9e02-ef4f595389cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9oZQaWCQrKEu9fAWDPhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3502,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3502
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 11_

输出被截断了，让我分段读取中间部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "2c8f8e47-086a-4248-9795-8090f1b1871d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9oZQaWCQrKEu9fAWDPhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3502,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3502
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BQne8Mes5GGFB5bMkz4mjR`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "0cf81047-5739-4612-9644-ca42635af365",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9oZQaWCQrKEu9fAWDPhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3502,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3502
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BRqNvnUUTv5RtB5oTPQcvf`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "48ab274b-c5d9-497e-9479-904a214532bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t9oZQaWCQrKEu9fAWDPhY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3502,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3502
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T03:02:38.902Z_

<details><summary>↩ Tool result · `toolu_01BQne8Mes5GGFB5bMkz4mjR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"400 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "560f3d83-8eb2-4e79-b1f7-c147a4c791ec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"400 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"400 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T03:02:39.754Z_

<details><summary>↩ Tool result · `toolu_01BRqNvnUUTv5RtB5oTPQcvf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-015: Neural Probe for Generational Depth Classification\\n\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import DataLoader, TensorDataset\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\n# ── Data loading ──────────────────────────────────────────────────────\\n\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\n    \\\"\\\"\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\"\\\"\\\"\\n    texts, depths, doc_ids = [], [], []\\n    for d in range(max_depth + 1):\\n        path = data_dir / f\\\"depth_{d}.jsonl\\\"\\n        if not path.exists():\\n            log.warning(f\\\"Missing {path}, skipping depth {d}\\\")\\n            continue\\n        count = 0\\n        with open(path) as f:\\n            for line in f:\\n                if num_samples is not None and count >= num_samples:\\n                    break\\n                rec = json.loads(line)\\n                texts.append(rec[\\\"text\\\"])\\n                depths.append(d)\\n                doc_ids.append(rec[\\\"doc_id\\\"])\\n                count += 1\\n        log.info(f\\\"  depth {d}: {count} samples\\\")\\n    return texts, np.array(depths), np.array(doc_ids)\\n\\n\\n# ── Embedding extraction ─────────────────────────────────────────────\\n\\n@torch.no_grad()\\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\\n    \\\"\\\"\\\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\\\"\\\"\\\"\\n    all_emb = []\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\"Embedding\\\"):\\n        batch = texts[i : i + batch_size]\\n        inputs = tokenizer(\\n            batch,\\n            return_tensors=\\\"pt\\\",\\n            padding=True,\\n            truncation=True,\\n            max_length=max_length,\\n        ).to(model.device)\\n\\n        out = model(**inputs, output_hidden_states=True)\\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\\n        mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1).float()\\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\\n        all_emb.append(pooled.cpu().float().numpy())\\n\\n    return np.concatenate(all_emb, axis=0)\\n\\n\\n# ── MLP ───────────────────────────────────────────────────────────────\\n\\nclass DepthMLP(nn.Module):\\n    def __init__(self, input_dim=1536, num_classes=6):\\n        super().__init__()\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, 512),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(512, 256),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(256, num_classes),\\n        )\\n\\n    def forward(self, x):\\n        return self.net(x)\\n\\n\\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\\\"cuda\\\"):\\n    \\\"\\\"\\\"Train MLP with early stopping. Returns best model in eval mode.\\\"\\\"\\\"\\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\\n    criterion = nn.CrossEntropyLoss()\\n\\n    ds = TensorDataset(\\n        torch.tensor(X_train, dtype=torch.float32),\\n        torch.tensor(y_train, dtype=torch.long),\\n    )\\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\\n\\n    best_loss = float(\\\"inf\\\")\\n    best_state = None\\n    wait = 0\\n\\n    for epoch in range(epochs):\\n        model.train()\\n        for xb, yb in loader:\\n            xb, yb = xb.to(device), yb.to(device)\\n            optimizer.zero_grad()\\n            criterion(model(xb), yb).backward()\\n            optimizer.step()\\n\\n        model.eval()\\n        with torch.no_grad():\\n            val_loss = criterion(model(X_val_t), y_val_t).item()\\n\\n        if val_loss < best_loss:\\n            best_loss = val_loss\\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\\n            wait = 0\\n        else:\\n            wait += 1\\n            if wait >= patience:\\n                break\\n\\n    model.load_state_dict(best_state)\\n    model.eval()\\n    return model\\n\\n\\n# ── Pairwise AUC ─────���────────────────────────────────────────────────\\n\\ndef compute_pairwise_auc(probas, depths, max_depth):\\n    \\\"\\\"\\\"Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict).\\\"\\\"\\\"\\n    def _auc_pair(i, j):\\n        mask = (depths == i) | (depths == j)\\n        y = (depths[mask] == j).astype(int)\\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\\n            return float(\\\"nan\\\")\\n        p_i = probas[mask, i]\\n        p_j = probas[mask, j]\\n        score = p_j / (p_i + p_j + 1e-12)\\n        return round(float(roc_auc_score(y, score)), 4)\\n\\n    adjacent = {}\\n    for k in range(1, max_depth + 1):\\n        adjacent[f\\\"{k-1}v{k}\\\"] = _auc_pair(k - 1, k)\\n\\n    all_pairs = {}\\n    for i in range(max_depth + 1):\\n        for j in range(i + 1, max_depth + 1):\\n            all_pairs[f\\\"{i}v{j}\\\"] = _auc_pair(i, j)\\n\\n    return adjacent, all_pairs\\n\\n\\n# ── Single dataset experiment ─────────────────────────────────────────\\n\\ndef run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):\\n    \\\"\\\"\\\"Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC.\\\"\\\"\\\"\\n    log.info(f\\\"\\\\n{'='*60}\\\")\\n    log.info(f\\\"Dataset: {label} ({data_dir})\\\")\\n    log.info(f\\\"{'='*60}\\\")\\n\\n    texts, depths, doc_ids = load_depth_data(\\n        Path(data_dir), args.max_depth, args.num_samples,\\n    )\\n    if len(texts) == 0:\\n        log.error(f\\\"No data in {data_dir}\\\")\\n        return None\\n\\n    num_classes = int(depths.max()) + 1\\n\\n    # Extract embeddings\\n    embeddings = extract_embeddings(\\n        llm_model, tokenizer, texts,\\n        batch_size=args.embed_batch_size,\\n        max_length=args.max_length,\\n    )\\n    input_dim = embeddings.shape[1]\\n    log.info(f\\\"Embeddings: {embeddings.shape}\\\")\\n\\n    # 5-fold GroupKFold CV\\n    gkf = GroupKFold(n_splits=5)\\n    all_probas = np.zeros((len(depths), num_classes))\\n    fold_adj_aucs = {f\\\"{k-1}v{k}\\\": [] for k in range(1, num_classes)}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "a1959f47-7812-4ace-bda8-cda520345149",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nexp-015: Neural Probe for Generational Depth Classification\\\\n\\\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport sys\\\\nfrom pathlib import Path\\\\n\\\\nimport numpy as np\\\\nimport torch\\\\nimport torch.nn as nn\\\\nfrom torch.utils.data import DataLoader, TensorDataset\\\\nfrom sklearn.metrics import roc_auc_score\\\\nfrom sklearn.model_selection import GroupKFold\\\\nfrom tqdm import tqdm\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s [%(levelname)s] %(message)s\\\\\\\",\\\\n    datefmt=\\\\\\\"%H:%M:%S\\\\\\\",\\\\n)\\\\nlog = logging.getLogger(__name__)\\\\n\\\\n\\\\n# ── Data loading ──────────────────────────────────────────────────────\\\\n\\\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    texts, depths, doc_ids = [], [], []\\\\n    for d in range(max_depth + 1):\\\\n        path = data_dir / f\\\\\\\"depth_{d}.jsonl\\\\\\\"\\\\n        if not path.exists():\\\\n            log.warning(f\\\\\\\"Missing {path}, skipping depth {d}\\\\\\\")\\\\n            continue\\\\n        count = 0\\\\n        with open(path) as f:\\\\n            for line in f:\\\\n                if num_samples is not None and count >= num_samples:\\\\n                    break\\\\n                rec = json.loads(line)\\\\n                texts.append(rec[\\\\\\\"text\\\\\\\"])\\\\n                depths.append(d)\\\\n                doc_ids.append(rec[\\\\\\\"doc_id\\\\\\\"])\\\\n                count += 1\\\\n        log.info(f\\\\\\\"  depth {d}: {count} samples\\\\\\\")\\\\n    return texts, np.array(depths), np.array(doc_ids)\\\\n\\\\n\\\\n# ── Embedding extraction ─────────────────────────────────────────────\\\\n\\\\n@torch.no_grad()\\\\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    all_emb = []\\\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\\\\\"Embedding\\\\\\\"):\\\\n        batch = texts[i : i + batch_size]\\\\n        inputs = tokenizer(\\\\n            batch,\\\\n            return_tensors=\\\\\\\"pt\\\\\\\",\\\\n            padding=True,\\\\n            truncation=True,\\\\n            max_length=max_length,\\\\n        ).to(model.device)\\\\n\\\\n        out = model(**inputs, output_hidden_states=True)\\\\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\\\\n        mask = inputs[\\\\\\\"attention_mask\\\\\\\"].unsqueeze(-1).float()\\\\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\\\\n        all_emb.append(pooled.cpu().float().numpy())\\\\n\\\\n    return np.concatenate(all_emb, axis=0)\\\\n\\\\n\\\\n# ── MLP ───────────────────────────────────────────────────────────────\\\\n\\\\nclass DepthMLP(nn.Module):\\\\n    def __init__(self, input_dim=1536, num_classes=6):\\\\n        super().__init__()\\\\n        self.net = nn.Sequential(\\\\n            nn.Linear(input_dim, 512),\\\\n            nn.ReLU(),\\\\n            nn.Dropout(0.1),\\\\n            nn.Linear(512, 256),\\\\n            nn.ReLU(),\\\\n            nn.Dropout(0.1),\\\\n            nn.Linear(256, num_classes),\\\\n        )\\\\n\\\\n    def forward(self, x):\\\\n        return self.net(x)\\\\n\\\\n\\\\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\\\\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\\\\\\\"cuda\\\\\\\"):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Train MLP with early stopping. Returns best model in eval mode.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\\\\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\\\\n    criterion = nn.CrossEntropyLoss()\\\\n\\\\n    ds = TensorDataset(\\\\n        torch.tensor(X_train, dtype=torch.float32),\\\\n        torch.tensor(y_train, dtype=torch.long),\\\\n    )\\\\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\\\\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\\\\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\\\\n\\\\n    best_loss = float(\\\\\\\"inf\\\\\\\")\\\\n    best_state = None\\\\n    wait = 0\\\\n\\\\n    for epoch in range(epochs):\\\\n        model.train()\\\\n        for xb, yb in loader:\\\\n            xb, yb = xb.to(device), yb.to(device)\\\\n            optimizer.zero_grad()\\\\n            criterion(model(xb), yb).backward()\\\\n            optimizer.step()\\\\n\\\\n        model.eval()\\\\n        with torch.no_grad():\\\\n            val_loss = criterion(model(X_val_t), y_val_t).item()\\\\n\\\\n        if val_loss < best_loss:\\\\n            best_loss = val_loss\\\\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\\\\n            wait = 0\\\\n        else:\\\\n            wait += 1\\\\n            if wait >= patience:\\\\n                break\\\\n\\\\n    model.load_state_dict(best_state)\\\\n    model.eval()\\\\n    return model\\\\n\\\\n\\\\n# ── Pairwise AUC ─────���────────────────────────────────────────────────\\\\n\\\\ndef compute_pairwise_auc(probas, depths, max_depth):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    def _auc_pair(i, j):\\\\n        mask = (depths == i) | (depths == j)\\\\n        y = (depths[mask] == j).astype(int)\\\\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\\\\n            return float(\\\\\\\"nan\\\\\\\")\\\\n        p_i = probas[mask, i]\\\\n        p_j = probas[mask, j]\\\\n        score = p_j / (p_i + p_j + 1e-12)\\\\n        return round(float(roc_auc_score(y, score)), 4)\\\\n\\\\n    adjacent = {}\\\\n    for k in range(1, max_depth + 1):\\\\n        adjacent[f\\\\\\\"{k-1}v{k}\\\\\\\"] = _auc_pair(k - 1, k)\\\\n\\\\n    all_pairs = {}\\\\n    for i in range(max_depth + 1):\\\\n        for j in range(i + 1, max_depth + 1):\\\\n            all_pairs[f\\\\\\\"{i}v{j}\\\\\\\"] = _auc_pair(i, j)\\\\n\\\\n    return adjacent, all_pairs\\\\n\\\\n\\\\n# ── Single dataset experiment ─────────────────────────────────────────\\\\n\\\\ndef run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    log.info(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n    log.info(f\\\\\\\"Dataset: {label} ({data_dir})\\\\\\\")\\\\n    log.info(f\\\\\\\"{'='*60}\\\\\\\")\\\\n\\\\n    texts, depths, doc_ids = load_depth_data(\\\\n        Path(data_dir), args.max_depth, args.num_samples,\\\\n    )\\\\n    if len(texts) == 0:\\\\n        log.error(f\\\\\\\"No data in {data_dir}\\\\\\\")\\\\n        return None\\\\n\\\\n    num_classes = int(depths.max()) + 1\\\\n\\\\n    # Extract embeddings\\\\n    embeddings = extract_embeddings(\\\\n        llm_model, tokenizer, texts,\\\\n        batch_size=args.embed_batch_size,\\\\n        max_length=args.max_length,\\\\n    )\\\\n    input_dim = embeddings.shape[1]\\\\n    log.info(f\\\\\\\"Embeddings: {embeddings.shape}\\\\\\\")\\\\n\\\\n    # 5-fold GroupKFold CV\\\\n    gkf = GroupKFold(n_splits=5)\\\\n    all_probas = np.zeros((len(depths), num_classes))\\\\n    fold_adj_aucs = {f\\\\\\\"{k-1}v{k}\\\\\\\": [] for k in range(1, num_classes)}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-015: Neural Probe for Generational Depth Classification\\n\\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn as nn\\nfrom torch.utils.data import DataLoader, TensorDataset\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nfrom tqdm import tqdm\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\n\\n# ── Data loading ──────────────────────────────────────────────────────\\n\\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\\n    \\\"\\\"\\\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\\\"\\\"\\\"\\n    texts, depths, doc_ids = [], [], []\\n    for d in range(max_depth + 1):\\n        path = data_dir / f\\\"depth_{d}.jsonl\\\"\\n        if not path.exists():\\n            log.warning(f\\\"Missing {path}, skipping depth {d}\\\")\\n            continue\\n        count = 0\\n        with open(path) as f:\\n            for line in f:\\n                if num_samples is not None and count >= num_samples:\\n                    break\\n                rec = json.loads(line)\\n                texts.append(rec[\\\"text\\\"])\\n                depths.append(d)\\n                doc_ids.append(rec[\\\"doc_id\\\"])\\n                count += 1\\n        log.info(f\\\"  depth {d}: {count} samples\\\")\\n    return texts, np.array(depths), np.array(doc_ids)\\n\\n\\n# ── Embedding extraction ─────────────────────────────────────────────\\n\\n@torch.no_grad()\\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\\n    \\\"\\\"\\\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\\\"\\\"\\\"\\n    all_emb = []\\n    for i in tqdm(range(0, len(texts), batch_size), desc=\\\"Embedding\\\"):\\n        batch = texts[i : i + batch_size]\\n        inputs = tokenizer(\\n            batch,\\n            return_tensors=\\\"pt\\\",\\n            padding=True,\\n            truncation=True,\\n            max_length=max_length,\\n        ).to(model.device)\\n\\n        out = model(**inputs, output_hidden_states=True)\\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\\n        mask = inputs[\\\"attention_mask\\\"].unsqueeze(-1).float()\\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\\n        all_emb.append(pooled.cpu().float().numpy())\\n\\n    return np.concatenate(all_emb, axis=0)\\n\\n\\n# ── MLP ───────────────────────────────────────────────────────────────\\n\\nclass DepthMLP(nn.Module):\\n    def __init__(self, input_dim=1536, num_classes=6):\\n        super().__init__()\\n        self.net = nn.Sequential(\\n            nn.Linear(input_dim, 512),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(512, 256),\\n            nn.ReLU(),\\n            nn.Dropout(0.1),\\n            nn.Linear(256, num_classes),\\n        )\\n\\n    def forward(self, x):\\n        return self.net(x)\\n\\n\\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\\\"cuda\\\"):\\n    \\\"\\\"\\\"Train MLP with early stopping. Returns best model in eval mode.\\\"\\\"\\\"\\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\\n    criterion = nn.CrossEntropyLoss()\\n\\n    ds = TensorDataset(\\n        torch.tensor(X_train, dtype=torch.float32),\\n        torch.tensor(y_train, dtype=torch.long),\\n    )\\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\\n\\n    best_loss = float(\\\"inf\\\")\\n    best_state = None\\n    wait = 0\\n\\n    for epoch in range(epochs):\\n        model.train()\\n        for xb, yb in loader:\\n            xb, yb = xb.to(device), yb.to(device)\\n            optimizer.zero_grad()\\n            criterion(model(xb), yb).backward()\\n            optimizer.step()\\n\\n        model.eval()\\n        with torch.no_grad():\\n            val_loss = criterion(model(X_val_t), y_val_t).item()\\n\\n        if val_loss < best_loss:\\n            best_loss = val_loss\\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\\n            wait = 0\\n        else:\\n            wait += 1\\n            if wait >= patience:\\n                break\\n\\n    model.load_state_dict(best_state)\\n    model.eval()\\n    return model\\n\\n\\n# ── Pairwise AUC ─────���────────────────────────────────────────────────\\n\\ndef compute_pairwise_auc(probas, depths, max_depth):\\n    \\\"\\\"\\\"Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict).\\\"\\\"\\\"\\n    def _auc_pair(i, j):\\n        mask = (depths == i) | (depths == j)\\n        y = (depths[mask] == j).astype(int)\\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\\n            return float(\\\"nan\\\")\\n        p_i = probas[mask, i]\\n        p_j = probas[mask, j]\\n        score = p_j / (p_i + p_j + 1e-12)\\n        return round(float(roc_auc_score(y, score)), 4)\\n\\n    adjacent = {}\\n    for k in range(1, max_depth + 1):\\n        adjacent[f\\\"{k-1}v{k}\\\"] = _auc_pair(k - 1, k)\\n\\n    all_pairs = {}\\n    for i in range(max_depth + 1):\\n        for j in range(i + 1, max_depth + 1):\\n            all_pairs[f\\\"{i}v{j}\\\"] = _auc_pair(i, j)\\n\\n    return adjacent, all_pairs\\n\\n\\n# ── Single dataset experiment ─────────────────────────────────────────\\n\\ndef run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):\\n    \\\"\\\"\\\"Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC.\\\"\\\"\\\"\\n    log.info(f\\\"\\\\n{'='*60}\\\")\\n    log.info(f\\\"Dataset: {label} ({data_dir})\\\")\\n    log.info(f\\\"{'='*60}\\\")\\n\\n    texts, depths, doc_ids = load_depth_data(\\n        Path(data_dir), args.max_depth, args.num_samples,\\n    )\\n    if len(texts) == 0:\\n        log.error(f\\\"No data in {data_dir}\\\")\\n        return None\\n\\n    num_classes = int(depths.max()) + 1\\n\\n    # Extract embeddings\\n    embeddings = extract_embeddings(\\n        llm_model, tokenizer, texts,\\n        batch_size=args.embed_batch_size,\\n        max_length=args.max_length,\\n    )\\n    input_dim = embeddings.shape[1]\\n    log.info(f\\\"Embeddings: {embeddings.shape}\\\")\\n\\n    # 5-fold GroupKFold CV\\n    gkf = GroupKFold(n_splits=5)\\n    all_probas = np.zeros((len(depths), num_classes))\\n    fold_adj_aucs = {f\\\"{k-1}v{k}\\\": [] for k in range(1, num_classes)}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013R6BhJaXAawiwPAaBPU6jW`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "5e06d8a7-bed9-4323-89a6-e48174111c11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnCcaniBJ549EhyD4Ya4xt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3123,
      "cache_read_input_tokens": 28121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3123
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T03:02:43.490Z_

<details><summary>↩ Tool result · `toolu_013R6BhJaXAawiwPAaBPU6jW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    fold_adj_aucs = {f\\\"{k-1}v{k}\\\": [] for k in range(1, num_classes)}\\n\\n    for fold, (tr_idx, te_idx) in enumerate(\\n        gkf.split(embeddings, depths, groups=doc_ids)\\n    ):\\n        log.info(f\\\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\\\")\\n        mlp = train_mlp(\\n            embeddings[tr_idx], depths[tr_idx],\\n            embeddings[te_idx], depths[te_idx],\\n            input_dim=input_dim, num_classes=num_classes,\\n            epochs=args.epochs, lr=args.lr,\\n            batch_size=args.mlp_batch_size,\\n            patience=args.patience, device=device,\\n        )\\n\\n        with torch.no_grad():\\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\\n\\n        all_probas[te_idx] = probas\\n\\n        # Per-fold adjacent AUC\\n        td = depths[te_idx]\\n        for k in range(1, num_classes):\\n            m = (td == k - 1) | (td == k)\\n            y = (td[m] == k).astype(int)\\n            if len(np.unique(y)) < 2 or m.sum() < 4:\\n                continue\\n            p0 = probas[m, k - 1]\\n            p1 = probas[m, k]\\n            s = p1 / (p0 + p1 + 1e-12)\\n            fold_adj_aucs[f\\\"{k-1}v{k}\\\"].append(round(float(roc_auc_score(y, s)), 4))\\n\\n        del mlp\\n        torch.cuda.empty_cache()\\n\\n    # Overall pairwise AUC\\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\\n\\n    # K*\\n    k_star = 0\\n    for k in range(1, num_classes):\\n        if adj_auc.get(f\\\"{k-1}v{k}\\\", 0) > 0.60:\\n            k_star = k\\n\\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\\n\\n    # Per-fold stats\\n    fold_stats = {}\\n    for key, aucs in fold_adj_aucs.items():\\n        if aucs:\\n            fold_stats[key] = {\\n                \\\"mean\\\": round(float(np.mean(aucs)), 4),\\n                \\\"std\\\": round(float(np.std(aucs)), 4),\\n                \\\"folds\\\": aucs,\\n            }\\n\\n    # Load baseline (hand-crafted features + LightGBM) if available\\n    baseline = None\\n    data_name = Path(data_dir).name\\n    results_name = data_name.replace(\\\"data_\\\", \\\"results_\\\")\\n    baseline_path = Path(data_dir).parent / results_name / \\\"pairwise_auc.json\\\"\\n    if baseline_path.exists():\\n        with open(baseline_path) as f:\\n            baseline = json.load(f)\\n        log.info(f\\\"  Loaded baseline from {baseline_path}\\\")\\n\\n    result = {\\n        \\\"dataset\\\": label,\\n        \\\"data_dir\\\": str(data_dir),\\n        \\\"num_samples_per_depth\\\": args.num_samples if args.num_samples else \\\"all\\\",\\n        \\\"max_depth\\\": args.max_depth,\\n        \\\"embedding_dim\\\": input_dim,\\n        \\\"mlp_arch\\\": f\\\"{input_dim}->512->256->{num_classes}\\\",\\n        \\\"neural_probe\\\": {\\n            \\\"pairwise_auc_adjacent\\\": adj_auc,\\n            \\\"pairwise_auc_all\\\": all_auc,\\n            \\\"fold_stats\\\": fold_stats,\\n            \\\"k_star\\\": k_star,\\n            \\\"k_star_threshold\\\": 0.60,\\n            \\\"classification_accuracy\\\": round(accuracy, 4),\\n        },\\n    }\\n    if baseline:\\n        result[\\\"lgbm_baseline\\\"] = {\\n            \\\"pairwise_auc_adjacent\\\": baseline[\\\"mean\\\"],\\n            \\\"k_star\\\": max(\\n                (k for k in range(1, 6) if baseline[\\\"mean\\\"].get(f\\\"{k-1}v{k}\\\", 0) > 0.60),\\n                default=0,\\n            ),\\n        }\\n\\n    # Log summary\\n    log.info(f\\\"\\\\n  K* (neural probe) = {k_star}\\\")\\n    log.info(f\\\"  Accuracy = {accuracy:.4f}\\\")\\n    for k in range(1, num_classes):\\n        key = f\\\"{k-1}v{k}\\\"\\n        a = adj_auc.get(key, \\\"N/A\\\")\\n        fs = fold_stats.get(key, {})\\n        std = fs.get(\\\"std\\\", 0)\\n        base = baseline[\\\"mean\\\"].get(key, \\\"—\\\") if baseline else \\\"—\\\"\\n        log.info(f\\\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\\\")\\n\\n    return result\\n\\n\\n# ── Main ──────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\",\\n    )\\n    parser.add_argument(\\n        \\\"--model_path\\\", type=str,\\n        default=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\\\",\\n    )\\n    parser.add_argument(\\\"--data_dir\\\", type=str, nargs=\\\"+\\\",\\n                        default=[\\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\"])\\n    parser.add_argument(\\\"--label\\\", type=str, nargs=\\\"+\\\", default=[\\\"Qwen-cont\\\"])\\n    parser.add_argument(\\n        \\\"--output\\\", type=str,\\n        default=\\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\",\\n    )\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=None,\\n                        help=\\\"Max samples per depth (default: all)\\\")\\n    parser.add_argument(\\\"--max_depth\\\", type=int, default=5)\\n    parser.add_argument(\\\"--embed_batch_size\\\", type=int, default=24)\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512)\\n    parser.add_argument(\\\"--mlp_batch_size\\\", type=int, default=256)\\n    parser.add_argument(\\\"--epochs\\\", type=int, default=20)\\n    parser.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    parser.add_argument(\\\"--patience\\\", type=int, default=5)\\n    parser.add_argument(\\\"--device\\\", type=str, default=\\\"cuda:0\\\")\\n    args = parser.parse_args()\\n\\n    if len(args.data_dir) != len(args.label):\\n        log.error(\\\"--data_dir and --label must have the same number of entries\\\")\\n        sys.exit(1)\\n\\n    device = args.device if torch.cuda.is_available() else \\\"cpu\\\"\\n    log.info(f\\\"Device: {device}\\\")\\n    if torch.cuda.is_available():\\n        props = torch.cuda.get_device_properties(0)\\n        log.info(f\\\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\\\")\\n\\n    # Load LLM once for all datasets\\n    from transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n    log.info(f\\\"Loading model from {args.model_path} ...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n        tokenizer.pad_token_id = tokenizer.eos_token_id\\n    tokenizer.padding_side = \\\"right\\\"\\n\\n    llm = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch.float16,\\n        device_map=\\\"auto\\\",\\n        trust_remote_code=True,\\n    )\\n    llm.eval()\\n    log.info(\\\"Model loaded.\\\")\\n\\n    # Run per-dataset\\n    all_results = []\\n    for dd, lab in zip(args.data_dir, args.label):\\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\\n        if r:\\n            all_results.append(r)\\n\\n    # Free LLM\\n    del llm\\n    torch.cuda.empty_cache()\\n\\n    # Save\\n    out = Path(args.output)\\n    out.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\\n    log.info(f\\\"\\\\nResults → {out}\\\")\\n\\n    # Final summary\\n    log.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    log.info(\\\"SUMMARY\\\")\\n    log.info(\\\"=\\\" * 60)\\n    for r in all_results:\\n        np_ks = r[\\\"neural_probe\\\"][\\\"k_star\\\"]\\n        base_ks = r.get(\\\"lgbm_baseline\\\", {}).get(\\\"k_star\\\", \\\"—\\\")\\n        log.info(f\\\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\\\")\\n\\n    k_stars = [r[\\\"neural_probe\\\"][\\\"k_star\\\"] for r in all_results]\\n    if len(k_stars) > 1:\\n        if all(k == k_stars[0] for k in k_stars):\\n            log.info(f\\\"\\\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\\\")\\n        else:\\n            log.info(f\\\"\\\\n  K* varies: {k_stars}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "a7060790-31ea-4e3e-9589-3ec48606232b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    fold_adj_aucs = {f\\\\\\\"{k-1}v{k}\\\\\\\": [] for k in range(1, num_classes)}\\\\n\\\\n    for fold, (tr_idx, te_idx) in enumerate(\\\\n        gkf.split(embeddings, depths, groups=doc_ids)\\\\n    ):\\\\n        log.info(f\\\\\\\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\\\\\\\")\\\\n        mlp = train_mlp(\\\\n            embeddings[tr_idx], depths[tr_idx],\\\\n            embeddings[te_idx], depths[te_idx],\\\\n            input_dim=input_dim, num_classes=num_classes,\\\\n            epochs=args.epochs, lr=args.lr,\\\\n            batch_size=args.mlp_batch_size,\\\\n            patience=args.patience, device=device,\\\\n        )\\\\n\\\\n        with torch.no_grad():\\\\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\\\\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\\\\n\\\\n        all_probas[te_idx] = probas\\\\n\\\\n        # Per-fold adjacent AUC\\\\n        td = depths[te_idx]\\\\n        for k in range(1, num_classes):\\\\n            m = (td == k - 1) | (td == k)\\\\n            y = (td[m] == k).astype(int)\\\\n            if len(np.unique(y)) < 2 or m.sum() < 4:\\\\n                continue\\\\n            p0 = probas[m, k - 1]\\\\n            p1 = probas[m, k]\\\\n            s = p1 / (p0 + p1 + 1e-12)\\\\n            fold_adj_aucs[f\\\\\\\"{k-1}v{k}\\\\\\\"].append(round(float(roc_auc_score(y, s)), 4))\\\\n\\\\n        del mlp\\\\n        torch.cuda.empty_cache()\\\\n\\\\n    # Overall pairwise AUC\\\\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\\\\n\\\\n    # K*\\\\n    k_star = 0\\\\n    for k in range(1, num_classes):\\\\n        if adj_auc.get(f\\\\\\\"{k-1}v{k}\\\\\\\", 0) > 0.60:\\\\n            k_star = k\\\\n\\\\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\\\\n\\\\n    # Per-fold stats\\\\n    fold_stats = {}\\\\n    for key, aucs in fold_adj_aucs.items():\\\\n        if aucs:\\\\n            fold_stats[key] = {\\\\n                \\\\\\\"mean\\\\\\\": round(float(np.mean(aucs)), 4),\\\\n                \\\\\\\"std\\\\\\\": round(float(np.std(aucs)), 4),\\\\n                \\\\\\\"folds\\\\\\\": aucs,\\\\n            }\\\\n\\\\n    # Load baseline (hand-crafted features + LightGBM) if available\\\\n    baseline = None\\\\n    data_name = Path(data_dir).name\\\\n    results_name = data_name.replace(\\\\\\\"data_\\\\\\\", \\\\\\\"results_\\\\\\\")\\\\n    baseline_path = Path(data_dir).parent / results_name / \\\\\\\"pairwise_auc.json\\\\\\\"\\\\n    if baseline_path.exists():\\\\n        with open(baseline_path) as f:\\\\n            baseline = json.load(f)\\\\n        log.info(f\\\\\\\"  Loaded baseline from {baseline_path}\\\\\\\")\\\\n\\\\n    result = {\\\\n        \\\\\\\"dataset\\\\\\\": label,\\\\n        \\\\\\\"data_dir\\\\\\\": str(data_dir),\\\\n        \\\\\\\"num_samples_per_depth\\\\\\\": args.num_samples if args.num_samples else \\\\\\\"all\\\\\\\",\\\\n        \\\\\\\"max_depth\\\\\\\": args.max_depth,\\\\n        \\\\\\\"embedding_dim\\\\\\\": input_dim,\\\\n        \\\\\\\"mlp_arch\\\\\\\": f\\\\\\\"{input_dim}->512->256->{num_classes}\\\\\\\",\\\\n        \\\\\\\"neural_probe\\\\\\\": {\\\\n            \\\\\\\"pairwise_auc_adjacent\\\\\\\": adj_auc,\\\\n            \\\\\\\"pairwise_auc_all\\\\\\\": all_auc,\\\\n            \\\\\\\"fold_stats\\\\\\\": fold_stats,\\\\n            \\\\\\\"k_star\\\\\\\": k_star,\\\\n            \\\\\\\"k_star_threshold\\\\\\\": 0.60,\\\\n            \\\\\\\"classification_accuracy\\\\\\\": round(accuracy, 4),\\\\n        },\\\\n    }\\\\n    if baseline:\\\\n        result[\\\\\\\"lgbm_baseline\\\\\\\"] = {\\\\n            \\\\\\\"pairwise_auc_adjacent\\\\\\\": baseline[\\\\\\\"mean\\\\\\\"],\\\\n            \\\\\\\"k_star\\\\\\\": max(\\\\n                (k for k in range(1, 6) if baseline[\\\\\\\"mean\\\\\\\"].get(f\\\\\\\"{k-1}v{k}\\\\\\\", 0) > 0.60),\\\\n                default=0,\\\\n            ),\\\\n        }\\\\n\\\\n    # Log summary\\\\n    log.info(f\\\\\\\"\\\\\\\\n  K* (neural probe) = {k_star}\\\\\\\")\\\\n    log.info(f\\\\\\\"  Accuracy = {accuracy:.4f}\\\\\\\")\\\\n    for k in range(1, num_classes):\\\\n        key = f\\\\\\\"{k-1}v{k}\\\\\\\"\\\\n        a = adj_auc.get(key, \\\\\\\"N/A\\\\\\\")\\\\n        fs = fold_stats.get(key, {})\\\\n        std = fs.get(\\\\\\\"std\\\\\\\", 0)\\\\n        base = baseline[\\\\\\\"mean\\\\\\\"].get(key, \\\\\\\"—\\\\\\\") if baseline else \\\\\\\"—\\\\\\\"\\\\n        log.info(f\\\\\\\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\\\\\\\")\\\\n\\\\n    return result\\\\n\\\\n\\\\n# ── Main ──────────────────────────────────────────────────────────────\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\\\\\",\\\\n    )\\\\n    parser.add_argument(\\\\n        \\\\\\\"--model_path\\\\\\\", type=str,\\\\n        default=\\\\\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\\\\\\\",\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--data_dir\\\\\\\", type=str, nargs=\\\\\\\"+\\\\\\\",\\\\n                        default=[\\\\\\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\\\\\"])\\\\n    parser.add_argument(\\\\\\\"--label\\\\\\\", type=str, nargs=\\\\\\\"+\\\\\\\", default=[\\\\\\\"Qwen-cont\\\\\\\"])\\\\n    parser.add_argument(\\\\n        \\\\\\\"--output\\\\\\\", type=str,\\\\n        default=\\\\\\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\\\\\",\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--num_samples\\\\\\\", type=int, default=None,\\\\n                        help=\\\\\\\"Max samples per depth (default: all)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max_depth\\\\\\\", type=int, default=5)\\\\n    parser.add_argument(\\\\\\\"--embed_batch_size\\\\\\\", type=int, default=24)\\\\n    parser.add_argument(\\\\\\\"--max_length\\\\\\\", type=int, default=512)\\\\n    parser.add_argument(\\\\\\\"--mlp_batch_size\\\\\\\", type=int, default=256)\\\\n    parser.add_argument(\\\\\\\"--epochs\\\\\\\", type=int, default=20)\\\\n    parser.add_argument(\\\\\\\"--lr\\\\\\\", type=float, default=1e-3)\\\\n    parser.add_argument(\\\\\\\"--patience\\\\\\\", type=int, default=5)\\\\n    parser.add_argument(\\\\\\\"--device\\\\\\\", type=str, default=\\\\\\\"cuda:0\\\\\\\")\\\\n    args = parser.parse_args()\\\\n\\\\n    if len(args.data_dir) != len(args.label):\\\\n        log.error(\\\\\\\"--data_dir and --label must have the same number of entries\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = args.device if torch.cuda.is_available() else \\\\\\\"cpu\\\\\\\"\\\\n    log.info(f\\\\\\\"Device: {device}\\\\\\\")\\\\n    if torch.cuda.is_available():\\\\n        props = torch.cuda.get_device_properties(0)\\\\n        log.info(f\\\\\\\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\\\\\\\")\\\\n\\\\n    # Load LLM once for all datasets\\\\n    from transformers import AutoModelForCausalLM, AutoTokenizer\\\\n\\\\n    log.info(f\\\\\\\"Loading model from {args.model_path} ...\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\\\n    if tokenizer.pad_token is None:\\\\n        tokenizer.pad_token = tokenizer.eos_token\\\\n        tokenizer.pad_token_id = tokenizer.eos_token_id\\\\n    tokenizer.padding_side = \\\\\\\"right\\\\\\\"\\\\n\\\\n    llm = AutoModelForCausalLM.from_pretrained(\\\\n        args.model_path,\\\\n        torch_dtype=torch.float16,\\\\n        device_map=\\\\\\\"auto\\\\\\\",\\\\n        trust_remote_code=True,\\\\n    )\\\\n    llm.eval()\\\\n    log.info(\\\\\\\"Model loaded.\\\\\\\")\\\\n\\\\n    # Run per-dataset\\\\n    all_results = []\\\\n    for dd, lab in zip(args.data_dir, args.label):\\\\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\\\\n        if r:\\\\n            all_results.append(r)\\\\n\\\\n    # Free LLM\\\\n    del llm\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    # Save\\\\n    out = Path(args.output)\\\\n    out.parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(out, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\\\\n    log.info(f\\\\\\\"\\\\\\\\nResults → {out}\\\\\\\")\\\\n\\\\n    # Final summary\\\\n    log.info(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 60)\\\\n    log.info(\\\\\\\"SUMMARY\\\\\\\")\\\\n    log.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    for r in all_results:\\\\n        np_ks = r[\\\\\\\"neural_probe\\\\\\\"][\\\\\\\"k_star\\\\\\\"]\\\\n        base_ks = r.get(\\\\\\\"lgbm_baseline\\\\\\\", {}).get(\\\\\\\"k_star\\\\\\\", \\\\\\\"—\\\\\\\")\\\\n        log.info(f\\\\\\\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\\\\\\\")\\\\n\\\\n    k_stars = [r[\\\\\\\"neural_probe\\\\\\\"][\\\\\\\"k_star\\\\\\\"] for r in all_results]\\\\n    if len(k_stars) > 1:\\\\n        if all(k == k_stars[0] for k in k_stars):\\\\n            log.info(f\\\\\\\"\\\\\\\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\\\\\\\")\\\\n        else:\\\\n            log.info(f\\\\\\\"\\\\\\\\n  K* varies: {k_stars}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    fold_adj_aucs = {f\\\"{k-1}v{k}\\\": [] for k in range(1, num_classes)}\\n\\n    for fold, (tr_idx, te_idx) in enumerate(\\n        gkf.split(embeddings, depths, groups=doc_ids)\\n    ):\\n        log.info(f\\\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\\\")\\n        mlp = train_mlp(\\n            embeddings[tr_idx], depths[tr_idx],\\n            embeddings[te_idx], depths[te_idx],\\n            input_dim=input_dim, num_classes=num_classes,\\n            epochs=args.epochs, lr=args.lr,\\n            batch_size=args.mlp_batch_size,\\n            patience=args.patience, device=device,\\n        )\\n\\n        with torch.no_grad():\\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\\n\\n        all_probas[te_idx] = probas\\n\\n        # Per-fold adjacent AUC\\n        td = depths[te_idx]\\n        for k in range(1, num_classes):\\n            m = (td == k - 1) | (td == k)\\n            y = (td[m] == k).astype(int)\\n            if len(np.unique(y)) < 2 or m.sum() < 4:\\n                continue\\n            p0 = probas[m, k - 1]\\n            p1 = probas[m, k]\\n            s = p1 / (p0 + p1 + 1e-12)\\n            fold_adj_aucs[f\\\"{k-1}v{k}\\\"].append(round(float(roc_auc_score(y, s)), 4))\\n\\n        del mlp\\n        torch.cuda.empty_cache()\\n\\n    # Overall pairwise AUC\\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\\n\\n    # K*\\n    k_star = 0\\n    for k in range(1, num_classes):\\n        if adj_auc.get(f\\\"{k-1}v{k}\\\", 0) > 0.60:\\n            k_star = k\\n\\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\\n\\n    # Per-fold stats\\n    fold_stats = {}\\n    for key, aucs in fold_adj_aucs.items():\\n        if aucs:\\n            fold_stats[key] = {\\n                \\\"mean\\\": round(float(np.mean(aucs)), 4),\\n                \\\"std\\\": round(float(np.std(aucs)), 4),\\n                \\\"folds\\\": aucs,\\n            }\\n\\n    # Load baseline (hand-crafted features + LightGBM) if available\\n    baseline = None\\n    data_name = Path(data_dir).name\\n    results_name = data_name.replace(\\\"data_\\\", \\\"results_\\\")\\n    baseline_path = Path(data_dir).parent / results_name / \\\"pairwise_auc.json\\\"\\n    if baseline_path.exists():\\n        with open(baseline_path) as f:\\n            baseline = json.load(f)\\n        log.info(f\\\"  Loaded baseline from {baseline_path}\\\")\\n\\n    result = {\\n        \\\"dataset\\\": label,\\n        \\\"data_dir\\\": str(data_dir),\\n        \\\"num_samples_per_depth\\\": args.num_samples if args.num_samples else \\\"all\\\",\\n        \\\"max_depth\\\": args.max_depth,\\n        \\\"embedding_dim\\\": input_dim,\\n        \\\"mlp_arch\\\": f\\\"{input_dim}->512->256->{num_classes}\\\",\\n        \\\"neural_probe\\\": {\\n            \\\"pairwise_auc_adjacent\\\": adj_auc,\\n            \\\"pairwise_auc_all\\\": all_auc,\\n            \\\"fold_stats\\\": fold_stats,\\n            \\\"k_star\\\": k_star,\\n            \\\"k_star_threshold\\\": 0.60,\\n            \\\"classification_accuracy\\\": round(accuracy, 4),\\n        },\\n    }\\n    if baseline:\\n        result[\\\"lgbm_baseline\\\"] = {\\n            \\\"pairwise_auc_adjacent\\\": baseline[\\\"mean\\\"],\\n            \\\"k_star\\\": max(\\n                (k for k in range(1, 6) if baseline[\\\"mean\\\"].get(f\\\"{k-1}v{k}\\\", 0) > 0.60),\\n                default=0,\\n            ),\\n        }\\n\\n    # Log summary\\n    log.info(f\\\"\\\\n  K* (neural probe) = {k_star}\\\")\\n    log.info(f\\\"  Accuracy = {accuracy:.4f}\\\")\\n    for k in range(1, num_classes):\\n        key = f\\\"{k-1}v{k}\\\"\\n        a = adj_auc.get(key, \\\"N/A\\\")\\n        fs = fold_stats.get(key, {})\\n        std = fs.get(\\\"std\\\", 0)\\n        base = baseline[\\\"mean\\\"].get(key, \\\"—\\\") if baseline else \\\"—\\\"\\n        log.info(f\\\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\\\")\\n\\n    return result\\n\\n\\n# ── Main ──────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\",\\n    )\\n    parser.add_argument(\\n        \\\"--model_path\\\", type=str,\\n        default=\\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\\\",\\n    )\\n    parser.add_argument(\\\"--data_dir\\\", type=str, nargs=\\\"+\\\",\\n                        default=[\\\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\\\"])\\n    parser.add_argument(\\\"--label\\\", type=str, nargs=\\\"+\\\", default=[\\\"Qwen-cont\\\"])\\n    parser.add_argument(\\n        \\\"--output\\\", type=str,\\n        default=\\\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\\\",\\n    )\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=None,\\n                        help=\\\"Max samples per depth (default: all)\\\")\\n    parser.add_argument(\\\"--max_depth\\\", type=int, default=5)\\n    parser.add_argument(\\\"--embed_batch_size\\\", type=int, default=24)\\n    parser.add_argument(\\\"--max_length\\\", type=int, default=512)\\n    parser.add_argument(\\\"--mlp_batch_size\\\", type=int, default=256)\\n    parser.add_argument(\\\"--epochs\\\", type=int, default=20)\\n    parser.add_argument(\\\"--lr\\\", type=float, default=1e-3)\\n    parser.add_argument(\\\"--patience\\\", type=int, default=5)\\n    parser.add_argument(\\\"--device\\\", type=str, default=\\\"cuda:0\\\")\\n    args = parser.parse_args()\\n\\n    if len(args.data_dir) != len(args.label):\\n        log.error(\\\"--data_dir and --label must have the same number of entries\\\")\\n        sys.exit(1)\\n\\n    device = args.device if torch.cuda.is_available() else \\\"cpu\\\"\\n    log.info(f\\\"Device: {device}\\\")\\n    if torch.cuda.is_available():\\n        props = torch.cuda.get_device_properties(0)\\n        log.info(f\\\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\\\")\\n\\n    # Load LLM once for all datasets\\n    from transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n    log.info(f\\\"Loading model from {args.model_path} ...\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n        tokenizer.pad_token_id = tokenizer.eos_token_id\\n    tokenizer.padding_side = \\\"right\\\"\\n\\n    llm = AutoModelForCausalLM.from_pretrained(\\n        args.model_path,\\n        torch_dtype=torch.float16,\\n        device_map=\\\"auto\\\",\\n        trust_remote_code=True,\\n    )\\n    llm.eval()\\n    log.info(\\\"Model loaded.\\\")\\n\\n    # Run per-dataset\\n    all_results = []\\n    for dd, lab in zip(args.data_dir, args.label):\\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\\n        if r:\\n            all_results.append(r)\\n\\n    # Free LLM\\n    del llm\\n    torch.cuda.empty_cache()\\n\\n    # Save\\n    out = Path(args.output)\\n    out.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out, \\\"w\\\") as f:\\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\\n    log.info(f\\\"\\\\nResults → {out}\\\")\\n\\n    # Final summary\\n    log.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    log.info(\\\"SUMMARY\\\")\\n    log.info(\\\"=\\\" * 60)\\n    for r in all_results:\\n        np_ks = r[\\\"neural_probe\\\"][\\\"k_star\\\"]\\n        base_ks = r.get(\\\"lgbm_baseline\\\", {}).get(\\\"k_star\\\", \\\"—\\\")\\n        log.info(f\\\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\\\")\\n\\n    k_stars = [r[\\\"neural_probe\\\"][\\\"k_star\\\"] for r in all_results]\\n    if len(k_stars) > 1:\\n        if all(k == k_stars[0] for k in k_stars):\\n            log.info(f\\\"\\\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\\\")\\n        else:\\n            log.info(f\\\"\\\\n  K* varies: {k_stars}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full script. Let me also check exp-007's bootstrap framework for reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "b323b8f3-dea8-4e66-9b63-739c7cece75f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K37xEauXB1v97M1wLdyi9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 31244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3387
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 19_

现在看 exp-007 的 bootstrap 框架作参考。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "ff5fa8af-aa89-49ea-953a-c1ebaf333ea8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K37xEauXB1v97M1wLdyi9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 31244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3387
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01D6gWgcw1oYpoTqjLQJawkM`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "cc36e6ab-86e1-4e3c-ae6a-35754ae80887",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K37xEauXB1v97M1wLdyi9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3387,
      "cache_read_input_tokens": 31244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3387
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T03:02:47.868Z_

<details><summary>↩ Tool result · `toolu_01D6gWgcw1oYpoTqjLQJawkM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "25606e3f-55e5-4e58-a055-1902d7902799",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QpQQcJpWqaYQ9H59A3GBtC`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "16bd9f01-d641-420f-8157-f9872b071bae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WnTALwvcSsZs8yJFxsVaN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 288,
      "cache_read_input_tokens": 34631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 288
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T03:02:51.367Z_

<details><summary>↩ Tool result · `toolu_01QpQQcJpWqaYQ9H59A3GBtC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci_exp017.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "4e0034ea-97e4-4d13-ba2d-24e65de5b588",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\\\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci_exp017.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci_exp017.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XgjDZ9kASRkgLBear7CWY2`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "d6e40d70-5de8-4d99-b836-9a7fb4e851a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GukwYHbWHtfebxpM7Xq7Ms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 34919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 360
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T03:02:54.768Z_

<details><summary>↩ Tool result · `toolu_01XgjDZ9kASRkgLBear7CWY2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Bootstrap 95% CI and permutation test for pairwise AUC.\\n\\nMethod:\\n  1. Compute out-of-fold predictions via GroupKFold(5) + LGBMClassifier (matching original pipeline)\\n  2. Bootstrap CI: resample doc_ids with replacement, compute AUC from OOF predictions (1000x)\\n  3. Permutation test: shuffle labels on OOF predictions, compute AUC (500x)\\n\\\"\\\"\\\"\\n\\nimport csv, json, time\\nimport numpy as np\\nfrom pathlib import Path\\nimport lightgbm as lgb\\nfrom sklearn.model_selection import GroupKFold\\nfrom sklearn.metrics import roc_auc_score\\n\\nFEAT_COLS = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\", \\\"freq_entropy\\\", \\\"low_freq_ratio\\\",\\n]\\n\\nEXPERIMENTS = {\\n    \\\"mvp_001_qwen_rewrite\\\": \\\"data/features.csv\\\",\\n    \\\"exp_001_pythia\\\": \\\"data_exp001_pythia/features.csv\\\",\\n    \\\"exp_002_olmo\\\": \\\"data_exp002_olmo/features.csv\\\",\\n}\\n\\nN_BOOTSTRAP = 1000\\nN_PERMUTATION = 500\\nMAX_DEPTH = 5\\nSEED = 42\\n\\n\\ndef load_features(path):\\n    with open(path) as f:\\n        rows = list(csv.DictReader(f))\\n    depths = np.array([int(r[\\\"depth\\\"]) for r in rows])\\n    doc_ids = np.array([int(r[\\\"doc_id\\\"]) for r in rows])\\n    X = np.array([\\n        [float(r[c]) if r[c] not in (\\\"\\\", \\\"nan\\\") else np.nan for c in FEAT_COLS]\\n        for r in rows\\n    ])\\n    col_means = np.nanmean(X, axis=0)\\n    for j in range(X.shape[1]):\\n        mask = np.isnan(X[:, j])\\n        X[mask, j] = col_means[j]\\n    return depths, doc_ids, X\\n\\n\\ndef oof_predictions(X, y, groups):\\n    preds = np.zeros(len(y))\\n    for tr, te in GroupKFold(5).split(X, y, groups):\\n        clf = lgb.LGBMClassifier(\\n            n_estimators=200, max_depth=6, learning_rate=0.05,\\n            num_leaves=31, verbose=-1, n_jobs=-1,\\n        )\\n        clf.fit(X[tr], y[tr])\\n        preds[te] = clf.predict_proba(X[te])[:, 1]\\n    return preds\\n\\n\\ndef bootstrap_auc(y, preds, doc_ids, n, rng):\\n    unique = np.unique(doc_ids)\\n    doc_idx = {d: np.where(doc_ids == d)[0] for d in unique}\\n    aucs = np.empty(n)\\n    valid = 0\\n    for i in range(n):\\n        sampled = rng.choice(unique, size=len(unique), replace=True)\\n        idx = np.concatenate([doc_idx[d] for d in sampled])\\n        yb, pb = y[idx], preds[idx]\\n        if len(np.unique(yb)) < 2:\\n            continue\\n        aucs[valid] = roc_auc_score(yb, pb)\\n        valid += 1\\n    return aucs[:valid]\\n\\n\\ndef permutation_pvalue(y, preds, obs_auc, n, rng):\\n    count = 0\\n    for _ in range(n):\\n        yp = rng.permutation(y)\\n        if len(np.unique(yp)) < 2:\\n            continue\\n        count += (roc_auc_score(yp, preds) >= obs_auc)\\n    return count / n\\n\\n\\ndef main():\\n    base = Path(\\\"/root/autodl-tmp/gen-depth-contamination\\\")\\n    rng = np.random.default_rng(SEED)\\n    results = {}\\n\\n    t0 = time.time()\\n    for exp_name, feat_path in EXPERIMENTS.items():\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"  {exp_name}\\\")\\n        print(f\\\"{'='*60}\\\")\\n\\n        depths, doc_ids, X = load_features(base / feat_path)\\n        exp_results = {}\\n\\n        for k in range(1, MAX_DEPTH + 1):\\n            pair = f\\\"{k-1}v{k}\\\"\\n            mask = (depths == k - 1) | (depths == k)\\n            Xp, yp = X[mask], (depths[mask] == k).astype(int)\\n            gp = doc_ids[mask]\\n\\n            if len(np.unique(yp)) < 2:\\n                print(f\\\"  {pair}: skipped (single class)\\\")\\n                continue\\n\\n            t1 = time.time()\\n            preds = oof_predictions(Xp, yp, gp)\\n            obs_auc = roc_auc_score(yp, preds)\\n\\n            boot_aucs = bootstrap_auc(yp, preds, gp, N_BOOTSTRAP, rng)\\n            ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\\n            boot_mean = np.mean(boot_aucs)\\n            boot_std = np.std(boot_aucs)\\n\\n            pval = permutation_pvalue(yp, preds, obs_auc, N_PERMUTATION, rng)\\n            elapsed = time.time() - t1\\n\\n            exp_results[pair] = {\\n                \\\"mean_auc\\\": round(float(obs_auc), 4),\\n                \\\"boot_mean\\\": round(float(boot_mean), 4),\\n                \\\"boot_std\\\": round(float(boot_std), 4),\\n                \\\"ci_lower\\\": round(float(ci_lo), 4),\\n                \\\"ci_upper\\\": round(float(ci_hi), 4),\\n                \\\"ci_width\\\": round(float(ci_hi - ci_lo), 4),\\n                \\\"perm_pvalue\\\": float(pval),\\n                \\\"n_bootstrap\\\": N_BOOTSTRAP,\\n                \\\"n_permutation\\\": N_PERMUTATION,\\n            }\\n\\n            flag = \\\"\\\"\\n            if exp_name == \\\"exp_002_olmo\\\" and pair == \\\"1v2\\\":\\n                if ci_lo >= 0.60:\\n                    flag = \\\" [CI lower > 0.60, K* robust]\\\"\\n                elif ci_lo >= 0.55:\\n                    flag = \\\" [CI lower in (0.55, 0.60), K* borderline]\\\"\\n                else:\\n                    flag = \\\" [CI lower < 0.55, K* NOT robust]\\\"\\n\\n            pval_s = f\\\"<{1/N_PERMUTATION}\\\" if pval == 0 else f\\\"{pval:.4f}\\\"\\n            print(f\\\"  {pair}: AUC={obs_auc:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  \\\"\\n                  f\\\"p={pval_s}  ({elapsed:.1f}s){flag}\\\")\\n\\n        results[exp_name] = exp_results\\n\\n    out_path = base / \\\"artifacts\\\" / \\\"bootstrap_ci_results.json\\\"\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n\\n    total = time.time() - t0\\n    print(f\\\"\\\\n{'='*80}\\\")\\n    print(f\\\"SUMMARY TABLE  (total {total:.0f}s)\\\")\\n    print(f\\\"{'='*80}\\\")\\n    print(f\\\"{'Experiment':<25} {'Pair':>5} {'AUC':>7} {'95% CI':>22} {'Width':>7} {'p-value':>10}\\\")\\n    print(\\\"-\\\" * 80)\\n    for exp_name, exp_res in results.items():\\n        for pair, r in exp_res.items():\\n            pval_s = f\\\"<{1/N_PERMUTATION}\\\" if r[\\\"perm_pvalue\\\"] == 0 else f\\\"{r['perm_pvalue']:.4f}\\\"\\n            ci_str = f\\\"[{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\\\"\\n            print(f\\\"{exp_name:<25} {pair:>5} {r['mean_auc']:>7.4f} {ci_str:>22} {r['ci_width']:>7.4f} {pval_s:>10}\\\")\\n\\n    olmo_1v2 = results.get(\\\"exp_002_olmo\\\", {}).get(\\\"1v2\\\", {})\\n    if olmo_1v2:\\n        lo = olmo_1v2[\\\"ci_lower\\\"]\\n        print(f\\\"\\\\n*** KEY CHECK: OLMo 1v2 CI lower = {lo:.4f} \\\", end=\\\"\\\")\\n        if lo >= 0.60:\\n            print(\\\"(> 0.60, K* claim ROBUST)\\\")\\n        elif lo >= 0.55:\\n            print(\\\"(< 0.60 but > 0.55, K* BORDERLINE)\\\")\\n        else:\\n            print(\\\"(< 0.55, K* NOT ROBUST)\\\")\\n\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "61ff44f5-3733-4728-a659-b01d35a89bb7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Bootstrap 95% CI and permutation test for pairwise AUC.\\\\n\\\\nMethod:\\\\n  1. Compute out-of-fold predictions via GroupKFold(5) + LGBMClassifier (matching original pipeline)\\\\n  2. Bootstrap CI: resample doc_ids with replacement, compute AUC from OOF predictions (1000x)\\\\n  3. Permutation test: shuffle labels on OOF predictions, compute AUC (500x)\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport csv, json, time\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\nimport lightgbm as lgb\\\\nfrom sklearn.model_selection import GroupKFold\\\\nfrom sklearn.metrics import roc_auc_score\\\\n\\\\nFEAT_COLS = [\\\\n    \\\\\\\"surp_mean\\\\\\\", \\\\\\\"surp_std\\\\\\\", \\\\\\\"surp_skew\\\\\\\", \\\\\\\"surp_kurt\\\\\\\",\\\\n    \\\\\\\"surp_d1_mean\\\\\\\", \\\\\\\"surp_d1_std\\\\\\\", \\\\\\\"surp_d1_skew\\\\\\\",\\\\n    \\\\\\\"surp_d2_mean\\\\\\\", \\\\\\\"surp_d2_std\\\\\\\",\\\\n    \\\\\\\"ttr\\\\\\\", \\\\\\\"hapax_ratio\\\\\\\", \\\\\\\"self_bleu\\\\\\\",\\\\n    \\\\\\\"freq_kurtosis\\\\\\\", \\\\\\\"freq_entropy\\\\\\\", \\\\\\\"low_freq_ratio\\\\\\\",\\\\n]\\\\n\\\\nEXPERIMENTS = {\\\\n    \\\\\\\"mvp_001_qwen_rewrite\\\\\\\": \\\\\\\"data/features.csv\\\\\\\",\\\\n    \\\\\\\"exp_001_pythia\\\\\\\": \\\\\\\"data_exp001_pythia/features.csv\\\\\\\",\\\\n    \\\\\\\"exp_002_olmo\\\\\\\": \\\\\\\"data_exp002_olmo/features.csv\\\\\\\",\\\\n}\\\\n\\\\nN_BOOTSTRAP = 1000\\\\nN_PERMUTATION = 500\\\\nMAX_DEPTH = 5\\\\nSEED = 42\\\\n\\\\n\\\\ndef load_features(path):\\\\n    with open(path) as f:\\\\n        rows = list(csv.DictReader(f))\\\\n    depths = np.array([int(r[\\\\\\\"depth\\\\\\\"]) for r in rows])\\\\n    doc_ids = np.array([int(r[\\\\\\\"doc_id\\\\\\\"]) for r in rows])\\\\n    X = np.array([\\\\n        [float(r[c]) if r[c] not in (\\\\\\\"\\\\\\\", \\\\\\\"nan\\\\\\\") else np.nan for c in FEAT_COLS]\\\\n        for r in rows\\\\n    ])\\\\n    col_means = np.nanmean(X, axis=0)\\\\n    for j in range(X.shape[1]):\\\\n        mask = np.isnan(X[:, j])\\\\n        X[mask, j] = col_means[j]\\\\n    return depths, doc_ids, X\\\\n\\\\n\\\\ndef oof_predictions(X, y, groups):\\\\n    preds = np.zeros(len(y))\\\\n    for tr, te in GroupKFold(5).split(X, y, groups):\\\\n        clf = lgb.LGBMClassifier(\\\\n            n_estimators=200, max_depth=6, learning_rate=0.05,\\\\n            num_leaves=31, verbose=-1, n_jobs=-1,\\\\n        )\\\\n        clf.fit(X[tr], y[tr])\\\\n        preds[te] = clf.predict_proba(X[te])[:, 1]\\\\n    return preds\\\\n\\\\n\\\\ndef bootstrap_auc(y, preds, doc_ids, n, rng):\\\\n    unique = np.unique(doc_ids)\\\\n    doc_idx = {d: np.where(doc_ids == d)[0] for d in unique}\\\\n    aucs = np.empty(n)\\\\n    valid = 0\\\\n    for i in range(n):\\\\n        sampled = rng.choice(unique, size=len(unique), replace=True)\\\\n        idx = np.concatenate([doc_idx[d] for d in sampled])\\\\n        yb, pb = y[idx], preds[idx]\\\\n        if len(np.unique(yb)) < 2:\\\\n            continue\\\\n        aucs[valid] = roc_auc_score(yb, pb)\\\\n        valid += 1\\\\n    return aucs[:valid]\\\\n\\\\n\\\\ndef permutation_pvalue(y, preds, obs_auc, n, rng):\\\\n    count = 0\\\\n    for _ in range(n):\\\\n        yp = rng.permutation(y)\\\\n        if len(np.unique(yp)) < 2:\\\\n            continue\\\\n        count += (roc_auc_score(yp, preds) >= obs_auc)\\\\n    return count / n\\\\n\\\\n\\\\ndef main():\\\\n    base = Path(\\\\\\\"/root/autodl-tmp/gen-depth-contamination\\\\\\\")\\\\n    rng = np.random.default_rng(SEED)\\\\n    results = {}\\\\n\\\\n    t0 = time.time()\\\\n    for exp_name, feat_path in EXPERIMENTS.items():\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"  {exp_name}\\\\\\\")\\\\n        print(f\\\\\\\"{'='*60}\\\\\\\")\\\\n\\\\n        depths, doc_ids, X = load_features(base / feat_path)\\\\n        exp_results = {}\\\\n\\\\n        for k in range(1, MAX_DEPTH + 1):\\\\n            pair = f\\\\\\\"{k-1}v{k}\\\\\\\"\\\\n            mask = (depths == k - 1) | (depths == k)\\\\n            Xp, yp = X[mask], (depths[mask] == k).astype(int)\\\\n            gp = doc_ids[mask]\\\\n\\\\n            if len(np.unique(yp)) < 2:\\\\n                print(f\\\\\\\"  {pair}: skipped (single class)\\\\\\\")\\\\n                continue\\\\n\\\\n            t1 = time.time()\\\\n            preds = oof_predictions(Xp, yp, gp)\\\\n            obs_auc = roc_auc_score(yp, preds)\\\\n\\\\n            boot_aucs = bootstrap_auc(yp, preds, gp, N_BOOTSTRAP, rng)\\\\n            ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\\\\n            boot_mean = np.mean(boot_aucs)\\\\n            boot_std = np.std(boot_aucs)\\\\n\\\\n            pval = permutation_pvalue(yp, preds, obs_auc, N_PERMUTATION, rng)\\\\n            elapsed = time.time() - t1\\\\n\\\\n            exp_results[pair] = {\\\\n                \\\\\\\"mean_auc\\\\\\\": round(float(obs_auc), 4),\\\\n                \\\\\\\"boot_mean\\\\\\\": round(float(boot_mean), 4),\\\\n                \\\\\\\"boot_std\\\\\\\": round(float(boot_std), 4),\\\\n                \\\\\\\"ci_lower\\\\\\\": round(float(ci_lo), 4),\\\\n                \\\\\\\"ci_upper\\\\\\\": round(float(ci_hi), 4),\\\\n                \\\\\\\"ci_width\\\\\\\": round(float(ci_hi - ci_lo), 4),\\\\n                \\\\\\\"perm_pvalue\\\\\\\": float(pval),\\\\n                \\\\\\\"n_bootstrap\\\\\\\": N_BOOTSTRAP,\\\\n                \\\\\\\"n_permutation\\\\\\\": N_PERMUTATION,\\\\n            }\\\\n\\\\n            flag = \\\\\\\"\\\\\\\"\\\\n            if exp_name == \\\\\\\"exp_002_olmo\\\\\\\" and pair == \\\\\\\"1v2\\\\\\\":\\\\n                if ci_lo >= 0.60:\\\\n                    flag = \\\\\\\" [CI lower > 0.60, K* robust]\\\\\\\"\\\\n                elif ci_lo >= 0.55:\\\\n                    flag = \\\\\\\" [CI lower in (0.55, 0.60), K* borderline]\\\\\\\"\\\\n                else:\\\\n                    flag = \\\\\\\" [CI lower < 0.55, K* NOT robust]\\\\\\\"\\\\n\\\\n            pval_s = f\\\\\\\"<{1/N_PERMUTATION}\\\\\\\" if pval == 0 else f\\\\\\\"{pval:.4f}\\\\\\\"\\\\n            print(f\\\\\\\"  {pair}: AUC={obs_auc:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  \\\\\\\"\\\\n                  f\\\\\\\"p={pval_s}  ({elapsed:.1f}s){flag}\\\\\\\")\\\\n\\\\n        results[exp_name] = exp_results\\\\n\\\\n    out_path = base / \\\\\\\"artifacts\\\\\\\" / \\\\\\\"bootstrap_ci_results.json\\\\\\\"\\\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, indent=2)\\\\n\\\\n    total = time.time() - t0\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*80}\\\\\\\")\\\\n    print(f\\\\\\\"SUMMARY TABLE  (total {total:.0f}s)\\\\\\\")\\\\n    print(f\\\\\\\"{'='*80}\\\\\\\")\\\\n    print(f\\\\\\\"{'Experiment':<25} {'Pair':>5} {'AUC':>7} {'95% CI':>22} {'Width':>7} {'p-value':>10}\\\\\\\")\\\\n    print(\\\\\\\"-\\\\\\\" * 80)\\\\n    for exp_name, exp_res in results.items():\\\\n        for pair, r in exp_res.items():\\\\n            pval_s = f\\\\\\\"<{1/N_PERMUTATION}\\\\\\\" if r[\\\\\\\"perm_pvalue\\\\\\\"] == 0 else f\\\\\\\"{r['perm_pvalue']:.4f}\\\\\\\"\\\\n            ci_str = f\\\\\\\"[{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\\\\\\\"\\\\n            print(f\\\\\\\"{exp_name:<25} {pair:>5} {r['mean_auc']:>7.4f} {ci_str:>22} {r['ci_width']:>7.4f} {pval_s:>10}\\\\\\\")\\\\n\\\\n    olmo_1v2 = results.get(\\\\\\\"exp_002_olmo\\\\\\\", {}).get(\\\\\\\"1v2\\\\\\\", {})\\\\n    if olmo_1v2:\\\\n        lo = olmo_1v2[\\\\\\\"ci_lower\\\\\\\"]\\\\n        print(f\\\\\\\"\\\\\\\\n*** KEY CHECK: OLMo 1v2 CI lower = {lo:.4f} \\\\\\\", end=\\\\\\\"\\\\\\\")\\\\n        if lo >= 0.60:\\\\n            print(\\\\\\\"(> 0.60, K* claim ROBUST)\\\\\\\")\\\\n        elif lo >= 0.55:\\\\n            print(\\\\\\\"(< 0.60 but > 0.55, K* BORDERLINE)\\\\\\\")\\\\n        else:\\\\n            print(\\\\\\\"(< 0.55, K* NOT ROBUST)\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {out_path}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.69}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Bootstrap 95% CI and permutation test for pairwise AUC.\\n\\nMethod:\\n  1. Compute out-of-fold predictions via GroupKFold(5) + LGBMClassifier (matching original pipeline)\\n  2. Bootstrap CI: resample doc_ids with replacement, compute AUC from OOF predictions (1000x)\\n  3. Permutation test: shuffle labels on OOF predictions, compute AUC (500x)\\n\\\"\\\"\\\"\\n\\nimport csv, json, time\\nimport numpy as np\\nfrom pathlib import Path\\nimport lightgbm as lgb\\nfrom sklearn.model_selection import GroupKFold\\nfrom sklearn.metrics import roc_auc_score\\n\\nFEAT_COLS = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\", \\\"freq_entropy\\\", \\\"low_freq_ratio\\\",\\n]\\n\\nEXPERIMENTS = {\\n    \\\"mvp_001_qwen_rewrite\\\": \\\"data/features.csv\\\",\\n    \\\"exp_001_pythia\\\": \\\"data_exp001_pythia/features.csv\\\",\\n    \\\"exp_002_olmo\\\": \\\"data_exp002_olmo/features.csv\\\",\\n}\\n\\nN_BOOTSTRAP = 1000\\nN_PERMUTATION = 500\\nMAX_DEPTH = 5\\nSEED = 42\\n\\n\\ndef load_features(path):\\n    with open(path) as f:\\n        rows = list(csv.DictReader(f))\\n    depths = np.array([int(r[\\\"depth\\\"]) for r in rows])\\n    doc_ids = np.array([int(r[\\\"doc_id\\\"]) for r in rows])\\n    X = np.array([\\n        [float(r[c]) if r[c] not in (\\\"\\\", \\\"nan\\\") else np.nan for c in FEAT_COLS]\\n        for r in rows\\n    ])\\n    col_means = np.nanmean(X, axis=0)\\n    for j in range(X.shape[1]):\\n        mask = np.isnan(X[:, j])\\n        X[mask, j] = col_means[j]\\n    return depths, doc_ids, X\\n\\n\\ndef oof_predictions(X, y, groups):\\n    preds = np.zeros(len(y))\\n    for tr, te in GroupKFold(5).split(X, y, groups):\\n        clf = lgb.LGBMClassifier(\\n            n_estimators=200, max_depth=6, learning_rate=0.05,\\n            num_leaves=31, verbose=-1, n_jobs=-1,\\n        )\\n        clf.fit(X[tr], y[tr])\\n        preds[te] = clf.predict_proba(X[te])[:, 1]\\n    return preds\\n\\n\\ndef bootstrap_auc(y, preds, doc_ids, n, rng):\\n    unique = np.unique(doc_ids)\\n    doc_idx = {d: np.where(doc_ids == d)[0] for d in unique}\\n    aucs = np.empty(n)\\n    valid = 0\\n    for i in range(n):\\n        sampled = rng.choice(unique, size=len(unique), replace=True)\\n        idx = np.concatenate([doc_idx[d] for d in sampled])\\n        yb, pb = y[idx], preds[idx]\\n        if len(np.unique(yb)) < 2:\\n            continue\\n        aucs[valid] = roc_auc_score(yb, pb)\\n        valid += 1\\n    return aucs[:valid]\\n\\n\\ndef permutation_pvalue(y, preds, obs_auc, n, rng):\\n    count = 0\\n    for _ in range(n):\\n        yp = rng.permutation(y)\\n        if len(np.unique(yp)) < 2:\\n            continue\\n        count += (roc_auc_score(yp, preds) >= obs_auc)\\n    return count / n\\n\\n\\ndef main():\\n    base = Path(\\\"/root/autodl-tmp/gen-depth-contamination\\\")\\n    rng = np.random.default_rng(SEED)\\n    results = {}\\n\\n    t0 = time.time()\\n    for exp_name, feat_path in EXPERIMENTS.items():\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"  {exp_name}\\\")\\n        print(f\\\"{'='*60}\\\")\\n\\n        depths, doc_ids, X = load_features(base / feat_path)\\n        exp_results = {}\\n\\n        for k in range(1, MAX_DEPTH + 1):\\n            pair = f\\\"{k-1}v{k}\\\"\\n            mask = (depths == k - 1) | (depths == k)\\n            Xp, yp = X[mask], (depths[mask] == k).astype(int)\\n            gp = doc_ids[mask]\\n\\n            if len(np.unique(yp)) < 2:\\n                print(f\\\"  {pair}: skipped (single class)\\\")\\n                continue\\n\\n            t1 = time.time()\\n            preds = oof_predictions(Xp, yp, gp)\\n            obs_auc = roc_auc_score(yp, preds)\\n\\n            boot_aucs = bootstrap_auc(yp, preds, gp, N_BOOTSTRAP, rng)\\n            ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\\n            boot_mean = np.mean(boot_aucs)\\n            boot_std = np.std(boot_aucs)\\n\\n            pval = permutation_pvalue(yp, preds, obs_auc, N_PERMUTATION, rng)\\n            elapsed = time.time() - t1\\n\\n            exp_results[pair] = {\\n                \\\"mean_auc\\\": round(float(obs_auc), 4),\\n                \\\"boot_mean\\\": round(float(boot_mean), 4),\\n                \\\"boot_std\\\": round(float(boot_std), 4),\\n                \\\"ci_lower\\\": round(float(ci_lo), 4),\\n                \\\"ci_upper\\\": round(float(ci_hi), 4),\\n                \\\"ci_width\\\": round(float(ci_hi - ci_lo), 4),\\n                \\\"perm_pvalue\\\": float(pval),\\n                \\\"n_bootstrap\\\": N_BOOTSTRAP,\\n                \\\"n_permutation\\\": N_PERMUTATION,\\n            }\\n\\n            flag = \\\"\\\"\\n            if exp_name == \\\"exp_002_olmo\\\" and pair == \\\"1v2\\\":\\n                if ci_lo >= 0.60:\\n                    flag = \\\" [CI lower > 0.60, K* robust]\\\"\\n                elif ci_lo >= 0.55:\\n                    flag = \\\" [CI lower in (0.55, 0.60), K* borderline]\\\"\\n                else:\\n                    flag = \\\" [CI lower < 0.55, K* NOT robust]\\\"\\n\\n            pval_s = f\\\"<{1/N_PERMUTATION}\\\" if pval == 0 else f\\\"{pval:.4f}\\\"\\n            print(f\\\"  {pair}: AUC={obs_auc:.4f}  95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]  \\\"\\n                  f\\\"p={pval_s}  ({elapsed:.1f}s){flag}\\\")\\n\\n        results[exp_name] = exp_results\\n\\n    out_path = base / \\\"artifacts\\\" / \\\"bootstrap_ci_results.json\\\"\\n    out_path.parent.mkdir(parents=True, exist_ok=True)\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n\\n    total = time.time() - t0\\n    print(f\\\"\\\\n{'='*80}\\\")\\n    print(f\\\"SUMMARY TABLE  (total {total:.0f}s)\\\")\\n    print(f\\\"{'='*80}\\\")\\n    print(f\\\"{'Experiment':<25} {'Pair':>5} {'AUC':>7} {'95% CI':>22} {'Width':>7} {'p-value':>10}\\\")\\n    print(\\\"-\\\" * 80)\\n    for exp_name, exp_res in results.items():\\n        for pair, r in exp_res.items():\\n            pval_s = f\\\"<{1/N_PERMUTATION}\\\" if r[\\\"perm_pvalue\\\"] == 0 else f\\\"{r['perm_pvalue']:.4f}\\\"\\n            ci_str = f\\\"[{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\\\"\\n            print(f\\\"{exp_name:<25} {pair:>5} {r['mean_auc']:>7.4f} {ci_str:>22} {r['ci_width']:>7.4f} {pval_s:>10}\\\")\\n\\n    olmo_1v2 = results.get(\\\"exp_002_olmo\\\", {}).get(\\\"1v2\\\", {})\\n    if olmo_1v2:\\n        lo = olmo_1v2[\\\"ci_lower\\\"]\\n        print(f\\\"\\\\n*** KEY CHECK: OLMo 1v2 CI lower = {lo:.4f} \\\", end=\\\"\\\")\\n        if lo >= 0.60:\\n            print(\\\"(> 0.60, K* claim ROBUST)\\\")\\n        elif lo >= 0.55:\\n            print(\\\"(< 0.60 but > 0.55, K* BORDERLINE)\\\")\\n        else:\\n            print(\\\"(< 0.55, K* NOT ROBUST)\\\")\\n\\n    print(f\\\"\\\\nResults saved to {out_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me write the improved script. Key changes:

1. **Memory optimization**: Process per-dataset with model load/unload cycle (actually, since it's the same model for all datasets, I should load once, extract all embeddings, then unload - but the task says "逐模型处理" which means per-model. Since there's only one model, the key is to load model → extract embeddings for all datasets → unload model → then train MLPs. Actually, re-reading: "加载一个 frozen LLM → 提取 embeddings → del model + torch.cuda.empty_cache() → 再加载下一个". 

This implies if there were multiple models. Since there's only one model, the key change is to extract ALL embeddings first, then free the LLM before training MLPs.) The original code loads the LLM once and processes all datasets, which is fine since there's one model. The problem was that it kept the LLM in memory while also running MLP training. The fix should be: load the LLM, extract embeddings for all datasets, delete the LLM and clear the cache, then train MLPs on the embeddings so they don't coexist in GPU memory.

2. **Bootstrap CI**: Adapt from bootstrap_ci.py - resample doc_ids with replacement, compute AUC from OOF predictions
3. **Permutation test**: Shuffle labels, compute AUC, report p-value
4. **Peak VRAM logging**: reset_peak_memory_stats before fold, max_memory_allocated after
5. **Batch size auto-adapt**: Try default, if OOM halve, retry

Now I'm ready to write the new script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "025840a1-7828-4568-99d5-5a722f752c9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrM1e4BQcw2Y6QnRqGVCzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 35279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 27_

已获取完整脚本和 bootstrap 参考。现在编写改进版本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "95220c2e-be89-4cf9-8787-db511eb94c39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrM1e4BQcw2Y6QnRqGVCzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 35279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Write · `toolu_01TMDVsMk9hC14GQrMrNk8mD`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "735aeeb3-16a0-400e-aa35-a09904888225",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrM1e4BQcw2Y6QnRqGVCzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 35279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T03:04:39.601Z_

<details><summary>↩ Tool result · reported error · `toolu_01TMDVsMk9hC14GQrMrNk8mD`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "d6558c3b-c541-40a5-97de-4c875c4f05f5",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rd6KRG5799hC61PqV5rog6`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "f3b065d6-cbd3-46b9-a70c-bf0cef5b3fd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GUZwZ4hGAwx7yNy9bVRxfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7744,
      "cache_read_input_tokens": 38421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7744
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T03:04:43.296Z_

<details><summary>↩ Tool result · `toolu_01Rd6KRG5799hC61PqV5rog6`</summary>

```text
plot_exp003_decoding_ablation.py
run_cross_transfer.py
run_exp003_ablation.sh
run_exp009_dose_response.py
run_exp013_cross_transfer.py
run_exp015_neural_probe.py
run_pipeline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "76b0ea96-58c0-404c-846d-7a5b8ca125f9",
  "tool_use_result": {
    "stdout": "plot_exp003_decoding_ablation.py\nrun_cross_transfer.py\nrun_exp003_ablation.sh\nrun_exp009_dose_response.py\nrun_exp013_cross_transfer.py\nrun_exp015_neural_probe.py\nrun_pipeline.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01URHMQFrvk4zSAiFgcRb6o2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "0e0f3b9b-b28d-4a14-9f5c-3328c9f3cb7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKpWR2Qvv82qjMUuVE8cfT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 46165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
      },
      "output_tokens": 71,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T03:04:46.144Z_

<details><summary>↩ Tool result · `toolu_01URHMQFrvk4zSAiFgcRb6o2`</summary>

```text
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
59	def extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):
60	    """Frozen LLM last hidden state → average pool → (N, hidden_dim)."""
61	    all_emb = []
62	    for i in tqdm(range(0, len(texts), batch_size), desc="Embedding"):
63	        batch = texts[i : i + batch_size]
64	        inputs = tokenizer(
65	            batch,
66	            return_tensors="pt",
67	            padding=True,
68	            truncation=True,
69	            max_length=max_length,
70	        ).to(model.device)
71	
72	        out = model(**inputs, output_hidden_states=True)
73	        hidden = out.hidden_states[-1]  # (B, seq, dim)
74	        mask = inputs["attention_mask"].unsqueeze(-1).float()
75	        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
76	        all_emb.append(pooled.cpu().float().numpy())
77	
78	    return np.concatenate(all_emb, axis=0)
79	
80	
81	# ── MLP ───────────────────────────────────────────────────────────────
82	
83	class DepthMLP(nn.Module):
84	    def __init__(self, input_dim=1536, num_classes=6):
85	        super().__init__()
86	        self.net = nn.Sequential(
87	            nn.Linear(input_dim, 512),
88	            nn.ReLU(),
89	            nn.Dropout(0.1),
90	            nn.Linear(512, 256),
91	            nn.ReLU(),
92	            nn.Dropout(0.1),
93	            nn.Linear(256, num_classes),
94	        )
95	
96	    def forward(self, x):
97	        return self.net(x)
98	
99	
100	def train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,
101	              epochs=20, lr=1e-3, batch_size=256, patience=5, device="cuda"):
102	    """Train MLP with early stopping. Returns best model in eval mode."""
103	    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)
104	    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
105	    criterion = nn.CrossEntropyLoss()
106	
107	    ds = TensorDataset(
108	        torch.tensor(X_train, dtype=torch.float32),
109	        torch.tensor(y_train, dtype=torch.long),
110	    )
111	    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)
112	    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)
113	    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)
114	
115	    best_loss = float("inf")
116	    best_state = None
117	    wait = 0
118	
119	    for epoch in range(epochs):
120	        model.train()
121	        for xb, yb in loader:
122	            xb, yb = xb.to(device), yb.to(device)
123	            optimizer.zero_grad()
124	            criterion(model(xb), yb).backward()
125	            optimizer.step()
126	
127	        model.eval()
128	        with torch.no_grad():
129	            val_loss = criterion(model(X_val_t), y_val_t).item()
130	
131	        if val_loss < best_loss:
132	            best_loss = val_loss
133	            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
134	            wait = 0
135	        else:
136	            wait += 1
137	            if wait >= patience:
138	                break
139	
140	    model.load_state_dict(best_state)
141	    model.eval()
142	    return model
143	
144	
145	# ── Pairwise AUC ──────────────────────────────────────────────────────
146	
147	def compute_pairwise_auc(probas, depths, max_depth):
148	    """Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict)."""
149	    def _auc_pair(i, j):
150	        mask = (depths == i) | (depths == j)
151	        y = (depths[mask] == j).astype(int)
152	        if len(np.unique(y)) < 2 or mask.sum() < 4:
153	            return float("nan")
154	        p_i = probas[mask, i]
155	        p_j = probas[mask, j]
156	        score = p_j / (p_i + p_j + 1e-12)
157	        return round(float(roc_auc_score(y, score)), 4)
158	
159	    adjacent = {}
160	    for k in range(1, max_depth + 1):
161	        adjacent[f"{k-1}v{k}"] = _auc_pair(k - 1, k)
162	
163	    all_pairs = {}
164	    for i in range(max_depth + 1):
165	        for j in range(i + 1, max_depth + 1):
166	            all_pairs[f"{i}v{j}"] = _auc_pair(i, j)
167	
168	    return adjacent, all_pairs
169	
170	
171	# ── Single dataset experiment ─────────────────────────────────────────
172	
173	def run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):
174	    """Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC."""
175	    log.info(f"\n{'='*60}")
176	    log.info(f"Dataset: {label} ({data_dir})")
177	    log.info(f"{'='*60}")
178	
179	    texts, depths, doc_ids = load_depth_data(
180	        Path(data_dir), args.max_depth, args.num_samples,
181	    )
182	    if len(texts) == 0:
183	        log.error(f"No data in {data_dir}")
184	        return None
185	
186	    num_classes = int(depths.max()) + 1
187	
188	    # Extract embeddings
189	    embeddings = extract_embeddings(
190	        llm_model, tokenizer, texts,
191	        batch_size=args.embed_batch_size,
192	        max_length=args.max_length,
193	    )
194	    input_dim = embeddings.shape[1]
195	    log.info(f"Embeddings: {embeddings.shape}")
196	
197	    # 5-fold GroupKFold CV
198	    gkf = GroupKFold(n_splits=5)
199	    all_probas = np.zeros((len(depths), num_classes))
200	    fold_adj_aucs = {f"{k-1}v{k}": [] for k in range(1, num_classes)}
201	
202	    for fold, (tr_idx, te_idx) in enumerate(
203	        gkf.split(embeddings, depths, groups=doc_ids)
204	    ):
205	        log.info(f"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}")
206	        mlp = train_mlp(
207	            embeddings[tr_idx], depths[tr_idx],
208	            embeddings[te_idx], depths[te_idx],
209	            input_dim=input_dim, num_classes=num_classes,
210	            epochs=args.epochs, lr=args.lr,
211	            batch_size=args.mlp_batch_size,
212	            patience=args.patience, device=device,
213	        )
214	
215	        with torch.no_grad():
216	            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))
217	            probas = torch.softmax(logits, dim=-1).cpu().numpy()
218	
219	        all_probas[te_idx] = probas
220	
221	        # Per-fold adjacent AUC
222	        td = depths[te_idx]
223	        for k in range(1, num_classes):
224	            m = (td == k - 1) | (td == k)
225	            y = (td[m] == k).astype(int)
226	            if len(np.unique(y)) < 2 or m.sum() < 4:
227	                continue
228	            p0 = probas[m, k - 1]
229	            p1 = probas[m, k]
230	            s = p1 / (p0 + p1 + 1e-12)
231	            fold_adj_aucs[f"{k-1}v{k}"].append(round(float(roc_auc_score(y, s)), 4))
232	
233	        del mlp
234	        torch.cuda.empty_cache()
235	
236	    # Overall pairwise AUC
237	    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)
238	
239	    # K*
240	    k_star = 0
241	    for k in range(1, num_classes):
242	        if adj_auc.get(f"{k-1}v{k}", 0) > 0.60:
243	            k_star = k
244	
245	    accuracy = float((all_probas.argmax(axis=1) == depths).mean())
246	
247	    # Per-fold stats
248	    fold_stats = {}
249	    for key, aucs in fold_adj_aucs.items():
250	        if aucs:
251	            fold_stats[key] = {
252	                "mean": round(float(np.mean(aucs)), 4),
253	                "std": round(float(np.std(aucs)), 4),
254	                "folds": aucs,
255	            }
256	
257	    # Load baseline (hand-crafted features + LightGBM) if available
258	    baseline = None
259	    data_name = Path(data_dir).name
260	    results_name = data_name.replace("data_", "results_")
261	    baseline_path = Path(data_dir).parent / results_name / "pairwise_auc.json"
262	    if baseline_path.exists():
263	        with open(baseline_path) as f:
264	            baseline = json.load(f)
265	        log.info(f"  Loaded baseline from {baseline_path}")
266	
267	    result = {
268	        "dataset": label,
269	        "data_dir": str(data_dir),
270	        "num_samples_per_depth": args.num_samples if args.num_samples else "all",
271	        "max_depth": args.max_depth,
272	        "embedding_dim": input_dim,
273	        "mlp_arch": f"{input_dim}->512->256->{num_classes}",
274	        "neural_probe": {
275	            "pairwise_auc_adjacent": adj_auc,
276	            "pairwise_auc_all": all_auc,
277	            "fold_stats": fold_stats,
278	            "k_star": k_star,
279	            "k_star_threshold": 0.60,
280	            "classification_accuracy": round(accuracy, 4),
281	        },
282	    }
283	    if baseline:
284	        result["lgbm_baseline"] = {
285	            "pairwise_auc_adjacent": baseline["mean"],
286	            "k_star": max(
287	                (k for k in range(1, 6) if baseline["mean"].get(f"{k-1}v{k}", 0) > 0.60),
288	                default=0,
289	            ),
290	        }
291	
292	    # Log summary
293	    log.info(f"\n  K* (neural probe) = {k_star}")
294	    log.info(f"  Accuracy = {accuracy:.4f}")
295	    for k in range(1, num_classes):
296	        key = f"{k-1}v{k}"
297	        a = adj_auc.get(key, "N/A")
298	        fs = fold_stats.get(key, {})
299	        std = fs.get("std", 0)
300	        base = baseline["mean"].get(key, "—") if baseline else "—"
301	        log.info(f"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}")
302	
303	    return result
304	
305	
306	# ── Main ──────────────────────────────────────────────────────────────
307	
308	def main():
309	    parser = argparse.ArgumentParser(
310	        description="exp-015: Neural Probe for depth classification (frozen LLM + MLP)",
311	    )
312	    parser.add_argument(
313	        "--model_path", type=str,
314	        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct",
315	    )
316	    parser.add_argument("--data_dir", type=str, nargs="+",
317	                        default=["/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont"])
318	    parser.add_argument("--label", type=str, nargs="+", default=["Qwen-cont"])
319	    parser.add_argument(
320	        "--output", type=str,
321	        default="/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json",
322	    )
323	    parser.add_argument("--num_samples", type=int, default=None,
324	                        help="Max samples per depth (default: all)")
325	    parser.add_argument("--max_depth", type=int, default=5)
326	    parser.add_argument("--embed_batch_size", type=int, default=24)
327	    parser.add_argument("--max_length", type=int, default=512)
328	    parser.add_argument("--mlp_batch_size", type=int, default=256)
329	    parser.add_argument("--epochs", type=int, default=20)
330	    parser.add_argument("--lr", type=float, default=1e-3)
331	    parser.add_argument("--patience", type=int, default=5)
332	    parser.add_argument("--device", type=str, default="cuda:0")
333	    args = parser.parse_args()
334	
335	    if len(args.data_dir) != len(args.label):
336	        log.error("--data_dir and --label must have the same number of entries")
337	        sys.exit(1)
338	
339	    device = args.device if torch.cuda.is_available() else "cpu"
340	    log.info(f"Device: {device}")
341	    if torch.cuda.is_available():
342	        props = torch.cuda.get_device_properties(0)
343	        log.info(f"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)")
344	
345	    # Load LLM once for all datasets
346	    from transformers import AutoModelForCausalLM, AutoTokenizer
347	
348	    log.info(f"Loading model from {args.model_path} ...")
349	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
350	    if tokenizer.pad_token is None:
351	        tokenizer.pad_token = tokenizer.eos_token
352	        tokenizer.pad_token_id = tokenizer.eos_token_id
353	    tokenizer.padding_side = "right"
354	
355	    llm = AutoModelForCausalLM.from_pretrained(
356	        args.model_path,
357	        torch_dtype=torch.float16,
358	        device_map="auto",
359	        trust_remote_code=True,
360	    )
361	    llm.eval()
362	    log.info("Model loaded.")
363	
364	    # Run per-dataset
365	    all_results = []
366	    for dd, lab in zip(args.data_dir, args.label):
367	        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)
368	        if r:
369	            all_results.append(r)
370	
371	    # Free LLM
372	    del llm
373	    torch.cuda.empty_cache()
374	
375	    # Save
376	    out = Path(args.output)
377	    out.parent.mkdir(parents=True, exist_ok=True)
378	    with open(out, "w") as f:
379	        json.dump(all_results, f, indent=2, ensure_ascii=False)
380	    log.info(f"\nResults → {out}")
381	
382	    # Final summary
383	    log.info("\n" + "=" * 60)
384	    log.info("SUMMARY")
385	    log.info("=" * 60)
386	    for r in all_results:
387	        np_ks = r["neural_probe"]["k_star"]
388	        base_ks = r.get("lgbm_baseline", {}).get("k_star", "—")
389	        log.info(f"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}")
390	
391	    k_stars = [r["neural_probe"]["k_star"] for r in all_results]
392	    if len(k_stars) > 1:
393	        if all(k == k_stars[0] for k in k_stars):
394	            log.info(f"\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic")
395	        else:
396	            log.info(f"\n  K* varies: {k_stars}")
397	
398	
399	if __name__ == "__main__":
400	    main()
401	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "6362811e-d0cf-4322-9ed4-b7d6b83efd33",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
      "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ── Data loading ──────────────────────────────────────────────────────\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    \"\"\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\"\"\"\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# ── Embedding extraction ─────────────────────────────────────────────\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\n    \"\"\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\"\"\"\n    all_emb = []\n    for i in tqdm(range(0, len(texts), batch_size), desc=\"Embedding\"):\n        batch = texts[i : i + batch_size]\n        inputs = tokenizer(\n            batch,\n            return_tensors=\"pt\",\n            padding=True,\n            truncation=True,\n            max_length=max_length,\n        ).to(model.device)\n\n        out = model(**inputs, output_hidden_states=True)\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\n        mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n        all_emb.append(pooled.cpu().float().numpy())\n\n    return np.concatenate(all_emb, axis=0)\n\n\n# ── MLP ───────────────────────────────────────────────────────────────\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    \"\"\"Train MLP with early stopping. Returns best model in eval mode.\"\"\"\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# ── Pairwise AUC ──────────────────────────────────────────────────────\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    \"\"\"Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict).\"\"\"\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# ── Single dataset experiment ─────────────────────────────────────────\n\ndef run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):\n    \"\"\"Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    texts, depths, doc_ids = load_depth_data(\n        Path(data_dir), args.max_depth, args.num_samples,\n    )\n    if len(texts) == 0:\n        log.error(f\"No data in {data_dir}\")\n        return None\n\n    num_classes = int(depths.max()) + 1\n\n    # Extract embeddings\n    embeddings = extract_embeddings(\n        llm_model, tokenizer, texts,\n        batch_size=args.embed_batch_size,\n        max_length=args.max_length,\n    )\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}\")\n\n    # 5-fold GroupKFold CV\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        # Per-fold adjacent AUC\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Load baseline (hand-crafted features + LightGBM) if available\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n        },\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        fs = fold_stats.get(key, {})\n        std = fs.get(\"std\", 0)\n        base = baseline[\"mean\"].get(key, \"—\") if baseline else \"—\"\n        log.info(f\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\")\n\n    return result\n\n\n# ── Main ──────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=24)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Load LLM once for all datasets\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    # Run per-dataset\n    all_results = []\n    for dd, lab in zip(args.data_dir, args.label):\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\n        if r:\n            all_results.append(r)\n\n    # Free LLM\n    del llm\n    torch.cuda.empty_cache()\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults → {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"—\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 401,
      "startLine": 1,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Write · `toolu_01X6CkVXce4tfG7XjBBNGic6`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "d9c7093a-b5ae-4547-bbc0-1bbdc14cb935",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J8pzYhtS5HFFrsefMN6Qz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5755,
      "cache_read_input_tokens": 46329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5755
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T03:06:05.026Z_

<details><summary>↩ Tool result · `toolu_01X6CkVXce4tfG7XjBBNGic6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "28f7830f-1c50-46ee-8737-470a1f5b7ab7",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
    "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all text data (cheap, CPU only)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    embed_peak = None\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM before MLP training — this is the key memory optimization\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 14,
        "newStart": 3,
        "newLines": 18,
        "lines": [
          " ",
          " Validates that K*=2 (found with 15D hand-crafted features + LightGBM) is",
          " data-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B",
          "-embeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.",
          "+embeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.",
          "+",
          "+v2 changes: memory-optimized (extract all embeddings then free LLM),",
          "+bootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.",
          " \"\"\"",
          " ",
          " import argparse",
          "+import gc",
          " import json",
          " import logging",
          "-import os",
          " import sys",
          "+import time",
          " from pathlib import Path",
          " ",
          " import numpy as np"
        ]
      },
      {
        "oldStart": 29,
        "oldLines": 10,
        "newStart": 33,
        "newLines": 9,
        "lines": [
          " log = logging.getLogger(__name__)",
          " ",
          " ",
          "-# ── Data loading ──────────────────────────────────────────────────────",
          "+# -- Data loading ------------------------------------------------------",
          " ",
          " def load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):",
          "-    \"\"\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\"\"\"",
          "     texts, depths, doc_ids = [], [], []",
          "     for d in range(max_depth + 1):",
          "         path = data_dir / f\"depth_{d}.jsonl\""
        ]
      },
      {
        "oldStart": 53,
        "oldLines": 33,
        "newStart": 56,
        "newLines": 47,
        "lines": [
          "     return texts, np.array(depths), np.array(doc_ids)",
          " ",
          " ",
          "-# ── Embedding extraction ─────────────────────────────────────────────",
          "+# -- Embedding extraction with OOM retry ------------------------------",
          " ",
          " @torch.no_grad()",
          "-def extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):",
          "-    \"\"\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\"\"\"",
          "+def extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):",
          "+    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"",
          "     all_emb = []",
          "-    for i in tqdm(range(0, len(texts), batch_size), desc=\"Embedding\"):",
          "-        batch = texts[i : i + batch_size]",
          "-        inputs = tokenizer(",
          "-            batch,",
          "-            return_tensors=\"pt\",",
          "-            padding=True,",
          "-            truncation=True,",
          "-            max_length=max_length,",
          "-        ).to(model.device)",
          "+    actual_bs = batch_size",
          "+    i = 0",
          "+    pbar = tqdm(total=len(texts), desc=\"Embedding\")",
          "+    while i < len(texts):",
          "+        batch = texts[i : i + actual_bs]",
          "+        try:",
          "+            inputs = tokenizer(",
          "+                batch,",
          "+                return_tensors=\"pt\",",
          "+                padding=True,",
          "+                truncation=True,",
          "+                max_length=max_length,",
          "+            ).to(model.device)",
          "+            out = model(**inputs, output_hidden_states=True)",
          "+            hidden = out.hidden_states[-1]",
          "+            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()",
          "+            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)",
          "+            all_emb.append(pooled.cpu().float().numpy())",
          "+            pbar.update(len(batch))",
          "+            i += actual_bs",
          "+        except torch.cuda.OutOfMemoryError:",
          "+            torch.cuda.empty_cache()",
          "+            if actual_bs <= 1:",
          "+                pbar.close()",
          "+                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")",
          "+            old_bs = actual_bs",
          "+            actual_bs = max(1, actual_bs // 2)",
          "+            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")",
          "+    pbar.close()",
          "+    log.info(f\"Embedding done (effective batch_size={actual_bs})\")",
          "+    return np.concatenate(all_emb, axis=0), actual_bs",
          " ",
          "-        out = model(**inputs, output_hidden_states=True)",
          "-        hidden = out.hidden_states[-1]  # (B, seq, dim)",
          "-        mask = inputs[\"attention_mask\"].unsqueeze(-1).float()",
          "-        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)",
          "-        all_emb.append(pooled.cpu().float().numpy())",
          " ",
          "-    return np.concatenate(all_emb, axis=0)",
          "+# -- MLP ---------------------------------------------------------------",
          " ",
          "-",
          "-# ── MLP ───────────────────────────────────────────────────────────────",
          "-",
          " class DepthMLP(nn.Module):",
          "     def __init__(self, input_dim=1536, num_classes=6):",
          "         super().__init__()"
        ]
      },
      {
        "oldStart": 99,
        "oldLines": 7,
        "newStart": 116,
        "newLines": 6,
        "lines": [
          " ",
          " def train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,",
          "               epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):",
          "-    \"\"\"Train MLP with early stopping. Returns best model in eval mode.\"\"\"",
          "     model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)",
          "     optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)",
          "     criterion = nn.CrossEntropyLoss()"
        ]
      },
      {
        "oldStart": 142,
        "oldLines": 10,
        "newStart": 158,
        "newLines": 9,
        "lines": [
          "     return model",
          " ",
          " ",
          "-# ── Pairwise AUC ──────────────────────────────────────────────────────",
          "+# -- Pairwise AUC ------------------------------------------------------",
          " ",
          " def compute_pairwise_auc(probas, depths, max_depth):",
          "-    \"\"\"Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict).\"\"\"",
          "     def _auc_pair(i, j):",
          "         mask = (depths == i) | (depths == j)",
          "         y = (depths[mask] == j).astype(int)"
        ]
      },
      {
        "oldStart": 168,
        "oldLines": 41,
        "newStart": 183,
        "newLines": 104,
        "lines": [
          "     return adjacent, all_pairs",
          " ",
          " ",
          "-# ── Single dataset experiment ─────────────────────────────────────────",
          "+# -- Bootstrap CI (doc-level resampling) --------------------------------",
          " ",
          "-def run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):",
          "-    \"\"\"Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC.\"\"\"",
          "+def bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,",
          "+                     n_resamples=1000, seed=42):",
          "+    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"",
          "+    mask = (depths == pair_i) | (depths == pair_j)",
          "+    y = (depths[mask] == pair_j).astype(int)",
          "+    p_i = probas[mask, pair_i]",
          "+    p_j = probas[mask, pair_j]",
          "+    scores = p_j / (p_i + p_j + 1e-12)",
          "+    docs_masked = doc_ids[mask]",
          "+",
          "+    if len(np.unique(y)) < 2:",
          "+        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),",
          "+                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}",
          "+",
          "+    obs_auc = float(roc_auc_score(y, scores))",
          "+",
          "+    rng = np.random.default_rng(seed)",
          "+    unique_docs = np.unique(docs_masked)",
          "+    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}",
          "+",
          "+    boot_aucs = []",
          "+    for _ in range(n_resamples):",
          "+        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)",
          "+        idx = np.concatenate([doc_idx_map[d] for d in sampled])",
          "+        yb, sb = y[idx], scores[idx]",
          "+        if len(np.unique(yb)) < 2:",
          "+            continue",
          "+        boot_aucs.append(roc_auc_score(yb, sb))",
          "+",
          "+    boot_aucs = np.array(boot_aucs)",
          "+    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])",
          "+",
          "+    return {",
          "+        \"auc\": round(obs_auc, 4),",
          "+        \"ci_lower\": round(float(ci_lo), 4),",
          "+        \"ci_upper\": round(float(ci_hi), 4),",
          "+        \"boot_std\": round(float(np.std(boot_aucs)), 4),",
          "+        \"n_valid_resamples\": len(boot_aucs),",
          "+    }",
          "+",
          "+",
          "+# -- Permutation test ---------------------------------------------------",
          "+",
          "+def permutation_test_auc(depths, probas, pair_i, pair_j,",
          "+                         n_permutations=500, seed=43):",
          "+    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"",
          "+    mask = (depths == pair_i) | (depths == pair_j)",
          "+    y = (depths[mask] == pair_j).astype(int)",
          "+    p_i = probas[mask, pair_i]",
          "+    p_j = probas[mask, pair_j]",
          "+    scores = p_j / (p_i + p_j + 1e-12)",
          "+",
          "+    if len(np.unique(y)) < 2:",
          "+        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}",
          "+",
          "+    obs_auc = roc_auc_score(y, scores)",
          "+    rng = np.random.default_rng(seed)",
          "+    count_ge = 0",
          "+    for _ in range(n_permutations):",
          "+        yp = rng.permutation(y)",
          "+        if len(np.unique(yp)) < 2:",
          "+            continue",
          "+        count_ge += (roc_auc_score(yp, scores) >= obs_auc)",
          "+",
          "+    return {",
          "+        \"obs_auc\": round(float(obs_auc), 4),",
          "+        \"p_value\": round(count_ge / n_permutations, 4),",
          "+        \"n_permutations\": n_permutations,",
          "+    }",
          "+",
          "+",
          "+# -- Single dataset experiment ------------------------------------------",
          "+",
          "+def run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):",
          "+    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"",
          "     log.info(f\"\\n{'='*60}\")",
          "     log.info(f\"Dataset: {label} ({data_dir})\")",
          "     log.info(f\"{'='*60}\")",
          " ",
          "-    texts, depths, doc_ids = load_depth_data(",
          "-        Path(data_dir), args.max_depth, args.num_samples,",
          "-    )",
          "-    if len(texts) == 0:",
          "-        log.error(f\"No data in {data_dir}\")",
          "-        return None",
          "-",
          "     num_classes = int(depths.max()) + 1",
          "-",
          "-    # Extract embeddings",
          "-    embeddings = extract_embeddings(",
          "-        llm_model, tokenizer, texts,",
          "-        batch_size=args.embed_batch_size,",
          "-        max_length=args.max_length,",
          "-    )",
          "     input_dim = embeddings.shape[1]",
          "-    log.info(f\"Embeddings: {embeddings.shape}\")",
          "+    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")",
          " ",
          "-    # 5-fold GroupKFold CV",
          "     gkf = GroupKFold(n_splits=5)",
          "     all_probas = np.zeros((len(depths), num_classes))",
          "     fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}",
          "+    peak_vram_mb = []",
          " ",
          "     for fold, (tr_idx, te_idx) in enumerate(",
          "         gkf.split(embeddings, depths, groups=doc_ids)",
          "     ):",
          "         log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")",
          "+",
          "+        if torch.cuda.is_available():",
          "+            torch.cuda.reset_peak_memory_stats(device)",
          "+",
          "         mlp = train_mlp(",
          "             embeddings[tr_idx], depths[tr_idx],",
          "             embeddings[te_idx], depths[te_idx],"
        ]
      },
      {
        "oldStart": 218,
        "oldLines": 7,
        "newStart": 296,
        "newLines": 6,
        "lines": [
          " ",
          "         all_probas[te_idx] = probas",
          " ",
          "-        # Per-fold adjacent AUC",
          "         td = depths[te_idx]",
          "         for k in range(1, num_classes):",
          "             m = (td == k - 1) | (td == k)"
        ]
      },
      {
        "oldStart": 230,
        "oldLines": 6,
        "newStart": 307,
        "newLines": 11,
        "lines": [
          "             s = p1 / (p0 + p1 + 1e-12)",
          "             fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))",
          " ",
          "+        if torch.cuda.is_available():",
          "+            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)",
          "+            peak_vram_mb.append(round(peak, 1))",
          "+            log.info(f\"    Peak VRAM: {peak:.1f} MB\")",
          "+",
          "         del mlp",
          "         torch.cuda.empty_cache()",
          " "
        ]
      },
      {
        "oldStart": 254,
        "oldLines": 7,
        "newStart": 336,
        "newLines": 32,
        "lines": [
          "                 \"folds\": aucs,",
          "             }",
          " ",
          "-    # Load baseline (hand-crafted features + LightGBM) if available",
          "+    # Bootstrap CI",
          "+    log.info(\"  Computing bootstrap CI ...\")",
          "+    bootstrap_results = {}",
          "+    for k in range(1, num_classes):",
          "+        pair = f\"{k-1}v{k}\"",
          "+        ci = bootstrap_auc_ci(",
          "+            depths, all_probas, k - 1, k, doc_ids,",
          "+            n_resamples=args.bootstrap_resamples,",
          "+        )",
          "+        bootstrap_results[pair] = ci",
          "+        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")",
          "+",
          "+    # Permutation test",
          "+    log.info(\"  Computing permutation tests ...\")",
          "+    permutation_results = {}",
          "+    for k in range(1, num_classes):",
          "+        pair = f\"{k-1}v{k}\"",
          "+        pt = permutation_test_auc(",
          "+            depths, all_probas, k - 1, k,",
          "+            n_permutations=args.permutation_resamples,",
          "+        )",
          "+        permutation_results[pair] = pt",
          "+        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"",
          "+        log.info(f\"    {pair}: p={pval_s}\")",
          "+",
          "+    # Load baseline",
          "     baseline = None",
          "     data_name = Path(data_dir).name",
          "     results_name = data_name.replace(\"data_\", \"results_\")"
        ]
      },
      {
        "oldStart": 278,
        "oldLines": 7,
        "newStart": 385,
        "newLines": 11,
        "lines": [
          "             \"k_star\": k_star,",
          "             \"k_star_threshold\": 0.60,",
          "             \"classification_accuracy\": round(accuracy, 4),",
          "+            \"bootstrap_ci\": bootstrap_results,",
          "+            \"permutation_test\": permutation_results,",
          "         },",
          "+        \"peak_vram_mb\": peak_vram_mb,",
          "+        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,",
          "     }",
          "     if baseline:",
          "         result[\"lgbm_baseline\"] = {"
        ]
      },
      {
        "oldStart": 292,
        "oldLines": 18,
        "newStart": 403,
        "newLines": 23,
        "lines": [
          "     # Log summary",
          "     log.info(f\"\\n  K* (neural probe) = {k_star}\")",
          "     log.info(f\"  Accuracy = {accuracy:.4f}\")",
          "+    if peak_vram_mb:",
          "+        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")",
          "     for k in range(1, num_classes):",
          "         key = f\"{k-1}v{k}\"",
          "         a = adj_auc.get(key, \"N/A\")",
          "-        fs = fold_stats.get(key, {})",
          "-        std = fs.get(\"std\", 0)",
          "-        base = baseline[\"mean\"].get(key, \"—\") if baseline else \"—\"",
          "-        log.info(f\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\")",
          "+        ci = bootstrap_results.get(key, {})",
          "+        ci_lo = ci.get(\"ci_lower\", \"?\")",
          "+        ci_hi = ci.get(\"ci_upper\", \"?\")",
          "+        pt = permutation_results.get(key, {})",
          "+        pv = pt.get(\"p_value\", \"?\")",
          "+        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"",
          "+        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")",
          " ",
          "     return result",
          " ",
          " ",
          "-# ── Main ──────────────────────────────────────────────────────────────",
          "+# -- Main ---------------------------------------------------------------",
          " ",
          " def main():",
          "     parser = argparse.ArgumentParser("
        ]
      },
      {
        "oldStart": 323,
        "oldLines": 13,
        "newStart": 439,
        "newLines": 15,
        "lines": [
          "     parser.add_argument(\"--num_samples\", type=int, default=None,",
          "                         help=\"Max samples per depth (default: all)\")",
          "     parser.add_argument(\"--max_depth\", type=int, default=5)",
          "-    parser.add_argument(\"--embed_batch_size\", type=int, default=24)",
          "+    parser.add_argument(\"--embed_batch_size\", type=int, default=16)",
          "     parser.add_argument(\"--max_length\", type=int, default=512)",
          "     parser.add_argument(\"--mlp_batch_size\", type=int, default=256)",
          "     parser.add_argument(\"--epochs\", type=int, default=20)",
          "     parser.add_argument(\"--lr\", type=float, default=1e-3)",
          "     parser.add_argument(\"--patience\", type=int, default=5)",
          "     parser.add_argument(\"--device\", type=str, default=\"cuda:0\")",
          "+    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)",
          "+    parser.add_argument(\"--permutation_resamples\", type=int, default=500)",
          "     args = parser.parse_args()",
          " ",
          "     if len(args.data_dir) != len(args.label):"
        ]
      },
      {
        "oldStart": 342,
        "oldLines": 7,
        "newStart": 460,
        "newLines": 25,
        "lines": [
          "         props = torch.cuda.get_device_properties(0)",
          "         log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")",
          " ",
          "-    # Load LLM once for all datasets",
          "+    # Phase 1: Load all text data (cheap, CPU only)",
          "+    dataset_info = []",
          "+    for dd, lab in zip(args.data_dir, args.label):",
          "+        texts, depths, doc_ids = load_depth_data(",
          "+            Path(dd), args.max_depth, args.num_samples,",
          "+        )",
          "+        if len(texts) == 0:",
          "+            log.error(f\"No data in {dd}\")",
          "+            continue",
          "+        dataset_info.append({",
          "+            \"data_dir\": dd, \"label\": lab,",
          "+            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,",
          "+        })",
          "+",
          "+    if not dataset_info:",
          "+        log.error(\"No valid datasets found\")",
          "+        sys.exit(1)",
          "+",
          "+    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM",
          "     from transformers import AutoModelForCausalLM, AutoTokenizer",
          " ",
          "     log.info(f\"Loading model from {args.model_path} ...\")"
        ]
      },
      {
        "oldStart": 361,
        "oldLines": 23,
        "newStart": 497,
        "newLines": 51,
        "lines": [
          "     llm.eval()",
          "     log.info(\"Model loaded.\")",
          " ",
          "-    # Run per-dataset",
          "+    if torch.cuda.is_available():",
          "+        torch.cuda.reset_peak_memory_stats(device)",
          "+",
          "+    for ds in dataset_info:",
          "+        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")",
          "+        emb, actual_bs = extract_embeddings(",
          "+            llm, tokenizer, ds[\"texts\"],",
          "+            batch_size=args.embed_batch_size,",
          "+            max_length=args.max_length,",
          "+        )",
          "+        ds[\"embeddings\"] = emb",
          "+        ds[\"actual_embed_bs\"] = actual_bs",
          "+        log.info(f\"  shape={emb.shape}\")",
          "+",
          "+    embed_peak = None",
          "+    if torch.cuda.is_available():",
          "+        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)",
          "+        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")",
          "+",
          "+    # Free LLM before MLP training — this is the key memory optimization",
          "+    del llm, tokenizer",
          "+    gc.collect()",
          "+    torch.cuda.empty_cache()",
          "+    if torch.cuda.is_available():",
          "+        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)",
          "+        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")",
          "+",
          "+    # Phase 3: Train MLP probes (LLM no longer in memory)",
          "     all_results = []",
          "-    for dd, lab in zip(args.data_dir, args.label):",
          "-        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)",
          "+    for ds in dataset_info:",
          "+        r = run_one_dataset(",
          "+            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],",
          "+            ds[\"label\"], ds[\"data_dir\"], args, device,",
          "+        )",
          "         if r:",
          "+            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]",
          "+            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None",
          "             all_results.append(r)",
          " ",
          "-    # Free LLM",
          "-    del llm",
          "-    torch.cuda.empty_cache()",
          "-",
          "     # Save",
          "     out = Path(args.output)",
          "     out.parent.mkdir(parents=True, exist_ok=True)",
          "     with open(out, \"w\") as f:",
          "         json.dump(all_results, f, indent=2, ensure_ascii=False)",
          "-    log.info(f\"\\nResults → {out}\")",
          "+    log.info(f\"\\nResults -> {out}\")",
          " ",
          "     # Final summary",
          "     log.info(\"\\n\" + \"=\" * 60)"
        ]
      },
      {
        "oldStart": 385,
        "oldLines": 13,
        "newStart": 549,
        "newLines": 19,
        "lines": [
          "     log.info(\"=\" * 60)",
          "     for r in all_results:",
          "         np_ks = r[\"neural_probe\"][\"k_star\"]",
          "-        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"—\")",
          "+        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")",
          "         log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")",
          " ",
          "+        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():",
          "+            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})",
          "+            pv = pt.get(\"p_value\", \"?\")",
          "+            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"",
          "+            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")",
          "+",
          "     k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]",
          "     if len(k_stars) > 1:",
          "         if all(k == k_stars[0] for k in k_stars):",
          "-            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\")",
          "+            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")",
          "         else:",
          "             log.info(f\"\\n  K* varies: {k_stars}\")",
          " "
        ]
      }
    ],
    "originalFile": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool → 1536-dim) + MLP classifier.\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ── Data loading ──────────────────────────────────────────────────────\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    \"\"\"Load depth_0..max_depth JSONL files. Returns texts, depths, doc_ids.\"\"\"\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# ── Embedding extraction ─────────────────────────────────────────────\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=24, max_length=512):\n    \"\"\"Frozen LLM last hidden state → average pool → (N, hidden_dim).\"\"\"\n    all_emb = []\n    for i in tqdm(range(0, len(texts), batch_size), desc=\"Embedding\"):\n        batch = texts[i : i + batch_size]\n        inputs = tokenizer(\n            batch,\n            return_tensors=\"pt\",\n            padding=True,\n            truncation=True,\n            max_length=max_length,\n        ).to(model.device)\n\n        out = model(**inputs, output_hidden_states=True)\n        hidden = out.hidden_states[-1]  # (B, seq, dim)\n        mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n        all_emb.append(pooled.cpu().float().numpy())\n\n    return np.concatenate(all_emb, axis=0)\n\n\n# ── MLP ───────────────────────────────────────────────────────────────\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    \"\"\"Train MLP with early stopping. Returns best model in eval mode.\"\"\"\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# ── Pairwise AUC ──────────────────────────────────────────────────────\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    \"\"\"Pairwise AUC from multi-class softmax. Returns (adjacent_dict, all_pairs_dict).\"\"\"\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# ── Single dataset experiment ─────────────────────────────────────────\n\ndef run_one_dataset(data_dir, label, llm_model, tokenizer, args, device):\n    \"\"\"Full pipeline for one dataset: embed → 5-fold MLP → pairwise AUC.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    texts, depths, doc_ids = load_depth_data(\n        Path(data_dir), args.max_depth, args.num_samples,\n    )\n    if len(texts) == 0:\n        log.error(f\"No data in {data_dir}\")\n        return None\n\n    num_classes = int(depths.max()) + 1\n\n    # Extract embeddings\n    embeddings = extract_embeddings(\n        llm_model, tokenizer, texts,\n        batch_size=args.embed_batch_size,\n        max_length=args.max_length,\n    )\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}\")\n\n    # 5-fold GroupKFold CV\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        # Per-fold adjacent AUC\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Load baseline (hand-crafted features + LightGBM) if available\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n        },\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        fs = fold_stats.get(key, {})\n        std = fs.get(\"std\", 0)\n        base = baseline[\"mean\"].get(key, \"—\") if baseline else \"—\"\n        log.info(f\"  AUC({k-1}v{k}): neural={a} ± {std:.4f}  lgbm={base}\")\n\n    return result\n\n\n# ── Main ──────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=24)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Load LLM once for all datasets\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    # Run per-dataset\n    all_results = []\n    for dd, lab in zip(args.data_dir, args.label):\n        r = run_one_dataset(dd, lab, llm, tokenizer, args, device)\n        if r:\n            all_results.append(r)\n\n    # Free LLM\n    del llm\n    torch.cuda.empty_cache()\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults → {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"—\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets → boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 36_

现在把脚本同步到服务器并 dry-run 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "1ca2b22c-336f-4901-ad73-0a343e4061f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7Ksd5fnQ1kjQ75iGo4Zcf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7232,
      "cache_read_input_tokens": 52084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7232
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ai672wa9oqxvKpnvEbhcB9`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "dbe86ffa-0639-4f46-83c3-613a44b62736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7Ksd5fnQ1kjQ75iGo4Zcf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7232,
      "cache_read_input_tokens": 52084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7232
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T03:06:09.133Z_

<details><summary>↩ Tool result · `toolu_01Ai672wa9oqxvKpnvEbhcB9`</summary>

```text
570
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "6e226c73-65da-452f-9f87-b203b4305021",
  "tool_use_result": {
    "stdout": "570",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01LqcRv9PgMPtDmJP814Ra7X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "e59a8029-1b3d-43cd-9eee-946cd00f2f6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYbXUPyBfWTXtwrmume7PS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 59316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T03:06:11.633Z_

<details><summary>↩ Tool result · `toolu_01LqcRv9PgMPtDmJP814Ra7X`</summary>

```text
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
59	# -- Embedding extraction with OOM retry ------------------------------
60	
61	@torch.no_grad()
62	def extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):
63	    """Auto-halves batch_size on OOM until batch_size=1."""
64	    all_emb = []
65	    actual_bs = batch_size
66	    i = 0
67	    pbar = tqdm(total=len(texts), desc="Embedding")
68	    while i < len(texts):
69	        batch = texts[i : i + actual_bs]
70	        try:
71	            inputs = tokenizer(
72	                batch,
73	                return_tensors="pt",
74	                padding=True,
75	                truncation=True,
76	                max_length=max_length,
77	            ).to(model.device)
78	            out = model(**inputs, output_hidden_states=True)
79	            hidden = out.hidden_states[-1]
80	            mask = inputs["attention_mask"].unsqueeze(-1).float()
81	            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
82	            all_emb.append(pooled.cpu().float().numpy())
83	            pbar.update(len(batch))
84	            i += actual_bs
85	        except torch.cuda.OutOfMemoryError:
86	            torch.cuda.empty_cache()
87	            if actual_bs <= 1:
88	                pbar.close()
89	                raise RuntimeError(f"OOM even at batch_size=1 on sample {i}")
90	            old_bs = actual_bs
91	            actual_bs = max(1, actual_bs // 2)
92	            log.warning(f"OOM at batch_size={old_bs}, retrying with {actual_bs}")
93	    pbar.close()
94	    log.info(f"Embedding done (effective batch_size={actual_bs})")
95	    return np.concatenate(all_emb, axis=0), actual_bs
96	
97	
98	# -- MLP ---------------------------------------------------------------
99	
100	class DepthMLP(nn.Module):
101	    def __init__(self, input_dim=1536, num_classes=6):
102	        super().__init__()
103	        self.net = nn.Sequential(
104	            nn.Linear(input_dim, 512),
105	            nn.ReLU(),
106	            nn.Dropout(0.1),
107	            nn.Linear(512, 256),
108	            nn.ReLU(),
109	            nn.Dropout(0.1),
110	            nn.Linear(256, num_classes),
111	        )
112	
113	    def forward(self, x):
114	        return self.net(x)
115	
116	
117	def train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,
118	              epochs=20, lr=1e-3, batch_size=256, patience=5, device="cuda"):
119	    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)
120	    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
121	    criterion = nn.CrossEntropyLoss()
122	
123	    ds = TensorDataset(
124	        torch.tensor(X_train, dtype=torch.float32),
125	        torch.tensor(y_train, dtype=torch.long),
126	    )
127	    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)
128	    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)
129	    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)
130	
131	    best_loss = float("inf")
132	    best_state = None
133	    wait = 0
134	
135	    for epoch in range(epochs):
136	        model.train()
137	        for xb, yb in loader:
138	            xb, yb = xb.to(device), yb.to(device)
139	            optimizer.zero_grad()
140	            criterion(model(xb), yb).backward()
141	            optimizer.step()
142	
143	        model.eval()
144	        with torch.no_grad():
145	            val_loss = criterion(model(X_val_t), y_val_t).item()
146	
147	        if val_loss < best_loss:
148	            best_loss = val_loss
149	            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
150	            wait = 0
151	        else:
152	            wait += 1
153	            if wait >= patience:
154	                break
155	
156	    model.load_state_dict(best_state)
157	    model.eval()
158	    return model
159	
160	
161	# -- Pairwise AUC ------------------------------------------------------
162	
163	def compute_pairwise_auc(probas, depths, max_depth):
164	    def _auc_pair(i, j):
165	        mask = (depths == i) | (depths == j)
166	        y = (depths[mask] == j).astype(int)
167	        if len(np.unique(y)) < 2 or mask.sum() < 4:
168	            return float("nan")
169	        p_i = probas[mask, i]
170	        p_j = probas[mask, j]
171	        score = p_j / (p_i + p_j + 1e-12)
172	        return round(float(roc_auc_score(y, score)), 4)
173	
174	    adjacent = {}
175	    for k in range(1, max_depth + 1):
176	        adjacent[f"{k-1}v{k}"] = _auc_pair(k - 1, k)
177	
178	    all_pairs = {}
179	    for i in range(max_depth + 1):
180	        for j in range(i + 1, max_depth + 1):
181	            all_pairs[f"{i}v{j}"] = _auc_pair(i, j)
182	
183	    return adjacent, all_pairs
184	
185	
186	# -- Bootstrap CI (doc-level resampling) --------------------------------
187	
188	def bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,
189	                     n_resamples=1000, seed=42):
190	    """Percentile bootstrap 95% CI, resampling at doc level to respect grouping."""
191	    mask = (depths == pair_i) | (depths == pair_j)
192	    y = (depths[mask] == pair_j).astype(int)
193	    p_i = probas[mask, pair_i]
194	    p_j = probas[mask, pair_j]
195	    scores = p_j / (p_i + p_j + 1e-12)
196	    docs_masked = doc_ids[mask]
197	
198	    if len(np.unique(y)) < 2:
199	        return {"auc": float("nan"), "ci_lower": float("nan"),
200	                "ci_upper": float("nan"), "boot_std": float("nan")}
201	
202	    obs_auc = float(roc_auc_score(y, scores))
203	
204	    rng = np.random.default_rng(seed)
205	    unique_docs = np.unique(docs_masked)
206	    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}
207	
208	    boot_aucs = []
209	    for _ in range(n_resamples):
210	        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)
211	        idx = np.concatenate([doc_idx_map[d] for d in sampled])
212	        yb, sb = y[idx], scores[idx]
213	        if len(np.unique(yb)) < 2:
214	            continue
215	        boot_aucs.append(roc_auc_score(yb, sb))
216	
217	    boot_aucs = np.array(boot_aucs)
218	    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])
219	
220	    return {
221	        "auc": round(obs_auc, 4),
222	        "ci_lower": round(float(ci_lo), 4),
223	        "ci_upper": round(float(ci_hi), 4),
224	        "boot_std": round(float(np.std(boot_aucs)), 4),
225	        "n_valid_resamples": len(boot_aucs),
226	    }
227	
228	
229	# -- Permutation test ---------------------------------------------------
230	
231	def permutation_test_auc(depths, probas, pair_i, pair_j,
232	                         n_permutations=500, seed=43):
233	    """Shuffle binary labels, report fraction of permuted AUC >= observed."""
234	    mask = (depths == pair_i) | (depths == pair_j)
235	    y = (depths[mask] == pair_j).astype(int)
236	    p_i = probas[mask, pair_i]
237	    p_j = probas[mask, pair_j]
238	    scores = p_j / (p_i + p_j + 1e-12)
239	
240	    if len(np.unique(y)) < 2:
241	        return {"p_value": float("nan"), "obs_auc": float("nan")}
242	
243	    obs_auc = roc_auc_score(y, scores)
244	    rng = np.random.default_rng(seed)
245	    count_ge = 0
246	    for _ in range(n_permutations):
247	        yp = rng.permutation(y)
248	        if len(np.unique(yp)) < 2:
249	            continue
250	        count_ge += (roc_auc_score(yp, scores) >= obs_auc)
251	
252	    return {
253	        "obs_auc": round(float(obs_auc), 4),
254	        "p_value": round(count_ge / n_permutations, 4),
255	        "n_permutations": n_permutations,
256	    }
257	
258	
259	# -- Single dataset experiment ------------------------------------------
260	
261	def run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):
262	    """MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test."""
263	    log.info(f"\n{'='*60}")
264	    log.info(f"Dataset: {label} ({data_dir})")
265	    log.info(f"{'='*60}")
266	
267	    num_classes = int(depths.max()) + 1
268	    input_dim = embeddings.shape[1]
269	    log.info(f"Embeddings: {embeddings.shape}, classes: {num_classes}")
270	
271	    gkf = GroupKFold(n_splits=5)
272	    all_probas = np.zeros((len(depths), num_classes))
273	    fold_adj_aucs = {f"{k-1}v{k}": [] for k in range(1, num_classes)}
274	    peak_vram_mb = []
275	
276	    for fold, (tr_idx, te_idx) in enumerate(
277	        gkf.split(embeddings, depths, groups=doc_ids)
278	    ):
279	        log.info(f"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}")
280	
281	        if torch.cuda.is_available():
282	            torch.cuda.reset_peak_memory_stats(device)
283	
284	        mlp = train_mlp(
285	            embeddings[tr_idx], depths[tr_idx],
286	            embeddings[te_idx], depths[te_idx],
287	            input_dim=input_dim, num_classes=num_classes,
288	            epochs=args.epochs, lr=args.lr,
289	            batch_size=args.mlp_batch_size,
290	            patience=args.patience, device=device,
291	        )
292	
293	        with torch.no_grad():
294	            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))
295	            probas = torch.softmax(logits, dim=-1).cpu().numpy()
296	
297	        all_probas[te_idx] = probas
298	
299	        td = depths[te_idx]
300	        for k in range(1, num_classes):
301	            m = (td == k - 1) | (td == k)
302	            y = (td[m] == k).astype(int)
303	            if len(np.unique(y)) < 2 or m.sum() < 4:
304	                continue
305	            p0 = probas[m, k - 1]
306	            p1 = probas[m, k]
307	            s = p1 / (p0 + p1 + 1e-12)
308	            fold_adj_aucs[f"{k-1}v{k}"].append(round(float(roc_auc_score(y, s)), 4))
309	
310	        if torch.cuda.is_available():
311	            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)
312	            peak_vram_mb.append(round(peak, 1))
313	            log.info(f"    Peak VRAM: {peak:.1f} MB")
314	
315	        del mlp
316	        torch.cuda.empty_cache()
317	
318	    # Overall pairwise AUC
319	    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)
320	
321	    # K*
322	    k_star = 0
323	    for k in range(1, num_classes):
324	        if adj_auc.get(f"{k-1}v{k}", 0) > 0.60:
325	            k_star = k
326	
327	    accuracy = float((all_probas.argmax(axis=1) == depths).mean())
328	
329	    # Per-fold stats
330	    fold_stats = {}
331	    for key, aucs in fold_adj_aucs.items():
332	        if aucs:
333	            fold_stats[key] = {
334	                "mean": round(float(np.mean(aucs)), 4),
335	                "std": round(float(np.std(aucs)), 4),
336	                "folds": aucs,
337	            }
338	
339	    # Bootstrap CI
340	    log.info("  Computing bootstrap CI ...")
341	    bootstrap_results = {}
342	    for k in range(1, num_classes):
343	        pair = f"{k-1}v{k}"
344	        ci = bootstrap_auc_ci(
345	            depths, all_probas, k - 1, k, doc_ids,
346	            n_resamples=args.bootstrap_resamples,
347	        )
348	        bootstrap_results[pair] = ci
349	        log.info(f"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]")
350	
351	    # Permutation test
352	    log.info("  Computing permutation tests ...")
353	    permutation_results = {}
354	    for k in range(1, num_classes):
355	        pair = f"{k-1}v{k}"
356	        pt = permutation_test_auc(
357	            depths, all_probas, k - 1, k,
358	            n_permutations=args.permutation_resamples,
359	        )
360	        permutation_results[pair] = pt
361	        pval_s = f"<{1/args.permutation_resamples}" if pt["p_value"] == 0 else f"{pt['p_value']:.4f}"
362	        log.info(f"    {pair}: p={pval_s}")
363	
364	    # Load baseline
365	    baseline = None
366	    data_name = Path(data_dir).name
367	    results_name = data_name.replace("data_", "results_")
368	    baseline_path = Path(data_dir).parent / results_name / "pairwise_auc.json"
369	    if baseline_path.exists():
370	        with open(baseline_path) as f:
371	            baseline = json.load(f)
372	        log.info(f"  Loaded baseline from {baseline_path}")
373	
374	    result = {
375	        "dataset": label,
376	        "data_dir": str(data_dir),
377	        "num_samples_per_depth": args.num_samples if args.num_samples else "all",
378	        "max_depth": args.max_depth,
379	        "embedding_dim": input_dim,
380	        "mlp_arch": f"{input_dim}->512->256->{num_classes}",
381	        "neural_probe": {
382	            "pairwise_auc_adjacent": adj_auc,
383	            "pairwise_auc_all": all_auc,
384	            "fold_stats": fold_stats,
385	            "k_star": k_star,
386	            "k_star_threshold": 0.60,
387	            "classification_accuracy": round(accuracy, 4),
388	            "bootstrap_ci": bootstrap_results,
389	            "permutation_test": permutation_results,
390	        },
391	        "peak_vram_mb": peak_vram_mb,
392	        "peak_vram_max_mb": max(peak_vram_mb) if peak_vram_mb else None,
393	    }
394	    if baseline:
395	        result["lgbm_baseline"] = {
396	            "pairwise_auc_adjacent": baseline["mean"],
397	            "k_star": max(
398	                (k for k in range(1, 6) if baseline["mean"].get(f"{k-1}v{k}", 0) > 0.60),
399	                default=0,
400	            ),
401	        }
402	
403	    # Log summary
404	    log.info(f"\n  K* (neural probe) = {k_star}")
405	    log.info(f"  Accuracy = {accuracy:.4f}")
406	    if peak_vram_mb:
407	        log.info(f"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB")
408	    for k in range(1, num_classes):
409	        key = f"{k-1}v{k}"
410	        a = adj_auc.get(key, "N/A")
411	        ci = bootstrap_results.get(key, {})
412	        ci_lo = ci.get("ci_lower", "?")
413	        ci_hi = ci.get("ci_upper", "?")
414	        pt = permutation_results.get(key, {})
415	        pv = pt.get("p_value", "?")
416	        base = baseline["mean"].get(key, "-") if baseline else "-"
417	        log.info(f"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}")
418	
419	    return result
420	
421	
422	# -- Main ---------------------------------------------------------------
423	
424	def main():
425	    parser = argparse.ArgumentParser(
426	        description="exp-015: Neural Probe for depth classification (frozen LLM + MLP)",
427	    )
428	    parser.add_argument(
429	        "--model_path", type=str,
430	        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct",
431	    )
432	    parser.add_argument("--data_dir", type=str, nargs="+",
433	                        default=["/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont"])
434	    parser.add_argument("--label", type=str, nargs="+", default=["Qwen-cont"])
435	    parser.add_argument(
436	        "--output", type=str,
437	        default="/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json",
438	    )
439	    parser.add_argument("--num_samples", type=int, default=None,
440	                        help="Max samples per depth (default: all)")
441	    parser.add_argument("--max_depth", type=int, default=5)
442	    parser.add_argument("--embed_batch_size", type=int, default=16)
443	    parser.add_argument("--max_length", type=int, default=512)
444	    parser.add_argument("--mlp_batch_size", type=int, default=256)
445	    parser.add_argument("--epochs", type=int, default=20)
446	    parser.add_argument("--lr", type=float, default=1e-3)
447	    parser.add_argument("--patience", type=int, default=5)
448	    parser.add_argument("--device", type=str, default="cuda:0")
449	    parser.add_argument("--bootstrap_resamples", type=int, default=1000)
450	    parser.add_argument("--permutation_resamples", type=int, default=500)
451	    args = parser.parse_args()
452	
453	    if len(args.data_dir) != len(args.label):
454	        log.error("--data_dir and --label must have the same number of entries")
455	        sys.exit(1)
456	
457	    device = args.device if torch.cuda.is_available() else "cpu"
458	    log.info(f"Device: {device}")
459	    if torch.cuda.is_available():
460	        props = torch.cuda.get_device_properties(0)
461	        log.info(f"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)")
462	
463	    # Phase 1: Load all text data (cheap, CPU only)
464	    dataset_info = []
465	    for dd, lab in zip(args.data_dir, args.label):
466	        texts, depths, doc_ids = load_depth_data(
467	            Path(dd), args.max_depth, args.num_samples,
468	        )
469	        if len(texts) == 0:
470	            log.error(f"No data in {dd}")
471	            continue
472	        dataset_info.append({
473	            "data_dir": dd, "label": lab,
474	            "texts": texts, "depths": depths, "doc_ids": doc_ids,
475	        })
476	
477	    if not dataset_info:
478	        log.error("No valid datasets found")
479	        sys.exit(1)
480	
481	    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM
482	    from transformers import AutoModelForCausalLM, AutoTokenizer
483	
484	    log.info(f"Loading model from {args.model_path} ...")
485	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
486	    if tokenizer.pad_token is None:
487	        tokenizer.pad_token = tokenizer.eos_token
488	        tokenizer.pad_token_id = tokenizer.eos_token_id
489	    tokenizer.padding_side = "right"
490	
491	    llm = AutoModelForCausalLM.from_pretrained(
492	        args.model_path,
493	        torch_dtype=torch.float16,
494	        device_map="auto",
495	        trust_remote_code=True,
496	    )
497	    llm.eval()
498	    log.info("Model loaded.")
499	
500	    if torch.cuda.is_available():
501	        torch.cuda.reset_peak_memory_stats(device)
502	
503	    for ds in dataset_info:
504	        log.info(f"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...")
505	        emb, actual_bs = extract_embeddings(
506	            llm, tokenizer, ds["texts"],
507	            batch_size=args.embed_batch_size,
508	            max_length=args.max_length,
509	        )
510	        ds["embeddings"] = emb
511	        ds["actual_embed_bs"] = actual_bs
512	        log.info(f"  shape={emb.shape}")
513	
514	    embed_peak = None
515	    if torch.cuda.is_available():
516	        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)
517	        log.info(f"Peak VRAM during embedding extraction: {embed_peak:.1f} MB")
518	
519	    # Free LLM before MLP training — this is the key memory optimization
520	    del llm, tokenizer
521	    gc.collect()
522	    torch.cuda.empty_cache()
523	    if torch.cuda.is_available():
524	        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)
525	        log.info(f"VRAM after freeing LLM: {post_free:.1f} MB")
526	
527	    # Phase 3: Train MLP probes (LLM no longer in memory)
528	    all_results = []
529	    for ds in dataset_info:
530	        r = run_one_dataset(
531	            ds["embeddings"], ds["depths"], ds["doc_ids"],
532	            ds["label"], ds["data_dir"], args, device,
533	        )
534	        if r:
535	            r["embed_batch_size_actual"] = ds["actual_embed_bs"]
536	            r["embed_peak_vram_mb"] = round(embed_peak, 1) if embed_peak else None
537	            all_results.append(r)
538	
539	    # Save
540	    out = Path(args.output)
541	    out.parent.mkdir(parents=True, exist_ok=True)
542	    with open(out, "w") as f:
543	        json.dump(all_results, f, indent=2, ensure_ascii=False)
544	    log.info(f"\nResults -> {out}")
545	
546	    # Final summary
547	    log.info("\n" + "=" * 60)
548	    log.info("SUMMARY")
549	    log.info("=" * 60)
550	    for r in all_results:
551	        np_ks = r["neural_probe"]["k_star"]
552	        base_ks = r.get("lgbm_baseline", {}).get("k_star", "-")
553	        log.info(f"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}")
554	
555	        for pair, ci in r["neural_probe"]["bootstrap_ci"].items():
556	            pt = r["neural_probe"]["permutation_test"].get(pair, {})
557	            pv = pt.get("p_value", "?")
558	            pval_s = f"<{1/args.permutation_resamples}" if pv == 0 else f"{pv}"
559	            log.info(f"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}")
560	
561	    k_stars = [r["neural_probe"]["k_star"] for r in all_results]
562	    if len(k_stars) > 1:
563	        if all(k == k_stars[0] for k in k_stars):
564	            log.info(f"\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic")
565	        else:
566	            log.info(f"\n  K* varies: {k_stars}")
567	
568	
569	if __name__ == "__main__":
570	    main()
571	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "efed40d7-fdf4-4c9e-92d7-545f5a1245dc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py",
      "content": "\"\"\"\nexp-015: Neural Probe for Generational Depth Classification\n\nValidates that K*=2 (found with 15D hand-crafted features + LightGBM) is\ndata-intrinsic, not a feature engineering artifact. Uses frozen Qwen2.5-1.5B\nembeddings (last hidden state, avg pool -> 1536-dim) + MLP classifier.\n\nv2 changes: memory-optimized (extract all embeddings then free LLM),\nbootstrap CI, permutation test, peak VRAM logging, OOM-safe batch adapt.\n\"\"\"\n\nimport argparse\nimport gc\nimport json\nimport logging\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nimport torch.nn as nn\nfrom torch.utils.data import DataLoader, TensorDataset\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# -- Data loading ------------------------------------------------------\n\ndef load_depth_data(data_dir: Path, max_depth: int, num_samples: int = None):\n    texts, depths, doc_ids = [], [], []\n    for d in range(max_depth + 1):\n        path = data_dir / f\"depth_{d}.jsonl\"\n        if not path.exists():\n            log.warning(f\"Missing {path}, skipping depth {d}\")\n            continue\n        count = 0\n        with open(path) as f:\n            for line in f:\n                if num_samples is not None and count >= num_samples:\n                    break\n                rec = json.loads(line)\n                texts.append(rec[\"text\"])\n                depths.append(d)\n                doc_ids.append(rec[\"doc_id\"])\n                count += 1\n        log.info(f\"  depth {d}: {count} samples\")\n    return texts, np.array(depths), np.array(doc_ids)\n\n\n# -- Embedding extraction with OOM retry ------------------------------\n\n@torch.no_grad()\ndef extract_embeddings(model, tokenizer, texts, batch_size=16, max_length=512):\n    \"\"\"Auto-halves batch_size on OOM until batch_size=1.\"\"\"\n    all_emb = []\n    actual_bs = batch_size\n    i = 0\n    pbar = tqdm(total=len(texts), desc=\"Embedding\")\n    while i < len(texts):\n        batch = texts[i : i + actual_bs]\n        try:\n            inputs = tokenizer(\n                batch,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=max_length,\n            ).to(model.device)\n            out = model(**inputs, output_hidden_states=True)\n            hidden = out.hidden_states[-1]\n            mask = inputs[\"attention_mask\"].unsqueeze(-1).float()\n            pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)\n            all_emb.append(pooled.cpu().float().numpy())\n            pbar.update(len(batch))\n            i += actual_bs\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if actual_bs <= 1:\n                pbar.close()\n                raise RuntimeError(f\"OOM even at batch_size=1 on sample {i}\")\n            old_bs = actual_bs\n            actual_bs = max(1, actual_bs // 2)\n            log.warning(f\"OOM at batch_size={old_bs}, retrying with {actual_bs}\")\n    pbar.close()\n    log.info(f\"Embedding done (effective batch_size={actual_bs})\")\n    return np.concatenate(all_emb, axis=0), actual_bs\n\n\n# -- MLP ---------------------------------------------------------------\n\nclass DepthMLP(nn.Module):\n    def __init__(self, input_dim=1536, num_classes=6):\n        super().__init__()\n        self.net = nn.Sequential(\n            nn.Linear(input_dim, 512),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(512, 256),\n            nn.ReLU(),\n            nn.Dropout(0.1),\n            nn.Linear(256, num_classes),\n        )\n\n    def forward(self, x):\n        return self.net(x)\n\n\ndef train_mlp(X_train, y_train, X_val, y_val, input_dim, num_classes,\n              epochs=20, lr=1e-3, batch_size=256, patience=5, device=\"cuda\"):\n    model = DepthMLP(input_dim=input_dim, num_classes=num_classes).to(device)\n    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)\n    criterion = nn.CrossEntropyLoss()\n\n    ds = TensorDataset(\n        torch.tensor(X_train, dtype=torch.float32),\n        torch.tensor(y_train, dtype=torch.long),\n    )\n    loader = DataLoader(ds, batch_size=batch_size, shuffle=True)\n    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)\n    y_val_t = torch.tensor(y_val, dtype=torch.long).to(device)\n\n    best_loss = float(\"inf\")\n    best_state = None\n    wait = 0\n\n    for epoch in range(epochs):\n        model.train()\n        for xb, yb in loader:\n            xb, yb = xb.to(device), yb.to(device)\n            optimizer.zero_grad()\n            criterion(model(xb), yb).backward()\n            optimizer.step()\n\n        model.eval()\n        with torch.no_grad():\n            val_loss = criterion(model(X_val_t), y_val_t).item()\n\n        if val_loss < best_loss:\n            best_loss = val_loss\n            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}\n            wait = 0\n        else:\n            wait += 1\n            if wait >= patience:\n                break\n\n    model.load_state_dict(best_state)\n    model.eval()\n    return model\n\n\n# -- Pairwise AUC ------------------------------------------------------\n\ndef compute_pairwise_auc(probas, depths, max_depth):\n    def _auc_pair(i, j):\n        mask = (depths == i) | (depths == j)\n        y = (depths[mask] == j).astype(int)\n        if len(np.unique(y)) < 2 or mask.sum() < 4:\n            return float(\"nan\")\n        p_i = probas[mask, i]\n        p_j = probas[mask, j]\n        score = p_j / (p_i + p_j + 1e-12)\n        return round(float(roc_auc_score(y, score)), 4)\n\n    adjacent = {}\n    for k in range(1, max_depth + 1):\n        adjacent[f\"{k-1}v{k}\"] = _auc_pair(k - 1, k)\n\n    all_pairs = {}\n    for i in range(max_depth + 1):\n        for j in range(i + 1, max_depth + 1):\n            all_pairs[f\"{i}v{j}\"] = _auc_pair(i, j)\n\n    return adjacent, all_pairs\n\n\n# -- Bootstrap CI (doc-level resampling) --------------------------------\n\ndef bootstrap_auc_ci(depths, probas, pair_i, pair_j, doc_ids,\n                     n_resamples=1000, seed=42):\n    \"\"\"Percentile bootstrap 95% CI, resampling at doc level to respect grouping.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n    docs_masked = doc_ids[mask]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": float(\"nan\"), \"ci_lower\": float(\"nan\"),\n                \"ci_upper\": float(\"nan\"), \"boot_std\": float(\"nan\")}\n\n    obs_auc = float(roc_auc_score(y, scores))\n\n    rng = np.random.default_rng(seed)\n    unique_docs = np.unique(docs_masked)\n    doc_idx_map = {d: np.where(docs_masked == d)[0] for d in unique_docs}\n\n    boot_aucs = []\n    for _ in range(n_resamples):\n        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)\n        idx = np.concatenate([doc_idx_map[d] for d in sampled])\n        yb, sb = y[idx], scores[idx]\n        if len(np.unique(yb)) < 2:\n            continue\n        boot_aucs.append(roc_auc_score(yb, sb))\n\n    boot_aucs = np.array(boot_aucs)\n    ci_lo, ci_hi = np.percentile(boot_aucs, [2.5, 97.5])\n\n    return {\n        \"auc\": round(obs_auc, 4),\n        \"ci_lower\": round(float(ci_lo), 4),\n        \"ci_upper\": round(float(ci_hi), 4),\n        \"boot_std\": round(float(np.std(boot_aucs)), 4),\n        \"n_valid_resamples\": len(boot_aucs),\n    }\n\n\n# -- Permutation test ---------------------------------------------------\n\ndef permutation_test_auc(depths, probas, pair_i, pair_j,\n                         n_permutations=500, seed=43):\n    \"\"\"Shuffle binary labels, report fraction of permuted AUC >= observed.\"\"\"\n    mask = (depths == pair_i) | (depths == pair_j)\n    y = (depths[mask] == pair_j).astype(int)\n    p_i = probas[mask, pair_i]\n    p_j = probas[mask, pair_j]\n    scores = p_j / (p_i + p_j + 1e-12)\n\n    if len(np.unique(y)) < 2:\n        return {\"p_value\": float(\"nan\"), \"obs_auc\": float(\"nan\")}\n\n    obs_auc = roc_auc_score(y, scores)\n    rng = np.random.default_rng(seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        yp = rng.permutation(y)\n        if len(np.unique(yp)) < 2:\n            continue\n        count_ge += (roc_auc_score(yp, scores) >= obs_auc)\n\n    return {\n        \"obs_auc\": round(float(obs_auc), 4),\n        \"p_value\": round(count_ge / n_permutations, 4),\n        \"n_permutations\": n_permutations,\n    }\n\n\n# -- Single dataset experiment ------------------------------------------\n\ndef run_one_dataset(embeddings, depths, doc_ids, label, data_dir, args, device):\n    \"\"\"MLP 5-fold CV + pairwise AUC + bootstrap CI + permutation test.\"\"\"\n    log.info(f\"\\n{'='*60}\")\n    log.info(f\"Dataset: {label} ({data_dir})\")\n    log.info(f\"{'='*60}\")\n\n    num_classes = int(depths.max()) + 1\n    input_dim = embeddings.shape[1]\n    log.info(f\"Embeddings: {embeddings.shape}, classes: {num_classes}\")\n\n    gkf = GroupKFold(n_splits=5)\n    all_probas = np.zeros((len(depths), num_classes))\n    fold_adj_aucs = {f\"{k-1}v{k}\": [] for k in range(1, num_classes)}\n    peak_vram_mb = []\n\n    for fold, (tr_idx, te_idx) in enumerate(\n        gkf.split(embeddings, depths, groups=doc_ids)\n    ):\n        log.info(f\"  Fold {fold+1}/5  train={len(tr_idx)} test={len(te_idx)}\")\n\n        if torch.cuda.is_available():\n            torch.cuda.reset_peak_memory_stats(device)\n\n        mlp = train_mlp(\n            embeddings[tr_idx], depths[tr_idx],\n            embeddings[te_idx], depths[te_idx],\n            input_dim=input_dim, num_classes=num_classes,\n            epochs=args.epochs, lr=args.lr,\n            batch_size=args.mlp_batch_size,\n            patience=args.patience, device=device,\n        )\n\n        with torch.no_grad():\n            logits = mlp(torch.tensor(embeddings[te_idx], dtype=torch.float32).to(device))\n            probas = torch.softmax(logits, dim=-1).cpu().numpy()\n\n        all_probas[te_idx] = probas\n\n        td = depths[te_idx]\n        for k in range(1, num_classes):\n            m = (td == k - 1) | (td == k)\n            y = (td[m] == k).astype(int)\n            if len(np.unique(y)) < 2 or m.sum() < 4:\n                continue\n            p0 = probas[m, k - 1]\n            p1 = probas[m, k]\n            s = p1 / (p0 + p1 + 1e-12)\n            fold_adj_aucs[f\"{k-1}v{k}\"].append(round(float(roc_auc_score(y, s)), 4))\n\n        if torch.cuda.is_available():\n            peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n            peak_vram_mb.append(round(peak, 1))\n            log.info(f\"    Peak VRAM: {peak:.1f} MB\")\n\n        del mlp\n        torch.cuda.empty_cache()\n\n    # Overall pairwise AUC\n    adj_auc, all_auc = compute_pairwise_auc(all_probas, depths, args.max_depth)\n\n    # K*\n    k_star = 0\n    for k in range(1, num_classes):\n        if adj_auc.get(f\"{k-1}v{k}\", 0) > 0.60:\n            k_star = k\n\n    accuracy = float((all_probas.argmax(axis=1) == depths).mean())\n\n    # Per-fold stats\n    fold_stats = {}\n    for key, aucs in fold_adj_aucs.items():\n        if aucs:\n            fold_stats[key] = {\n                \"mean\": round(float(np.mean(aucs)), 4),\n                \"std\": round(float(np.std(aucs)), 4),\n                \"folds\": aucs,\n            }\n\n    # Bootstrap CI\n    log.info(\"  Computing bootstrap CI ...\")\n    bootstrap_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        ci = bootstrap_auc_ci(\n            depths, all_probas, k - 1, k, doc_ids,\n            n_resamples=args.bootstrap_resamples,\n        )\n        bootstrap_results[pair] = ci\n        log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']}, {ci['ci_upper']}]\")\n\n    # Permutation test\n    log.info(\"  Computing permutation tests ...\")\n    permutation_results = {}\n    for k in range(1, num_classes):\n        pair = f\"{k-1}v{k}\"\n        pt = permutation_test_auc(\n            depths, all_probas, k - 1, k,\n            n_permutations=args.permutation_resamples,\n        )\n        permutation_results[pair] = pt\n        pval_s = f\"<{1/args.permutation_resamples}\" if pt[\"p_value\"] == 0 else f\"{pt['p_value']:.4f}\"\n        log.info(f\"    {pair}: p={pval_s}\")\n\n    # Load baseline\n    baseline = None\n    data_name = Path(data_dir).name\n    results_name = data_name.replace(\"data_\", \"results_\")\n    baseline_path = Path(data_dir).parent / results_name / \"pairwise_auc.json\"\n    if baseline_path.exists():\n        with open(baseline_path) as f:\n            baseline = json.load(f)\n        log.info(f\"  Loaded baseline from {baseline_path}\")\n\n    result = {\n        \"dataset\": label,\n        \"data_dir\": str(data_dir),\n        \"num_samples_per_depth\": args.num_samples if args.num_samples else \"all\",\n        \"max_depth\": args.max_depth,\n        \"embedding_dim\": input_dim,\n        \"mlp_arch\": f\"{input_dim}->512->256->{num_classes}\",\n        \"neural_probe\": {\n            \"pairwise_auc_adjacent\": adj_auc,\n            \"pairwise_auc_all\": all_auc,\n            \"fold_stats\": fold_stats,\n            \"k_star\": k_star,\n            \"k_star_threshold\": 0.60,\n            \"classification_accuracy\": round(accuracy, 4),\n            \"bootstrap_ci\": bootstrap_results,\n            \"permutation_test\": permutation_results,\n        },\n        \"peak_vram_mb\": peak_vram_mb,\n        \"peak_vram_max_mb\": max(peak_vram_mb) if peak_vram_mb else None,\n    }\n    if baseline:\n        result[\"lgbm_baseline\"] = {\n            \"pairwise_auc_adjacent\": baseline[\"mean\"],\n            \"k_star\": max(\n                (k for k in range(1, 6) if baseline[\"mean\"].get(f\"{k-1}v{k}\", 0) > 0.60),\n                default=0,\n            ),\n        }\n\n    # Log summary\n    log.info(f\"\\n  K* (neural probe) = {k_star}\")\n    log.info(f\"  Accuracy = {accuracy:.4f}\")\n    if peak_vram_mb:\n        log.info(f\"  Peak VRAM (max across folds) = {max(peak_vram_mb):.1f} MB\")\n    for k in range(1, num_classes):\n        key = f\"{k-1}v{k}\"\n        a = adj_auc.get(key, \"N/A\")\n        ci = bootstrap_results.get(key, {})\n        ci_lo = ci.get(\"ci_lower\", \"?\")\n        ci_hi = ci.get(\"ci_upper\", \"?\")\n        pt = permutation_results.get(key, {})\n        pv = pt.get(\"p_value\", \"?\")\n        base = baseline[\"mean\"].get(key, \"-\") if baseline else \"-\"\n        log.info(f\"  AUC({key}): neural={a}  95%CI=[{ci_lo},{ci_hi}]  p={pv}  lgbm={base}\")\n\n    return result\n\n\n# -- Main ---------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"exp-015: Neural Probe for depth classification (frozen LLM + MLP)\",\n    )\n    parser.add_argument(\n        \"--model_path\", type=str,\n        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct\",\n    )\n    parser.add_argument(\"--data_dir\", type=str, nargs=\"+\",\n                        default=[\"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\"])\n    parser.add_argument(\"--label\", type=str, nargs=\"+\", default=[\"Qwen-cont\"])\n    parser.add_argument(\n        \"--output\", type=str,\n        default=\"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\",\n    )\n    parser.add_argument(\"--num_samples\", type=int, default=None,\n                        help=\"Max samples per depth (default: all)\")\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--embed_batch_size\", type=int, default=16)\n    parser.add_argument(\"--max_length\", type=int, default=512)\n    parser.add_argument(\"--mlp_batch_size\", type=int, default=256)\n    parser.add_argument(\"--epochs\", type=int, default=20)\n    parser.add_argument(\"--lr\", type=float, default=1e-3)\n    parser.add_argument(\"--patience\", type=int, default=5)\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--bootstrap_resamples\", type=int, default=1000)\n    parser.add_argument(\"--permutation_resamples\", type=int, default=500)\n    args = parser.parse_args()\n\n    if len(args.data_dir) != len(args.label):\n        log.error(\"--data_dir and --label must have the same number of entries\")\n        sys.exit(1)\n\n    device = args.device if torch.cuda.is_available() else \"cpu\"\n    log.info(f\"Device: {device}\")\n    if torch.cuda.is_available():\n        props = torch.cuda.get_device_properties(0)\n        log.info(f\"GPU: {torch.cuda.get_device_name(0)} ({props.total_memory // 1024**3}GB)\")\n\n    # Phase 1: Load all text data (cheap, CPU only)\n    dataset_info = []\n    for dd, lab in zip(args.data_dir, args.label):\n        texts, depths, doc_ids = load_depth_data(\n            Path(dd), args.max_depth, args.num_samples,\n        )\n        if len(texts) == 0:\n            log.error(f\"No data in {dd}\")\n            continue\n        dataset_info.append({\n            \"data_dir\": dd, \"label\": lab,\n            \"texts\": texts, \"depths\": depths, \"doc_ids\": doc_ids,\n        })\n\n    if not dataset_info:\n        log.error(\"No valid datasets found\")\n        sys.exit(1)\n\n    # Phase 2: Load LLM, extract embeddings for ALL datasets, then free LLM\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(f\"Loading model from {args.model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n    tokenizer.padding_side = \"right\"\n\n    llm = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    llm.eval()\n    log.info(\"Model loaded.\")\n\n    if torch.cuda.is_available():\n        torch.cuda.reset_peak_memory_stats(device)\n\n    for ds in dataset_info:\n        log.info(f\"Extracting embeddings for {ds['label']} ({len(ds['texts'])} samples) ...\")\n        emb, actual_bs = extract_embeddings(\n            llm, tokenizer, ds[\"texts\"],\n            batch_size=args.embed_batch_size,\n            max_length=args.max_length,\n        )\n        ds[\"embeddings\"] = emb\n        ds[\"actual_embed_bs\"] = actual_bs\n        log.info(f\"  shape={emb.shape}\")\n\n    embed_peak = None\n    if torch.cuda.is_available():\n        embed_peak = torch.cuda.max_memory_allocated(device) / (1024 ** 2)\n        log.info(f\"Peak VRAM during embedding extraction: {embed_peak:.1f} MB\")\n\n    # Free LLM before MLP training — this is the key memory optimization\n    del llm, tokenizer\n    gc.collect()\n    torch.cuda.empty_cache()\n    if torch.cuda.is_available():\n        post_free = torch.cuda.memory_allocated(device) / (1024 ** 2)\n        log.info(f\"VRAM after freeing LLM: {post_free:.1f} MB\")\n\n    # Phase 3: Train MLP probes (LLM no longer in memory)\n    all_results = []\n    for ds in dataset_info:\n        r = run_one_dataset(\n            ds[\"embeddings\"], ds[\"depths\"], ds[\"doc_ids\"],\n            ds[\"label\"], ds[\"data_dir\"], args, device,\n        )\n        if r:\n            r[\"embed_batch_size_actual\"] = ds[\"actual_embed_bs\"]\n            r[\"embed_peak_vram_mb\"] = round(embed_peak, 1) if embed_peak else None\n            all_results.append(r)\n\n    # Save\n    out = Path(args.output)\n    out.parent.mkdir(parents=True, exist_ok=True)\n    with open(out, \"w\") as f:\n        json.dump(all_results, f, indent=2, ensure_ascii=False)\n    log.info(f\"\\nResults -> {out}\")\n\n    # Final summary\n    log.info(\"\\n\" + \"=\" * 60)\n    log.info(\"SUMMARY\")\n    log.info(\"=\" * 60)\n    for r in all_results:\n        np_ks = r[\"neural_probe\"][\"k_star\"]\n        base_ks = r.get(\"lgbm_baseline\", {}).get(\"k_star\", \"-\")\n        log.info(f\"  {r['dataset']:12s}  K*(neural)={np_ks}  K*(lgbm)={base_ks}  acc={r['neural_probe']['classification_accuracy']}\")\n\n        for pair, ci in r[\"neural_probe\"][\"bootstrap_ci\"].items():\n            pt = r[\"neural_probe\"][\"permutation_test\"].get(pair, {})\n            pv = pt.get(\"p_value\", \"?\")\n            pval_s = f\"<{1/args.permutation_resamples}\" if pv == 0 else f\"{pv}\"\n            log.info(f\"    {pair}: AUC={ci['auc']}  95%CI=[{ci['ci_lower']},{ci['ci_upper']}]  p={pval_s}\")\n\n    k_stars = [r[\"neural_probe\"][\"k_star\"] for r in all_results]\n    if len(k_stars) > 1:\n        if all(k == k_stars[0] for k in k_stars):\n            log.info(f\"\\n  Consistent K* = {k_stars[0]} across all datasets -> boundary is data-intrinsic\")\n        else:\n            log.info(f\"\\n  K* varies: {k_stars}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 571,
      "startLine": 1,
      "totalLines": 571
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

脚本已写好。现在上传到服务器并 dry-run `--help`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "fea1b9e1-cae3-470f-9cea-d65f270a47e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WRAbJjCMrMaWzUJT3g2oL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8399,
      "cache_read_input_tokens": 59449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8399
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01LNgJnuSdo1n3Adp6JjLpPS`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "a14de4b8-2998-4600-a9f2-2f6672b1249b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WRAbJjCMrMaWzUJT3g2oL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8399,
      "cache_read_input_tokens": 59449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8399
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T03:07:28.989Z_

<details><summary>↩ Tool result · `toolu_01LNgJnuSdo1n3Adp6JjLpPS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "bbd2c805-e30c-4ab5-b458-030045ecff4e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0137Muc3Ap3UQEiZYvFfz8uP`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "1840cf5e-cb20-4064-8ca3-d9d235171d77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSW35tpTCaaWqfUDHXDBzt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7407,
      "cache_read_input_tokens": 67848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7407
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T03:07:37.136Z_

<details><summary>↩ Tool result · `toolu_0137Muc3Ap3UQEiZYvFfz8uP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: run_exp015_neural_probe.py [-h] [--model_path MODEL_PATH]\\n                                  [--data_dir DATA_DIR [DATA_DIR ...]]\\n                                  [--label LABEL [LABEL ...]]\\n                                  [--output OUTPUT]\\n                                  [--num_samples NUM_SAMPLES]\\n                                  [--max_depth MAX_DEPTH]\\n                                  [--embed_batch_size EMBED_BATCH_SIZE]\\n                                  [--max_length MAX_LENGTH]\\n                                  [--mlp_batch_size MLP_BATCH_SIZE]\\n                                  [--epochs EPOCHS] [--lr LR]\\n                                  [--patience PATIENCE] [--device DEVICE]\\n                                  [--bootstrap_resamples BOOTSTRAP_RESAMPLES]\\n                                  [--permutation_resamples PERMUTATION_RESAMPLES]\\n\\nexp-015: Neural Probe for depth classification (frozen LLM + MLP)\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_path MODEL_PATH\\n  --data_dir DATA_DIR [DATA_DIR ...]\\n  --label LABEL [LABEL ...]\\n  --output OUTPUT\\n  --num_samples NUM_SAMPLES\\n                        Max samples per depth (default: all)\\n  --max_depth MAX_DEPTH\\n  --embed_batch_size EMBED_BATCH_SIZE\\n  --max_length MAX_LENGTH\\n  --mlp_batch_size MLP_BATCH_SIZE\\n  --epochs EPOCHS\\n  --lr LR\\n  --patience PATIENCE\\n  --device DEVICE\\n  --bootstrap_resamples BOOTSTRAP_RESAMPLES\\n  --permutation_resamples PERMUTATION_RESAMPLES\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.81}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "51c39973-767d-45fa-a1e0-b23846419163",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"usage: run_exp015_neural_probe.py [-h] [--model_path MODEL_PATH]\\\\n                                  [--data_dir DATA_DIR [DATA_DIR ...]]\\\\n                                  [--label LABEL [LABEL ...]]\\\\n                                  [--output OUTPUT]\\\\n                                  [--num_samples NUM_SAMPLES]\\\\n                                  [--max_depth MAX_DEPTH]\\\\n                                  [--embed_batch_size EMBED_BATCH_SIZE]\\\\n                                  [--max_length MAX_LENGTH]\\\\n                                  [--mlp_batch_size MLP_BATCH_SIZE]\\\\n                                  [--epochs EPOCHS] [--lr LR]\\\\n                                  [--patience PATIENCE] [--device DEVICE]\\\\n                                  [--bootstrap_resamples BOOTSTRAP_RESAMPLES]\\\\n                                  [--permutation_resamples PERMUTATION_RESAMPLES]\\\\n\\\\nexp-015: Neural Probe for depth classification (frozen LLM + MLP)\\\\n\\\\noptions:\\\\n  -h, --help            show this help message and exit\\\\n  --model_path MODEL_PATH\\\\n  --data_dir DATA_DIR [DATA_DIR ...]\\\\n  --label LABEL [LABEL ...]\\\\n  --output OUTPUT\\\\n  --num_samples NUM_SAMPLES\\\\n                        Max samples per depth (default: all)\\\\n  --max_depth MAX_DEPTH\\\\n  --embed_batch_size EMBED_BATCH_SIZE\\\\n  --max_length MAX_LENGTH\\\\n  --mlp_batch_size MLP_BATCH_SIZE\\\\n  --epochs EPOCHS\\\\n  --lr LR\\\\n  --patience PATIENCE\\\\n  --device DEVICE\\\\n  --bootstrap_resamples BOOTSTRAP_RESAMPLES\\\\n  --permutation_resamples PERMUTATION_RESAMPLES\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.81}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"usage: run_exp015_neural_probe.py [-h] [--model_path MODEL_PATH]\\n                                  [--data_dir DATA_DIR [DATA_DIR ...]]\\n                                  [--label LABEL [LABEL ...]]\\n                                  [--output OUTPUT]\\n                                  [--num_samples NUM_SAMPLES]\\n                                  [--max_depth MAX_DEPTH]\\n                                  [--embed_batch_size EMBED_BATCH_SIZE]\\n                                  [--max_length MAX_LENGTH]\\n                                  [--mlp_batch_size MLP_BATCH_SIZE]\\n                                  [--epochs EPOCHS] [--lr LR]\\n                                  [--patience PATIENCE] [--device DEVICE]\\n                                  [--bootstrap_resamples BOOTSTRAP_RESAMPLES]\\n                                  [--permutation_resamples PERMUTATION_RESAMPLES]\\n\\nexp-015: Neural Probe for depth classification (frozen LLM + MLP)\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_path MODEL_PATH\\n  --data_dir DATA_DIR [DATA_DIR ...]\\n  --label LABEL [LABEL ...]\\n  --output OUTPUT\\n  --num_samples NUM_SAMPLES\\n                        Max samples per depth (default: all)\\n  --max_depth MAX_DEPTH\\n  --embed_batch_size EMBED_BATCH_SIZE\\n  --max_length MAX_LENGTH\\n  --mlp_batch_size MLP_BATCH_SIZE\\n  --epochs EPOCHS\\n  --lr LR\\n  --patience PATIENCE\\n  --device DEVICE\\n  --bootstrap_resamples BOOTSTRAP_RESAMPLES\\n  --permutation_resamples PERMUTATION_RESAMPLES\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.81}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

验证文件行数一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "c6eac615-03d5-4b01-8ff4-2a305713b078",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTCDee6BmvzsYrmjjVJqZk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 75255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 684
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Qgu7vWGM22J3bznFTpKrg7`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "73b05bce-ece2-4757-9422-88204e96f211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QTCDee6BmvzsYrmjjVJqZk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 75255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 684
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T03:07:41.172Z_

<details><summary>↩ Tool result · `toolu_01Qgu7vWGM22J3bznFTpKrg7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"570 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "1767b394-b87c-4234-8107-6741a5f37c4f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"570 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"570 /root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "uuid": "497cead3-9f4b-4660-b3b9-39a4c6dda5b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsGvRhKK1RwJBWggT8esj9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 75939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 50_

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
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 336080,
  "duration_api_ms": 326228,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "4db9d11c-d983-4bff-a852-4bbe49c09274",
  "total_cost_usd": 1.393246,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 64344,
    "cache_read_input_tokens": 745156,
    "output_tokens": 24664,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 64344,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 690,
        "cache_read_input_tokens": 75939,
        "cache_creation_input_tokens": 246,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 246
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1713,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001813,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 24664,
      "cacheReadInputTokens": 745156,
      "cacheCreationInputTokens": 64344,
      "webSearchRequests": 0,
      "costUSD": 1.391433,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "21dcc1c0-6aed-43b8-8983-b2cad9d10be5"
}
```

</details>

---
