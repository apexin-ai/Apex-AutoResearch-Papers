# paper compilation check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compilation_check_20260528T062030_result.json`
- **Structured JSON:** [`f3e43cca19d6b8b14e8b.json`](../../sessions/f3/f3e43cca19d6b8b14e8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete audit:

---

## 论文状态清单

### 1. 文件位置
- **本地**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/` (main.tex + 7 section files + references.bib)
- **远程 (westd-34685)**: 无 .tex 文件，仅有分析产出 PDF（`/root/occsafe_vla/artifacts/`, `/root/occsafe_vla/analysis/`）
- **已有 Patch 模板**: `docs/paper/BATCH_A_PATCH_TEMPLATE.md`

### 2. 编译状态
- **最近成功编译**: 2026-05-28 02:04 UTC（main.pdf, 466KB）
- **编译错误**: **无**（main.log 中无 `!` error）
- 编译器: pdfTeX/TeX Live 2025

### 3. 内部数据不一致 (CRITICAL)

**Cell 4 (Detach+LN) 数值冲突**:
| 文件 | 行号 | CAR 值 | n |
|------|------|--------|---|
| results.tex | 28 | 0.826 | 1 |
| results.tex | 9, 49, 62 | 0.826 | 1 |
| **discussion.tex** | **10** | **0.814** | **2** |
| appendix.tex | 85, 156, 160 | 0.826 | 1 |
| method.tex | 51 | — | 1 |
| figures/fig1_overview.py | 216 | 0.826 | 1 |

`discussion.tex:10` 已更新为 n=2, CAR=0.814，但**所有其他文件仍为 n=1, CAR=0.826**。必须统一。

### 4. 需更新的位置（按 Cell 4 新数据到达后）

**BATCH_A_PATCH_TEMPLATE.md 已列出完整更新清单**，核心 16 处：

| # | 文件:行 | 当前值 | 更新内容 |
|---|---------|--------|---------|
| 1 | results.tex:28 | `0.826^{b}`, n=1, TSR=0.894, Δ=+8.1 | CAR/n/TSR/Δ |
| 2 | results.tex:9 | "0.826, n=1" | CAR/n |
| 3 | results.tex:49 | "-4.9pp, n=1 preliminary" | LN simple effect + n |
| 4 | results.tex:55 | "$^{b}$Cell~4 preliminary (n=1)" | caption |
| 5 | results.tex:62 | `$0.826^{b}$`, `-4.9^{b}` | Table 2 LN row |
| 6 | results.tex:72 | "Cell~4 n=1; in progress" | Figure 2 caption |
| 7 | discussion.tex:8 | "Cell~4 preliminary" | 移除 preliminary |
| 8 | discussion.tex:10 | **0.814 (n=2)** ← 已部分更新 | 统一到最终值 |
| 9 | appendix.tex:85 | "n=1, CAR $0.826$" | CAR/n |
| 10 | appendix.tex:139-154 | ANOVA: F=0.02, p=0.89, η²=0.003 | 全部重算 |
| 11 | appendix.tex:156,160 | "preliminary (n=1)" | caption |
| 12 | appendix.tex:169,171,172,177 | Pairwise d involving Cell 4 | 全部重算 |
| 13 | method.tex:51 | "n=1, preliminary" | n |
| 14 | main.tex:27 (abstract) | 无直接 0.826 引用，但引用效应量 | 核对效应量 |
| 15 | figures/factorial_2x2.pdf | Cell 4 单点 | **重绘** |
| 16 | figures/fig1_overview.py:216 | 0.826 hardcoded | **重绘** |

### 5. 派生统计量（需重算）

当 Cell 4 值确定后：
- Gradient flow 主效应 d（当前 d=-0.60）
- Normalization 主效应 d（当前 d≈1.03）
- LN simple effect（当前 -4.9pp）
- Δ(BN-LN) Grad OFF（当前 -5.9pp）
- ANOVA F/p/η²
- 6 个 pairwise Cohen's d

### 6. Placeholder

- **appendix.tex:116-117**: `CAR \textbf{X.XX} ($n{=}2$)` — LIBERO-Object Vanilla baseline，TODO 注释标注 "~08:45 UTC"

### 7. Cell 4 样本量提及

Cell 4 n 值的 "preliminary" / "$^{b}$" 标记出现在 **14 处**（上面已列）。如果最终 n≥3，所有 `$^{b}$` 和 "preliminary" 标记都需移除；如果 n=2，改为 "Two seeds; additional seeds in camera-ready"。

### 8. 当前训练进度（per paper_framing.md）
- `detach_ln_v2_s3` (34685:cuda:3) — ETA 05:51 UTC May 28
- `detach_ln_v2_s2` (34685:cuda:0) — resume
- `detach_ln_v2_s0c_r3` (10894:cuda:2) — ETA 22:45 UTC today（超 DDL）

最乐观情况: DDL 前 Cell 4 可达 n=2-3。

---
