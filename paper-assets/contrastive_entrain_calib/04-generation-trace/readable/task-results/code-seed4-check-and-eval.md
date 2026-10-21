# code seed4 check and eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed4-check-and-eval_20260525T072918_result.json`
- **Structured JSON:** [`8a9d0d8680cd3451c87c.json`](../../sessions/8a/8a9d0d8680cd3451c87c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### seed4 训练：已完成
- **2000/2000 步** 正常完成，耗时 ~2h（12:31–14:30 UTC）
- 5 个 checkpoint 完整：checkpoint-500/1000/1500/2000/final（均含 adapter_model.safetensors ~234MB）
- **S(t) 轨迹**：step 10=0.38 → step 20=0.55 → step 50=0.0001 → **step 60 起坍缩至 0.0000**，此后始终为 0
- **Probe retrain**：每 100 步重训一次（共 20 次），所有 retrain 后 acc=1.0000, auroc=1.0000
- **Final metrics**：loss=-0.0622, sft_loss=0.0002

### seed4 eval：已启动
- PID=12451 在 GPU:0 上运行（nohup）
- 评估 5 个 checkpoint（500/1000/1500/2000/final），每个跑 preset eval + entropy
- 日志：`/root/autodl-tmp/results/exp008_seed4_eval.log`
- 预计耗时 ~4-5h（每个 checkpoint ~1h）

### seed3 checkpoint-2000 / final 详细数据

| Checkpoint | ToF | NoF | SYCONScore | Entropy (bits) |
|---|---|---|---|---|
| checkpoint-1500 | 0.1878 | 0.8287 | 0.3063 | 0.1424 |
| checkpoint-2000 | 0.0442 | 0.9613 | 0.0845 | 0.1701 |
| final | 0.0442 | 0.9613 | 0.0845 | 0.1701 |

seed3 的 ckpt-2000 和 final 指标完全一致（ToF=0.0442, NoF=0.9613, SYCONScore=0.0845, entropy=0.1701 bits）。从 ckpt-1500→2000 有明显的 SYCONScore 下降（0.31→0.08），说明后 500 步训练进一步压低了 sycophancy 但 ToF 也降到了很低水平。

---
