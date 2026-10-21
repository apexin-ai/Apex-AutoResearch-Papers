# ops j16 theta cron check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j16_theta_cron_check_20260517T151143_result.json`
- **Structured JSON:** [`7e617a092899b3639959.json`](../../sessions/7e/7e617a092899b3639959.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态: 部分成功

**PID 4670 已退出（失败）**。8 个 domain fits 全部完成，但 pooled fit 在 sampling 60% 时因 "Operation not permitted" 崩溃（CmdStan 4 chains 同时 retcode=1）。随后有第二次部分重跑（22:41-22:53）为前 3 个 domain 添加了 theta，但后 5 个 domain 仍缺 theta。

---

## θ per model (posterior mean) — 仅 3 个有 theta 的 domain

| j | Model | Family | Scale | Dosage | STEM_Math | STEM_Science | STEM_CS_Eng |
|---|-------|--------|-------|--------|-----------|--------------|-------------|
| 0 | Qwen2.5-1.5B_d000_s123 | Qwen | 1.5B | 0 | -0.361 | +0.376 | +0.431 |
| 1 | Qwen2.5-1.5B_d000_s42 | Qwen | 1.5B | 0 | -0.409 | +0.406 | +0.441 |
| 2 | Qwen2.5-1.5B_d005_s123 | Qwen | 1.5B | 5 | -0.437 | +0.444 | +0.513 |
| 3 | Qwen2.5-1.5B_d005_s42 | Qwen | 1.5B | 5 | -0.466 | +0.361 | +0.496 |
| 4 | Qwen2.5-1.5B_d025_s123 | Qwen | 1.5B | 25 | -0.438 | +0.406 | +0.414 |
| 5 | Qwen2.5-1.5B_d025_s42 | Qwen | 1.5B | 25 | -0.507 | +0.424 | +0.390 |
| 6 | Qwen2.5-1.5B_d100_s123 | Qwen | 1.5B | 100 | -0.376 | +0.462 | +0.506 |
| 7 | Qwen2.5-1.5B_d100_s42 | Qwen | 1.5B | 100 | -0.474 | +0.391 | +0.382 |
| 8 | **Llama-3.2-3B_d000_s42** | Llama | 3B | 0 | **-1.464** | **-0.766** | **-0.682** |
| 9 | **Llama-3.2-3B_d005_s42** | Llama | 3B | 5 | **-1.641** | **-0.952** | **-0.760** |
| 10 | **Llama-3.2-3B_d025_s42** | Llama | 3B | 25 | **-1.742** | **-0.981** | **-0.955** |
| 11 | Qwen2.5-3B_d005_s123 | Qwen | 3B | 5 | +0.031 | +0.700 | +0.468 |
| 12 | Qwen2.5-3B_d025_s123 | Qwen | 3B | 25 | +0.098 | +0.751 | +0.443 |
| 13 | Qwen2.5-3B_d025_v3_s42 | Qwen | 3B | 25 | -0.160 | +0.573 | +0.353 |
| 14 | Qwen2.5-3B_d100_a32_s123 | Qwen | 3B | 100 | +0.050 | +0.721 | +0.482 |
| 15 | Qwen2.5-3B_d100_a32_s42 | Qwen | 3B | 100 | +0.061 | +0.693 | +0.546 |

---

## Qwen-3B vs Llama-3B θ 差异（同 dosage）

| Domain | Dosage | Qwen-3B θ | Llama-3B θ | Δ(Q-L) |
|--------|--------|-----------|-----------|--------|
| STEM_Math | d005 | +0.031 | -1.641 | **+1.672** |
| STEM_Math | d025 | +0.098 | -1.742 | **+1.839** |
| STEM_Science | d005 | +0.700 | -0.952 | **+1.652** |
| STEM_Science | d025 | +0.751 | -0.981 | **+1.732** |
| STEM_CS_Eng | d005 | +0.468 | -0.760 | **+1.228** |
| STEM_CS_Eng | d025 | +0.443 | -0.955 | **+1.398** |

---

## Gamma summary (全 8 domains)

| Domain | γ mean | 95% CI | PPP | n_items |
|--------|--------|--------|-----|---------|
| STEM_Math | -0.386 | [-1.00, +0.20] | 0.998 | 1190 |
| STEM_Science | +0.042 | [-0.53, +0.63] | 0.981 | 1397 |
| STEM_CS_Eng | +0.362 | [-0.44, +1.18] | 0.892 | 557 |
| Medical | +0.218 | [-0.34, +0.74] | 0.827 | 1640 |
| Humanities | **-0.947** | [-1.43, -0.49] | 1.000 | 2000 |
| Social_Sciences | **-1.092** | [-1.50, -0.67] | 1.000 | 2000 |
| Business_Law | -0.239 | [-0.68, +0.20] | 0.978 | 2000 |
| Other | **-0.880** | [-1.55, -0.23] | 0.982 | 883 |

---

## 关键发现

1. **Llama-3B 的 θ 远低于 Qwen-3B**（差 1.2-1.8 个标准差），说明在联合 IRT 下 Llama 基础能力显著弱于 Qwen-3B
2. **Llama θ 随 dosage 递减**（d000→d005→d025），与 Qwen-3B 的平坦趋势形成对比——暗示 Llama 在 contaminated items 上的表现提升未被 IRT 能力参数捕获（被 γ 吸收）
3. **5 个 domain 缺 theta**——需要重跑带 `--skip-pooled` 的脚本补齐 Medical/Humanities/Social_Sciences/Business_Law/Other 的 theta
4. **Pooled fit 失败原因**: CmdStan "Operation not permitted"——可能是容器安全策略限制了 /tmp 中的进程 fork 或文件操作

---
