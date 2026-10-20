# paper figures cohens d update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures_cohens_d_update_20260514T092027_result.json`
- **Structured JSON:** [`cc1488e6511981ff649b.json`](../../sessions/cc/cc1488e6511981ff649b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

### 新 Fig 2 已生成

**路径**: `/root/autodl-tmp/pacs/figures/fig2_cohens_d.pdf` (20.2 KB)

**新值（per-problem paired Cohen's d, B=10000 bootstrap CI）**:
| | s015 | s020 | s025 | s030 |
|---|---|---|---|---|
| **DeepSeek** d | 0.607 | 0.725 | 0.953 | 1.126 |
| DS 95% CI | [0.479, 1.040] | [0.597, 1.236] | [0.774, 1.206] | [0.931, 1.418] |
| **Qwen** d | 0.371 | 0.722 | 1.233 | 1.439 |
| QW 95% CI | [-0.028, 0.778] | [0.279, 1.341] | [0.957, 1.650] | [1.217, 1.867] |

- QW s015 标注为 "marginal"（Cohen's d CI 含 0，median_diff CI [-0.005, 0.110] 也含 0）
- Effect size thresholds (0.2/0.5/0.8) 水平虚线保留

### 其他 Figures
- **Fig 1** (Dose-Response)、**Fig 3** (Crossover)、**Fig 4** (Per-Problem Distribution): 不引用 Cohen's d，无需改动。已重新生成确认无报错。

### 旧图备份
- `/root/autodl-tmp/pacs/figures/fig2_cohens_d_segment_level.pdf` (20.4 KB) — 可用于 supplementary robustness check

### 脚本更新
- `generate_paper_figures.py` 已更新：Fig 2 从 `rebootstrap_b10000_results.json` 计算 per-problem paired Cohen's d + bootstrap CI，不再读取旧的 `cohens_d_bf16.json`/`cohens_d_bf16_qwen.json`
- 独立脚本 `generate_fig2_paired.py` 也保留可单独运行
- 计算得到的 CI 保存在 `analysis_output/cohens_d_paired_b10000.json`

---
