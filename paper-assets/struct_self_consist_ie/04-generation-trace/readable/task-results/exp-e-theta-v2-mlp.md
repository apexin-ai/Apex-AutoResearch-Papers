# exp e theta v2 mlp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_e_theta_v2_mlp_20260520T154102_result.json`
- **Structured JSON:** [`4914815651ca4d032cb3.json`](../../sessions/49/4914815651ca4d032cb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registered as `art_20260520_3fc00a`.

**E_θ Variant 2 (MLP) 结果汇总：**

| 指标 | 值 |
|------|-----|
| Configs | 18 (3 datasets × 2 models × 3 seeds) |
| N | 8 |
| θ Grid | {0.3, 0.35, ..., 0.7} |
| Mean F1 Fixed θ=0.5 | **0.7940** |
| Mean F1 MLP Adaptive | **0.7906** (Δ = -0.0034) |
| Mean F1 Oracle θ | **0.7953** (Δ = +0.0013) |
| θ Exact Match | 1/18 (5.6%) |
| θ Within ±0.05 | 5/18 (27.8%) |
| W/T/L vs Fixed | **5W / 0T / 13L** |

**关键观察：**
- MLP 在 LOCO-CV 下表现比 fixed θ=0.5 差，raw predictions 经常大幅偏离合理范围（如 -0.82, 0.71）
- Oracle θ 和 Fixed θ=0.5 之间的 gap 本身很小（仅 +0.13pp），留给 predictor 学习的空间有限
- 18 个数据点对 MLP 太少——same-seed configs 的 features 高度相似导致 LOCO-CV 几乎是在做 extrapolation
- MLP wins 集中在 Qwen×FewNERD 和 Qwen/LLaMA×SciERC（低 degeneracy configs 中 θ<0.5 更优）

---
