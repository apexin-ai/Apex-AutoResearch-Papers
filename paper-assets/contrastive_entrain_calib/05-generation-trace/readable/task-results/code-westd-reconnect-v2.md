# code westd reconnect v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-reconnect-v2_20260525T042628_result.json`
- **Structured JSON:** [`23426ee0319902e14e1e.json`](../../sessions/23/23426ee0319902e14e1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动，正在跑 seed3/checkpoint-2000（362 pairs）。

---

## 汇总

### 连接状态
- **westd-29046 连接成功**

### GPU 状态
- 2x NVIDIA RTX PRO 6000 Black (98GB each)
- 两块 GPU 均空闲，无 Python 进程（eval 中断后未恢复）
- eval 恢复脚本已启动在 cuda:0，PID=1729

### Checkpoint 完好性

| 实验 | Checkpoints | 状态 |
|------|------------|------|
| exp008_sft_seed42 (seed2) | 500, 1000, 1500, 2000, final | 全部存在 |
| exp008_sft_seed43 (seed3) | 500, 1000, 1500, 2000, final | 全部存在 |
| exp003_r3only_seed1 | 500-8000 (每500一个) + final | 全部存在 (17个) |
| exp003_r3only_seed2 | 500-8000 (每500一个) + final | 全部存在 (17个) |

### Eval 进度

| Seed | Checkpoint | Eval | Entropy |
|------|-----------|------|---------|
| seed2/500 | done | done | done |
| seed2/1000 | done | done | done |
| seed2/1500 | done | done | done |
| seed2/2000 | done | done | done |
| seed2/final | done | done | done |
| seed3/500 | done | done | done |
| seed3/1000 | done | done | done |
| seed3/1500 | done | done | done |
| seed3/2000 | **running** (PID=1729) | — | — |
| seed3/final | pending | — | — |

### 已启动任务
- **PID 1729**: seed3 恢复 eval（checkpoint-2000 + final），cuda:0
- 日志: `/root/autodl-tmp/results/exp008_seed3_resume_eval.log`
- 预计耗时：~70 min（每个 checkpoint ~35min）

### Seed4 并行可行性
- 每块 GPU 98GB，eval 占用约 20GB（Qwen3-8B + LoRA + NLI）
- cuda:1 完全空闲，**可以并行启动 seed4 训练**（~20GB）无冲突
- 也可在 cuda:0 上 eval 完成后复用

### 磁盘
- `/root/autodl-tmp/`: 250GB 总量，90GB 已用，161GB 可用 (36%) — 充足

### exp-003-len512-v3
- exp003_r3only_seed1 和 seed2 的 checkpoint 均完好（各 17 个 checkpoint + final）

---
