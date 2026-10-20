# analysis c4 think validation math500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_think_validation_math500_20260516T024906_result.json`
- **Structured JSON:** [`1b1468f7f7a1e7db0bc3.json`](../../sessions/1b/1b1468f7f7a1e7db0bc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果汇总：

**DS (DeepSeek-R1-Distill-Qwen-7B) — GSM8K, n=48:**
| 指标 | 值 | 阈值 | 通过 |
|---|---|---|---|
| Cohen's κ (adaptive) | **0.880** | ≥ 0.8 | ✓ |
| thinking_in_low | **0.816** | ≥ 0.5 | ✓ |
| answer_in_high | **0.655** | ≥ 0.5 | ✓ |

补充指标：per-problem κ mean=0.847±0.091，75% problems κ≥0.8，100% κ≥0.6。

**DS MATH-500 (间接，n=50):** 100% 的问题 low-sparsity phase 在 high-sparsity phase 之前（temporal ordering=0.576），与 think→answer 结构一致。MATH-500 无法做直接 κ 验证——n500 profiling 未保存 generation text。

**QW (Qwen2.5-7B-Instruct):** 确认无 `&lt;think>` 标记，50/50 样本均为纯文本 CoT。QW MATH-500 仍有 98% 正向 temporal ordering (0.479)，说明 phase 结构不依赖 `&lt;think>` tag。

**结论:** 所有 success criteria 满足。PPL-based phase segmentation 与显式 CoT 边界高度一致 (κ=0.88)。Registry `c4_think_validation_math500` 已更新。

---
