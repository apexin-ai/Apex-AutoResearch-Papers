# analysis w5 llama docred lora constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_llama_docred_lora_constrained_eval_20260516T045250_result.json`
- **Structured JSON:** [`452bfd5cd0baf613a44f.json`](../../sessions/45/452bfd5cd0baf613a44f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Llama DocRED 2x2 composability matrix 最后一格完成。结果：

**Violation reduction:**
- DR: 0.49% → 0.21% (**-57.1%** relative, 33 residual violations / 16,074 triples)
- RV: 0.15% → 0.00% (完全消除)
- ET: 保持 0%

**F1 preservation:**
- R-F1: 43.72% → 43.83% (**+0.11pp**, 略有提升)
- E-F1: 83.93% → 84.01% (+0.08pp)

**Cross-dataset pattern 一致:**
| Dataset | ΔDR (rel.) | ΔR-F1 |
|---------|-----------|-------|
| SciERC | -91.9% | +0.02pp |
| DocRED | -57.1% | +0.11pp |

DocRED 的相对降幅较小是因为 fine-tuned baseline 已经很低（0.49% vs SciERC 1.11%），改善空间有限。

**Conclusion: SUCCESS.** Composability claim 成立 — Fine-tuning + OntoCoDec 无干扰叠加，violations 进一步减半，F1 零损失。

---
