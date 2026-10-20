# paper table7 update m004 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table7_update_m004_v2_20260518T123424_result.json`
- **Structured JSON:** [`5f36a8355ae524aed490.json`](../../sessions/5f/5f36a8355ae524aed490.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总如下：

---

## 修改清单

### experiments.tex — Table 7 (`tab:generalization`)

| 位置 | 变更 |
|---|---|
| **Caption (L342)** | `single seed per condition` → `$n_{\text{perm}}{=}5{,}000$`; `8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded)` → `8~pairs per condition ... two seeds (s42, s43) to assess replicability` |
| **GPT-2m 行 (L349)** | `-- -- -- -- -- -- \textit{pending}` → `8/8 8/8 8/8 6/8 3/8 5/8 6/8` |
| **OPT-1.3B 行 (L350)** | Diff: `8/8` → `6/8` |
| **Scale 行 (L351)** | 添加 `(s42)` 标签 |
| **Scale s43 行 (NEW)** | `8/8 6/8 8/8 6/8 2/8 4/8 6/8` |
| **C4 行 (L352)** | 改为 `(s42)`；Diff `8/8→6/8`, Thresh `6/8→8/8`, PG_fwd `8/8→6/8`, PG_rev `4/8→3/8`, TY `4/8→3/8`, K≥4 `7/8†→6/8` |
| **C4 s43 行 (NEW)** | `8/8 6/8 8/8 6/8 0/8 3/8 6/8` |
| **Footnote** | 删除 `†` 注释（C4 专项）；保留 PG rev 通用说明 + perplexity 说明；3行→2行 |

### experiments.tex — 正文

| 位置 | 变更 |
|---|---|
| **Architecture 段: Threshold** | `reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's` → `reaches 8/8 on both GPT-2-medium and OPT-1.3B, where` |
| **Architecture 段: TY** | `ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M)` → `ranges from 4/8 (Pythia-410M) to 6/8 (OPT-1.3B), with GPT-2-medium at 5/8` |
| **Architecture 段: Despite** | `Despite this cross-method variance, the consensus threshold absorbs it: all three...` → `All three architectures converge at $K{\geq}4/5$ consensus.` |
| **Scale 段 (6行重写)** | 单 seed → 双 seed (s42 5/8, s43 6/8)；PG_rev/TY 分 seed 报告 |
| **Domain 段 (4行重写)** | `7/8` → `6/8 in both seeds`；ECE reverse 分 seed 报告；`8/8 PG_fwd` → `6/8` |

### discussion.tex

| 行 | old → new |
|---|---|
| **L15** | `Preliminary cross-architecture validation ... suggests ... all 6 ... 0/6 reverse` → `Cross-architecture validation ... confirms ... 6/8 ... reverse 0/4 token_entropy; 3/8 ECE` |
| **L17** | `In preliminary $\alpha{=}0.25$` → `In $\alpha{=}0.25$` |
| **L101** | `beyond our single-seed GPT-2-medium validation` → `beyond the current single-seed conditions` |

### conclusion.tex

| 行 | old → new |
|---|---|
| **L11** | `ECE: marginal reverse in 3/4 verified conditions` → `ECE: marginal reverse in most verified conditions` |
| **L12** | `yields even stronger consensus (7/8 at $K{\geq}4/5$)` → `yields Tier~3 consensus (6/8 at $K{\geq}4/5$ in both seeds)` |

### 验证结果
- TBD/TODO: 0
- Preliminary: 0
- pending (table): 0
- n_perm=5000: 在 caption 中确认

---
