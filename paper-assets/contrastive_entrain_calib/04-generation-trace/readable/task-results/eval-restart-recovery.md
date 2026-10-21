# eval restart recovery

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_restart-recovery_20260522T021002_result.json`
- **Structured JSON:** [`35d6a8614aa46cb96384.json`](../../sessions/35/35d6a8614aa46cb96384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### 已完成
- **Seed2 ckpt-4000**: 已在 GPU 1 上启动（PID 439037, 16.9GB VRAM），模型和 LoRA 加载完毕，正在 eval 362 pairs。Registry 新建条目 `exp-003-eval-s2-ckpt4000-v2` (RUNNING)。

### 阻塞：ACT ckpt-500/2000/8000
3 个 ACT eval 无法提交。原因：

- 原始 checkpoint 路径 `/root/autodl-tmp/outputs/exp-004-act-baseline/checkpoint-{500,2000,8000}` 在 **westd-28034** 上
- 当前服务器 **westd-29046** 的 `/root/autodl-tmp/` 下没有任何 exp-004 相关目录
- westd-29046 只有 `exp003_r3only_seed1` 和 `exp003_r3only_seed2` 的 checkpoints

### GPU 状态
| GPU | VRAM | 进程 |
|-----|------|------|
| 0 | 38GB/98GB | PID 237437 (未知任务) |
| 1 | 17GB/98GB | PID 439037 (seed2 ckpt-4000 eval) |

### 需要你确认
1. westd-28034 是否还能访问？需要从那边拷贝 ACT checkpoints 过来
2. 或者 ACT checkpoints 是否有其他副本/备份位置？

---
