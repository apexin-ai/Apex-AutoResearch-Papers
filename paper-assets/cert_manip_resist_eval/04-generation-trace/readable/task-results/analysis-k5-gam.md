# analysis k5 gam

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-gam_20260523T012252_result.json`
- **Structured JSON:** [`1ad4319bc2aa9ad302c4.json`](../../sessions/1a/1ad4319bc2aa9ad302c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=5 GAM 分析结果

**K=5 的 6:6 split 不成立。实际 split 是 7+/5-。**

唯一变化的条件：**`mmlu×sycophancy`** 从 K=3 的 K_eff 负方向翻转为 K=5 的正方向。

### K=3 vs K=5 对比表

| Condition | K=3 | K=5 | Changed |
|-----------|-----|-----|---------|
| arc_challenge × authority_bias | − | − | |
| arc_challenge × position_bias | + | + | |
| arc_challenge × prompt_injection | + | + | |
| arc_challenge × score_manipulation | + | + | |
| arc_challenge × sycophancy | − | − | |
| arc_challenge × verbosity_bias | − | − | |
| mmlu × authority_bias | − | − | |
| mmlu × position_bias | + | + | |
| mmlu × prompt_injection | + | + | |
| mmlu × score_manipulation | + | + | |
| **mmlu × sycophancy** | **−** | **+** | **YES** |
| mmlu × verbosity_bias | − | − | |

### 关键发现

1. **基础 GAM**: 12/12 FDR 显著，split **7+/5-**（`mmlu×sycophancy` 翻转）
2. **GAM+tier**: 12/12 FDR 显著，split **4+/8-**（tier 控制后方向变化更大，3 个额外条件翻转为负）
3. `mmlu×sycophancy` 在 K=3 时本身就是最弱的负向条件（p=1.04e-03，12 个条件中 p 值最大），K=5 下多数投票聚合效应改变了 sycophancy 在 MMLU 上的动力学
4. `arc_challenge×sycophancy` 保持负向不变 — 翻转是 dataset-specific 的
5. 这说明 K=3→K=5 的 transition **部分影响了 split pattern**，但影响很小（仅 1/12 条件翻转），且翻转方向与 K=5 bootstrap 的 K_eff 全正方向一致

---
