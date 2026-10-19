# diag v2 training status all

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_v2_training_status_all_20260516T135736_result.json`
- **Structured JSON:** [`c1e300dd814a2af05f36.json`](../../sessions/c1/c1e300dd814a2af05f36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 状态汇总

### nvidia-smi (21:57:50)

| GPU | 显存占用 | 利用率 | 当前进程 |
|-----|----------|--------|----------|
| 0 | 8280MiB / 97887MiB | 86% | PID 826346 (python3) — **非原训练进程** |
| 1 | 7966MiB / 97887MiB | 0% | PID 826873 (python, torch.compile中) — **非原训练进程** |
| 2 | 1MiB / 97887MiB | 0% | 空闲 |
| 3 | 1MiB / 97887MiB | 0% | 空闲 |

### 训练任务状态

| exp_id | status | final_step | final_loss | last_checkpoint | error |
|--------|--------|-----------|------------|-----------------|-------|
| v2_lora_visual_r16 | **已停止** (killed) | 6500/10000 | 0.7436 | step_6000 | 进程在 21:47 被外部终止，EXIT_CODE=0 |
| v2_lora_physical_r16 | **已停止** (killed) | 6450/10000 | 0.7355 | step_6000 | 进程在 21:47 被外部终止，EXIT_CODE=0 |
| v2_lora_universal_r16 | **已停止** (killed) | 4950/10000 | 0.7695 | step_4000 | 进程在 21:47 停止输出，无 traceback |
| v2_lora_spatial_r16 | **崩溃** | 2000/10000 | 0.8379 | step_1000 | `No space left on device` — 根分区满，save_pretrained 失败 |

### 关键发现

1. **所有原始训练进程（PID 665119/665199 等）均已不存在**
2. **visual/physical/universal 三个任务在 ~21:47-48 同时停止**，推测被同一操作 kill（可能是占用 GPU 0/1 的新进程启动前清理的）
3. **spatial 最早崩溃**（20:54），原因是根分区磁盘满（当前 27G/30G = 88%）
4. **Checkpoint 保存在两个位置**（根分区 + autodl-tmp），内容一致

### 磁盘

```
/           30G  27G  3.8G  88%
/root/autodl-tmp  250G  76G  175G  31%
```

### 需要恢复的工作

- visual: 从 step_6000 恢复，还需跑 4000 步
- physical: 从 step_6000 恢复，还需跑 4000 步
- universal: 从 step_4000 恢复，还需跑 6000 步
- spatial: 从 step_1000 恢复，还需跑 9000 步（且需修复 checkpoint 保存路径到 autodl-tmp，或清理根分区空间）

---
