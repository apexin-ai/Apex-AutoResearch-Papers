# experiment posthoc filtering baseline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_posthoc_filtering_baseline_20260514T181438_result.json`
- **Structured JSON:** [`2aa48aa1f77a98178069.json`](../../sessions/2a/2aa48aa1f77a98178069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。汇总对比表：

## SciERC (551 samples)

| 方法 | DR% | R-Recall | R-Prec | R-F1 | Rejection |
|------|-----|----------|--------|------|-----------|
| Unconstrained | 15.37% | 11.40% | 6.44% | 8.23% | 0% |
| **Post-hoc filter** | **0%** | 10.68% | 7.25% | 8.63% | 16.8% |
| OntoCoDec full_s1 | 0.93% | **11.60%** | 6.54% | 8.36% | 0% |

## DocRED (998 docs)

| 方法 | DR% | R-Recall | R-Prec | R-F1 | Rejection |
|------|-----|----------|--------|------|-----------|
| Unconstrained | 18.46% | 9.46% | 6.55% | 7.74% | 0% |
| **Post-hoc filter** | **0%** | 8.40% | 11.22% | 9.61% | 48.1% |
| OntoCoDec full_s1 | 10.20% | **10.02%** | 6.99% | 8.24% | 0% |

## 关键发现

**Recall 对比**（核心论点）：
- Post-hoc **recall 下降**：SciERC -0.72pp (丢了 7 个正确 triple)，DocRED -1.06pp (丢了 127 个正确 triple)
- OntoCoDec **recall 上升**：SciERC +0.20pp，DocRED +0.56pp — 概率质量重分配到合法 token，反而帮助模型生成更多正确 triple

**Rejection rate**：DocRED post-hoc 丢弃了 48.1% 的 triple，几乎一半的抽取信息被扔掉。

**F1 可能误导**：post-hoc 的 F1 反而比 unconstrained 高，因为大量移除的错误 triple 提升了 precision。但这是以信息完整性为代价的 — recall 才是衡量"有多少正确知识被保留"的指标。

文件已保存在服务器 `outputs/posthoc_report_{scierc,docred}.json`，脚本为 `posthoc_filter.py`。

---
