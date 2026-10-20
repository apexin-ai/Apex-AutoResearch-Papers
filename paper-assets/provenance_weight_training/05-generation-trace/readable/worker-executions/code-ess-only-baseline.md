# code ess only baseline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_code_ess_only_baseline_20260515T071521.log`
- **Structured JSON:** [`96a3763de7a82bd0cd74.json`](../../sessions/96/96a3763de7a82bd0cd74.json)

## Before a recorded user message

63 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "59ea9c77-1214-44ea-b1a6-a7990f498c53",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1778841000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8d658c13-b623-4103-99fc-b9be2c027b78",
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the main file to understand the current implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "48a58f5b-8801-49c0-869d-e613dba978fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wYuxQZ4qn8DDcYsc6RBAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
      },
      "output_tokens": 32,
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

先读取 `pretrain_weighted.py` 理解现有逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "92a41f83-4a84-45ef-bcb1-8be690bfb837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wYuxQZ4qn8DDcYsc6RBAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
      },
      "output_tokens": 32,
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

<details open><summary>🔧 Tool call — Read · `toolu_015xUWdw4GDdmJ96on2sCgb7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training/pretrain_weighted.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "aa4435f3-ec24-40aa-994f-90ad3bc03c72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wYuxQZ4qn8DDcYsc6RBAc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
      },
      "output_tokens": 32,
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

_source line 7 · 2026-05-15T07:15:34.226Z_

<details><summary>↩ Tool result · reported error · `toolu_015xUWdw4GDdmJ96on2sCgb7`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "8a536879-845f-4bd5-bcac-cd837e482c09",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training."
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01SPDAyQjzfDgtvabNC3wmtH`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "401d379f-0f25-40e9-86de-23014096883a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FR3CqkwJjTnTXCZfPHnofL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
      },
      "output_tokens": 55,
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

_source line 9 · 2026-05-15T07:15:37.564Z_

<details><summary>↩ Tool result · `toolu_01SPDAyQjzfDgtvabNC3wmtH`</summary>

