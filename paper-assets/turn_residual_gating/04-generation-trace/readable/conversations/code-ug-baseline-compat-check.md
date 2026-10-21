# code ug baseline compat check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_code_ug_baseline_compat_check_20260518T192003.jsonl`
- **Structured JSON:** [`1339a00794f31e3e6908.json`](../../sessions/13/1339a00794f31e3e6908.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-18T19:21:17.287488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/threadgate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/threadgate.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T19:21:17.287943+00:00_

1	import torch
2	import torch.nn as nn
3	from transformers import AutoModelForCausalLM, AutoTokenizer
4	
5	from config import (
6	    MODEL_NAME,
7	    LORA_RANK,
8	    GATE_HIDDEN_DIM,
9	    MAX_TURN_DISTANCE,
10	    TURN_EMBED_DIM,
11	)
12	
13	
14	class TurnEmbedding(nn.Module):
15	
16	    def __init__(self):
17	        super().__init__()
18	        half_dim = TURN_EMBED_DIM // 2
19	        num_buckets = MAX_TURN_DISTANCE + 1
20	        self.distance_embed = nn.Embedding(num_buckets, half_dim)
21	        self.index_embed = nn.Embedding(num_buckets, half_dim)
22	
23	    def forward(self, turn_distance, turn_index):
24	        td = turn_distance.clamp(0, MAX_TURN_DISTANCE)
25	        ti = turn_index.clamp(0, MAX_TURN_DISTANCE)
26	        return torch.cat([self.distance_embed(td), self.index_embed(ti)], dim=-1)
27	
28	
29	class GateNetwork(nn.Module):
30	
31	    def __init__(self, hidden_dim, turn_embedding, init_bias=5.0):
32	        super().__init__()
33	        self.down_proj = nn.Linear(hidden_dim, LORA_RANK, bias=False)
34	        self.turn_embedding = turn_embedding
35	        self.fc1 = nn.Linear(LORA_RANK + TURN_EMBED_DIM, GATE_HIDDEN_DIM)
36	        self.fc2 = nn.Linear(GATE_HIDDEN_DIM, 1)
37	        self.fc2.bias.data.fill_(init_bias)
38	
39	    def forward(self, hidden_state, turn_features):
40	        down = self.down_proj(hidden_state)
41	        turn_emb = self.turn_embedding(
42	            turn_features["turn_distance"],
43	            turn_features["turn_index"],
44	        )
45	        while turn_emb.dim() < down.dim():
46	            turn_emb = turn_emb.unsqueeze(0)
47	        if turn_emb.shape[0] == 1 and down.shape[0] > 1:
48	            turn_emb = turn_emb.expand(down.shape[0], -1, -1)
49	        combined = torch.cat([down, turn_emb], dim=-1)
50	        return torch.sigmoid(self.fc2(torch.relu(self.fc1(combined))))
51	
52	
53	class UniformGateNetwork(nn.Module):
54	
55	    def __init__(self, hidden_dim, init_bias=5.0):
56	        super().__init_
…[truncated 5028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:21:17.288157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/train_phase2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/train_phase2.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T19:21:17.288477+00:00_

1	import argparse
2	import os
3	import sys
4	import json
5	import time
6	import random
7	
8	import torch
9	import torch.nn.functional as F
10	import numpy as np
11	from torch.optim import AdamW
12	from torch.utils.data import DataLoader, Dataset
13	from transformers import AutoTokenizer, get_cosine_schedule_with_warmup
14	from peft import LoraConfig, get_peft_model
15	from datasets import load_from_disk
16	
17	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
18	from threadgate import ThreadGatedModel
19	from gar import GARMeasurer, compute_gar_loss
20	from turn_utils import detect_turn_boundaries, build_turn_features
21	from config import (
22	    MODEL_NAME, LORA_RANK, GAR_EPSILON, GAR_LAMBDA, LEARNING_RATE,
23	    BATCH_SIZE, GRADIENT_ACCUMULATION, MAX_SEQ_LEN, NUM_EPOCHS, SEED,
24	    INIT_BIAS, GAR_LOSS_MODE, GAR_TARGET, LAMBDA_GATE_DIV, MIN_GATE_STD,
25	)
26	
27	
28	def set_seed(seed):
29	    random.seed(seed)
30	    np.random.seed(seed)
31	    torch.manual_seed(seed)
32	    torch.cuda.manual_seed_all(seed)
33	
34	
35	class MultiTurnDataset(Dataset):
36	    def __init__(self, data_path, tokenizer, max_seq_len=2048):
37	        self.ds = load_from_disk(data_path)
38	        self.tokenizer = tokenizer
39	        self.max_seq_len = max_seq_len
40	
41	    def __len__(self):
42	        return len(self.ds)
43	
44	    def __getitem__(self, idx):
45	        messages = self.ds[idx]["messages"]
46	        text = self.tokenizer.apply_chat_template(messages, tokenize=False)
47	        encoding = self.tokenizer(
48	            text, truncation=True, max_length=self.max_seq_len, return_tensors="pt"
49	        )
50	        input_ids = encoding.input_ids.squeeze(0)
51	
52	        boundaries = detect_turn_boundaries(input_ids, self.tokenizer)
53	        turn_feats = build_turn_features(input_ids, self.tokenizer)
54	
55	        labels = input_ids.clone()
56	        labels[:] = -100
57	        for turn in boundaries["turns"]:
58	            if turn["role"] == "assis
…[truncated 14020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:21:17.288682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/gar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/gar.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:21:17.288877+00:00_

1	import warnings
2	from contextlib import contextmanager
3	
4	import torch
5	import torch.nn.functional as F
6	import numpy as np
7	
8	
9	class GARMeasurer:
10	    def __init__(self, model, measure_only=True):
11	        self.model = model
12	        self.measure_only = measure_only
13	        self._hooks = []
14	        self._attention_weights = {}
15	        self._active = False
16	
17	        self._attn_layers = []
18	        for i, layer in enumerate(model.model.layers):
19	            self._attn_layers.append((i, layer.self_attn))
20	        self.num_layers = len(self._attn_layers)
21	
22	        attn_impl = getattr(model.config, "_attn_implementation", None)
23	        if attn_impl and attn_impl != "eager":
24	            warnings.warn(
25	                f"attn_implementation={attn_impl!r} does not return attention weights. "
26	                f"Load model with attn_implementation='eager' for GAR measurement.",
27	                stacklevel=2,
28	            )
29	
30	    def _make_hook(self, layer_idx):
31	        def hook_fn(module, input, output):
32	            if isinstance(output, tuple) and len(output) > 1 and output[1] is not None:
33	                attn_w = output[1]
34	                if self.measure_only:
35	                    attn_w = attn_w.detach().float()
36	                else:
37	                    attn_w = attn_w.float()
38	                self._attention_weights[layer_idx] = attn_w
39	        return hook_fn
40	
41	    @contextmanager
42	    def measure(self):
43	        """Caller must pass output_attentions=True to model.forward() inside this context."""
44	        self._attention_weights = {}
45	        self._hooks = []
46	        self._active = True
47	
48	        try:
49	            for layer_idx, attn_module in self._attn_layers:
50	                h = attn_module.register_forward_hook(self._make_hook(layer_idx))
51	                self._hooks.append(h)
52	            yield self
53	        finally:
54	            for h in self._hoo
…[truncated 6245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T19:21:17.289076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/src/config.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T19:21:17.289211+00:00_

1	MODEL_NAME = "/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct"
2	LORA_RANK = 16
3	GATE_HIDDEN_DIM = 64
4	MAX_TURN_DISTANCE = 32
5	TURN_EMBED_DIM = 16
6	GAR_EPSILON = 0.001
7	GAR_LAMBDA = 2.0
8	LEARNING_RATE = 2e-4
9	BATCH_SIZE = 1
10	GRADIENT_ACCUMULATION = 8
11	MAX_SEQ_LEN = 2048
12	NUM_EPOCHS = 3
13	SEED = 42
14	INIT_BIAS = 2.0
15	GAR_LOSS_MODE = "mse_target"
16	GAR_TARGET = 0.5
17	LAMBDA_GATE_DIV = 1.0
18	MIN_GATE_STD = 0.05
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T19:21:17.289342+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.sh",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.sh",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T19:21:17.289503+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T19:21:17.289656+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "train_phase2|v7|training command",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "glob": "*.md",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "tool_args": {
    "pattern": "train_phase2|v7|training command",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
    "glob": "*.md",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:21:17.289778+00:00_

Found 4 files
ROADMAP.md
memory.md
report.md
artifacts/_project/intermediate/diagnose_gar_loss_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T19:21:17.289894+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "train_phase2.*v7|v7.*train|--gate-type|--gar-loss-mode|--lambda-gate-div\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/memory.md",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "tool_args": {
    "pattern": "train_phase2.*v7|v7.*train|--gate-type|--gar-loss-mode|--lambda-gate-div\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/memory.md",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T19:21:17.290010+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T19:21:17.290122+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "v7|train_phase2|--gar-loss-mode|--lambda-gate-div\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md",
  "output_mode": "content",
  "-C": "5",
  "head_limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "tool_args": {
    "pattern": "v7|train_phase2|--gar-loss-mode|--lambda-gate-div\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md",
    "output_mode": "content",
    "-C": "5",
    "head_limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:21:17.290243+00:00_

3-> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4-
5-## 运行中
6-| exp_id | 假设 | 状态 | 关键指标 | W&B |
7-|--------|------|------|---------|-----|
8:| phase2_tg_s42_v7 | MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。 | — | — | — |
9-
10-## 待处理
11-- phase2_ug_s42: Uniform Gate (无 turn conditioning) 作为消融 baseline，在相同 L_NTP+L_GAR 训练下 mid-turn GAR recovery 应低于 ThreadGate ≥3pp，因为 uniform gating 无法选择性恢复 turn boundary 处的 GAR（准备中）
12-
13-## 近期结论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T19:21:17.290368+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "phase2_tg_s42_v7|v7.*command|python.*train_phase2\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "output_mode": "content",
  "-C": "5",
  "glob": "*.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "tool_args": {
    "pattern": "phase2_tg_s42_v7|v7.*command|python.*train_phase2\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
    "output_mode": "content",
    "-C": "5",
    "glob": "*.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T19:21:17.290545+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-57-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-58-## 关键决策日志
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-59-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-60-| ID | 日期 | 摘要 | 关联实验 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-61-|----|------|------|----------|
ROADMAP.md:62:| D011 | 2026-05-18 | v7 gs200 达到 MVP Phase 2 关键里程碑：GAR 收敛到 target (0.48 | phase2_tg_s42_v7 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-63-| D010 | 2026-05-18 | Kill v6（smooth_saturation 未解决恒等退化），v7 改用 MSE(GAR,  | phase2_tg_s42_v6 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-64-| D009 | 2026-05-18 | Kill v5（maximize 模式 gate 分化失败确认），启动 v6 smooth_satu | phase2_tg_s42_v5 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-65-| D008 | 2026-05-18 | v5 复现 v3b 退化模式（总 loss 转负、gate 趋向 identity），确认 maxi | phase2_tg_s42_v5, phase2_tg_s42_v3b |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-66-| D007 | 2026-05-18 | L4/L5 gate-Dongre 对齐 claim 从 "perfect alignment" 降 | phase2_tg_s42_v3b, phase2_tg_s42_v4 |
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md-67-| D006 | 2026-05-18 | Dongre et al. (2605.12922) 发现后 framing 调整方向：从"发现+解 | phase2_tg_s42_v3b |
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-3-> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-4-
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md-5-## 运行中
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_res
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-18T19:21:17.290753+00:00_

## 检查结果

### 1. Uniform gate 兼容 v7 新 loss？**是，完全兼容。**

三个关键点全部通过：

**`get_gate_values(with_grad=True)`** — 兼容。这个方法定义在 `ThreadGatedModel` 上（threadgate.py:157-160），返回 `self._gate_values_with_grad`。该字典在 `_make_hook`（line 130-131）中对**两种 gate type 都会填充**：hook 通过 `self.gate_type` 分支调用对应 gate network（line 123-126），但无论走哪个分支，都执行 `self._gate_values_with_grad[layer_idx] = gate`。

**Gate diversity loss** — 兼容。train_phase2.py:259-266 只遍历 `gate_values_grad` 字典算 `per_layer_means` 的 std，不区分 gate type。UniformGateNetwork 的 gate 值同样有层间差异（每层独立的 `constant_vector` + `fc1/fc2`），diversity loss 正常工作。

**`mse_target` GAR loss** — 兼容。gar.py:196-204 只依赖 `gar_per_turn` 的 tensor 值，与 gate type 完全无关。

### 2. 无需修改

代码路径完整，没有遗漏的条件分支。

### 3. UG baseline 训练命令

config.py 的默认值已经是 v7 参数（`mse_target`, `lambda_gate_div=1.0`, `min_gate_std=0.05`），所以只需改 `--gate-type` 和 `--output-dir`：

```bash
cd /root/turn_residual_gating && python src/train_phase2.py \
  --gate-type uniform \
  --output-dir /root/turn_residual_gating/checkpoints/phase2_ug_s42 \
  --gar-loss-mode mse_target \
  --gar-target 0.5 \
  --lambda-gar 2.0 \
  --lambda-gate-div 1.0 \
  --min-gate-std 0.05 \
  --init-bias 2.0 \
  --lr 2e-4 \
  --grad-accum 8 \
  --epochs 3 \
  --seed 42
```

（显式写出所有参数确保与 v7 TG 实验完全对齐，虽然这些都是 config.py 默认值。）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_ug_baseline_compat_check_20260518T192003"
}
```

</details>

---
