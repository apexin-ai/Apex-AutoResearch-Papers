# figure fig2 legend fix v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig2-legend-fix-v2_20260524T105431_result.json`
- **Structured JSON:** [`b3d71b95ba74df270b0d.json`](../../sessions/b3/b3d71b95ba74df270b0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

**修改内容**
- 原始 legend 参数：`ax.legend(loc='upper left', frameon=False)` — 已有 `frameon=False`，无额外框相关参数需删除
- 修改后参数：`ax.legend(loc='upper left', frameon=False, bbox_to_anchor=(-0.02, 1.0))` — 新增 `bbox_to_anchor` 将图例左移至绘图区左边界外侧

**输出文件**
- PDF: `/root/trace-verdict-study/figures/paper/fig3_cross_model_gap.pdf`
- PNG: `/root/trace-verdict-study/figures/paper/fig3_cross_model_gap.png`
- 本地已同步至 `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper/`

**飞书上传**
- 已上传 PNG（文件名 `fig3_cross_model_gap_legend_left.png`）到当前会话飞书群。注意：`feishu_upload_file` 工具不支持指定 `chat_id`，文件上传到了默认群组（`oc_4e0fbdef...`），非任务指定的 A 群（`oc_32bf9618...`）。如需发到 A 群请手动转发。

---
