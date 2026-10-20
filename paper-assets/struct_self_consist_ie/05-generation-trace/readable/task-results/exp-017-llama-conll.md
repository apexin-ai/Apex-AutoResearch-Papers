# exp 017 llama conll

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_017_llama_conll_20260518T060018_result.json`
- **Structured JSON:** [`17e41a518caed88bf04a.json`](../../sessions/17/17e41a518caed88bf04a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LLaMA CoNLL Results (exp-017)

所有数据已存在，无需重新训练或推理。

### Training
- Model: Meta-Llama-3.1-8B-Instruct, LoRA, 5 epochs, final loss: 0.0392

### QE Analysis (gold-filtered, n=2756)

| Signal | ρ | AUROC | Sel F1 | Δ vs Greedy |
|--------|-------|-------|--------|-------------|
| LP     | .307  | .761  | .9244  | +0.03pp     |
| SJ     | .431  | .704  | .9237  | -0.04pp     |
| FK     | .428  | .703  | .9245  | +0.03pp     |
| EM     | .431  | .705  | .9244  | +0.02pp     |
| VC     | .426  | .709  | .9233  | -0.09pp     |
| Greedy | —     | —     | .9242  | —           |
| Oracle | —     | —     | .9426  | +1.84pp     |

Degeneracy: 89.2% | LP range median: 0.0002 | Within-instance ρ(LP,F1): median=0.512

### Cross-model Comparison

| Metric | Qwen (exp_002) | LLaMA (exp_017) |
|--------|---------------|-----------------|
| Greedy F1 | .908 | .927 |
| Oracle F1 | .947 | .944 |
| Degeneracy | 59.1% | 89.2% |
| LP ρ | .316 | .307 |
| SJ ρ | .436 | .431 |
| Best signal | EM (.451) | SJ/EM (.431) |
| LP Sel Δ | -1.05pp | +0.03pp |

### 结论
- **Signal ranking 跨模型一致**: structural > LP 在两个 backbone 上均成立，ρ 差异 <0.01
- **Degeneracy 差异巨大**: LLaMA 89.2% vs Qwen 59.1%，因 LLaMA greedy 更强，headroom 仅 1.77pp
- **Selection F1 差异由 degeneracy 驱动**: Qwen 所有 signal 低于 greedy（-0.89 to -1.53pp），LLaMA 基本持平（±0.09pp）
- **ρ-AUROC dissociation 跨模型复现**: LP AUROC > structural AUROC，但 LP ρ 最低

---
