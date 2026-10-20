# monitor mvp pilot v5 early steps

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_mvp_pilot_v5_early_steps_20260512T160544_result.json`
- **Structured JSON:** [`a5b38a7bd8017db8dad6.json`](../../sessions/a5/a5b38a7bd8017db8dad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已获取。汇报如下：

## mvp_pilot_v5 训练状态

### 进程状态
- **PID 32154**：存活，已运行 14 分 17 秒
- **当前进度**：~285/1373（~21%）
- **速度**：~1.99s/step

### Loss + Grad Norm（前 300 步）

| Step | Loss | Grad Norm | LR | Epoch |
|------|------|-----------|-----|-------|
| 50 | 2.6410 | 2.172 | 1.42e-06 | 0.036 |
| 100 | 2.6305 | 1.523 | 1.95e-06 | 0.073 |
| 150 | 2.5777 | 1.258 | 1.88e-06 | 0.109 |
| 200 | 2.5689 | 1.164 | 1.80e-06 | 0.146 |
| 250 | 2.5494 | 1.141 | 1.72e-06 | 0.182 |
| 300 | 2.5495 | 1.125 | 1.65e-06 | 0.218 |

### 趋势分析
- **Loss 持续下降**：2.641 → 2.550，前 150 步下降较快，200 步后趋于平稳（step 250 和 300 几乎相同）
- **Grad norm 收敛良好**：从 2.17 快速降至 ~1.13，说明训练稳定
- **LR schedule**：先 warmup（50→100 上升），然后 cosine decay

### GPU 状态
- 利用率 100%，显存 22213 MiB / 97887 MiB

### dtype
- 日志显示 `torch_dtype` 已设置（有 deprecation warning 建议改用 `dtype`），未找到 "bfloat" 关键词。需确认是否实际用的 bfloat16。

### 备注
- 日志文件因 nohup 全缓冲，step 200/250/300 的 loss 未刷新到日志，但 checkpoint-304 的 `trainer_state.json` 中有完整记录
- `save_steps=152`，已有 checkpoint-152 和 checkpoint-304
- 预计总训练时间 ~46 分钟，剩余 ~36 分钟

---