```text
artifacts/weighting/__init__.py
artifacts/weighting/alpha_eff.py
artifacts/detector/train_detector.py
artifacts/evaluation/eval_pipeline.py
artifacts/evaluation/compare_results.py
artifacts/data_generation/generate_synthetic.py
auto_eval_watcher.py
artifacts/training/extract_train_metrics.py
analyze_mvp.py
artifacts/training/pretrain_weighted.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "72910baf-1535-422a-97d1-a7e3d246e3d3",
  "tool_use_result": {
    "filenames": [
      "artifacts/weighting/__init__.py",
      "artifacts/weighting/alpha_eff.py",
      "artifacts/detector/train_detector.py",
      "artifacts/evaluation/eval_pipeline.py",
      "artifacts/evaluation/compare_results.py",
      "artifacts/data_generation/generate_synthetic.py",
      "auto_eval_watcher.py",
      "artifacts/training/extract_train_metrics.py",
      "analyze_mvp.py",
      "artifacts/training/pretrain_weighted.py"
    ],
    "durationMs": 32,
    "numFiles": 10,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01WKuequJrpHAgrPc47vn3Hc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "2db3aa69-9182-41d7-a177-01e257a76f45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxLjUEy87jTL8QRUA4Jmjg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 24114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
      },
      "output_tokens": 60,
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

_source line 11 · 2026-05-15T07:15:39.522Z_

<details><summary>↩ Tool result · `toolu_01WKuequJrpHAgrPc47vn3Hc`</summary>

```text
1	"""Weighted pretraining for Qwen3-0.6B on contaminated corpora.
2	
3	Supports three weighting methods:
4	  - uniform:  all samples equally weighted (baseline)
5	  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run
6	               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.
7	  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)
8	
9	Data format: jsonl with {"text": "...", "q_score": 0.xx, "label": "human"/"synthetic"}
10	"""
11	
12	import argparse
13	import json
14	import math
15	import os
16	import sys
17	import time
18	from pathlib import Path
19	
20	import torch
21	from torch.utils.data import Dataset
22	from transformers import (
23	    AutoModelForCausalLM,
24	    AutoTokenizer,
25	    Trainer,
26	    TrainingArguments,
27	    set_seed,
28	)
29	
30	sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
31	from weighting.alpha_eff import (
32	    compute_alpha_eff,
33	    compute_ess,
34	    compute_sample_weights,
35	    find_optimal_b,
36	)
37	
38	
39	GRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
40	
41	
42	class WeightedTextDataset(Dataset):
43	    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):
44	        self.tokenizer = tokenizer
45	        self.max_length = max_length
46	        self.examples = []
47	
48	        with open(data_path, "r") as f:
49	            for line in f:
50	                line = line.strip()
51	                if not line:
52	                    continue
53	                item = json.loads(line)
54	                self.examples.append(item)
55	
56	    def __len__(self):
57	        return len(self.examples)
58	
59	    def __getitem__(self, idx):
60	        item = self.examples[idx]
61	        encoding = self.tokenizer(
62	            item["text"],
63	            truncation=True,
64	            max_length=self.max_length,
65	            padding="max_length",
66	            return_tensors="pt",
67	        )
68	        input_ids = encoding["input_ids"].squeeze(0)
69	        attention_mask = encoding["attention_mask"].squeeze(0)
70	        return {
71	            "input_ids": input_ids,
72	            "attention_mask": attention_mask,
73	            "labels": input_ids.clone(),
74	            "q_score": item.get("q_score", 0.0),
75	        }
76	
77	
78	def collate_fn(batch):
79	    input_ids = torch.stack([x["input_ids"] for x in batch])
80	    attention_mask = torch.stack([x["attention_mask"] for x in batch])
81	    labels = torch.stack([x["labels"] for x in batch])
82	    q_scores = torch.tensor([x["q_score"] for x in batch], dtype=torch.float32)
83	    return {
84	        "input_ids": input_ids,
85	        "attention_mask": attention_mask,
86	        "labels": labels,
87	        "q_scores": q_scores,
88	    }
89	
90	
91	class WeightedTrainer(Trainer):
92	    def __init__(self, weighting_method: str, tau: float, n_min: int,
93	                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):
94	        super().__init__(**kwargs)
95	        self.weighting_method = weighting_method
96	        self.tau = tau
97	        self.n_min = n_min
98	        self.grid_b_value = grid_b_value
99	        self.log_path = log_path
100	        self._step_metrics = []
101	
102	    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
103	        q_scores = inputs.pop("q_scores")
104	        labels = inputs.get("labels")
105	
106	        outputs = model(**inputs)
107	        logits = outputs.logits
108	
109	        shift_logits = logits[..., :-1, :].contiguous()
110	        shift_labels = labels[..., 1:].contiguous()
111	        attention_mask = inputs.get("attention_mask")
112	        if attention_mask is not None:
113	            shift_mask = attention_mask[..., 1:].contiguous()
114	        else:
115	            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)
116	
117	        loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
118	        per_token_loss = loss_fct(
119	            shift_logits.view(-1, shift_logits.size(-1)),
120	            shift_labels.view(-1),
121	        ).view(shift_labels.size())
122	
123	        # Mask padding tokens
124	        per_token_loss = per_token_loss * shift_mask
125	
126	        # Per-sample loss: mean over tokens
127	        token_counts = shift_mask.sum(dim=-1).clamp(min=1)
128	        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts
129	
130	        unweighted_loss = per_sample_loss.mean()
131	
132	        b_val = 0.0
133	        alpha_val = compute_alpha_eff(q_scores, 0.0)
134	        ess_val = float(q_scores.numel())
135	
136	        if self.weighting_method == "uniform":
137	            loss = unweighted_loss
138	        elif self.weighting_method == "grid":
139	            b_val = self.grid_b_value
140	            weights = compute_sample_weights(q_scores, b_val)
141	            weights = weights.to(per_sample_loss.device)
142	            loss = (per_sample_loss * weights).sum() / weights.sum()
143	            alpha_val = compute_alpha_eff(q_scores, b_val)
144	            ess_val = compute_ess(q_scores, b_val)
145	        elif self.weighting_method == "adaptive":
146	            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)
147	            weights = compute_sample_weights(q_scores, b_val)
148	            weights = weights.to(per_sample_loss.device)
149	            loss = (per_sample_loss * weights).sum() / weights.sum()
150	            alpha_val = compute_alpha_eff(q_scores, b_val)
151	            ess_val = compute_ess(q_scores, b_val)
152	        else:
153	            raise ValueError(f"Unknown weighting method: {self.weighting_method}")
154	
155	        if model.training:
156	            step_info = {
157	                "step": self.state.global_step if self.state else 0,
158	                "loss": float(loss.detach()),
159	                "unweighted_loss": float(unweighted_loss.detach()),
160	                "b": b_val,
161	                "alpha_eff": alpha_val,
162	                "ess": ess_val,
163	                "mean_q": float(q_scores.mean()),
164	                "method": self.weighting_method,
165	            }
166	            self._step_metrics.append(step_info)
167	
168	            if self.log_path and len(self._step_metrics) % 10 == 0:
169	                self._flush_metrics()
170	
171	        return (loss, outputs) if return_outputs else loss
172	
173	    def _flush_metrics(self):
174	        if not self._step_metrics or not self.log_path:
175	            return
176	        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
177	        with open(self.log_path, "a") as f:
178	            for m in self._step_metrics:
179	                f.write(json.dumps(m) + "\n")
180	        self._step_metrics = []
181	
182	    def training_step(self, model, inputs, num_items_in_batch=None):
183	        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)
184	
185	        if self._step_metrics:
186	            latest = self._step_metrics[-1]
187	            self.log({
188	                "weighting/b": latest["b"],
189	                "weighting/alpha_eff": latest["alpha_eff"],
190	                "weighting/ess": latest["ess"],
191	                "weighting/mean_q": latest["mean_q"],
192	                "weighting/unweighted_loss": latest["unweighted_loss"],
193	                "weighting/weighted_loss": latest["loss"],
194	            })
195	
196	        return result
197	
198	    def save_model(self, output_dir=None, _internal_call=False):
199	        super().save_model(output_dir, _internal_call)
200	        self._flush_metrics()
201	
202	
203	def parse_args():
204	    parser = argparse.ArgumentParser(
205	        description="Weighted pretraining for LMs on contaminated corpora"
206	    )
207	    parser.add_argument("--data_path", type=str, required=True,
208	                        help="Path to training data (jsonl)")
209	    parser.add_argument("--output_dir", type=str, required=True,
210	                        help="Output directory for checkpoints and logs")
211	    parser.add_argument("--model_name", type=str, default="Qwen/Qwen3-0.6B",
212	                        help="HuggingFace model name or path")
213	    parser.add_argument("--weighting_method", type=str, default="adaptive",
214	                        choices=["uniform", "grid", "adaptive"],
215	                        help="Weighting method: uniform / grid / adaptive")
216	    parser.add_argument("--grid_b_value", type=float, default=1.0,
217	                        help="Fixed b value for grid method (one run per b, "
218	                             "grid search selects best across runs)")
219	    parser.add_argument("--contamination_ratio", type=float, default=0.2,
220	                        help="Expected contamination ratio (for adaptive tau)")
221	    parser.add_argument("--num_train_tokens", type=int, default=None,
222	                        help="Total training tokens (converted to max_steps)")
223	    parser.add_argument("--max_steps", type=int, default=-1,
224	                        help="Max training steps (overrides num_train_tokens)")
225	    parser.add_argument("--num_train_epochs", type=float, default=1.0,
226	                        help="Number of training epochs")
227	    parser.add_argument("--batch_size", type=int, default=4,
228	                        help="Per-device training batch size")
229	    parser.add_argument("--gradient_accumulation_steps", type=int, default=4,
230	                        help="Gradient accumulation steps")
231	    parser.add_argument("--learning_rate", type=float, default=5e-5,
232	                        help="Learning rate")
233	    parser.add_argument("--max_length", type=int, default=2048,
234	                        help="Max sequence length")
235	    parser.add_argument("--tau", type=float, default=None,
236	                        help="Alpha_eff target threshold (adaptive). "
237	                             "Defaults to 1 - contamination_ratio * 0.5")
238	    parser.add_argument("--n_min", type=int, default=None,
239	                        help="Minimum effective sample size. "
240	                             "Defaults to batch_size // 2")
241	    parser.add_argument("--use_wandb", action="store_true",
242	                        help="Enable Weights & Biases logging")
243	    parser.add_argument("--wandb_project", type=str,
244	                        default="provenance-weight-training",
245	                        help="W&B project name")
246	    parser.add_argument("--wandb_run_name", type=str, default=None,
247	                        help="W&B run name (passed to TrainingArguments.run_name)")
248	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
249	    parser.add_argument("--eval_data_path", type=str, default=None,
250	                        help="Path to evaluation data (jsonl)")
251	    parser.add_argument("--eval_steps", type=int, default=500,
252	                        help="Evaluate every N steps")
253	    parser.add_argument("--save_steps", type=int, default=500,
254	                        help="Save checkpoint every N steps")
255	    parser.add_argument("--logging_steps", type=int, default=10,
256	                        help="Log every N steps")
257	    parser.add_argument("--warmup_ratio", type=float, default=0.05,
258	                        help="Warmup ratio")
259	    parser.add_argument("--weight_decay", type=float, default=0.01,
260	                        help="Weight decay")
261	    parser.add_argument("--save_total_limit", type=int, default=3,
262	                        help="Keep only N most recent checkpoints")
263	    parser.add_argument("--save_only_model", action="store_true",
264	                        help="Save only model weights (skip optimizer/scheduler/rng)")
265	    parser.add_argument("--resume_from_checkpoint", type=str, default=None,
266	                        help="Path to checkpoint directory to resume from")
267	    parser.add_argument("--bf16", action="store_true", default=True,
268	                        help="Use bfloat16 (default: True)")
269	    parser.add_argument("--no_bf16", action="store_true",
270	                        help="Disable bfloat16")
271	    return parser.parse_args()
272	
273	
274	def main():
275	    args = parse_args()
276	    set_seed(args.seed)
277	
278	    if args.tau is None:
279	        args.tau = 1.0 - args.contamination_ratio * 0.5
280	    if args.n_min is None:
281	        args.n_min = max(2, args.batch_size // 2)
282	
283	    use_bf16 = args.bf16 and not args.no_bf16
284	
285	    report_to = []
286	    if args.use_wandb:
287	        report_to.append("wandb")
288	        os.environ.setdefault("WANDB_PROJECT", args.wandb_project)
289	
290	    print(f"Loading tokenizer: {args.model_name}")
291	    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
292	    if tokenizer.pad_token is None:
293	        tokenizer.pad_token = tokenizer.eos_token
294	
295	    print(f"Loading model: {args.model_name}")
296	    model = AutoModelForCausalLM.from_pretrained(
297	        args.model_name,
298	        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,
299	        trust_remote_code=True,
300	    )
301	
302	    print(f"Loading training data: {args.data_path}")
303	    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)
304	    print(f"  {len(train_dataset)} examples loaded")
305	
306	    eval_dataset = None
307	    if args.eval_data_path:
308	        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)
309	        print(f"  {len(eval_dataset)} eval examples loaded")
310	
311	    # Convert num_train_tokens to max_steps
312	    max_steps = args.max_steps
313	    if max_steps <= 0 and args.num_train_tokens is not None:
314	        tokens_per_step = (
315	            args.batch_size * args.gradient_accumulation_steps * args.max_length
316	        )
317	        max_steps = args.num_train_tokens // tokens_per_step
318	        print(f"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}")
319	
320	    log_path = os.path.join(args.output_dir, "step_metrics.jsonl")
321	
322	    training_args = TrainingArguments(
323	        output_dir=args.output_dir,
324	        run_name=args.wandb_run_name,
325	        per_device_train_batch_size=args.batch_size,
326	        gradient_accumulation_steps=args.gradient_accumulation_steps,
327	        learning_rate=args.learning_rate,
328	        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,
329	        max_steps=max_steps if max_steps > 0 else -1,
330	        warmup_ratio=args.warmup_ratio,
331	        weight_decay=args.weight_decay,
332	        bf16=use_bf16,
333	        logging_steps=args.logging_steps,
334	        eval_steps=args.eval_steps if eval_dataset else None,
335	        eval_strategy="steps" if eval_dataset else "no",
336	        save_steps=args.save_steps,
337	        save_strategy="steps",
338	        save_total_limit=args.save_total_limit,
339	        save_only_model=args.save_only_model,
340	        load_best_model_at_end=eval_dataset is not None,
341	        metric_for_best_model="eval_loss" if eval_dataset else None,
342	        report_to=report_to if report_to else "none",
343	        seed=args.seed,
344	        dataloader_drop_last=True,
345	        remove_unused_columns=False,
346	    )
347	
348	    trainer = WeightedTrainer(
349	        weighting_method=args.weighting_method,
350	        tau=args.tau,
351	        n_min=args.n_min,
352	        grid_b_value=args.grid_b_value,
353	        log_path=log_path,
354	        model=model,
355	        args=training_args,
356	        train_dataset=train_dataset,
357	        eval_dataset=eval_dataset,
358	        data_collator=collate_fn,
359	        tokenizer=tokenizer,
360	    )
361	
362	    config_summary = {
363	        "model_name": args.model_name,
364	        "weighting_method": args.weighting_method,
365	        "grid_b_value": args.grid_b_value if args.weighting_method == "grid" else None,
366	        "tau": args.tau,
367	        "n_min": args.n_min,
368	        "contamination_ratio": args.contamination_ratio,
369	        "batch_size": args.batch_size,
370	        "learning_rate": args.learning_rate,
371	        "max_steps": max_steps,
372	        "seed": args.seed,
373	        "num_examples": len(train_dataset),
374	    }
375	    print("\n=== Training Config ===")
376	    for k, v in config_summary.items():
377	        print(f"  {k}: {v}")
378	    print()
379	
380	    os.makedirs(args.output_dir, exist_ok=True)
381	    with open(os.path.join(args.output_dir, "config.json"), "w") as f:
382	        json.dump(config_summary, f, indent=2)
383	
384	    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)
385	    trainer._flush_metrics()
386	    trainer.save_model(os.path.join(args.output_dir, "final"))
387	    print(f"\nTraining complete. Model saved to {args.output_dir}/final")
388	
389	
390	if __name__ == "__main__":
391	    main()
392	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "de26fb4a-3cf0-407e-8150-a86738b0b47c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
      "content": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports three weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom torch.utils.data import Dataset\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    Trainer,\n    TrainingArguments,\n    set_seed,\n)\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\"))\nfrom weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_optimal_b,\n)\n\n\nGRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]\n\n\nclass WeightedTextDataset(Dataset):\n    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n        self.examples = []\n\n        with open(data_path, \"r\") as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                item = json.loads(line)\n                self.examples.append(item)\n\n    def __len__(self):\n        return len(self.examples)\n\n    def __getitem__(self, idx):\n        item = self.examples[idx]\n        encoding = self.tokenizer(\n            item[\"text\"],\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        input_ids = encoding[\"input_ids\"].squeeze(0)\n        attention_mask = encoding[\"attention_mask\"].squeeze(0)\n        return {\n            \"input_ids\": input_ids,\n            \"attention_mask\": attention_mask,\n            \"labels\": input_ids.clone(),\n            \"q_score\": item.get(\"q_score\", 0.0),\n        }\n\n\ndef collate_fn(batch):\n    input_ids = torch.stack([x[\"input_ids\"] for x in batch])\n    attention_mask = torch.stack([x[\"attention_mask\"] for x in batch])\n    labels = torch.stack([x[\"labels\"] for x in batch])\n    q_scores = torch.tensor([x[\"q_score\"] for x in batch], dtype=torch.float32)\n    return {\n        \"input_ids\": input_ids,\n        \"attention_mask\": attention_mask,\n        \"labels\": labels,\n        \"q_scores\": q_scores,\n    }\n\n\nclass WeightedTrainer(Trainer):\n    def __init__(self, weighting_method: str, tau: float, n_min: int,\n                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):\n        super().__init__(**kwargs)\n        self.weighting_method = weighting_method\n        self.tau = tau\n        self.n_min = n_min\n        self.grid_b_value = grid_b_value\n        self.log_path = log_path\n        self._step_metrics = []\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        q_scores = inputs.pop(\"q_scores\")\n        labels = inputs.get(\"labels\")\n\n        outputs = model(**inputs)\n        logits = outputs.logits\n\n        shift_logits = logits[..., :-1, :].contiguous()\n        shift_labels = labels[..., 1:].contiguous()\n        attention_mask = inputs.get(\"attention_mask\")\n        if attention_mask is not None:\n            shift_mask = attention_mask[..., 1:].contiguous()\n        else:\n            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)\n\n        loss_fct = torch.nn.CrossEntropyLoss(reduction=\"none\")\n        per_token_loss = loss_fct(\n            shift_logits.view(-1, shift_logits.size(-1)),\n            shift_labels.view(-1),\n        ).view(shift_labels.size())\n\n        # Mask padding tokens\n        per_token_loss = per_token_loss * shift_mask\n\n        # Per-sample loss: mean over tokens\n        token_counts = shift_mask.sum(dim=-1).clamp(min=1)\n        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts\n\n        unweighted_loss = per_sample_loss.mean()\n\n        b_val = 0.0\n        alpha_val = compute_alpha_eff(q_scores, 0.0)\n        ess_val = float(q_scores.numel())\n\n        if self.weighting_method == \"uniform\":\n            loss = unweighted_loss\n        elif self.weighting_method == \"grid\":\n            b_val = self.grid_b_value\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:\n            raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")\n\n        if model.training:\n            step_info = {\n                \"step\": self.state.global_step if self.state else 0,\n                \"loss\": float(loss.detach()),\n                \"unweighted_loss\": float(unweighted_loss.detach()),\n                \"b\": b_val,\n                \"alpha_eff\": alpha_val,\n                \"ess\": ess_val,\n                \"mean_q\": float(q_scores.mean()),\n                \"method\": self.weighting_method,\n            }\n            self._step_metrics.append(step_info)\n\n            if self.log_path and len(self._step_metrics) % 10 == 0:\n                self._flush_metrics()\n\n        return (loss, outputs) if return_outputs else loss\n\n    def _flush_metrics(self):\n        if not self._step_metrics or not self.log_path:\n            return\n        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)\n        with open(self.log_path, \"a\") as f:\n            for m in self._step_metrics:\n                f.write(json.dumps(m) + \"\\n\")\n        self._step_metrics = []\n\n    def training_step(self, model, inputs, num_items_in_batch=None):\n        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)\n\n        if self._step_metrics:\n            latest = self._step_metrics[-1]\n            self.log({\n                \"weighting/b\": latest[\"b\"],\n                \"weighting/alpha_eff\": latest[\"alpha_eff\"],\n                \"weighting/ess\": latest[\"ess\"],\n                \"weighting/mean_q\": latest[\"mean_q\"],\n                \"weighting/unweighted_loss\": latest[\"unweighted_loss\"],\n                \"weighting/weighted_loss\": latest[\"loss\"],\n            })\n\n        return result\n\n    def save_model(self, output_dir=None, _internal_call=False):\n        super().save_model(output_dir, _internal_call)\n        self._flush_metrics()\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Weighted pretraining for LMs on contaminated corpora\"\n    )\n    parser.add_argument(\"--data_path\", type=str, required=True,\n                        help=\"Path to training data (jsonl)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for checkpoints and logs\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-0.6B\",\n                        help=\"HuggingFace model name or path\")\n    parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",\n                        choices=[\"uniform\", \"grid\", \"adaptive\"],\n                        help=\"Weighting method: uniform / grid / adaptive\")\n    parser.add_argument(\"--grid_b_value\", type=float, default=1.0,\n                        help=\"Fixed b value for grid method (one run per b, \"\n                             \"grid search selects best across runs)\")\n    parser.add_argument(\"--contamination_ratio\", type=float, default=0.2,\n                        help=\"Expected contamination ratio (for adaptive tau)\")\n    parser.add_argument(\"--num_train_tokens\", type=int, default=None,\n                        help=\"Total training tokens (converted to max_steps)\")\n    parser.add_argument(\"--max_steps\", type=int, default=-1,\n                        help=\"Max training steps (overrides num_train_tokens)\")\n    parser.add_argument(\"--num_train_epochs\", type=float, default=1.0,\n                        help=\"Number of training epochs\")\n    parser.add_argument(\"--batch_size\", type=int, default=4,\n                        help=\"Per-device training batch size\")\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=4,\n                        help=\"Gradient accumulation steps\")\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5,\n                        help=\"Learning rate\")\n    parser.add_argument(\"--max_length\", type=int, default=2048,\n                        help=\"Max sequence length\")\n    parser.add_argument(\"--tau\", type=float, default=None,\n                        help=\"Alpha_eff target threshold (adaptive). \"\n                             \"Defaults to 1 - contamination_ratio * 0.5\")\n    parser.add_argument(\"--n_min\", type=int, default=None,\n                        help=\"Minimum effective sample size. \"\n                             \"Defaults to batch_size // 2\")\n    parser.add_argument(\"--use_wandb\", action=\"store_true\",\n                        help=\"Enable Weights & Biases logging\")\n    parser.add_argument(\"--wandb_project\", type=str,\n                        default=\"provenance-weight-training\",\n                        help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None,\n                        help=\"W&B run name (passed to TrainingArguments.run_name)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--eval_data_path\", type=str, default=None,\n                        help=\"Path to evaluation data (jsonl)\")\n    parser.add_argument(\"--eval_steps\", type=int, default=500,\n                        help=\"Evaluate every N steps\")\n    parser.add_argument(\"--save_steps\", type=int, default=500,\n                        help=\"Save checkpoint every N steps\")\n    parser.add_argument(\"--logging_steps\", type=int, default=10,\n                        help=\"Log every N steps\")\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05,\n                        help=\"Warmup ratio\")\n    parser.add_argument(\"--weight_decay\", type=float, default=0.01,\n                        help=\"Weight decay\")\n    parser.add_argument(\"--save_total_limit\", type=int, default=3,\n                        help=\"Keep only N most recent checkpoints\")\n    parser.add_argument(\"--save_only_model\", action=\"store_true\",\n                        help=\"Save only model weights (skip optimizer/scheduler/rng)\")\n    parser.add_argument(\"--resume_from_checkpoint\", type=str, default=None,\n                        help=\"Path to checkpoint directory to resume from\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True,\n                        help=\"Use bfloat16 (default: True)\")\n    parser.add_argument(\"--no_bf16\", action=\"store_true\",\n                        help=\"Disable bfloat16\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n    set_seed(args.seed)\n\n    if args.tau is None:\n        args.tau = 1.0 - args.contamination_ratio * 0.5\n    if args.n_min is None:\n        args.n_min = max(2, args.batch_size // 2)\n\n    use_bf16 = args.bf16 and not args.no_bf16\n\n    report_to = []\n    if args.use_wandb:\n        report_to.append(\"wandb\")\n        os.environ.setdefault(\"WANDB_PROJECT\", args.wandb_project)\n\n    print(f\"Loading tokenizer: {args.model_name}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"Loading model: {args.model_name}\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name,\n        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,\n        trust_remote_code=True,\n    )\n\n    print(f\"Loading training data: {args.data_path}\")\n    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)\n    print(f\"  {len(train_dataset)} examples loaded\")\n\n    eval_dataset = None\n    if args.eval_data_path:\n        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)\n        print(f\"  {len(eval_dataset)} eval examples loaded\")\n\n    # Convert num_train_tokens to max_steps\n    max_steps = args.max_steps\n    if max_steps <= 0 and args.num_train_tokens is not None:\n        tokens_per_step = (\n            args.batch_size * args.gradient_accumulation_steps * args.max_length\n        )\n        max_steps = args.num_train_tokens // tokens_per_step\n        print(f\"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}\")\n\n    log_path = os.path.join(args.output_dir, \"step_metrics.jsonl\")\n\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        run_name=args.wandb_run_name,\n        per_device_train_batch_size=args.batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,\n        max_steps=max_steps if max_steps > 0 else -1,\n        warmup_ratio=args.warmup_ratio,\n        weight_decay=args.weight_decay,\n        bf16=use_bf16,\n        logging_steps=args.logging_steps,\n        eval_steps=args.eval_steps if eval_dataset else None,\n        eval_strategy=\"steps\" if eval_dataset else \"no\",\n        save_steps=args.save_steps,\n        save_strategy=\"steps\",\n        save_total_limit=args.save_total_limit,\n        save_only_model=args.save_only_model,\n        load_best_model_at_end=eval_dataset is not None,\n        metric_for_best_model=\"eval_loss\" if eval_dataset else None,\n        report_to=report_to if report_to else \"none\",\n        seed=args.seed,\n        dataloader_drop_last=True,\n        remove_unused_columns=False,\n    )\n\n    trainer = WeightedTrainer(\n        weighting_method=args.weighting_method,\n        tau=args.tau,\n        n_min=args.n_min,\n        grid_b_value=args.grid_b_value,\n        log_path=log_path,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        data_collator=collate_fn,\n        tokenizer=tokenizer,\n    )\n\n    config_summary = {\n        \"model_name\": args.model_name,\n        \"weighting_method\": args.weighting_method,\n        \"grid_b_value\": args.grid_b_value if args.weighting_method == \"grid\" else None,\n        \"tau\": args.tau,\n        \"n_min\": args.n_min,\n        \"contamination_ratio\": args.contamination_ratio,\n        \"batch_size\": args.batch_size,\n        \"learning_rate\": args.learning_rate,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"num_examples\": len(train_dataset),\n    }\n    print(\"\\n=== Training Config ===\")\n    for k, v in config_summary.items():\n        print(f\"  {k}: {v}\")\n    print()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    with open(os.path.join(args.output_dir, \"config.json\"), \"w\") as f:\n        json.dump(config_summary, f, indent=2)\n\n    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)\n    trainer._flush_metrics()\n    trainer.save_model(os.path.join(args.output_dir, \"final\"))\n    print(f\"\\nTraining complete. Model saved to {args.output_dir}/final\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 392,
      "startLine": 1,
      "totalLines": 392
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01WYsccd1uH8LBDwvuq92y8T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "1936aae9-538a-43a1-bd30-3a2ef6024a84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9Hh5oSSv8r1zxA1aAAcbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5735,
      "cache_read_input_tokens": 24325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5735
      },
      "output_tokens": 35,
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

_source line 13 · 2026-05-15T07:15:43.281Z_

<details><summary>↩ Tool result · `toolu_01WYsccd1uH8LBDwvuq92y8T`</summary>

```text
1	"""Convergence-theoretic adaptive contamination reweighting.
2	
3	Implements the effective authenticity rate α_eff(b) and related quantities
4	for importance-weighted pretraining on contaminated corpora.
5	
6	Key idea: given a detector that outputs per-sample synthetic probability q_i,
7	assign weight w_i = (1 − q_i)^b. The parameter b controls the bias-variance
8	tradeoff: higher b downweights suspected synthetic data more aggressively
9	but reduces effective sample size (ESS).
10	
11	Core quantities:
12	  α_eff(b) = Σ (1−q_i)^{b+1} / Σ (1−q_i)^b    — effective authenticity rate
13	  ESS(b)   = (Σ w_i)² / Σ w_i²                  — effective sample size
14	  b*       = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b*) ≥ n_min
15	
16	References:
17	  - arXiv 2602.16065 (convergence bounds for weighted pretraining)
18	  - Drayson et al., EMNLP 2025 (grid-search weighting baseline)
19	
20	Inputs:  q_scores ∈ [0,1]^N (synthetic probabilities from detector)
21	Outputs: weights w ∈ R_+^N (normalized to sum to N)
22	"""
23	
24	import math
25	import torch
26	
27	
28	def compute_alpha_eff(q_scores: torch.Tensor, b: float) -> float:
29	    """Effective authenticity rate α_eff(b) = Σ (1−q)^{b+1} / Σ (1−q)^b.
30	
31	    Properties:
32	      α_eff(0) = 1 − ρ̂  (unweighted authenticity)
33	      α_eff(b) → 1 as b → ∞
34	      α_eff(b) is monotonically non-decreasing in b
35	    """
36	    q = q_scores.clamp(0.0, 1.0).double()
37	    one_minus_q = 1.0 - q
38	
39	    if b == 0.0:
40	        return float(one_minus_q.mean())
41	
42	    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
43	    log_w = b * log_omq
44	    log_w_shift = log_w - log_w.max()
45	    w = torch.exp(log_w_shift)
46	
47	    numerator = (w * one_minus_q).sum()
48	    denominator = w.sum()
49	
50	    if denominator < 1e-30:
51	        return 1.0
52	
53	    return float(numerator / denominator)
54	
55	
56	def compute_ess(q_scores: torch.Tensor, b: float) -> float:
57	    """Effective sample size ESS(b) = (Σ w_i)² / Σ w_i².
58	
59	    ESS = N when b=0 (uniform weights), decreases as b increases.
60	    """
61	    if b == 0.0:
62	        return float(q_scores.numel())
63	
64	    q = q_scores.clamp(0.0, 1.0).double()
65	    one_minus_q = 1.0 - q
66	
67	    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
68	    log_w = b * log_omq
69	    log_w_shift = log_w - log_w.max()
70	    w = torch.exp(log_w_shift)
71	
72	    sum_w = w.sum()
73	    sum_w2 = (w * w).sum()
74	
75	    if sum_w2 < 1e-30:
76	        return 0.0
77	
78	    return float((sum_w * sum_w) / sum_w2)
79	
80	
81	def find_optimal_b(
82	    q_scores: torch.Tensor,
83	    tau: float,
84	    n_min: int,
85	    b_max: float = 20.0,
86	    resolution: int = 1000,
87	) -> float:
88	    """Find b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b*) ≥ n_min.
89	
90	    When the batch is clean enough (ρ̂ < 1 − τ), returns b=0 (uniform).
91	    When the ESS constraint conflicts with the α_eff threshold, returns
92	    b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min.
93	    """
94	    alpha_0 = compute_alpha_eff(q_scores, 0.0)
95	    if alpha_0 >= tau:
96	        return 0.0
97	
98	    n = q_scores.numel()
99	    if n_min > n:
100	        n_min = n
101	
102	    # Phase 1: grid search to find the feasible region
103	    grid = torch.linspace(0.0, b_max, resolution + 1).tolist()
104	
105	    best_feasible_b = 0.0
106	    best_feasible_alpha = alpha_0
107	    threshold_b = None
108	
109	    for b_val in grid:
110	        ess = compute_ess(q_scores, b_val)
111	        if ess < n_min:
112	            break
113	
114	        alpha = compute_alpha_eff(q_scores, b_val)
115	
116	        if alpha > best_feasible_alpha:
117	            best_feasible_alpha = alpha
118	            best_feasible_b = b_val
119	
120	        if alpha >= tau and threshold_b is None:
121	            threshold_b = b_val
122	
123	    if threshold_b is not None:
124	        # Phase 2: refine with bisection
125	        lo = max(0.0, threshold_b - b_max / resolution)
126	        hi = threshold_b
127	        for _ in range(50):
128	            mid = (lo + hi) / 2.0
129	            if compute_alpha_eff(q_scores, mid) >= tau:
130	                hi = mid
131	            else:
132	                lo = mid
133	        b_star = hi
134	        if compute_ess(q_scores, b_star) >= n_min:
135	            return b_star
136	
137	    return best_feasible_b
138	
139	
140	def compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:
141	    """Per-sample weights w_i = (1−q_i)^b, normalized to sum to N."""
142	    n = q_scores.numel()
143	
144	    if b == 0.0:
145	        return torch.ones_like(q_scores)
146	
147	    q = q_scores.clamp(0.0, 1.0)
148	    one_minus_q = 1.0 - q
149	
150	    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
151	    log_w = b * log_omq
152	    log_w = log_w - log_w.max()
153	    w = torch.exp(log_w)
154	
155	    w = w * (n / w.sum().clamp(min=1e-30))
156	    return w.to(q_scores.dtype)
157	
158	
159	def compute_concentration_bound(
160	    q_scores: torch.Tensor, b: float, delta: float = 0.05
161	) -> float:
162	    """Concentration bound |α̂_eff − α_eff| ≤ O(√(w_max / (ESS · Σw))) · log(1/δ)).
163	
164	    Returns the upper bound on estimation error for α_eff with probability 1−δ.
165	    """
166	    if b == 0.0:
167	        n = q_scores.numel()
168	        return float(math.sqrt(math.log(2.0 / delta) / (2.0 * n)))
169	
170	    q = q_scores.clamp(0.0, 1.0).double()
171	    one_minus_q = 1.0 - q
172	    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
173	    log_w = b * log_omq
174	    log_w = log_w - log_w.max()
175	    w = torch.exp(log_w)
176	
177	    sum_w = w.sum()
178	    w_max = w.max()
179	    ess = compute_ess(q_scores, b)
180	
181	    if ess < 1e-10 or sum_w < 1e-30:
182	        return float("inf")
183	
184	    bound = float(torch.sqrt(w_max / (ess * sum_w))) * math.log(2.0 / delta)
185	    return bound
186	
187	
188	if __name__ == "__main__":
189	    torch.manual_seed(42)
190	    n = 1000
191	
192	    # Simulate: 80% human (low q), 20% synthetic (high q)
193	    q_human = torch.rand(800) * 0.2
194	    q_synth = 0.7 + torch.rand(200) * 0.3
195	    q_scores = torch.cat([q_human, q_synth])
196	    q_scores = q_scores[torch.randperm(n)]
197	
198	    print(f"N = {n}, mean q = {q_scores.mean():.4f}")
199	    print(f"True contamination ≈ 20%\n")
200	
201	    for b in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0]:
202	        alpha = compute_alpha_eff(q_scores, b)
203	        ess = compute_ess(q_scores, b)
204	        bound = compute_concentration_bound(q_scores, b)
205	        print(f"b={b:5.1f}  α_eff={alpha:.4f}  ESS={ess:8.1f}  bound={bound:.6f}")
206	
207	    print()
208	
209	    tau = 0.95
210	    n_min = 100
211	    b_star = find_optimal_b(q_scores, tau=tau, n_min=n_min)
212	    alpha_star = compute_alpha_eff(q_scores, b_star)
213	    ess_star = compute_ess(q_scores, b_star)
214	    print(f"Optimal b* = {b_star:.4f}  (tau={tau}, n_min={n_min})")
215	    print(f"  α_eff(b*) = {alpha_star:.4f}")
216	    print(f"  ESS(b*)   = {ess_star:.1f}")
217	
218	    weights = compute_sample_weights(q_scores, b_star)
219	    print(f"\nWeights: sum={weights.sum():.1f}, min={weights.min():.4f}, "
220	          f"max={weights.max():.4f}, std={weights.std():.4f}")
221	
222	    # Verify monotonicity of α_eff
223	    bs = [i * 0.5 for i in range(21)]
224	    alphas = [compute_alpha_eff(q_scores, b) for b in bs]
225	    monotone = all(alphas[i] <= alphas[i + 1] + 1e-10 for i in range(len(alphas) - 1))
226	    print(f"\nα_eff monotonicity check: {'PASS' if monotone else 'FAIL'}")
227	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "e1e519ec-3e4f-4de0-a8b7-3fd25276f399",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
      "content": "\"\"\"Convergence-theoretic adaptive contamination reweighting.\n\nImplements the effective authenticity rate α_eff(b) and related quantities\nfor importance-weighted pretraining on contaminated corpora.\n\nKey idea: given a detector that outputs per-sample synthetic probability q_i,\nassign weight w_i = (1 − q_i)^b. The parameter b controls the bias-variance\ntradeoff: higher b downweights suspected synthetic data more aggressively\nbut reduces effective sample size (ESS).\n\nCore quantities:\n  α_eff(b) = Σ (1−q_i)^{b+1} / Σ (1−q_i)^b    — effective authenticity rate\n  ESS(b)   = (Σ w_i)² / Σ w_i²                  — effective sample size\n  b*       = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b*) ≥ n_min\n\nReferences:\n  - arXiv 2602.16065 (convergence bounds for weighted pretraining)\n  - Drayson et al., EMNLP 2025 (grid-search weighting baseline)\n\nInputs:  q_scores ∈ [0,1]^N (synthetic probabilities from detector)\nOutputs: weights w ∈ R_+^N (normalized to sum to N)\n\"\"\"\n\nimport math\nimport torch\n\n\ndef compute_alpha_eff(q_scores: torch.Tensor, b: float) -> float:\n    \"\"\"Effective authenticity rate α_eff(b) = Σ (1−q)^{b+1} / Σ (1−q)^b.\n\n    Properties:\n      α_eff(0) = 1 − ρ̂  (unweighted authenticity)\n      α_eff(b) → 1 as b → ∞\n      α_eff(b) is monotonically non-decreasing in b\n    \"\"\"\n    q = q_scores.clamp(0.0, 1.0).double()\n    one_minus_q = 1.0 - q\n\n    if b == 0.0:\n        return float(one_minus_q.mean())\n\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w_shift = log_w - log_w.max()\n    w = torch.exp(log_w_shift)\n\n    numerator = (w * one_minus_q).sum()\n    denominator = w.sum()\n\n    if denominator < 1e-30:\n        return 1.0\n\n    return float(numerator / denominator)\n\n\ndef compute_ess(q_scores: torch.Tensor, b: float) -> float:\n    \"\"\"Effective sample size ESS(b) = (Σ w_i)² / Σ w_i².\n\n    ESS = N when b=0 (uniform weights), decreases as b increases.\n    \"\"\"\n    if b == 0.0:\n        return float(q_scores.numel())\n\n    q = q_scores.clamp(0.0, 1.0).double()\n    one_minus_q = 1.0 - q\n\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w_shift = log_w - log_w.max()\n    w = torch.exp(log_w_shift)\n\n    sum_w = w.sum()\n    sum_w2 = (w * w).sum()\n\n    if sum_w2 < 1e-30:\n        return 0.0\n\n    return float((sum_w * sum_w) / sum_w2)\n\n\ndef find_optimal_b(\n    q_scores: torch.Tensor,\n    tau: float,\n    n_min: int,\n    b_max: float = 20.0,\n    resolution: int = 1000,\n) -> float:\n    \"\"\"Find b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b*) ≥ n_min.\n\n    When the batch is clean enough (ρ̂ < 1 − τ), returns b=0 (uniform).\n    When the ESS constraint conflicts with the α_eff threshold, returns\n    b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min.\n    \"\"\"\n    alpha_0 = compute_alpha_eff(q_scores, 0.0)\n    if alpha_0 >= tau:\n        return 0.0\n\n    n = q_scores.numel()\n    if n_min > n:\n        n_min = n\n\n    # Phase 1: grid search to find the feasible region\n    grid = torch.linspace(0.0, b_max, resolution + 1).tolist()\n\n    best_feasible_b = 0.0\n    best_feasible_alpha = alpha_0\n    threshold_b = None\n\n    for b_val in grid:\n        ess = compute_ess(q_scores, b_val)\n        if ess < n_min:\n            break\n\n        alpha = compute_alpha_eff(q_scores, b_val)\n\n        if alpha > best_feasible_alpha:\n            best_feasible_alpha = alpha\n            best_feasible_b = b_val\n\n        if alpha >= tau and threshold_b is None:\n            threshold_b = b_val\n\n    if threshold_b is not None:\n        # Phase 2: refine with bisection\n        lo = max(0.0, threshold_b - b_max / resolution)\n        hi = threshold_b\n        for _ in range(50):\n            mid = (lo + hi) / 2.0\n            if compute_alpha_eff(q_scores, mid) >= tau:\n                hi = mid\n            else:\n                lo = mid\n        b_star = hi\n        if compute_ess(q_scores, b_star) >= n_min:\n            return b_star\n\n    return best_feasible_b\n\n\ndef compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:\n    \"\"\"Per-sample weights w_i = (1−q_i)^b, normalized to sum to N.\"\"\"\n    n = q_scores.numel()\n\n    if b == 0.0:\n        return torch.ones_like(q_scores)\n\n    q = q_scores.clamp(0.0, 1.0)\n    one_minus_q = 1.0 - q\n\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w = log_w - log_w.max()\n    w = torch.exp(log_w)\n\n    w = w * (n / w.sum().clamp(min=1e-30))\n    return w.to(q_scores.dtype)\n\n\ndef compute_concentration_bound(\n    q_scores: torch.Tensor, b: float, delta: float = 0.05\n) -> float:\n    \"\"\"Concentration bound |α̂_eff − α_eff| ≤ O(√(w_max / (ESS · Σw))) · log(1/δ)).\n\n    Returns the upper bound on estimation error for α_eff with probability 1−δ.\n    \"\"\"\n    if b == 0.0:\n        n = q_scores.numel()\n        return float(math.sqrt(math.log(2.0 / delta) / (2.0 * n)))\n\n    q = q_scores.clamp(0.0, 1.0).double()\n    one_minus_q = 1.0 - q\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w = log_w - log_w.max()\n    w = torch.exp(log_w)\n\n    sum_w = w.sum()\n    w_max = w.max()\n    ess = compute_ess(q_scores, b)\n\n    if ess < 1e-10 or sum_w < 1e-30:\n        return float(\"inf\")\n\n    bound = float(torch.sqrt(w_max / (ess * sum_w))) * math.log(2.0 / delta)\n    return bound\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    n = 1000\n\n    # Simulate: 80% human (low q), 20% synthetic (high q)\n    q_human = torch.rand(800) * 0.2\n    q_synth = 0.7 + torch.rand(200) * 0.3\n    q_scores = torch.cat([q_human, q_synth])\n    q_scores = q_scores[torch.randperm(n)]\n\n    print(f\"N = {n}, mean q = {q_scores.mean():.4f}\")\n    print(f\"True contamination ≈ 20%\\n\")\n\n    for b in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0]:\n        alpha = compute_alpha_eff(q_scores, b)\n        ess = compute_ess(q_scores, b)\n        bound = compute_concentration_bound(q_scores, b)\n        print(f\"b={b:5.1f}  α_eff={alpha:.4f}  ESS={ess:8.1f}  bound={bound:.6f}\")\n\n    print()\n\n    tau = 0.95\n    n_min = 100\n    b_star = find_optimal_b(q_scores, tau=tau, n_min=n_min)\n    alpha_star = compute_alpha_eff(q_scores, b_star)\n    ess_star = compute_ess(q_scores, b_star)\n    print(f\"Optimal b* = {b_star:.4f}  (tau={tau}, n_min={n_min})\")\n    print(f\"  α_eff(b*) = {alpha_star:.4f}\")\n    print(f\"  ESS(b*)   = {ess_star:.1f}\")\n\n    weights = compute_sample_weights(q_scores, b_star)\n    print(f\"\\nWeights: sum={weights.sum():.1f}, min={weights.min():.4f}, \"\n          f\"max={weights.max():.4f}, std={weights.std():.4f}\")\n\n    # Verify monotonicity of α_eff\n    bs = [i * 0.5 for i in range(21)]\n    alphas = [compute_alpha_eff(q_scores, b) for b in bs]\n    monotone = all(alphas[i] <= alphas[i + 1] + 1e-10 for i in range(len(alphas) - 1))\n    print(f\"\\nα_eff monotonicity check: {'PASS' if monotone else 'FAIL'}\")\n",
      "numLines": 227,
      "startLine": 1,
      "totalLines": 227
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the full picture. Let me implement the changes:

1. Add `find_ess_only_b` function in `alpha_eff.py` (or handle it in pretrain_weighted.py)
2. Add `ess_only` to the weighting method choices in argparse
3. Add the `ess_only` branch in `compute_loss`
4. Create the run script
5. Create the artifact documentation

The ESS-only method: find max{b : ESS(b) ≥ n_min}. Since ESS is monotonically non-increasing in b, I can use binary search on [0, b_max] to find the largest b where ESS ≥ n_min.


I'll add the `find_ess_only_b` function to `alpha_eff.py` alongside the existing `find_optimal_b`, then wire it up in `pretrain_weighted.py`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "8fbac8e4-ecc4-41d5-abae-c4182a34e741",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KyfEDqZaXeaaB2BcGBuzS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3427,
      "cache_read_input_tokens": 30060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3427
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

_source line 15_

现在理解了全部逻辑。开始实现：

1. 在 `alpha_eff.py` 添加 `find_ess_only_b` 函数
2. 在 `pretrain_weighted.py` 添加 `ess_only` 方法支持
3. 创建运行脚本和文档

先添加 `find_ess_only_b` 到 `alpha_eff.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "ab7ac9aa-15bd-47d0-a095-c794cddf2271",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KyfEDqZaXeaaB2BcGBuzS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3427,
      "cache_read_input_tokens": 30060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3427
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01CBfNirsiyNtJZRADHpzWL7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
  "old_string": "def compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:",
  "new_string": "def find_ess_only_b(\n    q_scores: torch.Tensor,\n    n_min: int,\n    b_max: float = 20.0,\n    tol: float = 0.01,\n) -> float:\n    \"\"\"Find b* = max{b : ESS(b) >= n_min} (ESS-only, no alpha_eff constraint).\n\n    ESS(b) is monotonically non-increasing in b, so binary search works.\n    Returns b_max if ESS(b_max) >= n_min; returns 0.0 if ESS(0) < n_min.\n    \"\"\"\n    if compute_ess(q_scores, 0.0) < n_min:\n        return 0.0\n\n    if compute_ess(q_scores, b_max) >= n_min:\n        return b_max\n\n    lo, hi = 0.0, b_max\n    while hi - lo > tol:\n        mid = (lo + hi) / 2.0\n        if compute_ess(q_scores, mid) >= n_min:\n            lo = mid\n        else:\n            hi = mid\n    return lo\n\n\ndef compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "a8e8cb8d-0247-47f6-9fdc-21ca29dc5f4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KyfEDqZaXeaaB2BcGBuzS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3427,
      "cache_read_input_tokens": 30060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3427
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

_source line 17 · 2026-05-15T07:15:58.429Z_

<details><summary>↩ Tool result · `toolu_01CBfNirsiyNtJZRADHpzWL7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "b3404e5a-cd12-48d1-aed2-d6c1c0cb7381",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
    "oldString": "def compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:",
    "newString": "def find_ess_only_b(\n    q_scores: torch.Tensor,\n    n_min: int,\n    b_max: float = 20.0,\n    tol: float = 0.01,\n) -> float:\n    \"\"\"Find b* = max{b : ESS(b) >= n_min} (ESS-only, no alpha_eff constraint).\n\n    ESS(b) is monotonically non-increasing in b, so binary search works.\n    Returns b_max if ESS(b_max) >= n_min; returns 0.0 if ESS(0) < n_min.\n    \"\"\"\n    if compute_ess(q_scores, 0.0) < n_min:\n        return 0.0\n\n    if compute_ess(q_scores, b_max) >= n_min:\n        return b_max\n\n    lo, hi = 0.0, b_max\n    while hi - lo > tol:\n        mid = (lo + hi) / 2.0\n        if compute_ess(q_scores, mid) >= n_min:\n            lo = mid\n        else:\n            hi = mid\n    return lo\n\n\ndef compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:",
    "originalFile": "\"\"\"Convergence-theoretic adaptive contamination reweighting.\n\nImplements the effective authenticity rate α_eff(b) and related quantities\nfor importance-weighted pretraining on contaminated corpora.\n\nKey idea: given a detector that outputs per-sample synthetic probability q_i,\nassign weight w_i = (1 − q_i)^b. The parameter b controls the bias-variance\ntradeoff: higher b downweights suspected synthetic data more aggressively\nbut reduces effective sample size (ESS).\n\nCore quantities:\n  α_eff(b) = Σ (1−q_i)^{b+1} / Σ (1−q_i)^b    — effective authenticity rate\n  ESS(b)   = (Σ w_i)² / Σ w_i²                  — effective sample size\n  b*       = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b*) ≥ n_min\n\nReferences:\n  - arXiv 2602.16065 (convergence bounds for weighted pretraining)\n  - Drayson et al., EMNLP 2025 (grid-search weighting baseline)\n\nInputs:  q_scores ∈ [0,1]^N (synthetic probabilities from detector)\nOutputs: weights w ∈ R_+^N (normalized to sum to N)\n\"\"\"\n\nimport math\nimport torch\n\n\ndef compute_alpha_eff(q_scores: torch.Tensor, b: float) -> float:\n    \"\"\"Effective authenticity rate α_eff(b) = Σ (1−q)^{b+1} / Σ (1−q)^b.\n\n    Properties:\n      α_eff(0) = 1 − ρ̂  (unweighted authenticity)\n      α_eff(b) → 1 as b → ∞\n      α_eff(b) is monotonically non-decreasing in b\n    \"\"\"\n    q = q_scores.clamp(0.0, 1.0).double()\n    one_minus_q = 1.0 - q\n\n    if b == 0.0:\n        return float(one_minus_q.mean())\n\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w_shift = log_w - log_w.max()\n    w = torch.exp(log_w_shift)\n\n    numerator = (w * one_minus_q).sum()\n    denominator = w.sum()\n\n    if denominator < 1e-30:\n        return 1.0\n\n    return float(numerator / denominator)\n\n\ndef compute_ess(q_scores: torch.Tensor, b: float) -> float:\n    \"\"\"Effective sample size ESS(b) = (Σ w_i)² / Σ w_i².\n\n    ESS = N when b=0 (uniform weights), decreases as b increases.\n    \"\"\"\n    if b == 0.0:\n        return float(q_scores.numel())\n\n    q = q_scores.clamp(0.0, 1.0).double()\n    one_minus_q = 1.0 - q\n\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w_shift = log_w - log_w.max()\n    w = torch.exp(log_w_shift)\n\n    sum_w = w.sum()\n    sum_w2 = (w * w).sum()\n\n    if sum_w2 < 1e-30:\n        return 0.0\n\n    return float((sum_w * sum_w) / sum_w2)\n\n\ndef find_optimal_b(\n    q_scores: torch.Tensor,\n    tau: float,\n    n_min: int,\n    b_max: float = 20.0,\n    resolution: int = 1000,\n) -> float:\n    \"\"\"Find b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b*) ≥ n_min.\n\n    When the batch is clean enough (ρ̂ < 1 − τ), returns b=0 (uniform).\n    When the ESS constraint conflicts with the α_eff threshold, returns\n    b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min.\n    \"\"\"\n    alpha_0 = compute_alpha_eff(q_scores, 0.0)\n    if alpha_0 >= tau:\n        return 0.0\n\n    n = q_scores.numel()\n    if n_min > n:\n        n_min = n\n\n    # Phase 1: grid search to find the feasible region\n    grid = torch.linspace(0.0, b_max, resolution + 1).tolist()\n\n    best_feasible_b = 0.0\n    best_feasible_alpha = alpha_0\n    threshold_b = None\n\n    for b_val in grid:\n        ess = compute_ess(q_scores, b_val)\n        if ess < n_min:\n            break\n\n        alpha = compute_alpha_eff(q_scores, b_val)\n\n        if alpha > best_feasible_alpha:\n            best_feasible_alpha = alpha\n            best_feasible_b = b_val\n\n        if alpha >= tau and threshold_b is None:\n            threshold_b = b_val\n\n    if threshold_b is not None:\n        # Phase 2: refine with bisection\n        lo = max(0.0, threshold_b - b_max / resolution)\n        hi = threshold_b\n        for _ in range(50):\n            mid = (lo + hi) / 2.0\n            if compute_alpha_eff(q_scores, mid) >= tau:\n                hi = mid\n            else:\n                lo = mid\n        b_star = hi\n        if compute_ess(q_scores, b_star) >= n_min:\n            return b_star\n\n    return best_feasible_b\n\n\ndef compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:\n    \"\"\"Per-sample weights w_i = (1−q_i)^b, normalized to sum to N.\"\"\"\n    n = q_scores.numel()\n\n    if b == 0.0:\n        return torch.ones_like(q_scores)\n\n    q = q_scores.clamp(0.0, 1.0)\n    one_minus_q = 1.0 - q\n\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w = log_w - log_w.max()\n    w = torch.exp(log_w)\n\n    w = w * (n / w.sum().clamp(min=1e-30))\n    return w.to(q_scores.dtype)\n\n\ndef compute_concentration_bound(\n    q_scores: torch.Tensor, b: float, delta: float = 0.05\n) -> float:\n    \"\"\"Concentration bound |α̂_eff − α_eff| ≤ O(√(w_max / (ESS · Σw))) · log(1/δ)).\n\n    Returns the upper bound on estimation error for α_eff with probability 1−δ.\n    \"\"\"\n    if b == 0.0:\n        n = q_scores.numel()\n        return float(math.sqrt(math.log(2.0 / delta) / (2.0 * n)))\n\n    q = q_scores.clamp(0.0, 1.0).double()\n    one_minus_q = 1.0 - q\n    log_omq = torch.log(one_minus_q.clamp(min=1e-30))\n    log_w = b * log_omq\n    log_w = log_w - log_w.max()\n    w = torch.exp(log_w)\n\n    sum_w = w.sum()\n    w_max = w.max()\n    ess = compute_ess(q_scores, b)\n\n    if ess < 1e-10 or sum_w < 1e-30:\n        return float(\"inf\")\n\n    bound = float(torch.sqrt(w_max / (ess * sum_w))) * math.log(2.0 / delta)\n    return bound\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    n = 1000\n\n    # Simulate: 80% human (low q), 20% synthetic (high q)\n    q_human = torch.rand(800) * 0.2\n    q_synth = 0.7 + torch.rand(200) * 0.3\n    q_scores = torch.cat([q_human, q_synth])\n    q_scores = q_scores[torch.randperm(n)]\n\n    print(f\"N = {n}, mean q = {q_scores.mean():.4f}\")\n    print(f\"True contamination ≈ 20%\\n\")\n\n    for b in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0]:\n        alpha = compute_alpha_eff(q_scores, b)\n        ess = compute_ess(q_scores, b)\n        bound = compute_concentration_bound(q_scores, b)\n        print(f\"b={b:5.1f}  α_eff={alpha:.4f}  ESS={ess:8.1f}  bound={bound:.6f}\")\n\n    print()\n\n    tau = 0.95\n    n_min = 100\n    b_star = find_optimal_b(q_scores, tau=tau, n_min=n_min)\n    alpha_star = compute_alpha_eff(q_scores, b_star)\n    ess_star = compute_ess(q_scores, b_star)\n    print(f\"Optimal b* = {b_star:.4f}  (tau={tau}, n_min={n_min})\")\n    print(f\"  α_eff(b*) = {alpha_star:.4f}\")\n    print(f\"  ESS(b*)   = {ess_star:.1f}\")\n\n    weights = compute_sample_weights(q_scores, b_star)\n    print(f\"\\nWeights: sum={weights.sum():.1f}, min={weights.min():.4f}, \"\n          f\"max={weights.max():.4f}, std={weights.std():.4f}\")\n\n    # Verify monotonicity of α_eff\n    bs = [i * 0.5 for i in range(21)]\n    alphas = [compute_alpha_eff(q_scores, b) for b in bs]\n    monotone = all(alphas[i] <= alphas[i + 1] + 1e-10 for i in range(len(alphas) - 1))\n    print(f\"\\nα_eff monotonicity check: {'PASS' if monotone else 'FAIL'}\")\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 6,
        "newStart": 137,
        "newLines": 33,
        "lines": [
          "     return best_feasible_b",
          " ",
          " ",
          "+def find_ess_only_b(",
          "+    q_scores: torch.Tensor,",
          "+    n_min: int,",
          "+    b_max: float = 20.0,",
          "+    tol: float = 0.01,",
          "+) -> float:",
          "+    \"\"\"Find b* = max{b : ESS(b) >= n_min} (ESS-only, no alpha_eff constraint).",
          "+",
          "+    ESS(b) is monotonically non-increasing in b, so binary search works.",
          "+    Returns b_max if ESS(b_max) >= n_min; returns 0.0 if ESS(0) < n_min.",
          "+    \"\"\"",
          "+    if compute_ess(q_scores, 0.0) < n_min:",
          "+        return 0.0",
          "+",
          "+    if compute_ess(q_scores, b_max) >= n_min:",
          "+        return b_max",
          "+",
          "+    lo, hi = 0.0, b_max",
          "+    while hi - lo > tol:",
          "+        mid = (lo + hi) / 2.0",
          "+        if compute_ess(q_scores, mid) >= n_min:",
          "+            lo = mid",
          "+        else:",
          "+            hi = mid",
          "+    return lo",
          "+",
          "+",
          " def compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:",
          "     \"\"\"Per-sample weights w_i = (1−q_i)^b, normalized to sum to N.\"\"\"",
          "     n = q_scores.numel()"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 18_

现在更新 `__init__.py` 导出新函数，然后修改 `pretrain_weighted.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "5eae3aa5-0f97-45f3-ab36-c64a32177c09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017X7gywM8hAPmFEa7BT9QLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 33487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 884
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_014RNBwKmTJAQ8MogUaVaSqE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "7338247b-341f-41c7-be12-fd6aad1444b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017X7gywM8hAPmFEa7BT9QLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 33487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 884
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

_source line 20 · 2026-05-15T07:16:01.155Z_

<details><summary>↩ Tool result · `toolu_014RNBwKmTJAQ8MogUaVaSqE`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "b10a05a1-aed6-4e17-a784-4d2ed49692e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/__init__.py",
      "content": "",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

`__init__.py` 是空的，import 是直接从 `alpha_eff` 模块引的。更新 `pretrain_weighted.py` 的 import 和逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "781d9bd5-9752-41c4-9223-2235fccff345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eL7rAvwk8UjURaBRstyku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 34371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01736Hn4QpPXkKxUiM27B88T`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "old_string": "from weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_optimal_b,\n)",
  "new_string": "from weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_ess_only_b,\n    find_optimal_b,\n)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "af0c0594-f47b-4596-933c-e85d79c1c0b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eL7rAvwk8UjURaBRstyku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 34371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
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

