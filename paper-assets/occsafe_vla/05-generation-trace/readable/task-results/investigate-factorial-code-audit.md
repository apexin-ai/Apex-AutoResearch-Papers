# investigate factorial code audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_factorial_code_audit_20260525T121748_result.json`
- **Structured JSON:** [`a531cc4cbac2a8466ee7.json`](../../sessions/a5/a531cc4cbac2a8466ee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整审计结果。

---

## 2×2 Factorial 代码版本审计报告

### 完整表格

| exp_id | 服务器 | 日志文件 | 训练开始 | `[OCC]` | `[AUX]` | 代码版本 | 数据可信度 |
|--------|--------|---------|---------|---------|---------|---------|-----------|
| **Cell 1: Grad ON + BN** | | | | | | | |
| mvp_occ_s0 (原始) | westd-34685 | `checkpoints/occ_s0_train.log` | May 21 00:35 | 451 | 0 | **v1** | 可用 |
| occ_s1_fresh | westd-34685 | `runs/.../occ_s1_fresh.log` | May 21 22:50 | 501 | 0 | **v1** | 可用 |
| mvp_occ_s2 (原始) | westd-34685 | `checkpoints/occ_s2_train.log` | May 21 00:36 | 451 | 0 | **v1** | 可用 |
| **Cell 2: Grad ON + LN** | | | | | | | |
| full_occ_ln_s0 | westd-10894 | `runs/.../full_occ_ln_s0.log` | May 24 17:00 | 0 | 501 | **v2** | 可用 |
| full_occ_ln_s1 | westd-10894 | `full_occ_ln_s1.log` + `_resume.log` | May 24 17:00 | 0 | 301+301 | **v2** | 可用 |
| full_occ_ln_s2 | westd-10894 | `full_occ_ln_s2.log` + `_resume.log` | May 24 17:00 | 0 | 301+301 | **v2** | 可用 |
| **Cell 3: Grad OFF + BN (Detach BN)** | | | | | | | |
| ablation_occ_detach_s0 | westd-10894 | `runs/.../ablation_occ_detach_s0.log` | May 21 19:02 | 0 | 0 | **v1** | **存疑** |
| ablation_occ_detach_s1 | westd-10894 | `runs/.../ablation_occ_detach_s1.log` | May 21 19:02 | 0 | 0 | **v1** | **存疑** |
| ablation_occ_detach_s2 | westd-10894 | `runs/.../ablation_occ_detach_s2.log` | May 22 14:12 | 0 | 0 | **v1** | **存疑** |
| **Cell 4: Grad OFF + LN (Detach LN)** | | | | | | | |
| detach_ln_s0 | westd-10894 | `runs/.../detach_ln_s0.log` | May 24 01:10 | 0 | 501 | **v2** | 可用 |
| detach_ln_s1 | westd-10894 | `runs/.../detach_ln_s1.log` | May 24 01:11 | 0 | 501 | **v2** | 可用 |
| detach_ln_s2 | westd-10894 | `runs/.../detach_ln_s2.log` | May 24 01:11 | 0 | 501 | **v2** | 可用 |

### Retrain 版本（参考）
| full_occ_retrain_s0 | westd-34685 | May 23 11:48 | 0 | 501 | **v2** |
| ablation_occ_detach_s0_retrain | westd-10894 | May 24 17:06 | 0 | 301 | **v2** |

---

### 核心发现：代码版本与归一化类型完全混淆

```
              BN          LN
Grad ON    v1 (Cell1)   v2 (Cell2)
Grad OFF   v1 (Cell3)   v2 (Cell4)
```

**所有 BN 实验 = v1 代码**（May 20-22），**所有 LN 实验 = v2 代码**（May 24+）。代码版本与归一化类型完美共线——无法分离。

### 具体问题

1. **Cell 3 (Detach BN/v1) 无任何辅助损失日志**：0 个 `[OCC]` 行、0 个 `[AUX]` 行。v1 的 detach 代码路径完全跳过了损失记录。这意味着 detach 的实际行为无法从日志验证——可能 detach 根本没有正确实施。

2. **Cell 1 (Full BN/v1) 使用 `[OCC]` 标签**（无 depth_loss 字段），Cell 2/4 (v2) 使用 `[AUX]` 标签（含 depth_loss 字段）。v2 代码结构明显不同。

3. **occ_s1_train 原始训练不完整**：仅 276 个 `[OCC]`（~1.8MB log vs 正常 ~3.1MB），s1_fresh 作为替代完成了完整训练（501 个 `[OCC]`）。

### 对 2×2 Factorial 的影响

**交互效应 (p=0.025) 不可信。** 该交互可能反映的是 v1→v2 代码差异（不同的损失函数、logging、DepthHead、detach 实现方式），而非 BN vs LN 的真实交互效应。

要获得有效的 2×2 factorial，需要在**同一代码版本**下重新训练 BN 实验（Cell 1 和 Cell 3），或者在 v1 代码下训练 LN 实验。鉴于 v2 代码更成熟且包含正确的 detach 实现，建议用 v2 代码重新训练 Cell 1 (Full BN) 和 Cell 3 (Detach BN)。

---
