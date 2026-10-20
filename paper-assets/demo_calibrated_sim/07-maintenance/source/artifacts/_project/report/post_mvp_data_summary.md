# Post-MVP 全实验数据汇总

> 生成日期: 2026-05-13 | 用途: paper_framing.md 更新 + experiment_plan.yaml 创建

---

## 1. 实验总览

| 实验线 | exp_id | 模型 | 方法 | Conclusion | 论文角色 |
|--------|--------|------|------|-----------|---------|
| 7B BCP | mvp-004 | Qwen2.5-7B-Instruct | BCP prompting | negative | C1 主证据 (FM1/FM2/FM3) |
| 7B DPO+BCP | hgate-dpo003-merged | Qwen2.5-7B-DPO003-merged | DPO LoRA + BCP | negative | C2 主证据 (FM4 reversal) |
| 14B BCP | qwen14b-bcp-001 | Qwen2.5-14B-Instruct (FP16, TP=2) | BCP prompting | success | C3 主证据 (scale transition) |
| 7B DPO training | dpo-003 | Qwen2.5-7B-Instruct | DPO LoRA (Fix B) | success | C2 辅助 (DPO 训练有效) |
| Diagnosis | diag-lora-merge | Qwen2.5-7B-DPO003-merged | merge eval | success | C2 辅助 (排除 LoRA bug) |
| Llama BCP | llama-bcp-001 | Llama-3-8B-Instruct | BCP prompting | killed | 辅助证据 (floor effect) |
| Mistral BCP | mistral-bcp-001 | Mistral-7B-Instruct-v0.3 | BCP prompting | negative | 辅助证据 (tool-call 能力不足) |

---

## 2. 7B BCP — mvp-004 (C1 主证据)

**设置**: Qwen2.5-7B-Instruct, tau-bench retail, 20 tasks, 6 variants, 1 run

### Per-variant 指标

| Variant | Completion | Politeness | Question Rate | n |
|---------|-----------|------------|---------------|---|
| baseline | 0.368 | 0.559 | 0.044 | 19 |
| aave_target | 0.100 | 0.468 | 0.015 | 20 |
| indian_english | 0.150 | 0.460 | 0.014 | 20 |
| overcorrected | 0.263 | 0.605 | 0.018 | 19 |
| single_dim_question | 0.250 | 0.416 | 0.065 | 20 |
| single_dim_politeness | 0.200 | 0.634 | 0.021 | 20 |

### FM 证据

| FM | 指标 | 值 | 判定 |
|----|------|-----|------|
| FM1 全局抑制 | aave retention | 27.2% (0.100/0.368) | **复现** (threshold <80%) |
| FM1 全局抑制 | indian retention | 40.8% (0.150/0.368) | **复现** |
| FM2 跨维度干扰 | sdq→politeness | -25.6% (0.416 vs 0.559) | **复现** |
| FM2 跨维度干扰 | sdp→question_rate | -52.3% (0.021 vs 0.044) | **复现** (但基线仅 0.044) |
| FM3 过校正反弹 | overcorrected pol | +8.2% (0.605 vs 0.559, +4.6pp) | **复现** |

### Gate 结果
H1: PASS | H2: FAIL | H3: FAIL | Overall: **FAIL (1/3)**

---

## 3. 7B DPO+BCP — hgate-dpo003-merged (C2 主证据)

**设置**: Qwen2.5-7B-DPO003-merged (merged model serving), tau-bench retail, 20 tasks, 6 variants, 4 runs

### Per-variant 指标 (4 runs)

#### Completion
| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| baseline | 0.278 | 0.150 | 0.400 | 0.350 | **0.294** |
| aave | 0.150 | 0.444 | 0.300 | 0.100 | **0.249** |
| indian_english | 0.150 | 0.158 | 0.250 | 0.105 | **0.166** |
| overcorrected | 0.150 | 0.250 | 0.278 | 0.158 | **0.209** |
| single_dim_question | 0.100 | 0.263 | 0.200 | 0.316 | **0.220** |
| single_dim_politeness | 0.300 | 0.150 | 0.350 | 0.316 | **0.279** |

