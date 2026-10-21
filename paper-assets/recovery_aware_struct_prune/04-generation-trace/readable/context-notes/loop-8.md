# director / loop_8.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`a4123cf8536438537df1.json`](../../sessions/a4/a4123cf8536438537df1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-16T10:10:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westb-23072 cuda:0/1 + westd-11672 cuda:0/1（约束 C001）
- RASP-RLVR 是当前最高优先级实验（用户明确指示），GPU 排期优先于 25% GRPO 和 Qwen Math GRPO
- Calibration 不一致已决定不重跑（D046）：DeepSeek cal=512, Qwen-Math cal=256，论文加 footnote
- grpo_standard_25 已被降优先级，让位给 sft_rasp_rlvr_20 → grpo_rasp_rlvr_20

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com) + westd-11672 (connect.westd.seetacloud.com)，root 用户
- 工作目录：/root/recovery_aware_struct_prune（代码）+ /root/autodl-tmp/recovery_aware_struct_prune（模型/数据/输出）
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base）
- 模型缓存：/root/autodl-tmp/.hf_cache
- westb 磁盘：72GB 可用（刚清理过旧 GRPO checkpoints）
- 活跃进程（截至 handoff）：
  - westb cuda:0: eval_sft_rasp_25 (PID 602990, N=1319, ~103/1319, ETA 6-8h)
  - westb cuda:1: eval_sft_standard_25 (PID 598084, ~550/1319, ETA 1-2h)
  - westd cuda:0+1: 刚空出（Qwen Math SFT 完成），即将启动 Qwen Math eval

### 3. 📊 当前状态
刚批准 RESET_BOTH。Agent 队列深度 ~8，正在处理 RASP-RLVR 剪枝指令 + westd Qwen Math eval 启动指令。

**Registry RUNNING/PREPARING 关键条目：**
- eval_sft_rasp_25: RUNNING (westb cuda:0, 阻塞 grpo_rasp_25)
- eval_sft_standard_25: RUNNING (westb cuda:1)
- prune_rasp_rlvr_20: QUEUED → Agent 刚派 Worker
- sft_rasp_rlvr_20: PREPARING（等剪枝完成 + westb cuda:1 空出）
- grpo_rasp_rlvr_20: PREPARING
- eval_sft_rasp_qwen_math: PREPARING（urgent 指令已发，westd cuda:0）
- eval_sft_standard_qwen_math: PREPARING（westd cuda:1）
- grpo_rasp_25 / grpo_standard_25: PREPARING（25% GRPO，被 RASP-RLVR 降优先级）

**Paper Agent 状态：** Step 4 完成（全 6 章节 D045 叙事一致），已预写 RASP-RLVR 框架（Method §3.3 + Experiments §4.6），等数据 Patch 后进 Step 5。Provenance v36, coverage 28/28, 0 critical。

### 4. 📋 待办（条件触发式）
- eval_sft_standard_25 完成 → 记录结果 → 启动 sft_rasp_rlvr_20 在 westb cuda:1（最高优先级）
- prune_rasp_rlvr_20 完成 → 确认 pruning_metadata 合理（检查 F≈0 边界情况）→ 注册 DONE
- sft_rasp_rlvr_20 完成 → 启动 grpo_rasp_rlvr_20（同 GPU，save_steps=5, max_steps=100）
- eval_sft_rasp_25 完成 → 记录 25% RASP SFT accuracy → 启动 grpo_rasp_25
- Qwen Math eval 双卡完成 → 记录 accuracy → 启动 grpo_rasp_qwen_math + grpo_standard_qwen_math
- grpo_rasp_rlvr_20 完成 → 这是关键判断点：collapse onset > step 60? → 论文升级为 "diagnosis + remedy"；collapse 仍早 → 重新评估方法贡献 viability
- 25% eval 全部到齐 → 更新 paper_framing.md evidence table + 通知 Paper Agent Patch
- 所有 GRPO 完成 → Paper Agent 一次性 Patch（25% + RASP-RLVR + Qwen Math）→ 进 Step 5 Refinement

### 5. 🎯 战略上下文
- **核心叙事（D044/D045）**：GRPO reward-accuracy decoupling 是普遍现象；pruning 特有的是 training collapse；collapse severity 与 redundancy removal 正相关（Redundancy-Stability Tradeoff）
- **D047 升级**：RASP-RLVR（保护冗余）如果成功防止 collapse，论文从纯分析升级为 "diagnosis + remedy"，竞争力大增
- **最容易判断错的事**：eval_sft_rasp_25 速度极慢（8-10h for N=1319），不是 bug 而是模型生成长 response。不要反复 kill/重启，让它跑完
- **C3 风险**：20% SFT gap p=0.25 不显著。25% interim 数据显示 RASP 56.7% > Standard 53.4%（+3.3pp），如果完整 eval 仍不显著则 C3 降级为 observation
- **Paper Agent 已预写 RASP-RLVR 框架**，数据到手后只需填 [TBD-RLVR] 占位符
- **DDL**：ARR May 25, 2026（~9 天），timeline 充裕（72 GPU-hours 实验 vs 864 可用）


---
