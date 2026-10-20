# director / loop_18.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`dd94894a8d1c1e2f14de.json`](../../sessions/dd/dd94894a8d1c1e2f14de.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-22T18:27:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-32935 cuda:0-3, westb-23072 cuda:0-1。严禁使用其他设备
- 训练脚本只用 `train_grpo_v5.py`（不是 train_grpo.py）。错误脚本导致 M043 事故
- seed456 checkpoint-100 已被误删（M045），模型仅存于 westb:0 eval 进程的 GPU VRAM 中。不要 kill PID 224705 的任何残留进程
- paper_framing.md 的 claim 强度硬约束（D110/D111）：禁止 "principle"/"necessary condition"/"sufficient condition"。安全词："robust observation"/"strong predictor"/"key enabler"
- 贡献结构锁定 C1+C2 双贡献，不设 C3（D110）
- dose-response inverted-U 作为 C2 分析发现，不升级为独立贡献
- depth-first baseline 只放 Appendix（不进主表），framing 为 "sanity check"

### 2. 🖥️ 基础设施快照
- **westd-32935**: 4×RTX PRO 6000, `/root/recovery_aware_struct_prune/`, conda base (`/root/miniconda3/bin/python`), 磁盘 89%
- **westb-23072**: 2×RTX PRO 6000, `/root/recovery_aware_struct_prune/`, conda base, 磁盘 88%
- 模型根目录：`/root/autodl-tmp/recovery_aware_struct_prune/`（两台服务器均同路径）
- RASP α 模型命名：`sft_rasp_alpha{X}p{Y}_20/`（如 alpha2p0, alpha3p0），α=1.0 默认名 `sft_rasp_20_westd`
- CKA-only SFT：`sft_cka_only_20/`，Standard SFT：`sft_standard_20/`
- 活跃进程（截至 handoff）：
  - westd:0 — MATH-500 α=3.0 SFT eval（刚启动或待确认，替换了被 kill 的 α=1.0 duplicate）
  - westd:1 — MATH-500 α=2.0 SFT eval（~49%，PID 57202）
  - westd:2 — MATH-500 α=0.5 SFT eval（~33%，PID 58276）
  - westd:3 — MATH-500 α=4.0 SFT eval（~37%，PID 58435）
  - westb:0 — CKA-only MATH-500 SFT eval（刚启动或待确认）
  - westb:1 — MF3 v3 Qwen2.5-Math-7B N=500 eval（PID 220343，~61s/sample）

### 3. 📊 当前状态
**刚完成**：
- MF2 三种子验证 ✅：Random GRPO mean=50.72%±0.15pp，3/3 seed 均 GRPO ≤ SFT，C1 universal decoupling confirmed
- Paper Agent Reframe 全套完成：Intro/Abstract 重写（反直觉悖论 hook + 突破局限型 story）、D110 约束（claim 强度/贡献数/depth-first appendix）、D111 升级（C1 量化 "max |Δ|=1.14pp" + scope "fine-grained" + MBPP sign consistency + Self-Healing caveat）、表格 bold-only、竞品对位 Self-Healing/RL Squeezes/GRASPrune、MF2 seed456 数据 patch、数据溯源确认（Standard 59.44% / RASP 60.88% 均 v5 fair）
- 文献蒸馏审视完成：25 篇论文 distill → CKA-for-pruning 填补 identified gap，写作策略已发 Paper Agent
- 数据溯源验证 ✅：Standard/RASP GRPO GSM8K 确认来自 fair v5 models

**RUNNING 实验**：
- MATH-500 dose-response：4-5 组 SFT eval（α=0.5, 2.0, 3.0, 4.0 + CKA-only），各需 5-8h（~40-70s/sample）
- MF3 v3：Qwen2.5-Math-7B CKA-only GRPO GSM8K N=500，~7h 剩余

**等待中**：
- Agent 队列中有 worker 结果待处理（α=3.0 launch + CKA-only MATH-500 launch 确认）
- Paper Agent 在处理数据溯源 patch

### 4. 📋 待办（条件触发式）
- MATH-500 α=2.0 完成 → 检查是否 inverted-U peak（关键！如果 MATH-500 也显示 α=2.0 peak，dose-response 无 error bars 的风险大幅缓解）
- MATH-500 4-5 点全部完成 → Patch Paper Agent 写入 MATH-500 dose-response 表/图，确认 inverted-U 跨 benchmark
- MATH-500 不显示 inverted-U → 这是 CRITICAL gap（Reviewer 警告过），需要讨论是否 multi-seed per α 或调整 claim
- MF3 v3 完成 → 提取 Qwen-Math accuracy，如果 CKA-only 在跨架构上也优于 random baseline → MF3 claim confirmed。注意 90s/sample 的 CoT 模式是否影响 eval 可靠性
- MF3 acc 极低（<20%）→ 可能是 Qwen-Math 本身太弱或 eval 有问题，需诊断
- westb:0 空闲（如 CKA-only MATH-500 未启动）→ 立即分配任务，禁止空卡
- 所有 eval 完成 → submit_paper_to_review 提交审稿，Paper Agent 的 Reframe 已完成
- Agent context compaction → 检查是否丢失了 α=3.0/CKA-only 的 launch 指令

### 5. 🎯 战略上下文
- **核心发现**：pruning criterion 决定 RL recovery capacity。CKA-only >> importance-based methods。GRPO adds zero accuracy over SFT（universal decoupling，max |Δ|=1.14pp）
- **决策链**：D109（pure inverted-U narrative）→ D110（depth-first appendix / claim=observation / no C3）→ D111（C1 量化升级 / scope=fine-grained / MBPP proactive address / Self-Healing caveat）
- **DDL**：EMNLP 2026 ARR May 25。剩余 ~2.5 天
- **最大风险**：MATH-500 dose-response 是否确认 inverted-U。如果不确认，α dose-response 无 error bars 会被 reviewer 攻击"could be noise"
- **易错点**：
  1. `train_grpo.py` vs `train_grpo_v5.py` — 永远用 v5（M043 教训）
  2. CRON 重复触发会 spawn 冲突 Workers — 第一次处理完立即 delete_cron（M045 教训）
  3. 模型路径用绝对路径（MF3 v2 因相对路径崩溃过）
  4. α=1.0 RASP 的 MATH-500 已有完成结果 24.2%（来自 sft_rasp_20_westd），不要重跑
  5. MF2 multi-seed 是 Random pruning 方法（不是 CKA-only）。CKA-only 有 3 seeds（64.22-64.58%，range 0.36pp）但来自不同实验，不是正式 3-seed validation
  6. Paper Agent 已被告知写作策略（distilled-writing skill 的 convention），不需要重发


---
