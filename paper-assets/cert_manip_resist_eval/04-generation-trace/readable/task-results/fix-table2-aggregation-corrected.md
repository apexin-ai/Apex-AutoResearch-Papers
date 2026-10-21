# fix table2 aggregation corrected

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table2-aggregation-corrected_20260523T181032_result.json`
- **Structured JSON:** [`c7166d78410aae6bb85d.json`](../../sessions/c7/c7166d78410aae6bb85d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Table 2 修正结果对比：

| Method | Metric | Old (buggy) | New (V2) |
|--------|--------|-------------|----------|
| **Threshold** | η_sig | 12/12 | 12/12 |
| | K_sig | 11/12 | 11/12 |
| | K_dir | 10+/1- | **11+/0-** |
| | R² | 0.89 | 0.829 |
| **Majority** | η_sig | 9/12 | **10/12** |
| | K_sig | 8/12 | **12/12** |
| | K_dir | 7+/1- | **12+/0-** |
| | R² | 0.298 | 0.327 |
| **Weighted** | η_sig | 9/12 | 9/12 |
| | K_sig | 9/12 | **12/12** |
| | K_dir | 9+/0- | **12+/0-** |
| | R² | 0.284 | 0.328 |
| **Bayesian** | η_sig | 9/12 | 9/12 |
| | K_sig | 7/12 | 6/12 |
| | K_dir | 1+/6- | **5+/1-** |
| | R² | 0.104 | 0.087 |

关键发现：
- **Bayesian direction reversal 确认**：1+/6- → 5+/1-，旧的负方向是 error 被当作 "tie" 导致的 log-odds 偏差伪影
- **Majority/Weighted**：K_eff 现在全部 12/12 显著且方向一致为正，error-as-tie 之前在掩盖 diversity signal
- **Threshold**：那个虚假的负方向条件消失了（10+/1- → 11+/0-）
- 修正后 **强化了论文的核心论点**：judge diversity 提升操纵抵抗力

输出已写入 `docs/paper/data/table2_corrected.json`。

---
