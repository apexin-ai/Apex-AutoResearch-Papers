# fix tiebreaking rerun k5 epsilon

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tiebreaking-rerun-k5-epsilon_20260523T143954_result.json`
- **Structured JSON:** [`d482de6443e4e0ac350e.json`](../../sessions/d4/d482de6443e4e0ac350e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

---

**方向一致性：0/72 方向变化** — 所有 12 个 condition × 3 个 ε × 2 个指标（K_eff, η_max）的系数方向全部一致（均为正），修复未改变任何结论。

**Top 5 最大 Δβ_std：**

| Condition | ε | metric | old_β | new_β | delta | dir_chg? |
|---|---|---|---|---|---|---|
| arc_challenge_authority_bias | 1e-09 | keff_beta_std | 0.1874 | 0.2857 | 0.0983 | no |
| arc_challenge_authority_bias | 1e-06 | keff_beta_std | 0.2093 | 0.3003 | 0.0910 | no |
| mmlu_score_manipulation | 1e-03 | keff_beta_std | 0.2755 | 0.3635 | 0.0880 | no |
| arc_challenge_position_bias | 1e-03 | keff_beta_std | 0.4902 | 0.5701 | 0.0799 | no |
| arc_challenge_position_bias | 1e-06 | keff_beta_std | 0.4903 | 0.5701 | 0.0799 | no |

**总结：方向变化 0/12 conditions。** 最大 Δβ_std = 0.098（arc_challenge_authority_bias）。ASR=0 比例有变动（最大变化：arc_challenge_authority_bias +0.1183），但不影响回归方向。max_coefficient_change 从 keff=105.75 变为 184.5，eta 从 55.54 变为 31.07。

已完成：
1. 修复 `run_epsilon_sensitivity_k5.py` 和 `run_k4_wild_cluster_bootstrap.py` 的 `counts = {}` → `counts = {"A": 0, "B": 0, "tie": 0}`
2. 重跑并生成新结果
3. 新结果已写入本地 `docs/paper/data/epsilon_sensitivity_k5.json`

---
