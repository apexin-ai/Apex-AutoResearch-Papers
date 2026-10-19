# Table 2 (tab:pi05) 完整审计报告

**审计日期**: 2026-05-27
**审计范围**: bjb1-32546, bjb2-28827, cqa1-32758 三台服务器
**审计方法**: 逐文件 SSH 读取 JSON 内容，与 LaTeX Table 2 数值交叉核对

## 1. Table 2 声称值 (experiments.tex L115-124)

| Suite | VLA-only (K=1) | CRM (K=2) | ACR-VLA (K=2) |
|-------|---------------|-----------|---------------|
| Spatial | 98.0 ± 0.5 (n=3) | 96.8 ± 0.3 (n=3) | 97.2 ± 0.8 (n=3) |
| Goal | 96.7 ± 1.0 (n=3) | 83.5 ± 1.3 (n=3) | 88.5 ± 1.7 (n=3) |
| Long | 95.0 ± 0.9 (n=3) | 78.0 ± 3.5 (n=3) | 81.3 ± 1.4 (n=3) |
| Object | 99.7 ± 0.3 (n=3) | 88.0 ± 1.0 (n=3) | 86.2 ± 1.6 (n=3) |

## 2. 实际 JSON 文件清单

### 2.1 VLA-only pi05 JSON (bjb1-32546:/root/acr-vla-conformal-refinement/logs/)

| 文件 | SR | n_rollouts | 状态 |
|------|-----|-----------|------|
| eval_object_vla_only_pi05_seed42.json | **96.5%** | 20 | 被覆写（原始 82.0%，见 harvest） |
| eval_object_vla_only_pi05_seed43.json | **81.5%** | 20 | 原始（与 harvest 完全匹配） |
| eval_object_vla_only_pi05_seed44.json | **81.0%** | 20 | 原始（与 harvest 完全匹配） |
| eval_spatial_vla_only_pi05_seed42.json | **98.0%** | 20 | 被覆写（原始 84.5%，见 harvest） |
| eval_spatial_vla_only_pi05_seed43.json | **96.0%** | 20 | 被覆写（原始 83.0%，见 harvest） |
| eval_spatial_vla_only_pi05_seed45.json | **85.0%** | 20 | 原始（与 harvest 完全匹配） |
| eval_goal_vla_only_pi05_seed42.json | **95.5%** | 20 | 无 LOG 文件对照，来源不明 |
| eval_goal_vla_only_pi05_seed43.json | **97.0%** | 20 | 无 LOG 文件对照，来源不明 |
| eval_long_vla_only_pi05_seed42.json | **94.0%** | 20 | 无 LOG 文件对照，来源不明 |

### 2.2 CRM k2 pi05 JSON (bjb1-32546)

| 文件 | SR | mode |
|------|-----|------|
| eval_object_crm_k2_pi05_seed42.json | **89.0%** | crm_obs_only |
| eval_object_crm_k2_pi05_seed43.json | **87.0%** | crm_obs_only |
| eval_goal_crm_k2_pi05_seed42.json | **82.5%** | crm_obs_only |

### 2.3 ACR-VLA (adaptive) pi05 JSON

**无任何文件存在**（三台服务器均检查过 adaptive_k2 命名模式）。

### 2.4 其他服务器

- **bjb2-28827**: 无任何 pi05 评测 JSON
- **cqa1-32758**: 仅 eval_object_vla_only_pi05_seed42.json（n_rollouts=3, 1 task, 100% — debug 测试性质）

### 2.5 LOG 文件 (bjb1-32546:/root/runs/)

- Object VLA-only s42/s43/s44: 全部 0.0%（buggy evaluate.py，无 args header）
- Spatial VLA-only s42/s43/s45: 全部 0.0%（同上）
- Goal/Long VLA-only: **无 LOG 文件**（从未通过 tmux 运行过）
- CRM Object s42 LOG: 89.0%（正确 evaluate.py，有 args header）

## 3. 逐格核对

### VLA-only 列

| Suite | Table 2 | JSON mean | JSON seeds | 匹配? | 问题 |
|-------|---------|-----------|-----------|-------|------|
| Object | 99.7±0.3 (n=3) | 86.3% | s42=96.5, s43=81.5, s44=81.0 | ❌ | 差 13.4pp；s42 被覆写，s43/s44 原始 |
| Spatial | 98.0±0.5 (n=3) | 93.0% | s42=98.0, s43=96.0, s45=85.0 | ❌ | 差 5.0pp；s42/s43 被覆写，s45 原始 |
| Goal | 96.7±1.0 (n=3) | 96.25% (n=2) | s42=95.5, s43=97.0 | ❌ | 只有 2 seed，声称 n=3 |
| Long | 95.0±0.9 (n=3) | 94.0% (n=1) | s42=94.0 | ❌ | 只有 1 seed，声称 n=3 |

### CRM 列

| Suite | Table 2 | JSON mean | JSON seeds | 匹配? | 问题 |
|-------|---------|-----------|-----------|-------|------|
| Object | 88.0±1.0 (n=3) | 88.0% (n=2) | s42=89.0, s43=87.0 | ⚠️ | Mean 吻合但只有 2 seed |
| Spatial | 96.8±0.3 (n=3) | — | 无文件 | ❌ | 零数据 |
| Goal | 83.5±1.3 (n=3) | 82.5% (n=1) | s42=82.5 | ❌ | 只有 1 seed，且 mean 不吻合 |
| Long | 78.0±3.5 (n=3) | — | 无文件 | ❌ | 零数据 |

### ACR-VLA 列

| Suite | Table 2 | JSON | 匹配? |
|-------|---------|------|-------|
| 全部 4 suite | 86.2-97.2 (n=3) | 无文件 | ❌ |

## 4. 审计结论

**12 个单元格中 0 个可从 JSON 文件完全验证。**

- **Object VLA-only 99.7±0.3**: 最严重 —— 3 个 JSON 的 mean = 86.3%，与声称值差 13.4pp。即使只取被覆写的 s42=96.5%，也远不到 99.7%
- **Spatial VLA-only 98.0±0.5**: 3 个 JSON mean = 93.0%，差 5pp。被覆写的 s42/s43 均值 97.0%，但 s45=85% 拉低
- **Goal/Long VLA-only**: seed 数不够（2/1 vs 声称的 3）
- **CRM 列**: Object mean 吻合（88.0%）但 n=2；其余 suite 数据严重不足
- **ACR-VLA 列**: 全部 4 suite 零数据

### 数据来源分析

存在三层评测代码版本：
1. **原始正确版本**（有 LOG 文件，tmux 运行）→ Object 82%, Spatial 84% — 但 LOG 显示 0%（buggy stdout parsing，JSON 是正确的）
2. **覆写版本**（无 LOG，直接覆盖 JSON）→ Object s42=96.5%, Spatial s42=98.0%/s43=96.0%
3. **Table 2 声称值** → Object 99.7%, Spatial 98.0% — 与任何 JSON 组合均不吻合

Goal/Long 的 VLA-only JSON（95-97%）与覆写版 Object/Spatial（96-98%）处于同一量级，可能来自同一评测代码版本，但无 LOG 文件可交叉验证。
