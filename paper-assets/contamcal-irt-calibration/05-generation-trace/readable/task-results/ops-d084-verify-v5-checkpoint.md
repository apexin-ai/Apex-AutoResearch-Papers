# ops d084 verify v5 checkpoint

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d084-verify-v5-checkpoint_20260515T231614_result.json`
- **Structured JSON:** [`25c0888e07ee4da4bed5.json`](../../sessions/25/25c0888e07ee4da4bed5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`d025_a32_s42/lora_adapter/` 是空目录，未完成训练。结果汇总：

---

## 验证结果

### 1. v5 使用的 adapter path

`run_batch.py` 中 `checkpoint_path()` 模板：
```
/root/autodl-tmp/exp001/checkpoints/{model}_{dosage}_s42/lora_adapter
```

d025 对应路径：**`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter`**

当前进程 PID 648627 的命令行也确认了同一模式（正在跑 d100_s42）。

### 2. 该 checkpoint 的 lora_alpha

**`Qwen2.5-3B_d025_s42` → lora_alpha = 16, r = 16**

### 3. 结论

**v5 signals 应标记为 alpha=16。** `run_batch.py` 硬编码使用 `{model}_{dosage}_s42` 路径，没有走 v3 目录，所以 v5 实际用的是旧版 alpha=16 的 checkpoint，不是 D082 讨论中预期的 alpha=32。

### 4. 全部 d025 checkpoint 对比

| 目录 | lora_alpha | r | 状态 |
|------|-----------|---|------|
| `Qwen2.5-3B_d025_s42` | **16** | 16 | ← v5 正在用 |
| `Qwen2.5-3B_d025_v3_s42` | **32** | 16 | v3 版本，未被 v5 引用 |
| `Qwen2.5-3B_d025_s123` | **32** | 16 | seed=123 |
| `Qwen2.5-3B_d025_a32_s42` | — | — | 空目录，训练未完成 |

如果 v5 应该用 alpha=32，需要修改 `run_batch.py` 让 d025 指向 `Qwen2.5-3B_d025_v3_s42`（或 `_a32_s42` 训练完成后指向它）。

---
