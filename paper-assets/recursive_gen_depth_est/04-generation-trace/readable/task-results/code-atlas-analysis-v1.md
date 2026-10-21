# code atlas analysis v1

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_atlas_analysis_v1_20260514T183352_result.json`
- **Structured JSON:** [`c95ed14b7789d25cf282.json`](../../sessions/c9/c95ed14b7789d25cf282.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果摘要：**

| 分析 | 关键数值 |
|------|---------|
| **Monotonicity** | var_surprisal、p90_ppl 在 4 个 chain 上 Spearman ρ 均在 -0.82~-0.89，符合预期 |
| **EDD** | 所有 19 个特征 × 4 个 chain 的 EDD 均为 3（depth 0-3 范围内未饱和，退化持续） |
| **Feature Consistency** | 3-way Jaccard = 0.667，三模型共享 top-5 中 4 个特征（var_surprisal, p90_ppl, p75_ppl, mean_surprisal） |
| **Rank Correlation** | Pythia↔GPT2XL ρ=0.904, OLMo↔GPT2XL ρ=0.853, Pythia↔OLMo ρ=0.647，全部 p<0.01 |

**文件位置：**
- 服务器：`/root/autodl-tmp/recursive_gen_depth_est/artifacts/atlas/` 下 4 个 JSON
- 本地脚本：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/scripts/atlas_analysis.py`
- 4 个 artifact 已注册

---
