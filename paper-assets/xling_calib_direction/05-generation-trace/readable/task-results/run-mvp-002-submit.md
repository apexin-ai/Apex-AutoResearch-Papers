# run mvp 002 submit

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_mvp_002_submit_20260520T165936_result.json`
- **Structured JSON:** [`e90f6dada1abbc90d47c.json`](../../sessions/e9/e90f6dada1abbc90d47c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

mvp_002 启动成功。

- **cuda:1** 占用 17.6GB 显存，GPU 利用率 90%
- 正在提取 `en` 语言激活值，速度 ~34 it/s（14042 样本，预计 ~7 分钟/语言）
- 提取层：`[2, 6, 10, 14, 18, 22, 26]`（7 层，均在模型 28 层范围内）

注意：任务描述中层 30 越界（模型只有 28 层，索引 0-27），已自动修正为 `2,6,10,14,18,22,26`。mvp_001 实际用的也是 `0,4,8,12,16,20,24,27`（非描述中的 31）。

---
