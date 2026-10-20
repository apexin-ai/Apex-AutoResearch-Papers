# paper fig2 cohens d regen

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig2_cohens_d_regen_20260514T092123_result.json`
- **Structured JSON:** [`b5af066d07675e41077f.json`](../../sessions/b5/b5af066d07675e41077f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

### 新旧 Cohen's d 对比

| Sparsity | DeepSeek 旧→新 | Qwen 旧→新 |
|----------|---------------|------------|
| 0.15 | 0.442 → **0.607** | 0.281 → **0.371** |
| 0.20 | 0.520 → **0.725** | 0.549 → **0.722** |
| 0.25 | 0.683 → **0.953** | 0.889 → **1.233** |
| 0.30 | 0.803 → **1.126** | 1.022 → **1.439** |

per-problem paired 计算下所有 d 值均高于旧的 unpaired 值，效应量更强。

### CI / Error bars
`bootstrap_ci_95` 是 median_diff 的 CI，非 Cohen's d 的 CI → **不含 error bars**，只画点+线。

### Qwen s015 标注
Qwen s015 median_diff CI = [-0.005, 0.110] 含 0，图上已用箭头标注 "CI incl. 0 (marginal)"。

输出文件：`/root/autodl-tmp/pacs/figures/fig2_cohens_d.pdf` 和 `.png`，已覆盖旧图。脚本：`/root/autodl-tmp/pacs/analysis/regen_fig2.py`。

---
