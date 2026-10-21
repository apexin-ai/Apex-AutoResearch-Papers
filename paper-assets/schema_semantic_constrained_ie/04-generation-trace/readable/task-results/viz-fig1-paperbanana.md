# viz fig1 paperbanana

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1_paperbanana_20260521T112804_result.json`
- **Structured JSON:** [`db21de6c49e6188b3824.json`](../../sessions/db/db21de6c49e6188b3824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 生成完成。

**输出路径：**
- PNG: `artifacts/_project/paper/figures/fig1_framework.png` (437 KB, 300 DPI)
- PDF: `artifacts/_project/paper/figures/fig1_framework.pdf` (52 KB)
- 源码: `artifacts/_project/paper/figures/gen_fig1.py`

**过程说明：**
- PaperBanana 的 methodology 图路径需要原生图像生成 API（Gemini Imagen/DALL-E），TUM proxy 只提供 OpenAI text 模型，不兼容
- 改用 matplotlib 手写方案直接生成，三面板布局（Schema Compilation → Constraint Layers → Token Masking），蓝色系=Grammar 组件，橙色系=Semantic 组件
- 如需修改任何布局/文字/颜色，编辑 `gen_fig1.py` 重新运行即可

---
