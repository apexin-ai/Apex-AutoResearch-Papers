# analysis bf16 ds rand batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_ds_rand_batch_20260514T070206_result.json`
- **Structured JSON:** [`40349e7b79a6c2c7aea8.json`](../../sessions/40/40349e7b79a6c2c7aea8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四个实验全部 DONE。汇总：

| 实验 | II high (mean/median) | II mid (mean/median) | II low (mean/median) | PPL both (H/M/L) | n_problems | Verdict |
|---|---|---|---|---|---|---|
| **rand_s015** | +0.38 / 0.11 | -172.66 / 0.10 | -5.73 / 0.11 | 5.76 / 11.32 / 6.29 | 50 | PASS |
| **rand_s020** | +2.53 / 0.33 | -36.05 / 0.30 | -2.48 / 0.39 | 8.81 / 11.50 / 9.20 | PASS |
| **rand_s025** | +5.59 / 1.55 | -514.24 / 1.02 | -9.11 / 1.89 | 17.74 / 29.47 / 17.97 | 50 | PASS |
| **importance_s020** | +0.13 / 0.01 | +1.26 / 0.20 | +6.03 / 1.50 | 2.10 / 5.42 / 23.74 | 50 | PASS |

关键对比（random vs importance at s=0.20）：
- **Random**: mean 受极端 outlier 主导（skewness -10~-12），median 三相几乎持平（~0.3），无 phase 区分效应
- **Importance**: II 单调递增 high→low（median 0.01→0.20→1.50），gradient_paired_aggregate=5.9x，PPL 梯度 2.1→23.7

Random masking 的 mean 值被少数灾难性 outlier 拉至大幅负值（尤其 mid_sparsity 的 attn PPL 爆炸：s015=298, s020=68, s025=868），但 median 层面三相无分化——符合预期：随机 masking 不具备 phase-aware 区分能力。

---
