# analyze codellama13b vota seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_codellama13b_vota_seed123_20260520T113459_result.json`
- **Structured JSON:** [`10609618a25fe920c33a.json`](../../sessions/10/10609618a25fe920c33a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（status=DONE, conclusion=success）。

## 结果汇总

**codellama13b_vota_seed123: 98.91% accuracy** (95% CI: [98.3%, 99.4%])

### 跨 seed 对比

| Seed | Accuracy | Pass F1 | Fail F1 |
|------|----------|---------|---------|
| seed42 | 98.57% | — | — |
| seed123 | 98.91% | 0.992 | 0.981 |
| **Δ** | **+0.34pp** | — | — |

### Conclusion

**Success.** seed123 (98.91%) 落在预期区间 97-100% 内，与 seed42 (98.57%) 仅差 0.34pp，两者 CI 重叠。CodeLlama-13B VOTA 跨 seed 稳定性确认。cuda:1 无残留进程，无需清理。

---
