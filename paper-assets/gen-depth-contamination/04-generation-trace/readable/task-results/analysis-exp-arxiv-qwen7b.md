# analysis exp arXiv qwen7b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_qwen7b_20260517T163548_result.json`
- **Structured JSON:** [`cde0d1dba8d0cfe633f1.json`](../../sessions/cd/cde0d1dba8d0cfe633f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_arXiv_qwen7b 分析完成。结论：SUCCESS，K\*=3。**

核心结果：

| Depth Pair | AUC | JSD |
|---|---|---|
| 0 vs 1 | 0.983 | 0.166 |
| 1 vs 2 | 0.835 | 0.067 |
| 2 vs 3 | 0.626 | 0.016 |
| **3 vs 4** | **0.544** (< 0.60) | **0.009** |
| 4 vs 5 | 0.513 | 0.006 |

K\*=3：depth 2v3 仍可区分（AUC=0.626），depth 3v4 不可区分（AUC=0.544）。

arXiv domain K\*=3 现已在 5 个模型、4 种架构（Pythia/LLaMA/Mistral/Qwen）、4 个规模（1.4B/1.5B/7B/8B）上全部验证通过。域属性（structured academic text）主导 K\* 值，模型架构和规模不影响。

产出已注册，registry 已更新为 DONE/success。

---
