# director / loop_11.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`b95c0ca2ccaeecce4660.json`](../../sessions/b9/b95c0ca2ccaeecce4660.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-17T21:27:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 cuda:0/1, westb-14838 cuda:0/1/2/3。不得使用其他设备
- 72B 推理：westb-13313 用 TP=2（2×RTX 5090 32GB），westb-14838 用 TP=1（RTX 6000 PRO 96GB）
- retry-control-baseline 结论是 "negative"（假设被否定，数据完整 N=220），registry 标记为 failed 是 cron 误判，不要重跑
- 用户指令：全部实验跑完后释放所有资源（游承松确认）
- 论文真源在本地 workspace `docs/paper/`，不是远程服务器。Reviewer R15 曾因读远程陈旧文件误判

### 2. 🖥️ 基础设施快照
- westb-13313: connect.westb.seetacloud.com, /root/autodl-tmp/simgate-modular-routing
- westb-14838: connect.westb.seetacloud.com, /root/autodl-tmp/simgate-modular-routing
- 72B 模型路径: AWQ 量化版，具体路径在远程 config 中
- 活跃进程:
  - westb-13313 PID 617494: 72B 收集（lifespan-longest-lived 6/20，后续含 measure-melting-point）
  - westb-14838 PID 321045 (cuda:0): 72B 收集，存活
  - westb-14838 PID 69734 (cuda:1): 72B 收集，存活
  - westb-14838 cuda:2: 刚派 Agent 补跑 measure-melting-point 剩余 5 episodes（~20min）
- 本地论文: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/

### 3. 📊 当前状态
72B 数据收集 10/11 tasks 完成（各 20 episodes），唯一缺口 measure-melting-point = 15/20。已批准 Agent 在 westb-14838 cuda:2 补跑 5 episodes（~20min 完成）。

刚发给 Agent 的指令：补跑完成后汇总 11 tasks aggregate DR + per-task breakdown 用于论文 Table 4。

论文状态：R20 = 8/10（Findings accept），等 72B 全量数据后做 micro-patch → R21 final → 提交 ARR。

Review chat_id: oc_0b622d6038b969b96148ee8a163a1a0c

### 4. 📋 待办
- Agent 回复 72B 汇总数据 → dispatch micro-patch 给 Paper Agent:
  - Table 4: "≥187 episodes" → "220 episodes", "10 of 11" → "11 tasks"
  - aggregate DR 更新为精确值
  - R20 info 修：(a) experiments.tex 过渡句解释 Abstract 35% vs Experiments 31.4% scope 差异; (b) discussion "comparable" → "similar-order" 或 "14-17pp"
- micro-patch 完成 → submit_paper_to_review(recommended_review_mode="continue") 提交 R21 final
- R21 无 critical → 通知用户可提交 ARR + 释放所有 GPU 资源
- ROADMAP 需更新：当前仍显示 retry=191/220, 72B=4/11，实际全部完成

### 5. 🎯 战略上下文
- 核心叙事（D104）："三种定性不同干预均无法达到 deterministic-level safety"
  - Retry: Δ≈0pp (DR 40.9% ≈ baseline 42.9%)
  - Scaling 7B→72B: Δ≈-14pp (death-prone ~51% → ~37%)
  - Reflexion: Δ≈-17pp (death-prone ~51% → ~35%)
  - 全部远高于 det 16.3%
- 易错点：72B 之前基于 4/11 tasks 说 "no improvement" 是错的。10/11 tasks 显示 -14pp 实质降幅。framing 已修正，不要回退
- 易错点：experimental triangle 中 scaling 和 reflexion 必须用同一个 baseline（death-prone tasks, ~51%）。之前 R19 因 baseline 不对称被打回
- DDL: ARR May 25（还剩 ~7 天）。论文已基本就绪，只差 micro-patch 这一步
- 提交清单中未完成：acl-pubcheck 自动验证 + 最终 PDF 编译确认 + OpenReview profile（需通知用户）


---
