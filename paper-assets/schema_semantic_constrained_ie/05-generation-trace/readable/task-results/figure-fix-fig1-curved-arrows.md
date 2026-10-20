# figure fix fig1 curved arrows

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fix-fig1-curved-arrows_20260522T064040_result.json`
- **Structured JSON:** [`c6b85fe21ba409499c42.json`](../../sessions/c6/c6b85fe21ba409499c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。图片验证结果：

- **蓝色箭头**（Grammar Automaton M_g → Grammar Layer）：已改为向上弧线，清晰绕过中间区域
- **橙色箭头**（Semantic Rules → Semantic Layer）：已改为向下弧线，清晰绕过中间区域
- 两条曲线方向相反，互不覆盖
- 其他所有元素（t+1 U 形折线、No/Yes 白色背景、enabling 标签等）保持不变

**改动详情**（`gen_fig1.py` 第 152-165 行）：
- 蓝色箭头：`draw_arrow` → `FancyArrowPatch` + `connectionstyle='arc3,rad=0.4'`（正值 = 向上弧）
- 橙色箭头：`draw_arrow` → `FancyArrowPatch` + `connectionstyle='arc3,rad=-0.5'`（负值 = 向下弧）

---
