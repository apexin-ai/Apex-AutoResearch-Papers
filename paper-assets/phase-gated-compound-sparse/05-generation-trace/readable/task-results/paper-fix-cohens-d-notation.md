# paper fix cohens d notation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-cohens-d-notation_20260514T094929_result.json`
- **Structured JSON:** [`b335cfed50f6b48bfbf9.json`](../../sessions/b3/b335cfed50f6b48bfbf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All remaining `$d{=}` are `$d{=}{-}0.04$` — random eviction, correctly kept as `$d$`.

---

**修改清单：**

| # | 文件 | 位置 | 旧值 | 新值 |
|---|------|------|------|------|
| 1 | abstract.tex:7 | paired effect size range | `Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large)` | `paired $d_z$ growing from $0.61$ (medium) to $1.13$ (large)` |
| 2 | abstract.tex:10 | Qwen threshold | `(Cohen's $d \geq 0.55$` | `($d_z \geq 0.72$` |
| 3 | introduction.tex:14 | DeepSeek effect sizes | `paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large)` | `paired effect sizes ($d_z$) increasing from $d_z{=}0.61$ (medium) to $d_z{=}1.13$ (large)` |
| 4 | introduction.tex:15 | Qwen threshold + marginal | `($d \geq 0.55$)…($d{=}0.28$` | `($d_z \geq 0.72$)…($d_z{=}0.37$` |
| 5 | results.tex:124 | cross-model d trajectories | `Cohen's $d$ trajectories (DeepSeek: $0.44 \to 0.80$; Qwen: $0.28 \to 1.02$…four-point $d$` | `paired $d_z$ trajectories (DeepSeek: $0.61 \to 1.13$; Qwen: $0.37 \to 1.44$…four-point $d_z$` |
| 6 | results.tex:124 | Qwen marginal + threshold | `($d{=}0.28$…($d \geq 0.55$)` | `($d_z{=}0.37$…($d_z \geq 0.72$)` |
| 7 | results.tex:141 | method intro | `Cohen's $d$ for effect size` | `paired $d_z$ for effect size` |
| 8 | results.tex:175 | paragraph header | `Cohen's $d$ (bootstrap` | `paired $d_z$ (bootstrap` |
| 9 | results.tex:180 | Table 4 caption | `Cohen's $d$ and per-problem` | `Paired $d_z$ and per-problem` |
| 10 | results.tex:184 | Table 4 header | `DeepSeek $d$`, `Qwen $d$` | `DeepSeek $d_z$`, `Qwen $d_z$` |
| 11 | results.tex:186 | Table row s015 | `0.44 (small)`, `0.28 (small)` | `0.61 (medium)`, `0.37 (small)` |
| 12 | results.tex:187 | Table row s020 | `0.52 (medium)`, `0.55 (medium)` | `0.73 (medium)`, `0.72 (medium)` |
| 13 | results.tex:188 | Table row s025 | `0.68 (medium)`, `0.89 (large)` | `0.95 (large)`, `1.23 (large)` |
| 14 | results.tex:189 | Table row s030 | `0.80 (large)`, `1.02 (large)` | `1.13 (large)`, `1.44 (large)` |
| 15 | results.tex:195 | DeepSeek text | `small ($d{=}0.44$)…large ($d{=}0.80$)` | `medium ($d_z{=}0.61$)…large ($d_z{=}1.13$)` |
| 16 | results.tex:196 | Qwen text | `($d{=}0.28$…($d \geq 0.55$)` | `($d_z{=}0.37$…($d_z \geq 0.72$)` |
| 17 | results.tex:197 | comparison | `($d{=}0.89$/$1.02$…$0.68$/$0.80$)` | `($d_z{=}1.23$/$1.44$…$0.95$/$1.13$)` |
| 18 | discussion.tex:25 | Spearman context | `Cohen's $d$ effect sizes` | `paired $d_z$ effect sizes` |
| 19 | discussion.tex:29 | onset threshold (3dp→2dp + d→d_z) | `Cohen's $d{=}0.442$…$d{=}0.549$…$d{=}0.281$` | `paired $d_z{=}0.61$…$d_z{=}0.72$…$d_z{=}0.37$` + comment updated to d_z 3dp |
| 20 | conclusion.tex:10 | DeepSeek effect sizes | `$d{=}0.44$ (small) to $d{=}0.80$ (large)` | `$d_z{=}0.61$ (medium) to $d_z{=}1.13$ (large)` |
| 21 | conclusion.tex:16 | Qwen threshold | `$d \geq 0.55$` | `$d_z \geq 0.72$` |

**验证结果：**
- 3dp 值 (0.607, 0.725, 0.953, 1.126, 0.371, 0.722, 1.233, 1.439) — 均仅出现在 discussion.tex:29 注释中 ✓
- `Cohen's $d$` 引用 paired effect size — 0 处 ✓（唯一残留的 `Cohen's $d = -0.04$` 在 results.tex:126 是 random eviction independent-samples d）
- 所有 `{=}0.61` 位置均使用 `$d_z` ✓
- 所有 `$d{=}{-}0.04$` 保持为 `$d$`（random eviction） ✓
- 旧 d 值 (0.44, 0.52, 0.68, 0.80, 0.28, 0.55, 0.89, 1.02) 在 `$d{=}` 模式中无残留 ✓

---
