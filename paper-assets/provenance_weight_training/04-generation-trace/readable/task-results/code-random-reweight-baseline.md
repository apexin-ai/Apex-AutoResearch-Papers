# code random reweight baseline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random_reweight_baseline_20260516T054943_result.json`
- **Structured JSON:** [`9569db7bd07ff80580e6.json`](../../sessions/95/9569db7bd07ff80580e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 修改内容

**`training/pretrain_weighted.py`** — 新增 `random` weighting method (line 174-179):
- 每个 batch 从 U(0, 2) 采样随机权重
- 归一化使 batch 内 mean = 1.0：`weights = weights * N / weights.sum()`
- 不使用 q_score，完全与 provenance signal 无关
- 记录 ESS 供 wandb 对比

**`scripts/run_random_reweight_seed42.sh`** — 训练脚本，参数对齐其他实验（`--weighting_method random`, `--tau 0.8`, `--n_min 2`, 200M tokens, seed=42）。

### 与现有 `run_random_reweight.sh` 的区别

| | 旧 `run_random_reweight.sh` | 新 `run_random_reweight_seed42.sh` |
|---|---|---|
| 方法 | `adaptive` + `--shuffle_scores` | `random` |
| 权重来源 | 真实 q_score 打乱分配 | U(0,2) 独立采样，与 q_score 无关 |
| 控制变量 | 保留权重分布，破坏 sample-score 关联 | 完全随机权重，仅保留 mean=1 |

两个 baseline 互补——shuffle 控制了权重分布形状，random 控制了非均匀加权本身。

---
