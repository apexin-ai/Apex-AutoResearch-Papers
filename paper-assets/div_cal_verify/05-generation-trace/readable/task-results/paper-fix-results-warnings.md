# paper fix results warnings

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_results_warnings_20260514T082602_result.json`
- **Structured JSON:** [`155f6e92a3caa086fd20.json`](../../sessions/15/155f6e92a3caa086fd20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处改动均已验证正确。

---

### 汇总

**WARNING 1 (§5.7 ratio 数据)** — 已修正 `results.tex:150`
- `0.83 at 355M` → `$0.85 \pm 0.03$ at 355M ($n{=}2$; 0.83 at seed=42, 0.87 at seed=123)`

**WARNING 2 (Table 2 脚注)** — 已修正 `results.tex:112`
- `statistical tests pending seed=123` → `pending Random~50\% seed=123 and all seed=456 experiments`

**Info 1 (§5.1 标题)** — 已修正 `results.tex:37`
- `Produces` → `Accelerates`

**Info 2 (figures 目录)** — 两个文件均存在：
- `docs/paper/figures/fig_ppl_trends.pdf` ✓
- `docs/paper/figures/fig_ratio_trajectory.pdf` ✓

**Info 3 (`%TODO(355M-seeds)` 占位符)** — 共 7 处：

| 文件 | 行号 | 内容 |
|------|------|------|
| `results.tex` | 125 | `update when Random seed=123 and all seed=456 complete` |
| `results.tex` | 145 | `confirm with seed=123 and report significance` |
| `results.tex` | 148 | `update with seed=456 data` |
| `results.tex` | 151 | `confirm ratio trajectory with seed=123 完成后补充完整 4-method 对比和统计检验` |
| `experiments.tex` | 76 | `update when seed=123 completes` |
| `discussion.tex` | 26 | `confirm with 3-seed data` |
| `discussion.tex` | 34 | `confirm with 3-seed data` |
| `discussion.tex` | 38 | `confirm with seed=123 data` |

---
