# paper audit tables 2 10

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_audit_tables_2_10_20260523T110133_result.json`
- **Structured JSON:** [`e0a8c8dfd50117bd516e.json`](../../sessions/e0/e0a8c8dfd50117bd516e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计总结

**已修复**：
- `experiments_c1.tex` line 49, 54 + `appendix_extended.tex` line 50：LLaMA-8B 0v1 从 `0.9225`（CV估计）改为 `0.9224`（bootstrap估计），与 Table 10 (.9224) 一致。

**需要人工核实 — Mistral-7B**：
论文 Table 10 中 Mistral-7B 的全部 5 个 AUC 值与 registry 中**所有** Mistral 实验都不匹配：

| Pair | 论文 | exp_019 (self) | exp_019b (cross) |
|------|------|----------------|------------------|
| 0v1 | .9170 | .9843 | .9209 |
| 1v2 | .5750 | .5935 | .5695 |
| 2v3 | .5369 | .5402 | .5335 |
| 3v4 | .5174 | .5232 | .5140 |
| 4v5 | .5175 | .5181 | .5184 |

这些值看起来介于 self-scored 和 cross-scored 之间，但不是简单平均。可能来自未注册的实验。请确认数据源。

**Registry 需更新（非论文错误）**：
- `exp_002_olmo_depth` 的 3v4 (0.5034) 和 4v5 (0.4971) 已过时，论文使用的是 `exp_olmo1b_c4_rerun` 的值 (0.5024, 0.4942)。

**可忽略的精度差异**：Gemma-2B 3v4 (Δ=0.0003) 和 4v5 (Δ=0.0001)，在存储精度误差范围内。

---
