# infra qwen25 folio cron cleanup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_qwen25-folio-cron-cleanup_20260522T110329_result.json`
- **Structured JSON:** [`567af0974145ec03ba3d.json`](../../sessions/56/567af0974145ec03ba3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

### 结果

**退出原因**：Guard script (PID 555317) 在 18:57:21 CST 检测到 204/204 文件完成，执行 `kill 510872`，随后自身退出。**预期行为，确认是 guard kill。**

**seed=789 FOLIO 最终结果**（来自 results.json）：

| 指标 | 值 |
|------|-----|
| SC accuracy | **74.02%** (151/204) |
| SICA accuracy | **72.55%** (148/204) |
| Delta (SICA - SC) | **-1.47pp** |
| Extraction rate | 98.0% |
| Contradiction rate | 0.91% (37/204 problems) |
| Wall time | 8750s (~2.4h) |

**进程状态**：PID 510872 (master) 和 PID 555317 (guard) 均已 DEAD。

**cuda:1 状态**：GPU utilization 0%，但内存占用 88259 MiB — 可能有残留的 vLLM 进程未释放显存。

**Master 日志注意**：master 被 kill 后，日志末尾还记录了 PW seed=789 完成（0% accuracy, "All 6 experiments completed"）。这应该是 cuda:0 侧 master 的日志写入同一文件，不影响 cuda:1 的诊断结论。

---
