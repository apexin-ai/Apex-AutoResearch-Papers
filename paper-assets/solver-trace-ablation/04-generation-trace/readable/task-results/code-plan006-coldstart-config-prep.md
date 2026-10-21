# code plan006 coldstart config prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-coldstart-config-prep_20260514T070756_result.json`
- **Structured JSON:** [`01cf04fac16653934bf3.json`](../../sessions/01/01cf04fac16653934bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置文件创建成功，YAML 可正常读取。

### 汇报

**新配置文件**: `/root/solver-trace-ablation/configs/grpo_prolog_exec_only_k16_warmup.yaml`
- `num_generations: 16` (原值 8)
- `warmup_ratio: 0.1` (新增)
- `output_dir` 改为 `grpo_prolog_exec_only_k16_warmup`
- 其余参数与原配置一致

**CLI override 可行性**:
- `--num_generations 16` — **可行**，argparse 已有该参数 (L328)，且传入 `GRPOConfig` (L415)
- `--warmup_ratio 0.1` — **不可行**，存在两个问题：
  1. argparse 没有定义 `--warmup_ratio`，CLI 直接传会报错
  2. YAML 加载路径虽然能把 `warmup_ratio` 设为 `args.warmup_ratio`（通过 `setattr`），但 `GRPOConfig(...)` 构造函数 (L408-427) **没有传入 `warmup_ratio`**，所以该值会被静默忽略

**需要修复** `scripts/train_grpo.py`：
1. 添加 `parser.add_argument("--warmup_ratio", type=float, default=0.0)`
2. 在 `GRPOConfig(...)` 中加入 `warmup_ratio=args.warmup_ratio`

是否现在修复？

---
