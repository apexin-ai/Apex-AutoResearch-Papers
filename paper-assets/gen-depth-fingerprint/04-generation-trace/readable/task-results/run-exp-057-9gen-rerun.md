# run exp 057 9gen rerun

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp_057_9gen_rerun_20260520T073632_result.json`
- **Structured JSON:** [`b41a218856b0a0567471.json`](../../sessions/b4/b41a218856b0a0567471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 9-gen LOGO 结果（修复 Gemma 数据后）

### 总体

| 指标 | 值 |
|------|-----|
| 总样本数 | 42,015 (旧: 38,119, +3,896) |
| 3-class F1 | **0.7510** |
| Binary F1 | **0.6661** |
| 8-gen baseline | 0.7698 |
| Δ (9gen - 8gen) | **-0.0188** |

### Per-generator 3-class F1（held-out）

| Generator | F1 | 95% CI | Binary F1 | Δ vs 8gen |
|-----------|-----|--------|-----------|-----------|
| pythia-1b | 0.8571 | [0.848, 0.866] | 0.7850 | +0.0007 |
| qwen3-0.6b | 0.8185 | [0.807, 0.830] | 0.7432 | -0.0039 |
| pythia-2.8b | 0.8117 | [0.801, 0.822] | 0.7281 | -0.0052 |
| qwen3-1.7b | 0.8114 | [0.800, 0.823] | 0.7460 | +0.0016 |
| olmo-2-1b | 0.7732 | [0.762, 0.784] | 0.6917 | -0.0010 |
| llama-3.2-3b | 0.7591 | [0.748, 0.770] | 0.6797 | -0.0030 |
| qwen3-8b | 0.6955 | [0.683, 0.709] | 0.6468 | -0.0054 |
| **gemma-2-2b** | **0.6279** | [0.622, 0.634] | **0.4402** | (new) |
| mistral-7b-v0.3 | 0.6045 | [0.593, 0.617] | 0.5338 | -0.0114 |

### 修复前后对比（Gemma-2-2B）

| 指标 | 旧 (1061行) | 新 (4957行) | 变化 |
|------|------------|------------|------|
| 3-class F1 | 0.6143 | 0.6279 | +0.014 |
| gen-0 F1 | 0.9737 | 0.9914 | +0.018 |
| gen-1 F1 | 0.0625 | 0.0363 | -0.026 |
| gen-2+ F1 | 0.8067 | 0.8560 | +0.049 |
| Binary F1 | 0.5539 | 0.4402 | **-0.114** |
| Binary CI | [0.422, 0.684] | [0.432, 0.449] | CI 大幅收窄 |

### 关键发现

1. **9-gen 总体 F1 基本不变**：0.7510 vs 旧的 0.7516，差异 -0.0006，修复 Gemma 数据对整体影响很小。

2. **Gemma-2-2B 是最难泛化的 generator 之一**：3-class F1=0.628，仅略高于 Mistral (0.605)。gen-1 F1 极低（0.036），说明分类器几乎无法区分 Gemma 的 gen-1 和其他类别。Binary F1=0.440，9 个 generator 中最低。

3. **Qwen3-8B（7B+ 代表）表现中等偏下**：3-class F1=0.696，binary F1=0.647。在小模型（pythia-1b=0.857, qwen3-0.6b=0.819）和大模型之间有明显的 gap，与 model scale 使分类更困难的假设一致。

4. **vs 8-gen baseline**：加入 Gemma 后，原有 8 个 generator 的表现普遍轻微下降（-0.011 ~ +0.002），最大降幅在 Mistral（-0.011）。总体 Δ=-0.019，表明增加 diverse generator 会稍微增加泛化难度。

5. **CI 收窄是修复的主要收益**：旧 Gemma binary CI 宽度 0.262，新的仅 0.017——数据充足后置信区间合理了。

---
