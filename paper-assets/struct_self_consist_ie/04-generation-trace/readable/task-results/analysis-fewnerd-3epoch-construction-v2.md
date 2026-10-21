# analysis fewnerd 3epoch construction v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd-3epoch-construction-v2_20260524T073554_result.json`
- **Structured JSON:** [`aaf93233e00517bdad4c.json`](../../sessions/aa/aaf93233e00517bdad4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

- **LP construction**: pooled **+0.75pp**，p<0.0001，显著。但 seed 间差异大（seed42 -0.02pp 不显著，seed456 +1.52pp 强显著）
- **MV construction**: pooled -0.02pp，p=0.62，不显著
- **Degeneracy rate**: 8.6%
- 与论文对比：SciERC 4-seed LP +1.40pp → FewNERD 2-seed LP +0.75pp，幅度约一半但 pooled 仍然显著，支持跨数据集泛化

结果已保存至：
- 服务器：`/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_3epoch_construction_results.txt`
- 本地：`artifacts/rebuttal_fewnerd_3epoch_construction.md`

---
