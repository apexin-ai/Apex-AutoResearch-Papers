# check plan006 data readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan006-data-readiness_20260514T105840_result.json`
- **Structured JSON:** [`db2606baaeeef5896c0b.json`](../../sessions/db/db2606baaeeef5896c0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. Prolog 数据文件

- **`data/prolog/` 目录不存在** — registry 旧 note 准确
- **`data/train_500_seed42.jsonl` 存在**，500 条，484KB
- 两个 Prolog 配置文件的 `data_path` 均指向 `data/train_500_seed42.jsonl`（通用训练数据），**不依赖** prolog 专用数据目录。数据路径有效。

### 2. 配置文件

| 配置 | reward_mode | exec_weight | sta_weight | output_dir |
|------|-------------|-------------|------------|------------|
| `grpo_prolog_exec_only.yaml` | execution_only | 1.0 | 0.0 | `grpo_prolog_exec_only` |
| `grpo_prolog_exec_sta.yaml` | execution_sta | 0.5 | 0.5 | `grpo_prolog_exec_sta` |

两者均: solver=prolog, seed=42, num_steps=500, model=Qwen3-4B, no_wandb=true

### 3. plan006-prolog-exec-s42 训练进度

- **Step 323/500 (65%)**，已跑 ~1h09m
- prove_rate 持续很高 (0.875–1.0)，parse_rate=1.0
- **ISR 很低** (0.01–0.2)，大部分 step reward=1.0, loss=0.0（模型已饱和，梯度为零）
- 预计还需 ~35 分钟完成

### 4. plan006-prolog-sta-s42 状态

- **已完成** (checkpoint-500)，模型权重已保存（~16GB），eval_results.json 和 eval_analysis.txt 已生成

### 5. 后续实验就绪度

| 条件 | 状态 |
|------|------|
| 训练数据 (train_500_seed42.jsonl) | ✅ 存在，500 条 |
| exec_only 配置 | ✅ 就绪 |
| exec_sta 配置 | ✅ 就绪 |
| 多 seed 支持 | ⚠️ 配置中 seed 硬编码为 42，启动 s43/s44 需要覆盖 seed 参数 |

**结论**: 数据和配置就绪，`data/prolog/` 不存在不影响实验（配置不引用它）。后续 s43/s44 实验启动时只需在命令行覆盖 `seed` 和 `output_dir` 参数。

---
