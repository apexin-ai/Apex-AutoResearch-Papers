# ops verify running experiments

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_running_experiments_20260521T090138_result.json`
- **Structured JSON:** [`9d64b3a088ef63762941.json`](../../sessions/9d/9d64b3a088ef63762941.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 8 个实验确认 RUNNING**，所有 GPU 都有活跃 python 进程和显存占用。

### westd-17855 (6 GPU)

| GPU | exp_id | PID | 进度 | 当前状态 |
|-----|--------|-----|------|---------|
| 0 | a000_s47_fp32 | 454255 | 5/10 | 生成 gen_5 合成数据 |
| 1 | gen_gpt2m_s43_fp32 | 442662 | **9/10** | 训练最后一轮 gen_9 |
| 2 | a000_s45_fp32 | 448950 | 8/10 | 生成 gen_8 合成数据 |
| 3 | scale_69b | 400550 | 7/10 | 训练 gen_7 (97%) |
| 4 | a052_s43_fp32 | 454331 | 5/10 | 生成 gen_5 合成数据 |
| 5 | a046_s43_fp32 | 454886 | 5/10 | 训练 gen_5 (77%) |

### westd-19828 (2 GPU)

| GPU | exp_id | PID | 进度 | 当前状态 |
|-----|--------|-----|------|---------|
| 0 | a000_s48_fp32 | 656193 | 2/10 | 生成 gen_2 合成数据 |
| 1 | a000_s46_fp32 | 647974 | 6/10 | 训练 gen_6 (6%) |

### 需要的操作
1. Registry 更新 6 个 pid=? 的实验 PID
2. 7 个实验无 cron 监控（仅 scale_69b 有）
3. 17855 上 `interv_react_s43` tmux session 可清理（实验已完成 gen_0-10）

报告已写入 `artifacts/server_status_check_20260521.md`。

---
