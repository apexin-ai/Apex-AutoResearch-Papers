# analysis bootstrap full rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-full-rerun_20260520T160048_result.json`
- **Structured JSON:** [`276867e93021b8301014.json`](../../sessions/27/276867e93021b8301014.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量 bootstrap 完成。5/5 家族 s42+s123 全部覆盖（58/75 cells，缺的是 s0 数据）。

### 结果摘要

| Family | n | Baseline | Δ(d100) | 95% CI | Pattern | ρ |
|---|---|---|---|---|---|---|
| Phi-4 | 2 | 76.40% | +0.83pp | [-11.84, +13.49]^t | Incomplete† | -0.10 |
| Qwen2.5-14B | 2 | 69.05% | -11.05pp | [-32.41, +10.30]^t | Collapse | 0.80 |
| Qwen2.5-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37]^t | V-recovery | 0.40 |
| Gemma-2-9B | 2 | 63.85% | +2.62pp | [-11.81, +17.06]^t | V-recovery† | 0.30 |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | Benefit-sat† | 0.03 |

### Qwen2.5-7B s123 加入后的变化
- 从 n=1（仅 s42）升级到 n=2，现在有 t-distribution CI
- Pattern：s42 V-recovery，s123 也是 V-recovery → **Consistent**（之前仅单种子无法判断）
- Δ(d100) 从 -1.78pp（单点）变为 -0.89pp [-12.16, +10.37]

### Phi-4 分类
- s42: Immune，s123: Benefit-sat，s0: Incomplete → **Inconsistent**
- 多数票落在 Incomplete（因为 Phi-4 n=3 但 s0 缺 d050/d100，majority 无法确定单一模式）
- LaTeX 表中标注 `Incomplete†`

### 注意事项
- Phi-4 的 n 在 Δ 表中显示 2（s0 缺数据不参与 d100 delta 计算），ρ=-0.10 表明两个种子的 dose-response 曲线方向不一致
- 所有 n=2 家族的 CI 极宽（t-distribution df=1），统计效力有限

---
