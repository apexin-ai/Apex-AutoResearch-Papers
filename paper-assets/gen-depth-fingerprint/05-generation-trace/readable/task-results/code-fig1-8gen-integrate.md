# code fig1 8gen integrate

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig1-8gen-integrate_20260516T171306_result.json`
- **Structured JSON:** [`f7e3096db08f6083bfb2.json`](../../sessions/f7/f7e3096db08f6083bfb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完毕，验证通过：

- **PDF**: 33KB, **PNG**: 100KB — 均满足大小要求
- 7 个 feature 列，每列 8 个彩色 dots（5 family 配色正确）+ 黑色 X Overall 标记
- 三区阴影带和标注清晰可见（Strong drift / Moderate / Near-stationary）
- hapax_ratio、ttr、entropy_mean 落在 Strong drift 区；entropy_max、tail_decay 在 Near-stationary 区附近；entropy_std、entropy_min 在 Moderate 区

文件已保存到本地论文目录：
- `artifacts/_project/paper/fig1_differential_response.pdf`
- `artifacts/_project/paper/fig1_differential_response.png`

---
