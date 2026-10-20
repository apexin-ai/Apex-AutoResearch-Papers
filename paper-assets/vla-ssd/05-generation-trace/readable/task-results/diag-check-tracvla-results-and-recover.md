# diag check tracvla results and recover

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check_tracvla_results_and_recover_20260521T191136_result.json`
- **Structured JSON:** [`462a6a903652ce3fcc6a.json`](../../sessions/46/462a6a903652ce3fcc6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 实验状态

| 实验 | 状态 | 当前阶段 | 进度 |
|------|------|---------|------|
| tracvla_long_v1 | **运行中** | trained / Phase 5 counterfactual / paraphrased | ~200/5000 |
| tracvla_goal_v1 | **运行中** | trained / Phase 5 counterfactual / paraphrased | ~400/5000 |

- GPU: 2× ~9GB/98GB，43% 利用率
- **`untrained/` 目录尚未创建**——两个实验都还在跑 trained 条件
- paraphrased 是第 4 个 counterfactual 条件（前 3 个: wrong, empty, shuffled 已完成）
- 预计 paraphrased 还需 ~28min，之后整个 untrained pipeline（Phase 1-5）约需 3h+

---

### tracvla_long — trained 已完成结果

**R² Probing (action_r2_probing.json):**

| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 0.7950 | 0.6160 |
| L4 | 0.8027 | 0.7733 |
| L8 | 0.8103 | 0.7924 |
| L11 | 0.8163 | **0.8168** (peak) |
| L16 | **0.8264** (peak) | 0.8079 |
| L20 | 0.8242 | 0.7980 |
| L24 | 0.8180 | 0.7496 |
| L28 | 0.8115 | 0.6144 |
| L30 | 0.7987 | **0.4336** (trough) |
| L31 | 0.7900 | 0.6186 (bounce) |

- image_mean: 平坦（0.795→0.790），几乎无衰减
- last_preaction: **严重 exit collapse**，peak 0.817@L11 → trough 0.434@L30，Δ=0.383

**L1 Attention:**
- Instruction-dominant: **30/32**，mixed: 2，image-dominant: 0
- Top 5: head_8=0.949, head_26=0.886, head_19=0.873, head_20=0.854, head_1=0.853
- Mixed heads: head_13=0.430, head_22=0.464

**Cross-instruction Classification:**
- image_mean: **1.0** all layers（L0-L31）
- last_preaction: L0=0.983, L1+=**1.0**

**Counterfactual (interim d-values from log):**
- wrong: d=1.418, empty: d=1.473, shuffled: d=1.391, paraphrased: running

---

### tracvla_goal — trained 已完成结果

**R² Probing (action_r2_probing.json):**

| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 0.8027 | 0.6122 |
| L4 | 0.8099 | 0.7949 |
| L8 | 0.8294 | 0.7827 |
| L12 | 0.8162 | 0.7843 |
| L18 | 0.8358 | **0.8024** (peak) |
| L23 | **0.8416** (peak) | 0.7499 |
| L24 | 0.8385 | 0.7411 |
| L28 | 0.8173 | 0.6046 |
| L30 | 0.8118 | **0.3072** (trough) |
| L31 | 0.8048 | 0.5741 (bounce) |

- image_mean: 平坦（0.803→0.805），range 仅 0.039
- last_preaction: **更严重的 exit collapse**，peak 0.802@L18 → trough **0.307@L30**，Δ=**0.495**

**L1 Attention:**
- Instruction-dominant: **27/32**，mixed: 5，image-dominant: 0
- Top 5: head_8=0.943, head_26=0.900, head_19=0.897, head_20=0.852, head_1=0.842
- Mixed heads: head_2=0.450, head_6=0.488, head_13=0.417, head_22=0.417, head_24=0.480

**Cross-instruction Classification:**
- image_mean: L0=0.996, L1+=~1.0
- last_preaction: L0=**0.915**, L1+=1.0

**Counterfactual (interim d-values from log):**
- wrong: d=1.405, empty: d=1.524, shuffled: d=1.336, paraphrased: running

---

### 关键数字记录（仅 trained，遵守 C001 不下结论）

1. **R² exit collapse**：两个实验一致，last_preaction 在 L30 出现深谷（long: 0.434, goal: **0.307**），goal 比 long 更极端
2. **L1 attention 分布**：两实验 top heads 高度一致（head_8/26/19/20/1），goal 的 mixed heads 更多（5 vs 2）
3. **Cross-instruction**：几乎完美可分（≥0.996），说明 instruction identity 在所有层都被保留
4. **Counterfactual interim ranking**：empty > wrong > shuffled（两实验一致）

**⚠️ 等 untrained 数据齐全后才能做 trained-vs-untrained 对比和归因分析。**

---
