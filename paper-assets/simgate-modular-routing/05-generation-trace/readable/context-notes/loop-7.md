# director / loop_7.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`d46fea46d44a8d1c7fb6.json`](../../sessions/d4/d46fea46d44a8d1c7fb6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T22:11:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目绑定 westb-13313，GPU 白名单 cuda:0, cuda:1（2× RTX 5090）
- 审稿阶段 review_chat_id: `oc_0b622d6038b969b96148ee8a163a1a0c`，Group C 独立负责论文格式/投稿材料
- Eval pipeline 必须统一 `enable_thinking=False`（D069 已定，混用 thinking mode 会引入 confound）
- Router-size ablation 只报 0.6B vs 4B（D070），不报 1.7B 直接对比（eval pipeline 不一致）
- 维持 2-way routing（deterministic vs internal），已放弃 3-way（D065）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，账户 root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- GPU：2× RTX 5090，cuda:0 + cuda:1，当前均空闲
- 活跃进程：无（全部实验已完成）
- Agent 队列：空闲（idle 188s，depth=0）

### 3. 📊 当前状态
**论文整合全部完成，等用户审批启动 Round 8 continue review。**

- 77 个实验全部 DONE（32 success，15 negative，12 failed/killed）
- Paper Agent 已完成 Round 7 全部 5 项整合：deep-internal ablation / failure taxonomy / cross-task transfer / router-size ablation / baseline caption 修正
- Round 7 所有 action done（4 MF + 7 SF），review_issues: 3 critical in_progress, 8 warning in_progress, 3 info in_progress
- 两张 GPU 空闲——等 Round 8 决定是否需要补充实验
- 无 RUNNING/PREPARING 实验，无待处理 Worker 回调

### 4. 📋 待办（条件触发式）
- 用户审批 continue review → `submit_paper_to_review` 启动 Round 8（recommended_review_mode="continue"）
- Round 8 审稿报告回传 → Read `review-report-action.skill.md` → Holistic Pass + Per-Comment Action Matrix
- Round 8 若报告需要补充实验 → 立即分配 GPU0/GPU1 并行跑（两卡都空着）
- Round 8 全部 resolved → 终稿定稿 → ARR 提交（DDL 5/25）

### 5. 🎯 战略上下文
- 目标：EMNLP 2026 Main Conference Long Paper，DDL 2026-05-25（剩 10 天）
- 核心发现：ScienceWorld 上 routing signal 主要来自 episode-level counterfactual 的 death avoidance pattern
- 覆盖率：C1 83.3%, C1+C2 100%, C2 40%（C2 低是因为 negative results，有信息量的否定）
- 决策链关键节点：D061（Round 7 action matrix）→ D065（2-way routing 定稿）→ D068-D070（router-size ablation 定稿 + eval pipeline 统一）
- 易踩坑：report.md 的"运行中"列表可能有残留旧条目（plan-008-v4-4b/0_6b 显示 RUNNING 但实际已完成），以 registry 为准
- **当前唯一 blocker 是用户审批 Round 8**——两张 GPU 空着不能浪费，如果用户长时间不回应，考虑主动催促或铺 ideas.md 中的候选实验


---
