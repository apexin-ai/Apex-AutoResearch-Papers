# ops figure status audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_figure-status-audit_20260515T102124_result.json`
- **Structured JSON:** [`abd974ebf4310eeaeca4.json`](../../sessions/ab/abd974ebf4310eeaeca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是审计结果。

---

## Figure 状态审计 — CoRL 2026

存在 **3 个 figure 目录**（多版本迭代）：
- **服务器** `figures/` — 旧版 (May 14)，3 个图
- **本地** `artifacts/paper_figures/` — 完整 6 图套件 (May 15 04:43)
- **本地** `artifacts/figures/paper/` — 最新版选图 (May 15 07:57–10:19)

### 按论文内容需求对照

| # | 论文需要的 Figure | 状态 | 最新文件路径 | 备注 |
|---|---|---|---|---|
| Fig 1 | Learning curves (hero figure, 全实验叠加) | **Done** | `artifacts/figures/paper/fig1_learning_curves.pdf` (25K, May 15 07:57) | 最新版。另有旧版在 `paper_figures/fig2_eval_curves.*` 和服务器 |
| Fig 2 | Normalized v/e ratio (>1.5x threshold 诊断) | **Draft — 需更新** | `artifacts/paper_figures/fig1_nve_diagnostic.pdf` (23K, May 15 04:43) | ⚠️ 缺 008e_v3_s2 崩溃轨迹 (D038/D040)。README 注明 s2 当时还在跑 |
| Fig 3 | Factorial / Multi-seed 2×2 grid | **Draft — 需更新** | `artifacts/paper_figures/fig4_multiseed.pdf` (21K, May 15 04:43) | ⚠️ 同上，需纳入 s2 完整数据 |
| Fig 4 | Causal chain / CIVO mechanism diagram | **Done** | `artifacts/paper_figures/fig3_causal_chain.pdf` (31K, May 15 04:43) | matplotlib 生成的概念图。可能需升级为 TikZ/矢量图 |
| Fig 5 | dt amplification (dt=1 vs 2 vs 4) | **Done** | `artifacts/figures/paper/fig5_dt_amplification.pdf` (22K, May 15 10:19) | 最新版 |
| Fig 6 | Multiple collapse pathways / Mitigation | **Draft — 需更新** | `artifacts/figures/paper/fig6_multiple_pathways.pdf` (48K, May 15 06:43) | ⚠️ 需反映 D038/D040：008e_v3_s2 崩溃 + 双通路机制 |
| Table 1 | RSSM fidelity (obs_MSE + reward_MAE) | **Done** | `artifacts/paper_figures/tab_rssm_fidelity.tex` + `fig5_rssm_fidelity.pdf` (23K) | LaTeX 表 + 可视化均有 |
| — | Threshold sensitivity analysis | **Not started** | — | paper_framing.md #10 提到 "0 GPU cost"，但无对应图 |

### 服务器独有 figure（旧版，可忽略）

| 文件 | 内容 | 大小 | 备注 |
|---|---|---|---|
| `figures/fig1_learning_curves.pdf` | 学习曲线 | 19K | 已被本地新版取代 |
| `figures/fig2_normalized_ve.pdf` | NVE ratio | 20K | 已被本地 paper_figures 取代 |
| `figures/fig3_value_scatter.pdf` | Value scatter | 21K | 本地无对应新版，内容可能已并入其他图 |

### 汇总

| 状态 | 数量 | 详情 |
|---|---|---|
| **Done** | 4 | Fig 1 (learning curves), Fig 4 (causal chain), Fig 5 (dt amplification), Table 1 (RSSM fidelity) |
| **Draft — 需更新** | 3 | Fig 2 (NVE diagnostic), Fig 3 (multiseed), Fig 6 (multiple pathways) — 均缺 008e_v3_s2 崩溃数据 |
| **Not started** | 1 | Threshold sensitivity analysis |

### 关键行动项

1. **P0**: Fig 2/3/6 需用 008e_v3_s2 完整数据（D038/D040）重新生成 — 这是论文 narrative 的核心变化（C6 partially falsified, dual pathway）
2. **P1**: Threshold sensitivity analysis 图（0 GPU cost，纯数据分析）
3. **P2**: Fig 4 (causal chain) 考虑是否需要更精美的矢量概念图

---
