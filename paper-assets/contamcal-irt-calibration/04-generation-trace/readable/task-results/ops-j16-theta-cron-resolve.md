# ops j16 theta cron resolve

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j16_theta_cron_resolve_20260517T151239_result.json`
- **Structured JSON:** [`a862793fdcf84c39b80b.json`](../../sessions/a8/a862793fdcf84c39b80b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态判断: PARTIAL SUCCESS

**原因**: 
- 第一轮运行（旧代码，无 theta 提取）：8/8 domain fitting 完成，但 pooled 阶段 crash（"Operation not permitted"，Stan sampler 在 /tmp 写入权限问题）
- 第二轮运行（新代码，含 theta 提取）：仅完成 3/8 domain（STEM_Math, STEM_Science, STEM_CS_Eng）后停止，无残留进程

**实际输出目录**: `/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/`（非任务中假设的路径）

---

## γ 结果（全 8 domain，来自第一轮 log）

| Domain | γ mean | 95% CI | Rhat | ESS | Div |
|--------|--------|--------|------|-----|-----|
| STEM_Math | -0.386 | [-0.999, 0.200] | 1.009 | 1448 | 0 |
| STEM_Science | 0.042 | [-0.535, 0.633] | 1.008 | 1444 | 0 |
| STEM_CS_Eng | 0.362 | [-0.443, 1.184] | 1.006 | 1615 | 0 |
| Medical | 0.218 | [-0.336, 0.738] | 1.010 | 1560 | 0 |
| Humanities | **-0.947** | [-1.430, -0.488] | 1.008 | 1477 | 0 |
| Social_Sciences | **-1.092** | [-1.497, -0.674] | 1.008 | 1338 | 0 |
| Business_Law | -0.239 | [-0.676, 0.203] | 1.007 | 1353 | 0 |
| Other | **-0.880** | [-1.549, -0.233] | 1.008 | 1331 | 0 |

---

## θ 结果（仅 3 个 STEM domain 有 theta）

Model order (J=16):

| Idx | Model | Family | Scale | Dosage |
|-----|-------|--------|-------|--------|
| 0 | Qwen2.5-1.5B_d000_s123 | Qwen | 1.5B | 0 |
| 1 | Qwen2.5-1.5B_d000_s42 | Qwen | 1.5B | 0 |
| 2 | Qwen2.5-1.5B_d005_s123 | Qwen | 1.5B | 5 |
| 3 | Qwen2.5-1.5B_d005_s42 | Qwen | 1.5B | 5 |
| 4 | Qwen2.5-1.5B_d025_s123 | Qwen | 1.5B | 25 |
| 5 | Qwen2.5-1.5B_d025_s42 | Qwen | 1.5B | 25 |
| 6 | Qwen2.5-1.5B_d100_s123 | Qwen | 1.5B | 100 |
| 7 | Qwen2.5-1.5B_d100_s42 | Qwen | 1.5B | 100 |
| 8 | Llama-3.2-3B_d000_s42 | **Llama** | 3B | 0 |
| 9 | Llama-3.2-3B_d005_s42 | **Llama** | 3B | 5 |
| 10 | Llama-3.2-3B_d025_s42 | **Llama** | 3B | 25 |
| 11 | Qwen2.5-3B_d005_s123 | Qwen | 3B | 5 |
| 12 | Qwen2.5-3B_d025_s123 | Qwen | 3B | 25 |
| 13 | Qwen2.5-3B_d025_v3_s42 | Qwen | 3B | 25 |
| 14 | Qwen2.5-3B_d100_a32_s123 | Qwen | 3B | 100 |
| 15 | Qwen2.5-3B_d100_a32_s42 | Qwen | 3B | 100 |

### θ per domain (posterior mean ± sd)

**STEM_Math** (PPP=0.998):
| Model | θ mean | θ sd |
|-------|--------|------|
| Qwen-1.5B_d000_s123 | -0.361 | 0.066 |
| Qwen-1.5B_d000_s42 | -0.409 | 0.067 |
| Qwen-1.5B_d005_s123 | -0.437 | 0.067 |
| Qwen-1.5B_d005_s42 | -0.466 | 0.066 |
| Qwen-1.5B_d025_s123 | -0.438 | 0.068 |
| Qwen-1.5B_d025_s42 | -0.507 | 0.066 |
| Qwen-1.5B_d100_s123 | -0.376 | 0.068 |
| Qwen-1.5B_d100_s42 | -0.474 | 0.066 |
| **Llama-3B_d000_s42** | **-1.464** | 0.067 |
| **Llama-3B_d005_s42** | **-1.641** | 0.070 |
| **Llama-3B_d025_s42** | **-1.742** | 0.072 |
| Qwen-3B_d005_s123 | 0.031 | 0.071 |
| Qwen-3B_d025_s123 | 0.098 | 0.070 |
| Qwen-3B_d025_v3_s42 | -0.160 | 0.071 |
| Qwen-3B_d100_a32_s123 | 0.050 | 0.071 |
| Qwen-3B_d100_a32_s42 | 0.061 | 0.069 |

**STEM_Science** (PPP=0.981):
| Model | θ mean | θ sd |
|-------|--------|------|
| Qwen-1.5B_d000_s123 | 0.376 | 0.064 |
| Qwen-1.5B_d000_s42 | 0.406 | 0.063 |
| Qwen-1.5B_d005_s123 | 0.444 | 0.065 |
| Qwen-1.5B_d005_s42 | 0.361 | 0.063 |
| Qwen-1.5B_d025_s123 | 0.406 | 0.063 |
| Qwen-1.5B_d025_s42 | 0.424 | 0.062 |
| Qwen-1.5B_d100_s123 | 0.462 | 0.065 |
| Qwen-1.5B_d100_s42 | 0.391 | 0.063 |
| **Llama-3B_d000_s42** | **-0.766** | 0.058 |
| **Llama-3B_d005_s42** | **-0.952** | 0.058 |
| **Llama-3B_d025_s42** | **-0.981** | 0.057 |
| Qwen-3B_d005_s123 | 0.700 | 0.068 |
| Qwen-3B_d025_s123 | 0.751 | 0.067 |
| Qwen-3B_d025_v3_s42 | 0.573 | 0.069 |
| Qwen-3B_d100_a32_s123 | 0.721 | 0.068 |
| Qwen-3B_d100_a32_s42 | 0.693 | 0.068 |

**STEM_CS_Eng** (PPP=0.893):
| Model | θ mean | θ sd |
|-------|--------|------|
| Qwen-1.5B_d000_s123 | 0.431 | 0.102 |
| Qwen-1.5B_d000_s42 | 0.441 | 0.102 |
| Qwen-1.5B_d005_s123 | 0.513 | 0.107 |
| Qwen-1.5B_d005_s42 | 0.496 | 0.104 |
| Qwen-1.5B_d025_s123 | 0.414 | 0.100 |
| Qwen-1.5B_d025_s42 | 0.390 | 0.103 |
| Qwen-1.5B_d100_s123 | 0.506 | 0.108 |
| Qwen-1.5B_d100_s42 | 0.382 | 0.105 |
| **Llama-3B_d000_s42** | **-0.682** | 0.089 |
| **Llama-3B_d005_s42** | **-0.760** | 0.089 |
| **Llama-3B_d025_s42** | **-0.955** | 0.092 |
| Qwen-3B_d005_s123 | 0.468 | 0.102 |
| Qwen-3B_d025_s123 | 0.443 | 0.105 |
| Qwen-3B_d025_v3_s42 | 0.353 | 0.108 |
| Qwen-3B_d100_a32_s123 | 0.482 | 0.107 |
| Qwen-3B_d100_a32_s42 | 0.546 | 0.108 |

---

## Qwen-3B vs Llama-3B 同 dosage θ 对比

| Domain | Dosage | Qwen-3B θ | Llama-3B θ | Δ(Qwen-Llama) |
|--------|--------|-----------|-----------|----------------|
| STEM_Math | d005 | +0.031 | -1.641 | **+1.67** |
| STEM_Math | d025 | +0.098 / -0.160 | -1.742 | **+1.84 / +1.58** |
| STEM_Science | d005 | +0.700 | -0.952 | **+1.65** |
| STEM_Science | d025 | +0.751 / +0.573 | -0.981 | **+1.73 / +1.55** |
| STEM_CS_Eng | d005 | +0.468 | -0.760 | **+1.23** |
| STEM_CS_Eng | d025 | +0.443 / +0.353 | -0.955 | **+1.40 / +1.31** |

Llama-3B 在所有 STEM domain 上 θ 显著低于 Qwen-3B（差距 1.2-1.8），且 Llama θ 随 dosage 增加而下降（d000→d025 持续降低），而 Qwen-3B 各 dosage 间 θ 基本稳定。

---

## 待处理

需要重跑剩余 5 个 domain（Medical, Humanities, Social_Sciences, Business_Law, Other）的 theta extraction。可选方案：
1. 用 `--domains Medical Humanities Social_Sciences Business_Law Other --skip-pooled` 只补跑缺失 domain
2. 或用 `extract_theta_no05b.py`（exp006 目录下已存在此脚本）从已有 Stan 输出中提取

---
