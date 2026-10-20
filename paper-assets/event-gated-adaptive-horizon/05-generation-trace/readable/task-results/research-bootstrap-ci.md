# research bootstrap ci

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bootstrap-ci_20260516T154234_result.json`
- **Structured JSON:** [`5a27691be410c9706ae0.json`](../../sessions/5a/5a27691be410c9706ae0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。关键结果：

**可用的 CI（n≥3）：**
- **trained_dt_emb** NVE peak: 3.43 [2.05, 4.12]，collapse rate: 0.667 [0.0, 1.0]
- **baseline_walker** eval_return_peak: 962.77 [950.96, 970.41]

**Effect size (trained − no_dt_emb)：**
- Δ NVE peak: +2.29 [+0.91, +3.10] — CI 不跨零，效应显著
- Δ eval_return_peak: −199.15 [−308.19, −90.11] — trained dt_emb 显著更差
- NVE > 1.5× exceedance: trained=100% vs no_dt_emb=0%，完美分离

**样本量不足需追加 seeds：**
| Condition | 现有 | 需要 |
|-----------|------|------|
| no_dt_emb | 2 | ≥3 |
| SGS_partial | 1 | ≥3 |
| SGS_full | 1 | ≥3 |
| frozen_dt_emb | 1 | ≥3 |

**Cross-env classification CI 无法计算** — 只有 1 个 Cheetah baseline，无 treatment condition 在 Cheetah 上运行过。

产出文件：
- 脚本：`artifacts/bootstrap_cis/compute_bootstrap_cis.py`
- 汇总表：`artifacts/bootstrap_cis/bootstrap_ci_summary.md`
- 已注册：`art_20260516_2b21be`

---
