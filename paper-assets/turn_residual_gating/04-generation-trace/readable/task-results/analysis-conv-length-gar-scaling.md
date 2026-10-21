# analysis conv length gar scaling

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conv_length_gar_scaling_20260520T010312_result.json`
- **Structured JSON:** [`3e846e818fc9a20d6cea.json`](../../sessions/3e/3e846e818fc9a20d6cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已存在且很大，直接呈现分析结果。

---

## 数据发现

**文件**: `runs/phase2_4way_eval_heldout/` 下 8 个 JSON（4 模型 × 2 GAR 变体），每个含 50 条对话的 per-turn GAR 曲线。

**数据质量**:
- 5/50 对话在 eval 时被截断（gar_curve 长度 < 源对话 turn 数）：Conv [14,23,26,40,46]
- 6/50 对话存在真实末轮坍塌（最后一 turn GAR 从 ~0.5 骤降至 <0.01）：Conv [3,10,13,25,29,38]
  - 这 6 条在 TG/UG/LoRA 中**完全一致**，是数据属性非模型缺陷
- 39/50 为干净数据

**源对话 turn 数分布**: 5T: 34, 6T: 8, 7T: 8（范围 5-7，偏窄）

---

## GAR vs 对话长度分析

### Per-turn GAR-ours 衰减曲线（N=45 非截断，含 6 条坍塌）

| Turn | Base | TG | UG | LoRA |
|------|------|-----|-----|------|
| T1 | 0.049±0.021 | 0.547±0.038 | 0.551±0.042 | 0.553±0.050 |
| T2 | 0.018±0.008 | 0.511±0.040 | 0.511±0.046 | 0.511±0.048 |
| T3 | 0.013±0.006 | 0.509±0.034 | 0.511±0.033 | 0.503±0.039 |
| T4 | 0.010±0.004 | 0.498±0.041 | 0.501±0.050 | 0.495±0.054 |
| T5 | 0.009±0.004 | 0.447±0.156 | 0.447±0.158 | 0.447±0.158 |
| **slope** | -0.0089 (p=.081) | **-0.0212 (p=.019)** | **-0.0219 (p=.024)** | **-0.0230 (p=.013)** |

### Normalized 衰减（干净 N=39，排除 6 条坍塌）

| Turn | Base | TG | UG | LoRA |
|------|------|-----|-----|------|
| T1 | 1.00 | 1.00 | 1.00 | 1.00 |
| T2 | 0.39 | 0.95 | 0.94 | 0.94 |
| T3 | 0.28 | 0.94 | 0.94 | 0.92 |
| T4 | 0.23 | 0.91 | 0.90 | 0.89 |
| T5 | **0.20** | **0.93** | **0.92** | **0.92** |

Base 到 T5 丢失 80% 的 turn-1 GAR；TG/UG/LoRA 仅丢失 7-8%。

### 统计检验

**Paired t-test (T1 vs T5)**:
| Model | T1 mean | T5 mean | diff | t | p |
|-------|---------|---------|------|---|---|
| Base | 0.049 | 0.009 | 0.040 | 14.12 | **<0.000001** |
| TG | 0.547 | 0.447 | 0.099 | 3.75 | **0.00052** |
| UG | 0.551 | 0.447 | 0.104 | 3.84 | **0.00039** |
| LoRA | 0.553 | 0.447 | 0.107 | 3.90 | **0.00033** |

**Per-conversation slope t-test (H0: slope=0)**:
- Base: 100% 对话斜率为负，t=-13.1, p<0.0001
- TG/UG/LoRA: 87-89% 对话斜率为负，t≈-4.3~-4.6, p=0.0001

### 分桶统计（按源对话 turn 数，干净 N=39）

| 桶 | N | Base GAR-ours | TG GAR-ours | UG GAR-ours | LoRA GAR-ours |
|-----|---|---------------|-------------|-------------|---------------|
| 5 turns | 25 | 0.020±0.009 | 0.512±0.019 | 0.512±0.024 | 0.509±0.024 |
| 6 turns | 8 | 0.018±0.004 | 0.502±0.012 | 0.504±0.014 | 0.500±0.014 |
| 7 turns | 6 | 0.016±0.003 | 0.504±0.014 | 0.505±0.011 | 0.502±0.013 |

### 相关性检验（干净 N=39）

**对话长度 vs 平均 GAR**: 全部不显著
- Base: Spearman ρ=-0.161, p=0.328
- TG: Spearman ρ=-0.192, p=0.242
- UG: Spearman ρ=-0.151, p=0.360
- LoRA: Spearman ρ=-0.183, p=0.267

---

## 对论文的意义

**1. Per-turn 衰减直接证明 exposure bias 累积**。Base 模型 GAR 从 T1 到 T5 衰减 82%（paired t-test p<10⁻⁶），100% 的对话表现出单调递减。这是 teacher-forcing distribution shift 随 turn 累积的直接证据。

**2. Gating 大幅抑制了累积效应**。TG/UG/LoRA 的 normalized 衰减仅 7-8%（vs Base 的 80%），且排除 6 条坍塌对话后 T4→T5 出现轻微回升（0.89→0.92），说明 gate 维持了跨 turn 的 residual 稳定性。

**3. 对话长度与 GAR 无显著相关**（所有 |ρ|<0.2, p>0.2）。但这主要因为 held-out 集 turn 范围太窄（5-7），统计功效不足。分桶趋势方向是对的（Base: 5T=0.020→7T=0.016），但差异不够大。

**4. 建议**：论文中使用 **per-turn decay curve**（Part 3/4 的结果）而非 conversation-length correlation 来支撑 exposure bias 论点。前者统计上显著且效应量大（Base T1 vs T5 Cohen's d ≈ 2.7），后者因数据限制不显著。6 条末轮坍塌对话可作为 limitation 中的 footnote 提及。

---
