# agent / loop_21.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`a2c3b42f8f0b2f5e6487.json`](../../sessions/a2/a2c3b42f8f0b2f5e6487.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: idle_timeout
updated: '2026-05-21T23:53:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westb-23072 cuda:0/1, westd-29022 cuda:0/1/2/3
- **westd-29022 网络离线**：所有实验命令必须带 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`，否则 HF datasets 发 HEAD 请求导致崩溃（已有 5+ 次 MBPP eval 因此失败）
- westb 上 SFT RASP 20% 模型路径是 `sft_rasp_20_1p5b`，不是 `sft_rasp_20`
- grpo_cka_only_25 的正确 checkpoint 在 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25`（根目录，不是 checkpoint-100 子目录），v1/v2 都因路径错 failed
- submit_training_job 的 command 必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 投稿目标 EMNLP 2026 ARR May 25，**剩 ~4 天**

### 2. 🖥️ 基础设施快照
- **westb-23072**: 2× RTX PRO 6000, 23GB free, 工作目录 `/root/recovery_aware_struct_prune`, Python `/root/miniconda3/bin/python`
- **westd-29022**: 4× RTX PRO 6000, ~21GB free（实验完成后需清理 dense 15G + old ckpt 12G → 释放 ~27GB）, 同上路径结构
- 模型/数据: `/root/autodl-tmp/recovery_aware_struct_prune/` 下各 checkpoint
- conda 环境: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃进程:
  - westb cuda:0: eval_math500_sft_standard_25_v2 (PID 62714)
  - westb cuda:1: eval_gsm8k_grpo_standard_25 (PID 75282)
  - westd cuda:0: eval_gsm8k_grpo_cka_only_25_v3 (PID 322443)
  - westd cuda:1: eval_gsm8k_sft_cka_only_25 (PID 329698)
  - westd cuda:2: eval_gsm8k_sft_random_20 (PID 329770)
  - westd cuda:3: **空闲**
- Cron 监控: 5 个活跃 cron 对应上述 5 个 RUNNING 实验（reconcile 已确认全部进程存活）

### 3. 📊 当前状态
Loop #21 完成 session-start 初始化：read_registry + reconcile_crons + 补注册 eval_math500_sft_standard_25_v2（之前缺 registry 条目）+ 向 Director 汇报。5 个 eval 全部 RUNNING 等 cron 回调，无 Worker 在跑，无 Director 决策 pending。30 个 PREPARING 实验大部分历史遗留/低优先级。

### 4. 📋 待办（条件触发式）
- eval_gsm8k_grpo_cka_only_25_v3 完成 → **#1 优先级**：更新 registry + 对比 Standard 25% (51.1%) / RASP 25% (53.15%)。若 CKA-only > Standard → Table 3 cross-sparsity 行完成 → 汇报 Director → 更新论文
- eval_gsm8k_grpo_standard_25 完成 → 记录 GSM8K accuracy（预期极低，reward=0.008 near-collapse）→ 与 CKA-only 25% 对比放大 Δ
- eval_gsm8k_sft_cka_only_25 完成 → SFT baseline floor → 计算 SFT→GRPO recovery delta
- eval_gsm8k_sft_random_20 完成 → Random 20% SFT floor → Table 2 补充
- eval_math500_sft_standard_25_v2 完成 → MATH-500 补充数据点
- 所有 25% eval 完成 → 汇总 cross-sparsity 全景（15%/20%/25%）→ 更新论文 Table 3 → 向 Director 汇报是否摸到 3.5→4.0 天花板
- westd 当前 eval 完成后 → 磁盘清理（删 dense model 15G + old checkpoint 12G → 释放 ~27GB），不要中途操作

### 5. 🎯 战略上下文
- **核心结论**: CKA-only pruning 在 GRPO recovery 上显著优于 Standard（20%: +4.55pp p=0.0009, 15%: +7.20pp p<0.001）。25% 是补强数据点（Standard 已 collapse reward=0.008, CKA-only reward=0.2875）
- **决策链**: D087 否决 claim 升级保持 analysis paper → D090 保留 3-seed mean → D091 驳回 2-seed → D092 15% 三种子完成 → D093 25% 单种子 pilot → D094 Round 2 action matrix → D095 补强实验
- **审稿状态**: Round 3 得分 3.0/5, 34 issues 全部 resolved, 编译通过 ≤8 页。加入 25% 数据后 Reviewer 预期天花板 3.5, 有望 4.0
- **易错点**:
  - westd 离线——忘加 `HF_DATASETS_OFFLINE=1` 是最常见失败原因（每隔几轮就有人忘）
  - PREPARING 实验有 30 个但大部分历史遗留，不要盲目提交——只看 ROADMAP 近期任务
  - westd cuda:3 空闲但当前无高优先级 eval 可提交，已向 Director 请示
  - CKA scoring stability 已验证（ρ > 0.964），Reviewer 相关质疑可直接用数据回应


---
