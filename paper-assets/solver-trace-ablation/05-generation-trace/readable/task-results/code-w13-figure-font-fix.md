# code w13 figure font fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w13-figure-font-fix_20260520T100141_result.json`
- **Structured JSON:** [`dd2686fbc1b476a8d284.json`](../../sessions/dd/dd2686fbc1b476a8d284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个文件全部更新完成。

变更总结：
- **Fig 3 / Fig 4**：字号已满足要求（legend ≥8, ticks ≥8, labels ≥9），无需改动，仅重新生成
- **Fig 5**：修改了 `gen_fig5.py` 中 5 处字号——rcParams 里 `axes.labelsize` 8→9、`xtick/ytick.labelsize` 7.5→8、`legend.fontsize` 7→8；两处 annotation 和 legend 的 inline fontsize 从 6/6.5→8

---
