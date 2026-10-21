# eval check acts2 eval results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-acts2-eval-results_20260522T151807_result.json`
- **Structured JSON:** [`c4e5a02a49dbcb01dd1d.json`](../../sessions/c4/c4e5a02a49dbcb01dd1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成。结果汇总：

| Checkpoint | SYCONScore | ToF | NoF |
|---|---|---|---|
| **ckpt-2000** | 0.2139 | 0.1215 | 0.8895 |
| **ckpt-3000** | 0.2543 | 0.1492 | 0.8619 |
| vanilla baseline | 0.1335 | — | — |

**两个 checkpoint 的 SYCONScore 都高于 vanilla (0.1335)**，无异常。ckpt-3000 比 ckpt-2000 高约 4 个点，训练继续有提升。

GPU 状态：GPU0/1/3 空闲（0%, 2MiB），GPU2 在使用（62%, 16458MiB）。Eval 已结束释放了 GPU0 和 GPU1。

---
