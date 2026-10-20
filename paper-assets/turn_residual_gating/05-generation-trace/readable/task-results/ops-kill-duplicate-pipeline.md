# ops kill duplicate pipeline

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_duplicate_pipeline_20260519T000528_result.json`
- **Structured JSON:** [`0ff857cf06787af1f9fe.json`](../../sessions/0f/0ff857cf06787af1f9fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整汇报

### 步骤 1: Kill 多余 pipeline
- PID 22503 已成功 kill（SIGTERM，未需 force kill）
- 残留进程确认：只剩 PID 22666/22667 (`run_post_v7.sh`)，双 pipeline 碰撞已消除

### 步骤 2: 全面状态检查

**Pipeline 标记:**
```
NO_DONE_MARKER
```
POST_V7_DONE 标记不存在，pipeline 尚未完成。

**Pipeline 日志:**
```
=== Pipeline started at Tue May 19 07:58:50 CST 2026 ===
Waiting for v7...
```
Pipeline 正在等待 v7 训练完成。

**v7 训练 log 最后 30 行:**
```
Epoch 2 Step 4500 | L_NTP=0.7697 L_GAR=0.0018 L_DIV=0.0000 Loss=0.7715 | Gate=0.9523 | Mem=53.1GB
Epoch 2 Step 4550 | L_NTP=0.9659 L_GAR=0.0002 L_DIV=0.0000 Loss=0.9661 | Gate=0.9495 | Mem=53.1GB
Epoch 2 Step 4600 | L_NTP=0.7175 L_GAR=0.0000 L_DIV=0.0000 Loss=0.7175 | Gate=0.9452 | Mem=53.1GB
Epoch 2 Step 4650 | L_NTP=0.9324 L_GAR=0.0003 L_DIV=0.0000 Loss=0.9327 | Gate=0.9524 | Mem=53.1GB
Epoch 2 Step 4700 | L_NTP=0.7982 L_GAR=0.0003 L_DIV=0.0000 Loss=0.7985 | Gate=0.9431 | Mem=53.1GB
Epoch 2 Step 4750 | L_NTP=0.7690 L_GAR=0.0000 L_DIV=0.0000 Loss=0.7690 | Gate=0.9463 | Mem=53.1GB
[GATE] step=2600 mean=0.9427 std=0.0503 min=0.7969 max=0.9922
[GATE-PROFILE] step=2600 L0:0.863 L1:0.992 L2:0.957 L3:0.797 L4:0.797 L5:0.895 L6:0.977 L7:0.949 L8:0.969 L9:0.953 L10:0.977 L11:0.926 L12:0.918 L13:0.926 L14:0.914 L15:0.957 L16:0.938 L17:0.961 L18:0.941 L19:0.973 L20:0.965 L21:0.969 L22:0.984 L23:0.965 L24:0.969 L25:0.988 L26:0.984 L27:0.992
Epoch 2 Step 4800 | L_NTP=1.0034 L_GAR=0.0001 L_DIV=0.0000 Loss=1.0035 | Gate=0.9516 | Mem=53.1GB
...
Epoch 2 Step 5700 | L_NTP=0.9139 L_GAR=0.0005 L_DIV=0.0000 Loss=0.9145 | Gate=0.9474 | Mem=53.1GB
```
训练正在进行，当前 Epoch 2 Step 5700。Gate 均值稳定在 ~0.94-0.95。

**v7 checkpoint 状态:**
```
total 3324
drwxr-xr-x 5 root root     119 May 19 06:41 .
drwxr-xr-x 3 root root      52 May 19 04:42 epoch_0
drwxr-xr-x 3 root root      52 May 19 06:41 epoch_1
-rw-r--r-- 1 root root 3392947 May 19 02:43 gate_params.pt
drwxr-xr-x 2 root root      99 May 19 02:43 lora
-rw-r--r-- 1 root root     353 May 19 02:43 train_config.json
```
epoch_0 和 epoch_1 checkpoint 都已保存。

**tmux sessions:**
```
v7_train: 1 windows (created Tue May 19 02:43:37 2026)
```

**GPU 状态:**
```
index, utilization.gpu [%], memory.used [MiB], memory.total [MiB]
0, 98 %, 86625 MiB, 97887 MiB
```
GPU 利用率 98%，训练运行正常。

### 步骤 3: Eval 结果
```
NO_EVAL_RESULTS
```
v7 eval 结果尚不存在，符合预期（训练仍在 Epoch 2 进行中）。

### 总结

| 项目 | 状态 |
|------|------|
| 双 pipeline 碰撞 | **已消除**，kill 22503 成功 |
| v7 训练 | Epoch 2 Step 5700 进行中，GPU 98% |
| Pipeline | 正常等待 v7 训练完成 |
| Checkpoint | epoch_0 + epoch_1 已保存 |
| Eval | 尚未开始（训练未完成） |

---
