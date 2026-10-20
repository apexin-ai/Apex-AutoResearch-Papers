# analysis rho03 uniform seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho03_uniform_seed456_20260523T064947_result.json`
- **Structured JSON:** [`d8e9cc26330e93d273ae.json`](../../sessions/d8/d8e9cc26330e93d273ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success。

**rho03_uniform_seed456 结果汇总：**

| 指标 | seed42 | seed123 | seed456 |
|------|--------|---------|---------|
| holdout PPL | 17.422 | 17.433 | **17.419** |
| owt PPL | 18.113 | 18.126 | **18.109** |
| wiki PPL | 15.204 | 15.204 | **15.168** |

- 训练 6103/6103 steps，EXIT_CODE=0，无 WARNING/ERROR
- 三个 seed 的 holdout PPL 极其一致（17.419–17.433），方差极小，适合 t-test 配对比较
- checkpoint: `/root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed456/final`

---
