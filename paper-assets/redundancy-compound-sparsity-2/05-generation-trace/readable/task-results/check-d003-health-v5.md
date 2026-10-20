# check d003 health v5

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d003_health_v5_20260512T152722_result.json`
- **Structured JSON:** [`4918a901b18bf49e3dc0.json`](../../sessions/49/4918a901b18bf49e3dc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### EXP2 日志 (d003_wikitext_32k) 完整状态

**模型加载成功**，48 layers, kv_heads=8

**WikiText-2 数据**: 32768 tokens, split: prefill=26214, eval=6554, budget=13107

**已完成的策略**:
- `full` — 已完成
- `ema_0.7` — 已完成，PPL=8.1367 (耗时 1281.9s)

**正在运行的策略**:
- `ema_0.5` — prefill 阶段 83% (43/52)，速度 ~16s/it，预计还需约 2.5 分钟完成 prefill，之后进入 eval 阶段 (6554 items)

---

### 总结

| 实验 | 状态 | 当前阶段 | 备注 |
|------|------|---------|------|
| EXP1 (reasoning_traces) | **运行中** | `full` 策略 eval 阶段进行中 | PID 28311, GPU 0, ~30.6GB 显存 |
| EXP2 (wikitext_32k) | **运行中** | `ema_0.5` 策略 prefill 83% | PID 28390, GPU 1, ~32.4GB 显存，已完成 full + ema_0.7 |

两个实验均正常运行，无错误，无结果文件（尚未完成）。

---
