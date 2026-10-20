# ops gpu and experiment check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-and-experiment-check_20260517T201050_result.json`
- **Structured JSON:** [`ae765b938e9aa84f76a7.json`](../../sessions/ae/ae765b938e9aa84f76a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有完整信息了。最后确认一下 ISR-s42 的 taxonomy 里 genuine 计算。按 C013 标准：genuine = proved - H7 - H1_exact - H8。

## GPU 状态

| GPU | 状态 | 备注 |
|-----|------|------|
| cuda:0 | **空闲** | 0MiB 占用，无进程（GPU-Util 显示 100% 但 Processes 空，疑为 driver 延迟/残留状态，实际无计算负载） |
| cuda:1 | **不存在** | 此服务器只有 1 张 RTX PRO 6000 Black (96GB) |

无 Python/训练进程在跑。GPU 空闲可用。

## 实验状态

所有 5 个 β=0.05 实验训练均已完成（500 步），eval 也已完成。

| 实验 | 训练 | Eval | PR | H7 | H1 | H8 | Genuine | ISR(mean) |
|------|------|------|-----|-----|-----|-----|---------|-----------|
| sweep-isr-b005-s42 | Done | Done | 55% | 55 (100%) | 0 | 0 | **0** (0%) | 0.76 (proved) |
| sweep-isr-b005-s43 | Done | Done | 99% | 96 (97%) | 0 | 0 | **3** (3%) | 0.55 |
| sweep-isr-b005-s44 | Done | Done | 99% | 86 (87%) | 0 | 10 | **3** (3%) | 0.55 |
| sweep-random-b005-s42 | Done (ckpt deleted) | Done | 0% | 0 | 0 | 0 | **0** (0%) | 0.0 |
| sweep-random-b005-s43 | Done | Done | 62% | 0 | 48 (77%) | 7 | **8** (13%) | 0.006 |
| sweep-random-b005-s44 | Done | Done | 7% | 0 | 5 (71%) | 2 | **0** (0%) | 0.0 |

### 关键观察

**ISR 侧：** 三个 seed 表现分裂。s42 完全坍缩（100% H7 = 全部 conclusion-in-premise 退化），s43/s44 也高度 H7 但有少量 genuine。ISR reward 很高（0.55-0.76）但几乎全是 gaming。

**Random 侧：** 高度不稳定。s42 完全崩溃（PR=0%），s43 表现最好（PR=62%，8 个 genuine），s44 也近乎崩溃（PR=7%）。

**结论：** 所有实验训练和 eval 均已完成。GPU 空闲，无待运行任务。

---
