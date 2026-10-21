# analysis alternative ews r05

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alternative-ews-r05_20260518T111432_result.json`
- **Structured JSON:** [`1cb867538cc9f4d6c015.json`](../../sessions/1c/1cb867538cc9f4d6c015.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结果：

---

## 对比表：r=0 vs r=0.5

| Metric | r=0 方向 | r=0 变化幅度 | r=0.5 方向 | r=0.5 变化幅度 | 方向一致? | Signal preserved? |
|---|---|---|---|---|---|---|
| Token entropy | DOWN | -9.58% | UP | +2.37% | **REVERSED** | NO |
| Stable rank (attn) | DOWN | -14.01% | UP | +3.70% | **REVERSED** | NO |
| Spectral norm (attn) | UP | +7.95% | DOWN | -1.24% | **REVERSED** | NO |
| Spectral norm (ffn) | UP | +0.66% | DOWN | -0.25% | **REVERSED** | NO |
| Isotropy (avg cos) | DOWN | -75.45% | DOWN | -89.78% | MATCH | NO* |
| Stable rank (ffn) | UP | +1.00% | UP | +2.67% | MATCH | NO* |

\* Isotropy 和 FFN stable rank 方向一致但**不是 collapse-specific**：它们在 r=0.5 下变化更大，说明是 fine-tuning 适应行为而非 collapse 信号。

## Raw Values（关键 Gen）

**Token entropy:**
| | Gen 0 | Gen 2 | Gen 5 | Gen 10 |
|---|---|---|---|---|
| r=0 | 6.752 | 6.714 | 6.511 | **6.106** |
| r=0.5 (adaptive) | 6.752 | 6.784 | 6.838 | **6.912** |
| r=0.5 (fixed_mix) | 6.752 | 6.784 | 6.835 | **6.914** |

**Stable rank (attn):**
| | Gen 0 | Gen 2 | Gen 5 | Gen 10 |
|---|---|---|---|---|
| r=0 | 33.83 | 33.72 | 32.83 | **29.09** |
| r=0.5 (adaptive) | 33.83 | 34.01 | 34.31 | **35.08** |
| r=0.5 (fixed_mix) | 33.83 | 33.52 | 33.76 | **34.88** |

## 核心结论

1. **Token entropy 不突破 SLV paradox。** r=0 下严格单调下降 (-9.6%)，r=0.5 下严格单调**上升** (+2.4%)。方向完全反转。真实数据注入使预测多样性增加，完全掩盖 collapse 信号。

2. **Stable rank (attn) 不突破 SLV paradox。** r=0 下 -14.0%，r=0.5 下 +3.7%。方向完全反转。

3. **所有测试的替代 EWS 都受同样的 signal attenuation paradox 影响。** 4 个指标方向反转，2 个方向一致但不是 collapse-specific（isotropy 和 FFN stable rank 在 r=0.5 下变化反而更大）。

4. **exp_006 (adaptive) 和 exp_004 (fixed_mix) 结果高度一致**（两种 r=0.5 实现方式给出相同结论），增强了结果可信度。

## Token Entropy 计算方法

Shannon entropy of the **argmax predicted token distribution**: 对 200 个 eval 样本做模型 forward pass → 取 logits argmax → 统计 token 频率 → H = -Σ p(t) log p(t)。这是基于**模型输出 logits 分布**的 entropy（非预先生成文本的 token 频率），衡量模型输出多样性。

---
