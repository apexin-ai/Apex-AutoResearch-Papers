# check v9 pcgrad status urgent

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v9_pcgrad_status_urgent_20260519T230817_result.json`
- **Structured JSON:** [`3bbb589ceb97aa17f5bc.json`](../../sessions/3b/3bbb589ceb97aa17f5bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论
状态: **RUNNING**
PID: 83865 (存活，运行 5h26m，CPU 100%)
GPU: GPU 0 占用 98%，86.5GB / 97.9GB 显存
进度: Epoch 2 Step 350 / 24000 micro-steps (约 8350/24000 = **34.8%**)
预估剩余: **~10h** (按 25.6 steps/min 估算)

## 原始数据

**检查 1 — 进程**
```
PID 83860  05:26:26  bash wrapper (存活)
PID 83865  05:26:26  python src/train_phase2_v9_pcgrad.py (存活, CPU 100%)
```

**检查 2 — GPU**
```
GPU 0: 98%, 86473 MiB / 97887 MiB
PID 83865 占用 86464 MiB
```

**检查 3 — 训练日志末尾**
```
Epoch 1 done | Avg Loss=0.9449 Avg NTP=0.9435 Avg GAR=0.0013 Avg DIV=0.0000
Checkpoint saved to checkpoints/tg_v9_pcgrad_s42/epoch_1
Epoch 2 Step 350 | L_NTP=1.0505 L_GAR=0.0033 L_DIV=0.0000 Loss=1.0537 | Gate=0.9414

[GATE] step=2000 mean=0.9607 std=0.0503 min=0.7617 max=1.0000
[PCGRAD] step=2000 cos_sim=0.0190 conflict_layers=51.3%
```

**检查 4 — Checkpoints**
```
epoch_0/  (May 20 04:21)
epoch_1/  (May 20 07:01)
```

---
