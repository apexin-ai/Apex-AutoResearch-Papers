# diag exp 062 failure

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-062-failure_20260519T151122_result.json`
- **Structured JSON:** [`171b9f5b2da3f559a304.json`](../../sessions/17/171b9f5b2da3f559a304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnose_exp062_exp065.md`。

**结论：两个实验均已正常完成，cron 误报为 failed。**

| 实验 | 模型 | 数据集 | SICA | SC | 耗时 |
|------|------|--------|------|----|------|
| exp-062 | Gemma-3-27B-IT | FOLIO 204 | **80.4%** | 80.9% | 357 min |
| exp-065 | Qwen2.5-7B | ProofWriter 600 | **68.0%** | 72.0% | 340 min |

**误报原因**：实验完成后 run session 正常退出，但未写 sentinel 文件且无 W&B，cron 将 session 消失误判为进程崩溃。

**待处理**：GPU 3 上 exp062_vllm 残留进程占 88GB 显存，需要清理。

---
