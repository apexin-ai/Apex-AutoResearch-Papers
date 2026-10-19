# agent / loop_22.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`dc26e9f6323c3caa75ea.json`](../../sessions/dc/dc26e9f6323c3caa75ea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-25T14:55:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 bjb1-17606 的 **cuda:0** 一张 RTX PRO 6000，禁止使用其他 GPU 编号
- bjb1-17606 是共享服务器，`/root/autodl-tmp/` 下可能有其他项目文件，严禁删除非本项目文件
- 投稿目标 EMNLP 2026 via ARR，DDL **2026-05-25 AoE = 2026-05-26 11:59 UTC**——极度紧迫
- Cell D (ScienceWorld) 排在 hsweep 之后，hsweep_h10_seed2_retry2 已 success，cuda:0 现在空闲
- Seed 分类已定稿（N=11），不可随意修改：Collapsed 3, Stagnant 4, Generalized 4

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，工作目录推测 `/root/autodl-tmp/` 下（需 Worker 确认具体路径）
- Python 环境：aml-train 镜像，conda base（`/root/miniconda3/bin/python`）
- 模型：Qwen3-1.7B（具体本地路径需 Worker 探查确认）
- 数据：ScienceWorld SFT expert trajectories（D143 决策启动 CPU 数据生成，路径需确认）
- W&B / HF cache：未在 registry 记录，需探查
- 活跃进程：**无**——当前 0 个 RUNNING 实验，cuda:0 空闲
- Cron：reconcile 返回 0 条活跃

### 3. 📊 当前状态
**刚做完**：收到 `scienceworld_sft_bjb1` 失败 cron 回调（EXIT_CODE=1，无 W&B metrics），已派 Worker `worker_diagnose_scienceworld_sft_bjb1_20260524T225428` SSH 到 bjb1-17606 诊断失败原因。**Worker 尚未返回结果。**

**Registry 关键状态**：
- 总计 188 实验：DONE 155（success 46, negative 23, failed 65, killed 21），PREPARING 32，QUEUED 1
- RUNNING：0（全部空闲）
- `scienceworld_sft_bjb1`：DONE/failed，registry 条目极稀疏（无 spec/log_path/command）
- `hsweep_h10_seed2_retry2`：success（刚完成）

**等待中**：
- Worker 诊断回调（`worker_diagnose_scienceworld_sft_bjb1_20260524T225428`）
- 尚未向 Director 汇报此次失败（等诊断结果后一并汇报）

### 4. 📋 待办
- 诊断 Worker 回调 → 读取失败原因 → update_registry 写入 failure_reason + spec → 向 Director 汇报失败原因和修复方案
- 修复后重新提交 scienceworld_sft → SFT 完成后接 Cell D GRPO → eval（整条 pipeline）
- cuda:0 现在空闲（hsweep 已完成）→ 修复 SFT 后立即提交，不浪费 GPU 时间
- DDL 极近（<24h AoE）→ 如果 Cell D 来不及，需向 Director 汇报时间评估让 Director 决策是否放弃 Cell D

### 5. 🎯 战略上下文
- 核心方向：Step-independent agent RL 的双机制信用分配病理（M1 信息丢失 + M2 符号错误归因）+ episode-level 修复
- Paper 处于 Round 3 审稿 + DDL 前补强阶段，主文已编译合规（≤8页，0 critical warnings）
- Cell D (ScienceWorld) 是跨环境泛化证据，SFT 是 Cell D 的第一步。SFT 失败阻塞整条 Cell D pipeline
- hsweep_h10_seed2_retry2 已 success → h-sweep 图数据就绪，可写入论文
- `binary_credit_agreement` 已 success → M2 机制确认（sign-episode correlation ~100%）
- 易错点：(1) bjb1 只有 1 张卡，不要同时提交多个 GPU 实验；(2) scienceworld_sft_bjb1 的 registry 几乎没有 spec 信息，诊断后务必补全；(3) 不要假设 `.venv` 存在，bjb1 用 conda


---
