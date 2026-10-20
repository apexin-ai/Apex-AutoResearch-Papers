# audit a32 alpha stop loss

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_a32_alpha_stop_loss_20260515T204048_result.json`
- **Structured JSON:** [`8cb1d0dcbb1ac0f905e0.json`](../../sessions/8c/8cb1d0dcbb1ac0f905e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果：**Bug 不存在，alpha=32 正确传入**

### 代码验证

`train_sft.py` 第 137 行正确传递了 `args.lora_alpha` 给 `LoraConfig`：
```python
lora_config = LoraConfig(
    r=args.lora_r,
    lora_alpha=args.lora_alpha,   # ← 正确连接
    ...
)
```

### 所有 a32 训练日志确认 alpha=32

| 日志文件 | 实际 alpha | 状态 |
|---------|-----------|------|
| exp_001_sft_3B_d100_s123_a32_v2.log (PID 594494, GPU 0) | **32** | RUNNING |
| exp_001_sft_3B_d100_s42_a32_v3.log (PID 628668, GPU 1) | **32** | RUNNING |
| exp_001_sft_3B_d000_s42_a32.log (PID 633041, GPU 5) | **32** | RUNNING |
| exp_001_sft_3B_d100_s42_a32.log | **32** | 已完成/失败 |
| exp_001_sft_3B_d100_s42_a32_v2.log | **32** | 已完成/失败 |
| exp_001_sft_3B_d025_s42_a32.log | **32** | 已完成/失败 |

已保存的 checkpoint `Qwen2.5-3B_d025_v3_s42/lora_adapter/adapter_config.json` 也确认 `lora_alpha: 32`, `r: 16`。

### 结论

**不需要 kill 任何进程。** 所有 _a32_ 实验的 `--lora-alpha 32` 被正确传递到 LoraConfig，训练结果有效。

---
