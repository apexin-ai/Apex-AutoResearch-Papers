# monitor v9d detailed status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9d_detailed_status_20260520T000318_result.json`
- **Structured JSON:** [`ed024ae8074e95f9cc21.json`](../../sessions/ed/ed024ae8074e95f9cc21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### 阶段: Step 0/30 — 刚进入训练循环

- **val_before_train 已完成**（耗时 177s），初始指标：
  - `success`: **40.625%** (32 episodes, 满足 ≥16 要求)
  - `pass@1`: 40.625%
  - `action_is_valid`: 92.3%
  - `response_length`: 1813.6
- 日志最后一行: `Training Progress: 0%| | 0/30` — 正在执行第 1 个 training step

### GPU 状态 (4x RTX PRO 6000 96GB)

| GPU | 显存占用 | 利用率 | 温度 |
|-----|---------|--------|------|
| 0 | 1259/97887 MiB | 0% | 34°C |
| 1 | 1259/97887 MiB | 0% | 32°C |
| 2 | 1259/97887 MiB | 0% | 33°C |
| 3 | 1259/97887 MiB | 0% | 33°C |

每张卡上都有 `ray::WorkerDict` 进程。GPU util 0% 是快照瞬时值——vLLM 在 rollout 时动态加载权重，当前可能处于 step 0 的数据准备 / CPU 计算阶段。

### 进程 & W&B
- PID 279579 正常运行（启动于 07:57）
- Ray 集群完整：4 个 WorkerDict + 1 个 TaskRunner (71% CPU) + ~30 个 IDLE worker
- W&B run `gl7zu17e` 活跃，日志文件 360KB 且持续增长

### Checkpoint
- 保存目录 `/root/autodl-tmp/checkpoints/8b-cell-c/` 存在但为空（save_freq=5, step 0 尚未产出 checkpoint）
- 无 `8b-cell-c-v9` 子目录，checkpoint 可能直接写入 `8b-cell-c/`

### 时间估算
- 启动 07:57 → val 完成 08:01 → 当前 08:03，训练刚开始约 2 分钟
- 30 步 GRPO + 8B 模型 + 4 GPU，预计总训练时间 **3-6 小时**（取决于 rollout 长度和 batch size），大约在 11:00-14:00 完成

---
