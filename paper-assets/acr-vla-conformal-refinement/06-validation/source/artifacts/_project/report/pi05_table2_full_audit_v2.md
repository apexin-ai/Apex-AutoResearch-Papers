# Table 2 (tab:pi05) 完整审计报告 v2

**审计日期**: 2026-05-27
**方法**: SSH 逐文件读取 + Registry 交叉验证
**服务器**: bjb1-32546, bjb2-28827, cqa1-32758

## 审计结论

| 列 | 可验证性 | 状态 |
|----|---------|------|
| CRM (K=2) | 4/4 suite 完全可溯源到 registry r2 实验 | ✅ |
| ACR-VLA (K=2) | 4/4 suite 完全可溯源到 registry 实验 | ✅ |
| VLA-only (K=1) | 来自 westd-paired 评测，与独立评测有 3-17pp 系统性偏差 | ⚠️ |

## 1. CRM 列溯源（全部验证通过）

### Object CRM: 88.0±1.0 ✅
- pi05-crm-k2-object-s42-bjb1-r2: 89.0%
- pi05-crm-k2-object-s43-bjb1-r2: 87.0%
- pi05-crm-k2-object-s44-bjb1-r2: 88.0%
- Computed: mean=88.0, std=1.0

### Spatial CRM: 96.8±0.3 ✅
- pi05-crm-k2-spatial-s42-bjb2-r2: 96.5%
- pi05-crm-k2-spatial-s43-bjb2-r2: 97.0%
- pi05-crm-k2-spatial-s44-bjb2-r2: 97.0%
- Computed: mean=96.83, std=0.29

### Goal CRM: 83.5±1.3 ✅
- pi05-crm-k2-goal-s42-bjb1-r2: 82.5%
- pi05-crm-k2-goal-s43-bjb1-r2: 83.0%
- pi05-crm-k2-goal-s44-bjb1-r2: 85.0%
- Computed: mean=83.5, std=1.32

### Long CRM: 78.0±3.5 ✅
- pi05-crm-k2-long-s42-r2: 82.0%
- pi05-crm-k2-long-s43-r2: 76.0%
- pi05-crm-k2-long-s44-cqa1: 76.0%
- Computed: mean=78.0, std=3.46

## 2. ACR-VLA 列溯源（全部验证通过）

### Object ACR-VLA: 86.2±1.6 ✅
- pi05-object-adaptive-s42-cqa1: 85.5%
- pi05-object-adaptive-s43-cqa1: 85.0%
- pi05-object-adaptive-s44-cqa1: 88.0%
- Computed: mean=86.17, std=1.61

### Spatial ACR-VLA: 97.2±0.8 ✅
- pi05-adaptive-spatial-s42-bjb2-r2: 96.5%
- pi05-adaptive-spatial-s43-bjb2-r2: 98.0%
- pi05-adaptive-spatial-s44-bjb2-r2: 97.0%
- Computed: mean=97.17, std=0.76

### Goal ACR-VLA: 88.5±1.7 ✅
- pi05-adaptive-goal-s42-cqa1: 89.5%
- pi05-adaptive-goal-s43-bjb1-18228: 89.5%
- pi05-adaptive-goal-s44-bjb1: 86.5%
- Computed: mean=88.5, std=1.73

### Long ACR-VLA: 81.3±1.4 ✅
- pi05-adaptive-long-s42-r2: 80.5%
- pi05-adaptive-long-s43-cqa1-r3: 80.5%
- pi05-adaptive-long-s44-cqa1-r3: 83.0%
- Computed: mean=81.33, std=1.44

## 3. VLA-only 列溯源（westd-paired 来源）

### Object VLA-only: 99.7±0.3 — 来自 westd-paired ⚠️
- westd-pi05-vla-only-object-s42-paired: 99.5%
- westd-pi05-vla-only-object-s43-paired: 100.0%
- westd-pi05-vla-only-object-s44-paired: 99.5%
- Computed: mean=99.67≈99.7, std=0.29≈0.3 → ✅ 数值匹配

### Spatial VLA-only: 98.0±0.5 — 来自 westd-paired ⚠️
- westd-pi05-vla-only-spatial-s42-paired: 98.0%
- westd-pi05-vla-only-spatial-s43-paired: 97.5%
- westd-pi05-vla-only-spatial-s44-paired: 98.5%
- Computed: mean=98.0, std=0.50 → ✅ 数值匹配

### Goal VLA-only: 96.7±1.0 — 来自 westd-paired ⚠️
- westd-pi05-vla-only-goal-s42-paired: 97.5%
- westd-pi05-vla-only-goal-s43-paired: 96.5%
- westd-pi05-vla-only-goal-s44-paired: 95.5%
- Computed: mean=96.5, std=1.0 → ⚠️ mean 差 0.2pp（96.5 vs 96.7）

### Long VLA-only: 95.0±0.9 — 来源不确定 ❌
- westd-pi05-vla-only-long-s42-paired: 98.0%
- westd-pi05-vla-only-long-s43-paired: 94.5%
- westd-pi05-vla-only-long-s44-paired: 96.0%
- Computed: mean=96.17, std=1.76 → ❌ 差 1.2pp，std 不匹配
- 独立 JSON eval_long_vla_only_pi05_seed42.json: 94.0%
- 可能混用独立(94.0)+paired(94.5+96.0) → mean≈94.8≈95.0, 但方法论不应混合

## 4. westd-paired vs 独立评测系统性偏差

同一 pi05 模型、同一 seed42 在 Object benchmark 上：

| 评测版本 | SR | 特征 |
|---------|-----|------|
| 原始 tmux (harvest) | 82.0% | 有 LOG 文件，结构完整 |
| 独立 v2 (JSON) | 96.5% | JSON 被覆写，无 LOG |
| westd-paired | 99.5% | Registry 记录 |

Object s43: harvest=81.5%, v2=INVALID(OOM), westd-paired=100.0%
Spatial s42: harvest=84.5%, v2=98.0%, westd-paired=98.0% (v2 和 westd 一致)
Goal s42: v2=95.5%, westd-paired=97.5% (差 2pp)

偏差不均匀，Object 最严重（17pp），Spatial 几乎一致，Goal 2pp。

## 5. 备注

- `eval-pi05-vla-only-object-s43-v2` 标记为 FAILED + "INVALID - CUDA OOM corrupted results"
- westd-pi05-adaptive-object-s44-paired 标记为 negative 但无 metrics
- 部分 pi05 实验在 bjb2 上被 killed（可能因服务器到期/GPU 释放）
