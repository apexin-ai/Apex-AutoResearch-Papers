# theory causal dag tikz

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_theory_causal-dag-tikz_20260523T010527_result.json`
- **Structured JSON:** [`ecbd0355243d374f59b9.json`](../../sessions/ec/ecbd0355243d374f59b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/causal_dag_tikz.tex`。

结构：
- **M → T → A → C → S** 水平主链，T→C 弯曲绕行
- **A** 红色高亮（bottleneck），T→A 和 A→C 红色粗箭头
- **Y** 虚线框浮于 A 上方，Y--A 虚线表示隐式目标关系
- **C ⊥ Y | A** 标注在 Y 右侧小框中
- 文件顶部可直接 `pdflatex` 编译预览，底部注释块含完整 `figure` 环境供论文粘贴

---