_source line 23 · 2026-05-15T07:16:06.380Z_

<details><summary>↩ Tool result · `toolu_01736Hn4QpPXkKxUiM27B88T`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "dce5d90d-c25e-4ad4-ae7e-d4731161f11d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
    "oldString": "from weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_optimal_b,\n)",
    "newString": "from weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_ess_only_b,\n    find_optimal_b,\n)",
    "originalFile": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports three weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom torch.utils.data import Dataset\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    Trainer,\n    TrainingArguments,\n    set_seed,\n)\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\"))\nfrom weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_optimal_b,\n)\n\n\nGRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]\n\n\nclass WeightedTextDataset(Dataset):\n    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n        self.examples = []\n\n        with open(data_path, \"r\") as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                item = json.loads(line)\n                self.examples.append(item)\n\n    def __len__(self):\n        return len(self.examples)\n\n    def __getitem__(self, idx):\n        item = self.examples[idx]\n        encoding = self.tokenizer(\n            item[\"text\"],\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        input_ids = encoding[\"input_ids\"].squeeze(0)\n        attention_mask = encoding[\"attention_mask\"].squeeze(0)\n        return {\n            \"input_ids\": input_ids,\n            \"attention_mask\": attention_mask,\n            \"labels\": input_ids.clone(),\n            \"q_score\": item.get(\"q_score\", 0.0),\n        }\n\n\ndef collate_fn(batch):\n    input_ids = torch.stack([x[\"input_ids\"] for x in batch])\n    attention_mask = torch.stack([x[\"attention_mask\"] for x in batch])\n    labels = torch.stack([x[\"labels\"] for x in batch])\n    q_scores = torch.tensor([x[\"q_score\"] for x in batch], dtype=torch.float32)\n    return {\n        \"input_ids\": input_ids,\n        \"attention_mask\": attention_mask,\n        \"labels\": labels,\n        \"q_scores\": q_scores,\n    }\n\n\nclass WeightedTrainer(Trainer):\n    def __init__(self, weighting_method: str, tau: float, n_min: int,\n                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):\n        super().__init__(**kwargs)\n        self.weighting_method = weighting_method\n        self.tau = tau\n        self.n_min = n_min\n        self.grid_b_value = grid_b_value\n        self.log_path = log_path\n        self._step_metrics = []\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        q_scores = inputs.pop(\"q_scores\")\n        labels = inputs.get(\"labels\")\n\n        outputs = model(**inputs)\n        logits = outputs.logits\n\n        shift_logits = logits[..., :-1, :].contiguous()\n        shift_labels = labels[..., 1:].contiguous()\n        attention_mask = inputs.get(\"attention_mask\")\n        if attention_mask is not None:\n            shift_mask = attention_mask[..., 1:].contiguous()\n        else:\n            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)\n\n        loss_fct = torch.nn.CrossEntropyLoss(reduction=\"none\")\n        per_token_loss = loss_fct(\n            shift_logits.view(-1, shift_logits.size(-1)),\n            shift_labels.view(-1),\n        ).view(shift_labels.size())\n\n        # Mask padding tokens\n        per_token_loss = per_token_loss * shift_mask\n\n        # Per-sample loss: mean over tokens\n        token_counts = shift_mask.sum(dim=-1).clamp(min=1)\n        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts\n\n        unweighted_loss = per_sample_loss.mean()\n\n        b_val = 0.0\n        alpha_val = compute_alpha_eff(q_scores, 0.0)\n        ess_val = float(q_scores.numel())\n\n        if self.weighting_method == \"uniform\":\n            loss = unweighted_loss\n        elif self.weighting_method == \"grid\":\n            b_val = self.grid_b_value\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:\n            raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")\n\n        if model.training:\n            step_info = {\n                \"step\": self.state.global_step if self.state else 0,\n                \"loss\": float(loss.detach()),\n                \"unweighted_loss\": float(unweighted_loss.detach()),\n                \"b\": b_val,\n                \"alpha_eff\": alpha_val,\n                \"ess\": ess_val,\n                \"mean_q\": float(q_scores.mean()),\n                \"method\": self.weighting_method,\n            }\n            self._step_metrics.append(step_info)\n\n            if self.log_path and len(self._step_metrics) % 10 == 0:\n                self._flush_metrics()\n\n        return (loss, outputs) if return_outputs else loss\n\n    def _flush_metrics(self):\n        if not self._step_metrics or not self.log_path:\n            return\n        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)\n        with open(self.log_path, \"a\") as f:\n            for m in self._step_metrics:\n                f.write(json.dumps(m) + \"\\n\")\n        self._step_metrics = []\n\n    def training_step(self, model, inputs, num_items_in_batch=None):\n        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)\n\n        if self._step_metrics:\n            latest = self._step_metrics[-1]\n            self.log({\n                \"weighting/b\": latest[\"b\"],\n                \"weighting/alpha_eff\": latest[\"alpha_eff\"],\n                \"weighting/ess\": latest[\"ess\"],\n                \"weighting/mean_q\": latest[\"mean_q\"],\n                \"weighting/unweighted_loss\": latest[\"unweighted_loss\"],\n                \"weighting/weighted_loss\": latest[\"loss\"],\n            })\n\n        return result\n\n    def save_model(self, output_dir=None, _internal_call=False):\n        super().save_model(output_dir, _internal_call)\n        self._flush_metrics()\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Weighted pretraining for LMs on contaminated corpora\"\n    )\n    parser.add_argument(\"--data_path\", type=str, required=True,\n                        help=\"Path to training data (jsonl)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for checkpoints and logs\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-0.6B\",\n                        help=\"HuggingFace model name or path\")\n    parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",\n                        choices=[\"uniform\", \"grid\", \"adaptive\"],\n                        help=\"Weighting method: uniform / grid / adaptive\")\n    parser.add_argument(\"--grid_b_value\", type=float, default=1.0,\n                        help=\"Fixed b value for grid method (one run per b, \"\n                             \"grid search selects best across runs)\")\n    parser.add_argument(\"--contamination_ratio\", type=float, default=0.2,\n                        help=\"Expected contamination ratio (for adaptive tau)\")\n    parser.add_argument(\"--num_train_tokens\", type=int, default=None,\n                        help=\"Total training tokens (converted to max_steps)\")\n    parser.add_argument(\"--max_steps\", type=int, default=-1,\n                        help=\"Max training steps (overrides num_train_tokens)\")\n    parser.add_argument(\"--num_train_epochs\", type=float, default=1.0,\n                        help=\"Number of training epochs\")\n    parser.add_argument(\"--batch_size\", type=int, default=4,\n                        help=\"Per-device training batch size\")\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=4,\n                        help=\"Gradient accumulation steps\")\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5,\n                        help=\"Learning rate\")\n    parser.add_argument(\"--max_length\", type=int, default=2048,\n                        help=\"Max sequence length\")\n    parser.add_argument(\"--tau\", type=float, default=None,\n                        help=\"Alpha_eff target threshold (adaptive). \"\n                             \"Defaults to 1 - contamination_ratio * 0.5\")\n    parser.add_argument(\"--n_min\", type=int, default=None,\n                        help=\"Minimum effective sample size. \"\n                             \"Defaults to batch_size // 2\")\n    parser.add_argument(\"--use_wandb\", action=\"store_true\",\n                        help=\"Enable Weights & Biases logging\")\n    parser.add_argument(\"--wandb_project\", type=str,\n                        default=\"provenance-weight-training\",\n                        help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None,\n                        help=\"W&B run name (passed to TrainingArguments.run_name)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--eval_data_path\", type=str, default=None,\n                        help=\"Path to evaluation data (jsonl)\")\n    parser.add_argument(\"--eval_steps\", type=int, default=500,\n                        help=\"Evaluate every N steps\")\n    parser.add_argument(\"--save_steps\", type=int, default=500,\n                        help=\"Save checkpoint every N steps\")\n    parser.add_argument(\"--logging_steps\", type=int, default=10,\n                        help=\"Log every N steps\")\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05,\n                        help=\"Warmup ratio\")\n    parser.add_argument(\"--weight_decay\", type=float, default=0.01,\n                        help=\"Weight decay\")\n    parser.add_argument(\"--save_total_limit\", type=int, default=3,\n                        help=\"Keep only N most recent checkpoints\")\n    parser.add_argument(\"--save_only_model\", action=\"store_true\",\n                        help=\"Save only model weights (skip optimizer/scheduler/rng)\")\n    parser.add_argument(\"--resume_from_checkpoint\", type=str, default=None,\n                        help=\"Path to checkpoint directory to resume from\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True,\n                        help=\"Use bfloat16 (default: True)\")\n    parser.add_argument(\"--no_bf16\", action=\"store_true\",\n                        help=\"Disable bfloat16\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n    set_seed(args.seed)\n\n    if args.tau is None:\n        args.tau = 1.0 - args.contamination_ratio * 0.5\n    if args.n_min is None:\n        args.n_min = max(2, args.batch_size // 2)\n\n    use_bf16 = args.bf16 and not args.no_bf16\n\n    report_to = []\n    if args.use_wandb:\n        report_to.append(\"wandb\")\n        os.environ.setdefault(\"WANDB_PROJECT\", args.wandb_project)\n\n    print(f\"Loading tokenizer: {args.model_name}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"Loading model: {args.model_name}\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name,\n        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,\n        trust_remote_code=True,\n    )\n\n    print(f\"Loading training data: {args.data_path}\")\n    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)\n    print(f\"  {len(train_dataset)} examples loaded\")\n\n    eval_dataset = None\n    if args.eval_data_path:\n        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)\n        print(f\"  {len(eval_dataset)} eval examples loaded\")\n\n    # Convert num_train_tokens to max_steps\n    max_steps = args.max_steps\n    if max_steps <= 0 and args.num_train_tokens is not None:\n        tokens_per_step = (\n            args.batch_size * args.gradient_accumulation_steps * args.max_length\n        )\n        max_steps = args.num_train_tokens // tokens_per_step\n        print(f\"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}\")\n\n    log_path = os.path.join(args.output_dir, \"step_metrics.jsonl\")\n\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        run_name=args.wandb_run_name,\n        per_device_train_batch_size=args.batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,\n        max_steps=max_steps if max_steps > 0 else -1,\n        warmup_ratio=args.warmup_ratio,\n        weight_decay=args.weight_decay,\n        bf16=use_bf16,\n        logging_steps=args.logging_steps,\n        eval_steps=args.eval_steps if eval_dataset else None,\n        eval_strategy=\"steps\" if eval_dataset else \"no\",\n        save_steps=args.save_steps,\n        save_strategy=\"steps\",\n        save_total_limit=args.save_total_limit,\n        save_only_model=args.save_only_model,\n        load_best_model_at_end=eval_dataset is not None,\n        metric_for_best_model=\"eval_loss\" if eval_dataset else None,\n        report_to=report_to if report_to else \"none\",\n        seed=args.seed,\n        dataloader_drop_last=True,\n        remove_unused_columns=False,\n    )\n\n    trainer = WeightedTrainer(\n        weighting_method=args.weighting_method,\n        tau=args.tau,\n        n_min=args.n_min,\n        grid_b_value=args.grid_b_value,\n        log_path=log_path,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        data_collator=collate_fn,\n        tokenizer=tokenizer,\n    )\n\n    config_summary = {\n        \"model_name\": args.model_name,\n        \"weighting_method\": args.weighting_method,\n        \"grid_b_value\": args.grid_b_value if args.weighting_method == \"grid\" else None,\n        \"tau\": args.tau,\n        \"n_min\": args.n_min,\n        \"contamination_ratio\": args.contamination_ratio,\n        \"batch_size\": args.batch_size,\n        \"learning_rate\": args.learning_rate,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"num_examples\": len(train_dataset),\n    }\n    print(\"\\n=== Training Config ===\")\n    for k, v in config_summary.items():\n        print(f\"  {k}: {v}\")\n    print()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    with open(os.path.join(args.output_dir, \"config.json\"), \"w\") as f:\n        json.dump(config_summary, f, indent=2)\n\n    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)\n    trainer._flush_metrics()\n    trainer.save_model(os.path.join(args.output_dir, \"final\"))\n    print(f\"\\nTraining complete. Model saved to {args.output_dir}/final\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 6,
        "newStart": 32,
        "newLines": 7,
        "lines": [
          "     compute_alpha_eff,",
          "     compute_ess,",
          "     compute_sample_weights,",
          "+    find_ess_only_b,",
          "     find_optimal_b,",
          " )",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01WPVnPe1HHauH7HrDPT9F3u`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "old_string": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports three weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"",
  "new_string": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports four weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)\n  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "1ccb1312-ed23-484b-a7c1-f13b88481336",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012r2D7jTMjuRrvgyozrCAKf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 34535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 457
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

_source line 25 · 2026-05-15T07:16:16.944Z_

<details><summary>↩ Tool result · `toolu_01WPVnPe1HHauH7HrDPT9F3u`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "ab05f9f6-098f-49cb-a9f7-3fe389257d10",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
    "oldString": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports three weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"",
    "newString": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports four weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)\n  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"",
    "originalFile": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports three weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom torch.utils.data import Dataset\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    Trainer,\n    TrainingArguments,\n    set_seed,\n)\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\"))\nfrom weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_ess_only_b,\n    find_optimal_b,\n)\n\n\nGRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]\n\n\nclass WeightedTextDataset(Dataset):\n    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n        self.examples = []\n\n        with open(data_path, \"r\") as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                item = json.loads(line)\n                self.examples.append(item)\n\n    def __len__(self):\n        return len(self.examples)\n\n    def __getitem__(self, idx):\n        item = self.examples[idx]\n        encoding = self.tokenizer(\n            item[\"text\"],\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        input_ids = encoding[\"input_ids\"].squeeze(0)\n        attention_mask = encoding[\"attention_mask\"].squeeze(0)\n        return {\n            \"input_ids\": input_ids,\n            \"attention_mask\": attention_mask,\n            \"labels\": input_ids.clone(),\n            \"q_score\": item.get(\"q_score\", 0.0),\n        }\n\n\ndef collate_fn(batch):\n    input_ids = torch.stack([x[\"input_ids\"] for x in batch])\n    attention_mask = torch.stack([x[\"attention_mask\"] for x in batch])\n    labels = torch.stack([x[\"labels\"] for x in batch])\n    q_scores = torch.tensor([x[\"q_score\"] for x in batch], dtype=torch.float32)\n    return {\n        \"input_ids\": input_ids,\n        \"attention_mask\": attention_mask,\n        \"labels\": labels,\n        \"q_scores\": q_scores,\n    }\n\n\nclass WeightedTrainer(Trainer):\n    def __init__(self, weighting_method: str, tau: float, n_min: int,\n                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):\n        super().__init__(**kwargs)\n        self.weighting_method = weighting_method\n        self.tau = tau\n        self.n_min = n_min\n        self.grid_b_value = grid_b_value\n        self.log_path = log_path\n        self._step_metrics = []\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        q_scores = inputs.pop(\"q_scores\")\n        labels = inputs.get(\"labels\")\n\n        outputs = model(**inputs)\n        logits = outputs.logits\n\n        shift_logits = logits[..., :-1, :].contiguous()\n        shift_labels = labels[..., 1:].contiguous()\n        attention_mask = inputs.get(\"attention_mask\")\n        if attention_mask is not None:\n            shift_mask = attention_mask[..., 1:].contiguous()\n        else:\n            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)\n\n        loss_fct = torch.nn.CrossEntropyLoss(reduction=\"none\")\n        per_token_loss = loss_fct(\n            shift_logits.view(-1, shift_logits.size(-1)),\n            shift_labels.view(-1),\n        ).view(shift_labels.size())\n\n        # Mask padding tokens\n        per_token_loss = per_token_loss * shift_mask\n\n        # Per-sample loss: mean over tokens\n        token_counts = shift_mask.sum(dim=-1).clamp(min=1)\n        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts\n\n        unweighted_loss = per_sample_loss.mean()\n\n        b_val = 0.0\n        alpha_val = compute_alpha_eff(q_scores, 0.0)\n        ess_val = float(q_scores.numel())\n\n        if self.weighting_method == \"uniform\":\n            loss = unweighted_loss\n        elif self.weighting_method == \"grid\":\n            b_val = self.grid_b_value\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:\n            raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")\n\n        if model.training:\n            step_info = {\n                \"step\": self.state.global_step if self.state else 0,\n                \"loss\": float(loss.detach()),\n                \"unweighted_loss\": float(unweighted_loss.detach()),\n                \"b\": b_val,\n                \"alpha_eff\": alpha_val,\n                \"ess\": ess_val,\n                \"mean_q\": float(q_scores.mean()),\n                \"method\": self.weighting_method,\n            }\n            self._step_metrics.append(step_info)\n\n            if self.log_path and len(self._step_metrics) % 10 == 0:\n                self._flush_metrics()\n\n        return (loss, outputs) if return_outputs else loss\n\n    def _flush_metrics(self):\n        if not self._step_metrics or not self.log_path:\n            return\n        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)\n        with open(self.log_path, \"a\") as f:\n            for m in self._step_metrics:\n                f.write(json.dumps(m) + \"\\n\")\n        self._step_metrics = []\n\n    def training_step(self, model, inputs, num_items_in_batch=None):\n        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)\n\n        if self._step_metrics:\n            latest = self._step_metrics[-1]\n            self.log({\n                \"weighting/b\": latest[\"b\"],\n                \"weighting/alpha_eff\": latest[\"alpha_eff\"],\n                \"weighting/ess\": latest[\"ess\"],\n                \"weighting/mean_q\": latest[\"mean_q\"],\n                \"weighting/unweighted_loss\": latest[\"unweighted_loss\"],\n                \"weighting/weighted_loss\": latest[\"loss\"],\n            })\n\n        return result\n\n    def save_model(self, output_dir=None, _internal_call=False):\n        super().save_model(output_dir, _internal_call)\n        self._flush_metrics()\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Weighted pretraining for LMs on contaminated corpora\"\n    )\n    parser.add_argument(\"--data_path\", type=str, required=True,\n                        help=\"Path to training data (jsonl)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for checkpoints and logs\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-0.6B\",\n                        help=\"HuggingFace model name or path\")\n    parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",\n                        choices=[\"uniform\", \"grid\", \"adaptive\"],\n                        help=\"Weighting method: uniform / grid / adaptive\")\n    parser.add_argument(\"--grid_b_value\", type=float, default=1.0,\n                        help=\"Fixed b value for grid method (one run per b, \"\n                             \"grid search selects best across runs)\")\n    parser.add_argument(\"--contamination_ratio\", type=float, default=0.2,\n                        help=\"Expected contamination ratio (for adaptive tau)\")\n    parser.add_argument(\"--num_train_tokens\", type=int, default=None,\n                        help=\"Total training tokens (converted to max_steps)\")\n    parser.add_argument(\"--max_steps\", type=int, default=-1,\n                        help=\"Max training steps (overrides num_train_tokens)\")\n    parser.add_argument(\"--num_train_epochs\", type=float, default=1.0,\n                        help=\"Number of training epochs\")\n    parser.add_argument(\"--batch_size\", type=int, default=4,\n                        help=\"Per-device training batch size\")\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=4,\n                        help=\"Gradient accumulation steps\")\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5,\n                        help=\"Learning rate\")\n    parser.add_argument(\"--max_length\", type=int, default=2048,\n                        help=\"Max sequence length\")\n    parser.add_argument(\"--tau\", type=float, default=None,\n                        help=\"Alpha_eff target threshold (adaptive). \"\n                             \"Defaults to 1 - contamination_ratio * 0.5\")\n    parser.add_argument(\"--n_min\", type=int, default=None,\n                        help=\"Minimum effective sample size. \"\n                             \"Defaults to batch_size // 2\")\n    parser.add_argument(\"--use_wandb\", action=\"store_true\",\n                        help=\"Enable Weights & Biases logging\")\n    parser.add_argument(\"--wandb_project\", type=str,\n                        default=\"provenance-weight-training\",\n                        help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None,\n                        help=\"W&B run name (passed to TrainingArguments.run_name)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--eval_data_path\", type=str, default=None,\n                        help=\"Path to evaluation data (jsonl)\")\n    parser.add_argument(\"--eval_steps\", type=int, default=500,\n                        help=\"Evaluate every N steps\")\n    parser.add_argument(\"--save_steps\", type=int, default=500,\n                        help=\"Save checkpoint every N steps\")\n    parser.add_argument(\"--logging_steps\", type=int, default=10,\n                        help=\"Log every N steps\")\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05,\n                        help=\"Warmup ratio\")\n    parser.add_argument(\"--weight_decay\", type=float, default=0.01,\n                        help=\"Weight decay\")\n    parser.add_argument(\"--save_total_limit\", type=int, default=3,\n                        help=\"Keep only N most recent checkpoints\")\n    parser.add_argument(\"--save_only_model\", action=\"store_true\",\n                        help=\"Save only model weights (skip optimizer/scheduler/rng)\")\n    parser.add_argument(\"--resume_from_checkpoint\", type=str, default=None,\n                        help=\"Path to checkpoint directory to resume from\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True,\n                        help=\"Use bfloat16 (default: True)\")\n    parser.add_argument(\"--no_bf16\", action=\"store_true\",\n                        help=\"Disable bfloat16\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n    set_seed(args.seed)\n\n    if args.tau is None:\n        args.tau = 1.0 - args.contamination_ratio * 0.5\n    if args.n_min is None:\n        args.n_min = max(2, args.batch_size // 2)\n\n    use_bf16 = args.bf16 and not args.no_bf16\n\n    report_to = []\n    if args.use_wandb:\n        report_to.append(\"wandb\")\n        os.environ.setdefault(\"WANDB_PROJECT\", args.wandb_project)\n\n    print(f\"Loading tokenizer: {args.model_name}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"Loading model: {args.model_name}\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name,\n        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,\n        trust_remote_code=True,\n    )\n\n    print(f\"Loading training data: {args.data_path}\")\n    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)\n    print(f\"  {len(train_dataset)} examples loaded\")\n\n    eval_dataset = None\n    if args.eval_data_path:\n        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)\n        print(f\"  {len(eval_dataset)} eval examples loaded\")\n\n    # Convert num_train_tokens to max_steps\n    max_steps = args.max_steps\n    if max_steps <= 0 and args.num_train_tokens is not None:\n        tokens_per_step = (\n            args.batch_size * args.gradient_accumulation_steps * args.max_length\n        )\n        max_steps = args.num_train_tokens // tokens_per_step\n        print(f\"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}\")\n\n    log_path = os.path.join(args.output_dir, \"step_metrics.jsonl\")\n\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        run_name=args.wandb_run_name,\n        per_device_train_batch_size=args.batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,\n        max_steps=max_steps if max_steps > 0 else -1,\n        warmup_ratio=args.warmup_ratio,\n        weight_decay=args.weight_decay,\n        bf16=use_bf16,\n        logging_steps=args.logging_steps,\n        eval_steps=args.eval_steps if eval_dataset else None,\n        eval_strategy=\"steps\" if eval_dataset else \"no\",\n        save_steps=args.save_steps,\n        save_strategy=\"steps\",\n        save_total_limit=args.save_total_limit,\n        save_only_model=args.save_only_model,\n        load_best_model_at_end=eval_dataset is not None,\n        metric_for_best_model=\"eval_loss\" if eval_dataset else None,\n        report_to=report_to if report_to else \"none\",\n        seed=args.seed,\n        dataloader_drop_last=True,\n        remove_unused_columns=False,\n    )\n\n    trainer = WeightedTrainer(\n        weighting_method=args.weighting_method,\n        tau=args.tau,\n        n_min=args.n_min,\n        grid_b_value=args.grid_b_value,\n        log_path=log_path,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        data_collator=collate_fn,\n        tokenizer=tokenizer,\n    )\n\n    config_summary = {\n        \"model_name\": args.model_name,\n        \"weighting_method\": args.weighting_method,\n        \"grid_b_value\": args.grid_b_value if args.weighting_method == \"grid\" else None,\n        \"tau\": args.tau,\n        \"n_min\": args.n_min,\n        \"contamination_ratio\": args.contamination_ratio,\n        \"batch_size\": args.batch_size,\n        \"learning_rate\": args.learning_rate,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"num_examples\": len(train_dataset),\n    }\n    print(\"\\n=== Training Config ===\")\n    for k, v in config_summary.items():\n        print(f\"  {k}: {v}\")\n    print()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    with open(os.path.join(args.output_dir, \"config.json\"), \"w\") as f:\n        json.dump(config_summary, f, indent=2)\n\n    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)\n    trainer._flush_metrics()\n    trainer.save_model(os.path.join(args.output_dir, \"final\"))\n    print(f\"\\nTraining complete. Model saved to {args.output_dir}/final\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 10,
        "newStart": 1,
        "newLines": 11,
        "lines": [
          " \"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.",
          " ",
          "-Supports three weighting methods:",
          "+Supports four weighting methods:",
          "   - uniform:  all samples equally weighted (baseline)",
          "   - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run",
          "                once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.",
          "-  - adaptive: batch-adaptive b* via α_eff convergence theory (ours)",
          "+  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)",
          "+  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)",
          " ",
          " Data format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}",
          " \"\"\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_015jLUQnMUMiKwGRvpTTJGfY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "old_string": "                        choices=[\"uniform\", \"grid\", \"adaptive\"],\n                        help=\"Weighting method: uniform / grid / adaptive\")",
  "new_string": "                        choices=[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"],\n                        help=\"Weighting method: uniform / grid / adaptive / ess_only\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "c4993002-9563-468c-8c19-616fca420f37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9dTaS7z9Z91M4eKrEZG8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 34992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 593
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

_source line 27 · 2026-05-15T07:16:20.104Z_

<details><summary>↩ Tool result · `toolu_015jLUQnMUMiKwGRvpTTJGfY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "7e680c6c-f4dd-419b-947f-726b2ddede7c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
    "oldString": "                        choices=[\"uniform\", \"grid\", \"adaptive\"],\n                        help=\"Weighting method: uniform / grid / adaptive\")",
    "newString": "                        choices=[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"],\n                        help=\"Weighting method: uniform / grid / adaptive / ess_only\")",
    "originalFile": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports four weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)\n  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom torch.utils.data import Dataset\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    Trainer,\n    TrainingArguments,\n    set_seed,\n)\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\"))\nfrom weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_ess_only_b,\n    find_optimal_b,\n)\n\n\nGRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]\n\n\nclass WeightedTextDataset(Dataset):\n    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n        self.examples = []\n\n        with open(data_path, \"r\") as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                item = json.loads(line)\n                self.examples.append(item)\n\n    def __len__(self):\n        return len(self.examples)\n\n    def __getitem__(self, idx):\n        item = self.examples[idx]\n        encoding = self.tokenizer(\n            item[\"text\"],\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        input_ids = encoding[\"input_ids\"].squeeze(0)\n        attention_mask = encoding[\"attention_mask\"].squeeze(0)\n        return {\n            \"input_ids\": input_ids,\n            \"attention_mask\": attention_mask,\n            \"labels\": input_ids.clone(),\n            \"q_score\": item.get(\"q_score\", 0.0),\n        }\n\n\ndef collate_fn(batch):\n    input_ids = torch.stack([x[\"input_ids\"] for x in batch])\n    attention_mask = torch.stack([x[\"attention_mask\"] for x in batch])\n    labels = torch.stack([x[\"labels\"] for x in batch])\n    q_scores = torch.tensor([x[\"q_score\"] for x in batch], dtype=torch.float32)\n    return {\n        \"input_ids\": input_ids,\n        \"attention_mask\": attention_mask,\n        \"labels\": labels,\n        \"q_scores\": q_scores,\n    }\n\n\nclass WeightedTrainer(Trainer):\n    def __init__(self, weighting_method: str, tau: float, n_min: int,\n                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):\n        super().__init__(**kwargs)\n        self.weighting_method = weighting_method\n        self.tau = tau\n        self.n_min = n_min\n        self.grid_b_value = grid_b_value\n        self.log_path = log_path\n        self._step_metrics = []\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        q_scores = inputs.pop(\"q_scores\")\n        labels = inputs.get(\"labels\")\n\n        outputs = model(**inputs)\n        logits = outputs.logits\n\n        shift_logits = logits[..., :-1, :].contiguous()\n        shift_labels = labels[..., 1:].contiguous()\n        attention_mask = inputs.get(\"attention_mask\")\n        if attention_mask is not None:\n            shift_mask = attention_mask[..., 1:].contiguous()\n        else:\n            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)\n\n        loss_fct = torch.nn.CrossEntropyLoss(reduction=\"none\")\n        per_token_loss = loss_fct(\n            shift_logits.view(-1, shift_logits.size(-1)),\n            shift_labels.view(-1),\n        ).view(shift_labels.size())\n\n        # Mask padding tokens\n        per_token_loss = per_token_loss * shift_mask\n\n        # Per-sample loss: mean over tokens\n        token_counts = shift_mask.sum(dim=-1).clamp(min=1)\n        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts\n\n        unweighted_loss = per_sample_loss.mean()\n\n        b_val = 0.0\n        alpha_val = compute_alpha_eff(q_scores, 0.0)\n        ess_val = float(q_scores.numel())\n\n        if self.weighting_method == \"uniform\":\n            loss = unweighted_loss\n        elif self.weighting_method == \"grid\":\n            b_val = self.grid_b_value\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:\n            raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")\n\n        if model.training:\n            step_info = {\n                \"step\": self.state.global_step if self.state else 0,\n                \"loss\": float(loss.detach()),\n                \"unweighted_loss\": float(unweighted_loss.detach()),\n                \"b\": b_val,\n                \"alpha_eff\": alpha_val,\n                \"ess\": ess_val,\n                \"mean_q\": float(q_scores.mean()),\n                \"method\": self.weighting_method,\n            }\n            self._step_metrics.append(step_info)\n\n            if self.log_path and len(self._step_metrics) % 10 == 0:\n                self._flush_metrics()\n\n        return (loss, outputs) if return_outputs else loss\n\n    def _flush_metrics(self):\n        if not self._step_metrics or not self.log_path:\n            return\n        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)\n        with open(self.log_path, \"a\") as f:\n            for m in self._step_metrics:\n                f.write(json.dumps(m) + \"\\n\")\n        self._step_metrics = []\n\n    def training_step(self, model, inputs, num_items_in_batch=None):\n        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)\n\n        if self._step_metrics:\n            latest = self._step_metrics[-1]\n            self.log({\n                \"weighting/b\": latest[\"b\"],\n                \"weighting/alpha_eff\": latest[\"alpha_eff\"],\n                \"weighting/ess\": latest[\"ess\"],\n                \"weighting/mean_q\": latest[\"mean_q\"],\n                \"weighting/unweighted_loss\": latest[\"unweighted_loss\"],\n                \"weighting/weighted_loss\": latest[\"loss\"],\n            })\n\n        return result\n\n    def save_model(self, output_dir=None, _internal_call=False):\n        super().save_model(output_dir, _internal_call)\n        self._flush_metrics()\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Weighted pretraining for LMs on contaminated corpora\"\n    )\n    parser.add_argument(\"--data_path\", type=str, required=True,\n                        help=\"Path to training data (jsonl)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for checkpoints and logs\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-0.6B\",\n                        help=\"HuggingFace model name or path\")\n    parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",\n                        choices=[\"uniform\", \"grid\", \"adaptive\"],\n                        help=\"Weighting method: uniform / grid / adaptive\")\n    parser.add_argument(\"--grid_b_value\", type=float, default=1.0,\n                        help=\"Fixed b value for grid method (one run per b, \"\n                             \"grid search selects best across runs)\")\n    parser.add_argument(\"--contamination_ratio\", type=float, default=0.2,\n                        help=\"Expected contamination ratio (for adaptive tau)\")\n    parser.add_argument(\"--num_train_tokens\", type=int, default=None,\n                        help=\"Total training tokens (converted to max_steps)\")\n    parser.add_argument(\"--max_steps\", type=int, default=-1,\n                        help=\"Max training steps (overrides num_train_tokens)\")\n    parser.add_argument(\"--num_train_epochs\", type=float, default=1.0,\n                        help=\"Number of training epochs\")\n    parser.add_argument(\"--batch_size\", type=int, default=4,\n                        help=\"Per-device training batch size\")\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=4,\n                        help=\"Gradient accumulation steps\")\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5,\n                        help=\"Learning rate\")\n    parser.add_argument(\"--max_length\", type=int, default=2048,\n                        help=\"Max sequence length\")\n    parser.add_argument(\"--tau\", type=float, default=None,\n                        help=\"Alpha_eff target threshold (adaptive). \"\n                             \"Defaults to 1 - contamination_ratio * 0.5\")\n    parser.add_argument(\"--n_min\", type=int, default=None,\n                        help=\"Minimum effective sample size. \"\n                             \"Defaults to batch_size // 2\")\n    parser.add_argument(\"--use_wandb\", action=\"store_true\",\n                        help=\"Enable Weights & Biases logging\")\n    parser.add_argument(\"--wandb_project\", type=str,\n                        default=\"provenance-weight-training\",\n                        help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None,\n                        help=\"W&B run name (passed to TrainingArguments.run_name)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--eval_data_path\", type=str, default=None,\n                        help=\"Path to evaluation data (jsonl)\")\n    parser.add_argument(\"--eval_steps\", type=int, default=500,\n                        help=\"Evaluate every N steps\")\n    parser.add_argument(\"--save_steps\", type=int, default=500,\n                        help=\"Save checkpoint every N steps\")\n    parser.add_argument(\"--logging_steps\", type=int, default=10,\n                        help=\"Log every N steps\")\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05,\n                        help=\"Warmup ratio\")\n    parser.add_argument(\"--weight_decay\", type=float, default=0.01,\n                        help=\"Weight decay\")\n    parser.add_argument(\"--save_total_limit\", type=int, default=3,\n                        help=\"Keep only N most recent checkpoints\")\n    parser.add_argument(\"--save_only_model\", action=\"store_true\",\n                        help=\"Save only model weights (skip optimizer/scheduler/rng)\")\n    parser.add_argument(\"--resume_from_checkpoint\", type=str, default=None,\n                        help=\"Path to checkpoint directory to resume from\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True,\n                        help=\"Use bfloat16 (default: True)\")\n    parser.add_argument(\"--no_bf16\", action=\"store_true\",\n                        help=\"Disable bfloat16\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n    set_seed(args.seed)\n\n    if args.tau is None:\n        args.tau = 1.0 - args.contamination_ratio * 0.5\n    if args.n_min is None:\n        args.n_min = max(2, args.batch_size // 2)\n\n    use_bf16 = args.bf16 and not args.no_bf16\n\n    report_to = []\n    if args.use_wandb:\n        report_to.append(\"wandb\")\n        os.environ.setdefault(\"WANDB_PROJECT\", args.wandb_project)\n\n    print(f\"Loading tokenizer: {args.model_name}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"Loading model: {args.model_name}\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name,\n        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,\n        trust_remote_code=True,\n    )\n\n    print(f\"Loading training data: {args.data_path}\")\n    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)\n    print(f\"  {len(train_dataset)} examples loaded\")\n\n    eval_dataset = None\n    if args.eval_data_path:\n        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)\n        print(f\"  {len(eval_dataset)} eval examples loaded\")\n\n    # Convert num_train_tokens to max_steps\n    max_steps = args.max_steps\n    if max_steps <= 0 and args.num_train_tokens is not None:\n        tokens_per_step = (\n            args.batch_size * args.gradient_accumulation_steps * args.max_length\n        )\n        max_steps = args.num_train_tokens // tokens_per_step\n        print(f\"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}\")\n\n    log_path = os.path.join(args.output_dir, \"step_metrics.jsonl\")\n\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        run_name=args.wandb_run_name,\n        per_device_train_batch_size=args.batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,\n        max_steps=max_steps if max_steps > 0 else -1,\n        warmup_ratio=args.warmup_ratio,\n        weight_decay=args.weight_decay,\n        bf16=use_bf16,\n        logging_steps=args.logging_steps,\n        eval_steps=args.eval_steps if eval_dataset else None,\n        eval_strategy=\"steps\" if eval_dataset else \"no\",\n        save_steps=args.save_steps,\n        save_strategy=\"steps\",\n        save_total_limit=args.save_total_limit,\n        save_only_model=args.save_only_model,\n        load_best_model_at_end=eval_dataset is not None,\n        metric_for_best_model=\"eval_loss\" if eval_dataset else None,\n        report_to=report_to if report_to else \"none\",\n        seed=args.seed,\n        dataloader_drop_last=True,\n        remove_unused_columns=False,\n    )\n\n    trainer = WeightedTrainer(\n        weighting_method=args.weighting_method,\n        tau=args.tau,\n        n_min=args.n_min,\n        grid_b_value=args.grid_b_value,\n        log_path=log_path,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        data_collator=collate_fn,\n        tokenizer=tokenizer,\n    )\n\n    config_summary = {\n        \"model_name\": args.model_name,\n        \"weighting_method\": args.weighting_method,\n        \"grid_b_value\": args.grid_b_value if args.weighting_method == \"grid\" else None,\n        \"tau\": args.tau,\n        \"n_min\": args.n_min,\n        \"contamination_ratio\": args.contamination_ratio,\n        \"batch_size\": args.batch_size,\n        \"learning_rate\": args.learning_rate,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"num_examples\": len(train_dataset),\n    }\n    print(\"\\n=== Training Config ===\")\n    for k, v in config_summary.items():\n        print(f\"  {k}: {v}\")\n    print()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    with open(os.path.join(args.output_dir, \"config.json\"), \"w\") as f:\n        json.dump(config_summary, f, indent=2)\n\n    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)\n    trainer._flush_metrics()\n    trainer.save_model(os.path.join(args.output_dir, \"final\"))\n    print(f\"\\nTraining complete. Model saved to {args.output_dir}/final\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 213,
        "oldLines": 8,
        "newStart": 213,
        "newLines": 8,
        "lines": [
          "     parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-0.6B\",",
          "                         help=\"HuggingFace model name or path\")",
          "     parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",",
          "-                        choices=[\"uniform\", \"grid\", \"adaptive\"],",
          "-                        help=\"Weighting method: uniform / grid / adaptive\")",
          "+                        choices=[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"],",
          "+                        help=\"Weighting method: uniform / grid / adaptive / ess_only\")",
          "     parser.add_argument(\"--grid_b_value\", type=float, default=1.0,",
          "                         help=\"Fixed b value for grid method (one run per b, \"",
          "                              \"grid search selects best across runs)\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 28_

现在在 `compute_loss` 中添加 `ess_only` 分支。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "8446f9b7-77cf-41eb-bd79-4eca4b3c8f44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rfjc2Vp5iVcTpBLLzLoZ9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 35585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_011SndfBafwBjkHXdyivgbkE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "old_string": "        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:",
  "new_string": "        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"ess_only\":\n            b_val = find_ess_only_b(q_scores, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "63a916bf-6b29-4e96-803b-5c6bb18b332d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rfjc2Vp5iVcTpBLLzLoZ9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 35585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 30 · 2026-05-15T07:16:31.275Z_

<details><summary>↩ Tool result · `toolu_011SndfBafwBjkHXdyivgbkE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "aa594714-29c9-47cc-b61a-25c2d3f790d6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
    "oldString": "        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:",
    "newString": "        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"ess_only\":\n            b_val = find_ess_only_b(q_scores, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:",
    "originalFile": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports four weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)\n  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nimport time\nfrom pathlib import Path\n\nimport torch\nfrom torch.utils.data import Dataset\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    Trainer,\n    TrainingArguments,\n    set_seed,\n)\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\"))\nfrom weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_ess_only_b,\n    find_optimal_b,\n)\n\n\nGRID_B_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]\n\n\nclass WeightedTextDataset(Dataset):\n    def __init__(self, data_path: str, tokenizer, max_length: int = 2048):\n        self.tokenizer = tokenizer\n        self.max_length = max_length\n        self.examples = []\n\n        with open(data_path, \"r\") as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                item = json.loads(line)\n                self.examples.append(item)\n\n    def __len__(self):\n        return len(self.examples)\n\n    def __getitem__(self, idx):\n        item = self.examples[idx]\n        encoding = self.tokenizer(\n            item[\"text\"],\n            truncation=True,\n            max_length=self.max_length,\n            padding=\"max_length\",\n            return_tensors=\"pt\",\n        )\n        input_ids = encoding[\"input_ids\"].squeeze(0)\n        attention_mask = encoding[\"attention_mask\"].squeeze(0)\n        return {\n            \"input_ids\": input_ids,\n            \"attention_mask\": attention_mask,\n            \"labels\": input_ids.clone(),\n            \"q_score\": item.get(\"q_score\", 0.0),\n        }\n\n\ndef collate_fn(batch):\n    input_ids = torch.stack([x[\"input_ids\"] for x in batch])\n    attention_mask = torch.stack([x[\"attention_mask\"] for x in batch])\n    labels = torch.stack([x[\"labels\"] for x in batch])\n    q_scores = torch.tensor([x[\"q_score\"] for x in batch], dtype=torch.float32)\n    return {\n        \"input_ids\": input_ids,\n        \"attention_mask\": attention_mask,\n        \"labels\": labels,\n        \"q_scores\": q_scores,\n    }\n\n\nclass WeightedTrainer(Trainer):\n    def __init__(self, weighting_method: str, tau: float, n_min: int,\n                 grid_b_value: float = 0.0, log_path: str = None, **kwargs):\n        super().__init__(**kwargs)\n        self.weighting_method = weighting_method\n        self.tau = tau\n        self.n_min = n_min\n        self.grid_b_value = grid_b_value\n        self.log_path = log_path\n        self._step_metrics = []\n\n    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):\n        q_scores = inputs.pop(\"q_scores\")\n        labels = inputs.get(\"labels\")\n\n        outputs = model(**inputs)\n        logits = outputs.logits\n\n        shift_logits = logits[..., :-1, :].contiguous()\n        shift_labels = labels[..., 1:].contiguous()\n        attention_mask = inputs.get(\"attention_mask\")\n        if attention_mask is not None:\n            shift_mask = attention_mask[..., 1:].contiguous()\n        else:\n            shift_mask = torch.ones_like(shift_labels, dtype=torch.float32)\n\n        loss_fct = torch.nn.CrossEntropyLoss(reduction=\"none\")\n        per_token_loss = loss_fct(\n            shift_logits.view(-1, shift_logits.size(-1)),\n            shift_labels.view(-1),\n        ).view(shift_labels.size())\n\n        # Mask padding tokens\n        per_token_loss = per_token_loss * shift_mask\n\n        # Per-sample loss: mean over tokens\n        token_counts = shift_mask.sum(dim=-1).clamp(min=1)\n        per_sample_loss = per_token_loss.sum(dim=-1) / token_counts\n\n        unweighted_loss = per_sample_loss.mean()\n\n        b_val = 0.0\n        alpha_val = compute_alpha_eff(q_scores, 0.0)\n        ess_val = float(q_scores.numel())\n\n        if self.weighting_method == \"uniform\":\n            loss = unweighted_loss\n        elif self.weighting_method == \"grid\":\n            b_val = self.grid_b_value\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:\n            raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")\n\n        if model.training:\n            step_info = {\n                \"step\": self.state.global_step if self.state else 0,\n                \"loss\": float(loss.detach()),\n                \"unweighted_loss\": float(unweighted_loss.detach()),\n                \"b\": b_val,\n                \"alpha_eff\": alpha_val,\n                \"ess\": ess_val,\n                \"mean_q\": float(q_scores.mean()),\n                \"method\": self.weighting_method,\n            }\n            self._step_metrics.append(step_info)\n\n            if self.log_path and len(self._step_metrics) % 10 == 0:\n                self._flush_metrics()\n\n        return (loss, outputs) if return_outputs else loss\n\n    def _flush_metrics(self):\n        if not self._step_metrics or not self.log_path:\n            return\n        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)\n        with open(self.log_path, \"a\") as f:\n            for m in self._step_metrics:\n                f.write(json.dumps(m) + \"\\n\")\n        self._step_metrics = []\n\n    def training_step(self, model, inputs, num_items_in_batch=None):\n        result = super().training_step(model, inputs, num_items_in_batch=num_items_in_batch)\n\n        if self._step_metrics:\n            latest = self._step_metrics[-1]\n            self.log({\n                \"weighting/b\": latest[\"b\"],\n                \"weighting/alpha_eff\": latest[\"alpha_eff\"],\n                \"weighting/ess\": latest[\"ess\"],\n                \"weighting/mean_q\": latest[\"mean_q\"],\n                \"weighting/unweighted_loss\": latest[\"unweighted_loss\"],\n                \"weighting/weighted_loss\": latest[\"loss\"],\n            })\n\n        return result\n\n    def save_model(self, output_dir=None, _internal_call=False):\n        super().save_model(output_dir, _internal_call)\n        self._flush_metrics()\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(\n        description=\"Weighted pretraining for LMs on contaminated corpora\"\n    )\n    parser.add_argument(\"--data_path\", type=str, required=True,\n                        help=\"Path to training data (jsonl)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for checkpoints and logs\")\n    parser.add_argument(\"--model_name\", type=str, default=\"Qwen/Qwen3-0.6B\",\n                        help=\"HuggingFace model name or path\")\n    parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",\n                        choices=[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"],\n                        help=\"Weighting method: uniform / grid / adaptive / ess_only\")\n    parser.add_argument(\"--grid_b_value\", type=float, default=1.0,\n                        help=\"Fixed b value for grid method (one run per b, \"\n                             \"grid search selects best across runs)\")\n    parser.add_argument(\"--contamination_ratio\", type=float, default=0.2,\n                        help=\"Expected contamination ratio (for adaptive tau)\")\n    parser.add_argument(\"--num_train_tokens\", type=int, default=None,\n                        help=\"Total training tokens (converted to max_steps)\")\n    parser.add_argument(\"--max_steps\", type=int, default=-1,\n                        help=\"Max training steps (overrides num_train_tokens)\")\n    parser.add_argument(\"--num_train_epochs\", type=float, default=1.0,\n                        help=\"Number of training epochs\")\n    parser.add_argument(\"--batch_size\", type=int, default=4,\n                        help=\"Per-device training batch size\")\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=4,\n                        help=\"Gradient accumulation steps\")\n    parser.add_argument(\"--learning_rate\", type=float, default=5e-5,\n                        help=\"Learning rate\")\n    parser.add_argument(\"--max_length\", type=int, default=2048,\n                        help=\"Max sequence length\")\n    parser.add_argument(\"--tau\", type=float, default=None,\n                        help=\"Alpha_eff target threshold (adaptive). \"\n                             \"Defaults to 1 - contamination_ratio * 0.5\")\n    parser.add_argument(\"--n_min\", type=int, default=None,\n                        help=\"Minimum effective sample size. \"\n                             \"Defaults to batch_size // 2\")\n    parser.add_argument(\"--use_wandb\", action=\"store_true\",\n                        help=\"Enable Weights & Biases logging\")\n    parser.add_argument(\"--wandb_project\", type=str,\n                        default=\"provenance-weight-training\",\n                        help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run_name\", type=str, default=None,\n                        help=\"W&B run name (passed to TrainingArguments.run_name)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--eval_data_path\", type=str, default=None,\n                        help=\"Path to evaluation data (jsonl)\")\n    parser.add_argument(\"--eval_steps\", type=int, default=500,\n                        help=\"Evaluate every N steps\")\n    parser.add_argument(\"--save_steps\", type=int, default=500,\n                        help=\"Save checkpoint every N steps\")\n    parser.add_argument(\"--logging_steps\", type=int, default=10,\n                        help=\"Log every N steps\")\n    parser.add_argument(\"--warmup_ratio\", type=float, default=0.05,\n                        help=\"Warmup ratio\")\n    parser.add_argument(\"--weight_decay\", type=float, default=0.01,\n                        help=\"Weight decay\")\n    parser.add_argument(\"--save_total_limit\", type=int, default=3,\n                        help=\"Keep only N most recent checkpoints\")\n    parser.add_argument(\"--save_only_model\", action=\"store_true\",\n                        help=\"Save only model weights (skip optimizer/scheduler/rng)\")\n    parser.add_argument(\"--resume_from_checkpoint\", type=str, default=None,\n                        help=\"Path to checkpoint directory to resume from\")\n    parser.add_argument(\"--bf16\", action=\"store_true\", default=True,\n                        help=\"Use bfloat16 (default: True)\")\n    parser.add_argument(\"--no_bf16\", action=\"store_true\",\n                        help=\"Disable bfloat16\")\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n    set_seed(args.seed)\n\n    if args.tau is None:\n        args.tau = 1.0 - args.contamination_ratio * 0.5\n    if args.n_min is None:\n        args.n_min = max(2, args.batch_size // 2)\n\n    use_bf16 = args.bf16 and not args.no_bf16\n\n    report_to = []\n    if args.use_wandb:\n        report_to.append(\"wandb\")\n        os.environ.setdefault(\"WANDB_PROJECT\", args.wandb_project)\n\n    print(f\"Loading tokenizer: {args.model_name}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    print(f\"Loading model: {args.model_name}\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_name,\n        torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,\n        trust_remote_code=True,\n    )\n\n    print(f\"Loading training data: {args.data_path}\")\n    train_dataset = WeightedTextDataset(args.data_path, tokenizer, args.max_length)\n    print(f\"  {len(train_dataset)} examples loaded\")\n\n    eval_dataset = None\n    if args.eval_data_path:\n        eval_dataset = WeightedTextDataset(args.eval_data_path, tokenizer, args.max_length)\n        print(f\"  {len(eval_dataset)} eval examples loaded\")\n\n    # Convert num_train_tokens to max_steps\n    max_steps = args.max_steps\n    if max_steps <= 0 and args.num_train_tokens is not None:\n        tokens_per_step = (\n            args.batch_size * args.gradient_accumulation_steps * args.max_length\n        )\n        max_steps = args.num_train_tokens // tokens_per_step\n        print(f\"  num_train_tokens={args.num_train_tokens} → max_steps={max_steps}\")\n\n    log_path = os.path.join(args.output_dir, \"step_metrics.jsonl\")\n\n    training_args = TrainingArguments(\n        output_dir=args.output_dir,\n        run_name=args.wandb_run_name,\n        per_device_train_batch_size=args.batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        num_train_epochs=args.num_train_epochs if max_steps <= 0 else 100,\n        max_steps=max_steps if max_steps > 0 else -1,\n        warmup_ratio=args.warmup_ratio,\n        weight_decay=args.weight_decay,\n        bf16=use_bf16,\n        logging_steps=args.logging_steps,\n        eval_steps=args.eval_steps if eval_dataset else None,\n        eval_strategy=\"steps\" if eval_dataset else \"no\",\n        save_steps=args.save_steps,\n        save_strategy=\"steps\",\n        save_total_limit=args.save_total_limit,\n        save_only_model=args.save_only_model,\n        load_best_model_at_end=eval_dataset is not None,\n        metric_for_best_model=\"eval_loss\" if eval_dataset else None,\n        report_to=report_to if report_to else \"none\",\n        seed=args.seed,\n        dataloader_drop_last=True,\n        remove_unused_columns=False,\n    )\n\n    trainer = WeightedTrainer(\n        weighting_method=args.weighting_method,\n        tau=args.tau,\n        n_min=args.n_min,\n        grid_b_value=args.grid_b_value,\n        log_path=log_path,\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        eval_dataset=eval_dataset,\n        data_collator=collate_fn,\n        tokenizer=tokenizer,\n    )\n\n    config_summary = {\n        \"model_name\": args.model_name,\n        \"weighting_method\": args.weighting_method,\n        \"grid_b_value\": args.grid_b_value if args.weighting_method == \"grid\" else None,\n        \"tau\": args.tau,\n        \"n_min\": args.n_min,\n        \"contamination_ratio\": args.contamination_ratio,\n        \"batch_size\": args.batch_size,\n        \"learning_rate\": args.learning_rate,\n        \"max_steps\": max_steps,\n        \"seed\": args.seed,\n        \"num_examples\": len(train_dataset),\n    }\n    print(\"\\n=== Training Config ===\")\n    for k, v in config_summary.items():\n        print(f\"  {k}: {v}\")\n    print()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    with open(os.path.join(args.output_dir, \"config.json\"), \"w\") as f:\n        json.dump(config_summary, f, indent=2)\n\n    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)\n    trainer._flush_metrics()\n    trainer.save_model(os.path.join(args.output_dir, \"final\"))\n    print(f\"\\nTraining complete. Model saved to {args.output_dir}/final\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 151,
        "oldLines": 6,
        "newStart": 151,
        "newLines": 13,
        "lines": [
          "             loss = (per_sample_loss * weights).sum() / weights.sum()",
          "             alpha_val = compute_alpha_eff(q_scores, b_val)",
          "             ess_val = compute_ess(q_scores, b_val)",
          "+        elif self.weighting_method == \"ess_only\":",
          "+            b_val = find_ess_only_b(q_scores, n_min=self.n_min)",
          "+            weights = compute_sample_weights(q_scores, b_val)",
          "+            weights = weights.to(per_sample_loss.device)",
          "+            loss = (per_sample_loss * weights).sum() / weights.sum()",
          "+            alpha_val = compute_alpha_eff(q_scores, b_val)",
          "+            ess_val = compute_ess(q_scores, b_val)",
          "         else:",
          "             raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 31_

创建运行脚本和文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "3fcc30a3-caea-4118-a38e-9a5114f017ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9pZDw2yTkYYT4aEtPXYZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 35857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01BckiiL4w2Q9bFRdCcH85Jm`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check training directory existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "c23bf02b-aa20-43c5-a82a-bd94c08b6f05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9pZDw2yTkYYT4aEtPXYZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 35857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 33 · 2026-05-15T07:16:34.697Z_

<details><summary>↩ Tool result · `toolu_01BckiiL4w2Q9bFRdCcH85Jm`</summary>

```text
DIR_NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "213dc807-0332-4fd8-ade2-e3f27eb21780",
  "tool_use_result": {
    "stdout": "DIR_NOT_FOUND",
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01XK2amLxyGvqsn9YYatycTZ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ 2>/dev/null",
  "description": "Check artifacts directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "2194609b-9c7a-4d8d-975c-7572041055ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9pZDw2yTkYYT4aEtPXYZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 35857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 35 · 2026-05-15T07:16:35.274Z_

<details><summary>↩ Tool result · `toolu_01XK2amLxyGvqsn9YYatycTZ`</summary>

```text
_project
bstar_distribution_analysis.md
data_generation
detector
drayson_comparison.md
dream_reports
evaluation
experiment_setup_draft.md
grid_b5_0_seed123
interim_mvp_analysis.md
literature_diff_drayson.md
literature_notes.md
manifest.yaml
method_section_draft.md
mvp_analysis_draft.md
mvp_analysis_summary.md
new_scripts_manifest.md
novelty_drayson_analysis.md
q1_ess_equivalence_analysis.md
related_work_notes.md
run_mvp.sh
seed42_diagnostic.md
tau_fix_changelog.md
training
training_progress_check.md
weighting
worker_output.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "e24167d5-395a-4594-a474-846b4c58b12c",
  "tool_use_result": {
    "stdout": "_project\nbstar_distribution_analysis.md\ndata_generation\ndetector\ndrayson_comparison.md\ndream_reports\nevaluation\nexperiment_setup_draft.md\ngrid_b5_0_seed123\ninterim_mvp_analysis.md\nliterature_diff_drayson.md\nliterature_notes.md\nmanifest.yaml\nmethod_section_draft.md\nmvp_analysis_draft.md\nmvp_analysis_summary.md\nnew_scripts_manifest.md\nnovelty_drayson_analysis.md\nq1_ess_equivalence_analysis.md\nrelated_work_notes.md\nrun_mvp.sh\nseed42_diagnostic.md\ntau_fix_changelog.md\ntraining\ntraining_progress_check.md\nweighting\nworker_output.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 36_

`training/` 目录在任务描述中指定但不存在于项目根目录，脚本实际在 `artifacts/training/` 下。按任务要求的路径创建。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "dc440d36-1357-48c4-99d1-35b26082dc8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DdoL2cB4Zz4eGouRco48b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 36509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
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

<details open><summary>🔧 Tool call — Bash · `toolu_01JUxExrfT3eibvGneq66Y2X`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training",
  "description": "Create training directory at project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "9cb8bed6-5292-41f4-aa20-8a6bc7876fc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DdoL2cB4Zz4eGouRco48b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 36509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
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

_source line 38 · 2026-05-15T07:16:40.316Z_

<details><summary>↩ Tool result · `toolu_01JUxExrfT3eibvGneq66Y2X`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "7c312886-8cfb-4cfe-9105-bc284407c17e",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Write · `toolu_01WRPjLfrMgR38DeoLyLvs1L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training/run_ess_only_seed42.sh",
  "content": "#!/bin/bash\n# ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) >= n_min}\n# Purpose: prove min-intervention (adaptive) > max-intervention (ess_only)\n\nsource /root/miniconda3/etc/profile.d/conda.sh\nconda activate base\ncd /root/provenance_weight_training\n\nWANDB_MODE=disabled python training/pretrain_weighted.py \\\n    --data_path data/scored_data.jsonl \\\n    --output_dir output/models/ess_only_seed42 \\\n    --weighting_method ess_only \\\n    --model_name models/Qwen/Qwen3-0.6B \\\n    --num_train_tokens 200000000 \\\n    --batch_size 4 \\\n    --gradient_accumulation_steps 4 \\\n    --max_length 2048 \\\n    --learning_rate 5e-5 \\\n    --seed 42 \\\n    --logging_steps 10 \\\n    --save_steps 500 \\\n    --save_total_limit 2 \\\n    --save_only_model \\\n    --contamination_ratio 0.4 \\\n    --tau 0.8 \\\n    --bf16\n\necho \"ESS-only seed42 training complete\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "f1336ac3-6cd7-4b2e-a59f-8fd632b3d135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfQQK2oQEY1izGanrEGoYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 178,
      "cache_read_input_tokens": 36984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 178
      },
      "output_tokens": 59,
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

_source line 40 · 2026-05-15T07:16:51.841Z_

<details><summary>↩ Tool result · `toolu_01WRPjLfrMgR38DeoLyLvs1L`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training/run_ess_only_seed42.sh
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "b2a0b1e7-bf68-48c9-a818-8963b49a689a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training/run_ess_only_seed42.sh",
    "content": "#!/bin/bash\n# ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) >= n_min}\n# Purpose: prove min-intervention (adaptive) > max-intervention (ess_only)\n\nsource /root/miniconda3/etc/profile.d/conda.sh\nconda activate base\ncd /root/provenance_weight_training\n\nWANDB_MODE=disabled python training/pretrain_weighted.py \\\n    --data_path data/scored_data.jsonl \\\n    --output_dir output/models/ess_only_seed42 \\\n    --weighting_method ess_only \\\n    --model_name models/Qwen/Qwen3-0.6B \\\n    --num_train_tokens 200000000 \\\n    --batch_size 4 \\\n    --gradient_accumulation_steps 4 \\\n    --max_length 2048 \\\n    --learning_rate 5e-5 \\\n    --seed 42 \\\n    --logging_steps 10 \\\n    --save_steps 500 \\\n    --save_total_limit 2 \\\n    --save_only_model \\\n    --contamination_ratio 0.4 \\\n    --tau 0.8 \\\n    --bf16\n\necho \"ESS-only seed42 training complete\"\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_013a2n2qQsizLTQcvsTjq5fD`</summary>

```json
{
  "command": "chmod +x /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/training/run_ess_only_seed42.sh",
  "description": "Make script executable"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "65e5cbba-3bba-4831-95a4-e39fb0fdf25f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCE33iLL5Z3w2ZM1SE9xoD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 37162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 599
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

_source line 42 · 2026-05-15T07:16:55.173Z_

<details><summary>↩ Tool result · `toolu_013a2n2qQsizLTQcvsTjq5fD`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "1ae65d31-2703-413d-8d3b-5a2f90fb50ca",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 43_

写文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "d640d341-46fe-449f-a403-f50dbbaf5933",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4iPq4DRn1DV4s6nPt7Skd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 37761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
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

_source line 44_

<details open><summary>🔧 Tool call — Write · `toolu_01RgyMVucjMKqQih3MnLqnFR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ess_only_implementation.md",
  "content": "# ESS-only Baseline Implementation\n\n## 修改文件\n\n### 1. `artifacts/weighting/alpha_eff.py`\n- **新增函数 `find_ess_only_b`**（第 82–103 行区域）\n- 在 `compute_sample_weights` 前插入\n\n### 2. `artifacts/training/pretrain_weighted.py`\n- **import**：新增 `find_ess_only_b`\n- **docstring**：更新为 4 种方法\n- **argparse choices**：`[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"]`\n- **compute_loss**：新增 `ess_only` 分支，调用 `find_ess_only_b`\n\n### 3. `training/run_ess_only_seed42.sh`（新建）\n- 运行脚本，`--weighting_method ess_only`，seed=42，200M tokens\n\n## b* 计算算法\n\n**ESS-only**: `b* = max{b ≥ 0 : ESS(b) ≥ n_min}`\n\nESS(b) 对 b 单调非递增（b 越大，权重越不均匀，ESS 越小），因此用二分搜索：\n- 搜索范围 `[0, b_max]`，`b_max=20.0`\n- 精度 `tol=0.01`\n- 若 `ESS(0) < n_min`，返回 0（数据本身 ESS 不足）\n- 若 `ESS(b_max) ≥ n_min`，返回 `b_max`\n- 否则二分找 `lo` 使得 `ESS(lo) ≥ n_min` 且 `ESS(hi) < n_min`\n\n## 与 adaptive 的关键差异\n\n| | adaptive (ours) | ess_only (baseline) |\n|---|---|---|\n| 目标 | `inf{b : α_eff(b) ≥ τ}` s.t. `ESS ≥ n_min` | `max{b : ESS(b) ≥ n_min}` |\n| 准则 | 最小干预（minimum intervention） | 最大干预（maximum intervention） |\n| b* 大小 | 较小（刚好满足 α_eff 阈值） | 较大（推到 ESS 边界） |\n| α_eff 约束 | 有（≥ τ） | 无 |\n| 预期效果 | 保留更多数据信号 | 过度下权导致信息损失 |\n\nadaptive 找到最小的 b 使 α_eff 达标（保守），ess_only 找最大的 b 直到 ESS 刚好够（激进）。ess_only 的 b* ≥ adaptive 的 b*。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "b58297a6-282e-4c21-947d-ebaf2bfbd84f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4iPq4DRn1DV4s6nPt7Skd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 37761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 133
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

_source line 45 · 2026-05-15T07:17:12.733Z_

<details><summary>↩ Tool result · `toolu_01RgyMVucjMKqQih3MnLqnFR`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ess_only_implementation.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "86e6b9e2-4bce-4600-865d-75ee27536ad5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/ess_only_implementation.md",
    "content": "# ESS-only Baseline Implementation\n\n## 修改文件\n\n### 1. `artifacts/weighting/alpha_eff.py`\n- **新增函数 `find_ess_only_b`**（第 82–103 行区域）\n- 在 `compute_sample_weights` 前插入\n\n### 2. `artifacts/training/pretrain_weighted.py`\n- **import**：新增 `find_ess_only_b`\n- **docstring**：更新为 4 种方法\n- **argparse choices**：`[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"]`\n- **compute_loss**：新增 `ess_only` 分支，调用 `find_ess_only_b`\n\n### 3. `training/run_ess_only_seed42.sh`（新建）\n- 运行脚本，`--weighting_method ess_only`，seed=42，200M tokens\n\n## b* 计算算法\n\n**ESS-only**: `b* = max{b ≥ 0 : ESS(b) ≥ n_min}`\n\nESS(b) 对 b 单调非递增（b 越大，权重越不均匀，ESS 越小），因此用二分搜索：\n- 搜索范围 `[0, b_max]`，`b_max=20.0`\n- 精度 `tol=0.01`\n- 若 `ESS(0) < n_min`，返回 0（数据本身 ESS 不足）\n- 若 `ESS(b_max) ≥ n_min`，返回 `b_max`\n- 否则二分找 `lo` 使得 `ESS(lo) ≥ n_min` 且 `ESS(hi) < n_min`\n\n## 与 adaptive 的关键差异\n\n| | adaptive (ours) | ess_only (baseline) |\n|---|---|---|\n| 目标 | `inf{b : α_eff(b) ≥ τ}` s.t. `ESS ≥ n_min` | `max{b : ESS(b) ≥ n_min}` |\n| 准则 | 最小干预（minimum intervention） | 最大干预（maximum intervention） |\n| b* 大小 | 较小（刚好满足 α_eff 阈值） | 较大（推到 ESS 边界） |\n| α_eff 约束 | 有（≥ τ） | 无 |\n| 预期效果 | 保留更多数据信号 | 过度下权导致信息损失 |\n\nadaptive 找到最小的 b 使 α_eff 达标（保守），ess_only 找最大的 b 直到 ESS 刚好够（激进）。ess_only 的 b* ≥ adaptive 的 b*。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 46_

验证修改后的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "59385ea3-fc7f-4f33-bfff-8dc3a400db16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3cFBew1cTCwSwk3ZpeseB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 37894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 945
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

<details open><summary>🔧 Tool call — Read · `toolu_01Ae9TnvGidrmgzWtDKmSE5f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "offset": 1,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "3fe3ea4d-a5c3-4453-a622-2708cb527df2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3cFBew1cTCwSwk3ZpeseB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 37894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 945
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

_source line 48 · 2026-05-15T07:17:15.525Z_

<details><summary>↩ Tool result · `toolu_01Ae9TnvGidrmgzWtDKmSE5f`</summary>

```text
1	"""Weighted pretraining for Qwen3-0.6B on contaminated corpora.
2	
3	Supports four weighting methods:
4	  - uniform:  all samples equally weighted (baseline)
5	  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run
6	               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.
7	  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)
8	  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)
9	
10	Data format: jsonl with {"text": "...", "q_score": 0.xx, "label": "human"/"synthetic"}
11	"""
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "9352a446-be82-4627-8e9b-fe4509895a89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
      "content": "\"\"\"Weighted pretraining for Qwen3-0.6B on contaminated corpora.\n\nSupports four weighting methods:\n  - uniform:  all samples equally weighted (baseline)\n  - grid:     fixed b value per run (Drayson et al. EMNLP 2025). Grid search = run\n               once per b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, pick best val ppl.\n  - adaptive: batch-adaptive b* via α_eff convergence theory (ours, min-intervention)\n  - ess_only: b* = max{b : ESS(b) ≥ n_min} (max-intervention baseline)\n\nData format: jsonl with {\"text\": \"...\", \"q_score\": 0.xx, \"label\": \"human\"/\"synthetic\"}\n\"\"\"\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01DDwP13H8z84uuA8DgyzVE4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "offset": 30,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "f67af2e7-528d-44ee-9232-4700d17bd5f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3cFBew1cTCwSwk3ZpeseB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 37894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 945
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

_source line 50 · 2026-05-15T07:17:16.460Z_

<details><summary>↩ Tool result · `toolu_01DDwP13H8z84uuA8DgyzVE4`</summary>

```text
30	
31	sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
32	from weighting.alpha_eff import (
33	    compute_alpha_eff,
34	    compute_ess,
35	    compute_sample_weights,
36	    find_ess_only_b,
37	    find_optimal_b,
38	)
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "f6c30c7d-3091-4728-8e98-0c9a8a87e81b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
      "content": "\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\"))\nfrom weighting.alpha_eff import (\n    compute_alpha_eff,\n    compute_ess,\n    compute_sample_weights,\n    find_ess_only_b,\n    find_optimal_b,\n)\n",
      "numLines": 10,
      "startLine": 30,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01UqkxoL1ZcgWLEJy3y7QAby`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "offset": 144,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "a362b407-47e3-4546-82c6-e43e7c915403",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3cFBew1cTCwSwk3ZpeseB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 37894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 945
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

_source line 52 · 2026-05-15T07:17:17.404Z_

<details><summary>↩ Tool result · `toolu_01UqkxoL1ZcgWLEJy3y7QAby`</summary>

```text
144	            loss = (per_sample_loss * weights).sum() / weights.sum()
145	            alpha_val = compute_alpha_eff(q_scores, b_val)
146	            ess_val = compute_ess(q_scores, b_val)
147	        elif self.weighting_method == "adaptive":
148	            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)
149	            weights = compute_sample_weights(q_scores, b_val)
150	            weights = weights.to(per_sample_loss.device)
151	            loss = (per_sample_loss * weights).sum() / weights.sum()
152	            alpha_val = compute_alpha_eff(q_scores, b_val)
153	            ess_val = compute_ess(q_scores, b_val)
154	        elif self.weighting_method == "ess_only":
155	            b_val = find_ess_only_b(q_scores, n_min=self.n_min)
156	            weights = compute_sample_weights(q_scores, b_val)
157	            weights = weights.to(per_sample_loss.device)
158	            loss = (per_sample_loss * weights).sum() / weights.sum()
159	            alpha_val = compute_alpha_eff(q_scores, b_val)
160	            ess_val = compute_ess(q_scores, b_val)
161	        else:
162	            raise ValueError(f"Unknown weighting method: {self.weighting_method}")
163	
164	        if model.training:
165	            step_info = {
166	                "step": self.state.global_step if self.state else 0,
167	                "loss": float(loss.detach()),
168	                "unweighted_loss": float(unweighted_loss.detach()),
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "4fffceee-23dc-49e3-91af-96b073db0c32",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
      "content": "            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"adaptive\":\n            b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        elif self.weighting_method == \"ess_only\":\n            b_val = find_ess_only_b(q_scores, n_min=self.n_min)\n            weights = compute_sample_weights(q_scores, b_val)\n            weights = weights.to(per_sample_loss.device)\n            loss = (per_sample_loss * weights).sum() / weights.sum()\n            alpha_val = compute_alpha_eff(q_scores, b_val)\n            ess_val = compute_ess(q_scores, b_val)\n        else:\n            raise ValueError(f\"Unknown weighting method: {self.weighting_method}\")\n\n        if model.training:\n            step_info = {\n                \"step\": self.state.global_step if self.state else 0,\n                \"loss\": float(loss.detach()),\n                \"unweighted_loss\": float(unweighted_loss.detach()),",
      "numLines": 25,
      "startLine": 144,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01U99rtyBCW2jPLLhKZ2Ew5Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "offset": 214,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "561529ad-076f-423b-92e0-9edefede023a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3cFBew1cTCwSwk3ZpeseB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 37894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 945
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

_source line 54 · 2026-05-15T07:17:18.098Z_

<details><summary>↩ Tool result · `toolu_01U99rtyBCW2jPLLhKZ2Ew5Z`</summary>

```text
214	        description="Weighted pretraining for LMs on contaminated corpora"
215	    )
216	    parser.add_argument("--data_path", type=str, required=True,
217	                        help="Path to training data (jsonl)")
218	    parser.add_argument("--output_dir", type=str, required=True,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "672056bc-c547-41d2-a991-bfd22a551f93",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
      "content": "        description=\"Weighted pretraining for LMs on contaminated corpora\"\n    )\n    parser.add_argument(\"--data_path\", type=str, required=True,\n                        help=\"Path to training data (jsonl)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,",
      "numLines": 5,
      "startLine": 214,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01AcpsyFGTDjG3Ev5HKuE9GC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
  "offset": 222,
  "limit": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "1ab62a12-944d-4d4e-a9f7-e4babfd3672f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCh1ibpSerck4GD54qN9LB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1475,
      "cache_read_input_tokens": 38839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1475
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

_source line 56 · 2026-05-15T07:17:22.404Z_

<details><summary>↩ Tool result · `toolu_01AcpsyFGTDjG3Ev5HKuE9GC`</summary>

```text
222	    parser.add_argument("--weighting_method", type=str, default="adaptive",
223	                        choices=["uniform", "grid", "adaptive", "ess_only"],
224	                        help="Weighting method: uniform / grid / adaptive / ess_only")
225	    parser.add_argument("--grid_b_value", type=float, default=1.0,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "2df53cf7-4f93-47e7-898a-129f9f2e1e04",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/training/pretrain_weighted.py",
      "content": "    parser.add_argument(\"--weighting_method\", type=str, default=\"adaptive\",\n                        choices=[\"uniform\", \"grid\", \"adaptive\", \"ess_only\"],\n                        help=\"Weighting method: uniform / grid / adaptive / ess_only\")\n    parser.add_argument(\"--grid_b_value\", type=float, default=1.0,",
      "numLines": 4,
      "startLine": 222,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01RDcDeAQQpfQjZuBjM7cXF2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
  "offset": 81,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "38d19827-6510-4430-85e8-cc49f72fc1ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWo2oh5fk6Y1rT54nn4eba",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 40314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 232
      },
      "output_tokens": 70,
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

_source line 58 · 2026-05-15T07:17:24.951Z_

<details><summary>↩ Tool result · `toolu_01RDcDeAQQpfQjZuBjM7cXF2`</summary>

```text
81	def find_optimal_b(
82	    q_scores: torch.Tensor,
83	    tau: float,
84	    n_min: int,
85	    b_max: float = 20.0,
86	    resolution: int = 1000,
87	) -> float:
88	    """Find b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b*) ≥ n_min.
89	
90	    When the batch is clean enough (ρ̂ < 1 − τ), returns b=0 (uniform).
91	    When the ESS constraint conflicts with the α_eff threshold, returns
92	    b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min.
93	    """
94	    alpha_0 = compute_alpha_eff(q_scores, 0.0)
95	    if alpha_0 >= tau:
96	        return 0.0
97	
98	    n = q_scores.numel()
99	    if n_min > n:
100	        n_min = n
101	
102	    # Phase 1: grid search to find the feasible region
103	    grid = torch.linspace(0.0, b_max, resolution + 1).tolist()
104	
105	    best_feasible_b = 0.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "5a612087-42e2-458b-887d-811597b7355e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
      "content": "def find_optimal_b(\n    q_scores: torch.Tensor,\n    tau: float,\n    n_min: int,\n    b_max: float = 20.0,\n    resolution: int = 1000,\n) -> float:\n    \"\"\"Find b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b*) ≥ n_min.\n\n    When the batch is clean enough (ρ̂ < 1 − τ), returns b=0 (uniform).\n    When the ESS constraint conflicts with the α_eff threshold, returns\n    b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min.\n    \"\"\"\n    alpha_0 = compute_alpha_eff(q_scores, 0.0)\n    if alpha_0 >= tau:\n        return 0.0\n\n    n = q_scores.numel()\n    if n_min > n:\n        n_min = n\n\n    # Phase 1: grid search to find the feasible region\n    grid = torch.linspace(0.0, b_max, resolution + 1).tolist()\n\n    best_feasible_b = 0.0",
      "numLines": 25,
      "startLine": 81,
      "totalLines": 254
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

查看新增的 `find_ess_only_b` 函数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "31e69617-691b-430e-9615-ad234655ce1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHMJiRadAcSVyTjBHHzsN3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 40546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
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

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01SyeEX9r6pX5ZVnuakAXCHu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
  "offset": 140,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "e38cac5e-ed2c-4bce-bfe0-10253b8e51df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHMJiRadAcSVyTjBHHzsN3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 40546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
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

_source line 61 · 2026-05-15T07:17:28.573Z_

<details><summary>↩ Tool result · `toolu_01SyeEX9r6pX5ZVnuakAXCHu`</summary>

```text
140	def find_ess_only_b(
141	    q_scores: torch.Tensor,
142	    n_min: int,
143	    b_max: float = 20.0,
144	    tol: float = 0.01,
145	) -> float:
146	    """Find b* = max{b : ESS(b) >= n_min} (ESS-only, no alpha_eff constraint).
147	
148	    ESS(b) is monotonically non-increasing in b, so binary search works.
149	    Returns b_max if ESS(b_max) >= n_min; returns 0.0 if ESS(0) < n_min.
150	    """
151	    if compute_ess(q_scores, 0.0) < n_min:
152	        return 0.0
153	
154	    if compute_ess(q_scores, b_max) >= n_min:
155	        return b_max
156	
157	    lo, hi = 0.0, b_max
158	    while hi - lo > tol:
159	        mid = (lo + hi) / 2.0
160	        if compute_ess(q_scores, mid) >= n_min:
161	            lo = mid
162	        else:
163	            hi = mid
164	    return lo
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "ee2d9fe3-8451-45e2-a7d7-d897b110d005",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/weighting/alpha_eff.py",
      "content": "def find_ess_only_b(\n    q_scores: torch.Tensor,\n    n_min: int,\n    b_max: float = 20.0,\n    tol: float = 0.01,\n) -> float:\n    \"\"\"Find b* = max{b : ESS(b) >= n_min} (ESS-only, no alpha_eff constraint).\n\n    ESS(b) is monotonically non-increasing in b, so binary search works.\n    Returns b_max if ESS(b_max) >= n_min; returns 0.0 if ESS(0) < n_min.\n    \"\"\"\n    if compute_ess(q_scores, 0.0) < n_min:\n        return 0.0\n\n    if compute_ess(q_scores, b_max) >= n_min:\n        return b_max\n\n    lo, hi = 0.0, b_max\n    while hi - lo > tol:\n        mid = (lo + hi) / 2.0\n        if compute_ess(q_scores, mid) >= n_min:\n            lo = mid\n        else:\n            hi = mid\n    return lo",
      "numLines": 25,
      "startLine": 140,
      "totalLines": 254
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

所有修改正确。注意任务要求脚本路径和 `pretrain_weighted.py` 路径在 `training/` 下，但代码实际在 `artifacts/training/`。服务器端的 `training/` 目录会包含脚本，而服务器上的 `pretrain_weighted.py` 路径可能也是 `training/pretrain_weighted.py`（通过 sync_code）。脚本中 `python training/pretrain_weighted.py` 的路径需要与服务器目录结构一致。

完成。修改总结：

**`artifacts/weighting/alpha_eff.py`**：新增 `find_ess_only_b(q_scores, n_min, b_max=20.0, tol=0.01)` — 二分搜索找 `max{b : ESS(b) ≥ n_min}`。

**`artifacts/training/pretrain_weighted.py`**：
- import 新增 `find_ess_only_b`
- argparse choices 加入 `ess_only`
- `compute_loss` 新增 `ess_only` 分支，调用 `find_ess_only_b` 计算 b*

**`training/run_ess_only_seed42.sh`**：新建运行脚本（已 chmod +x）

**`artifacts/ess_only_implementation.md`**：实现文档

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "uuid": "fb1e6e8c-abf1-4e2a-856a-c6e95012fe83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018e8TDGmtsEACJFtUcCDSPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 41153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 497
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

_source line 63_

所有修改正确。注意任务要求脚本路径和 `pretrain_weighted.py` 路径在 `training/` 下，但代码实际在 `artifacts/training/`。服务器端的 `training/` 目录会包含脚本，而服务器上的 `pretrain_weighted.py` 路径可能也是 `training/pretrain_weighted.py`（通过 sync_code）。脚本中 `python training/pretrain_weighted.py` 的路径需要与服务器目录结构一致。

完成。修改总结：

**`artifacts/weighting/alpha_eff.py`**：新增 `find_ess_only_b(q_scores, n_min, b_max=20.0, tol=0.01)` — 二分搜索找 `max{b : ESS(b) ≥ n_min}`。

**`artifacts/training/pretrain_weighted.py`**：
- import 新增 `find_ess_only_b`
- argparse choices 加入 `ess_only`
- `compute_loss` 新增 `ess_only` 分支，调用 `find_ess_only_b` 计算 b*

**`training/run_ess_only_seed42.sh`**：新建运行脚本（已 chmod +x）

**`artifacts/ess_only_implementation.md`**：实现文档

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 127956,
  "duration_api_ms": 128938,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "f02c10a7-7439-4455-89de-6141ba8f011e",
  "total_cost_usd": 0.67458075,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 29809,
    "cache_read_input_tokens": 670241,
    "output_tokens": 6041,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29809,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 384,
        "cache_read_input_tokens": 41153,
        "cache_creation_input_tokens": 497,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 497
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1939,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0020239999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 6041,
      "cacheReadInputTokens": 670241,
      "cacheCreationInputTokens": 29809,
      "webSearchRequests": 0,
      "costUSD": 0.6725567499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1fce845c-07dd-4463-8ceb-1d812e33cc75"
}
```

</details>

---
