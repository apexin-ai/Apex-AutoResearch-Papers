# reviewer / loop_14.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`a9f69e37dde04ab57636.json`](../../sessions/a9/a9f69e37dde04ab57636.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T09:08:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0 + cuda:1 on westb-13313。越界立即 CRITICAL。
- 论文已达提交状态（R11 fixes 完成，编译 clean 15页）。任何对 paper 的修改必须重新编译验证 0 errors + 0 undefined citations。
- MATH 数据：正确 N=795（从 960 行 math_clean_800.jsonl 去重而来）。不要用 N=960 或 N=800。
- Registry 中 backbone-scaling-70b 正在跑。不要 kill 或干扰。

### 2. ��️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 /root/autodl-tmp/simgate-modular-routing
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/
- 论文目录：docs/paper/（main.tex + 各 section .tex）
- 数据：/root/autodl-tmp/simgate-modular-routing/data/math-counterfactual/math_clean_800.jsonl (960 lines, dedup→795)
- 活跃进程：backbone-scaling-70b (tmux session, PID 607756, cuda:0+1, Qwen2.5-72B-Instruct-AWQ, TP=2)
- 模型下载中：modelscope 11 shards，~25-35 min remaining（截至 09:05 UTC），之后自动启动 220 episodes collection
- 无 W&B 配置（本项目不用 wandb）

### 3. 📊 当前状态
刚完成：R11 action matrix 审查 + ARR submission prep 审查 + reference audit + 70b experiment 初始状态验证。

Registry RUNNING/ANALYZING：
- backbone-scaling-70b (ANALYZING)：72B-AWQ episode collection，模型下载中，预计 episode 收集 ~数小时后出结果

等待中：
- 72B 下载完成 → episode collection 自动开始 → 完成后需要审查 death rate 结果
- R11 审稿最终结果（已提交修复版，等 reviewer response）
- ARR 正式提交（Director 决定时机）

### 4. 📋 待办
- backbone-scaling-70b 完成 → 审查 72B death rate vs 7B (42.9%) 对比，验证 "stronger backbone → lower DAF" prediction
- 72B death rate 显著下降 → 建议纳入论文（Discussion 或 Appendix），需重新编译
- 72B death rate 未下降 → 检查 AWQ 量化影响，可能是 informative negative
- ARR 提交时 → 提醒 Director：Abstract ≤200 words（当前 ~169 words ✅）、Responsible Checklist 需人工填、正文 ~5-6 页（建议移 appendix 精华入正文）
- 如果 Director 问页数问题 → 已确认 5 页不 desk reject 但审稿人可能觉得 thin

### 5. 🎯 战略上下文
- 核心结论：78.9% routing labels from death asymmetry（penalty-independent），DAF=90.4% at P=100。MATH confirmed null 支持 "no death → no routing signal"。
- 决策链：D096(78.9% headline) → D101(Findings reframe) → D102(MATH N=795 null)
- 论文定位：EMNLP 2026 Findings，DDL 2026-05-25
- 修改轨迹：R8(3.25) → R9(3.0) → R10(2.75) → R11(pending, weak accept after fixes)
- 易错点：
  - sim_ratio 有两个含义：step-level (95.6% det) vs episode-level decision field (5.3% int)——两者兼容不矛盾
  - r=0.97 是代数后果不是独立发现（P constant → δ·P collinear with δ），已删 partial corr
  - 4B router 59% episode accuracy 但 deployed score (-10.72) 不 beat always-det (-9.47)
  - ALFWorld DAF=1 是 tautological（det never dies, int dies = 100% death contribution），机制是 information asymmetry 不是 death avoidance
  - 0.5B 实验 death rate=13.3%（不是之前误报的 80%），是"太弱到达不了危险状态"现象


---
