# analysis 72b zeroshot partial results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_72b_zeroshot_partial_results_20260519T113709_result.json`
- **Structured JSON:** [`93007d8eecce45a240c2.json`](../../sessions/93/93007d8eecce45a240c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。核心结果：

## 72B Zero-Shot 信号报告摘要

### Greedy F1 & Oracle Headroom

| Dataset | Greedy F1 | Oracle F1 | Headroom |
|---------|-----------|-----------|----------|
| SciERC | 0.399 | 0.549 | **+15.0pp** |
| CoNLL | 0.712 | 0.765 | **+5.3pp** |

### Signal ρ（与 instance-level F1 的 Spearman 相关）

| Signal | SciERC | CoNLL |
|--------|--------|-------|
| LP | 0.081 | **-0.002** |
| SJ | 0.217 | 0.304 |
| FK | 0.227 | 0.302 |
| VC | **0.277** | 0.297 |
| EM | 0.181 | 0.281 |

### LP Selection Δ

| Dataset | Δ vs Greedy |
|---------|-------------|
| SciERC | **-0.10pp** (hurt) |
| CoNLL | **-0.39pp** (hurt) |

### 关键发现

1. **LP 信号在零样本下彻底失效**：ρ 接近零（SciERC 0.081, CoNLL -0.002），LP selection 反而损害性能。这是与 fine-tuned 模型最大的差异。
2. **非 LP 信号仍有效**：VC/SJ/FK 的 ρ 在 0.22-0.30 之间，说明结构一致性信号不依赖 fine-tuning。
3. **Greedy F1 在 SciERC 上远低于 fine-tuned 7B**（0.40 vs ~0.55+），但 CoNLL 表现尚可（0.71）。
4. **Oracle headroom 大**（SciERC 15pp），但没有现有方法能有效利用——所有聚合方法均无法稳定超越 greedy。
5. **Degeneracy 数据不在信号报告中**，需要从 samples.jsonl 单独计算。

### FewNERD 状态

72b_zeroshot/ 下没有 fewnerd 目录或输出文件，推理可能尚未启动。

产出已写入 `artifacts/72b_zeroshot_signal_summary.json`。

---
