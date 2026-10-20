# code exp 011 ood cross dataset

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_011_ood_cross_dataset_20260515T113645_result.json`
- **Structured JSON:** [`ab194cfd47ab1e80ca26.json`](../../sessions/ab/ab194cfd47ab1e80ca26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**实验 1 (SciERC→CoNLL, NER only)**：强结果。所有 5 个信号在 OOD 条件下均高度显著 (p<0.001)。
- VC 最强：ρ=+0.4689 (AUROC=0.7366)，比 in-domain 提升 +0.08
- SJ：ρ=+0.3777 (AUROC=0.6920)
- 所有结构信号 > LP baseline (ρ=+0.2458)
- 结论：结构一致性信号在 domain shift 下不仅保持有效，某些信号反而更强

**实验 2 (CoNLL→SciERC, joint NER+RE)**：模型几乎完全失败 (NER F1=0.009, RE F1=0.001)。NER-only 模型无法产生 SciERC entity types 和 relations，99.9% samples F1=0。所有信号 ρ 接近 0 或为负，AUROC 无法计算。这是 catastrophic OOD failure 场景——信号无法从噪声中区分质量。

**关键发现**：SCS 结构信号在模型保留合理能力的 OOD 场景 (Exp1) 下表现稳健甚至增强；在模型完全崩溃的极端 OOD 场景 (Exp2) 下，所有信号（包括 LP baseline）都失效。结构信号在两种场景下都优于或持平 LP。

---
