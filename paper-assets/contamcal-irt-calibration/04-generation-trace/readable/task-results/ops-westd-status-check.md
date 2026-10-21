# ops westd status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-status-check_20260518T101626_result.json`
- **Structured JSON:** [`dd0c213491d710cdaec3.json`](../../sessions/dd/dd0c213491d710cdaec3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 状态报告 (2026-05-18 18:17 UTC)

---

### 1. 7B Pilot 训练 (PID 17819, cuda:0)

| 指标 | 值 |
|------|-----|
| 进度 | **308 / 3125 steps (10%)** |
| 速度 | ~1.8-2.1 s/it |
| 已耗时 | ~8m54s |
| 预计剩余 | ~1h42m |
| GPU 显存 | 63,272 MiB / 97,887 MiB (65%) |
| GPU Util | 76% |
| GPU 温度 | 71°C |

**Loss 状态: 无输出。** log 文件仅 11 行（全是启动信息），进度条中无 loss 值。无 trainer_state.json，无 W&B runs 目录。Trainer 的 `logging_steps` 可能设得较大，或 loss 尚未到首个 logging 节点。需关注。

---

### 2. 模型下载状态

| 模型 | 大小 | safetensors | .incomplete | 状态 |
|------|------|-------------|-------------|------|
| Qwen2.5-7B | — | — | 无 | **完成** |
| Qwen2.5-14B | 26G | 5 | 无 | **下载中** (PID 5066) |
| gemma-2-9b | 23G | 4 | 无 | **下载中** (PID 6380) |
| phi-4 | 1.6G | **0** | 无 | **仅 metadata，无权重** |
| OLMo-2-1124-7B | 13G | 1 | 无 | **可能不完整，无活跃下载进程** |

phi-4 目录内只有 config/tokenizer 文件，无 safetensors 权重。OLMo 仅 1 个 safetensors 且无活跃下载。这两个模型没有下载进程在跑。

---

### 3. 活跃下载进程

- PID 5066: `hf download Qwen/Qwen2.5-14B`
- PID 6380: `hf download google/gemma-2-9b`

phi-4 和 OLMo 无活跃下载。

---

### 4. 磁盘空间

```
/root/autodl-tmp: 77G / 250G used (31%), 174G 可用
```

---

### 5. cuda:3 状态

**异常：GPU-Util 100% 但无进程、显存 0MiB。** 温度 35°C，功耗 198W。可能是驱动残留状态或刚结束的进程未清理。无实际计算负载。

---

### 需关注项

1. **7B 训练无 loss 输出** — 训练在跑但看不到 loss，建议检查训练脚本的 `logging_steps` 设置，或等第一个 checkpoint 后看 trainer_state.json
2. **phi-4 / OLMo 下载未启动或中断** — 需要手动启动下载
3. **cuda:3 100% Util 异常** — 建议后续观察是否自行恢复

---
