# figure fix bcs scaling all3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fix_bcs_scaling_all3_20260515T232401_result.json`
- **Structured JSON:** [`54b85cde38fd8176b328.json`](../../sessions/54/54b85cde38fd8176b328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 26K，有效。

**修改摘要：**

| 修复 | 内容 |
|------|------|
| **修复 1** | 模型名 `Qwen3-32B-FP8` → `Qwen3-32B`，`LLaMA-3.1-8B-Instruct` → `LLaMA-3.1-8B` |
| **修复 2** | Panel (a): 16-rel/80-rel 保持实心 marker + 实线；40-rel 改为空心 marker（`markerfacecolor='white'`）+ 虚线连接。Panel (b): 40-rel 柱状图加斜线填充（`hatch='///'`）区分 |
| **修复 3** | 删除 `axhspan` 绿色阴影和 `saturation zone` italic 标注 |

**数据未变**：Qwen3-32B 16-rel Δ=9.1pp, 40-rel Δ=33.3pp, 80-rel Δ=31.2pp; LLaMA-3.1-8B 80-rel Δ=27.1pp — 与脚本输出验证一致。

---
