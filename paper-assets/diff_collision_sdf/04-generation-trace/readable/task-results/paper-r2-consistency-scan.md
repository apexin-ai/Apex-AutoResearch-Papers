# paper r2 consistency scan

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r2-consistency-scan_20260528T065433_result.json`
- **Structured JSON:** [`cdcfa9b1201250c24eaa.json`](../../sessions/cd/cdcfa9b1201250c24eaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fix verified. Here's the full scan report:

---

### 1. 术语一致性 — **PASS**
- "frozen episodes" / "frozen rate": 仅存在于 `archive/` 目录（不参与编译）和 `main.aux`（上次编译残留）。所有活跃 .tex 文件已统一使用 "action-collapsed episodes" 和 "action-collapse rate"。
- "fake safety": 仅在 `introduction.tex:12` 首次引入时出现一次（`colloquially, ``fake safety''`），其后全文不再出现。`\label{sec:fake_safety}` 标识符保持不变。

### 2. SafeVLA 分类一致性 — **FAIL → FIXED**
- `related_work.tex:12`: "Constrained optimization" ✓
- `discussion.tex:6`: "Constrained-optimization approaches (e.g., SafeVLA)" ✓
- ~~`introduction.tex:3`: SafeVLA 被标记为 "SDF-augmented training"（应为 "constrained optimization"），CAPE 被标记为 "constraint-based planning"~~
- **已修复**: 改为 `constrained optimization~\cite{zhang2025safevla}, diffusion-process collision costs~\cite{yang2025cape}`，与 related_work.tex 一致。

### 3. "redundant" 用词 — **PASS**
- `related_work.tex:12`: "redundant **at the tested scale**" ✓
- `discussion.tex:20`: "redundant **at the tested scale** with demonstration data" ✓
- 两处均有适当限定。

### 4. Scope 限定 — **PASS**
- `discussion.tex:3` 首句: "**CAR-based** VLA safety evaluation, **as currently practiced on SafeLIBERO**" ✓
- `abstract.tex:6` 末句: "**EE-only geometric supervision**" ✓
- Claim 3 多处: "**at the tested scale**" / "**across the tested range**" ✓

### 5. "20×" 使用 — **PASS**
活跃文件中恰好 3 处（均在 `claim3.tex`）：
- L3: 首次定义 "a 20$\times$ range of loss weights"
- L32: 关键论证 "a 20$\times$ increase in SDF loss weight"
- L46: figure caption "a 20$\times$ loss-weight range"

### 6. 引用完整性 — **PASS**
- `related_work.tex:15`: HazardArena (`chen2026hazardarena`) 和 VLA-Risk (`vlariskanon2026`) 均已引用 ✓
- `references.bib`: 两者 bib 条目均存在 ✓
- 所有 33 个 `\cite`/`\citep` 引用键均有对应 bib 条目，无悬空引用。

### 7. Oracle caveat 准确性 — **PASS**
`claim2.tex` 末段诚实承认: "the Pi0+A1 baseline (TSR$\,\approx\,$0%) is already fully action-collapsed" 和 "The LoRA baseline is itself largely action-collapsed (99.4% collapsed episodes)"。无 TSR≈70-80% 的错误声称。

### 8. 数值一致性 — **PASS**
- `abstract.tex:5`: "**nearly all** measured avoidance gains" ✓
- bimodal gap: `method.tex:36`, `experimental_framework.tex:23`, `appendix.tex:7` 均为 "below 1\,$\mu$m ... above 200\,mm" ✓

---

**总结**: 8 项检查中 7 项直接 PASS，1 项 FAIL 已修复（introduction.tex 中 SafeVLA 和 CAPE 的分类描述与 related_work.tex 不一致）。

---
