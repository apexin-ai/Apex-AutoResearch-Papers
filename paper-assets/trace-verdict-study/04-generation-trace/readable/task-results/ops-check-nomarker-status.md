# ops check nomarker status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_nomarker_status_20260516T160538_result.json`
- **Structured JSON:** [`2d240a90307312a29672.json`](../../sessions/2d/2d240a90307312a29672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告：`exception_only_nomarker_seed42`

**状态：正在训练中（活跃）**

### 训练进度
- 当前进度：**99/444 steps (22%)**
- 速度：~9.5s/step
- 预计剩余：~55 分钟
- PID：287933（GPU 0，占用 40914 MiB，利用率 97%）
- 实际训练开始时间：2026-05-16 23:49（非 registry 中的 06:03）

### Eval 情况
- 23:46 有人提前触发了 eval，但因为训练尚未完成（`final/` 目录不存在），eval 报错退出：
  ```
  ValueError: Can't find 'adapter_config.json' at '.../exception_only_nomarker_seed42/final'
  ```

### Checkpoint 目录状态
- `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42/` 存在，但只有 tensorboard events 文件，尚无模型 checkpoint 保存

### 其他 GPU 活动
- GPU 1（PID 279483）在跑另一个实验（可能是 `codellama13b_vota_seed42`，已有 checkpoint-148）

### 结论
实验正常运行中，预计约 55 分钟后训练完成。registry 标记 RUNNING 正确，但 06:03 到 23:49 之间存在长时间延迟（可能排队等前面实验完成）。训练结束后需要重新触发 eval。

---
