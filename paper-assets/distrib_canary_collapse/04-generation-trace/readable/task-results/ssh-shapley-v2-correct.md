# ssh shapley v2 correct

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_shapley_v2_correct_20260517T094130_result.json`
- **Structured JSON:** [`9e07cf32d6b984dd871c.json`](../../sessions/9e/9e07cf32d6b984dd871c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## 真 Shapley Values（K=ceil(0.8·|S|)，32 coalition 枚举）

| 方法 | Shapley(FPR) | Shapley(FNR) |
|---|---|---|
| Naive XCorr | **+0.192** | -0.242 |
| Diff XCorr (FDR) | +0.028 | -0.242 |
| Threshold Onset | -0.034 | -0.242 |
| Perm Granger (FDR) | **-0.110** | -0.242 |
| TY Granger | -0.076 | **-0.033** |

**数据范围**：
- FPR: α=0.0, 3 seeds (s42/s43/s44), 8 pairs/seed = 24 obs
- FNR: α=1.0, 4 seeds (s42/s43/s44/s45), 6 reference pairs/seed = 24 obs

**与 method.tex 已有数字的对比**：
- 论文中 PermG Shapley=+0.375, TY=-2.625 是 **LOO 值**（Leave-One-Out），不是真 Shapley
- 真 Shapley 证实了相同定性结论：PermG 是 FPR 贡献最强的方法（最大幅度减少 FPR），TY 是 FNR 贡献最弱的（仅 -0.033，因为 ECE 通道的 Type II errors）
- 量级差异大：LOO 过度放大了单方法的边际贡献，Shapley 给出跨所有 coalition 的加权平均

**产出**：
- PDF: `docs/paper/figures/shapley_method_contribution.pdf`（服务器）
- JSON: `results/shapley_values.json`（含三种阈值策略的完整结果）
- Artifact: `art_20260517_fbea27`

---
