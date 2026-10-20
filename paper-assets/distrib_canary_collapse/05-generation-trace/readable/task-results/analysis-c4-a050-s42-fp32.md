# analysis c4 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_a050_s42_fp32_20260519T182208_result.json`
- **Structured JSON:** [`2d3a445e208a2c1cd9d4.json`](../../sessions/2d/2d3a445e208a2c1cd9d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，实验已推进到 DONE。

## 结论：bf16 precision artifact 确认

| | bf16 parent | fp32 (本实验) |
|---|---|---|
| **PermG fwd (D106)** | **0/8** | **8/8** |
| PermG rev | 0/8 | 7/8 |
| K≥4 (3σ) | 0/8 | 8/8 |
| token_entropy Δ | -38.2% | -48.0% |
| perplexity final | 122.8 | 727.95 |
| mauve final | 0.078 | 0.379 |

C4 α=0.50 **不是 blind zone**——bf16 精度完全抹杀了因果信号。fp32 下所有 8 对 canary→diversity 都呈现显著的前向因果领先（canary onset gen 1, downstream onset gen 2–3）。D079 (fp32 mandatory for ≤3B) 再次被验证。

---
