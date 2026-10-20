# diagnose exp 001 sft 15B d025 s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_15B_d025_s123_v2_20260515T133423_result.json`
- **Structured JSON:** [`e118b36d68b5b02fe65c.json`](../../sessions/e1/e118b36d68b5b02fe65c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断结果

### 根因：训练实际上**成功完成**，EXIT_CODE=1 是误报

### 证据

训练跑完了全部 3384 步（epoch=1.0），所有产出文件完整：

| 检查项 | 状态 |
|--------|------|
| 训练步数 | 3384/3384 (100%) |
| 最终 loss | 1.2723 |
| 运行时间 | 6729s (~1h52m) |
| adapter_model.safetensors | 73MB ✓ |
| adapter_config.json | ✓ |
| tokenizer 文件 | ✓ |
| checkpoint-3384 | ✓ |
| train_config.json | ✓ (脚本最后一个 I/O) |
| "Training complete" 日志 | ✓ (脚本最后一行 log) |
| GPU 0 当前状态 | 空闲 (0MiB) |
| 磁盘空间 | 42GB 剩余，充足 |

### 误报原因

日志开头有 bitsandbytes 加载失败的 traceback：

```
[ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file
OSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory
```

这是非致命错误——bitsandbytes 是 transformers/peft 的传递依赖，本次 bf16 LoRA 训练不需要它。但监控系统可能因为日志中的 `[ERROR]` 标签或 traceback 将实验标记为 EXIT_CODE=1。

### 建议

1. **不需要重跑** — checkpoint 完整可用，直接进入下游评估
2. **消除误报**（可选）：`pip install nvidia-cuda-nvjitlink-cu12` 安装缺失的 `libnvJitLink.so.13`，或在 `train_sft.py` 中将 bitsandbytes 错误降级为 WARNING 而非 ERROR
3. **v1 (pid 533174)** 的日志已不存在（`/tmp/sft_15B_d025_s123_v1.log` 不在了），无法确认 v1 是否也是同样的误报

### 是否可以直接重试

**不需要重试。** 训练已成功，`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter/` 下的 adapter 可直接使用。

---
