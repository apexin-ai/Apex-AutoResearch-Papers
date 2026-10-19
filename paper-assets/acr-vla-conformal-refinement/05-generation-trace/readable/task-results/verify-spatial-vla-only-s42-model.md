# verify spatial vla only s42 model

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_spatial-vla-only-s42-model_20260524T211224_result.json`
- **Structured JSON:** [`1d95a894823ee34cd824.json`](../../sessions/1d/1d95a894823ee34cd824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## P0 确认：spatial-vla-only-s42 确实是 SmolVLA，wall_clock 长因为服务器负载

### 关键证据

日志明确记录：
```
[evaluate] args: {..., 'model': 'smolvla', 'smolvla_path': '/root/autodl-tmp/models/smolvla_libero/', ...}
[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...
Reducing the number of VLM layers to 16 ...
Loading weights from local directory
```

- `model` 参数为 `smolvla`
- 加载路径为 SmolVLA 专用路径 `/root/autodl-tmp/models/smolvla_libero/`
- "Reducing VLM layers to 16" 是 SmolVLA 的架构特征
- 无任何 pi05 / π0.5 字样

### wall_clock 长的原因

进程仍在运行（PID 76497，从03:34开始），该服务器**同时跑着6个eval进程**（GPU 0-5全占满），CPU争用严重（每个进程~800% CPU）。日志显示实验在第6/10个task处被tee缓冲截断，尚未完成。

**结论：数据可信，无需从 Table 1 剔除。**

---
