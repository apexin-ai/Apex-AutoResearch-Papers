# analysis wild6 kappa aware sc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wild6-kappa-aware-sc_20260520T072246_result.json`
- **Structured JSON:** [`e4d24151ab01d69c856b.json`](../../sessions/e4/e4d24151ab01d69c856b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总如下：

## Wild 6 结果：κ-aware Adaptive SC — Negative Result

**结论：没有任何 adaptive threshold 策略能超过 standard SC。** 在全部 11 个实验（5 模型 × 2 数据集）中，Δ = 0。

### Summary Table

| Model | Dataset | N | Standard SC | Best Adaptive | Δ |
|-------|---------|---|-------------|---------------|---|
| Mistral-7B (s42) | FOLIO-204 | 204 | 55.88% | 55.88% | 0 |
| Mistral-7B (s789) | FOLIO-204 | 204 | 54.41% | 54.41% | 0 |
| Mistral-7B (s123) | FOLIO-204 | 204 | 54.41% | 54.41% | 0 |
| Qwen2.5-7B | FOLIO-204 | 204 | 75.98% | 75.98% | 0 |
| Qwen2.5-14B (s123) | FOLIO-204 | 204 | 74.51% | 74.51% | 0 |
| Qwen2.5-14B | FOLIO-204 | 204 | 75.98% | 75.98% | 0 |
| Gemma2-27B | FOLIO-204 | 204 | 80.88% | 80.88% | 0 |
| LLaMA-3.1-8B | FOLIO-204 | 204 | 66.18% | 66.18% | 0 |
| Mistral-7B | LogiQA-200 | 200 | 48.50% | 48.50% | 0 |
| Qwen2.5-7B | LogiQA-200 | 200 | 68.50% | 68.50% | 0 |
| LLaMA-3.1-8B | LogiQA-200 | 200 | 61.00% | 61.00% | 0 |

### 核心发现：Accuracy 随 agreement 单调递增

| Agreement Regime | Acc Range (FOLIO) | Acc Range (LogiQA) |
|------------------|-------------------|---------------------|
| Unanimous (mf=1.0) | 70-93% | 82-88% |
| Strong (0.75-1.0) | 63-76% | 50-70% |
| Moderate (0.5-0.75) | 37-63% | 44-49% |
| Weak (≤0.5) | 25-60% | 32-44% |

### 为什么 adaptive SC 不 work

1. **没有 groupthink 效应**：高一致性 = 高正确率，unanimity 最强（70-93% acc），不是假共识
2. **CJT 假设成立**：agreement 是 correctness 的良好 proxy，单调递增
3. 所有"怀疑高一致性"的策略（anti-groupthink, second-answer flip）都严格更差
4. 置信阈值（confidence threshold）只在 coverage-accuracy tradeoff 上有效果，但整体 accuracy 永远不高于 standard SC

### 保存位置
- 服务器：`/root/symb_invariant_consensus/results/wild6_kappa_aware_sc/results.json`（两台服务器）
- 本地：`artifacts/wild6_kappa_aware_sc_results.json`（已注册 artifact）

---