#### Politeness
| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| baseline | 0.475 | 0.466 | 0.532 | 0.534 | **0.502** |
| aave | 0.609 | 0.559 | 0.583 | 0.514 | **0.566** |
| indian_english | 0.577 | 0.534 | 0.510 | 0.638 | **0.565** |
| overcorrected | 0.569 | 0.508 | 0.581 | 0.637 | **0.574** |
| single_dim_question | 0.477 | 0.402 | 0.478 | 0.545 | **0.475** |
| single_dim_politeness | 0.576 | 0.669 | 0.590 | 0.604 | **0.610** |

### FM4 (DPO+BCP Reversal) 证据

| 指标 | Base BCP (mvp-004) | DPO+BCP (hgate-dpo003-merged) | 方向 |
|------|-------------------|-------------------------------|------|
| AAVE pol gap | -0.091 (correct ↓) | +0.064 (**reversed** ↑) | ⚠️ 反转 |
| Indian pol gap | -0.099 (correct ↓) | +0.063 (**reversed** ↑) | ⚠️ 反转 |
| H2 gap reduction | 25-28% | **-10.3%** (wrong direction) | ⚠️ 反转 |
| Variant×run gap expansion | — | **10/12** checks expanded | ⚠️ 系统性 |
| Overcorrected rebound | +8.2% | **+14.3%** (amplified) | ⚠️ 放大 |

### Gate 结果 (aggregate)
H1: PASS (4/4) | H2: **FAIL (0/4)** | H3: FAIL (3/4) | Overall: **FAIL**

### DPO 训练有效性证据 (dpo-003 + diag-lora-merge)
- DPO-003 training: loss 0.653, accuracy 0.75-1.0, margin 0.05-0.17 (有效学习)
- Merged model completion: 60% vs base 40% (+50%) → DPO 改善了 tool-calling
- vLLM LoRA serving bug: 15% vs merged 60% → 已排除 serving artifact

---

## 4. 14B BCP — qwen14b-bcp-001 (C3 主证据)

**设置**: Qwen2.5-14B-Instruct FP16 (TP=2), tau-bench retail, 20 tasks, 6 variants, 4 runs

### Per-variant 指标 (4 runs)

#### Completion
| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| baseline | 0.737 | 0.550 | 0.579 | 0.600 | **0.616** |
| aave_target | 0.700 | 0.474 | 0.632 | 0.600 | **0.601** |
| indian_english | 0.650 | 0.600 | 0.842 | 0.650 | **0.686** |
| overcorrected | 0.750 | 0.500 | 0.600 | 0.650 | **0.625** |
| single_dim_question | 0.500 | 0.700 | 0.600 | 0.600 | **0.600** |
| single_dim_politeness | 0.600 | 0.800 | 0.474 | 0.750 | **0.656** |

#### Politeness
| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| baseline | 0.470 | 0.588 | 0.497 | 0.536 | **0.523** |
| aave_target | 0.393 | 0.454 | 0.493 | 0.455 | **0.449** |
| indian_english | 0.462 | 0.442 | 0.427 | 0.444 | **0.444** |
| overcorrected | 0.453 | 0.419 | 0.466 | 0.467 | **0.451** |
| single_dim_question | 0.449 | 0.499 | 0.463 | 0.512 | **0.481** |
| single_dim_politeness | 0.489 | 0.438 | 0.456 | 0.403 | **0.447** |

#### Question Rate
| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| baseline | 0.037 | 0.035 | 0.054 | 0.041 | **0.042** |
| aave_target | 0.044 | 0.015 | 0.044 | 0.008 | **0.028** |
| indian_english | 0.038 | 0.023 | 0.027 | 0.018 | **0.027** |
| overcorrected | 0.015 | 0.028 | 0.010 | 0.011 | **0.016** |
| single_dim_question | 0.048 | 0.017 | 0.034 | 0.005 | **0.026** |
| single_dim_politeness | 0.018 | 0.023 | 0.016 | 0.021 | **0.020** |

