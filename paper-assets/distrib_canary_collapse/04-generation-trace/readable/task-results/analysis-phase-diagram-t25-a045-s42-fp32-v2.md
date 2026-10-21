# analysis phase diagram t25 a045 s42 fp32 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t25_a045_s42_fp32_v2_20260521T235931_result.json`
- **Structured JSON:** [`4b35e31332e9589f5cb7.json`](../../sessions/4b/4b35e31332e9589f5cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

```
PermG:           6/8
Diff XCorr:      6/8
Threshold Onset: 6/8
TY Granger:      1/8
K≥3 (robust):   6/8

结论: success
```

PermG reverse = 0/8，forward = 6/8，方向性清晰。6 个 pair 中除 mauve 相关的 2 对外全部检出。

与假设对比：
| T | α=0.45 PermG |
|---|-------------|
| 10 | 0/8 |
| 15 | 6/8 |
| 20 | 5/8 |
| **25** | **6/8** |

T=25 α=0.45 ≥6/8，确认 detection scaling — 随 T 增大（超过 α_c(T) 阈值后），检测率稳定在 5-6/8。

---
