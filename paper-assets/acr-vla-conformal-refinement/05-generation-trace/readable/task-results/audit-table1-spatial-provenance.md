# audit table1 spatial provenance

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-spatial-provenance_20260525T015026_result.json`
- **Structured JSON:** [`2d787a6806b5f5547833.json`](../../sessions/2d/2d787a6806b5f5547833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Let me compile the comprehensive audit report.

---

# Table 1 Spatial Suite — Full Provenance Audit

## [Spatial] [CRM] seeds=[42,43,44] → 79.8±1.3 ✅

All on **bjb1-32546**, registry-confirmed `three_seed_summary`.

| Seed | SR | Successes | File | n_rollouts | baseline_mode | mode | mtime (UTC) | Birth=Modify? |
|------|----|-----------|------|------------|---------------|------|-------------|---------------|
| s42 | 80.0% | 160/200 | `eval_spatial_crm_obs_only_norm0.05_seed42.json` | 20 ✓ | single ✓ | crm_obs_only ✓ | 2026-05-23 03:10 | ✅ 未覆写 |
| s43 | 81.0% | 162/200 | `eval_spatial_crm_obs_only_norm0.05_seed43.json` | 20 ✓ | single ✓ | crm_obs_only ✓ | 2026-05-23 08:28 | ✅ 未覆写 |
| s44 | 78.5% | 157/200 | `eval_spatial_crm_obs_only_norm0.05_seed44.json` | 20 ✓ | single ✓ | crm_obs_only ✓ | 2026-05-23 08:48 | ✅ 未覆写 |

**重算:** mean=(80+81+78.5)/3=**79.83%**, std=**1.26%** → Table 1 报告: 79.8±1.3% ✅ (std 四舍五入 1.26→1.3)

---

## [Spatial] [Adaptive] seeds=[42,43,44] → 80.8±1.1 ⚠️ 文件覆写问题

All on **bjb1-32546**. Registry experiments: `eval-supp-adapt-tau025-spatial-s42-r2`, `-s43`, `-s44`.

| Seed | Registry SR | JSON SR | File | n_rollouts | baseline_mode | mtime (UTC) | Birth vs Modify |
|------|------------|---------|------|------------|---------------|-------------|-----------------|
| s42 | **82.0%** (164/200) | **79.5%** (159/200) | `..._tau0.25_seed42.json` | 20 ✓ | single ✓ | 2026-05-24 17:09 | **⚠️ 已覆写** Birth=05-23 06:06, Modify=05-24 17:09 |
| s43 | 80.0% (160/200) | 80.0% ✓ | `..._tau0.25_seed43.json` | 20 ✓ | single ✓ | 2026-05-23 08:28 | ✅ Birth=Modify |
| s44 | 80.5% (161/200) | 80.5% ✓ | `..._tau0.25_seed44.json` | 20 ✓ | single ✓ | 2026-05-23 08:36 | ✅ Birth=Modify |

**⚠️ 关键问题：s42 文件被τ-sweep覆写。**
- 原始实验 (eval-supp-adapt-tau025-spatial-s42-r2) 于 2026-05-23 06:12 完成，SR=82%
- 文件于 2026-05-24 17:09 被后续τ-sweep实验覆写，当前SR=79.5%
- **Registry 值 (82%) 与当前 JSON 文件值 (79.5%) 不一致**
- **Table 1 使用的是 registry 值 82%，无法从文件系统验证**

**重算 (用 registry 值):** mean=(82+80+80.5)/3=**80.83%**, std=**1.04%** → Table 1 报告: 80.8±1.1%
- mean 匹配 ✅
- **std 不精确**: 计算值 1.04，报告值 1.1 (向上取整，差异 0.06pp) ⚠️

---

## [Spatial] [VLA-only] seeds=[42,43,44] → 78.7±0.3 🔴 无法追溯

| Seed | Registry exp_id | Registry SR | JSON 所在服务器 | JSON SR | 问题 |
|------|----------------|-------------|----------------|---------|------|
| s42 | eval-supp-spatial-vla-only-s42 | 80.0% | bjb1-18228 | 80.0% | 🔴 **model=pi05 元数据** (应为 SmolVLA) |
| s42 | eval-supp-spatial-vla-only-smolvla-s42 | FAILED | cqa1-32758 | 78.5% | 🔴 **Registry 标记为 failed，但文件完整 (200 rollouts)** |
| s43 | eval-supp-spatial-vla-only-s43 | 79.0% | cqa1-32758 | 79.0% ✓ | ✅ |
| s44 | eval-supp-spatial-vla-only-s44 | 78.5% | bjb2-40593 | 78.5% ✓ | ✅ |

**数学验证 Table 1 使用了哪些值:**

| 候选组合 | Mean | Std | 匹配 78.7±0.3? |
|----------|------|-----|----------------|
| bjb1-18228 s42=80.0, cqa1 s43=79.0, bjb2-40593 s44=78.5 | 79.17 | 0.76 | ❌ |
| cqa1 s42=78.5, cqa1 s43=79.0, bjb2-40593 s44=78.5 | **78.67** | **0.29** | ✅ |

**结论: Table 1 VLA-only 使用了 cqa1 的 s42=78.5%**，但该实验在 registry 中标记为 **FAILED**。

### 额外问题

1. **跨服务器数据**: 同一 seed 在不同服务器产生不同 SR:
   - s42: bjb1-18228=80.0%, cqa1=78.5% (Δ=1.5pp)
   - s43: cqa1=79.0%, bjb2-28827=80.5% (Δ=1.5pp)
   - s44: bjb2-40593=78.5%, bjb2-28827=80.5% (Δ=2.0pp)

2. **Model 疑虑**: eval-supp-spatial-vla-only-s42 在 bjb1-18228 的 registry metadata 显示 model=pi05，wall_clock=3.14h（pi05 典型值，SmolVLA 约 30min）。8-seed 表使用了此值 (80.0%)，可能存在模型混淆。

3. **bjb2-28827 无 registry 记录的文件**: 该服务器存在 `eval_spatial_vla_only_seed43.json` (SR=80.5%) 和 `eval_spatial_vla_only_seed44.json` (SR=80.5%)，n_rollouts=20，但在 registry 中找不到对应实验。来源不明。

---

## 总结

| 方法 | Table 1 值 | 重算值 | 文件可追溯? | 严重问题 |
|------|-----------|--------|------------|----------|
| CRM | 79.8±1.3 | 79.8±1.3 | ✅ 全部匹配 | 无 |
| Adaptive | 80.8±1.1 | 80.8±1.0 | ⚠️ s42文件被覆写 | s42 JSON 当前内容≠registry; std 1.0→1.1 |
| VLA-only | 78.7±0.3 | 78.7±0.3 | 🔴 s42 来自 failed 实验 | s42 来源不清; 8-seed 表切换到 pi05 model 的 s42=80% |

### 建议处理

1. **Adaptive s42**: 需要重跑 `--mode adaptive_conformal_crm --conformal_threshold 0.25 --seed 42 --n_rollouts 20` 以恢复被覆写的数据
2. **VLA-only s42**: 需要在同一服务器用 SmolVLA (非 pi05) 重跑 seed 42 的 baseline，解决 model 混淆
3. **8-seed 表已存在**，建议直接使用 8-seed 数据（但需先解决 s42 model 问题）

---
