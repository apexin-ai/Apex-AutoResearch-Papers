# reviewer / loop_18.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`84fefa02bf771a086447.json`](../../sessions/84/84fefa02bf771a086447.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-22T18:21:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-47453 白名单**: GPU [0,1,2,3]。seed100 v2 用 0,1；seed200 用 2,3。
- **bjb1-17606 白名单**: GPU [0,1]。seed300 OOD eval 在 GPU 0。
- **seed100 原始训练数据已丢失**：v1 checkpoint 在磁盘清理中被删，v1 日志被 v2 覆盖（原文件 seed100_episode_grpo.log）。v1 的 step 1-4 指标只存在于之前的 reviewer 报告和 W&B run `zsrodv2f` 中。不要引用 seed100 v1 数据作为有效实验结果。
- **bjb1 数据盘紧张**: `/root/autodl-tmp` 89% (29GB free)，ray session 仍报 >95% full。清理后 FSDP checkpoint `exp029-seed300` 已删除，仅保留 HF 版本。
- **统一 OOD eval 管线**: seed.val=321, enable_response_mask=false, 134 OOD tasks (AlfworldSG_OOD), T=0.4, val_only=True, enable_think=False。偏离任一参数 → 数据不可比。

### 2. 🖥️ 基础设施快照
- **westd-47453**: `/root/cost-verify-agent-rl/RAGEN`，conda base (`/root/miniconda3/bin/python`)
  - seed100 v2: PID 78400/78937/78938, log `/root/autodl-tmp/logs/seed100_episode_grpo_v2.log`, W&B `zsrodv2f`(v1,已死) / v2 run ID 待确认
  - seed200: PID 66207/66567/66568, log `/root/autodl-tmp/logs/seed200_episode_grpo.log`, W&B `z7e85fie`
- **bjb1-17606**: `/root/cost-verify-agent-rl/RAGEN`，conda base
  - seed300 OOD eval: PID 441087/441259, log `/root/autodl-tmp/logs/seed300_step5_ood_eval.log`, W&B `z1qs706b`
  - 旧 seed300 训练进程 PID 433097 仍在 CPU 层面运行（zombie-like）
  - HF checkpoint: `/root/autodl-tmp/checkpoints/qwen_exp029_seed300_step5_hf/` (3.8GB)
  - SFT base: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- **W&B**: entity `xiaoyucorynne-`, project `cost-verify-agent-rl`

### 3. 📊 当前状态
最后一次巡检 (~02:25 UTC)：
- **seed100 v2** (westd GPU 0,1): step 1 训练中，~27min elapsed，仅有 step 0 val (6.25%)。FSDP 间歇期 0% compute / 44-45GB。
- **seed200** (westd GPU 2,3): step 1 训练中，~35min elapsed，仅有 step 0 val (6.25%)。两者 step 1 即将完成。
- **seed300 OOD eval** (bjb1 GPU 0): 运行 ~27min，日志仅磁盘警告无结果。eval 进程活跃 (96% CPU)。预计 2-3h 出结果。
- **bjb1 GPU 1 完全空闲**。
- **Registry 问题**: `exp029_seed300_episode` 卡在 ANALYZING 状态，analysis worker 完成但未写入 metrics/conclusion。已报告 Director。

### 4. 📋 待办（条件触发式）
- seed200 step 1 指标出现 → 提取 train_success / response_length / entropy，检查 collapse 信号（response_length +50% 或 success 下降 → warning）
- seed100 v2 step 1 指标出现 → 同上，特别关注是否复现 v1 的 early collapse（v1 step 1: success 19.5%, resp_len 2017 → step 4: success 12.5%, resp_len 3921）
- seed300 OOD eval 出 step:0 结果 → 提取 success rate，>20% 确认 healthy，<15% 意外需要深查
- seed100/200 任一完成全 5 步 → 检查 checkpoint 保存 + 触发 OOD eval
- bjb1 GPU 1 空闲时间 >1h → 提醒 Director 安排任务（如 response_mask ablation `exp029_seed5_response_mask_check`）

### 5. 🎯 战略上下文
- **核心问题**: Episode-level GRPO 的 collapse rate 是多少？当前 N=7 seeds 中 4 collapsed (57%)，正在扩展到 N=10 (seed100/200/300)。
- **seed300 训练已确认 healthy**: val 12.5%→25%，无 response inflation，等 OOD eval 入 Table 1。
- **seed2 是 "delayed learner" (D130)**: 15.67% OOD，介于 collapsed (8-13%) 和 healthy (25-31%) 之间，单独分类。
- **ScienceWorld Cell C 已终止 (D131)**: 4 次尝试全失败，诚实承认 limitation。
- **三层证据层级 (D128)**: Primary (sign accuracy) → Secondary (factorial) → Supplementary (intervention)。
- **易错点**:
  - GPU 0% compute + 高 memory ≠ 异常，是 FSDP step 间正常同步
  - seed100 有 v1 和 v2 两个版本，v1 数据不可用（checkpoint 和原始日志均丢失）
  - `exp029_seed300_step5_hf` 和 `qwen_exp029_seed300_step5_hf` 可能是重复 checkpoint，后者是 OOD eval 使用的
  - Table 1 中 seed1 (23.88%) 使用非统一管线，checkpoint 已丢失无法重测——必须在论文中标注或排除


---
