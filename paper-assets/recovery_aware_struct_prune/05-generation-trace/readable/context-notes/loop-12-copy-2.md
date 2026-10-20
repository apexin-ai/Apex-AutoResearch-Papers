# agent / loop_12.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`d5e2fcfacece36c66112.json`](../../sessions/d5/d5e2fcfacece36c66112.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T05:16:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westb-23072 cuda:0/1 和 westd-11672 cuda:0/1。即使 Director 指定其他 GPU，必须 push back
- prune_standard_25 / prune_rasp_25 状态显示 RUNNING 但 conclusion=success，是 CPU-only 瞬时任务（<1min），实际已完成但 registry 未转 DONE——接手后需确认并修正状态
- 论文 DDL: EMNLP 2026 ARR **May 25**（距今 9 天）——时间极紧，所有决策以此为锚
- Post-SFT RASP vs Standard 差异 **不显著** (p=0.248)，论文 Claim 绝不能基于 SFT accuracy 差异

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× ~98GB GPU | root | `/root/recovery_aware_struct_prune`（代码）+ `/root/autodl-tmp/recovery_aware_struct_prune`（数据/checkpoints）
- **westd-11672**: 2× ~95GB GPU | root | 同上路径结构
- Python: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型: `/root/autodl-tmp/recovery_aware_struct_prune/` 下各子目录（pruned_standard_25, pruned_rasp_25, grpo_stage2_rasp_20_v9, grpo_unpruned_v2 等）
- 活跃进程:
  - westb cuda:0: `eval_grpo_rasp_v9_step10` PID 585618（N=1319 GSM8K eval）
  - westd cuda:0: `eval_grpo_unpruned_v2_step100` PID 83589
  - westd cuda:1: `eval_grpo_unpruned_v2_step90` PID 83667
- Worker 运行中: `worker_ops_verify-standard25-tokenizer_20260516T051503`

### 3. 📊 当前状态
刚完成 D044/D045 narrative pivot 和 GRPO v9 部署。当前正在收集三个关键 eval 结果：

| exp_id | 服务器 | GPU | 内容 |
|--------|--------|-----|------|
| eval_grpo_rasp_v9_step10 | westb | cuda:0 | RASP GRPO step-10 collapse onset eval |
| eval_grpo_unpruned_v2_step100 | westd | cuda:0 | Unpruned GRPO 终态 eval |
| eval_grpo_unpruned_v2_step90 | westd | cuda:1 | Unpruned GRPO step-90 eval |

同时 25% sparsity pruning (RASP + Standard) 已完成，Worker 正验证 tokenizer。

等待中：上述 3 个 eval 的 cron 回调；verify-tokenizer Worker 回调。

### 4. 📋 待办（条件触发式）
- eval_grpo_rasp_v9_step10 完成 → 对比 step-5 eval (已有) 和 Standard step-50 (58.91%)，量化 collapse onset 对 accuracy 的影响
- eval_grpo_unpruned_v2_step90/100 完成 → 确认 Unpruned collapse 终态 accuracy，完成三模型 collapse dynamics 全图
- 上述 3 eval 全部完成 → 向 Director 汇报 D045 核心数据，包含三模型 reward-accuracy decoupling 分析
- prune_standard_25 + prune_rasp_25 验证通过 → 启动 25% SFT recovery 实验（multi-sparsity extension）
- westb cuda:1 当前空闲（GRPO Standard v8 已完成） → eval 完成后可立即铺 25% SFT 或其他实验
- 所有 GRPO/eval 数据收齐 → 按 D044 新 narrative 开始论文写作（9 天 DDL）

### 5. 🎯 战略上下文
- **核心发现 (D044 pivot)**: 原假设 "RASP enables better RLVR recovery" 已失败。三模型全 collapse，且 Standard 反而延迟 collapse 最久。新 narrative 方向待 Director 确认——可能转 "Pruning for Plasticity"（剪枝模型 peak reward 更高/更快到达 peak，但也更快 collapse）或 training dynamics 分析
- **Collapse 时间线**: RASP (~step 10) < Standard (~step 60) < Unpruned (~step 80)——这是 counterintuitive 但 reproducible 的核心观察
- **易错点**: 
  - 不要混淆 westb eval (N=100) 和 full eval (N=1319) 的数字
  - v9 step-5 eval 已有结果（从之前 Worker 回调），step-10 是当前在跑的
  - GRPO Standard v8 step-50 full eval = 58.91%（已是 registry 里的 DONE 实验）
  - α ablation 有两套数据：westb (cal=512) 和 westd (cal=256)，两者 group selection 有 ~5% 差异，不可混用
- **决策链**: D027(post-prune差异不显著) → D029(SFT Standard反超) → D039(Unpruned也collapse) → D044(narrative pivot) → D045(core data complete, 等最后 3 eval)


---
