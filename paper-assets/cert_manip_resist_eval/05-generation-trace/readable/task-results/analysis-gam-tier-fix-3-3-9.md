# analysis gam tier fix 3 3 9

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gam-tier-fix-3-3-9_20260522T192555_result.json`
- **Structured JSON:** [`94e753eba1bb814b962d.json`](../../sessions/94/94e753eba1bb814b962d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存至 `/root/cert_manip_resist_eval/artifacts/results/plan001/gam_tier_analysis_corrected.json`。

## 结果汇总

### Panel Tier 分布（3/3/9 分类）
- Frontier: 37 panels
- Mid: 37 panels  
- Lightweight: **381** panels (83.7%，符合预期)

### 新旧对比（Old 4/6/5 → New 3/3/9）

| Method | K_eff FDR sig | η_max FDR sig |
|---|---|---|
| Canonical OLS | 8/12 → **8/12** (不变) | 11/12 → **11/12** (不变) |
| + Tier indicators | 5/12 → **5/12** (不变) | 10/12 → **11/12** (+1) |
| GAM (nonlinear) | 12/12 → **12/12** (不变) | 12/12 → **12/12** (不变) |

### Tier-indicator OLS (K_eff 5/12 sig, 4+/1−)
- 显著的 5 个 condition: mmlu×prompt_injection (+), mmlu×verbosity_bias (+), arc×prompt_injection (+), arc×sycophancy (−), arc×position_bias (+)

### GAM K_eff sign split
6+/6− 方向 split **仍然成立**，与旧分类一致。

### 关键发现
修正 tier 分类后聚合结论完全不变——K_eff 从 canonical 8/12 降到 tier-controlled 5/12，η_max 保持 11-12/12 高度显著。tier 分类的具体选择对宏观结论不敏感。

---
