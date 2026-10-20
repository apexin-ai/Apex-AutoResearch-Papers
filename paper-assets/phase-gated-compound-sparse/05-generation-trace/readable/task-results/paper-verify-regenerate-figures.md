# paper verify regenerate figures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_verify-regenerate-figures_20260514T102449_result.json`
- **Structured JSON:** [`d4d17074c7a52be86157.json`](../../sessions/d4/d4d17074c7a52be86157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

所有 5 个图表已从 bf16 canonical 数据重新生成，输出至 `/root/autodl-tmp/pacs/paper_figures/`。

### 各图状态

| 图表 | 状态 | 关键数值确认 |
|------|------|-------------|
| **Fig 1** (dose_response) | 重新生成 | G_imp 6-point: [5.6, 69.2, 103.1, 222.4, 274.2, 273.6]; G_rand: [1.1, 0.95, 1.67, 1.61] |
| **Fig 3** (crossover) | 重新生成 | imp_high=0.032, rand_high=0.818; imp_low=7.196, rand_low=1.363 |
| **Fig 4** (forest) | 重新生成 | DS d_z: 0.44/0.52/0.68/0.80; QW d_z: 0.28/0.55/0.89/1.02 — 全部 vs cohens_d_bf16.json 验证 OK |
| **Fig 5** (crossmodel) | 重新生成 | Spearman ρ=1.0, gradient perm p=0.043 |
| **Cohen's d 6-point** | 重新生成 | 已修正为真正 paired d_z（旧版用的是 pooled d） |

### 修正的关键问题

1. **Fig 1**：旧版使用 v5 数据/硬编码值 → 现在从 bf16 原始 profiling 数据计算
2. **Fig 4**：旧版无 Cohen's d 注释 → 现在标注 paired d_z + significance stars，双模型双面板
3. **Fig 5**：旧版缺少 Spearman/p 注释 → 现在标注 ρ=1.0, p=0.043，并在每点标注 d_z
4. **Cohen's d 6-point**：旧版 `regen_cohens_d_6point.py` 使用 **pooled d 公式**（违反 D048） → 已修正为 paired d_z = mean(D)/SD(D)

### 修正后的 6-point paired d_z 值

| s | DS d_z | QW d_z |
|---|--------|--------|
| 0.10 | 0.376 (marginal) | -0.049 (d<0) |
| 0.15 | 0.442 | 0.281 (marginal) |
| 0.20 | 0.520 | 0.549 |
| 0.25 | 0.683 | 0.889 |
| 0.30 | 0.803 | 1.022 |
| 0.35 | 0.815 | 1.102 |

数据文件：`canonical_bf16_stats.json` 和 `cohens_d_paired_dz_6point.json` 已保存。

---
