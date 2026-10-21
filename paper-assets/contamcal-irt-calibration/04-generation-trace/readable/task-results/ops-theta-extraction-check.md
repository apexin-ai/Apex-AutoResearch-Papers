# ops theta extraction check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_theta_extraction_check_20260517T095906_result.json`
- **Structured JSON:** [`2d711243d737f7a90168.json`](../../sessions/2d/2d711243d737f7a90168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验成功完成，registry 已更新。结果汇总：

## θ 提取结果 (J=13, 2PL+γ, 排除 0.5B)

**模型**: 1.5B (θ_1–8), 3B (θ_9–13)

| Domain | θ_1.5B_mean | θ_3B_mean | Δθ | 95% CI |
|--------|------------|----------|------|--------|
| STEM_Math | -0.5320 | 0.1193 | **0.6513** | [0.5704, 0.7314] |
| STEM_Science | 0.3210 | 0.7803 | **0.4593** | [0.3702, 0.5462] |
| STEM_CS_Eng | 0.3724 | 0.5415 | **0.1691** | [0.0300, 0.3037] |
| Medical | 0.5214 | 1.0528 | **0.5314** | [0.4521, 0.6091] |
| Humanities | 0.2278 | 0.4959 | **0.2680** | [0.2018, 0.3367] |
| Social_Sciences | 0.9403 | 1.5398 | **0.5994** | [0.5233, 0.6746] |
| Business_Law | 0.0825 | 0.4169 | **0.3344** | [0.2614, 0.4102] |
| Other | 0.8168 | 1.5652 | **0.7483** | [0.6465, 0.8456] |
| **pooled** | **0.3109** | **0.8111** | **0.5002** | [0.4312, 0.5683] |

**关键观察**:
- 所有 9 个域的 Δθ 95% CI 均不含 0，1.5B 和 3B 在所有域上能力显著分离
- Δθ 范围：0.17 (STEM_CS_Eng) 到 0.75 (Other)
- STEM_CS_Eng 分离最小（CI 下界仅 0.03），其余域分离稳健
- γ (contamination) 在 STEM_CS_Eng 最高 (0.68)，Social_Sciences 最低 (-0.49)
- 总 fit 时间 ≈ 55 分钟

---
