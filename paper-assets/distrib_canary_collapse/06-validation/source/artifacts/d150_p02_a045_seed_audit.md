# D150-P02: α=0.45 Seed Audit

## 找到的 Seed 列表

| Seed | 本地 Artifact 目录 | 分析报告 | 服务器数据 |
|------|-------------------|---------|-----------|
| s42 | `artifacts/alpha_sweep_a045_s42_fp32/` | ✅ 完整 | 两台服务器均已清理 |
| s43 | `artifacts/alpha_sweep_a045_s43_fp32/` | ✅ 完整 | 两台服务器均已清理 |
| s44 | — | ❌ 不存在 | — |

**实际 seed 数 = 2**（s42, s43）

## 每个 Seed 的 PermG 结果

### s42 (fp32, WikiText-103, Pythia-410M)
- **PermG fwd (FDR) = 0/8**
- Min FDR-p = 0.091（距阈值 0.05 有 82%）
- K≥3 = 3/8, K≥4 = 0/8

### s43 (fp32, WikiText-103, Pythia-410M)
- **PermG fwd (FDR) = 0/8**
- Min FDR-p = 0.059（距阈值 0.05 仅 18%）
- K≥3 = 2/8, K≥4 = 0/8

**两个 seed 一致: PermG = 0/8，blind zone 判定稳健。**

## D120 Canonical 分析状态

无独立 D120 JSON（D120 pipeline 可能在 a045 完成前建立）。但有：
- `fdr_gradient_a045.json` — 完整的 2 seed × 8 pair FDR p-values
- 两份独立分析报告（s42: `analysis_alpha_sweep_a045_s42_fp32.md`, s43: `analysis_report.md`）
- `consensus_heatmap_data_m035.csv` — 仅收录 s42（s43 未入 heatmap）
- `dose_response_5method_regime_m035.csv` — α=0.45 行仅 1 seed

## 论文不一致

| 位置 | 当前表述 | 实际情况 |
|------|---------|---------|
| `docs/paper/experiments.tex` L14 | "seven single-seed probing points (α ∈ {0.05, 0.30, 0.35, 0.40, **0.45**, 0.55, 0.60})" | α=0.45 有 2 seeds |
| `docs/paper/experiments.tex` L15 | "remaining levels use a single seed (42)" | α=0.45 实际有 s42+s43 |
| `docs/paper/appendix.tex` L139 | "Table reports BH-corrected p-values ... across **two seeds** at α=0.45" | ✅ 正确 |
| `docs/paper/appendix.tex` Tab `fdr_gradient_a045` | 报了 Seed 42 和 Seed 43 | ✅ 正确 |

**矛盾**：主体文 Section 4.1 称 α=0.45 为 "single-seed probing point"，但 Appendix Table 明确报了 2 seeds。

## 建议修正

`docs/paper/experiments.tex` L14-15 应改为：

> **方案 A**（推荐）：将 α=0.45 从 "single-seed probing points" 列表移出，改为 "six single-seed probing points (α ∈ {0.05, 0.30, 0.35, 0.40, 0.55, 0.60})"，并补充 "α=0.45 uses two seeds {42, 43} to confirm the onset boundary"。

> **方案 B**：L15 改为 "remaining levels use a single seed (42), except α=0.45 which uses two seeds {42, 43}"。

两种方案均需同步更新 seed count 总数（当前 "Total: 15 combinations" 可能也需核实）。
