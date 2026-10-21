# diag arc s123 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_arc-s123-results_20260520T164525_result.json`
- **Structured JSON:** [`f241a496b600bda28dfc.json`](../../sessions/f2/f241a496b600bda28dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部分结果（10/20 完成）

Batch 仍在运行：qwen14b 和 phi4 全部完成，qwen7b 正在运行（~8%），olmo2 尚未开始。预计还需 ~35 分钟。

### ARC Challenge 25-shot Accuracy (s123)

| Family | d000 | d005 | d025 | d050 | d100 | Δ(d100-d000) |
|--------|------|------|------|------|------|-------------|
| **Qwen-14B** | 90.44% | 91.47% | 89.76% | 88.74% | 87.29% | **-3.15pp** |
| **Phi-4** | 91.89% | 91.89% | 92.24% | 92.58% | 92.75% | **+0.86pp** |
| Qwen-7B | — | — | — | — | — | 运行中 |
| OLMo-2 | — | — | — | — | — | 待运行 |

### 与 MMLU s123 对比

| Family | MMLU Δ(d100) | ARC Δ(d100) | 模式 |
|--------|-------------|-------------|------|
| **Qwen-14B** | -12.74pp | -3.15pp | 双降，ARC 附带损伤较轻 |
| **Phi-4** | +1.83pp | +0.86pp | 双升，contamination 训练无负面影响 |
| Qwen-7B | ~0pp V-recovery | ? | 待完成 |
| OLMo-2 | -0.55pp | ? | 待完成 |

Qwen-14B 的 ARC 下降趋势是单调的（90.44→91.47→89.76→88.74→87.29），d005 有小幅反弹后持续下降，与 MMLU 崩溃模式一致但程度弱得多。Phi-4 在 ARC 上也呈现单调上升，与 MMLU 表现一致——contamination SFT 对该模型有正向迁移效应。

qwen7b 和 olmo2 结果需等 batch 完成后再收集。

---
