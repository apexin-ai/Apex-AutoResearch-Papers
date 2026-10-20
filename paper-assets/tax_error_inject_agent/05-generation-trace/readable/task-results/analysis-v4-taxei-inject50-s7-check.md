# analysis v4 taxei inject50 s7 check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-inject50-s7-check_20260516T010449_result.json`
- **Structured JSON:** [`31a4bd8608020b1d8375.json`](../../sessions/31/31a4bd8608020b1d8375.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验 registry 已更新完毕。汇总：

| exp_id | GPU | train_loss | token_acc | runtime | memory | status |
|--------|-----|-----------|-----------|---------|--------|--------|
| v4-taxei-fixed-inject50-s1-r2 | cuda:0 | 0.4667 | 0.9072 | 3858s (64m) | 30.37 GiB | DONE ✓ |
| v4-random-fixed-inject50-s1-r2 | cuda:1 | 0.4664 | 0.9012 | 3928s (65m) | 30.37 GiB | DONE ✓ |
| v4-taxei-fixed-inject50-s7 | cuda:2 | 0.4674 | 0.9189 | 3834s (64m) | 29.94 GiB | DONE ✓ |
| v4-random-fixed-inject50-s7 | cuda:3 | 0.4672 | 0.9156 | 3832s (64m) | 29.94 GiB | DONE ✓ |

GPU 全部释放（0 MiB / 0%），4 张卡空闲可用。无 session 内 cron 需要清理。

---
