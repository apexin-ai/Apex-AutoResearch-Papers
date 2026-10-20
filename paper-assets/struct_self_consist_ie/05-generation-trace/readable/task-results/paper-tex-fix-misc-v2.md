# paper tex fix misc v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_tex-fix-misc-v2_20260525T203524_result.json`
- **Structured JSON:** [`7cbab530c3f180b9cb5e.json`](../../sessions/7c/7cbab530c3f180b9cb5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是搜索结果总结：

## 修改摘要

### Task 4a: Scale Ablation Table — **值不存在，无法修改**

在编译版（`docs/paper/sections/`）中彻底搜索了 `.938`、`.793`、`.662`：
- `.938` **不存在于任何编译版 tex 文件**（仅出现在 `figures/_gen_fig_oracle_scaling.py` 的曲线拟合参数中）
- `.793` 出现在 `appendix.tex:2001`，但是 Few-NERD **Location 实体类型** 的 Greedy F1（不是 SciERC 4B Oracle F1）
- `.662` 出现在 `appendix.tex:1996`，但是 Few-NERD **Event 实体类型** 的 LP Selection F1（不是 SciERC 4B Greedy F1）

两个 scale ablation 表：
- `tab:scale_comparison`（appendix.tex:1614）— 无 4B 行，只有 7B/8B/14B/72B
- `tab:scale_ablation_app`（appendix.tex:1650）— 只有 QE ρ（SJ, FK），无 Oracle/Greedy F1 列

**结论：4B 的 Oracle F1 和 Greedy F1 数据未以表格形式出现在编译版中。**

### Task 4b: WNUT-17 SJ ρ — **已验证，无需修改**

`grep -rn "0\.062" docs/paper/` 结果：仅出现在不相关上下文中（LP range 0.0623、FK conditional σ ±0.062、LP range median 0.062），与 WNUT-17 SJ ρ 无关。

### Task 4c: RE zero-F1 百分比 — **编译版已正确，无需修改**

RE zero-F1 在编译版中已经是 "40%"：
- `appendix.tex:1047`: "40\% of RE instances receive zero F1"
- `appendix.tex:1052`: "RE's $40$\% zero-F1 rate"
- `appendix.tex:1075`: "159 (40\%) have zero F1"

唯一的 "44%" 出现在 `appendix.tex:449`，描述的是 SciERC NER 高多样性实例（≥4 unique outputs, n=232/529=44%），与 RE zero-F1 无关。

### Task 4d: Fisher z-test — **比较不存在于编译版中**

计算结果：z = 2.44, p = 0.0146（SJ NER ρ=0.360 vs RE ρ=0.211）。

编译版中的 Fisher z-test 引用：
1. `appendix.tex:160` — RE SJ ρ Q1 vs Q4 sentence length（p=0.004）— **不是 NER vs RE 比较**
2. `appendix.tex:323` — SJ > LP 5-seed Holm 校正 — **不是 NER vs RE 比较**
3. `appendix.tex:390` — 同 #1 的 p-value 表格条目

**NER SJ ρ vs RE SJ ρ 的 Fisher z-test 比较不存在于编译版论文中。**

### 编译状态

论文编译成功（0 errors），PDF 共 45 页。

---

**总结：编译版 (`docs/paper/`) 中这四个 task 涉及的目标值要么已经正确（4b, 4c），要么不存在于编译版中（4a, 4d）。所有修改请求都无法在编译版中找到对应的旧值。可能这些值存在于某个尚未合入编译版的草稿中，或者由之前的 Worker 已经修正/移除。**

---
