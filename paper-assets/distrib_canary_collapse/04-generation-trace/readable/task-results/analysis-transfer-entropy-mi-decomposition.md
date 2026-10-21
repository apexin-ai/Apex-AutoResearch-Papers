# analysis transfer entropy mi decomposition

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_transfer_entropy_mi_decomposition_20260521T083812_result.json`
- **Structured JSON:** [`04f0d86a446afc561a4e.json`](../../sessions/04/04f0d86a446afc561a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. Here's the analysis summary:

---

## Transfer Entropy / MI Decomposition 结果

### 实验规模
- **T=10**: 15 个 α 值 (0.00–1.00), 8 metric pairs × 1000 bootstrap = 120 组计算
- **T=20**: 6 个 α 值, 48 组计算
- Bootstrap CI 稳定性: 0/120 (T=10) 和 0/48 (T=20) 的 TE CI 包含 0

### 核心发现

**1. "高MI低TE" 假设：部分支持**
- 仅 **2/8 pairs** 完全支持假设（均涉及 perplexity）：
  - `ece → perplexity`: α=0.50 MI=0.11/TE=1.10 → α=0.60 MI=0.52/TE=0.28 (MI上升，TE下降)
  - `token_entropy → perplexity`: α=0.50 MI=0.0007/TE=1.03 → α=0.60 MI=0.12/TE=0.32
- 其余 6/8 pairs: α=0.60 时 MI 和 TE **同时升高**（非"同步但无因果领先"）

**2. TE 方向性——最清晰的结果**
| α | forward-dominant pairs | avg net TE |
|---|---|---|
| 0.25 | 4/8 (coin flip) | 0.14 |
| 0.50 | 5/8 | 0.42 |
| 0.60 | 6/8 | 0.57 |
| 0.75 | 6/8 | 0.99 |
| 1.00 | **8/8** | 1.59 |

α 越大，canary→downstream 的因果方向越强、越一致。这与论文"canary 是 early warning"的叙事一致。

**3. Sync dip 区间特征**
- dip zone (α=0.60–0.65) 的 avg MI 略高于 detection zone (α=0.40–0.52)，但 TE 并非特别低
- α=0.50 反而是 TE 最低的 detection zone 点 (avg TE=0.94 vs 其他 >1.3)
- 解读：sync dip 的本质可能不是"同步但无因果"，而是中间 α 区间 canary 和 downstream 受同一 upstream force 驱动的共变效应

### 输出文件
- 脚本: `westd-17855:results/analysis/transfer_entropy/transfer_entropy_analysis.py`
- 结果 JSON: `te_mi_results.json` (83KB)
- 图表: `fig1_mi_vs_alpha`, `fig2_te_vs_alpha`, `fig3_mi_te_gap`, `fig4_comparison_a050_a060` (PDF+PNG)
- 3 个 artifact 已注册

---
