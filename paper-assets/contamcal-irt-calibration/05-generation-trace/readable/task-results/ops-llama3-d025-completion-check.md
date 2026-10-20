# ops llama3 d025 completion check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-d025-completion-check_20260521T123104_result.json`
- **Structured JSON:** [`daab3f32fe98c69eb673.json`](../../sessions/da/daab3f32fe98c69eb673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
训练结果: success
.done: 存在 (May 21 20:29)
checkpoint: 完整 (adapter_model.safetensors 167MB + adapter_config.json + tokenizer + checkpoint-3384)
log 关键行: 3384/3384 steps, train_loss=1.383, epoch=1.0, runtime=8581s (~2h23m)
eval 触发: 是, PID 521464 (evaluate.py --benchmarks mmlu, d025_s0), 由 monitor PID 521169 触发
GPU 0 状态: 18589 MiB 占用 / 0% util — eval 在 GPU 0 上运行(刚启动，正在加载模型)
GPU 3: 97% util, 37913 MiB — d100_s0 SFT 训练中 (PID 510203)
```

d025 s0 训练正常完成，eval 已自动触发且只有一个 evaluate 进程（PID 521464，mmlu benchmark，GPU 0）。无重复提交。

---
