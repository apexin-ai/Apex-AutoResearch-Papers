# director / loop_1.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`deeeec569a7f460957c8.json`](../../sessions/de/deeeec569a7f460957c8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-21T06:43:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35694 cuda:0/1/2/3（4张卡），严禁使用其他设备号
- Mistral 当前只有 seed=42 单 seed，**不能**以 Cohen's d 形式报告 Mistral 结果，只能报原始 Δlz*
- 论文**绝不能** claim "lz* < -2 即为污染"——固定阈值跨家族失效（Qwen contam_15 lz*=+3.85 仍为正值），检测必须基于 Δlz*/Cohen's d
- "minimal-information" 措辞已决定改为 "minimal information from the target model"，PSN-IRT 参数为外部依赖——不能回退到旧措辞
- ARR DDL 问了 5+ 次未确认，不要替用户假设 DDL

### 2. 🖥️ 基础设施快照
- 服务器：westd-35694 (connect.westd.seetacloud.com)，root 用户
- 远程代码路径：未在 project config 中配置（get_project_status 显示 ✗），实际代码在 /root/autodl-tmp/ 下（需确认）
- 模型缓存：/root/autodl-tmp/ 下（AutoDL 根分区只有 30GB，大文件必须放数据盘）
- GPU 状态（最后 Reviewer 确认 ~06:10 UTC）：
  - cuda:0: Qwen clean_s4 训练 (seed=301)
  - cuda:1: Qwen clean_s5 训练 (seed=302)（之前有 stale Mistral eval 进程需 kill）
  - cuda:2: exp-post-rl GRPO 46.6% (3269/7021 steps), ETA ~08:30 UTC
  - cuda:3: eval_with_ht.py --stage base (D022 HT post-RL) + Qwen clean_s5 训练
- 飞书群：A群 oc_9840a7d708128f2f1d02985bd9b8d901, C群（审稿）oc_6c76a266d9f5997de21a1604bc79c209

### 3. 📊 当前状态
刚完成 Dream Round 2 分析（D022）并执行了行动项：
- paper_framing.md 已更新：R12 (HT 四场景应对 + 数据无关差异化), R13 (minimal-information), 跨家族 baseline lz* divergence (#13/#14), headline template 修正
- ROADMAP 已更新（Dream Round 2 结果 + Path to 3.5）
- Paper Agent 已收到 patch 指令（跨家族 baseline 讨论 + minimal-information 措辞 + inverted-U model-dependent caveat）
- 引用扩充完成（30 条 verified，Reviewer PASS），Agent 队列中有整合到 bib 的指令
- **Agent 队列 depth=4**，正在逐条处理（seeds 启动 → Mistral 清理 → 引用整合 → HT 结果查询）

**等待中的关键回调：**
1. HT post-RL base/SFT 阶段结果 — eval_with_ht.py 在跑，这是 D022 最高优先级
2. GRPO 训练完成（~08:30 UTC）→ 需要跑 GRPO 阶段的 lz* + HT eval
3. Qwen seeds s4/s5 训练完成 → eval → 继续排 s6-s10 + Mistral/Llama seeds
4. Paper Agent patch 回复（跨家族 baseline 讨论 + minimal-information）

### 4. 📋 待办（条件触发式）
- HT post-RL base+SFT 结果回来 → 对比 ℓz* vs HT 效应量，判断四场景中属于哪个（Best/Good/Neutral/Bad），更新 paper_framing.md R12
- GRPO 完成（~08:30 UTC）→ 派 Agent 跑 eval_with_ht.py --stage grpo（注意：eval 需 base→SFT merge→GRPO adapter 的正确加载顺序，之前有 bug 已修）→ 这是 D022 的决定性数据点
- Qwen s4/s5 完成 → eval_lz → 排 s6-s10 on freed GPUs → 同时排 Mistral clean seeds (seed=43,44,45...)
- 全部 seeds n=10 完成 + HT post-RL 结果 + Mistral Cohen's d → 综合更新论文 + re-dream（第三轮）
- Post-RL Llama 实验：GRPO cuda:2 释放后启动 Llama SFT→GRPO（~8 GPU·h），Dream 三档一致需要第二家族
- 引用整合完成 → 确认 HT 原始论文(Harnisch 1983)、PSN-IRT、Wang et al. 2025 在 bib 中
- Paper Agent patch 完成 → 确认跨家族 baseline 表格、minimal-information 措辞、inverted-U caveat 都到位

### 5. 🎯 战略上下文
- **项目核心**：IRT person-fit (ℓz*) 检测 LLM benchmark contamination，目标 EMNLP 2026 Main
- **Dream 评分轨迹**：Round 1 (B:3.0/M:2.5/W:~2.0) → Round 2 (B:3.0/M:3.0/W:2.5)，median 提升但仍 Findings 水平
- **通往 3.5 (Borderline Conference) 的关键路径**：(1) HT post-RL 差异化 — 如果 ℓz* 保留信号 HT 不保留→决定性；(2) Post-RL Llama 第二家族；(3) 引用 30→60+；(4) Seeds n=10 收紧 CI；(5) 诚实 headline（包含 HT 比较）
- **最易判断错的事**：HT post-RL 结果可能不是 Best case（均保留或均丢失）。D022/paper_framing.md R12 已准备四种场景应对——如果 Neutral/Bad，不要慌，转用数据无关差异化点（parametric null, Snijders correction, multi-parameter weighting）
- **容易踩的坑**：(1) Agent 队列积压——当前 depth=4，不要继续堆消息，等处理完再发；(2) Mistral 只有 1 seed，不要用 Cohen's d 引用；(3) Inverted-U 是模型相关的（Qwen 有，Llama/Mistral 没有），不能 claim universal；(4) cuda:0/1 可能有 stale eval 进程占显存，确认清理
- **决策链**：D020 (C群审稿处理) → D021 (Action Matrix: seeds n=10, R² 降级) → D022 (Dream Round 2: HT post-RL 突破口 + 六项结构性问题)


---
