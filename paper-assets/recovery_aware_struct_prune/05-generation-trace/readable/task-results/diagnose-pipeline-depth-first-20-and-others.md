# diagnose pipeline depth first 20 and others

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pipeline_depth_first_20_and_others_20260522T111057_result.json`
- **Structured JSON:** [`ae551c5ea0f593930aaa.json`](../../sessions/ae/ae551c5ea0f593930aaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：3 个实验均未失败，全部是 reconcile 误报

---

**1. pipeline_depth_first_20 (cuda:3)** — **仍在运行**

- 当前状态：Phase 4 (eval_gsm8k on grpo_depth_first_20)，GSM8K 16/1319
- PID 从 36167（parent bash）变为 40073（eval 子进程），reconcile 追踪的是旧 PID
- Phase 2 (SFT) → Phase 3 (GRPO 100/100 steps) 均已完成，GRPO 模型已保存
- GPU 3 占用 16234MiB，利用率 97%

**2. eval_math500_grpo_standard_20_fair_2048_v2 (cuda:0)** — **正常完成**

- 完成时间：2026-05-22 19:01:57
- 结果：**MATH-500 Acc = 0.2640 ± 0.0197 (132/500)**
- 结果已保存至 `/root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json`
- GPU 0 已释放（0MiB）
- 未写 sentinel 文件 → reconcile 认为进程异常退出

**3. grpo_random_20_seed123 (cuda:2)** — **正常完成**

- 完成时间：2026-05-22 19:02:13
- GRPO 100/100 steps 完成，模型已保存至 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123`
- W&B run: `grpo_sft_random_20` (run ID: `1silchcm`)
- sentinel 文件只有 `grpo_random_20.exit`（5/21 旧的），无 `grpo_random_20_seed123.exit` → reconcile 匹配不到
- GPU 2 已被新任务 `eval_gsm8k_sft_alpha3p0_20` (PID 37026) 接管

---

### 共同根因

**Reconcile 系统误报**，不是实验失败。三个 false alarm 的原因：

| 实验 | 误报原因 |
|------|----------|
| pipeline_depth_first_20 | 多阶段 pipeline 子进程 PID 与 reconcile 追踪的父 PID 不同 |
| eval_math500 | Eval 脚本未写 sentinel 文件 |
| grpo_random_20_seed123 | sentinel 文件名带 seed 后缀，与已有 sentinel 不匹配 |

### 磁盘警告

数据盘 `/root/autodl-tmp` 使用率 **98%**（636G/650G，仅剩 15GB）。pipeline_depth_first_20 后续还有 Phase 5（eval SFT）要跑，可能需要注意空间。

### 行动

- 无需重试任何实验
- 两个已完成的实验结果可直接使用
- pipeline_depth_first_20 正在跑，等它自然完成即可

---
