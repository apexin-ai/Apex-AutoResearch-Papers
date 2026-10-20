# fix config merge bug

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_config-merge-bug_20260516T030423_result.json`
- **Structured JSON:** [`212143fbf22934b3022f.json`](../../sessions/21/212143fbf22934b3022f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 修改的参数（13 个）

| 参数 | 旧 default | 新 default |
|---|---|---|
| `--num_steps` | `100` | `None` |
| `--per_device_batch_size` | `4` | `None` |
| `--gradient_accumulation_steps` | `2` | `None` |
| `--num_generations` | `4` | `None` |
| `--max_completion_length` | `512` | `None` |
| `--learning_rate` | `1e-6` | `None` |
| `--exec_weight` | `0.5` | `None` |
| `--sta_weight` | `0.5` | `None` |
| `--beta` | `0.3` | `None` |
| `--beta_schedule` | `"fixed"` | `None` |
| `--beta_schedule_midpoint` | `250` | `None` |
| `--seed` | `42` | `None` |
| `--warmup_ratio` | `0.0` | `None` |

**未改的参数：**
- `--model_path`, `--data_path`, `--reward_mode`, `--output_dir`, `--solver`, `--logic_type`, `--wandb_project`, `--wandb_run`, `--config` — 本来就是 `default=None`
- `--no_wandb` — `action="store_true"` bool flag，不受此 bug 影响

### 2. Config merge 逻辑

不需要改。原逻辑 `if current is None` 在 argparse defaults 改为 None 后已能正确让 YAML config 值覆盖。优先级链现在是：**CLI 显式传参 > YAML config > 代码 fallback defaults**。

### 3. Diff（config merge fix 部分）

```diff
-    parser.add_argument("--num_steps", type=int, default=100)
-    parser.add_argument("--per_device_batch_size", type=int, default=4)
-    parser.add_argument("--gradient_accumulation_steps", type=int, default=2)
-    parser.add_argument("--num_generations", type=int, default=4)
-    parser.add_argument("--max_completion_length", type=int, default=512)
-    parser.add_argument("--learning_rate", type=float, default=1e-6)
-    parser.add_argument("--exec_weight", type=float, default=0.5)
-    parser.add_argument("--sta_weight", type=float, default=0.5)
-    parser.add_argument("--beta", type=float, default=0.3,
-    parser.add_argument("--beta_schedule", type=str, default="fixed",
-    parser.add_argument("--beta_schedule_midpoint", type=int, default=250,
-    parser.add_argument("--seed", type=int, default=42)
-    parser.add_argument("--warmup_ratio", type=float, default=0.0)
+    parser.add_argument("--num_steps", type=int, default=None)
+    parser.add_argument("--per_device_batch_size", type=int, default=None)
+    parser.add_argument("--gradient_accumulation_steps", type=int, default=None)
+    parser.add_argument("--num_generations", type=int, default=None)
+    parser.add_argument("--max_completion_length", type=int, default=None)
+    parser.add_argument("--learning_rate", type=float, default=None)
+    parser.add_argument("--exec_weight", type=float, default=None)
+    parser.add_argument("--sta_weight", type=float, default=None)
+    parser.add_argument("--beta", type=float, default=None,
+    parser.add_argument("--beta_schedule", type=str, default=None,
+    parser.add_argument("--beta_schedule_midpoint", type=int, default=None,
+    parser.add_argument("--seed", type=int, default=None)
+    parser.add_argument("--warmup_ratio", type=float, default=None)

     # Apply defaults for optional args after config merge
+    if args.num_steps is None:
+        args.num_steps = 100
+    if args.per_device_batch_size is None:
+        args.per_device_batch_size = 4
+    if args.gradient_accumulation_steps is None:
+        args.gradient_accumulation_steps = 2
+    if args.num_generations is None:
+        args.num_generations = 4
+    if args.max_completion_length is None:
+        args.max_completion_length = 512
+    if args.learning_rate is None:
+        args.learning_rate = 1e-6
+    if args.exec_weight is None:
+        args.exec_weight = 0.5
+    if args.sta_weight is None:
+        args.sta_weight = 0.5
+    if args.beta is None:
+        args.beta = 0.3
+    if args.beta_schedule is None:
+        args.beta_schedule = "fixed"
+    if args.beta_schedule_midpoint is None:
+        args.beta_schedule_midpoint = 250
+    if args.seed is None:
+        args.seed = 42
+    if args.warmup_ratio is None:
+        args.warmup_ratio = 0.0
     if args.solver is None:
         args.solver = "prover9"
     if args.logic_type is None:
         args.logic_type = "fol"
```

### 4. 本地同步

服务器上无 git 仓库，本地 repo 只有 `artifacts/train_grpo.py`（旧版本）。修改只在服务器 `/root/solver-trace-ablation/scripts/train_grpo.py` 生效。下次 `sync_code_to_remote` 推送前需确保本地也有对应文件，否则会被覆盖。

---
