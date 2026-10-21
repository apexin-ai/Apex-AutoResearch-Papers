# director / loop_14.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`891f23658d83be9c31bc.json`](../../sessions/89/891f23658d83be9c31bc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-26T06:34:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-51268 的 cuda:0 和 cuda:1（bjb1-45299 已宕机不可用）
- RSSM prediction gap 论文数字只引用 v3 standardized 结果（v1/v2/dry-run 已废弃）
- exp_091 registry conclusion=success 但实际是 CIVO confirmed（registry 不支持自定义 conclusion，已在 notes 标注）
- exp_101 已取消（与 rssm_fidelity_v2 冗余），不要重新启动
- paper_framing.md C2 Cheetah onset rate 已更新为 2/3（exp_091 完成后），exp_097 完成后需再更新为 3/4

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268 (connect.westd.seetacloud.com)，2× GPU
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- bjb1-45299：宕机，端口不可达。Cheetah baseline/frozen checkpoints 在该服务器上，不可用
- westd 可用 checkpoints：exp_008d (Walker trained), exp_009d (Walker baseline), exp_009c (Walker no_dt_emb, 20ep), exp_084 (Walker frozen), exp_091 (Cheetah trained 008d s2), exp_092/093 (Cheetah no_dt_emb)
- 活跃进程：exp_097 PID 3794 (cuda:0), exp_100 PID 5591 (cuda:1) — 均应已完成（16h+ 未处理）
- v3 分析脚本：scripts/analyze_rssm_exp101.py（可复用）

### 3. 📊 当前状态
刚给新 Agent session 发了综合指令：检查 exp_097/100 是否完成 → 提取结果更新 registry → 用 exp_097 checkpoint 跑 Cheetah trained_dt_emb v3 RSSM 分析 → 提交 exp_102/103 (Cheetah 008a) 到释放的 GPU。

- exp_097 (Cheetah 008d s3, C1): CIVO onset@45K 已确认(transient)，65K 自修复。应已跑完 105K，等最终分类
- exp_100 (Walker 008a s1, C3): 56K 时 eval=457 稳步上升，无 CIVO。应已跑完
- exp_102/103 (Cheetah 008a s0/s1, C3 cross-env): QUEUED，等 GPU 释放
- Cheetah v3 RSSM 分析：等 exp_097 checkpoint（CPU 任务）
- 等待 Agent 回复上述指令的执行结果

### 4. 📋 待办
- exp_097 完成确认 → 提取最终 NVE + 分类(transient/sustained) → 更新 paper_framing.md C2 Cheetah onset 3/4 + cross-env 6/7 → 用其 checkpoint 跑 Cheetah trained_dt_emb v3 RSSM (CPU)
- exp_100 完成确认 → NVE 分析确认无 CIVO → C3 Walker 008a 2-seed 证据闭合
- GPU 释放 → 立即提交 exp_102 (cuda:0) + exp_103 (cuda:1)，Cheetah 008a C3 cross-env
- Cheetah v3 RSSM 完成 → 与 Walker v3 合并锁定论文 RSSM Fidelity Table，替换旧 2.78× 数字
- 全部数据到齐 → 更新 ROADMAP → 通知 Paper Agent 更新论文数字 → 数据锁定

### 5. 🎯 战略上下文
- 投稿目标 ICML 2026 (DDL 5/29)，数据锁定 5/27，极度紧迫
- 核心发现：trained dt_emb 驱动 CIVO，onset rate 6/7 (86%) vs frozen/removed 0/13 (Fisher p<0.0001)
- RSSM 机制：trained dt_emb 改善 obs 预测但恶化 reward 预测（Walker reward ratio 1.63× vs baseline 1.56×），dissociation 是关键 insight
- frozen dt_emb reward MAE 异常高 (0.35 vs 0.03-0.06) 是真实效应——frozen 阻止 CIVO 的机制是让 reward prediction 丧失 dt 区分能力，不是维持好预测
- Walker no_dt_emb 只有 20 episodes（已决定接受+标注，不补跑）
- 易错点：exp_097 是 trained_dt_emb 模型（dt_embed_dim=32 默认值），不要误判为 "非 trained_dt_emb"。008d 配置 = trained_dt_emb + subsample ON + fixed_dt=2
- C003 论文 claim 的 2.78× 来自旧方法论，数据锁定前必须用 v3 数字替换


---
