# ssh check n500 progress loop9

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-n500-progress-loop9_20260514T222953_result.json`
- **Structured JSON:** [`253283df6680da4025da.json`](../../sessions/25/253283df6680da4025da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 n=500 实验各完成约 50%，4 GPU 满载运行，无异常。

**实验 1 — c2_n500_deepseek (GPU 0+1)**

| Condition | Done/500 | Status | ETA |
|-----------|----------|--------|-----|
| imp_s015 | 500 | ✅ | - |
| imp_s020 | 461 | 🔄 | ~06:52 |
| imp_s025 | 0 | ⏳ | ~11:17 |
| imp_s030 | 0 | ⏳ | ~15:42 |
| rand_s015 | 500 | ✅ | - |
| rand_s020 | 500 | ✅ | - |
| rand_s025 | 5 | 🔄 | ~10:55 |
| rand_s030 | 0 | ⏳ | ~15:20 |

速率 ~113 samples/hr，每 condition ~4h25m。**全部完成 ETA ~15:42**

**实验 2 — c2_qw_n500_r3 (GPU 2+3)**

| Condition | Done/500 | Status | ETA |
|-----------|----------|--------|-----|
| imp_s015 | 500 | ✅ | - |
| imp_s020 | 500 | ✅ | - |
| imp_s025 | 11 | 🔄 | ~09:52 |
| imp_s030 | 0 | ⏳ | ~13:17 |
| rand_s015 | 500 | ✅ | - |
| rand_s020 | 489 | 🔄 | ~06:37 |
| rand_s025 | 0 | ⏳ | ~10:02 |
| rand_s030 | 0 | ⏳ | ~13:27 |

速率 ~146 samples/hr，每 condition ~3h25m。**全部完成 ETA ~13:27**

**GPU 快照**: GPU0 77%, GPU1 96%, GPU2 77%, GPU3 76% — 全部正常。

报告已写入 `artifacts/n500_progress_20260515_0632.md`。

---
