# code router sft class weight

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_code_router-sft-class-weight_20260513T200820.jsonl`
- **Structured JSON:** [`5ee9c330bf7e9ad6bcc7.json`](../../sessions/5e/5ee9c330bf7e9ad6bcc7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-13T20:23:17.360425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T20:23:17.360735+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T20:23:17.360918+00:00_

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
  "session": "worker_code_router-sft-class-weight_20260513T200820",
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

_source line 4 · 2026-05-13T20:23:17.361120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T20:23:17.361255+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "cat /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T20:23:17.361525+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Router SFT training script for SimGate modular routing.\\n# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data\\n# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.\\n#\\n# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl\\n# Usage: python src/router_sft_train.py --help\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nimport random\\nfrom collections import Counter\\nfrom typing import List, Dict, Any, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom torch.utils.data import Dataset\\nfrom sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix\\nfrom transformers import (\\n    AutoTokenizer,\\n    AutoModelForSequenceClassification,\\n    TrainingArguments,\\n    Trainer,\\n    EarlyStoppingCallback,\\n)\\nfrom peft import LoraConfig, get_peft_model, TaskType\\n\\nLABEL2ID = {\\\"internal\\\": 0, \\\"deterministic\\\": 1}\\nID2LABEL = {0: \\\"internal\\\", 1: \\\"deterministic\\\"}\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are a routing classifier. Given the current observation and action history, \\\"\\n    \\\"predict which reasoning modality will lead to a better outcome.\\\"\\n)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Router SFT: finetune LLM for 2-way routing classification\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, default=\\\"results/plan_c/\\\",\\n                    help=\\\"Directory containing {task_type}/labeled_steps.jsonl\\\")\\n    p.add_argument(\\\"--model_name\\\", type=str, default=\\\"Qwen/Qwen3-1.7B\\\",\\n                    help=\\\"HuggingFace model name or local path\\\")\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"results/router_sft/\\\",\\n                    help=\\\"Output directory for checkpoints and reports\\\")\\n    p.add_argument(\\\"--epochs\\\", type=int, default=3)\\n    p.add_argume
…[truncated 7234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T20:23:17.361714+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "wc -l /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "wc -l /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T20:23:17.361851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "head -n 200 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "head -n 200 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T20:23:17.361980+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"351 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T20:23:17.362257+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Router SFT training script for SimGate modular routing.\\n# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data\\n# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.\\n#\\n# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl\\n# Usage: python src/router_sft_train.py --help\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nimport random\\nfrom collections import Counter\\nfrom typing import List, Dict, Any, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom torch.utils.data import Dataset\\nfrom sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix\\nfrom transformers import (\\n    AutoTokenizer,\\n    AutoModelForSequenceClassification,\\n    TrainingArguments,\\n    Trainer,\\n    EarlyStoppingCallback,\\n)\\nfrom peft import LoraConfig, get_peft_model, TaskType\\n\\nLABEL2ID = {\\\"internal\\\": 0, \\\"deterministic\\\": 1}\\nID2LABEL = {0: \\\"internal\\\", 1: \\\"deterministic\\\"}\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are a routing classifier. Given the current observation and action history, \\\"\\n    \\\"predict which reasoning modality will lead to a better outcome.\\\"\\n)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Router SFT: finetune LLM for 2-way routing classification\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, default=\\\"results/plan_c/\\\",\\n                    help=\\\"Directory containing {task_type}/labeled_steps.jsonl\\\")\\n    p.add_argument(\\\"--model_name\\\", type=str, default=\\\"Qwen/Qwen3-1.7B\\\",\\n                    help=\\\"HuggingFace model name or local path\\\")\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"results/router_sft/\\\",\\n                    help=\\\"Output directory for checkpoints and reports\\\")\\n    p.add_argument(\\\"--epochs\\\", type=int, default=3)\\n    p.add_argume
…[truncated 6549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T20:23:17.362412+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "tail -n +200 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "tail -n +200 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T20:23:17.362613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    )\\n    model = get_peft_model(model, lora_config)\\n    model.print_trainable_parameters()\\n    return model, tokenizer\\n\\n\\n# ---------------------------------------------------------------------------\\n# Metrics\\n# ---------------------------------------------------------------------------\\n\\ndef compute_metrics(eval_pred):\\n    logits, labels = eval_pred\\n    preds = np.argmax(logits, axis=-1)\\n    acc = accuracy_score(labels, preds)\\n    prec, rec, f1, _ = precision_recall_fscore_support(labels, preds, average=None, labels=[0, 1])\\n    return {\\n        \\\"accuracy\\\": acc,\\n        \\\"precision_internal\\\": prec[0],\\n        \\\"recall_internal\\\": rec[0],\\n        \\\"f1_internal\\\": f1[0],\\n        \\\"precision_deterministic\\\": prec[1],\\n        \\\"recall_deterministic\\\": rec[1],\\n        \\\"f1_deterministic\\\": f1[1],\\n    }\\n\\n\\ndef per_task_evaluation(trainer, val_dataset, val_samples) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Compute per-task accuracy and confusion matrix.\\\"\\\"\\\"\\n    predictions = trainer.predict(val_dataset)\\n    preds = np.argmax(predictions.predictions, axis=-1)\\n    labels = predictions.label_ids\\n\\n    cm = confusion_matrix(labels, preds, labels=[0, 1]).tolist()\\n\\n    task_metrics = {}\\n    by_task: Dict[str, Dict[str, list]] = {}\\n    for i, s in enumerate(val_samples):\\n        t = s[\\\"task_type\\\"]\\n        if t not in by_task:\\n            by_task[t] = {\\\"preds\\\": [], \\\"labels\\\": []}\\n        by_task[t][\\\"preds\\\"].append(preds[i])\\n        by_task[t][\\\"labels\\\"].append(labels[i])\\n\\n    for task, data in sorted(by_task.items()):\\n        acc = accuracy_score(data[\\\"labels\\\"], data[\\\"preds\\\"])\\n        n = len(data[\\\"labels\\\"])\\n        task_metrics[task] = {\\\"accuracy\\\": acc, \\\"n_samples\\\": n}\\n\\n    return {\\n        \\\"overall_accuracy\\\": accuracy_score(labels, pred
…[truncated 4110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T20:23:17.363051+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py",
  "content": "# Router SFT training script for SimGate modular routing.\n# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data\n# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.\n#\n# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl\n# Usage: python src/router_sft_train.py --help\n\nimport argparse\nimport json\nimport os\nimport glob\nimport random\nimport warnings\nfrom collections import Counter\nfrom typing import List, Dict, Any, Optional, Tuple\n\nimport numpy as np\nimport torch\nfrom torch.utils.data import Dataset, DataLoader, WeightedRandomSampler\nfrom sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix\nfrom transformers import (\n    AutoTokenizer,\n    AutoModelForSequenceClassification,\n    TrainingArguments,\n    Trainer,\n    EarlyStoppingCallback,\n)\nfrom peft import LoraConfig, get_peft_model, TaskType\n\nLABEL2ID = {\"internal\": 0, \"deterministic\": 1}\nID2LABEL = {0: \"internal\", 1: \"deterministic\"}\n\nSYSTEM_PROMPT = (\n    \"You are a routing classifier. Given the current observation and action history, \"\n    \"predict which reasoning modality will lead to a better outcome.\"\n)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Router SFT: finetune LLM for 2-way routing classification\")\n    p.add_argument(\"--data_dir\", type=str, default=\"results/plan_c/\",\n                    help=\"Directory containing {task_type}/labeled_steps.jsonl\")\n    p.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-1.7B\",\n                    help=\"HuggingFace model name or local path\")\n    p.add_argument(\"--output_dir\", type=str, default=\"results/router_sft/\",\n                    help=\"Output directory for checkpoints and reports\")\n    p.add_argument(\"--epochs\", type=int, default=3)\n    p.add_argument(\"--batch_size\", type=int, default=16)\n    p.add_argument(\"--eval_batch_size\", type=int, default=32)\n    p.add_argument(\"--lr\", type=float, default=2e-4)\n    p.add_argument(\"--lora_r\", type=int, default=16)\n    p.add_argument(\"--lora_alpha\", type=int, default=32)\n    p.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    p.add_argument(\"--max_seq_len\", type=int, default=512)\n    p.add_argument(\"--gpu_id\", type=int, default=0)\n    p.add_argument(\"--wandb_project\", type=str, default=\"simgate-router-sft\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--eval_split\", type=float, default=0.2)\n    p.add_argument(\"--warmup_ratio\", type=float, default=0.1)\n    p.add_argument(\"--weight_decay\", type=float, default=0.01)\n    p.add_argument(\"--early_stopping_patience\", type=int, default=2)\n    p.add_argument(\"--dry_run\", action=\"store_true\", help=\"Only validate imports and args, skip training\")\n    p.add_argument(\"--class_weights\", type=str, default=None,\n                    help='\"auto\" for inverse-frequency weights, or \"w0,w1\" (internal:w0, det:w1)')\n    p.add_argument(\"--min_internal_samples\", type=int, default=10,\n                    help=\"Warn if internal samples < this threshold (default: 10)\")\n    p.add_argument(\"--upsample_minority\", action=\"store_true\",\n                    help=\"Use WeightedRandomSampler to oversample minority class\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:\n    \"\"\"Keep the most recent N actions as a summary.\"\"\"\n    recent = action_history[-max_actions:] if action_history else []\n    if not recent:\n        return \"(none)\"\n    return \" → \".join(recent)\n\n\ndef build_prompt(observation: str, action_history: List[str]) -> str:\n    history_summary = summarize_action_history(action_history)\n    return (\n        f\"<|system|>{SYSTEM_PROMPT}<|end|>\\n\"\n        f\"<|user|>\\n\"\n        f\"Observation: {observation}\\n\"\n        f\"Action history: {history_summary}\\n\"\n        f\"<|end|>\"\n    )\n\n\ndef load_labeled_data(data_dir: str) -> List[Dict[str, Any]]:\n    \"\"\"Load all labeled_steps.jsonl files, filtering out ties.\"\"\"\n    pattern = os.path.join(data_dir, \"*\", \"labeled_steps.jsonl\")\n    files = sorted(glob.glob(pattern))\n    if not files:\n        pattern_flat = os.path.join(data_dir, \"labeled_steps.jsonl\")\n        if os.path.exists(pattern_flat):\n            files = [pattern_flat]\n    if not files:\n        raise FileNotFoundError(f\"No labeled_steps.jsonl found in {data_dir}\")\n\n    samples = []\n    for fpath in files:\n        task_type = os.path.basename(os.path.dirname(fpath))\n        with open(fpath) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                record = json.loads(line)\n                label = record.get(\"label\", \"\")\n                if label not in LABEL2ID:\n                    continue\n                samples.append({\n                    \"observation\": record.get(\"observation\", \"\"),\n                    \"action_history\": record.get(\"action_history\", []),\n                    \"label\": label,\n                    \"label_id\": LABEL2ID[label],\n                    \"task_type\": record.get(\"task_name\", task_type),\n                })\n\n    print(f\"Loaded {len(samples)} samples from {len(files)} files (ties excluded)\")\n    label_dist = Counter(s[\"label\"] for s in samples)\n    for k, v in sorted(label_dist.items()):\n        print(f\"  {k}: {v} ({v/len(samples)*100:.1f}%)\")\n    return samples\n\n\ndef stratified_split(\n    samples: List[Dict], eval_ratio: float, seed: int\n) -> Tuple[List[Dict], List[Dict]]:\n    \"\"\"Stratified train/val split by task_type.\"\"\"\n    rng = random.Random(seed)\n    by_task: Dict[str, List[Dict]] = {}\n    for s in samples:\n        by_task.setdefault(s[\"task_type\"], []).append(s)\n\n    train_set, val_set = [], []\n    for task, items in by_task.items():\n        rng.shuffle(items)\n        n_val = max(1, int(len(items) * eval_ratio))\n        val_set.extend(items[:n_val])\n        train_set.extend(items[n_val:])\n\n    rng.shuffle(train_set)\n    rng.shuffle(val_set)\n    print(f\"Split: train={len(train_set)}, val={len(val_set)}\")\n    return train_set, val_set\n\n\nclass RouterDataset(Dataset):\n    def __init__(self, samples: List[Dict], tokenizer, max_length: int):\n        self.samples = samples\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n\n    def __len__(self):\n        return len(self.samples)\n\n    def __getitem__(self, idx):\n        s = self.samples[idx]\n        prompt = build_prompt(s[\"observation\"], s[\"action_history\"])\n        encoding = self.tokenizer(\n            prompt,\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        return {\n            \"input_ids\": encoding[\"input_ids\"].squeeze(0),\n            \"attention_mask\": encoding[\"attention_mask\"].squeeze(0),\n            \"labels\": torch.tensor(s[\"label_id\"], dtype=torch.long),\n        }\n\n\n# ---------------------------------------------------------------------------\n# Class weighting\n# ---------------------------------------------------------------------------\n\ndef compute_class_weights(train_samples: List[Dict], mode: str = \"auto\") -> torch.Tensor:\n    # \"auto\": weight_c = N_total / (num_classes * N_c), i.e. inverse frequency —\n    #         rarer class gets proportionally higher weight.\n    # \"w0,w1\": manual weights, e.g. \"1.0,5.0\" -> internal=1.0, deterministic=5.0\n    num_classes = len(LABEL2ID)\n    if mode == \"auto\":\n        counts = Counter(s[\"label_id\"] for s in train_samples)\n        total = len(train_samples)\n        weights = torch.tensor(\n            [total / (num_classes * max(counts.get(i, 1), 1)) for i in range(num_classes)],\n            dtype=torch.float32,\n        )\n    else:\n        parts = [float(x.strip()) for x in mode.split(\",\")]\n        if len(parts) != num_classes:\n            raise ValueError(f\"Expected {num_classes} weights, got {len(parts)}: {mode}\")\n        weights = torch.tensor(parts, dtype=torch.float32)\n    return weights\n\n\nclass WeightedCETrainer(Trainer):\n    \"\"\"Trainer with class-weighted CrossEntropyLoss and optional WeightedRandomSampler.\"\"\"\n\n    def __init__(self, class_weights: Optional[torch.Tensor] = None,\n                 weighted_sampler: Optional[WeightedRandomSampler] = None, **kwargs):\n        super().__init__(**kwargs)\n        self._class_weights = class_weights\n        self._weighted_sampler = weighted_sampler\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        labels = inputs.pop(\"labels\")\n        outputs = model(**inputs)\n        logits = outputs.logits\n        if self._class_weights is not None:\n            loss_fn = torch.nn.CrossEntropyLoss(weight=self._class_weights.to(logits.device))\n        else:\n            loss_fn = torch.nn.CrossEntropyLoss()\n        loss = loss_fn(logits, labels)\n        return (loss, outputs) if return_outputs else loss\n\n    def get_train_dataloader(self) -> DataLoader:\n        if self._weighted_sampler is None:\n            return super().get_train_dataloader()\n        return DataLoader(\n            self.train_dataset,\n            batch_size=self.args.per_device_train_batch_size,\n            sampler=self._weighted_sampler,\n            num_workers=self.args.dataloader_num_workers,\n            pin_memory=self.args.dataloader_pin_memory,\n        )\n\n\n# ---------------------------------------------------------------------------\n# Model setup\n# ---------------------------------------------------------------------------\n\ndef setup_model(model_name: str, args):\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForSequenceClassification.from_pretrained(\n        model_name,\n        num_labels=2,\n        id2label=ID2LABEL,\n        label2id=LABEL2ID,\n        trust_remote_code=True,\n        torch_dtype=torch.bfloat16,\n    )\n    model.config.pad_token_id = tokenizer.pad_token_id\n\n    lora_config = LoraConfig(\n        r=args.lora_r,\n        lora_alpha=args.lora_alpha,\n        target_modules=[\"q_proj\", \"v_proj\", \"k_proj\", \"o_proj\"],\n        lora_dropout=args.lora_dropout,\n        task_type=TaskType.SEQ_CLS,\n        modules_to_save=[\"score\"],\n    )\n    model = get_peft_model(model, lora_config)\n    model.print_trainable_parameters()\n    return model, tokenizer\n\n\n# ---------------------------------------------------------------------------\n# Metrics\n# ---------------------------------------------------------------------------\n\ndef compute_metrics(eval_pred):\n    logits, labels = eval_pred\n    preds = np.argmax(logits, axis=-1)\n    acc = accuracy_score(labels, preds)\n    prec, rec, f1, _ = precision_recall_fscore_support(labels, preds, average=None, labels=[0, 1])\n    return {\n        \"accuracy\": acc,\n        \"precision_internal\": prec[0],\n        \"recall_internal\": rec[0],\n        \"f1_internal\": f1[0],\n        \"precision_deterministic\": prec[1],\n        \"recall_deterministic\": rec[1],\n        \"f1_deterministic\": f1[1],\n    }\n\n\ndef per_task_evaluation(trainer, val_dataset, val_samples) -> Dict[str, Any]:\n    \"\"\"Compute per-task accuracy and confusion matrix.\"\"\"\n    predictions = trainer.predict(val_dataset)\n    preds = np.argmax(predictions.predictions, axis=-1)\n    labels = predictions.label_ids\n\n    cm = confusion_matrix(labels, preds, labels=[0, 1]).tolist()\n\n    task_metrics = {}\n    by_task: Dict[str, Dict[str, list]] = {}\n    for i, s in enumerate(val_samples):\n        t = s[\"task_type\"]\n        if t not in by_task:\n            by_task[t] = {\"preds\": [], \"labels\": []}\n        by_task[t][\"preds\"].append(preds[i])\n        by_task[t][\"labels\"].append(labels[i])\n\n    for task, data in sorted(by_task.items()):\n        acc = accuracy_score(data[\"labels\"], data[\"preds\"])\n        n = len(data[\"labels\"])\n        task_metrics[task] = {\"accuracy\": acc, \"n_samples\": n}\n\n    return {\n        \"overall_accuracy\": accuracy_score(labels, preds),\n        \"confusion_matrix\": cm,\n        \"confusion_labels\": [\"internal\", \"deterministic\"],\n        \"per_task\": task_metrics,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n\n    if args.dry_run:\n        print(\"Dry run: imports OK, args parsed successfully.\")\n        print(f\"  model_name:            {args.model_name}\")\n        print(f\"  data_dir:              {args.data_dir}\")\n        print(f\"  output_dir:            {args.output_dir}\")\n        print(f\"  class_weights:         {args.class_weights}\")\n        print(f\"  min_internal_samples:  {args.min_internal_samples}\")\n        print(f\"  upsample_minority:     {args.upsample_minority}\")\n        return\n\n    os.environ[\"CUDA_VISIBLE_DEVICES\"] = str(args.gpu_id)\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    samples = load_labeled_data(args.data_dir)\n    train_samples, val_samples = stratified_split(samples, args.eval_split, args.seed)\n\n    # --- Check minority class sample count ---\n    train_label_counts = Counter(s[\"label\"] for s in train_samples)\n    n_internal = train_label_counts.get(\"internal\", 0)\n    if n_internal < args.min_internal_samples:\n        warnings.warn(\n            f\"Only {n_internal} internal samples in training set \"\n            f\"(threshold: {args.min_internal_samples}). \"\n            f\"Consider collecting more data or using --class_weights auto.\",\n            stacklevel=1,\n        )\n\n    # --- Compute class weights (inverse frequency or manual) ---\n    class_weights = None\n    if args.class_weights is not None:\n        class_weights = compute_class_weights(train_samples, args.class_weights)\n        weight_dict = {label: class_weights[lid].item() for label, lid in LABEL2ID.items()}\n        print(f\"Class weights: {weight_dict}\")\n        print(f\"Effective sample counts: {dict(train_label_counts)}\")\n\n    model, tokenizer = setup_model(args.model_name, args)\n\n    train_dataset = RouterDataset(train_samples, tokenizer, args.max_seq_len)\n    val_dataset = RouterDataset(val_samples, tokenizer, args.max_seq_len)\n\n    # --- Build WeightedRandomSampler for minority oversampling ---\n    # Per-sample weight = 1 / count_of_its_class, so minority samples are drawn more often.\n    weighted_sampler = None\n    if args.upsample_minority:\n        sample_weights = [1.0 / train_label_counts[s[\"label\"]] for s in train_samples]\n        weighted_sampler = WeightedRandomSampler(\n            weights=sample_weights,\n            num_samples=len(train_samples),\n            replacement=True,\n        )\n        print(f\"Upsampling enabled: WeightedRandomSampler with {len(train_samples)} draws/epoch\")\n\n    use_bf16 = torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        num_train_epochs=args.epochs,\n        per_device_train_batch_size=args.batch_size,\n        per_device_eval_batch_size=args.eval_batch_size,\n        learning_rate=args.lr,\n        weight_decay=args.weight_decay,\n        warmup_ratio=args.warmup_ratio,\n        eval_strategy=\"epoch\",\n        save_strategy=\"epoch\",\n        load_best_model_at_end=True,\n        metric_for_best_model=\"accuracy\",\n        greater_is_better=True,\n        bf16=use_bf16,\n        fp16=(not use_bf16 and torch.cuda.is_available()),\n        logging_steps=10,\n        dataloader_num_workers=4,\n        report_to=\"wandb\",\n        run_name=f\"router-sft-{os.path.basename(args.model_name)}-r{args.lora_r}\",\n        seed=args.seed,\n        save_total_limit=2,\n    )\n\n    os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n\n    # --- Log class weighting config to W&B ---\n    try:\n        import wandb\n        wandb_config = vars(args).copy()\n        if class_weights is not None:\n            wandb_config[\"class_weights_values\"] = {\n                label: class_weights[lid].item() for label, lid in LABEL2ID.items()\n            }\n        wandb_config[\"train_label_counts\"] = dict(train_label_counts)\n        wandb_config[\"upsample_minority\"] = args.upsample_minority\n        wandb.init(\n            project=args.wandb_project,\n            name=training_args.run_name,\n            config=wandb_config,\n        )\n    except Exception:\n        pass\n\n    trainer = WeightedCETrainer(\n        class_weights=class_weights,\n        weighted_sampler=weighted_sampler,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=val_dataset,\n        compute_metrics=compute_metrics,\n        callbacks=[EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience)],\n    )\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Starting training: {len(train_dataset)} train / {len(val_dataset)} val samples\")\n    print(f\"Model: {args.model_name}, LoRA r={args.lora_r}, lr={args.lr}\")\n    if class_weights is not None:\n        print(f\"Class weights: {class_weights.tolist()}\")\n    if args.upsample_minority:\n        print(\"Minority oversampling: enabled\")\n    print(f\"{'='*60}\\n\")\n\n    trainer.train()\n\n    adapter_dir = os.path.join(args.output_dir, \"final_adapter\")\n    model.save_pretrained(adapter_dir)\n    tokenizer.save_pretrained(adapter_dir)\n    print(f\"Adapter saved to {adapter_dir}\")\n\n    print(\"\\n--- Evaluation ---\")\n    eval_report = per_task_evaluation(trainer, val_dataset, val_samples)\n\n    report_path = os.path.join(args.output_dir, \"eval_report.json\")\n    with open(report_path, \"w\") as f:\n        json.dump(eval_report, f, indent=2)\n    print(f\"Eval report saved to {report_path}\")\n\n    print(f\"\\nOverall accuracy: {eval_report['overall_accuracy']:.4f}\")\n    print(f\"Confusion matrix (rows=true, cols=pred):\")\n    print(f\"  {eval_report['confusion_labels']}\")\n    for row in eval_report[\"confusion_matrix\"]:\n        print(f\"  {row}\")\n    print(\"\\nPer-task accuracy:\")\n    for task, m in sorted(eval_report[\"per_task\"].items()):\n        print(f\"  {task}: {m['accuracy']:.3f} (n={m['n_samples']})\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py",
    "content": "# Router SFT training script for SimGate modular routing.\n# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data\n# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.\n#\n# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl\n# Usage: python src/router_sft_train.py --help\n\nimport argparse\nimport json\nimport os\nimport glob\nimport random\nimport warnings\nfrom collections import Counter\nfrom typing import List, Dict, Any, Optional, Tuple\n\nimport numpy as np\nimport torch\nfrom torch.utils.data import Dataset, DataLoader, WeightedRandomSampler\nfrom sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix\nfrom transformers import (\n    AutoTokenizer,\n    AutoModelForSequenceClassification,\n    TrainingArguments,\n    Trainer,\n    EarlyStoppingCallback,\n)\nfrom peft import LoraConfig, get_peft_model, TaskType\n\nLABEL2ID = {\"internal\": 0, \"deterministic\": 1}\nID2LABEL = {0: \"internal\", 1: \"deterministic\"}\n\nSYSTEM_PROMPT = (\n    \"You are a routing classifier. Given the current observation and action history, \"\n    \"predict which reasoning modality will lead to a better outcome.\"\n)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Router SFT: finetune LLM for 2-way routing classification\")\n    p.add_argument(\"--data_dir\", type=str, default=\"results/plan_c/\",\n                    help=\"Directory containing {task_type}/labeled_steps.jsonl\")\n    p.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-1.7B\",\n                    help=\"HuggingFace model name or local path\")\n    p.add_argument(\"--output_dir\", type=str, default=\"results/router_sft/\",\n                    help=\"Output directory for checkpoints and reports\")\n    p.add_argument(\"--epochs\", type=int, default=3)\n    p.add_argument(\"--batch_size\", type=int, default=16)\n    p.add_argument(\"--eval_batch_size\", type=int, default=32)\n    p.add_argument(\"--lr\", type=float, default=2e-4)\n    p.add_argument(\"--lora_r\", type=int, default=16)\n    p.add_argument(\"--lora_alpha\", type=int, default=32)\n    p.add_argument(\"--lora_dropout\", type=float, default=0.05)\n    p.add_argument(\"--max_seq_len\", type=int, default=512)\n    p.add_argument(\"--gpu_id\", type=int, default=0)\n    p.add_argument(\"--wandb_project\", type=str, default=\"simgate-router-sft\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    p.add_argument(\"--eval_split\", type=float, default=0.2)\n    p.add_argument(\"--warmup_ratio\", type=float, default=0.1)\n    p.add_argument(\"--weight_decay\", type=float, default=0.01)\n    p.add_argument(\"--early_stopping_patience\", type=int, default=2)\n    p.add_argument(\"--dry_run\", action=\"store_true\", help=\"Only validate imports and args, skip training\")\n    p.add_argument(\"--class_weights\", type=str, default=None,\n                    help='\"auto\" for inverse-frequency weights, or \"w0,w1\" (internal:w0, det:w1)')\n    p.add_argument(\"--min_internal_samples\", type=int, default=10,\n                    help=\"Warn if internal samples < this threshold (default: 10)\")\n    p.add_argument(\"--upsample_minority\", action=\"store_true\",\n                    help=\"Use WeightedRandomSampler to oversample minority class\")\n    return p.parse_args()\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:\n    \"\"\"Keep the most recent N actions as a summary.\"\"\"\n    recent = action_history[-max_actions:] if action_history else []\n    if not recent:\n        return \"(none)\"\n    return \" → \".join(recent)\n\n\ndef build_prompt(observation: str, action_history: List[str]) -> str:\n    history_summary = summarize_action_history(action_history)\n    return (\n        f\"<|system|>{SYSTEM_PROMPT}<|end|>\\n\"\n        f\"<|user|>\\n\"\n        f\"Observation: {observation}\\n\"\n        f\"Action history: {history_summary}\\n\"\n        f\"<|end|>\"\n    )\n\n\ndef load_labeled_data(data_dir: str) -> List[Dict[str, Any]]:\n    \"\"\"Load all labeled_steps.jsonl files, filtering out ties.\"\"\"\n    pattern = os.path.join(data_dir, \"*\", \"labeled_steps.jsonl\")\n    files = sorted(glob.glob(pattern))\n    if not files:\n        pattern_flat = os.path.join(data_dir, \"labeled_steps.jsonl\")\n        if os.path.exists(pattern_flat):\n            files = [pattern_flat]\n    if not files:\n        raise FileNotFoundError(f\"No labeled_steps.jsonl found in {data_dir}\")\n\n    samples = []\n    for fpath in files:\n        task_type = os.path.basename(os.path.dirname(fpath))\n        with open(fpath) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                record = json.loads(line)\n                label = record.get(\"label\", \"\")\n                if label not in LABEL2ID:\n                    continue\n                samples.append({\n                    \"observation\": record.get(\"observation\", \"\"),\n                    \"action_history\": record.get(\"action_history\", []),\n                    \"label\": label,\n                    \"label_id\": LABEL2ID[label],\n                    \"task_type\": record.get(\"task_name\", task_type),\n                })\n\n    print(f\"Loaded {len(samples)} samples from {len(files)} files (ties excluded)\")\n    label_dist = Counter(s[\"label\"] for s in samples)\n    for k, v in sorted(label_dist.items()):\n        print(f\"  {k}: {v} ({v/len(samples)*100:.1f}%)\")\n    return samples\n\n\ndef stratified_split(\n    samples: List[Dict], eval_ratio: float, seed: int\n) -> Tuple[List[Dict], List[Dict]]:\n    \"\"\"Stratified train/val split by task_type.\"\"\"\n    rng = random.Random(seed)\n    by_task: Dict[str, List[Dict]] = {}\n    for s in samples:\n        by_task.setdefault(s[\"task_type\"], []).append(s)\n\n    train_set, val_set = [], []\n    for task, items in by_task.items():\n        rng.shuffle(items)\n        n_val = max(1, int(len(items) * eval_ratio))\n        val_set.extend(items[:n_val])\n        train_set.extend(items[n_val:])\n\n    rng.shuffle(train_set)\n    rng.shuffle(val_set)\n    print(f\"Split: train={len(train_set)}, val={len(val_set)}\")\n    return train_set, val_set\n\n\nclass RouterDataset(Dataset):\n    def __init__(self, samples: List[Dict], tokenizer, max_length: int):\n        self.samples = samples\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n\n    def __len__(self):\n        return len(self.samples)\n\n    def __getitem__(self, idx):\n        s = self.samples[idx]\n        prompt = build_prompt(s[\"observation\"], s[\"action_history\"])\n        encoding = self.tokenizer(\n            prompt,\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        return {\n            \"input_ids\": encoding[\"input_ids\"].squeeze(0),\n            \"attention_mask\": encoding[\"attention_mask\"].squeeze(0),\n            \"labels\": torch.tensor(s[\"label_id\"], dtype=torch.long),\n        }\n\n\n# ---------------------------------------------------------------------------\n# Class weighting\n# ---------------------------------------------------------------------------\n\ndef compute_class_weights(train_samples: List[Dict], mode: str = \"auto\") -> torch.Tensor:\n    # \"auto\": weight_c = N_total / (num_classes * N_c), i.e. inverse frequency —\n    #         rarer class gets proportionally higher weight.\n    # \"w0,w1\": manual weights, e.g. \"1.0,5.0\" -> internal=1.0, deterministic=5.0\n    num_classes = len(LABEL2ID)\n    if mode == \"auto\":\n        counts = Counter(s[\"label_id\"] for s in train_samples)\n        total = len(train_samples)\n        weights = torch.tensor(\n            [total / (num_classes * max(counts.get(i, 1), 1)) for i in range(num_classes)],\n            dtype=torch.float32,\n        )\n    else:\n        parts = [float(x.strip()) for x in mode.split(\",\")]\n        if len(parts) != num_classes:\n            raise ValueError(f\"Expected {num_classes} weights, got {len(parts)}: {mode}\")\n        weights = torch.tensor(parts, dtype=torch.float32)\n    return weights\n\n\nclass WeightedCETrainer(Trainer):\n    \"\"\"Trainer with class-weighted CrossEntropyLoss and optional WeightedRandomSampler.\"\"\"\n\n    def __init__(self, class_weights: Optional[torch.Tensor] = None,\n                 weighted_sampler: Optional[WeightedRandomSampler] = None, **kwargs):\n        super().__init__(**kwargs)\n        self._class_weights = class_weights\n        self._weighted_sampler = weighted_sampler\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        labels = inputs.pop(\"labels\")\n        outputs = model(**inputs)\n        logits = outputs.logits\n        if self._class_weights is not None:\n            loss_fn = torch.nn.CrossEntropyLoss(weight=self._class_weights.to(logits.device))\n        else:\n            loss_fn = torch.nn.CrossEntropyLoss()\n        loss = loss_fn(logits, labels)\n        return (loss, outputs) if return_outputs else loss\n\n    def get_train_dataloader(self) -> DataLoader:\n        if self._weighted_sampler is None:\n            return super().get_train_dataloader()\n        return DataLoader(\n            self.train_dataset,\n            batch_size=self.args.per_device_train_batch_size,\n            sampler=self._weighted_sampler,\n            num_workers=self.args.dataloader_num_workers,\n            pin_memory=self.args.dataloader_pin_memory,\n        )\n\n\n# ---------------------------------------------------------------------------\n# Model setup\n# ---------------------------------------------------------------------------\n\ndef setup_model(model_name: str, args):\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForSequenceClassification.from_pretrained(\n        model_name,\n        num_labels=2,\n        id2label=ID2LABEL,\n        label2id=LABEL2ID,\n        trust_remote_code=True,\n        torch_dtype=torch.bfloat16,\n    )\n    model.config.pad_token_id = tokenizer.pad_token_id\n\n    lora_config = LoraConfig(\n        r=args.lora_r,\n        lora_alpha=args.lora_alpha,\n        target_modules=[\"q_proj\", \"v_proj\", \"k_proj\", \"o_proj\"],\n        lora_dropout=args.lora_dropout,\n        task_type=TaskType.SEQ_CLS,\n        modules_to_save=[\"score\"],\n    )\n    model = get_peft_model(model, lora_config)\n    model.print_trainable_parameters()\n    return model, tokenizer\n\n\n# ---------------------------------------------------------------------------\n# Metrics\n# ---------------------------------------------------------------------------\n\ndef compute_metrics(eval_pred):\n    logits, labels = eval_pred\n    preds = np.argmax(logits, axis=-1)\n    acc = accuracy_score(labels, preds)\n    prec, rec, f1, _ = precision_recall_fscore_support(labels, preds, average=None, labels=[0, 1])\n    return {\n        \"accuracy\": acc,\n        \"precision_internal\": prec[0],\n        \"recall_internal\": rec[0],\n        \"f1_internal\": f1[0],\n        \"precision_deterministic\": prec[1],\n        \"recall_deterministic\": rec[1],\n        \"f1_deterministic\": f1[1],\n    }\n\n\ndef per_task_evaluation(trainer, val_dataset, val_samples) -> Dict[str, Any]:\n    \"\"\"Compute per-task accuracy and confusion matrix.\"\"\"\n    predictions = trainer.predict(val_dataset)\n    preds = np.argmax(predictions.predictions, axis=-1)\n    labels = predictions.label_ids\n\n    cm = confusion_matrix(labels, preds, labels=[0, 1]).tolist()\n\n    task_metrics = {}\n    by_task: Dict[str, Dict[str, list]] = {}\n    for i, s in enumerate(val_samples):\n        t = s[\"task_type\"]\n        if t not in by_task:\n            by_task[t] = {\"preds\": [], \"labels\": []}\n        by_task[t][\"preds\"].append(preds[i])\n        by_task[t][\"labels\"].append(labels[i])\n\n    for task, data in sorted(by_task.items()):\n        acc = accuracy_score(data[\"labels\"], data[\"preds\"])\n        n = len(data[\"labels\"])\n        task_metrics[task] = {\"accuracy\": acc, \"n_samples\": n}\n\n    return {\n        \"overall_accuracy\": accuracy_score(labels, preds),\n        \"confusion_matrix\": cm,\n        \"confusion_labels\": [\"internal\", \"deterministic\"],\n        \"per_task\": task_metrics,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    args = parse_args()\n\n    if args.dry_run:\n        print(\"Dry run: imports OK, args parsed successfully.\")\n        print(f\"  model_name:            {args.model_name}\")\n        print(f\"  data_dir:              {args.data_dir}\")\n        print(f\"  output_dir:            {args.output_dir}\")\n        print(f\"  class_weights:         {args.class_weights}\")\n        print(f\"  min_internal_samples:  {args.min_internal_samples}\")\n        print(f\"  upsample_minority:     {args.upsample_minority}\")\n        return\n\n    os.environ[\"CUDA_VISIBLE_DEVICES\"] = str(args.gpu_id)\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    samples = load_labeled_data(args.data_dir)\n    train_samples, val_samples = stratified_split(samples, args.eval_split, args.seed)\n\n    # --- Check minority class sample count ---\n    train_label_counts = Counter(s[\"label\"] for s in train_samples)\n    n_internal = train_label_counts.get(\"internal\", 0)\n    if n_internal < args.min_internal_samples:\n        warnings.warn(\n            f\"Only {n_internal} internal samples in training set \"\n            f\"(threshold: {args.min_internal_samples}). \"\n            f\"Consider collecting more data or using --class_weights auto.\",\n            stacklevel=1,\n        )\n\n    # --- Compute class weights (inverse frequency or manual) ---\n    class_weights = None\n    if args.class_weights is not None:\n        class_weights = compute_class_weights(train_samples, args.class_weights)\n        weight_dict = {label: class_weights[lid].item() for label, lid in LABEL2ID.items()}\n        print(f\"Class weights: {weight_dict}\")\n        print(f\"Effective sample counts: {dict(train_label_counts)}\")\n\n    model, tokenizer = setup_model(args.model_name, args)\n\n    train_dataset = RouterDataset(train_samples, tokenizer, args.max_seq_len)\n    val_dataset = RouterDataset(val_samples, tokenizer, args.max_seq_len)\n\n    # --- Build WeightedRandomSampler for minority oversampling ---\n    # Per-sample weight = 1 / count_of_its_class, so minority samples are drawn more often.\n    weighted_sampler = None\n    if args.upsample_minority:\n        sample_weights = [1.0 / train_label_counts[s[\"label\"]] for s in train_samples]\n        weighted_sampler = WeightedRandomSampler(\n            weights=sample_weights,\n            num_samples=len(train_samples),\n            replacement=True,\n        )\n        print(f\"Upsampling enabled: WeightedRandomSampler with {len(train_samples)} draws/epoch\")\n\n    use_bf16 = torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        num_train_epochs=args.epochs,\n        per_device_train_batch_size=args.batch_size,\n        per_device_eval_batch_size=args.eval_batch_size,\n        learning_rate=args.lr,\n        weight_decay=args.weight_decay,\n        warmup_ratio=args.warmup_ratio,\n        eval_strategy=\"epoch\",\n        save_strategy=\"epoch\",\n        load_best_model_at_end=True,\n        metric_for_best_model=\"accuracy\",\n        greater_is_better=True,\n        bf16=use_bf16,\n        fp16=(not use_bf16 and torch.cuda.is_available()),\n        logging_steps=10,\n        dataloader_num_workers=4,\n        report_to=\"wandb\",\n        run_name=f\"router-sft-{os.path.basename(args.model_name)}-r{args.lora_r}\",\n        seed=args.seed,\n        save_total_limit=2,\n    )\n\n    os.environ[\"WANDB_PROJECT\"] = args.wandb_project\n\n    # --- Log class weighting config to W&B ---\n    try:\n        import wandb\n        wandb_config = vars(args).copy()\n        if class_weights is not None:\n            wandb_config[\"class_weights_values\"] = {\n                label: class_weights[lid].item() for label, lid in LABEL2ID.items()\n            }\n        wandb_config[\"train_label_counts\"] = dict(train_label_counts)\n        wandb_config[\"upsample_minority\"] = args.upsample_minority\n        wandb.init(\n            project=args.wandb_project,\n            name=training_args.run_name,\n            config=wandb_config,\n        )\n    except Exception:\n        pass\n\n    trainer = WeightedCETrainer(\n        class_weights=class_weights,\n        weighted_sampler=weighted_sampler,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=val_dataset,\n        compute_metrics=compute_metrics,\n        callbacks=[EarlyStoppingCallback(early_stopping_patience=args.early_stopping_patience)],\n    )\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Starting training: {len(train_dataset)} train / {len(val_dataset)} val samples\")\n    print(f\"Model: {args.model_name}, LoRA r={args.lora_r}, lr={args.lr}\")\n    if class_weights is not None:\n        print(f\"Class weights: {class_weights.tolist()}\")\n    if args.upsample_minority:\n        print(\"Minority oversampling: enabled\")\n    print(f\"{'='*60}\\n\")\n\n    trainer.train()\n\n    adapter_dir = os.path.join(args.output_dir, \"final_adapter\")\n    model.save_pretrained(adapter_dir)\n    tokenizer.save_pretrained(adapter_dir)\n    print(f\"Adapter saved to {adapter_dir}\")\n\n    print(\"\\n--- Evaluation ---\")\n    eval_report = per_task_evaluation(trainer, val_dataset, val_samples)\n\n    report_path = os.path.join(args.output_dir, \"eval_report.json\")\n    with open(report_path, \"w\") as f:\n        json.dump(eval_report, f, indent=2)\n    print(f\"Eval report saved to {report_path}\")\n\n    print(f\"\\nOverall accuracy: {eval_report['overall_accuracy']:.4f}\")\n    print(f\"Confusion matrix (rows=true, cols=pred):\")\n    print(f\"  {eval_report['confusion_labels']}\")\n    for row in eval_report[\"confusion_matrix\"]:\n        print(f\"  {row}\")\n    print(\"\\nPer-task accuracy:\")\n    for task, m in sorted(eval_report[\"per_task\"].items()):\n        print(f\"  {task}: {m['accuracy']:.3f} (n={m['n_samples']})\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T20:23:17.363474+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T20:23:17.363646+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "base64 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py",
  "description": "Base64 encode the modified file for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "Bash",
  "tool_args": {
    "command": "base64 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py",
    "description": "Base64 encode the modified file for transfer"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T20:23:17.363872+00:00_

IyBSb3V0ZXIgU0ZUIHRyYWluaW5nIHNjcmlwdCBmb3IgU2ltR2F0ZSBtb2R1bGFyIHJvdXRpbmcu
CiMgRmluZXR1bmVzIFF3ZW4zLTEuN0IgKG9yIGZhbGxiYWNrKSBvbiBlcGlzb2RlLWxldmVsIGxh
YmVsZWQgZGF0YQojIGZyb20gUGxhbiBDIChsYWJlbGVkX3N0ZXBzLmpzb25sKSBmb3IgMi13YXkg
Y2xhc3NpZmljYXRpb246IGludGVybmFsIHZzIGRldGVybWluaXN0aWMuCiMKIyBEYXRhIGRlcGVu
ZGVuY3k6IHJlc3VsdHMvcGxhbl9jL3t0YXNrX3R5cGV9L2xhYmVsZWRfc3RlcHMuanNvbmwKIyBV
c2FnZTogcHl0aG9uIHNyYy9yb3V0ZXJfc2Z0X3RyYWluLnB5IC0taGVscAoKaW1wb3J0IGFyZ3Bh
cnNlCmltcG9ydCBqc29uCmltcG9ydCBvcwppbXBvcnQgZ2xvYgppbXBvcnQgcmFuZG9tCmltcG9y
dCB3YXJuaW5ncwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gdHlwaW5nIGlt
cG9ydCBMaXN0LCBEaWN0LCBBbnksIE9wdGlvbmFsLCBUdXBsZQoKaW1wb3J0IG51bXB5IGFzIG5w
CmltcG9ydCB0b3JjaApmcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFzZXQsIERhdGFM
b2FkZXIsIFdlaWdodGVkUmFuZG9tU2FtcGxlcgpmcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQg
YWNjdXJhY3lfc2NvcmUsIHByZWNpc2lvbl9yZWNhbGxfZnNjb3JlX3N1cHBvcnQsIGNvbmZ1c2lv
bl9tYXRyaXgKZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0ICgKICAgIEF1dG9Ub2tlbml6ZXIsCiAg
ICBBdXRvTW9kZWxGb3JTZXF1ZW5jZUNsYXNzaWZpY2F0aW9uLAogICAgVHJhaW5pbmdBcmd1bWVu
dHMsCiAgICBUcmFpbmVyLAogICAgRWFybHlTdG9wcGluZ0NhbGxiYWNrLAopCmZyb20gcGVmdCBp
bXBvcnQgTG9yYUNvbmZpZywgZ2V0X3BlZnRfbW9kZWwsIFRhc2tUeXBlCgpMQUJFTDJJRCA9IHsi
aW50ZXJuYWwiOiAwLCAiZGV0ZXJtaW5pc3RpYyI6IDF9CklEMkxBQkVMID0gezA6ICJpbnRlcm5h
bCIsIDE6ICJkZXRlcm1pbmlzdGljIn0KClNZU1RFTV9QUk9NUFQgPSAoCiAgICAiWW91IGFyZSBh
IHJvdXRpbmcgY2xhc3NpZmllci4gR2l2ZW4gdGhlIGN1cnJlbnQgb2JzZXJ2YXRpb24gYW5kIGFj
dGlvbiBoaXN0b3J5LCAiCiAgICAicHJlZGljdCB3aGljaCByZWFzb25pbmcgbW9kYWxpdHkgd2ls
bCBsZWFkIHRvIGEgYmV0dGVyIG91dGNvbWUuIgopCgoKZGVmIHBhcnNlX2FyZ3MoKToKICAgIHAg
PSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0iUm91dGVyIFNGVDogZmluZXR1
bmUgTExNIGZvciAyLXdheSByb3V0aW5nIGNsYXNzaWZpY2F0aW9uIikKICAgIHAuYWRkX2FyZ3Vt
ZW50KCItLWRhdGFfZGlyIiwgdHlwZT1zdHIsIGRlZmF1bHQ9InJlc3VsdHMvcGxhbl9jLyIsCiAg
ICAgICAgICAgICAgICAgICAgaGVscD0iRGlyZWN0b3J5IGNvbnRhaW5pbmcge3Rhc2tfdHlwZX0v
bGFiZWxlZF9zdGVwcy5qc29ubCIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1tb2RlbF9uYW1lIiw
…[truncated 22684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T20:23:17.364038+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "cp /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py.bak && echo \"BACKUP_OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "cp /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py.bak && echo \"BACKUP_OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T20:23:17.364171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"BACKUP_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T20:23:17.364365+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "cat << 'B64EOF' | base64 -d > /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py\nIyBSb3V0ZXIgU0ZUIHRyYWluaW5nIHNjcmlwdCBmb3IgU2ltR2F0ZSBtb2R1bGFyIHJvdXRpbmcu\nCiMgRmluZXR1bmVzIFF3ZW4zLTEuN0IgKG9yIGZhbGxiYWNrKSBvbiBlcGlzb2RlLWxldmVsIGxh\nYmVsZWQgZGF0YQojIGZyb20gUGxhbiBDIChsYWJlbGVkX3N0ZXBzLmpzb25sKSBmb3IgMi13YXkg\nY2xhc3NpZmljYXRpb246IGludGVybmFsIHZzIGRldGVybWluaXN0aWMuCiMKIyBEYXRhIGRlcGVu\nZGVuY3k6IHJlc3VsdHMvcGxhbl9jL3t0YXNrX3R5cGV9L2xhYmVsZWRfc3RlcHMuanNvbmwKIyBV\nc2FnZTogcHl0aG9uIHNyYy9yb3V0ZXJfc2Z0X3RyYWluLnB5IC0taGVscAoKaW1wb3J0IGFyZ3Bh\ncnNlCmltcG9ydCBqc29uCmltcG9ydCBvcwppbXBvcnQgZ2xvYgppbXBvcnQgcmFuZG9tCmltcG9y\ndCB3YXJuaW5ncwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gdHlwaW5nIGlt\ncG9ydCBMaXN0LCBEaWN0LCBBbnksIE9wdGlvbmFsLCBUdXBsZQoKaW1wb3J0IG51bXB5IGFzIG5w\nCmltcG9ydCB0b3JjaApmcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFzZXQsIERhdGFM\nb2FkZXIsIFdlaWdodGVkUmFuZG9tU2FtcGxlcgpmcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQg\nYWNjdXJhY3lfc2NvcmUsIHByZWNpc2lvbl9yZWNhbGxfZnNjb3JlX3N1cHBvcnQsIGNvbmZ1c2lv\nbl9tYXRyaXgKZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0ICgKICAgIEF1dG9Ub2tlbml6ZXIsCiAg\nICBBdXRvTW9kZWxGb3JTZXF1ZW5jZUNsYXNzaWZpY2F0aW9uLAogICAgVHJhaW5pbmdBcmd1bWVu\ndHMsCiAgICBUcmFpbmVyLAogICAgRWFybHlTdG9wcGluZ0NhbGxiYWNrLAopCmZyb20gcGVmdCBp\nbXBvcnQgTG9yYUNvbmZpZywgZ2V0X3BlZnRfbW9kZWwsIFRhc2tUeXBlCgpMQUJFTDJJRCA9IHsi\naW50ZXJuYWwiOiAwLCAiZGV0ZXJtaW5pc3RpYyI6IDF9CklEMkxBQkVMID0gezA6ICJpbnRlcm5h\nbCIsIDE6ICJkZXRlcm1pbmlzdGljIn0KClNZU1RFTV9QUk9NUFQgPSAoCiAgICAiWW91IGFyZSBh\nIHJvdXRpbmcgY2xhc3NpZmllci4gR2l2ZW4gdGhlIGN1cnJlbnQgb2JzZXJ2YXRpb24gYW5kIGFj\ndGlvbiBoaXN0b3J5LCAiCiAgICAicHJlZGljdCB3aGljaCByZWFzb25pbmcgbW9kYWxpdHkgd2ls\nbCBsZWFkIHRvIGEgYmV0dGVyIG91dGNvbWUuIgopCgoKZGVmIHBhcnNlX2FyZ3MoKToKICAgIHAg\nPSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0iUm91dGVyIFNGVDogZmluZXR1\nbmUgTExNIGZvciAyLXdheSByb3V0aW5nIGNsYXNzaWZpY2F0aW9uIikKICAgIHAuYWRkX2FyZ3Vt\nZW50KCItLWRhdGFfZGlyIiwgdHlwZT1zdHIsIGRlZmF1bHQ9InJlc3VsdHMvcGxhbl9jLyIsCiAg\nICAgICAgICAgICAgICAgICAgaGVscD0iRGlyZWN0b3J5IGNvbnRhaW5pbmcge3Rhc2tfdHlwZX0v\nbGFiZWxlZF9zdGVwcy5qc29ubCIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1tb2RlbF9uYW1lIiwg\ndHlwZT1zdHIsIGRlZmF1bHQ9IlF3ZW4vUXdlbjMtMS43QiIsCiAgICAgICAgICAgICAgICAgICAg\naGVscD0iSHVnZ2luZ0ZhY2UgbW9kZWwgbmFtZSBvciBsb2NhbCBwYXRoIikKICAgIHAuYWRkX2Fy\nZ3VtZW50KCItLW91dHB1dF9kaXIiLCB0eXBlPXN0ciwgZGVmYXVsdD0icmVzdWx0cy9yb3V0ZXJf\nc2Z0LyIsCiAgICAgICAgICAgICAgICAgICAgaGVscD0iT3V0cHV0IGRpcmVjdG9yeSBmb3IgY2hl\nY2twb2ludHMgYW5kIHJlcG9ydHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tZXBvY2hzIiwgdHlw\nZT1pbnQsIGRlZmF1bHQ9MykKICAgIHAuYWRkX2FyZ3VtZW50KCItLWJhdGNoX3NpemUiLCB0eXBl\nPWludCwgZGVmYXVsdD0xNikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWV2YWxfYmF0Y2hfc2l6ZSIs\nIHR5cGU9aW50LCBkZWZhdWx0PTMyKQogICAgcC5hZGRfYXJndW1lbnQoIi0tbHIiLCB0eXBlPWZs\nb2F0LCBkZWZhdWx0PTJlLTQpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1sb3JhX3IiLCB0eXBlPWlu\ndCwgZGVmYXVsdD0xNikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWxvcmFfYWxwaGEiLCB0eXBlPWlu\ndCwgZGVmYXVsdD0zMikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWxvcmFfZHJvcG91dCIsIHR5cGU9\nZmxvYXQsIGRlZmF1bHQ9MC4wNSkKICAgIHAuYWRkX2FyZ3VtZW50KCItLW1heF9zZXFfbGVuIiwg\ndHlwZT1pbnQsIGRlZmF1bHQ9NTEyKQogICAgcC5hZGRfYXJndW1lbnQoIi0tZ3B1X2lkIiwgdHlw\nZT1pbnQsIGRlZmF1bHQ9MCkKICAgIHAuYWRkX2FyZ3VtZW50KCItLXdhbmRiX3Byb2plY3QiLCB0\neXBlPXN0ciwgZGVmYXVsdD0ic2ltZ2F0ZS1yb3V0ZXItc2Z0IikKICAgIHAuYWRkX2FyZ3VtZW50\nKCItLXNlZWQiLCB0eXBlPWludCwgZGVmYXVsdD00MikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWV2\nYWxfc3BsaXQiLCB0eXBlPWZsb2F0LCBkZWZhdWx0PTAuMikKICAgIHAuYWRkX2FyZ3VtZW50KCIt\nLXdhcm11cF9yYXRpbyIsIHR5cGU9ZmxvYXQsIGRlZmF1bHQ9MC4xKQogICAgcC5hZGRfYXJndW1l\nbnQoIi0td2VpZ2h0X2RlY2F5IiwgdHlwZT1mbG9hdCwgZGVmYXVsdD0wLjAxKQogICAgcC5hZGRf\nYXJndW1lbnQoIi0tZWFybHlfc3RvcHBpbmdfcGF0aWVuY2UiLCB0eXBlPWludCwgZGVmYXVsdD0y\nKQogICAgcC5hZGRfYXJndW1lbnQoIi0tZHJ5X3J1biIsIGFjdGlvbj0ic3RvcmVfdHJ1ZSIsIGhl\nbHA9Ik9ubHkgdmFsaWRhdGUgaW1wb3J0cyBhbmQgYXJncywgc2tpcCB0cmFpbmluZyIpCiAgICBw\nLmFkZF9hcmd1bWVudCgiLS1jbGFzc193ZWlnaHRzIiwgdHlwZT1zdHIsIGRlZmF1bHQ9Tm9uZSwK\nICAgICAgICAgICAgICAgICAgICBoZWxwPSciYXV0byIgZm9yIGludmVyc2UtZnJlcXVlbmN5IHdl\naWdodHMsIG9yICJ3MCx3MSIgKGludGVybmFsOncwLCBkZXQ6dzEpJykKICAgIHAuYWRkX2FyZ3Vt\nZW50KCItLW1pbl9pbnRlcm5hbF9zYW1wbGVzIiwgdHlwZT1pbnQsIGRlZmF1bHQ9MTAsCiAgICAg\nICAgICAgICAgICAgICAgaGVscD0iV2FybiBpZiBpbnRlcm5hbCBzYW1wbGVzIDwgdGhpcyB0aHJl\nc2hvbGQgKGRlZmF1bHQ6IDEwKSIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS11cHNhbXBsZV9taW5v\ncml0eSIsIGFjdGlvbj0ic3RvcmVfdHJ1ZSIsCiAgICAgICAgICAgICAgICAgICAgaGVscD0iVXNl\nIFdlaWdodGVkUmFuZG9tU2FtcGxlciB0byBvdmVyc2FtcGxlIG1pbm9yaXR5IGNsYXNzIikKICAg\nIHJldHVybiBwLnBhcnNlX2FyZ3MoKQoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgRGF0YSBsb2Fk\naW5nCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgc3VtbWFyaXplX2FjdGlvbl9oaXN0b3J5KGFj\ndGlvbl9oaXN0b3J5OiBMaXN0W3N0cl0sIG1heF9hY3Rpb25zOiBpbnQgPSA1KSAtPiBzdHI6CiAg\nICAiIiJLZWVwIHRoZSBtb3N0IHJlY2VudCBOIGFjdGlvbnMgYXMgYSBzdW1tYXJ5LiIiIgogICAg\ncmVjZW50ID0gYWN0aW9uX2hpc3RvcnlbLW1heF9hY3Rpb25zOl0gaWYgYWN0aW9uX2hpc3Rvcnkg\nZWxzZSBbXQogICAgaWYgbm90IHJlY2VudDoKICAgICAgICByZXR1cm4gIihub25lKSIKICAgIHJl\ndHVybiAiIOKGkiAiLmpvaW4ocmVjZW50KQoKCmRlZiBidWlsZF9wcm9tcHQob2JzZXJ2YXRpb246\nIHN0ciwgYWN0aW9uX2hpc3Rvcnk6IExpc3Rbc3RyXSkgLT4gc3RyOgogICAgaGlzdG9yeV9zdW1t\nYXJ5ID0gc3VtbWFyaXplX2FjdGlvbl9oaXN0b3J5KGFjdGlvbl9oaXN0b3J5KQogICAgcmV0dXJu\nICgKICAgICAgICBmIjx8c3lzdGVtfD57U1lTVEVNX1BST01QVH08fGVuZHw+XG4iCiAgICAgICAg\nZiI8fHVzZXJ8PlxuIgogICAgICAgIGYiT2JzZXJ2YXRpb246IHtvYnNlcnZhdGlvbn1cbiIKICAg\nICAgICBmIkFjdGlvbiBoaXN0b3J5OiB7aGlzdG9yeV9zdW1tYXJ5fVxuIgogICAgICAgIGYiPHxl\nbmR8PiIKICAgICkKCgpkZWYgbG9hZF9sYWJlbGVkX2RhdGEoZGF0YV9kaXI6IHN0cikgLT4gTGlz\ndFtEaWN0W3N0ciwgQW55XV06CiAgICAiIiJMb2FkIGFsbCBsYWJlbGVkX3N0ZXBzLmpzb25sIGZp\nbGVzLCBmaWx0ZXJpbmcgb3V0IHRpZXMuIiIiCiAgICBwYXR0ZXJuID0gb3MucGF0aC5qb2luKGRh\ndGFfZGlyLCAiKiIsICJsYWJlbGVkX3N0ZXBzLmpzb25sIikKICAgIGZpbGVzID0gc29ydGVkKGds\nb2IuZ2xvYihwYXR0ZXJuKSkKICAgIGlmIG5vdCBmaWxlczoKICAgICAgICBwYXR0ZXJuX2ZsYXQg\nPSBvcy5wYXRoLmpvaW4oZGF0YV9kaXIsICJsYWJlbGVkX3N0ZXBzLmpzb25sIikKICAgICAgICBp\nZiBvcy5wYXRoLmV4aXN0cyhwYXR0ZXJuX2ZsYXQpOgogICAgICAgICAgICBmaWxlcyA9IFtwYXR0\nZXJuX2ZsYXRdCiAgICBpZiBub3QgZmlsZXM6CiAgICAgICAgcmFpc2UgRmlsZU5vdEZvdW5kRXJy\nb3IoZiJObyBsYWJlbGVkX3N0ZXBzLmpzb25sIGZvdW5kIGluIHtkYXRhX2Rpcn0iKQoKICAgIHNh\nbXBsZXMgPSBbXQogICAgZm9yIGZwYXRoIGluIGZpbGVzOgogICAgICAgIHRhc2tfdHlwZSA9IG9z\nLnBhdGguYmFzZW5hbWUob3MucGF0aC5kaXJuYW1lKGZwYXRoKSkKICAgICAgICB3aXRoIG9wZW4o\nZnBhdGgpIGFzIGY6CiAgICAgICAgICAgIGZvciBsaW5lIGluIGY6CiAgICAgICAgICAgICAgICBs\naW5lID0gbGluZS5zdHJpcCgpCiAgICAgICAgICAgICAgICBpZiBub3QgbGluZToKICAgICAgICAg\nICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICAgICAgcmVjb3JkID0ganNvbi5sb2Fkcyhs\naW5lKQogICAgICAgICAgICAgICAgbGFiZWwgPSByZWNvcmQuZ2V0KCJsYWJlbCIsICIiKQogICAg\nICAgICAgICAgICAgaWYgbGFiZWwgbm90IGluIExBQkVMMklEOgogICAgICAgICAgICAgICAgICAg\nIGNvbnRpbnVlCiAgICAgICAgICAgICAgICBzYW1wbGVzLmFwcGVuZCh7CiAgICAgICAgICAgICAg\nICAgICAgIm9ic2VydmF0aW9uIjogcmVjb3JkLmdldCgib2JzZXJ2YXRpb24iLCAiIiksCiAgICAg\nICAgICAgICAgICAgICAgImFjdGlvbl9oaXN0b3J5IjogcmVjb3JkLmdldCgiYWN0aW9uX2hpc3Rv\ncnkiLCBbXSksCiAgICAgICAgICAgICAgICAgICAgImxhYmVsIjogbGFiZWwsCiAgICAgICAgICAg\nICAgICAgICAgImxhYmVsX2lkIjogTEFCRUwySURbbGFiZWxdLAogICAgICAgICAgICAgICAgICAg\nICJ0YXNrX3R5cGUiOiByZWNvcmQuZ2V0KCJ0YXNrX25hbWUiLCB0YXNrX3R5cGUpLAogICAgICAg\nICAgICAgICAgfSkKCiAgICBwcmludChmIkxvYWRlZCB7bGVuKHNhbXBsZXMpfSBzYW1wbGVzIGZy\nb20ge2xlbihmaWxlcyl9IGZpbGVzICh0aWVzIGV4Y2x1ZGVkKSIpCiAgICBsYWJlbF9kaXN0ID0g\nQ291bnRlcihzWyJsYWJlbCJdIGZvciBzIGluIHNhbXBsZXMpCiAgICBmb3IgaywgdiBpbiBzb3J0\nZWQobGFiZWxfZGlzdC5pdGVtcygpKToKICAgICAgICBwcmludChmIiAge2t9OiB7dn0gKHt2L2xl\nbihzYW1wbGVzKSoxMDA6LjFmfSUpIikKICAgIHJldHVybiBzYW1wbGVzCgoKZGVmIHN0cmF0aWZp\nZWRfc3BsaXQoCiAgICBzYW1wbGVzOiBMaXN0W0RpY3RdLCBldmFsX3JhdGlvOiBmbG9hdCwgc2Vl\nZDogaW50CikgLT4gVHVwbGVbTGlzdFtEaWN0XSwgTGlzdFtEaWN0XV06CiAgICAiIiJTdHJhdGlm\naWVkIHRyYWluL3ZhbCBzcGxpdCBieSB0YXNrX3R5cGUuIiIiCiAgICBybmcgPSByYW5kb20uUmFu\nZG9tKHNlZWQpCiAgICBieV90YXNrOiBEaWN0W3N0ciwgTGlzdFtEaWN0XV0gPSB7fQogICAgZm9y\nIHMgaW4gc2FtcGxlczoKICAgICAgICBieV90YXNrLnNldGRlZmF1bHQoc1sidGFza190eXBlIl0s\nIFtdKS5hcHBlbmQocykKCiAgICB0cmFpbl9zZXQsIHZhbF9zZXQgPSBbXSwgW10KICAgIGZvciB0\nYXNrLCBpdGVtcyBpbiBieV90YXNrLml0ZW1zKCk6CiAgICAgICAgcm5nLnNodWZmbGUoaXRlbXMp\nCiAgICAgICAgbl92YWwgPSBtYXgoMSwgaW50KGxlbihpdGVtcykgKiBldmFsX3JhdGlvKSkKICAg\nICAgICB2YWxfc2V0LmV4dGVuZChpdGVtc1s6bl92YWxdKQogICAgICAgIHRyYWluX3NldC5leHRl\nbmQoaXRlbXNbbl92YWw6XSkKCiAgICBybmcuc2h1ZmZsZSh0cmFpbl9zZXQpCiAgICBybmcuc2h1\nZmZsZSh2YWxfc2V0KQogICAgcHJpbnQoZiJTcGxpdDogdHJhaW49e2xlbih0cmFpbl9zZXQpfSwg\ndmFsPXtsZW4odmFsX3NldCl9IikKICAgIHJldHVybiB0cmFpbl9zZXQsIHZhbF9zZXQKCgpjbGFz\ncyBSb3V0ZXJEYXRhc2V0KERhdGFzZXQpOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIHNhbXBsZXM6\nIExpc3RbRGljdF0sIHRva2VuaXplciwgbWF4X2xlbmd0aDogaW50KToKICAgICAgICBzZWxmLnNh\nbXBsZXMgPSBzYW1wbGVzCiAgICAgICAgc2VsZi50b2tlbml6ZXIgPSB0b2tlbml6ZXIKICAgICAg\nICBzZWxmLm1heF9sZW5ndGggPSBtYXhfbGVuZ3RoCgogICAgZGVmIF9fbGVuX18oc2VsZik6CiAg\nICAgICAgcmV0dXJuIGxlbihzZWxmLnNhbXBsZXMpCgogICAgZGVmIF9fZ2V0aXRlbV9fKHNlbGYs\nIGlkeCk6CiAgICAgICAgcyA9IHNlbGYuc2FtcGxlc1tpZHhdCiAgICAgICAgcHJvbXB0ID0gYnVp\nbGRfcHJvbXB0KHNbIm9ic2VydmF0aW9uIl0sIHNbImFjdGlvbl9oaXN0b3J5Il0pCiAgICAgICAg\nZW5jb2RpbmcgPSBzZWxmLnRva2VuaXplcigKICAgICAgICAgICAgcHJvbXB0LAogICAgICAgICAg\nICB0cnVuY2F0aW9uPVRydWUsCiAgICAgICAgICAgIG1heF9sZW5ndGg9c2VsZi5tYXhfbGVuZ3Ro\nLAogICAgICAgICAgICBwYWRkaW5nPSJtYXhfbGVuZ3RoIiwKICAgICAgICAgICAgcmV0dXJuX3Rl\nbnNvcnM9InB0IiwKICAgICAgICApCiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgImlucHV0\nX2lkcyI6IGVuY29kaW5nWyJpbnB1dF9pZHMiXS5zcXVlZXplKDApLAogICAgICAgICAgICAiYXR0\nZW50aW9uX21hc2siOiBlbmNvZGluZ1siYXR0ZW50aW9uX21hc2siXS5zcXVlZXplKDApLAogICAg\nICAgICAgICAibGFiZWxzIjogdG9yY2gudGVuc29yKHNbImxhYmVsX2lkIl0sIGR0eXBlPXRvcmNo\nLmxvbmcpLAogICAgICAgIH0KCgojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQojIENsYXNzIHdlaWdodGlu\nZwojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIGNvbXB1dGVfY2xhc3Nfd2VpZ2h0cyh0cmFpbl9z\nYW1wbGVzOiBMaXN0W0RpY3RdLCBtb2RlOiBzdHIgPSAiYXV0byIpIC0+IHRvcmNoLlRlbnNvcjoK\nICAgICMgImF1dG8iOiB3ZWlnaHRfYyA9IE5fdG90YWwgLyAobnVtX2NsYXNzZXMgKiBOX2MpLCBp\nLmUuIGludmVyc2UgZnJlcXVlbmN5IOKAlAogICAgIyAgICAgICAgIHJhcmVyIGNsYXNzIGdldHMg\ncHJvcG9ydGlvbmFsbHkgaGlnaGVyIHdlaWdodC4KICAgICMgIncwLHcxIjogbWFudWFsIHdlaWdo\ndHMsIGUuZy4gIjEuMCw1LjAiIC0+IGludGVybmFsPTEuMCwgZGV0ZXJtaW5pc3RpYz01LjAKICAg\nIG51bV9jbGFzc2VzID0gbGVuKExBQkVMMklEKQogICAgaWYgbW9kZSA9PSAiYXV0byI6CiAgMDg0\nODQwYTEzZmM4CiAgICAgICAgY291bnRzID0gQ291bnRlcihzWyJsYWJlbF9pZCJdIGZvciBzIGlu\nIHRyYWluX3NhbXBsZXMpCiAgICAgICAgdG90YWwgPSBsZW4odHJhaW5fc2FtcGxlcykKICAgICAg\nICB3ZWlnaHRzID0gdG9yY2gudGVuc29yKAogICAgICAgICAgICBbdG90YWwgLyAobnVtX2NsYXNz\nZXMgKiBtYXgoY291bnRzLmdldChpLCAxKSwgMSkpIGZvciBpIGluIHJhbmdlKG51bV9jbGFzc2Vz\nKV0sCiAgICAgICAgICAgIGR0eXBlPXRvcmNoLmZsb2F0MzIsCiAgICAgICAgKQogICAgZWxzZToK\nICAgICAgICBwYXJ0cyA9IFtmbG9hdCh4LnN0cmlwKCkpIGZvciB4IGluIG1vZGUuc3BsaXQoIiwi\nKV0KICAgICAgICBpZiBsZW4ocGFydHMpICE9IG51bV9jbGFzc2VzOgogICAgICAgICAgICByYWlz\nZSBWYWx1ZUVycm9yKGYiRXhwZWN0ZWQge251bV9jbGFzc2VzfSB3ZWlnaHRzLCBnb3Qge2xlbihw\nYXJ0cyl9OiB7bW9kZX0iKQogICAgICAgIHdlaWdodHMgPSB0b3JjaC50ZW5zb3IocGFydHMsIGR0\neXBlPXRvcmNoLmZsb2F0MzIpCiAgICByZXR1cm4gd2VpZ2h0cwoKCmNsYXNzIFdlaWdodGVkQ0VU\ncmFpbmVyKFRyYWluZXIpOgogICAgIiIiVHJhaW5lciB3aXRoIGNsYXNzLXdlaWdodGVkIENyb3Nz\nRW50cm9weUxvc3MgYW5kIG9wdGlvbmFsIFdlaWdodGVkUmFuZG9tU2FtcGxlci4iIiIKCiAgICBk\nZWYgX19pbml0X18oc2VsZiwgY2xhc3Nfd2VpZ2h0czogT3B0aW9uYWxbdG9yY2guVGVuc29yXSA9\nIE5vbmUsCiAgICAgICAgICAgICAgICAgd2VpZ2h0ZWRfc2FtcGxlcjogT3B0aW9uYWxbV2VpZ2h0\nZWRSYW5kb21TYW1wbGVyXSA9IE5vbmUsICoqa3dhcmdzKToKICAgICAgICBzdXBlcigpLl9faW5p\ndF9fKCoqa3dhcmdzKQogICAgICAgIHNlbGYuX2NsYXNzX3dlaWdodHMgPSBjbGFzc193ZWlnaHRz\nCiAgICAgICAgc2VsZi5fd2VpZ2h0ZWRfc2FtcGxlciA9IHdlaWdodGVkX3NhbXBsZXIKCiAgICBk\nZWYgY29tcHV0ZV9sb3NzKHNlbGYsIG1vZGVsLCBpbnB1dHMsIHJldHVybl9vdXRwdXRzPUZhbHNl\nLCAqKmt3YXJncyk6CiAgICAgICAgbGFiZWxzID0gaW5wdXRzLnBvcCgibGFiZWxzIikKICAgICAg\nICBvdXRwdXRzID0gbW9kZWwoKippbnB1dHMpCiAgICAgICAgbG9naXRzID0gb3V0cHV0cy5sb2dp\ndHMKICAgICAgICBpZiBzZWxmLl9jbGFzc193ZWlnaHRzIGlzIG5vdCBOb25lOgogICAgICAgICAg\nICBsb3NzX2ZuID0gdG9yY2gubm4uQ3Jvc3NFbnRyb3B5TG9zcyh3ZWlnaHQ9c2VsZi5fY2xhc3Nf\nd2VpZ2h0cy50byhsb2dpdHMuZGV2aWNlKSkKICAgICAgICBlbHNlOgogICAgICAgICAgICBsb3Nz\nX2ZuID0gdG9yY2gubm4uQ3Jvc3NFbnRyb3B5TG9zcygpCiAgICAgICAgbG9zcyA9IGxvc3NfZm4o\nbG9naXRzLCBsYWJlbHMpCiAgICAgICAgcmV0dXJuIChsb3NzLCBvdXRwdXRzKSBpZiByZXR1cm5f\nb3V0cHV0cyBlbHNlIGxvc3MKCiAgICBkZWYgZ2V0X3RyYWluX2RhdGFsb2FkZXIoc2VsZikgLT4g\nRGF0YUxvYWRlcjoKICAgICAgICBpZiBzZWxmLl93ZWlnaHRlZF9zYW1wbGVyIGlzIE5vbmU6CiAg\nICAgICAgICAgIHJldHVybiBzdXBlcigpLmdldF90cmFpbl9kYXRhbG9hZGVyKCkKICAgICAgICBy\nZXR1cm4gRGF0YUxvYWRlcigKICAgICAgICAgICAgc2VsZi50cmFpbl9kYXRhc2V0LAogICAgICAg\nICAgICBiYXRjaF9zaXplPXNlbGYuYXJncy5wZXJfZGV2aWNlX3RyYWluX2JhdGNoX3NpemUsCiAg\nICAgICAgICAgIHNhbXBsZXI9c2VsZi5fd2VpZ2h0ZWRfc2FtcGxlciwKICAgICAgICAgICAgbnVt\nX3dvcmtlcnM9c2VsZi5hcmdzLmRhdGFsb2FkZXJfbnVtX3dvcmtlcnMsCiAgICAgICAgICAgIHBp\nbl9tZW1vcnk9c2VsZi5hcmdzLmRhdGFsb2FkZXJfcGluX21lbW9yeSwKICAgICAgICApCgoKIyAt\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0KIyBNb2RlbCBzZXR1cAojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVm\nIHNldHVwX21vZGVsKG1vZGVsX25hbWU6IHN0ciwgYXJncyk6CiAgICB0b2tlbml6ZXIgPSBBdXRv\nVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lLCB0cnVzdF9yZW1vdGVfY29kZT1U\ncnVlKQogICAgaWYgdG9rZW5pemVyLnBhZF90b2tlbiBpcyBOb25lOgogICAgICAgIHRva2VuaXpl\nci5wYWRfdG9rZW4gPSB0b2tlbml6ZXIuZW9zX3Rva2VuCgogICAgbW9kZWwgPSBBdXRvTW9kZWxG\nb3JTZXF1ZW5jZUNsYXNzaWZpY2F0aW9uLmZyb21fcHJldHJhaW5lZCgKICAgICAgICBtb2RlbF9u\nYW1lLAogICAgICAgIG51bV9sYWJlbHM9MiwKICAgICAgICBpZDJsYWJlbD1JRDJMQUJFTCwKICAg\nICAgICBsYWJlbDJpZD1MQUJFTDJJRCwKICAgICAgICB0cnVzdF9yZW1vdGVfY29kZT1UcnVlLAog\nICAgICAgIHRvcmNoX2R0eXBlPXRvcmNoLmJmbG9hdDE2LAogICAgKQogICAgbW9kZWwuY29uZmln\nLnBhZF90b2tlbl9pZCA9IHRva2VuaXplci5wYWRfdG9rZW5faWQKCiAgICBsb3JhX2NvbmZpZyA9\nIExvcmFDb25maWcoCiAgICAgICAgcj1hcmdzLmxvcmFfciwKICAgICAgICBsb3JhX2FscGhhPWFy\nZ3MubG9yYV9hbHBoYSwKICAgICAgICB0YXJnZXRfbW9kdWxlcz1bInFfcHJvaiIsICJ2X3Byb2oi\nLCAia19wcm9qIiwgIm9fcHJvaiJdLAogICAgICAgIGxvcmFfZHJvcG91dD1hcmdzLmxvcmFfZHJv\ncG91dCwKICAgICAgICB0YXNrX3R5cGU9VGFza1R5cGUuU0VRX0NMUywKICAgICAgICBtb2R1bGVz\nX3RvX3NhdmU9WyJzY29yZSJdLAogICAgKQogICAgbW9kZWwgPSBnZXRfcGVmdF9tb2RlbChtb2Rl\nbCwgbG9yYV9jb25maWcpCiAgICBtb2RlbC5wcmludF90cmFpbmFibGVfcGFyYW1ldGVycygpCiAg\nICByZXR1cm4gbW9kZWwsIHRva2VuaXplcgoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgTWV0cmlj\ncwojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIGNvbXB1dGVfbWV0cmljcyhldmFsX3ByZWQpOgog\nICAgbG9naXRzLCBsYWJlbHMgPSBldmFsX3ByZWQKICAgIHByZWRzID0gbnAuYXJnbWF4KGxvZ2l0\ncywgYXhpcz0tMSkKICAgIGFjYyA9IGFjY3VyYWN5X3Njb3JlKGxhYmVscywgcHJlZHMpCiAgICBw\ncmVjLCByZWMsIGYxLCBfID0gcHJlY2lzaW9uX3JlY2FsbF9mc2NvcmVfc3VwcG9ydChsYWJlbHMs\nIHByZWRzLCBhdmVyYWdlPU5vbmUsIGxhYmVscz1bMCwgMV0pCiAgICByZXR1cm4gewogICAgICAg\nICJhY2N1cmFjeSI6IGFjYywKICAgICAgICAicHJlY2lzaW9uX2ludGVybmFsIjogcHJlY1swXSwK\nICAgICAgICAicmVjYWxsX2ludGVybmFsIjogcmVjWzBdLAogICAgICAgICJmMV9pbnRlcm5hbCI6\nIGYxWzBdLAogICAgICAgICJwcmVjaXNpb25fZGV0ZXJtaW5pc3RpYyI6IHByZWNbMV0sCiAgICAg\nICAgInJlY2FsbF9kZXRlcm1pbmlzdGljIjogcmVjWzFdLAogICAgICAgICJmMV9kZXRlcm1pbmlz\ndGljIjogZjFbMV0sCiAgICB9CgoKZGVmIHBlcl90YXNrX2V2YWx1YXRpb24odHJhaW5lciwgdmFs\nX2RhdGFzZXQsIHZhbF9zYW1wbGVzKSAtPiBEaWN0W3N0ciwgQW55XToKICAgICIiIkNvbXB1dGUg\ncGVyLXRhc2sgYWNjdXJhY3kgYW5kIGNvbmZ1c2lvbiBtYXRyaXguIiIiCiAgICBwcmVkaWN0aW9u\ncyA9IHRyYWluZXIucHJlZGljdCh2YWxfZGF0YXNldCkKICAgIHByZWRzID0gbnAuYXJnbWF4KHBy\nZWRpY3Rpb25zLnByZWRpY3Rpb25zLCBheGlzPS0xKQogICAgbGFiZWxzID0gcHJlZGljdGlvbnMu\nbGFiZWxfaWRzCgogICAgY20gPSBjb25mdXNpb25fbWF0cml4KGxhYmVscywgcHJlZHMsIGxhYmVs\ncz1bMCwgMV0pLnRvbGlzdCgpCgogICAgdGFza19tZXRyaWNzID0ge30KICAgIGJ5X3Rhc2s6IERp\nY3Rbc3RyLCBEaWN0W3N0ciwgbGlzdF1dID0ge30KICAgIGZvciBpLCBzIGluIGVudW1lcmF0ZSh2\nYWxfc2FtcGxlcyk6CiAgICAgICAgdCA9IHNbInRhc2tfdHlwZSJdCiAgICAgICAgaWYgdCBub3Qg\naW4gYnlfdGFzazoKICAgICAgICAgICAgYnlfdGFza1t0XSA9IHsicHJlZHMiOiBbXSwgImxhYmVs\ncyI6IFtdfQogICAgICAgIGJ5X3Rhc2tbdF1bInByZWRzIl0uYXBwZW5kKHByZWRzW2ldKQogICAg\nICAgIGJ5X3Rhc2tbdF1bImxhYmVscyJdLmFwcGVuZChsYWJlbHNbaV0pCgogICAgZm9yIHRhc2ss\nIGRhdGEgaW4gc29ydGVkKGJ5X3Rhc2suaXRlbXMoKSk6CiAgICAgICAgYWNjID0gYWNjdXJhY3lf\nc2NvcmUoZGF0YVsibGFiZWxzIl0sIGRhdGFbInByZWRzIl0pCiAgICAgICAgbiA9IGxlbihkYXRh\nWyJsYWJlbHMiXSkKICAgICAgICB0YXNrX21ldHJpY3NbdGFza10gPSB7ImFjY3VyYWN5IjogYWNj\nLCAibl9zYW1wbGVzIjogbn0KCiAgICByZXR1cm4gewogICAgICAgICJvdmVyYWxsX2FjY3VyYWN5\nIjogYWNjdXJhY3lfc2NvcmUobGFiZWxzLCBwcmVkcyksCiAgICAgICAgImNvbmZ1c2lvbl9tYXRy\naXgiOiBjbSwKICAgICAgICAiY29uZnVzaW9uX2xhYmVscyI6IFsiaW50ZXJuYWwiLCAiZGV0ZXJt\naW5pc3RpYyJdLAogICAgICAgICJwZXJfdGFzayI6IHRhc2tfbWV0cmljcywKICAgIH0KCgojIC0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLQojIE1haW4KIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmRlZiBtYWluKCk6\nCiAgICBhcmdzID0gcGFyc2VfYXJncygpCgogICAgaWYgYXJncy5kcnlfcnVuOgogICAgICAgIHBy\naW50KCJEcnkgcnVuOiBpbXBvcnRzIE9LLCBhcmdzIHBhcnNlZCBzdWNjZXNzZnVsbHkuIikKICAg\nICAgICBwcmludChmIiAgbW9kZWxfbmFtZTogICAgICAgICAgICB7YXJncy5tb2RlbF9uYW1lfSIp\nCiAgICAgICAgcHJpbnQoZiIgIGRhdGFfZGlyOiAgICAgICAgICAgICAge2FyZ3MuZGF0YV9kaXJ9\nIikKICAgICAgICBwcmludChmIiAgb3V0cHV0X2RpcjogICAgICAgICAgICB7YXJncy5vdXRwdXRf\nZGlyfSIpCiAgICAgICAgcHJpbnQoZiIgIGNsYXNzX3dlaWdodHM6ICAgICAgICAge2FyZ3MuY2xh\nc3Nfd2VpZ2h0c30iKQogICAgICAgIHByaW50KGYiICBtaW5faW50ZXJuYWxfc2FtcGxlczogIHth\ncmdzLm1pbl9pbnRlcm5hbF9zYW1wbGVzfSIpCiAgICAgICAgcHJpbnQoZiIgIHVwc2FtcGxlX21p\nbm9yaXR5OiAgICAge2FyZ3MudXBzYW1wbGVfbWlub3JpdHl9IikKICAgICAgICByZXR1cm4KCiAg\nICBvcy5lbnZpcm9uWyJDVURBX1ZJU0lCTEVfREVWSUNFUyJdID0gc3RyKGFyZ3MuZ3B1X2lkKQog\nICAgcmFuZG9tLnNlZWQoYXJncy5zZWVkKQogICAgbnAucmFuZG9tLnNlZWQoYXJncy5zZWVkKQog\nICAgdG9yY2gubWFudWFsX3NlZWQoYXJncy5zZWVkKQoKICAgIG9zLm1ha2VkaXJzKGFyZ3Mub3V0\ncHV0X2RpciwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBzYW1wbGVzID0gbG9hZF9sYWJlbGVkX2RhdGEo\nYXJncy5kYXRhX2RpcikKICAgIHRyYWluX3NhbXBsZXMsIHZhbF9zYW1wbGVzID0gc3RyYXRpZmll\nZF9zcGxpdChzYW1wbGVzLCBhcmdzLmV2YWxfc3BsaXQsIGFyZ3Muc2VlZCkKCiAgICAjIC0tLSBD\naGVjayBtaW5vcml0eSBjbGFzcyBzYW1wbGUgY291bnQgLS0tCiAgICB0cmFpbl9sYWJlbF9jb3Vu\ndHMgPSBDb3VudGVyKHNbImxhYmVsIl0gZm9yIHMgaW4gdHJhaW5fc2FtcGxlcykKICAgIG5faW50\nZXJuYWwgPSB0cmFpbl9sYWJlbF9jb3VudHMuZ2V0KCJpbnRlcm5hbCIsIDApCiAgICBpZiBuX2lu\ndGVybmFsIDwgYXJncy5taW5faW50ZXJuYWxfc2FtcGxlczoKICAgICAgICB3YXJuaW5ncy53YXJu\nKAogICAgICAgICAgICBmIk9ubHkge25faW50ZXJuYWx9IGludGVybmFsIHNhbXBsZXMgaW4gdHJh\naW5pbmcgc2V0ICIKICAgICAgICAgICAgZiIodGhyZXNob2xkOiB7YXJncy5taW5faW50ZXJuYWxf\nc2FtcGxlc30pLiAiCiAgICAgICAgICAgIGYiQ29uc2lkZXIgY29sbGVjdGluZyBtb3JlIGRhdGEg\nb3IgdXNpbmcgLS1jbGFzc193ZWlnaHRzIGF1dG8uIiwKICAgICAgICAgICAgc3RhY2tsZXZlbD0x\nLAogICAgICAgICkKCiAgICAjIC0tLSBDb21wdXRlIGNsYXNzIHdlaWdodHMgKGludmVyc2UgZnJl\ncXVlbmN5IG9yIG1hbnVhbCkgLS0tCiAgICBjbGFzc193ZWlnaHRzID0gTm9uZQogICAgaWYgYXJn\ncy5jbGFzc193ZWlnaHRzIGlzIG5vdCBOb25lOgogICAgICAgIGNsYXNzX3dlaWdodHMgPSBjb21w\ndXRlX2NsYXNzX3dlaWdodHModHJhaW5fc2FtcGxlcywgYXJncy5jbGFzc193ZWlnaHRzKQogICAg\nICAgIHdlaWdodF9kaWN0ID0ge2xhYmVsOiBjbGFzc193ZWlnaHRzW2xpZF0uaXRlbSgpIGZvciBs\nYWJlbCwgbGlkIGluIExBQkVMMklELml0ZW1zKCl9CiAgICAgICAgcHJpbnQoZiJDbGFzcyB3ZWln\naHRzOiB7d2VpZ2h0X2RpY3R9IikKICAgICAgICBwcmludChmIkVmZmVjdGl2ZSBzYW1wbGUgY291\nbnRzOiB7ZGljdCh0cmFpbl9sYWJlbF9jb3VudHMpfSIpCgogICAgbW9kZWwsIHRva2VuaXplciA9\nIHNldHVwX21vZGVsKGFyZ3MubW9kZWxfbmFtZSwgYXJncykKCiAgICB0cmFpbl9kYXRhc2V0ID0g\nUm91dGVyRGF0YXNldCh0cmFpbl9zYW1wbGVzLCB0b2tlbml6ZXIsIGFyZ3MubWF4X3NlcV9sZW4p\nCiAgICB2YWxfZGF0YXNldCA9IFJvdXRlckRhdGFzZXQodmFsX3NhbXBsZXMsIHRva2VuaXplciwg\nYXJncy5tYXhfc2VxX2xlbikKCiAgICAjIC0tLSBCdWlsZCBXZWlnaHRlZFJhbmRvbVNhbXBsZXIg\nZm9yIG1pbm9yaXR5IG92ZXJzYW1wbGluZyAtLS0KICAgICMgUGVyLXNhbXBsZSB3ZWlnaHQgPSAx\nIC8gY291bnRfb2ZfaXRzX2NsYXNzLCBzbyBtaW5vcml0eSBzYW1wbGVzIGFyZSBkcmF3biBtb3Jl\nIG9mdGVuLgogICAgd2VpZ2h0ZWRfc2FtcGxlciA9IE5vbmUKICAgIGlmIGFyZ3MudXBzYW1wbGVf\nbWlub3JpdHk6CiAgICAgICAgc2FtcGxlX3dlaWdodHMgPSBbMS4wIC8gdHJhaW5fbGFiZWxfY291\nbnRzW3NbImxhYmVsIl1dIGZvciBzIGluIHRyYWluX3NhbXBsZXNdCiAgICAgICAgd2VpZ2h0ZWRf\nc2FtcGxlciA9IFdlaWdodGVkUmFuZG9tU2FtcGxlcigKICAgICAgICAgICAgd2VpZ2h0cz1zYW1w\nbGVfd2VpZ2h0cywKICAgICAgICAgICAgbnVtX3NhbXBsZXM9bGVuKHRyYWluX3NhbXBsZXMpLAog\nICAgICAgICAgICByZXBsYWNlbWVudD1UcnVlLAogICAgICAgICkKICAgICAgICBwcmludChmIlVw\nc2FtcGxpbmcgZW5hYmxlZDogV2VpZ2h0ZWRSYW5kb21TYW1wbGVyIHdpdGgge2xlbih0cmFpbl9z\nYW1wbGVzKX0gZHJhd3MvZXBvY2giKQoKICAgIHVzZV9iZjE2ID0gdG9yY2guY3VkYS5pc19hdmFp\nbGFibGUoKSBhbmQgdG9yY2guY3VkYS5nZXRfZGV2aWNlX2NhcGFiaWxpdHkoKVswXSA+PSA4CiAg\nICB0cmFpbmluZ19hcmdzID0gVHJhaW5pbmdBcmd1bWVudHMoCiAgICAgICAgb3V0cHV0X2Rpcj1h\ncmdzLm91dHB1dF9kaXIsCiAgICAgICAgbnVtX3RyYWluX2Vwb2Nocz1hcmdzLmVwb2NocywKICAg\nICAgICBwZXJfZGV2aWNlX3RyYWluX2JhdGNoX3NpemU9YXJncy5iYXRjaF9zaXplLAogICAgICAg\nIHBlcl9kZXZpY2VfZXZhbF9iYXRjaF9zaXplPWFyZ3MuZXZhbF9iYXRjaF9zaXplLAogICAgICAg\nIGxlYXJuaW5nX3JhdGU9YXJncy5sciwKICAgICAgICB3ZWlnaHRfZGVjYXk9YXJncy53ZWlnaHRf\nZGVjYXksCiAgICAgICAgd2FybXVwX3JhdGlvPWFyZ3Mud2FybXVwX3JhdGlvLAogICAgICAgIGV2\nYWxfc3RyYXRlZ3k9ImVwb2NoIiwKICAgICAgICBzYXZlX3N0cmF0ZWd5PSJlcG9jaCIsCiAgICAg\nICAgbG9hZF9iZXN0X21vZGVsX2F0X2VuZD1UcnVlLAogICAgICAgIG1ldHJpY19mb3JfYmVzdF9t\nb2RlbD0iYWNjdXJhY3kiLAogICAgICAgIGdyZWF0ZXJfaXNfYmV0dGVyPVRydWUsCiAgICAgICAg\nYmYxNj11c2VfYmYxNiwKICAgICAgICBmcDE2PShub3QgdXNlX2JmMTYgYW5kIHRvcmNoLmN1ZGEu\naXNfYXZhaWxhYmxlKCkpLAogICAgICAgIGxvZ2dpbmdfc3RlcHM9MTAsCiAgICAgICAgZGF0YWxv\nYWRlcl9udW1fd29ya2Vycz00LAogICAgICAgIHJlcG9ydF90bz0id2FuZGIiLAogICAgICAgIHJ1\nbl9uYW1lPWYicm91dGVyLXNmdC17b3MucGF0aC5iYXNlbmFtZShhcmdzLm1vZGVsX25hbWUpfS1y\ne2FyZ3MubG9yYV9yfSIsCiAgICAgICAgc2VlZD1hcmdzLnNlZWQsCiAgICAgICAgc2F2ZV90b3Rh\nbF9saW1pdD0yLAogICAgKQoKICAgIG9zLmVudmlyb25bIldBTkRCX1BST0pFQ1QiXSA9IGFyZ3Mu\nd2FuZGJfcHJvamVjdAoKICAgICMgLS0tIExvZyBjbGFzcyB3ZWlnaHRpbmcgY29uZmlnIHRvIFcm\nQiAtLS0KICAgIHRyeToKICAgICAgICBpbXBvcnQgd2FuZGIKICAgICAgICB3YW5kYl9jb25maWcg\nPSB2YXJzKGFyZ3MpLmNvcHkoKQogICAgICAgIGlmIGNsYXNzX3dlaWdodHMgaXMgbm90IE5vbmU6\nCiAgICAgICAgICAgIHdhbmRiX2NvbmZpZ1siY2xhc3Nfd2VpZ2h0c192YWx1ZXMiXSA9IHsKICAg\nICAgICAgICAgICAgIGxhYmVsOiBjbGFzc193ZWlnaHRzW2xpZF0uaXRlbSgpIGZvciBsYWJlbCwg\nbGlkIGluIExBQkVMMklELml0ZW1zKCkKICAgICAgICAgICAgfQogICAgICAgIHdhbmRiX2NvbmZp\nZ1sidHJhaW5fbGFiZWxfY291bnRzIl0gPSBkaWN0KHRyYWluX2xhYmVsX2NvdW50cykKICAgICAg\nICB3YW5kYl9jb25maWdbInVwc2FtcGxlX21pbm9yaXR5Il0gPSBhcmdzLnVwc2FtcGxlX21pbm9y\naXR5CiAgICAgICAgd2FuZGIuaW5pdCgKICAgICAgICAgICAgcHJvamVjdD1hcmdzLndhbmRiX3By\nb2plY3QsCiAgICAgICAgICAgIG5hbWU9dHJhaW5pbmdfYXJncy5ydW5fbmFtZSwKICAgICAgICAg\nICAgY29uZmlnPXdhbmRiX2NvbmZpZywKICAgICAgICApCiAgICBleGNlcHQgRXhjZXB0aW9uOgog\nICAgICAgIHBhc3MKCiAgICB0cmFpbmVyID0gV2VpZ2h0ZWRDRVRyYWluZXIoCiAgICAgICAgY2xh\nc3Nfd2VpZ2h0cz1jbGFzc193ZWlnaHRzLAogICAgICAgIHdlaWdodGVkX3NhbXBsZXI9d2VpZ2h0\nZWRfc2FtcGxlciwKICAgICAgICBtb2RlbD1tb2RlbCwKICAgICAgICBhcmdzPXRyYWluaW5nX2Fy\nZ3MsCiAgICAgICAgdHJhaW5fZGF0YXNldD10cmFpbl9kYXRhc2V0LAogICAgICAgIGV2YWxfZGF0\nYXNldD12YWxfZGF0YXNldCwKICAgICAgICBjb21wdXRlX21ldHJpY3M9Y29tcHV0ZV9tZXRyaWNz\nLAogICAgICAgIGNhbGxiYWNrcz1bRWFybHlTdG9wcGluZ0NhbGxiYWNrKGVhcmx5X3N0b3BwaW5n\nX3BhdGllbmNlPWFyZ3MuZWFybHlfc3RvcHBpbmdfcGF0aWVuY2UpXSwKICAgICkKCiAgICBwcmlu\ndChmIlxueyc9Jyo2MH0iKQogICAgcHJpbnQoZiJTdGFydGluZyB0cmFpbmluZzoge2xlbih0cmFp\nbl9kYXRhc2V0KX0gdHJhaW4gLyB7bGVuKHZhbF9kYXRhc2V0KX0gdmFsIHNhbXBsZXMiKQog\nICAgcHJpbnQoZiJNb2RlbDoge2FyZ3MubW9kZWxfbmFtZX0sIExvUkEgcj17YXJncy5sb3JhX3J9\nLCBscj17YXJncy5scn0iKQogICAgaWYgY2xhc3Nfd2VpZ2h0cyBpcyBub3QgTm9uZToKICAgICAg\nICBwcmludChmIkNsYXNzIHdlaWdodHM6IHtjbGFzc193ZWlnaHRzLnRvbGlzdCgpfSIpCiAgICBp\nZiBhcmdzLnVwc2FtcGxlX21pbm9yaXR5OgogICAgICAgIHByaW50KCJNaW5vcml0eSBvdmVyc2Ft\ncGxpbmc6IGVuYWJsZWQiKQogICAgcHJpbnQoZiJ7Jz0nKjYwfVxuIikKCiAgICB0cmFpbmVyLnRy\nYWluKCkKCiAgICBhZGFwdGVyX2RpciA9IG9zLnBhdGguam9pbihhcmdzLm91dHB1dF9kaXIsICJm\naW5hbF9hZGFwdGVyIikKICAgIG1vZGVsLnNhdmVfcHJldHJhaW5lZChhZGFwdGVyX2RpcikKICAg\nIHRva2VuaXplci5zYXZlX3ByZXRyYWluZWQoYWRhcHRlcl9kaXIpCiAgICBwcmludChmIkFkYXB0\nZXIgc2F2ZWQgdG8ge2FkYXB0ZXJfZGlyfSIpCgogICAgcHJpbnQoIlxuLS0tIEV2YWx1YXRpb24g\nLS0tIikKICAgIGV2YWxfcmVwb3J0ID0gcGVyX3Rhc2tfZXZhbHVhdGlvbih0cmFpbmVyLCB2YWxf\nZGF0YXNldCwgdmFsX3NhbXBsZXMpCgogICAgcmVwb3J0X3BhdGggPSBvcy5wYXRoLmpvaW4oYXJn\ncy5vdXRwdXRfZGlyLCAiZXZhbF9yZXBvcnQuanNvbiIpCiAgICB3aXRoIG9wZW4ocmVwb3J0X3Bh\ndGgsICJ3IikgYXMgZjoKICAgICAgICBqc29uLmR1bXAoZXZhbF9yZXBvcnQsIGYsIGluZGVudD0y\nKQogICAgcHJpbnQoZiJFdmFsIHJlcG9ydCBzYXZlZCB0byB7cmVwb3J0X3BhdGh9IikKCiAgICBw\ncmludChmIlxuT3ZlcmFsbCBhY2N1cmFjeToge2V2YWxfcmVwb3J0WydvdmVyYWxsX2FjY3VyYWN5\nJ106LjRmfSIpCiAgICBwcmludChmIkNvbmZ1c2lvbiBtYXRyaXggKHJvd3M9dHJ1ZSwgY29scz1w\ncmVkKToiKQogICAgcHJpbnQoZiIgIHtldmFsX3JlcG9ydFsnY29uZnVzaW9uX2xhYmVscyddfSIp\nCiAgICBmb3Igcm93IGluIGV2YWxfcmVwb3J0WyJjb25mdXNpb25fbWF0cml4Il06CiAgICAgICAg\ncHJpbnQoZiIgIHtyb3d9IikKICAgIHByaW50KCJcblBlci10YXNrIGFjY3VyYWN5OiIpCiAgICBm\nb3IgdGFzaywgbSBpbiBzb3J0ZWQoZXZhbF9yZXBvcnRbInBlcl90YXNrIl0uaXRlbXMoKSk6CiAg\nICAgICAgcHJpbnQoZiIgIHt0YXNrfToge21bJ2FjY3VyYWN5J106LjNmfSAobj17bVsnbl9zYW1w\nbGVzJ119KSIpCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=\nB64EOF\necho \"WRITE_OK: $(wc -l < /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py) lines\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat << 'B64EOF' | base64 -d > /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py\nIyBSb3V0ZXIgU0ZUIHRyYWluaW5nIHNjcmlwdCBmb3IgU2ltR2F0ZSBtb2R1bGFyIHJvdXRpbmcu\nCiMgRmluZXR1bmVzIFF3ZW4zLTEuN0IgKG9yIGZhbGxiYWNrKSBvbiBlcGlzb2RlLWxldmVsIGxh\nYmVsZWQgZGF0YQojIGZyb20gUGxhbiBDIChsYWJlbGVkX3N0ZXBzLmpzb25sKSBmb3IgMi13YXkg\nY2xhc3NpZmljYXRpb246IGludGVybmFsIHZzIGRldGVybWluaXN0aWMuCiMKIyBEYXRhIGRlcGVu\nZGVuY3k6IHJlc3VsdHMvcGxhbl9jL3t0YXNrX3R5cGV9L2xhYmVsZWRfc3RlcHMuanNvbmwKIyBV\nc2FnZTogcHl0aG9uIHNyYy9yb3V0ZXJfc2Z0X3RyYWluLnB5IC0taGVscAoKaW1wb3J0IGFyZ3Bh\ncnNlCmltcG9ydCBqc29uCmltcG9ydCBvcwppbXBvcnQgZ2xvYgppbXBvcnQgcmFuZG9tCmltcG9y\ndCB3YXJuaW5ncwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gdHlwaW5nIGlt\ncG9ydCBMaXN0LCBEaWN0LCBBbnksIE9wdGlvbmFsLCBUdXBsZQoKaW1wb3J0IG51bXB5IGFzIG5w\nCmltcG9ydCB0b3JjaApmcm9tIHRvcmNoLnV0aWxzLmRhdGEgaW1wb3J0IERhdGFzZXQsIERhdGFM\nb2FkZXIsIFdlaWdodGVkUmFuZG9tU2FtcGxlcgpmcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQg\nYWNjdXJhY3lfc2NvcmUsIHByZWNpc2lvbl9yZWNhbGxfZnNjb3JlX3N1cHBvcnQsIGNvbmZ1c2lv\nbl9tYXRyaXgKZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0ICgKICAgIEF1dG9Ub2tlbml6ZXIsCiAg\nICBBdXRvTW9kZWxGb3JTZXF1ZW5jZUNsYXNzaWZpY2F0aW9uLAogICAgVHJhaW5pbmdBcmd1bWVu\ndHMsCiAgICBUcmFpbmVyLAogICAgRWFybHlTdG9wcGluZ0NhbGxiYWNrLAopCmZyb20gcGVmdCBp\nbXBvcnQgTG9yYUNvbmZpZywgZ2V0X3BlZnRfbW9kZWwsIFRhc2tUeXBlCgpMQUJFTDJJRCA9IHsi\naW50ZXJuYWwiOiAwLCAiZGV0ZXJtaW5pc3RpYyI6IDF9CklEMkxBQkVMID0gezA6ICJpbnRlcm5h\nbCIsIDE6ICJkZXRlcm1pbmlzdGljIn0KClNZU1RFTV9QUk9NUFQgPSAoCiAgICAiWW91IGFyZSBh\nIHJvdXRpbmcgY2xhc3NpZmllci4gR2l2ZW4gdGhlIGN1cnJlbnQgb2JzZXJ2YXRpb24gYW5kIGFj\ndGlvbiBoaXN0b3J5LCAiCiAgICAicHJlZGljdCB3aGljaCByZWFzb25pbmcgbW9kYWxpdHkgd2ls\nbCBsZWFkIHRvIGEgYmV0dGVyIG91dGNvbWUuIgopCgoKZGVmIHBhcnNlX2FyZ3MoKToKICAgIHAg\nPSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0iUm91dGVyIFNGVDogZmluZXR1\nbmUgTExNIGZvciAyLXdheSByb3V0aW5nIGNsYXNzaWZpY2F0aW9uIikKICAgIHAuYWRkX2FyZ3Vt\nZW50KCItLWRhdGFfZGlyIiwgdHlwZT1zdHIsIGRlZmF1bHQ9InJlc3VsdHMvcGxhbl9jLyIsCiAg\nICAgICAgICAgICAgICAgICAgaGVscD0iRGlyZWN0b3J5IGNvbnRhaW5pbmcge3Rhc2tfdHlwZX0v\nbGFiZWxlZF9zdGVwcy5qc29ubCIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1tb2RlbF9uYW1lIiwg\ndHlwZT1zdHIsIGRlZmF1bHQ9IlF3ZW4vUXdlbjMtMS43QiIsCiAgICAgICAgICAgICAgICAgICAg\naGVscD0iSHVnZ2luZ0ZhY2UgbW9kZWwgbmFtZSBvciBsb2NhbCBwYXRoIikKICAgIHAuYWRkX2Fy\nZ3VtZW50KCItLW91dHB1dF9kaXIiLCB0eXBlPXN0ciwgZGVmYXVsdD0icmVzdWx0cy9yb3V0ZXJf\nc2Z0LyIsCiAgICAgICAgICAgICAgICAgICAgaGVscD0iT3V0cHV0IGRpcmVjdG9yeSBmb3IgY2hl\nY2twb2ludHMgYW5kIHJlcG9ydHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tZXBvY2hzIiwgdHlw\nZT1pbnQsIGRlZmF1bHQ9MykKICAgIHAuYWRkX2FyZ3VtZW50KCItLWJhdGNoX3NpemUiLCB0eXBl\nPWludCwgZGVmYXVsdD0xNikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWV2YWxfYmF0Y2hfc2l6ZSIs\nIHR5cGU9aW50LCBkZWZhdWx0PTMyKQogICAgcC5hZGRfYXJndW1lbnQoIi0tbHIiLCB0eXBlPWZs\nb2F0LCBkZWZhdWx0PTJlLTQpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1sb3JhX3IiLCB0eXBlPWlu\ndCwgZGVmYXVsdD0xNikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWxvcmFfYWxwaGEiLCB0eXBlPWlu\ndCwgZGVmYXVsdD0zMikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWxvcmFfZHJvcG91dCIsIHR5cGU9\nZmxvYXQsIGRlZmF1bHQ9MC4wNSkKICAgIHAuYWRkX2FyZ3VtZW50KCItLW1heF9zZXFfbGVuIiwg\ndHlwZT1pbnQsIGRlZmF1bHQ9NTEyKQogICAgcC5hZGRfYXJndW1lbnQoIi0tZ3B1X2lkIiwgdHlw\nZT1pbnQsIGRlZmF1bHQ9MCkKICAgIHAuYWRkX2FyZ3VtZW50KCItLXdhbmRiX3Byb2plY3QiLCB0\neXBlPXN0ciwgZGVmYXVsdD0ic2ltZ2F0ZS1yb3V0ZXItc2Z0IikKICAgIHAuYWRkX2FyZ3VtZW50\nKCItLXNlZWQiLCB0eXBlPWludCwgZGVmYXVsdD00MikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWV2\nYWxfc3BsaXQiLCB0eXBlPWZsb2F0LCBkZWZhdWx0PTAuMikKICAgIHAuYWRkX2FyZ3VtZW50KCIt\nLXdhcm11cF9yYXRpbyIsIHR5cGU9ZmxvYXQsIGRlZmF1bHQ9MC4xKQogICAgcC5hZGRfYXJndW1l\nbnQoIi0td2VpZ2h0X2RlY2F5IiwgdHlwZT1mbG9hdCwgZGVmYXVsdD0wLjAxKQogICAgcC5hZGRf\nYXJndW1lbnQoIi0tZWFybHlfc3RvcHBpbmdfcGF0aWVuY2UiLCB0eXBlPWludCwgZGVmYXVsdD0y\nKQogICAgcC5hZGRfYXJndW1lbnQoIi0tZHJ5X3J1biIsIGFjdGlvbj0ic3RvcmVfdHJ1ZSIsIGhl\nbHA9Ik9ubHkgdmFsaWRhdGUgaW1wb3J0cyBhbmQgYXJncywgc2tpcCB0cmFpbmluZyIpCiAgICBw\nLmFkZF9hcmd1bWVudCgiLS1jbGFzc193ZWlnaHRzIiwgdHlwZT1zdHIsIGRlZmF1bHQ9Tm9uZSwK\nICAgICAgICAgICAgICAgICAgICBoZWxwPSciYXV0byIgZm9yIGludmVyc2UtZnJlcXVlbmN5IHdl\naWdodHMsIG9yICJ3MCx3MSIgKGludGVybmFsOncwLCBkZXQ6dzEpJykKICAgIHAuYWRkX2FyZ3Vt\nZW50KCItLW1pbl9pbnRlcm5hbF9zYW1wbGVzIiwgdHlwZT1pbnQsIGRlZmF1bHQ9MTAsCiAgICAg\nICAgICAgICAgICAgICAgaGVscD0iV2FybiBpZiBpbnRlcm5hbCBzYW1wbGVzIDwgdGhpcyB0aHJl\nc2hvbGQgKGRlZmF1bHQ6IDEwKSIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS11cHNhbXBsZV9taW5v\ncml0eSIsIGFjdGlvbj0ic3RvcmVfdHJ1ZSIsCiAgICAgICAgICAgICAgICAgICAgaGVscD0iVXNl\nIFdlaWdodGVkUmFuZG9tU2FtcGxlciB0byBvdmVyc2FtcGxlIG1pbm9yaXR5IGNsYXNzIikKICAg\nIHJldHVybiBwLnBhcnNlX2FyZ3MoKQoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgRGF0YSBsb2Fk\naW5nCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpkZWYgc3VtbWFyaXplX2FjdGlvbl9oaXN0b3J5KGFj\ndGlvbl9oaXN0b3J5OiBMaXN0W3N0cl0sIG1heF9hY3Rpb25zOiBpbnQgPSA1KSAtPiBzdHI6CiAg\nICAiIiJLZWVwIHRoZSBtb3N0IHJlY2VudCBOIGFjdGlvbnMgYXMgYSBzdW1tYXJ5LiIiIgogICAg\ncmVjZW50ID0gYWN0aW9uX2hpc3RvcnlbLW1heF9hY3Rpb25zOl0gaWYgYWN0aW9uX2hpc3Rvcnkg\nZWxzZSBbXQogICAgaWYgbm90IHJlY2VudDoKICAgICAgICByZXR1cm4gIihub25lKSIKICAgIHJl\ndHVybiAiIOKGkiAiLmpvaW4ocmVjZW50KQoKCmRlZiBidWlsZF9wcm9tcHQob2JzZXJ2YXRpb246\nIHN0ciwgYWN0aW9uX2hpc3Rvcnk6IExpc3Rbc3RyXSkgLT4gc3RyOgogICAgaGlzdG9yeV9zdW1t\nYXJ5ID0gc3VtbWFyaXplX2FjdGlvbl9oaXN0b3J5KGFjdGlvbl9oaXN0b3J5KQogICAgcmV0dXJu\nICgKICAgICAgICBmIjx8c3lzdGVtfD57U1lTVEVNX1BST01QVH08fGVuZHw+XG4iCiAgICAgICAg\nZiI8fHVzZXJ8PlxuIgogICAgICAgIGYiT2JzZXJ2YXRpb246IHtvYnNlcnZhdGlvbn1cbiIKICAg\nICAgICBmIkFjdGlvbiBoaXN0b3J5OiB7aGlzdG9yeV9zdW1tYXJ5fVxuIgogICAgICAgIGYiPHxl\nbmR8PiIKICAgICkKCgpkZWYgbG9hZF9sYWJlbGVkX2RhdGEoZGF0YV9kaXI6IHN0cikgLT4gTGlz\ndFtEaWN0W3N0ciwgQW55XV06CiAgICAiIiJMb2FkIGFsbCBsYWJlbGVkX3N0ZXBzLmpzb25sIGZp\nbGVzLCBmaWx0ZXJpbmcgb3V0IHRpZXMuIiIiCiAgICBwYXR0ZXJuID0gb3MucGF0aC5qb2luKGRh\ndGFfZGlyLCAiKiIsICJsYWJlbGVkX3N0ZXBzLmpzb25sIikKICAgIGZpbGVzID0gc29ydGVkKGds\nb2IuZ2xvYihwYXR0ZXJuKSkKICAgIGlmIG5vdCBmaWxlczoKICAgICAgICBwYXR0ZXJuX2ZsYXQg\nPSBvcy5wYXRoLmpvaW4oZGF0YV9kaXIsICJsYWJlbGVkX3N0ZXBzLmpzb25sIikKICAgICAgICBp\nZiBvcy5wYXRoLmV4aXN0cyhwYXR0ZXJuX2ZsYXQpOgogICAgICAgICAgICBmaWxlcyA9IFtwYXR0\nZXJuX2ZsYXRdCiAgICBpZiBub3QgZmlsZXM6CiAgICAgICAgcmFpc2UgRmlsZU5vdEZvdW5kRXJy\nb3IoZiJObyBsYWJlbGVkX3N0ZXBzLmpzb25sIGZvdW5kIGluIHtkYXRhX2Rpcn0iKQoKICAgIHNh\nbXBsZXMgPSBbXQogICAgZm9yIGZwYXRoIGluIGZpbGVzOgogICAgICAgIHRhc2tfdHlwZSA9IG9z\nLnBhdGguYmFzZW5hbWUob3MucGF0aC5kaXJuYW1lKGZwYXRoKSkKICAgICAgICB3aXRoIG9wZW4o\nZnBhdGgpIGFzIGY6CiAgICAgICAgICAgIGZvciBsaW5lIGluIGY6CiAgICAgICAgICAgICAgICBs\naW5lID0gbGluZS5zdHJpcCgpCiAgICAgICAgICAgICAgICBpZiBub3QgbGluZToKICAgICAgICAg\nICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICAgICAgcmVjb3JkID0ganNvbi5sb2Fkcyhs\naW5lKQogICAgICAgICAgICAgICAgbGFiZWwgPSByZWNvcmQuZ2V0KCJsYWJlbCIsICIiKQogICAg\nICAgICAgICAgICAgaWYgbGFiZWwgbm90IGluIExBQkVMMklEOgogICAgICAgICAgICAgICAgICAg\nIGNvbnRpbnVlCiAgICAgICAgICAgICAgICBzYW1wbGVzLmFwcGVuZCh7CiAgICAgICAgICAgICAg\nICAgICAgIm9ic2VydmF0aW9uIjogcmVjb3JkLmdldCgib2JzZXJ2YXRpb24iLCAiIiksCiAgICAg\nICAgICAgICAgICAgICAgImFjdGlvbl9oaXN0b3J5IjogcmVjb3JkLmdldCgiYWN0aW9uX2hpc3Rv\ncnkiLCBbXSksCiAgICAgICAgICAgICAgICAgICAgImxhYmVsIjogbGFiZWwsCiAgICAgICAgICAg\nICAgICAgICAgImxhYmVsX2lkIjogTEFCRUwySURbbGFiZWxdLAogICAgICAgICAgICAgICAgICAg\nICJ0YXNrX3R5cGUiOiByZWNvcmQuZ2V0KCJ0YXNrX25hbWUiLCB0YXNrX3R5cGUpLAogICAgICAg\nICAgICAgICAgfSkKCiAgICBwcmludChmIkxvYWRlZCB7bGVuKHNhbXBsZXMpfSBzYW1wbGVzIGZy\nb20ge2xlbihmaWxlcyl9IGZpbGVzICh0aWVzIGV4Y2x1ZGVkKSIpCiAgICBsYWJlbF9kaXN0ID0g\nQ291bnRlcihzWyJsYWJlbCJdIGZvciBzIGluIHNhbXBsZXMpCiAgICBmb3IgaywgdiBpbiBzb3J0\nZWQobGFiZWxfZGlzdC5pdGVtcygpKToKICAgICAgICBwcmludChmIiAge2t9OiB7dn0gKHt2L2xl\nbihzYW1wbGVzKSoxMDA6LjFmfSUpIikKICAgIHJldHVybiBzYW1wbGVzCgoKZGVmIHN0cmF0aWZp\nZWRfc3BsaXQoCiAgICBzYW1wbGVzOiBMaXN0W0RpY3RdLCBldmFsX3JhdGlvOiBmbG9hdCwgc2Vl\nZDogaW50CikgLT4gVHVwbGVbTGlzdFtEaWN0XSwgTGlzdFtEaWN0XV06CiAgICAiIiJTdHJhdGlm\naWVkIHRyYWluL3ZhbCBzcGxpdCBieSB0YXNrX3R5cGUuIiIiCiAgICBybmcgPSByYW5kb20uUmFu\nZG9tKHNlZWQpCiAgICBieV90YXNrOiBEaWN0W3N0ciwgTGlzdFtEaWN0XV0gPSB7fQogICAgZm9y\nIHMgaW4gc2FtcGxlczoKICAgICAgICBieV90YXNrLnNldGRlZmF1bHQoc1sidGFza190eXBlIl0s\nIFtdKS5hcHBlbmQocykKCiAgICB0cmFpbl9zZXQsIHZhbF9zZXQgPSBbXSwgW10KICAgIGZvciB0\nYXNrLCBpdGVtcyBpbiBieV90YXNrLml0ZW1zKCk6CiAgICAgICAgcm5nLnNodWZmbGUoaXRlbXMp\nCiAgICAgICAgbl92YWwgPSBtYXgoMSwgaW50KGxlbihpdGVtcykgKiBldmFsX3JhdGlvKSkKICAg\nICAgICB2YWxfc2V0LmV4dGVuZChpdGVtc1s6bl92YWxdKQogICAgICAgIHRyYWluX3NldC5leHRl\nbmQoaXRlbXNbbl92YWw6XSkKCiAgICBybmcuc2h1ZmZsZSh0cmFpbl9zZXQpCiAgICBybmcuc2h1\nZmZsZSh2YWxfc2V0KQogICAgcHJpbnQoZiJTcGxpdDogdHJhaW49e2xlbih0cmFpbl9zZXQpfSwg\ndmFsPXtsZW4odmFsX3NldCl9IikKICAgIHJldHVybiB0cmFpbl9zZXQsIHZhbF9zZXQKCgpjbGFz\ncyBSb3V0ZXJEYXRhc2V0KERhdGFzZXQpOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIHNhbXBsZXM6\nIExpc3RbRGljdF0sIHRva2VuaXplciwgbWF4X2xlbmd0aDogaW50KToKICAgICAgICBzZWxmLnNh\nbXBsZXMgPSBzYW1wbGVzCiAgICAgICAgc2VsZi50b2tlbml6ZXIgPSB0b2tlbml6ZXIKICAgICAg\nICBzZWxmLm1heF9sZW5ndGggPSBtYXhfbGVuZ3RoCgogICAgZGVmIF9fbGVuX18oc2VsZik6CiAg\nICAgICAgcmV0dXJuIGxlbihzZWxmLnNhbXBsZXMpCgogICAgZGVmIF9fZ2V0aXRlbV9fKHNlbGYs\nIGlkeCk6CiAgICAgICAgcyA9IHNlbGYuc2FtcGxlc1tpZHhdCiAgICAgICAgcHJvbXB0ID0gYnVp\nbGRfcHJvbXB0KHNbIm9ic2VydmF0aW9uIl0sIHNbImFjdGlvbl9oaXN0b3J5Il0pCiAgICAgICAg\nZW5jb2RpbmcgPSBzZWxmLnRva2VuaXplcigKICAgICAgICAgICAgcHJvbXB0LAogICAgICAgICAg\nICB0cnVuY2F0aW9uPVRydWUsCiAgICAgICAgICAgIG1heF9sZW5ndGg9c2VsZi5tYXhfbGVuZ3Ro\nLAogICAgICAgICAgICBwYWRkaW5nPSJtYXhfbGVuZ3RoIiwKICAgICAgICAgICAgcmV0dXJuX3Rl\nbnNvcnM9InB0IiwKICAgICAgICApCiAgICAgICAgcmV0dXJuIHsKICAgICAgICAgICAgImlucHV0\nX2lkcyI6IGVuY29kaW5nWyJpbnB1dF9pZHMiXS5zcXVlZXplKDApLAogICAgICAgICAgICAiYXR0\nZW50aW9uX21hc2siOiBlbmNvZGluZ1siYXR0ZW50aW9uX21hc2siXS5zcXVlZXplKDApLAogICAg\nICAgICAgICAibGFiZWxzIjogdG9yY2gudGVuc29yKHNbImxhYmVsX2lkIl0sIGR0eXBlPXRvcmNo\nLmxvbmcpLAogICAgICAgIH0KCgojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQojIENsYXNzIHdlaWdodGlu\nZwojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIGNvbXB1dGVfY2xhc3Nfd2VpZ2h0cyh0cmFpbl9z\nYW1wbGVzOiBMaXN0W0RpY3RdLCBtb2RlOiBzdHIgPSAiYXV0byIpIC0+IHRvcmNoLlRlbnNvcjoK\nICAgICMgImF1dG8iOiB3ZWlnaHRfYyA9IE5fdG90YWwgLyAobnVtX2NsYXNzZXMgKiBOX2MpLCBp\nLmUuIGludmVyc2UgZnJlcXVlbmN5IOKAlAogICAgIyAgICAgICAgIHJhcmVyIGNsYXNzIGdldHMg\ncHJvcG9ydGlvbmFsbHkgaGlnaGVyIHdlaWdodC4KICAgICMgIncwLHcxIjogbWFudWFsIHdlaWdo\ndHMsIGUuZy4gIjEuMCw1LjAiIC0+IGludGVybmFsPTEuMCwgZGV0ZXJtaW5pc3RpYz01LjAKICAg\nIG51bV9jbGFzc2VzID0gbGVuKExBQkVMMklEKQogICAgaWYgbW9kZSA9PSAiYXV0byI6CiAgMDg0\nODQwYTEzZmM4CiAgICAgICAgY291bnRzID0gQ291bnRlcihzWyJsYWJlbF9pZCJdIGZvciBzIGlu\nIHRyYWluX3NhbXBsZXMpCiAgICAgICAgdG90YWwgPSBsZW4odHJhaW5fc2FtcGxlcykKICAgICAg\nICB3ZWlnaHRzID0gdG9yY2gudGVuc29yKAogICAgICAgICAgICBbdG90YWwgLyAobnVtX2NsYXNz\nZXMgKiBtYXgoY291bnRzLmdldChpLCAxKSwgMSkpIGZvciBpIGluIHJhbmdlKG51bV9jbGFzc2Vz\nKV0sCiAgICAgICAgICAgIGR0eXBlPXRvcmNoLmZsb2F0MzIsCiAgICAgICAgKQogICAgZWxzZToK\nICAgICAgICBwYXJ0cyA9IFtmbG9hdCh4LnN0cmlwKCkpIGZvciB4IGluIG1vZGUuc3BsaXQoIiwi\nKV0KICAgICAgICBpZiBsZW4ocGFydHMpICE9IG51bV9jbGFzc2VzOgogICAgICAgICAgICByYWlz\nZSBWYWx1ZUVycm9yKGYiRXhwZWN0ZWQge251bV9jbGFzc2VzfSB3ZWlnaHRzLCBnb3Qge2xlbihw\nYXJ0cyl9OiB7bW9kZX0iKQogICAgICAgIHdlaWdodHMgPSB0b3JjaC50ZW5zb3IocGFydHMsIGR0\neXBlPXRvcmNoLmZsb2F0MzIpCiAgICByZXR1cm4gd2VpZ2h0cwoKCmNsYXNzIFdlaWdodGVkQ0VU\ncmFpbmVyKFRyYWluZXIpOgogICAgIiIiVHJhaW5lciB3aXRoIGNsYXNzLXdlaWdodGVkIENyb3Nz\nRW50cm9weUxvc3MgYW5kIG9wdGlvbmFsIFdlaWdodGVkUmFuZG9tU2FtcGxlci4iIiIKCiAgICBk\nZWYgX19pbml0X18oc2VsZiwgY2xhc3Nfd2VpZ2h0czogT3B0aW9uYWxbdG9yY2guVGVuc29yXSA9\nIE5vbmUsCiAgICAgICAgICAgICAgICAgd2VpZ2h0ZWRfc2FtcGxlcjogT3B0aW9uYWxbV2VpZ2h0\nZWRSYW5kb21TYW1wbGVyXSA9IE5vbmUsICoqa3dhcmdzKToKICAgICAgICBzdXBlcigpLl9faW5p\ndF9fKCoqa3dhcmdzKQogICAgICAgIHNlbGYuX2NsYXNzX3dlaWdodHMgPSBjbGFzc193ZWlnaHRz\nCiAgICAgICAgc2VsZi5fd2VpZ2h0ZWRfc2FtcGxlciA9IHdlaWdodGVkX3NhbXBsZXIKCiAgICBk\nZWYgY29tcHV0ZV9sb3NzKHNlbGYsIG1vZGVsLCBpbnB1dHMsIHJldHVybl9vdXRwdXRzPUZhbHNl\nLCAqKmt3YXJncyk6CiAgICAgICAgbGFiZWxzID0gaW5wdXRzLnBvcCgibGFiZWxzIikKICAgICAg\nICBvdXRwdXRzID0gbW9kZWwoKippbnB1dHMpCiAgICAgICAgbG9naXRzID0gb3V0cHV0cy5sb2dp\ndHMKICAgICAgICBpZiBzZWxmLl9jbGFzc193ZWlnaHRzIGlzIG5vdCBOb25lOgogICAgICAgICAg\nICBsb3NzX2ZuID0gdG9yY2gubm4uQ3Jvc3NFbnRyb3B5TG9zcyh3ZWlnaHQ9c2VsZi5fY2xhc3Nf\nd2VpZ2h0cy50byhsb2dpdHMuZGV2aWNlKSkKICAgICAgICBlbHNlOgogICAgICAgICAgICBsb3Nz\nX2ZuID0gdG9yY2gubm4uQ3Jvc3NFbnRyb3B5TG9zcygpCiAgICAgICAgbG9zcyA9IGxvc3NfZm4o\nbG9naXRzLCBsYWJlbHMpCiAgICAgICAgcmV0dXJuIChsb3NzLCBvdXRwdXRzKSBpZiByZXR1cm5f\nb3V0cHV0cyBlbHNlIGxvc3MKCiAgICBkZWYgZ2V0X3RyYWluX2RhdGFsb2FkZXIoc2VsZikgLT4g\nRGF0YUxvYWRlcjoKICAgICAgICBpZiBzZWxmLl93ZWlnaHRlZF9zYW1wbGVyIGlzIE5vbmU6CiAg\nICAgICAgICAgIHJldHVybiBzdXBlcigpLmdldF90cmFpbl9kYXRhbG9hZGVyKCkKICAgICAgICBy\nZXR1cm4gRGF0YUxvYWRlcigKICAgICAgICAgICAgc2VsZi50cmFpbl9kYXRhc2V0LAogICAgICAg\nICAgICBiYXRjaF9zaXplPXNlbGYuYXJncy5wZXJfZGV2aWNlX3RyYWluX2JhdGNoX3NpemUsCiAg\nICAgICAgICAgIHNhbXBsZXI9c2VsZi5fd2VpZ2h0ZWRfc2FtcGxlciwKICAgICAgICAgICAgbnVt\nX3dvcmtlcnM9c2VsZi5hcmdzLmRhdGFsb2FkZXJfbnVtX3dvcmtlcnMsCiAgICAgICAgICAgIHBp\nbl9tZW1vcnk9c2VsZi5hcmdzLmRhdGFsb2FkZXJfcGluX21lbW9yeSwKICAgICAgICApCgoKIyAt\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0KIyBNb2RlbCBzZXR1cAojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVm\nIHNldHVwX21vZGVsKG1vZGVsX25hbWU6IHN0ciwgYXJncyk6CiAgICB0b2tlbml6ZXIgPSBBdXRv\nVG9rZW5pemVyLmZyb21fcHJldHJhaW5lZChtb2RlbF9uYW1lLCB0cnVzdF9yZW1vdGVfY29kZT1U\ncnVlKQogICAgaWYgdG9rZW5pemVyLnBhZF90b2tlbiBpcyBOb25lOgogICAgICAgIHRva2VuaXpl\nci5wYWRfdG9rZW4gPSB0b2tlbml6ZXIuZW9zX3Rva2VuCgogICAgbW9kZWwgPSBBdXRvTW9kZWxG\nb3JTZXF1ZW5jZUNsYXNzaWZpY2F0aW9uLmZyb21fcHJldHJhaW5lZCgKICAgICAgICBtb2RlbF9u\nYW1lLAogICAgICAgIG51bV9sYWJlbHM9MiwKICAgICAgICBpZDJsYWJlbD1JRDJMQUJFTCwKICAg\nICAgICBsYWJlbDJpZD1MQUJFTDJJRCwKICAgICAgICB0cnVzdF9yZW1vdGVfY29kZT1UcnVlLAog\nICAgICAgIHRvcmNoX2R0eXBlPXRvcmNoLmJmbG9hdDE2LAogICAgKQogICAgbW9kZWwuY29uZmln\nLnBhZF90b2tlbl9pZCA9IHRva2VuaXplci5wYWRfdG9rZW5faWQKCiAgICBsb3JhX2NvbmZpZyA9\nIExvcmFDb25maWcoCiAgICAgICAgcj1hcmdzLmxvcmFfciwKICAgICAgICBsb3JhX2FscGhhPWFy\nZ3MubG9yYV9hbHBoYSwKICAgICAgICB0YXJnZXRfbW9kdWxlcz1bInFfcHJvaiIsICJ2X3Byb2oi\nLCAia19wcm9qIiwgIm9fcHJvaiJdLAogICAgICAgIGxvcmFfZHJvcG91dD1hcmdzLmxvcmFfZHJv\ncG91dCwKICAgICAgICB0YXNrX3R5cGU9VGFza1R5cGUuU0VRX0NMUywKICAgICAgICBtb2R1bGVz\nX3RvX3NhdmU9WyJzY29yZSJdLAogICAgKQogICAgbW9kZWwgPSBnZXRfcGVmdF9tb2RlbChtb2Rl\nbCwgbG9yYV9jb25maWcpCiAgICBtb2RlbC5wcmludF90cmFpbmFibGVfcGFyYW1ldGVycygpCiAg\nICByZXR1cm4gbW9kZWwsIHRva2VuaXplcgoKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiMgTWV0cmlj\ncwojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKZGVmIGNvbXB1dGVfbWV0cmljcyhldmFsX3ByZWQpOgog\nICAgbG9naXRzLCBsYWJlbHMgPSBldmFsX3ByZWQKICAgIHByZWRzID0gbnAuYXJnbWF4KGxvZ2l0\ncywgYXhpcz0tMSkKICAgIGFjYyA9IGFjY3VyYWN5X3Njb3JlKGxhYmVscywgcHJlZHMpCiAgICBw\ncmVjLCByZWMsIGYxLCBfID0gcHJlY2lzaW9uX3JlY2FsbF9mc2NvcmVfc3VwcG9ydChsYWJlbHMs\nIHByZWRzLCBhdmVyYWdlPU5vbmUsIGxhYmVscz1bMCwgMV0pCiAgICByZXR1cm4gewogICAgICAg\nICJhY2N1cmFjeSI6IGFjYywKICAgICAgICAicHJlY2lzaW9uX2ludGVybmFsIjogcHJlY1swXSwK\nICAgICAgICAicmVjYWxsX2ludGVybmFsIjogcmVjWzBdLAogICAgICAgICJmMV9pbnRlcm5hbCI6\nIGYxWzBdLAogICAgICAgICJwcmVjaXNpb25fZGV0ZXJtaW5pc3RpYyI6IHByZWNbMV0sCiAgICAg\nICAgInJlY2FsbF9kZXRlcm1pbmlzdGljIjogcmVjWzFdLAogICAgICAgICJmMV9kZXRlcm1pbmlz\ndGljIjogZjFbMV0sCiAgICB9CgoKZGVmIHBlcl90YXNrX2V2YWx1YXRpb24odHJhaW5lciwgdmFs\nX2RhdGFzZXQsIHZhbF9zYW1wbGVzKSAtPiBEaWN0W3N0ciwgQW55XToKICAgICIiIkNvbXB1dGUg\ncGVyLXRhc2sgYWNjdXJhY3kgYW5kIGNvbmZ1c2lvbiBtYXRyaXguIiIiCiAgICBwcmVkaWN0aW9u\ncyA9IHRyYWluZXIucHJlZGljdCh2YWxfZGF0YXNldCkKICAgIHByZWRzID0gbnAuYXJnbWF4KHBy\nZWRpY3Rpb25zLnByZWRpY3Rpb25zLCBheGlzPS0xKQogICAgbGFiZWxzID0gcHJlZGljdGlvbnMu\nbGFiZWxfaWRzCgogICAgY20gPSBjb25mdXNpb25fbWF0cml4KGxhYmVscywgcHJlZHMsIGxhYmVs\ncz1bMCwgMV0pLnRvbGlzdCgpCgogICAgdGFza19tZXRyaWNzID0ge30KICAgIGJ5X3Rhc2s6IERp\nY3Rbc3RyLCBEaWN0W3N0ciwgbGlzdF1dID0ge30KICAgIGZvciBpLCBzIGluIGVudW1lcmF0ZSh2\nYWxfc2FtcGxlcyk6CiAgICAgICAgdCA9IHNbInRhc2tfdHlwZSJdCiAgICAgICAgaWYgdCBub3Qg\naW4gYnlfdGFzazoKICAgICAgICAgICAgYnlfdGFza1t0XSA9IHsicHJlZHMiOiBbXSwgImxhYmVs\ncyI6IFtdfQogICAgICAgIGJ5X3Rhc2tbdF1bInByZWRzIl0uYXBwZW5kKHByZWRzW2ldKQogICAg\nICAgIGJ5X3Rhc2tbdF1bImxhYmVscyJdLmFwcGVuZChsYWJlbHNbaV0pCgogICAgZm9yIHRhc2ss\nIGRhdGEgaW4gc29ydGVkKGJ5X3Rhc2suaXRlbXMoKSk6CiAgICAgICAgYWNjID0gYWNjdXJhY3lf\nc2NvcmUoZGF0YVsibGFiZWxzIl0sIGRhdGFbInByZWRzIl0pCiAgICAgICAgbiA9IGxlbihkYXRh\nWyJsYWJlbHMiXSkKICAgICAgICB0YXNrX21ldHJpY3NbdGFza10gPSB7ImFjY3VyYWN5IjogYWNj\nLCAibl9zYW1wbGVzIjogbn0KCiAgICByZXR1cm4gewogICAgICAgICJvdmVyYWxsX2FjY3VyYWN5\nIjogYWNjdXJhY3lfc2NvcmUobGFiZWxzLCBwcmVkcyksCiAgICAgICAgImNvbmZ1c2lvbl9tYXRy\naXgiOiBjbSwKICAgICAgICAiY29uZnVzaW9uX2xhYmVscyI6IFsiaW50ZXJuYWwiLCAiZGV0ZXJt\naW5pc3RpYyJdLAogICAgICAgICJwZXJfdGFzayI6IHRhc2tfbWV0cmljcywKICAgIH0KCgojIC0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLQojIE1haW4KIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmRlZiBtYWluKCk6\nCiAgICBhcmdzID0gcGFyc2VfYXJncygpCgogICAgaWYgYXJncy5kcnlfcnVuOgogICAgICAgIHBy\naW50KCJEcnkgcnVuOiBpbXBvcnRzIE9LLCBhcmdzIHBhcnNlZCBzdWNjZXNzZnVsbHkuIikKICAg\nICAgICBwcmludChmIiAgbW9kZWxfbmFtZTogICAgICAgICAgICB7YXJncy5tb2RlbF9uYW1lfSIp\nCiAgICAgICAgcHJpbnQoZiIgIGRhdGFfZGlyOiAgICAgICAgICAgICAge2FyZ3MuZGF0YV9kaXJ9\nIikKICAgICAgICBwcmludChmIiAgb3V0cHV0X2RpcjogICAgICAgICAgICB7YXJncy5vdXRwdXRf\nZGlyfSIpCiAgICAgICAgcHJpbnQoZiIgIGNsYXNzX3dlaWdodHM6ICAgICAgICAge2FyZ3MuY2xh\nc3Nfd2VpZ2h0c30iKQogICAgICAgIHByaW50KGYiICBtaW5faW50ZXJuYWxfc2FtcGxlczogIHth\ncmdzLm1pbl9pbnRlcm5hbF9zYW1wbGVzfSIpCiAgICAgICAgcHJpbnQoZiIgIHVwc2FtcGxlX21p\nbm9yaXR5OiAgICAge2FyZ3MudXBzYW1wbGVfbWlub3JpdHl9IikKICAgICAgICByZXR1cm4KCiAg\nICBvcy5lbnZpcm9uWyJDVURBX1ZJU0lCTEVfREVWSUNFUyJdID0gc3RyKGFyZ3MuZ3B1X2lkKQog\nICAgcmFuZG9tLnNlZWQoYXJncy5zZWVkKQogICAgbnAucmFuZG9tLnNlZWQoYXJncy5zZWVkKQog\nICAgdG9yY2gubWFudWFsX3NlZWQoYXJncy5zZWVkKQoKICAgIG9zLm1ha2VkaXJzKGFyZ3Mub3V0\ncHV0X2RpciwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBzYW1wbGVzID0gbG9hZF9sYWJlbGVkX2RhdGEo\nYXJncy5kYXRhX2RpcikKICAgIHRyYWluX3NhbXBsZXMsIHZhbF9zYW1wbGVzID0gc3RyYXRpZmll\nZF9zcGxpdChzYW1wbGVzLCBhcmdzLmV2YWxfc3BsaXQsIGFyZ3Muc2VlZCkKCiAgICAjIC0tLSBD\naGVjayBtaW5vcml0eSBjbGFzcyBzYW1wbGUgY291bnQgLS0tCiAgICB0cmFpbl9sYWJlbF9jb3Vu\ndHMgPSBDb3VudGVyKHNbImxhYmVsIl0gZm9yIHMgaW4gdHJhaW5fc2FtcGxlcykKICAgIG5faW50\nZXJuYWwgPSB0cmFpbl9sYWJlbF9jb3VudHMuZ2V0KCJpbnRlcm5hbCIsIDApCiAgICBpZiBuX2lu\ndGVybmFsIDwgYXJncy5taW5faW50ZXJuYWxfc2FtcGxlczoKICAgICAgICB3YXJuaW5ncy53YXJu\nKAogICAgICAgICAgICBmIk9ubHkge25faW50ZXJuYWx9IGludGVybmFsIHNhbXBsZXMgaW4gdHJh\naW5pbmcgc2V0ICIKICAgICAgICAgICAgZiIodGhyZXNob2xkOiB7YXJncy5taW5faW50ZXJuYWxf\nc2FtcGxlc30pLiAiCiAgICAgICAgICAgIGYiQ29uc2lkZXIgY29sbGVjdGluZyBtb3JlIGRhdGEg\nb3IgdXNpbmcgLS1jbGFzc193ZWlnaHRzIGF1dG8uIiwKICAgICAgICAgICAgc3RhY2tsZXZlbD0x\nLAogICAgICAgICkKCiAgICAjIC0tLSBDb21wdXRlIGNsYXNzIHdlaWdodHMgKGludmVyc2UgZnJl\ncXVlbmN5IG9yIG1hbnVhbCkgLS0tCiAgICBjbGFzc193ZWlnaHRzID0gTm9uZQogICAgaWYgYXJn\ncy5jbGFzc193ZWlnaHRzIGlzIG5vdCBOb25lOgogICAgICAgIGNsYXNzX3dlaWdodHMgPSBjb21w\ndXRlX2NsYXNzX3dlaWdodHModHJhaW5fc2FtcGxlcywgYXJncy5jbGFzc193ZWlnaHRzKQogICAg\nICAgIHdlaWdodF9kaWN0ID0ge2xhYmVsOiBjbGFzc193ZWlnaHRzW2xpZF0uaXRlbSgpIGZvciBs\nYWJlbCwgbGlkIGluIExBQkVMMklELml0ZW1zKCl9CiAgICAgICAgcHJpbnQoZiJDbGFzcyB3ZWln\naHRzOiB7d2VpZ2h0X2RpY3R9IikKICAgICAgICBwcmludChmIkVmZmVjdGl2ZSBzYW1wbGUgY291\nbnRzOiB7ZGljdCh0cmFpbl9sYWJlbF9jb3VudHMpfSIpCgogICAgbW9kZWwsIHRva2VuaXplciA9\nIHNldHVwX21vZGVsKGFyZ3MubW9kZWxfbmFtZSwgYXJncykKCiAgICB0cmFpbl9kYXRhc2V0ID0g\nUm91dGVyRGF0YXNldCh0cmFpbl9zYW1wbGVzLCB0b2tlbml6ZXIsIGFyZ3MubWF4X3NlcV9sZW4p\nCiAgICB2YWxfZGF0YXNldCA9IFJvdXRlckRhdGFzZXQodmFsX3NhbXBsZXMsIHRva2VuaXplciwg\nYXJncy5tYXhfc2VxX2xlbikKCiAgICAjIC0tLSBCdWlsZCBXZWlnaHRlZFJhbmRvbVNhbXBsZXIg\nZm9yIG1pbm9yaXR5IG92ZXJzYW1wbGluZyAtLS0KICAgICMgUGVyLXNhbXBsZSB3ZWlnaHQgPSAx\nIC8gY291bnRfb2ZfaXRzX2NsYXNzLCBzbyBtaW5vcml0eSBzYW1wbGVzIGFyZSBkcmF3biBtb3Jl\nIG9mdGVuLgogICAgd2VpZ2h0ZWRfc2FtcGxlciA9IE5vbmUKICAgIGlmIGFyZ3MudXBzYW1wbGVf\nbWlub3JpdHk6CiAgICAgICAgc2FtcGxlX3dlaWdodHMgPSBbMS4wIC8gdHJhaW5fbGFiZWxfY291\nbnRzW3NbImxhYmVsIl1dIGZvciBzIGluIHRyYWluX3NhbXBsZXNdCiAgICAgICAgd2VpZ2h0ZWRf\nc2FtcGxlciA9IFdlaWdodGVkUmFuZG9tU2FtcGxlcigKICAgICAgICAgICAgd2VpZ2h0cz1zYW1w\nbGVfd2VpZ2h0cywKICAgICAgICAgICAgbnVtX3NhbXBsZXM9bGVuKHRyYWluX3NhbXBsZXMpLAog\nICAgICAgICAgICByZXBsYWNlbWVudD1UcnVlLAogICAgICAgICkKICAgICAgICBwcmludChmIlVw\nc2FtcGxpbmcgZW5hYmxlZDogV2VpZ2h0ZWRSYW5kb21TYW1wbGVyIHdpdGgge2xlbih0cmFpbl9z\nYW1wbGVzKX0gZHJhd3MvZXBvY2giKQoKICAgIHVzZV9iZjE2ID0gdG9yY2guY3VkYS5pc19hdmFp\nbGFibGUoKSBhbmQgdG9yY2guY3VkYS5nZXRfZGV2aWNlX2NhcGFiaWxpdHkoKVswXSA+PSA4CiAg\nICB0cmFpbmluZ19hcmdzID0gVHJhaW5pbmdBcmd1bWVudHMoCiAgICAgICAgb3V0cHV0X2Rpcj1h\ncmdzLm91dHB1dF9kaXIsCiAgICAgICAgbnVtX3RyYWluX2Vwb2Nocz1hcmdzLmVwb2NocywKICAg\nICAgICBwZXJfZGV2aWNlX3RyYWluX2JhdGNoX3NpemU9YXJncy5iYXRjaF9zaXplLAogICAgICAg\nIHBlcl9kZXZpY2VfZXZhbF9iYXRjaF9zaXplPWFyZ3MuZXZhbF9iYXRjaF9zaXplLAogICAgICAg\nIGxlYXJuaW5nX3JhdGU9YXJncy5sciwKICAgICAgICB3ZWlnaHRfZGVjYXk9YXJncy53ZWlnaHRf\nZGVjYXksCiAgICAgICAgd2FybXVwX3JhdGlvPWFyZ3Mud2FybXVwX3JhdGlvLAogICAgICAgIGV2\nYWxfc3RyYXRlZ3k9ImVwb2NoIiwKICAgICAgICBzYXZlX3N0cmF0ZWd5PSJlcG9jaCIsCiAgICAg\nICAgbG9hZF9iZXN0X21vZGVsX2F0X2VuZD1UcnVlLAogICAgICAgIG1ldHJpY19mb3JfYmVzdF9t\nb2RlbD0iYWNjdXJhY3kiLAogICAgICAgIGdyZWF0ZXJfaXNfYmV0dGVyPVRydWUsCiAgICAgICAg\nYmYxNj11c2VfYmYxNiwKICAgICAgICBmcDE2PShub3QgdXNlX2JmMTYgYW5kIHRvcmNoLmN1ZGEu\naXNfYXZhaWxhYmxlKCkpLAogICAgICAgIGxvZ2dpbmdfc3RlcHM9MTAsCiAgICAgICAgZGF0YWxv\nYWRlcl9udW1fd29ya2Vycz00LAogICAgICAgIHJlcG9ydF90bz0id2FuZGIiLAogICAgICAgIHJ1\nbl9uYW1lPWYicm91dGVyLXNmdC17b3MucGF0aC5iYXNlbmFtZShhcmdzLm1vZGVsX25hbWUpfS1y\ne2FyZ3MubG9yYV9yfSIsCiAgICAgICAgc2VlZD1hcmdzLnNlZWQsCiAgICAgICAgc2F2ZV90b3Rh\nbF9saW1pdD0yLAogICAgKQoKICAgIG9zLmVudmlyb25bIldBTkRCX1BST0pFQ1QiXSA9IGFyZ3Mu\nd2FuZGJfcHJvamVjdAoKICAgICMgLS0tIExvZyBjbGFzcyB3ZWlnaHRpbmcgY29uZmlnIHRvIFcm\nQiAtLS0KICAgIHRyeToKICAgICAgICBpbXBvcnQgd2FuZGIKICAgICAgICB3YW5kYl9jb25maWcg\nPSB2YXJzKGFyZ3MpLmNvcHkoKQogICAgICAgIGlmIGNsYXNzX3dlaWdodHMgaXMgbm90IE5vbmU6\nCiAgICAgICAgICAgIHdhbmRiX2NvbmZpZ1siY2xhc3Nfd2VpZ2h0c192YWx1ZXMiXSA9IHsKICAg\nICAgICAgICAgICAgIGxhYmVsOiBjbGFzc193ZWlnaHRzW2xpZF0uaXRlbSgpIGZvciBsYWJlbCwg\nbGlkIGluIExBQkVMMklELml0ZW1zKCkKICAgICAgICAgICAgfQogICAgICAgIHdhbmRiX2NvbmZp\nZ1sidHJhaW5fbGFiZWxfY291bnRzIl0gPSBkaWN0KHRyYWluX2xhYmVsX2NvdW50cykKICAgICAg\nICB3YW5kYl9jb25maWdbInVwc2FtcGxlX21pbm9yaXR5Il0gPSBhcmdzLnVwc2FtcGxlX21pbm9y\naXR5CiAgICAgICAgd2FuZGIuaW5pdCgKICAgICAgICAgICAgcHJvamVjdD1hcmdzLndhbmRiX3By\nb2plY3QsCiAgICAgICAgICAgIG5hbWU9dHJhaW5pbmdfYXJncy5ydW5fbmFtZSwKICAgICAgICAg\nICAgY29uZmlnPXdhbmRiX2NvbmZpZywKICAgICAgICApCiAgICBleGNlcHQgRXhjZXB0aW9uOgog\nICAgICAgIHBhc3MKCiAgICB0cmFpbmVyID0gV2VpZ2h0ZWRDRVRyYWluZXIoCiAgICAgICAgY2xh\nc3Nfd2VpZ2h0cz1jbGFzc193ZWlnaHRzLAogICAgICAgIHdlaWdodGVkX3NhbXBsZXI9d2VpZ2h0\nZWRfc2FtcGxlciwKICAgICAgICBtb2RlbD1tb2RlbCwKICAgICAgICBhcmdzPXRyYWluaW5nX2Fy\nZ3MsCiAgICAgICAgdHJhaW5fZGF0YXNldD10cmFpbl9kYXRhc2V0LAogICAgICAgIGV2YWxfZGF0\nYXNldD12YWxfZGF0YXNldCwKICAgICAgICBjb21wdXRlX21ldHJpY3M9Y29tcHV0ZV9tZXRyaWNz\nLAogICAgICAgIGNhbGxiYWNrcz1bRWFybHlTdG9wcGluZ0NhbGxiYWNrKGVhcmx5X3N0b3BwaW5n\nX3BhdGllbmNlPWFyZ3MuZWFybHlfc3RvcHBpbmdfcGF0aWVuY2UpXSwKICAgICkKCiAgICBwcmlu\ndChmIlxueyc9Jyo2MH0iKQogICAgcHJpbnQoZiJTdGFydGluZyB0cmFpbmluZzoge2xlbih0cmFp\nbl9kYXRhc2V0KX0gdHJhaW4gLyB7bGVuKHZhbF9kYXRhc2V0KX0gdmFsIHNhbXBsZXMiKQog\nICAgcHJpbnQoZiJNb2RlbDoge2FyZ3MubW9kZWxfbmFtZX0sIExvUkEgcj17YXJncy5sb3JhX3J9\nLCBscj17YXJncy5scn0iKQogICAgaWYgY2xhc3Nfd2VpZ2h0cyBpcyBub3QgTm9uZToKICAgICAg\nICBwcmludChmIkNsYXNzIHdlaWdodHM6IHtjbGFzc193ZWlnaHRzLnRvbGlzdCgpfSIpCiAgICBp\nZiBhcmdzLnVwc2FtcGxlX21pbm9yaXR5OgogICAgICAgIHByaW50KCJNaW5vcml0eSBvdmVyc2Ft\ncGxpbmc6IGVuYWJsZWQiKQogICAgcHJpbnQoZiJ7Jz0nKjYwfVxuIikKCiAgICB0cmFpbmVyLnRy\nYWluKCkKCiAgICBhZGFwdGVyX2RpciA9IG9zLnBhdGguam9pbihhcmdzLm91dHB1dF9kaXIsICJm\naW5hbF9hZGFwdGVyIikKICAgIG1vZGVsLnNhdmVfcHJldHJhaW5lZChhZGFwdGVyX2RpcikKICAg\nIHRva2VuaXplci5zYXZlX3ByZXRyYWluZWQoYWRhcHRlcl9kaXIpCiAgICBwcmludChmIkFkYXB0\nZXIgc2F2ZWQgdG8ge2FkYXB0ZXJfZGlyfSIpCgogICAgcHJpbnQoIlxuLS0tIEV2YWx1YXRpb24g\nLS0tIikKICAgIGV2YWxfcmVwb3J0ID0gcGVyX3Rhc2tfZXZhbHVhdGlvbih0cmFpbmVyLCB2YWxf\nZGF0YXNldCwgdmFsX3NhbXBsZXMpCgogICAgcmVwb3J0X3BhdGggPSBvcy5wYXRoLmpvaW4oYXJn\ncy5vdXRwdXRfZGlyLCAiZXZhbF9yZXBvcnQuanNvbiIpCiAgICB3aXRoIG9wZW4ocmVwb3J0X3Bh\ndGgsICJ3IikgYXMgZjoKICAgICAgICBqc29uLmR1bXAoZXZhbF9yZXBvcnQsIGYsIGluZGVudD0y\nKQogICAgcHJpbnQoZiJFdmFsIHJlcG9ydCBzYXZlZCB0byB7cmVwb3J0X3BhdGh9IikKCiAgICBw\ncmludChmIlxuT3ZlcmFsbCBhY2N1cmFjeToge2V2YWxfcmVwb3J0WydvdmVyYWxsX2FjY3VyYWN5\nJ106LjRmfSIpCiAgICBwcmludChmIkNvbmZ1c2lvbiBtYXRyaXggKHJvd3M9dHJ1ZSwgY29scz1w\ncmVkKToiKQogICAgcHJpbnQoZiIgIHtldmFsX3JlcG9ydFsnY29uZnVzaW9uX2xhYmVscyddfSIp\nCiAgICBmb3Igcm93IGluIGV2YWxfcmVwb3J0WyJjb25mdXNpb25fbWF0cml4Il06CiAgICAgICAg\ncHJpbnQoZiIgIHtyb3d9IikKICAgIHByaW50KCJcblBlci10YXNrIGFjY3VyYWN5OiIpCiAgICBm\nb3IgdGFzaywgbSBpbiBzb3J0ZWQoZXZhbF9yZXBvcnRbInBlcl90YXNrIl0uaXRlbXMoKSk6CiAg\nICAgICAgcHJpbnQoZiIgIHt0YXNrfToge21bJ2FjY3VyYWN5J106LjNmfSAobj17bVsnbl9zYW1w\nbGVzJ119KSIpCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=\nB64EOF\necho \"WRITE_OK: $(wc -l < /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py) lines\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T20:23:17.364695+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WRITE_OK: 473 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T20:23:17.364844+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "grep -n \"084840\" /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "grep -n \"084840\" /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T20:23:17.364964+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"191:  084840a13fc8\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T20:23:17.365123+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "head -n 195 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "head -n 195 /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T20:23:17.365369+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Router SFT training script for SimGate modular routing.\\n# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data\\n# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.\\n#\\n# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl\\n# Usage: python src/router_sft_train.py --help\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nimport random\\nimport warnings\\nfrom collections import Counter\\nfrom typing import List, Dict, Any, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom torch.utils.data import Dataset, DataLoader, WeightedRandomSampler\\nfrom sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix\\nfrom transformers import (\\n    AutoTokenizer,\\n    AutoModelForSequenceClassification,\\n    TrainingArguments,\\n    Trainer,\\n    EarlyStoppingCallback,\\n)\\nfrom peft import LoraConfig, get_peft_model, TaskType\\n\\nLABEL2ID = {\\\"internal\\\": 0, \\\"deterministic\\\": 1}\\nID2LABEL = {0: \\\"internal\\\", 1: \\\"deterministic\\\"}\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are a routing classifier. Given the current observation and action history, \\\"\\n    \\\"predict which reasoning modality will lead to a better outcome.\\\"\\n)\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Router SFT: finetune LLM for 2-way routing classification\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, default=\\\"results/plan_c/\\\",\\n                    help=\\\"Directory containing {task_type}/labeled_steps.jsonl\\\")\\n    p.add_argument(\\\"--model_name\\\", type=str, default=\\\"Qwen/Qwen3-1.7B\\\",\\n                    help=\\\"HuggingFace model name or local path\\\")\\n    p.add_argument(\\\"--output_dir\\\", type=str, default=\\\"results/router_sft/\\\",\\n                    help=\\\"Output directory for checkpoints and reports\\\")\\n    p.add_argument(\\\"
…[truncated 6941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T20:23:17.365539+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "sed -i '191d' /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py && echo \"FIXED: $(wc -l < /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py) lines\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "sed -i '191d' /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py && echo \"FIXED: $(wc -l < /root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py) lines\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T20:23:17.365687+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"FIXED: 472 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T20:23:17.365822+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "python3 -c \"import ast; ast.parse(open('/root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py').read()); print('SYNTAX_OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "python3 -c \"import ast; ast.parse(open('/root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py').read()); print('SYNTAX_OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T20:23:17.365945+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T20:23:17.366084+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "cd /root/autodl-tmp/simgate-modular-routing && python3 -c \"import ast; ast.parse(open('src/router_sft_train.py').read()); print('SYNTAX_OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "cd /root/autodl-tmp/simgate-modular-routing && python3 -c \"import ast; ast.parse(open('src/router_sft_train.py').read()); print('SYNTAX_OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T20:23:17.366214+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/simgate-modular-routing && python3 -c \\\"import ast; ast.parse(open(\\\\'src/router_sft_train.py\\\\').read()); print(\\\\'SYNTAX_OK\\\\')\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T20:23:17.366329+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westb-13313",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westb-13313",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T20:23:17.366444+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T20:23:17.366553+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "ls /root/miniconda3/bin/python 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "ls /root/miniconda3/bin/python 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T20:23:17.366665+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T20:23:17.366805+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "which python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "which python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T20:23:17.366917+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T20:23:17.367044+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import ast; ast.parse(open('/root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py').read()); print('SYNTAX_OK')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import ast; ast.parse(open('/root/autodl-tmp/simgate-modular-routing/src/router_sft_train.py').read()); print('SYNTAX_OK')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T20:23:17.367162+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SYNTAX_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T20:23:17.367292+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/simgate-modular-routing && python src/router_sft_train.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/simgate-modular-routing && python src/router_sft_train.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T20:23:17.367428+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: router_sft_train.py [-h] [--data_dir DATA_DIR]\\n                           [--model_name MODEL_NAME] [--output_dir OUTPUT_DIR]\\n                           [--epochs EPOCHS] [--batch_size BATCH_SIZE]\\n                           [--eval_batch_size EVAL_BATCH_SIZE] [--lr LR]\\n                           [--lora_r LORA_R] [--lora_alpha LORA_ALPHA]\\n                           [--lora_dropout LORA_DROPOUT]\\n                           [--max_seq_len MAX_SEQ_LEN] [--gpu_id GPU_ID]\\n                           [--wandb_project WANDB_PROJECT] [--seed SEED]\\n                           [--eval_split EVAL_SPLIT]\\n                           [--warmup_ratio WARMUP_RATIO]\\n                           [--weight_decay WEIGHT_DECAY]\\n                           [--early_stopping_patience EARLY_STOPPING_PATIENCE]\\n                           [--dry_run] [--class_weights CLASS_WEIGHTS]\\n                           [--min_internal_samples MIN_INTERNAL_SAMPLES]\\n                           [--upsample_minority]\\n\\nRouter SFT: finetune LLM for 2-way routing classification\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --data_dir DATA_DIR   Directory containing {task_type}/labeled_steps.jsonl\\n  --model_name MODEL_NAME\\n                        HuggingFace model name or local path\\n  --output_dir OUTPUT_DIR\\n                        Output directory for checkpoints and reports\\n  --epochs EPOCHS\\n  --batch_size BATCH_SIZE\\n  --eval_batch_size EVAL_BATCH_SIZE\\n  --lr LR\\n  --lora_r LORA_R\\n  --lora_alpha LORA_ALPHA\\n  --lora_dropout LORA_DROPOUT\\n  --max_seq_len MAX_SEQ_LEN\\n  --gpu_id GPU_ID\\n  --wandb_project WANDB_PROJECT\\n  --seed SEED\\n  --eval_split EVAL_SPLIT\\n  --warmup_ratio WARMUP_RATIO\\n  --weight_decay WEIGHT_DECAY\\n  --early_stopping_patience EARLY_STOPPING_PATIENCE\\n  --dry_run             Only validate imports and args, skip training\\n  --class_weights CLASS_
…[truncated 486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T20:23:17.367578+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/simgate-modular-routing && python src/router_sft_train.py --dry_run --class_weights auto --upsample_minority --min_internal_samples 5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/simgate-modular-routing && python src/router_sft_train.py --dry_run --class_weights auto --upsample_minority --min_internal_samples 5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T20:23:17.367700+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Dry run: imports OK, args parsed successfully.\\n  model_name:            Qwen/Qwen3-1.7B\\n  data_dir:              results/plan_c/\\n  output_dir:            results/router_sft/\\n  class_weights:         auto\\n  min_internal_samples:  5\\n  upsample_minority:     True\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_router-sft-class-weight_20260513T200820",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T20:23:17.367861+00:00_

完成。修改摘要：

**新增参数**（向后兼容，所有默认值保持原行为）：
- `--class_weights`: `"auto"`（inverse frequency: `N_total / (num_classes * N_c)`）或手动 `"w0,w1"`，传入 `CrossEntropyLoss(weight=...)`
- `--min_internal_samples 10`: internal 样本低于阈值时打印 WARNING
- `--upsample_minority`: 启用 `WeightedRandomSampler`（per-sample weight = `1/class_count`）

**新增组件**：
- `compute_class_weights()` — 计算 class weights
- `WeightedCETrainer(Trainer)` — 自定义 Trainer，重写 `compute_loss`（加权 CE）和 `get_train_dataloader`（可选 sampler）
- W&B 日志中记录 `class_weights_values`、`train_label_counts`、`upsample_minority`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_router-sft-class-weight_20260513T200820"
}
```

</details>

---
