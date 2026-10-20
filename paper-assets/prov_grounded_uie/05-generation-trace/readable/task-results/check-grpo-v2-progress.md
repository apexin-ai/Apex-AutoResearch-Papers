# check grpo v2 progress

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_grpo_v2_progress_20260513T061947_result.json`
- **Structured JSON:** [`89f2cce3ed0f02e49d7e.json`](../../sessions/89/89f2cce3ed0f02e49d7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Step: 16/100
Latest reward: 0.6148 (波动范围 0.62-0.79，无明显上升趋势)
KL: 0.0008 (趋势: 先升后降，step 1→15 从 0.0 升至 0.0016，step 16 回落至 0.0008)
Step time: ~190-205s（最近 step 205s）
预计剩余时间: ~4h26m（tqdm 估算）
GPU 0 状态: 空闲（0%, 0 MiB）
GPU 1 状态: 占用（82%, 35813/97887 MiB）— v2 训练中
```

**关注点**：
- Reward 在 0.61-0.79 间波动，16 步内未见稳定上升，可能需要更多 step 观察
- KL 极低（<0.002），策略几乎没有偏离参考模型，clip_ratio 全为 0——学习信号可能不足
- `completions/clipped_ratio` 达 0.19-0.56，部分生成被截断在 max_length=2048

---