### FM 复现分析

| FM | 指标 | 14B 值 | 7B 值 | 14B 判定 |
|----|------|--------|-------|---------|
| FM1 | aave retention | 97.6% | 27.2% | **未复现** |
| FM1 | indian retention | 111.2% | 40.8% | **未复现** |
| FM2 | sdq→politeness | -8.0% (-4.2pp) | -25.6% | **弱复现** |
| FM2 | sdp→question_rate | -52.8% (-2.2pp) | -52.3% | **弱复现** (绝对值小) |
| FM3 | overcorrected pol | -13.6% (-7.1pp) | +8.2% (+4.6pp) | **未复现** (方向反) |

### Gate 结果
H1: PASS (4/4) | H2: **FAIL (1/4)** | H3: PASS (4/4) | Overall: 1/4

---

## 5. Scale-Dependent Failure Mode Transition (核心发现)

| 维度 | 7B (mvp-004) | 14B (qwen14b-bcp-001) |
|------|-------------|----------------------|
| **失败模式** | 灾难性崩溃 (过度响应) | 选择性忽略 (不够响应) |
| **Completion** | 10-26% (崩溃) | 60-69% (正常) |
| **FM1 全局抑制** | ✅ 严重 (retention 27-41%) | ❌ 未复现 (retention >97%) |
| **FM2 跨维度** | ✅ 显著 | ⚠️ 弱 (幅度远小) |
| **FM3 过校正** | ✅ 反弹 (+4.6pp) | ❌ 反向 (-7.1pp) |
| **H2 校准** | FAIL | FAIL |
| **根因** | BCP prompt 扰动 > 模型能力 → 行为崩溃 | 模型能力 > BCP prompt → 忽略校准 |

**结论**: BCP 在所有 scale 都失败，但失败机制随 scale 转变。不存在"刚好合适"的 scale 让 BCP 成功——7B 太弱会崩溃，14B 太强会忽略。这是方法论层面的缺陷。

---

## 6. 辅助实验数据

### Llama-3-8B (llama-bcp-001) — killed
- Completion: 5% (floor effect, tool-calling 能力不足)
- 三 variant completion 完全一致，BCP 对 completion 效果严格为零
- 降级为辅助证据：仅支持"低能力模型在 BCP 下也展现行为偏移"

### Mistral-7B (mistral-bcp-001) — negative  
- Completion: 0% (无法在 16-tool 场景生成 structured tool_calls)
- 1 tool 正常, 16 tools FAIL
- 无可用 BCP 数据

---

## 7. Paper Claims → Evidence 映射 (更新版)

| Claim | Evidence | Strength | exp_id |
|-------|----------|----------|--------|
| C1: FM1 全局抑制 | 7B retention 27-41% | Moderate (1 model, 1 run, n=19-20) | mvp-004 |
| C1: FM2 跨维度干扰 | 7B politeness -25.6%, qrate -52.3% | Moderate | mvp-004 |
| C1: FM3 过校正反弹 | 7B +4.6pp (1 run); DPO+BCP +7.2pp mean (4 runs, 4/4) | Moderate-Strong | mvp-004, hgate-dpo003-merged |
| C2: FM4 DPO reversal | gap expansion 10/12, H2 -10.3% wrong direction | Strong (4 runs, 80 episodes) | hgate-dpo003-merged |
| C2: DPO 训练有效 | acc 0.75-1.0; merged 60% vs base 40% | Strong | dpo-003, diag-lora-merge |
| C3: Scale transition | 14B H2 FAIL but FM1/FM3 NOT replicated → different failure mode | Strong (4 runs, 80 episodes) | qwen14b-bcp-001 |
| C3: No "right" scale | 7B over-responds, 14B under-responds, both fail H2 | Moderate (2 scales, 1 model family) | mvp-004, qwen14b-bcp-001 |
| C4: Implications | Analytical, grounded in C1-C3 | Analytical | — |
