# ssh exp020 diagnosis analysis

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp020-diagnosis-analysis_20260525T151912_result.json`
- **Structured JSON:** [`9e0e1cf9a8d81b7448a0.json`](../../sessions/9e/9e0e1cf9a8d81b7448a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已收集。以下是诊断汇总：

---

## 诊断结果汇总

### Diagnosis 1: 逐模型排名表

| Model | Grp | ELO | ELO_R | Raw_R | Joint_R | ΔJoint | c_joint |
|---|---|---|---|---|---|---|---|
| claude-3-5-sonnet | NEW | 1298 | 2 | 1 | 1 | -1 | 1.28 |
| gpt-4o | ORIG | 1300 | 1 | 2 | 2 | +1 | 0.96 |
| qwen2.5-72b | ORIG | 1269 | 6 | 4 | **3** | **-3** | 1.64 |
| gpt-4-turbo | NEW | 1272 | 5 | 3 | 4 | -1 | 3.76 |
| mistral-large | NEW | 1250 | 9 | 6 | **5** | **-4** | 1.45 |
| gpt-4o-mini | ORIG | 1286 | 3 | 5 | **6** | **+3** | 1.47 |
| llama-3.3-70b | ORIG | 1275 | 4 | 7 | **7** | **+3** | 1.32 |
| claude-3-opus | NEW | 1262 | 7 | 8 | 8 | +1 | 1.57 |
| gemma-2-27b | NEW | 1231 | 10 | 10 | 9 | -1 | 1.48 |
| llama-3.1-70b | NEW | 1261 | 8 | 9 | **10** | **+2** | 2.49 |
| gpt-4-0613 | ORIG | 1186 | 14 | 16 | 16 | +2 | 3.78 |

**Joint 引入的 3 个额外 pairwise 错误**（Raw 没有的）：
- `gemma-2-27b > llama-3.1-70b`（Arena: <）
- `gpt-4-turbo < qwen2.5-72b`（Arena: >）
- `gpt-4o-mini < mistral-large`（Arena: >）

Raw 没有 Joint 不犯的错误——Joint 严格增加了 3 个 disagreement（11→14/136）。

### Diagnosis 2: 原始 8 模型子集

原始 7 个模型（去掉 qwen3-8b）在 N=17 run 中：
- **所有方法 τ 都一样** = 0.810，ρ = 0.893
- 对比 N=8 standalone τ=0.857，**退化了 Δτ=-0.048**
- 说明退化不只来自新模型，**原始模型间的排名精度也在大 N 下变差**

新增 10 模型子集：raw τ=0.867, joint τ=0.822 → joint 在新模型上也劣于 raw。

### Diagnosis 3: Exposure 估计

**关键发现**：
- Exposure CSV 仅覆盖 **317/500 items**（来自 exp-002 的原始 Arena Hard 子集）
- **53.8% 的 items（269/500）e_i=0**，包括 86 个 CSV 中本身 e_i=0 的 + 183 个没有覆盖的
- G-MFRM 的 gating 机制对超过一半的 items 完全没有 contamination 信号
- 这导致 G-MFRM 在大部分 items 上退化为 vanilla MFRM，contamination 校正效果打了折

### Diagnosis 5: Ground Truth

- 所有 17 模型都成功匹配到 Arena ELO
- 中间段极其密集：ELO 1261-1300 之间挤了 8 个模型，差距仅 1-12 分
- 特别是 `claude-3-opus`(1262) vs `llama-3.1-70b`(1261) 仅差 1 分，`gpt-4-turbo`(1272) vs `qwen2.5-72b`(1269) 仅差 3 分
- 排名 3-8 位的模型 ELO 间距极小，**任何微小的 θ 估计偏差都会导致排名反转**

### 根因分析

τ 退化的主要原因是 **三重叠加**：
1. **Exposure 覆盖不足**（53.8% items 无 exposure）→ gating 半盲，contamination 校正不完整
2. **ELO 中段过于密集**（8 个模型挤在 39 ELO 范围内）→ 排名对 θ 误差极敏感
3. **joint_gmfrm 的 c 估计对 gpt-4-0613/gpt-4-turbo 给出极高 c（~3.8）**，可能过度校正了这两个模型的 θ，引入了额外排名误差

---
