# ops plan007 completion check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan007-completion-check_20260515T220649_result.json`
- **Structured JSON:** [`03b66b965b3fa4ec2338.json`](../../sessions/03/03b66b965b3fa4ec2338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron 任务，无需删除。

---

**plan-007 cross-model chains 实验：成功完成。**

三阶段（generate → extract → evaluate）全部正常退出。关键结果：

| 指标 | 值 |
|------|-----|
| **3-class macro-F1** | **0.8089 ± 0.0166** |
| binary F1 (gen-1 vs gen-2+) | 0.7635 |
| binary F1 (gen-0 vs gen-2+) | 0.8372 |
| gen-0 F1 | 0.9285 |
| gen-1 F1 | 0.7367 |
| gen-2+ F1 | 0.7614 |
| 样本数 | 4773 (995 seeds × 5 depths, 自然衰减) |
| 平均每链使用生成器数 | 3.0 ± 0.67 |

**对比 single-model baselines：**

| Generator | macro-F1 |
|-----------|----------|
| pythia-1b | 0.8622 |
| qwen3-0.6b | 0.8354 |
| pythia-2.8b | 0.8156 |
| qwen3-1.7b | 0.8106 |
| olmo-2-1b | 0.7801 |
| **cross-model** | **0.8089** |

Cross-model F1 (0.809) 略低于多数 single-model baselines，但仍处于可分类水平——depth fingerprint 在跨模型链场景下保持有效，只是信号略弱。Feature importance 排序：hapax_ratio (0.357) > entropy_mean (0.204) > ttr (0.202)。

结果已保存至 `results/cross_model_chains_results.json`，registry 已更新为 success。

---
