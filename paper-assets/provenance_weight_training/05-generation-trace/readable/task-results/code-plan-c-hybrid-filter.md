# code plan c hybrid filter

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_c_hybrid_filter_20260516T101107_result.json`
- **Structured JSON:** [`b6f2d94db243af983074.json`](../../sessions/b6/b6f2d94db243af983074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 结果

### 过滤前后数据量

| 数据集 | 过滤前 | 过滤后 (q≤0.95) | 移除 |
|--------|--------|-----------------|------|
| ρ=0.4 (`scored_data.jsonl`) | 371,499 | 253,584 | 117,915 (31.7%) |
| ρ=0.6 (`scored_data_rho06.jsonl`) | 371,499 | 244,502 | 126,997 (34.2%) |

过滤后 max_q=0.950，mean_q 从 0.599→0.418 (ρ=0.4)，0.624→0.436 (ρ=0.6)。

### 训练脚本

| 脚本 | 参数 |
|------|------|
| `scripts/run_hybrid_rho04_seed42.sh` | data=`scored_data_hybrid.jsonl`, tau=0.8, n_min=2, contamination_ratio=0.4 |
| `scripts/run_hybrid_rho06_seed42.sh` | data=`scored_data_hybrid_rho06.jsonl`, tau=0.7, n_min=2, contamination_ratio=0.6 |

### 实际 contamination ratio 变化

过滤移除的主要是高 q-score 样本（大概率是 synthetic），实际剩余数据中 contamination 比例会低于标称值：
- ρ=0.4 标称 → 过滤后实际约 0.28（假设移除的全是 synthetic）
- ρ=0.6 标称 → 过滤后实际约 0.47

两个脚本中 `--contamination_ratio` 仍传原始值，adaptive reweight 会据此计算权重——如需传入过滤后的实际比例请告知调整。WANDB_MODE 已设为 offline。

---
