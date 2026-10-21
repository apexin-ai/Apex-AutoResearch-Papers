# diagnose docred re done

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_docred_re_done_20260520T210316_result.json`
- **Structured JSON:** [`615429e786e36abb0aaa.json`](../../sessions/61/615429e786e36abb0aaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已删除，registry 已更新为 DONE/success。

## DocRED RE SC 诊断结果

实验在 `autodl-5090-c:cuda:3` 正常完成（200 instances × 8 samples，~38s 推理）。

### 核心指标

| 指标 | 值 |
|------|-----|
| Greedy F1 (mean) | 0.0284 |
| Construction F1 (mean) | 0.0338 |
| Majority Vote F1 (mean) | 0.0263 |
| Oracle F1 (mean) | 0.0999 |
| Fleiss' κ | -0.0253 |
| Soft Jaccard | 0.2907 |
| Degeneracy rate | 3.5% |

### Failure Mode 分布

| Mode | % |
|------|---|
| F1 (degeneracy) | 3.5% |
| **F2 (low agreement)** | **94.5%** |
| F3 (high agreement, low quality) | 2.0% |

### Bootstrap (Construction - Greedy)
- Diff: +0.0053, 95% CI: [-0.004, +0.015], p=0.1276 (不显著)

### 与 SciERC RE (exp_a3_ace05_re) 对比

| | SciERC RE | DocRED RE |
|--|-----------|-----------|
| Greedy F1 | 0.078 | 0.028 |
| Oracle F1 | 0.157 | 0.100 |
| Degen rate | 0.8% | 3.5% |
| **F2 占比** | **93.5%** | **94.5%** |
| Construction-Greedy gap | -0.018 (显著) | +0.005 (不显著) |

### 结论

**Hypothesis confirmed (success)**：SC diagnostic cascade 成功推广到 document-level RE。F2 (low agreement) 压倒性主导（94.5%），与 sentence-level RE（93.5%）高度一致——failure mode structure 在 RE 任务上具有跨粒度稳定性。

绝对性能极低（F1 ~3%），说明 7B 模型 few-shot 做 DocRED 级别的 document-level RE 本身不可行，但 SC 诊断框架正确地诊断出了原因：模型在 sample 间几乎无一致性（κ 为负），绝大多数 instance 落入 F2 failure mode。

---
