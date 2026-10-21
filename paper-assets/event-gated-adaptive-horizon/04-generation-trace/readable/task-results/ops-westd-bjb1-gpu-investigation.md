# ops westd bjb1 gpu investigation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_bjb1_gpu_investigation_20260525T173621_result.json`
- **Structured JSON:** [`2baccdd95deb61571fc4.json`](../../sessions/2b/2baccdd95deb61571fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。汇总如下：

---

## westd-19154 cuda:0 — 发现 orphan 进程

cuda:0 上有 **两个相同的 exp_086 python 进程**：

| PID | 启动时间 | 身份 | GPU 内存 |
|-----|---------|------|---------|
| 37174 | 00:49:33 | **旧的 exp_086**（未被清理的前一次提交） | 3223 MiB |
| 37520 | 00:51:21 | **新的 exp_086**（pid=37515 的子进程） | 3223 MiB |

重提交 exp_086 时旧进程 (37174) 未被 kill，两个进程同时跑在 cuda:0 且写入同一个 logdir，存在 **metrics.jsonl 数据污染风险**。这就是 system 报告的 57% 利用率未注册进程来源。

**建议：kill 旧进程 pid=37174（及其父 37173）**，但等 Director 确认。

---

## bjb1-45299 — 低利用率属正常

当前 GPU 快照：cuda:0 = 7%, cuda:1 = 22%。两个实验进程确认正常运行，无 orphan。

低利用率原因：DreamerV3 交替执行 CPU 环境步（MuJoCo）和 GPU 训练步。frozen dt_emb + 小型 proprio 观测空间（Walker 24维）→ 每步 GPU 计算量很轻，大部分时间花在 CPU 环境仿真上。这是正常行为，不是瓶颈。

---

## 4 个 frozen 实验当前状态

| 实验 | 服务器 | 当前 step | FPS | 最近 eval_return | 目标 |
|------|--------|----------|-----|-----------------|------|
| exp_086 (Cheetah s0) | westd cuda:0 | ~32k | 9.5 | 146.8 @25k | 105k |
| exp_087 (Cheetah s1) | westd cuda:1 | ~60k | 14.0 | 207.2 @55k | 105k |
| exp_084 (Walker s0) | bjb1 cuda:0 | ~48k | 9.5 | 312.7 @45k | 105k |
| exp_085 (Walker s1) | bjb1 cuda:1 | ~48k | 9.8 | 200.4 @45k | 105k |

exp_086 进度落后（32k vs 其他 48-60k），且因 orphan 进程抢 GPU 资源，FPS 和 exp_087 差距大（9.5 vs 14.0）。清理 orphan 后 FPS 应回升。

---
