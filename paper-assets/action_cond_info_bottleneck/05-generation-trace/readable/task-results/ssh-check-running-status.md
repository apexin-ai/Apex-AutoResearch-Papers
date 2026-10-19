# ssh check running status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_running_status_20260518T010625_result.json`
- **Structured JSON:** [`4e071dcf267d885db50e.json`](../../sessions/4e/4e071dcf267d885db50e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. PID 745668 (LoRA 训练) — **存活**
- GPU 0，15276 MiB 占用

### 2. LoRA 训练进度
- **Step 14200 / 20000**（71%）
- loss ≈ 0.25，task_loss ≈ 0.07，ib ≈ 0.50，β=0.01
- **1.8 steps/s**，scorer_mean ≈ 0.365
- 剩余 5800 steps → **预估 ~54 分钟**

### 3. Eval 进程 — **存活**
- nvidia-smi 显示 GPU 1 上 PID **759167**（可能是 759162 的子进程），6533 MiB

### 4. Eval 进度
- Checkpoint: `acib_connector_only_seed42/checkpoint-20000`，scoring_alpha=0.0
- 4 个 suite：`libero_spatial` → `libero_object` → `libero_goal` → `libero_10`
- 当前：**libero_spatial**（第 1/4 个），rollout 进度 176/280（63%），running_success_rate=0.0%
- 刚启动不久（09:03 开始），大部分评估还在前面

### 5. GPU 状态

| GPU | 显存 | 利用率 | 温度 | 功耗 |
|-----|------|--------|------|------|
| 0 | 15287 / 97887 MiB | 74% | 68°C | 504W/600W |
| 1 | 6552 / 97887 MiB | 1% | 35°C | 87W/600W |

---
