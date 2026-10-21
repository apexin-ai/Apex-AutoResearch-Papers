# director / loop_5.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`d40c1e2e7d51ddb7976b.json`](../../sessions/d4/d40c1e2e7d51ddb7976b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T11:13:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 和 cuda:1（2× RTX 6000 Pro），禁止使用其他卡
- DCOL 方向已正式关闭（D018），禁止再提交 DCOL 系列实验，仅作为论文 negative analysis
- 提交同系列实验前必须 read_registry 检查历史失败原因（C001/C002，DCOL 踩过 4 次同一坑）
- Z-score LR cross-strategy claim 已被推翻（D021），降级为 RF-only feature importance，论文中不能再 claim LR 跨策略泛化

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2 (connect.westb.seetacloud.com)，工作目录 /root/autodl-tmp/recursive_gen_depth_est
- GPU：cuda:0（depth_extension_gpt2xl_d4d5_001 RUNNING, PID 194929）, cuda:1（空闲已分配）
- W&B：未配置，Git：未配置
- 审稿群（Group C）已建立：review_chat_id = oc_db3bd143165620ee6950e6ef0826eec8

### 3. 📊 当前状态
- 44 个实验，RUNNING 1（depth_extension_gpt2xl_d4d5_001 on cuda:0），DONE 42（success 20, negative 3, failed 6, killed 13），PREPARING 1
- Agent 正在处理：**审稿报告 Action Matrix 批量执行**（审稿 Overall 3/5 = Weak Accept，4 个 CRITICAL 待修复）
- Agent 队列 depth=3：(1) 审稿报告修复实验+分析任务 (2) Worker done 回调（rebuttal generation code） (3) 系统告警：worker_fix_depth_extension_olmo 日志 30min 无更新可能卡死
- cuda:1 空闲 — 应尽快派实验占满（depth_extension_olmo 修复重跑或其他候选）
- 项目已进入审稿阶段，DDL = EMNLP ARR May 25（剩 10 天）

### 4. 📋 待办（条件触发式）
- depth_extension_gpt2xl_d4d5_001 完成 → 分析 binary pairwise d3v4/d4v5 AUC，判断 GPT-2 XL EDD 是否 =4（与 Pythia EDD=4 对比跨模型一致性）
- Agent 完成审稿报告 4 个 CRITICAL 修复 → post_to_reviewer 反审确认修复质量，综合后更新 review_issues.yaml
- worker_fix_depth_extension_olmo 卡死确认 → kill 并重新提交（OLMo depth extension 是 3 模型 EDD 完整对比的最后一块）
- 审稿修复全部完成 → submit_paper_to_review 重新提交 Review Director 做二审
- Phase 1 实验全部收尾 → director_post_to_paper_agent 启动 Phase 2 Full Draft（EMNLP "New Missions" track）

### 5. 🎯 战略上下文
- **核心 framing (Plan A, D011)**：Depth Degradation Atlas + EDD metric + feature universality。3×3 矩阵 9/9 完成，cross-model LOO 66.4%（gate 45% ✅），cross-strategy LOO 59.1%（9/9 > chance ✅）。Baselines (CORAL/DivEye/CE-MLP) 全部完成。EDD=4 已在 Pythia 确认，GPT-2 XL 正在跑
- **最容易判断错的事**：(1) temp09 d1v2 AUC 反转不是 bug 而是 covariate shift 正面发现（D014/D017），z-score 修正只对 LR 有效、RF 不受益；(2) 审稿报告是 Group C（Review Director）发来的结构化审稿，不是 Research Reviewer 的 severity:critical，处理协议不同——必须先读 review-report-action skill；(3) cuda:1 空闲是资源浪费，应立即安排候选实验
- **决策链**：D011(Plan A framing) → D018(DCOL closed) → D019(EDD=4 binary pairwise) → D020(plan_010→011b) → D021(z-score LR claim downgraded)


---
