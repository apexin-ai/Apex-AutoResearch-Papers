# data fig probe trap json

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fig-probe-trap-json_20260520T181034_result.json`
- **Structured JSON:** [`7cca4f656bbf60339a10.json`](../../sessions/7c/7cca4f656bbf60339a10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已写入 `artifacts/figures/probe_trap_data.json` 并注册为 artifact `art_20260520_43877a`。

数据来源：westd-28034 上 exp-008v3 训练日志（TRL trainer 每 10 步输出的 summary dict 中提取 entropy，`[step N]` 行提取 R1_mean），D027 eval 数据来自 registry。R1_mean 的剧烈波动（0→0.875→0.25→1.0）源于 probe 每 500 步重训，但模型行为（stubbornness, ToF≈0）从 step 500 起锁死不变。

---
