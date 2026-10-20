# figure fig1 trace overview

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1_trace_overview_20260516T013107_result.json`
- **Structured JSON:** [`82e50dfd6b1f6d40090d.json`](../../sessions/82/82e50dfd6b1f6d40090d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 `register_artifact` 工具可用。

**任务完成。** 生成脚本位于 `/root/trace-verdict-study/figures/gen_fig1.py`，输出：

| 文件 | 路径 | 大小 |
|------|------|------|
| PDF | `/root/trace-verdict-study/figures/paper/fig1_trace_overview.pdf` | 37K |
| PNG | `/root/trace-verdict-study/figures/paper/fig1_trace_overview.png` | 200K |

图表内容：从左到右的 pipeline 流程图，包含 Code+Test → Execute → Raw Trace → Compression（4 种策略分支，虚线框标注）→ SFT Training → Verdict，每个压缩策略标注了 accuracy，Exception Only 用绿色高亮并带星号标记。

---
