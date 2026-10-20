# monitor grpo v8 early check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo-v8-early-check_20260515T150447_result.json`
- **Structured JSON:** [`abd0ddf92fc5abf492fe.json`](../../sessions/ab/abd0ddf92fc5abf492fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRPO v8 早期信号检查报告

### 进程状态：✅ 两个实验都在运行

| 实验 | PID | Step | Speed | Uptime | ETA |
|------|-----|------|-------|--------|-----|
| **RASP v8** | 532861 | 3/100 | ~400s/step | 31min | ~10.8h |
| **Standard v8** | 534667 | 2/100 | ~411s/step | 22min | ~11.2h |

### GPU 状态：✅ 正常
| GPU | VRAM | Utilization |
|-----|------|-------------|
| cuda:0 (RASP) | 72GB / 98GB | 100% |
| cuda:1 (Standard) | 72GB / 98GB | 100% |

### WandB 指标：⏳ 尚无训练指标
- `logging_steps=10`，当前 step 2-3，首次指标日志预计在 **step 10**（RASP ~47min 后，Standard ~55min 后）
- wandb run 存活，已记录系统指标（_step=83/55），但 reward/grad_norm/loss 尚未到首次记录点

### 磁盘状态：⚠️ WARNING
| 分区 | 使用率 | 可用空间 |
|------|--------|----------|
| 根分区 /root | 29% | 22GB ✅ |
| 数据盘 /root/autodl-tmp | **89%** | **29GB** ⚠️ |

**风险：** sft_rasp_20 和 sft_standard_20 各占 81GB（共 162GB）。`save_steps=50` 且 `save_only_model=false`，每个 checkpoint 约 18-24GB。step 50 时两个实验几乎同时保存，**29GB 不够存两个 checkpoint，第二个会因磁盘满失败**（v7 崩溃根因重现）。

### 建议操作（step 50 前必须执行之一）
1. 清理旧 GRPO v1-v7 空目录 + 不需要的文件释放空间
2. 或设置 `save_only_model=true` 减小 checkpoint 体积（需重启训练）
3. 或将其中一个 SFT 模型移到其他位置（两者共 162GB）

### 下次检查时间
- **Step 5 check**（~33min 后）：确认 wandb 有无异常系统指标
- **Step 10 check**（~47min 后）：首批训练指标可用，验证 reward>0 和 grad_norm>0

---
