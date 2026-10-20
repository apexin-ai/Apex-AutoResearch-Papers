# diagnose mvp collapse decoupling

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_collapse_decoupling_20260515T203535_result.json`
- **Structured JSON:** [`b35925d22d819db9835f.json`](../../sessions/b3/b35925d22d819db9835f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diagnose_mvp_collapse_decoupling.md`。

**摘要**：`train.py:79` 的 `wandb.init()` 因服务器未配置 wandb API key 而抛出 `UsageError`，导致 Gen1 Step 3 (Training) 启动即崩溃。前面的合成数据生成和混合数据准备均已完成（耗时约 2.25 小时），`checkpoints/` 为空。最简修复：重跑前加 `export WANDB_MODE=offline`。

---
