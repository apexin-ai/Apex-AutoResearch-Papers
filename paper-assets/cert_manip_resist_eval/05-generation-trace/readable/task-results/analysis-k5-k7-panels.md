# analysis k5 k7 panels

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-k7-panels_20260523T001931_result.json`
- **Structured JSON:** [`403b8f8d5a6a6068d689.json`](../../sessions/40/403b8f8d5a6a6068d689.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。核心发现：

### Cross-K Comparison Table

| Panel Size | Method | η_max FDR sig | K_eff FDR sig | K_eff sig+ | K_eff sig- |
|---|---|---|---|---|---|
| K=3 | OLS | 11/12 | 8/12 | 7 | 1 |
| K=3 | Clustered SE | 8/12 | 0/12 | 0 | 0 |
| **K=5** | OLS | 10/12 | **12/12** | **11** | 1 |
| **K=5** | Clustered SE | 7/12 | **10/12** | **10** | 0 |
| **K=7** | OLS | 12/12 | **11/12** | **10** | 1 |
| **K=7** | Clustered SE | 6/12 | **10/12** | **10** | 0 |

### 关键结论

**K=3 时的 η_max dominance 在 K=5/K=7 下完全反转为 K_eff dominance：**

1. **K_eff 效应随 K 增大急剧增强**：Clustered SE 从 K=3 的 0/12 飙升至 K=5/K=7 的 10/12，全部为正方向（更多独立 judges → 更高 panel ASR）

2. **η_max 效应被削弱**：Clustered SE 从 K=3 的 8/12 降至 K=7 的 6/12——随 panel 增大，单一最弱 judge 的影响力被稀释

3. **方向一致**：K_eff 显著时几乎全部为正方向（10+/0-），唯一的负方向仅出现在 OLS 中（arc_challenge × sycophancy），且在 clustered SE 下不显著

4. **解释**：K=3 时 panel 太小，diversity 变异不足以压过 weakest-link 效应；K≥5 时 diversity 变异被放大，majority vote 的容错机制使得 independent judges 的价值远超弱 judge 的拖累

---
