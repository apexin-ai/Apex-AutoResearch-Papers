# figure fig5 controller signal

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig5-controller-signal_20260523T125812_result.json`
- **Structured JSON:** [`18df90a896a56973b716.json`](../../sessions/18/18df90a896a56973b716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件全部生成。各 mixing ratio 的 max signal：

| r | Max \|ΔS̃_t\| |
|---|---|
| 0 | 33.33 |
| 0.2 | 2.41 |
| 0.25 | 0.79 |
| 0.3 | 0.45 |
| 0.5 | 0.77 |

r=0.3 和 r=0.5 的信号不严格为零（EMA 在初始几步有微小负差分），但相对 r=0 的 33.33 已经可以忽略（<1.5%），视觉上几乎贴近基线。"signal = 0" 标注未放置，因为值非零。如需强制标注或将小于某阈值的值截断为 0，告诉我即可。

---
