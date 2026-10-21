# write section6 reviewer fixes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_section6_reviewer_fixes_20260514T184201_result.json`
- **Structured JSON:** [`1f11424d6c05278d0b67.json`](../../sessions/1f/1f11424d6c05278d0b67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 项修复已完成。汇总：

---

### 修复汇总

**Fix 1 — 双数据集报告**（3 处）

| 位置 | 原文 | 修改后 |
|------|------|--------|
| L85 (Post-hoc段末) | `near-complete elimination (DR↓94%, from 15.37% to 0.93%)` | `near-complete to substantial elimination (DR↓94% on SciERC, ↓45% on DocRED)` |
| L98 (Quality段) | `violations decrease from 15.37% to 0.93% (↓94%)` + 仅SciERC F1 | `violations decrease by 94% on SciERC (15.37%→0.93%) and 45% on DocRED` + 标注 F1 为 SciERC |
| L108 (Our Approach) | `near-complete elimination ... (DR 15.37%→0.93%)` | `near-complete to substantial elimination (DR↓94% on SciERC, ↓45% on DocRED)` + 标注 quality cost 为 SciERC |

**Fix 2 — S2 降级**
- 原：`OntoCoDec's S2 (two-pass) strategy can also be viewed as an instantiation of CRANE's alternating approach: the first pass performs...`
- 改：`A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference...`

**Fix 3 — "First" claims 防御性修改**（2 处）
- L33：`first to migrate` → `first to \emph{automatically compile} IE ontology axioms...into token-level decoding masks`
- L106：加 `\emph{automatically compile}` 和 `without manually authored rules`（与 EnriCo 的手动 ASP 规则区分）

**Fix 4 — Our Approach 补充**
- L108 新增：`This approach is orthogonal to supervised IE methods and applicable to any autoregressive LM without model modification or additional training.`

**Fix 5 — Bib cite key**
- `synchromesh_neurips2022` → `synchromesh_iclr2022`（已更新 3 个文件：`relwork_new_entries.bib`、`section6_related_work.tex`、`section6_relwork_outline.tex`）
- `roth_yih_2004` 确认 venue 为 CoNLL-2004 at HLT-NAACL 2004 ✓

---
