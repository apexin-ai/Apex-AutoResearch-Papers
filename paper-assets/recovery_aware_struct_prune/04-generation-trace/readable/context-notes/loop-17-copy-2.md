# agent / loop_17.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`1f3a69eabf69b424a608.json`](../../sessions/1f/1f3a69eabf69b424a608.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-17T17:41:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westb-23072 cuda:0/1, westd-11672 cuda:0/1/2/3（共 6 张）。不得使用白名单外 GPU，即使 Director 指令也要 push back
- **EMNLP ARR May 25 DDL**: 距今 ~8 天，25% GRPO + scoring ablation + paper writing 必须并行
- **eval_math500 GRPO 模型超时问题**: GRPO 模型生成极长推理链（~112s/problem），MATH-500 eval 必须去掉 timeout wrapper 或用足够大的 timeout_hours，否则反复 fail（v1/v2 均因此失败，v3 已去掉 timeout）
- **D051 裁定**: MATH-500 GRPO RASP vs Standard 对比因配置不公平**不可用于 C3 论证**
- **D052 裁定**: C3 降级为 observation，C2 collapse gradient 升为主力贡献
- **D053 (provisional)**: CKA-only GRPO 如果最稳定，可能重构 "Redundancy-Stability Tradeoff" narrative
- **submit_training_job 命令必须自带环境激活**: `bash -c "source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && ..."`
- **GPU 编号始终从 0 开始**（框架自动映射物理 GPU）

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× ~98GB GPU, 工作目录 `/root/recovery_aware_struct_prune`, 数据/模型 `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westd-11672**: 4× ~95GB GPU（本项目分配全部 4 张）, 同上路径结构
- **Python**: `/root/miniconda3/bin/python`（两台服务器均通过 `source /root/miniconda3/bin/activate` 激活，不走 conda activate）
- **关键模型路径**:
  - Unpruned: `/root/autodl-tmp/recovery_aware_struct_prune/qwen2.5_3b_instruct`
  - SFT checkpoints: `sft_rasp_20`, `sft_standard_20`, `sft_cka_only_20`, `sft_random_20` 等（同目录下）
  - GRPO checkpoints: `grpo_stage2_rasp_20_v9`, `grpo_stage2_standard_20_v8/checkpoint-50`, `grpo_cka_only_20`(训练中), `grpo_random_20`(训练中)
- **W&B**: run_name 对应 exp_id，project 为 `recovery_aware_struct_prune`
- **活跃进程**:
  - `grpo_cka_only_20`: PID 725227, westb cuda:0, tmux session
  - `grpo_random_20`: PID 719679, westb cuda:1, tmux session
  - `eval_humaneval_grpo_standard_20_2048`: PID 27194, westd cuda:2, tmux session
  - `eval_math500_grpo_rasp_20_v3`: PID 31706, westd cuda:3, tmux session
  - `eval_humaneval_sft_standard_20_2048_v2`: PID 36724, westd cuda:0, tmux session
  - `eval_math500_grpo_standard_20`: westd cuda:1（cron reconcile 确认 PID 14556 still running）
- **活跃 cron**: eval_math500_grpo_standard_20, grpo_random_20, eval_humaneval_grpo_standard_20_2048（reconcile 确认均 still running）
- **磁盘**: westb `/autodl-pub` 7T/14T 可用; westd `/autodl-pub` 5.3T/7.3T 可用。充裕

### 3. 📊 当前状态
**6 个实验 RUNNING，5/6 GPU 在用，westd cuda:1 空闲**（eval_math500_grpo_standard_20 registry 显示 RUNNING 但 GPU 未明确标记——reconcile 确认 PID 14556 alive，需确认它绑定的是哪张卡）。

**刚完成的关键实验**:
- `sft_cka_only_20` (success): CKA-only 20% post-SFT GSM8K = **64.0%** (N=200)，是所有方法中最高，比 RASP 61.49% 高 ~2.5pp
- `eval_humaneval_unpruned_2048` (success): unpruned HumanEval@2048 基线已有
- `eval_humaneval_sft_rasp_20_2048` (success): SFT RASP HumanEval@2048 = 10.37%
- `eval_humaneval_grpo_rasp_20_2048` (failed): EXIT_CODE=129，需要诊断
- `eval_math500_grpo_rasp_20_v2` (failed): timeout，v3 已重提交（去掉 timeout wrapper）

**正在等待的回调**:
- `grpo_cka_only_20` 完成 → **D053 关键数据点**：如果 CKA-only GRPO 不 collapse（或 collapse 远晚于 RASP），则 "去掉冗余=伤 RL" 的 narrative 被推翻，需要重构为 "保留冗余=稳定 RL"
- `grpo_random_20` 完成 → collapse 行为决定 C2 gradient 叙事（random collapse 位置 = RASP/Standard/中间 哪个？）
- `eval_math500_grpo_standard_20` 完成 → C1 cross-benchmark 验证
- `eval_math500_grpo_rasp_20_v3` 完成 → C1 RASP 侧 MATH-500 数据
- `eval_humaneval_grpo_standard_20_2048` 完成 → HumanEval 矩阵
- `eval_humaneval_sft_standard_20_2048_v2` 完成 → HumanEval 矩阵

**Worker 池 = 0**（⚠️ 违反 L1 红线"Worker 池 < 2 = 失职"）。下一个 session 应立即派 Worker 处理待办任务。

**18 个 PREPARING 实验** 等待调度，包括 scoring ablation 全套、25% eval、unstructured pruning、Qwen Math pipeline 等。

### 4. 📋 待办（条件触发式）
- `grpo_cka_only_20` 完成 → 读 W&B collapse dynamics（frac_zero_std、reward 曲线），与 RASP step~10 / Standard step~60 对比 → 更新 D053 → 汇报 Director。**如果 CKA-only 最稳定，narrative 从 "redundancy removal hurts RL" 强化为 "redundancy = RL stability buffer"**
- `grpo_random_20` 完成 → 同上分析 collapse timing → 四方对比（Random / CKA-only / Standard / RASP）完成 C2 collapse gradient 完整证据链
- `eval_math500_grpo_standard_20` + `eval_math500_grpo_rasp_20_v3` 均完成 → 对比两者 + 对比各自 SFT baseline → 更新 C1 cross-benchmark 证据
- `eval_humaneval_*_2048` 系列全完成 → 汇总 5-way HumanEval@2048 矩阵（unpruned / SFT RASP / SFT Standard / GRPO Standard / GRPO RASP）
- westd cuda:1 空闲 → 立即从 PREPARING 队列中提交下一个 eval（优先 `eval_sft_standard_25` 或 `eval_postprune_25`）
- GRPO random + CKA-only 均完成后 → 所有 4 种 scoring 的 GRPO collapse 数据齐全 → 可以画 Figure 2（collapse dynamics 对比图）→ 派 paper-writing Worker
- Paper Agent Step 2 (Plot Generation) 需要推进 → 派 Worker 生成关键 figures

### 5. 🎯 战略上下文
**核心结论链**:
- D044: Major narrative pivot → "RASP enables better RLVR recovery" 被推翻，转为 "universal decoupling + collapse gradient"
- D045: Core 20% data complete，3 claims fully supported
- D048: C3 reframe 为 observation（SFT marginal advantage p=0.25 不显著）
- D052: C2 collapse gradient 升为主力贡献，C3 降级
- D053 (provisional): 等 grpo_cka_only_20 + grpo_random_20 结果定论

**最容易判断错的事**:
1. **不要把 CKA-only post-prune 优势（38.5% vs 19%）外推为 "CKA-only 是最优方法"** — SFT equalizing effect 会缩小差距（64% vs 61%），GRPO collapse 行为才是关键判别器
2. **eval_humaneval_grpo_rasp_20_2048 的 EXIT_CODE=129 是 SIGKILL（OOM 或被系统 kill）**，不是代码 bug — 重提交时注意 GPU 内存，GRPO 模型 + 2048 tokens 可能比 SFT 占更多显存
3. **MATH-500 eval 对比需注意公平性** — D051 已裁定 RASP vs Standard GRPO MATH-500 不可用于 C3（配置差异）。只能用于 C1（GRPO vs 同方法 SFT 对比）
4. **Paper writing 不能等所有实验** — 20% core data 已齐全，先用 20% 写主体，25%/scoring ablation/Qwen Math 作为 patch 后续插入
5. **距 DDL 8 天** — 25% GRPO（2 个实验）+ Qwen Math full pipeline + scoring ablation 剩余 + paper draft 必须全部并行，不能串行。GPU 预算约 192 GPU-hours 剩余（4 GPU × 48h），GRPO 训练每个约 6-8h，eval 每个 1-4h，时间紧但可行


---
