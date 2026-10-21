# gpu conll n16 s123 launch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_conll_n16_s123_launch_20260521T120112_result.json`
- **Structured JSON:** [`2dc280be0321bc1bdb59.json`](../../sessions/2d/2dc280be0321bc1bdb59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动完成。

**结果汇总：**
- **PID**: 316620 (vLLM EngineCore PID: 316916)
- **GPU**: cuda:2 on autodl-5090-c — 16,399 MiB 占用，正在加载模型
- **数据**: 3453 test instances loaded from conll2003
- **日志**: `~/runs/struct_self_consist_ie/exp_conll_n16_s123.log`
- **状态**: 模型 checkpoint shards 加载中 (75% completed at last check)，vLLM v0.18.1 初始化正常，FLASH_ATTN v2 backend

上次在 autodl-5090 的 tokenizer 问题未复现，说明 autodl-5090-c 上的 checkpoint 是完整的。

---
