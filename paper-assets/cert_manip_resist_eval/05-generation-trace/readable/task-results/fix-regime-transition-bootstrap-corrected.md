# fix regime transition bootstrap corrected

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_regime-transition-bootstrap-corrected_20260523T175031_result.json`
- **Structured JSON:** [`05516ed5017fc0e6fc9b.json`](../../sessions/05/05516ed5017fc0e6fc9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总耗时约 7 分钟（K=3: 9s, K=5: 104s, K=7: 296s）。

## 结果对比（Old → New）

| K | η_max sig | K_eff sig | 变化 |
|---|-----------|-----------|------|
| K=3 | 5 → **3** | 1 → **4** | **Changed** |
| K=5 | 0 → **0** | 7 → **10** | **Changed** |
| K=7 | 0 → **0** | 5 → **9** | **Changed** |

修正 error handling 后的影响：

- **K_eff 显著性普遍增强**：K=3 从 1→4, K=5 从 7→10, K=7 从 5→9。排除 error 样本后 K_eff 的 regime transition 效应更强更一致。
- **η_max 在 K=3 下降**：5→3。之前将 API error 当作 tie 人为膨胀了 η_max 的显著性。
- **K=5/K=7 的 η_max 保持 0**：修正前后都不显著。
- 1365 个无效样本被过滤（占总量 ~2%）。

结果已写入 `docs/paper/data/regime_transition_corrected.json`。

---
