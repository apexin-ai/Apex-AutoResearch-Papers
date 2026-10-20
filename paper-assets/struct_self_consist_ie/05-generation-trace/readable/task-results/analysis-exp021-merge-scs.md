# analysis exp021 merge scs

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp021_merge_scs_20260516T215554_result.json`
- **Structured JSON:** [`b0d8ca053c1ffa8bc8a4.json`](../../sessions/b0/b0d8ca053c1ffa8bc8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

有足够数据了。下面输出完整结构化报告。

---

## EXP-021 Few-NERD 全量 SCS 分析报告

### 基本信息
| 指标 | 值 |
|------|------|
| 数据集 | Few-NERD |
| 实例数 | 37,648 |
| N (samples/instance) | 8 |
| 模型 | Qwen (exp_021_fewnerd_full LoRA) |

### 1. Greedy / Oracle F1

| 指标 | Few-NERD | SciERC | 差异 |
|------|----------|--------|------|
| Greedy macro F1 | 0.6469 | 0.6633 | -0.0164 |
| Oracle macro F1 | 0.7541 | 0.7775 | -0.0234 |
| **Headroom** | **0.1073** | **0.1142** | -0.0070 |

### 2. Zero-F1 率

| 指标 | Few-NERD | SciERC |
|------|----------|--------|
| Zero-F1 rate | 0.1744 (6565/37648) | ~0.1259 (52+22 filtered / 551) |
| F1>0 instances | 28,688 | 477 |

### 3. 五信号 Global ρ 和 Conditional ρ

| Signal | Few-NERD Global ρ | Few-NERD Cond ρ | SciERC Global ρ | SciERC Cond ρ |
|--------|-------------------|-----------------|-----------------|---------------|
| LP | **-0.0897** | **0.2299** | 0.2052 | 0.1538 |
| SJ | -0.0079 | **0.2619** | 0.3599 | 0.3113 |
| FK | -0.0418 | 0.0551 | 0.2665 | 0.1761 |
| EM | -0.0620 | **0.4412** | 0.2945 | 0.3596 |
| VC | **0.5200** | 0.0897 | 0.3792 | 0.3000 |

### 4. Selection Delta (选择后 F1 - Greedy F1)

| Signal | Few-NERD Sel F1 | Few-NERD Δ | SciERC Δ (N=16, 3seed mean) |
|--------|----------------|-----------|------------------------------|
| LP | 0.6586 | **+0.0117** | -- |
| SJ | 0.6273 | -0.0195 | -0.0005 |
| FK | 0.6136 | -0.0333 | +0.0015 |
| EM | 0.6136 | -0.0333 | -- |
| VC | 0.6314 | -0.0154 | -0.0309 |

### 5. Bootstrap CI for LP Delta

| 指标 | 值 |
|------|------|
| LP delta mean | +0.0118 |
| 95% CI | **[+0.0102, +0.0134]** |

CI 不含零，LP selection 在 Few-NERD 上**显著**优于 greedy (p < 0.025)。

### 6. Scenario 判定

**判定：Scenario B — Headroom 大但信号弱/反转**

理由：
- Headroom = 0.1073，与 SciERC 相当（0.1142），说明上限充足
- 但 5 个信号中仅 LP 实现 selection > greedy (+0.0117)，其余 4 个**负 delta**
- Global ρ 全面崩坏：SJ/FK/EM 为负或接近零，仅 VC 保持正 (0.52) 但 selection 仍为负
- Conditional ρ 信号相对保留（LP 0.23, SJ 0.26, EM 0.44），但无法转化为有效选择
- 核心矛盾：高 zero-F1 率 (17.4%) 导致 global ρ 被"一致错误"的高信号实例拉向负方向——模型 confident 地生成一致但完全错误的输出

### 7. 关键发现

1. **LP 是 Few-NERD 上唯一有效的 selection 信号**，delta = +0.0117 且统计显著
2. **VC 的 global ρ 极高 (0.52) 但 selection delta 为负**——因为 VC 高的实例往往是模型反复犯同一个错误
3. **EM conditional ρ = 0.4412 是所有信号中最高**——但 EM mode selection 选的 majority 答案恰好不如 greedy
4. Few-NERD 的细粒度类型体系导致模型更容易一致性地错误分类（如 building vs location），高一致性 ≠ 高质量
5. 与 SciERC 对比：所有结构一致性信号 (SJ/FK/EM) 的 global ρ 从正变负，说明信号有效性**不跨数据集泛化**

---
