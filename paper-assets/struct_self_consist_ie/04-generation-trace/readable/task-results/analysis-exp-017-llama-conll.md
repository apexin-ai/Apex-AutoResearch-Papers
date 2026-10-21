# analysis exp 017 llama conll

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_017_llama_conll_20260517T113825_result.json`
- **Structured JSON:** [`1a1b94db0ac49df24732.json`](../../sessions/1a/1a1b94db0ac49df24732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

## exp_017 LLaMA CoNLL N=8 完整信号分析

| 指标 | LLaMA | Qwen3 |
|------|------:|------:|
| Greedy F1 | 0.9242 | 0.7250 |
| Oracle F1 | 0.9426 | 0.7570 |
| Headroom | 1.84pp | 3.20pp |
| **Degeneracy (CF1 gold-filtered)** | **89.2%** | **47.4%** |

### Selection F1 (全部在 greedy 附近，headroom 太窄无法区分)
| Signal | F1 | Δ vs Greedy |
|--------|---:|------------:|
| SJ | 0.9237 | -0.04pp |
| FK | 0.9240 | -0.02pp |
| VC | 0.9250 | +0.08pp |
| EM | 0.9244 | +0.02pp |
| LP | 0.9244 | +0.02pp |
| Random | 0.9207 | — |

### QE Diagnostic (ρ / AUROC)
| Signal | Spearman ρ | AUROC |
|--------|----------:|------:|
| SJ | 0.431 | 0.704 |
| FK | 0.428 | 0.703 |
| EM | 0.431 | 0.705 |
| VC | 0.426 | 0.709 |
| LP | 0.307 | 0.761 |

### LP Range
mean=0.0198, std=0.0315, median=0.0002 (极度压缩)

### Conclusion: **success** (cross-model validation 通过)

LLaMA on CoNLL 显示与 Qwen3 **一致且更极端**的模式：
1. 极高 degeneracy (89.2% vs 47.4%) → selection 对所有信号均无效
2. 结构信号仍保持 ρ≈0.43 的诊断能力，显著优于 LP (ρ=0.31)
3. ρ-AUROC 分离现象存在（LP AUROC 0.761 > structural ~0.704，但 ρ 最低）
4. LP range 极窄（median=0.0002），与 high degeneracy 一致

---
