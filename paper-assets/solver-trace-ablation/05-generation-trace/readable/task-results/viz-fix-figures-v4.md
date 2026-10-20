# viz fix figures v4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fix-figures-v4_20260515T041523_result.json`
- **Structured JSON:** [`6f8330d2b6887bd54218.json`](../../sessions/6f/6f8330d2b6887bd54218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三张图全部正确嵌入 PDF：
- **fig2_isr_collapse.pdf** → 第5页
- **fig4_prolog_comparison.pdf** → 第6页
- **fig3_hacking_composition.pdf** → 第6页

编译无错误，main.pdf 14页 513KB。

**完成总结**：
- Fig 4 (Prolog comparison): 重新生成，35KB
- Fig 3 (Hacking composition): 新建 gen_fig3.py 并生成，24KB，含 H7/H1/Genuine/Other 堆叠条形图 + 箭头标注
- LaTeX 二遍编译通过，三张图均正确嵌入

---
