# analysis partial knowledge adversary

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partial-knowledge-adversary_20260523T004625_result.json`
- **Structured JSON:** [`8f521fafbfa464b159c2.json`](../../sessions/8f/8f521fafbfa464b159c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

**Partial-Knowledge Adversary Ablation (2/3 vs 3/3 judges known)**

| Metric | Oracle | Partial-Knowledge |
|--------|--------|-------------------|
| η_max β_std (mean) | 0.387 | 0.589 (+52.2%) |
| η_max FDR sig | 11/12 | **12/12** |
| K_eff β_std (mean) | 0.164 | -0.011 |
| K_eff FDR sig | 8/12 | 5/12 |

核心发现：partial-knowledge adversary 下 η_max dominance 不仅没有减弱，反而**增强**了。η_max 标准化 β 增加 52%，FDR 显著条件从 11/12 增到 12/12。K_eff 预测力大幅下降（β 接近零）。

论文 narrative：oracle adversary assumption 不是 η_max dominance 的必要条件——即使 adversary 只知道 2/3 judges，weakest-link 效应仍然主导 panel 脆弱性。

产出：
- 脚本：`/root/cert_manip_resist_eval/scripts/run_partial_knowledge_adversary.py`
- 结果：`artifacts/results/plan001/partial_knowledge_adversary.json`（服务器+本地）

---
