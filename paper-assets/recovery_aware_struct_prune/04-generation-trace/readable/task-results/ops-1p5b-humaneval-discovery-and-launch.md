# ops 1p5b humaneval discovery and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_1p5b_humaneval_discovery_and_launch_20260519T112624_result.json`
- **Structured JSON:** [`37056b66c93919c1a029.json`](../../sessions/37/37056b66c93919c1a029.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件大小完全匹配。4 个 checkpoint 已就绪，2 个评估在跑，2 个 SFT 还在传输。

汇总：

**Checkpoints 定位**（全部 6 个在 westb-23072，已传/传输中到 westd-29022）：

| Checkpoint | 路径 (westd) | 大小 | 状态 |
|---|---|---|---|
| sft_cka_only_20_1p5b | `/root/autodl-tmp/.../sft_cka_only_20_1p5b` | 2.77GB | 已传输，**评估运行中** (cuda:1) |
| grpo_cka_only_20_1p5b | `/root/autodl-tmp/.../grpo_cka_only_20_1p5b` | 2.77GB | 已传输，**评估运行中** (cuda:2) |
| grpo_standard_20_1p5b | `/root/autodl-tmp/.../grpo_standard_20_1p5b` | 2.79GB | 已传输，待启动 |
| grpo_rasp_20_1p5b | `/root/autodl-tmp/.../grpo_rasp_20_1p5b` | 2.77GB | 已传输，待启动 |
| sft_standard_20_1p5b | `/root/autodl-tmp/.../sft_standard_20_1p5b` | 2.77GB | 传输中 (~16%) |
| sft_rasp_20_1p5b | `/root/autodl-tmp/.../sft_rasp_20_1p5b` | 2.77GB | 传输队列中 |

**已启动实验（cuda:1 & cuda:2）：**
- `eval_humaneval_sft_cka_only_20_1p5b_2048` → cuda:1, PID 95940
- `eval_humaneval_grpo_cka_only_20_1p5b_2048` → cuda:2, PID 96018

两个评估已成功加载模型并在运行 HumanEval。1.5B 模型在 RTX PRO 6000 上预计 30-60 分钟完成 164 题。

**待启动（grpo_standard 和 grpo_rasp 已就绪）：** 可用 cuda:0/cuda:3 启动，或等 cuda:1/2 空闲后复用。sft_standard 和 sft_rasp 的传输约 20-30 分钟后完成。

**Registry 状态：** 全部 6 个实验已注册（含 hypothesis）。前两个 RUNNING，后四个 PREPARING。

---
