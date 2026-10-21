# code fix figure fontsize v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_figure_fontsize_v2_20260517T113417_result.json`
- **Structured JSON:** [`8a812a47db375f17f4c2.json`](../../sessions/8a/8a812a47db375f17f4c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终报告

| PDF | 本地路径 | 远程路径 | 大小 | 最小字体 | 结果 |
|-----|---------|---------|------|---------|------|
| `fig_32layer_attention.pdf` | artifacts/.../paper/ (14867B, May 17 08:08 UTC) | `/root/vla-ssd/scripts/fig_32layer_attention_profile.pdf` (14854B) | ~14.9KB | **8.00pt** | **PASS** |
| `fig_l1_stacked_bar.pdf` | artifacts/.../paper/ (29419B, May 17 07:39 UTC) | `/root/autodl-tmp/vla-ssd/results/attention/fig_l1_attention_three_conditions.pdf` (23264B) | ~23-29KB | **8.00pt** | **PASS** |

### 字体详情

- **fig_32layer_attention**: 字体尺寸 `[8.0, 9.0]`。8pt 用于 annotations (entry/exit routing, mid-layer processing) 和 legend。9pt 用于轴标签。
- **fig_l1_stacked_bar**: 字体尺寸 `[8.0, 9.0, 10.0]`。8pt 用于 tick labels、annotation text 和 legend。9pt 用于 xlabel/ylabel。10pt 用于 subplot titles。

### 结论

两个 PDF 最小字体均为 8pt，满足 ≥ 8pt 要求。无需修改生成脚本。

---
