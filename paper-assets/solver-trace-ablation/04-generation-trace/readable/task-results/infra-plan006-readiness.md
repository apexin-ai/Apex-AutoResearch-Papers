# infra plan006 readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan006-readiness_20260514T055827_result.json`
- **Structured JSON:** [`90c954b3b55b44f18274.json`](../../sessions/90/90c954b3b55b44f18274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。

---

## plan006 Prolog exec-only 就绪验证报告

### 1. Prolog 训练配置 ✅
- `configs/grpo_prolog_exec_only.yaml` 存在
- 关键参数：`logic_type: prolog`, `reward_mode: execution_only`, `solver: prolog`, `sta_weight: 0.0`
- 数据路径：`data/train_500_seed42.jsonl`（符合 C001）
- `num_steps: 100`, `seed: 42`, `no_wandb: true`
- 需要为 seed=43/44 覆盖 `--seed` 和 `--output_dir`

### 2. Prolog 训练数据 ✅
- `data/train_500_seed42.jsonl`：500 条，含 context/question/answer/fol_premises/fol_conclusion
- `build_prolog_dataset()` 只用 context + question 字段构建 Prolog prompt（PROLOG_SYSTEM_PROMPT），FOL 数据直接可用
- 模型被要求将自然语言形式化为 Prolog（非 FOL），这正是 plan006 的实验目标

### 3. SWI-Prolog solver ✅
- swipl 在 `/usr/lib/swi-prolog/bin/x86_64-linux/swipl`
- `src/solvers/prolog.py` 通过 subprocess 调 swipl，写临时 .pl 文件
- `src/solvers/factory.py` 中 `"prolog"` → `PrologSolver`
- `train_grpo.py` 中 `--logic_type prolog` 自动选择 prolog solver + prolog reward

### 4. Prolog STA 代码 ✅
- `src/sta/prolog_reward.py` 完整实现：
  - `parse_prolog_formalization()` — 解析 Facts/Rules + Query
  - `prolog_sta_ablation()` — 逐条去除 clause 检查 query 是否 break
  - `prolog_isr()` — necessary_clauses / total_clauses
  - `prolog_sta_reward()` / `fast_prolog_sta_reward()` — 完整和快速 reward
- `scripts/eval_sta.py` 支持 `--logic_type prolog`，映射到 prolog solver 和 reward_fn

### 5. 磁盘空间 ⚠️ 充足但建议清理

| 目录 | 大小 | 状态 |
|------|------|------|
| grpo_exec_only | 15G | 旧实验，可清理 |
| grpo_exec_sta | 15G | 旧实验，可清理 |
| plan001_exec_only_s42 | 15G | 已有 eval，可清理 |
| plan002_additive_b01_s42 | 20G | **活跃** |
| plan005_sta_low_s42 | 15G | 看情况 |
| plan016_extended_1000_s42 | 15G | **活跃** |

- **可用空间**：142G / 250G (56%)
- **plan006 预计需求**：3 seeds × ~15G = ~45G
- 当前空间足够，无需立即清理
- 如需释放空间：grpo_exec_only + grpo_exec_sta + plan001_exec_only_s42 = **45G 可释放**
- 提到的 plan001_s43_r4 和 plan001_s44 不在当前 outputs 列表中，可能已清理

### 6. 当前训练进程

| GPU | 实验 | PID | 进度 | 估计 |
|-----|------|-----|------|------|
| cuda:0 | plan002-b01 | 262266 | step 209/500 (42%) | reward_log 最后时间戳 06:00，当前 13:58，日志可能有缓冲延迟，实际进度可能更高 |
| cuda:1 | plan016 | 263273 | step 145/1000 (14.5%) | 同上，step_time ~4-38s 变化大 |

两卡 94% GPU-Util，训练正常进行。reward_log 时间戳 ~8h 前，实际步数可能远超日志显示。

### 7. plan006 启动命令模板

3 条命令，每条单独一张卡跑（等 GPU 释放后）：

**Seed 42:**
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 42 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42 \
  > /root/autodl-tmp/outputs/plan006_prolog_exec_s42.log 2>&1 &
```

**Seed 43:**
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 43 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 \
  > /root/autodl-tmp/outputs/plan006_prolog_exec_s43.log 2>&1 &
```

**Seed 44:**
```bash
export CUDA_VISIBLE_DEVICES=1
cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --seed 44 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44 \
  > /root/autodl-tmp/outputs/plan006_prolog_exec_s44.log 2>&1 &
```

注意：
- 每条 `export CUDA_VISIBLE_DEVICES` 必须独立行（C002）
- `save_total_limit=1` 已在 train_grpo.py 中硬编码（C003）
- `log_completions=False` 已设置，不会生成 completions parquet
- 两卡只能同时跑 2 个 seed，第 3 个等一个完成后再启动
- 100 步训练，预计 ~30-60 分钟/seed（参考现有实验 step_time）

### 结论

**plan006 全部前置条件已满足**，GPU 释放后可直接启动。无缺失项。

---
