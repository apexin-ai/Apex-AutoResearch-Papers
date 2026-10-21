# ops verify d050 s123 and cuda0

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-d050-s123-and-cuda0_20260518T190955_result.json`
- **Structured JSON:** [`f470b9bdf95d50f6ccf4.json`](../../sessions/f4/f470b9bdf95d50f6ccf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### d050_s123：**成功**
- checkpoint 完整：`adapter_model.safetensors` (154MB) 存在，`lora_alpha=32` 符合规范
- `should_training_stop=true`，max_steps=3642，训练正常结束
- 最后 step 3640 metrics：
  - loss: **0.935**
  - mean_token_accuracy: **0.776**
  - epoch: ~1.0
  - total_flos: 1.22e18
- 无独立日志文件（`train_7b_d050_s123.log` 不存在，可能是 batch 脚本 `exp002_s1_7B_batch.log` 统一输出）

### cuda:0：**空闲**
- 0MiB / 97887MiB，无进程
- cuda:1 (55.5G, PID 49198), cuda:2 (550M, PID 53527), cuda:3 (62.8G, PID 46876) 在用

### Phi-4 下载：**失败（不完整）**
- 路径为 `/root/autodl-tmp/models/phi-4/`（小写）
- 缺少 `model-00005-of-00006.safetensors`（6 个分片只有 5 个）
- PID 49771 已死亡
- restart 日志显示 `[Errno 101] Network is unreachable`，仅返回了本地缓存

### OLMo-2 下载：**失败（不完整）**
- 缺少 `model-00003-of-00006.safetensors`（6 个分片只有 5 个）
- PID 49929 已死亡
- restart 日志同样 `Network is unreachable`，返回本地缓存

两个模型下载都因网络不可达而中断，各缺 1 个分片，需要恢复网络后重新下载补全。

---
