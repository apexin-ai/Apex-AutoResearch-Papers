# diagnose a3 scierc re done

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a3_scierc_re_done_20260520T210241_result.json`
- **Structured JSON:** [`f3d9c2f463ba7680ba42.json`](../../sessions/f3/f3d9c2f463ba7680ba42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_a3_ace05_re — RE SC 诊断结果（SciERC RE, Qwen2.5-7B, N=8, T=1.0）

| 指标 | 值 |
|------|-----|
| **Greedy F1 (mean)** | 0.0777 |
| **Construction F1 (mean)** | 0.0599 |
| **Majority Vote F1 (mean)** | 0.0491 |
| **Oracle F1 (mean)** | 0.1567 |
| **Greedy Micro F1** | 0.0688 |
| **Construction Micro F1** | 0.0602 |
| **Fleiss' κ** | -0.0021 |
| **Soft Jaccard** | 0.2425 |
| **Degeneracy rate** | 0.76% (3/397) |

### Failure Mode 分布

| Mode | 占比 |
|------|------|
| F1 (degeneracy) | 0.8% |
| **F2 (low agreement)** | **93.5%** |
| F3 (high agreement, low quality) | 4.5% |
| None (SC works) | 1.3% |

### Bootstrap

- Diff (construction - greedy): **-0.0178**
- 95% CI: [-0.0334, -0.0024] — 不过零，显著为负
- p-value: 0.989

### 结论：**success**

SC 诊断 cascade 从 NER 成功推广到 RE，且表现更极端：

1. **Correlation-selection gap 确认**：agreement 与 correctness 弱正相关（soft Jaccard=0.24），但 MV (0.049) 显著劣于 greedy (0.078)，construction 也劣于 greedy。Voting 不仅没帮上忙，反而伤害了性能。
2. **F2 压倒性主导**（93.5%）：比 NER 还极端。模型在 RE 上的 8 次采样之间几乎没有一致性（κ ≈ 0），导致投票无法汇聚。
3. **Oracle gap 巨大**：Oracle F1 (0.157) 是 greedy 的 2 倍，说明正确答案存在于样本中，但 MV 无法选出。
4. 低绝对 F1 反映 Qwen2.5-7B 在 few-shot RE 上的基础能力较弱，但诊断 pattern 与 NER 一致——这正是 cross-task universality 的证据。

Registry 已更新为 DONE/success，cron 已删除。

---
