# paper figure fig architecture

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_architecture_20260517T114323_result.json`
- **Structured JSON:** [`9fdd4353d1e2e559e0ae.json`](../../sessions/9f/9fdd4353d1e2e559e0ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

输出文件：
- PDF: `figures/paper/fig_architecture.pdf` (34K)
- PNG: `figures/paper/fig_architecture.png` (185K)
- 生成脚本: `figures/paper/gen_fig_architecture.py`

图中内容：左到右流程 Camera 1/2 → SigLIP Vision Encoder (128 tokens) → MLP Connector → **Token Reduction** (红色虚线框，标注三种机制：Zero-mask, True removal, Merge) → Qwen2 1.5B LLM → Flow Matching Action Head → 7-DoF Action。Language instruction 通过底部路径直连 LLM。左上角附 SigLIP 非重叠 spatial patch 示意图。

---
