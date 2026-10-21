# analysis process kappa diagnostic

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_process-kappa-diagnostic_20260520T134125_result.json`
- **Structured JSON:** [`52aa0d464af8ab48b01f.json`](../../sessions/52/52aa0d464af8ab48b01f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 三分位表

| Tercile | n | SC Acc | SICA Acc | Mean κ |
|---------|---|--------|----------|--------|
| low     | 68 | 0.5588 | 0.5882 | 0.6483 |
| mid     | 68 | 0.5147 | 0.5882 | 0.7504 |
| high    | 68 | 0.5588 | 0.6029 | 0.8300 |

### Abstention Curve (丢弃 high-κ)

| Drop% | Coverage | n | SC Acc | SICA Acc |
|-------|----------|---|--------|----------|
| 10% | 0.90 | 184 | 0.5272 | 0.5761 |
| 20% | 0.80 | 164 | 0.5244 | 0.5732 |
| 30% | 0.70 | 143 | 0.5315 | 0.5804 |
| 40% | 0.60 | 123 | 0.5366 | 0.5935 |
| 50% | 0.50 | 102 | 0.5588 | 0.6078 |

### 统计检验

- **Fisher exact test**: odds ratio = 1.0, p = 1.0（low-κ vs high-κ SC accuracy 完全相同，38/68 vs 38/68）
- **AUROC**: 0.4930（≈ 随机，process-κ 对 SC 错误无预测力）

### Baselines

- Overall SC: 54.41% (110/204)
- Overall SICA: 59.31% (121/204)

### 结论

**负结果**：TF-IDF cosine similarity 定义的 process-κ 在此数据上对 SC 可靠性没有区分能力。三个分层 SC accuracy 几乎一样（~0.53-0.56），AUROC 0.493 低于随机。高同质化的 traces 并不比低同质化的更容易出错。

可能原因：(1) TF-IDF 在长推理文本上粒度太粗，词袋级相似度无法捕捉推理结构的同质化；(2) Mistral-7B 在 FOLIO 上整体 SC accuracy 只有 54%，本身就接近随机，信号太弱。可考虑用 sentence embedding (e.g., Sentence-BERT) 替代 TF-IDF，或在更强模型的数据上验证。

JSON 已保存至 `westd-25068:/root/symb_invariant_consensus/results/process_kappa_diagnostic/results.json`。

---
