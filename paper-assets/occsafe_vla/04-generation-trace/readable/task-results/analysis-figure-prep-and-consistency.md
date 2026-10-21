# analysis figure prep and consistency

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_figure_prep_and_consistency_20260525T082701_result.json`
- **Structured JSON:** [`773ea5deb09ecd92912f.json`](../../sessions/77/773ea5deb09ecd92912f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在汇总三部分结果。

---

## Part 1: 数据一致性检查

**结论：无风险。** 两台服务器上不存在 factorial 2×2 bar chart 脚本或任何包含硬编码 CAR 值的图表生成代码。搜索范围：
- `find` 全路径搜索 `*factorial*`, `*2x2*`, `*bar*` → 无匹配
- `grep "0.797"` 在所有 `.py` 分析脚本中 → 无匹配
- 无 LaTeX 文件存在

现有的 CKA/gradient dose-response 脚本引用 `full_occ_retrain_s0` checkpoint，但仅用于机制分析（CKA similarity、gradient norms），不涉及 CAR 值。**factorial 2×2 图表尚未生成。**

后续创建时须确保使用原始 3-seed 数据（Full OCC BN mean=0.797），而非 retrain_s0 数据。

---

## Part 2: Dose-Response 图表模板

已创建并生成：
- **脚本**: `/root/autodl-tmp/analysis/dose_response_figure.py`
- **输出**: `/root/autodl-tmp/analysis/dose_response_car.pdf` + `.png`
- **副本**: `/root/occsafe_vla/artifacts/dose_response_car.png`

特性：
- 主曲线：Forward cutoff (15K→25K→35K→45K→50K/Full) 含 SE error band
- Reverse cutoff 单独标注为菱形（◇），偏移放置避免混入主趋势线
- Vanilla baseline 水平虚线
- 实心圆 = 3-seed 完成，空心圆 = 待补 seed（标 `n=2` 或 `n=1`）
- 15K→Vanilla gap 标注 `+0.2%`
- 底部注释 "Open markers: 3rd seed pending"
- 300 DPI PDF + PNG，DejaVu Sans 字体，色盲友好配色

---

## Part 3: 现有 Figures 清单

### `/root/autodl-tmp/analysis/` (westd-10894)

| 文件 | 修改时间 | 分析类型 |
|------|---------|---------|
| `cka_random_occ/cka_analysis.pdf` | 05-24 13:33 | CKA vs pretrained (Random OCC) |
| `cka_detach_ln/cka_analysis.pdf` | 05-24 16:37 | CKA vs pretrained (Detach+LN) |
| `cka_full_occ_ln/cka_analysis.pdf` | 05-25 09:47 | CKA vs pretrained (Full OCC LN, s0) |
| `cka_full_occ_ln_s1/cka_analysis.pdf` | 05-25 10:31 | CKA vs pretrained (Full OCC LN, s1) |
| `cka_full_occ_ln_s2/cka_analysis.pdf` | 05-25 11:15 | CKA vs pretrained (Full OCC LN, s2) |
| `cka_same_seed/cka_analysis.pdf` | 05-25 13:03 | CKA 4-condition same-seed 对比 |
| `cka_dose_response/cka_dose_response.pdf` | 05-25 14:00 | CKA dose-response (per-layer) |
| `gradient_same_seed/gradient_summary.pdf` | 05-25 11:28 | Gradient 4-condition summary (6-panel) |
| `gradient_same_seed/gradient_analysis.pdf` | 05-25 11:28 | Gradient analysis (合并版) |
| `gradient_same_seed/action_gradient_norms.pdf` | 05-25 11:28 | Per-layer action gradient norms |
| `gradient_same_seed/occ_gradient_norms.pdf` | 05-25 11:28 | Per-layer aux gradient norms |
| `gradient_same_seed/gradient_amplification.pdf` | 05-25 11:28 | Full/Detach amplification ratio |
| `gradient_same_seed/cosine_similarity.pdf` | 05-25 11:28 | Action↔Aux cosine similarity |
| `gradient_same_seed/conflict_rate.pdf` | 05-25 11:28 | Gradient conflict rate |
| `gradient_same_seed/bn_drift.pdf` | 05-25 11:28 | BN running stats drift |
| `gradient_dose_response_s0/gradient_dose_response.pdf` | 05-25 15:48 | Gradient dose-response (all conditions, s0) |
| **`dose_response_car.pdf`** | **05-25 16:30** | **CAR dose-response (新建)** |

### `/root/occsafe_vla/analysis/results/` (westd-10894)

| 文件 | 修改时间 | 分析类型 |
|------|---------|---------|
| `random_occ_s2_dryrun_gradient_analysis.pdf` | 05-23 12:09 | Random OCC s2 dryrun gradient |
| `random_occ_s2_gradient_analysis.pdf` | 05-23 12:13 | Random OCC s2 gradient |
| `detach_s2_gradient_analysis.pdf` | 05-23 12:14 | Detach s2 gradient |
| `gradient_comparison.pdf` | 05-23 12:15 | Multi-condition gradient comparison |

### `/root/occsafe_vla/artifacts/` (westd-10894)

10 张 BEV 可视化 demo (`bev_*.png`) + 新增 `dose_response_car.png`

### westd-34685

无 figure 文件（仅用于训练和 eval，分析产出在 10894）。

---
