# ops verify d050 s123 start

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-d050-s123-start_20260518T172326_result.json`
- **Structured JSON:** [`178dd21b95dd49d151c4.json`](../../sessions/17/178dd21b95dd49d151c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动成功，正在初始化。**

- PID 46061 存活
- 模型已加载（Qwen2.5-7B, 339 weights），LoRA 配置正确（r=16, alpha=32）
- 训练数据已加载（58,266 samples）
- 当前处于 Trainer 初始化阶段（设置 optimizer/dataloader），尚未将模型移至 GPU，所以 cuda:0 暂时空闲

日志最后一行是 `warmup_ratio` 弃用警告，无报错。预计几十秒内 GPU 显存会被占用并开始训练。

---
