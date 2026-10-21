# ssh status check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status-check-34685_20260528T232344_result.json`
- **Structured JSON:** [`535b47a9f2b870bb766b.json`](../../sessions/53/535b47a9f2b870bb766b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 状态

### 训练进度 (full_occ_bn_v2_s2_r5, PID 30149)

| 指标 | 值 |
|------|-----|
| 状态 | **运行中**，已运行 14m47s |
| 当前 step | **858 / 50,005** (1.7%) |
| 训练速度 | ~1.0 it/s |
| 预估剩余时间 | **~13h56m** |
| Checkpoint | 尚未保存（save_freq=10000，需到 step 10000） |

### Loss 趋势

| Step | occ_loss | action_loss |
|------|----------|-------------|
| 0 | 0.1422 | 0.6641 |
| 800 | 0.0273 | 0.2520 |

两个 loss 均持续下降，趋势正常。occ_loss 从 0.14 降到 0.027（-81%），action_loss 从 0.66 降到 0.25（-62%）。

### GPU 状况

| GPU | 型号 | 显存使用 | 显存空闲 | 总显存 |
|-----|------|---------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 62.5 GB | 32.5 GB | 95.6 GB |

- **仅可见 1 张卡**（cgroup v2 限制），非白名单中的 4 张
- 该卡被 PID 30149 独占（63,940 MiB）
- **无空闲 GPU 可用**

### 关键问题

按当前速度 ~1.0 it/s，完成 50,005 步需 ~14h，预计完成时间约 **5/29 21:00 UTC**，**已超过 C003 截止时间**（5/28 12:00 UTC）。

---
