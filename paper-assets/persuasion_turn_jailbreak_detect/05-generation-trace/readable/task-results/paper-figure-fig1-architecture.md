# paper figure fig1 architecture

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_architecture_20260518T033455_result.json`
- **Structured JSON:** [`8d9bfc760cf4b64d181a.json`](../../sessions/8d/8d9bfc760cf4b64d181a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

输出文件：
- **PDF**: `figures/paper/fig1_architecture.pdf`
- **PNG**: `figures/paper/fig1_architecture.png`
- **生成脚本**: `figures/paper/gen_fig1_architecture.py`

图表展示了 DisPeD 两阶段架构：上方 Treatment Pipeline（蓝色系，Persuasion-Aware DeBERTa + 8-class persuasion 橙色头 + jailbreak intent 绿色头），下方 Baseline Pipeline（灰色系，Vanilla DeBERTa），共享 Stage 2 的 Mean Pooling + Binary Classifier。两个 Stage 用虚线框分隔标注。

---
