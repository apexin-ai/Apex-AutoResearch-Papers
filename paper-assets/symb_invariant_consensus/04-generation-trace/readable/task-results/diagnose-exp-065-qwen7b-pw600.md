# diagnose exp 065 qwen7b pw600

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-065-qwen7b-pw600_20260519T144555_result.json`
- **Structured JSON:** [`e322b4b7a3c1a25ce47b.json`](../../sessions/e3/e322b4b7a3c1a25ce47b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已经从日志 tail 获取了所有需要的信息。

## 诊断结论

**实验 exp-065-qwen7b-pw600 已成功完成。Cron 是误报。**

### 关键数据

| 指标 | 值 |
|------|-----|
| **总题数** | 600/600 (ProofWriter OWA-D5) |
| **SICA accuracy** | **68.0%** (408/600) |
| **SC accuracy** | **72.0%** (432/600) |
| **SC - SICA delta** | **+4.0%** (SC 优于 SICA) |
| Extraction rate | 99.7% |
| Contradiction rate | 2.3% (288/600 problems) |
| Wall time | 340.4 min |
| 完成时间 | 2026-05-19 22:33 |

### 文件路径
- 结果: `/root/symb_invariant_consensus/results/exp065_qwen7b_pw600/exp065_results.json` (1MB)
- 日志: `/root/symb_invariant_consensus/results/exp065_qwen7b_pw600/exp065_run.log` (1.9MB)

### 误报原因
与 exp-070 完全相同的模式：`run_full_mvp.py` 输出 JSON 而非 W&B，cron 找不到 metrics 就判定失败。日志最后一行是 `FULL_MVP_DONE`，无任何 Traceback/Error。

---
