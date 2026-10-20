# analysis exp e2 pretrained fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620_result.json`
- **Structured JSON:** [`42bd56622946625ef8af.json`](../../sessions/42/42bd56622946625ef8af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是结果汇总：

## exp_e2_pretrained_fewnerd — 结果分析

### 核心 Metrics

| Metric | FewNERD (本实验) | CoNLL (对照) |
|--------|:---:|:---:|
| Greedy F1 | 0.512 | 0.539 |
| Oracle F1 | 0.618 | 0.628 |
| **Oracle headroom** | **+0.105** | +0.089 |
| Fleiss κ | 0.450 | 0.547 |
| Soft Jaccard | 0.688 | 0.776 |
| ρ(SJ, F1) full | +0.433 | +0.392 |
| ρ(SJ, F1) cond | +0.440 | +0.467 |
| Structural > Surface | YES (+0.050) | YES (+0.015) |
| LP full ρ | +0.189 | -0.020 (ns) |
| LP full AUROC | 0.596 | 0.538 |
| Verdict | **PASS** | MARGINAL |

### Conclusion: **SUCCESS**

Correlation-selection gap 在未微调的 Qwen2.5-7B-Instruct 上明确存在：
1. **Gap 大**: Oracle F1 超 Greedy F1 达 10.5pp — 8 个样本中蕴含大量未被利用的选择潜力
2. **Agreement 正相关但不够用**: ρ(SJ,F1)=+0.43，agreement 确实预测 correctness，但 naive aggregation 仍无法逼近 oracle — 典型 correlation-selection gap
3. **Structural > Surface**: Soft Jaccard 比 Fleiss κ 多 +0.05 的相关性优势，跨数据集一致
4. **Logprob 弱**: FewNERD LP ρ=0.19（显著但弱），CoNLL full LP 甚至不显著 — 单靠 log-probability 不足以做 selection
5. **跨数据集复现**: FewNERD (37.6K) 比 CoNLL (3.5K) headroom 更大、structural advantage 更强

**核心含义**: Gap 是 model-intrinsic 而非 fine-tuning artifact，motivates learned selection/weighting approaches。

---
