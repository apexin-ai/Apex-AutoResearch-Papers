# director / loop_10.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`edc8434993639c5b9699.json`](../../sessions/ed/edc8434993639c5b9699.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-17T09:08:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 的 cuda:0 + cuda:1（2× RTX 5090, 32GB each）
- 当前 70B 实验占用 TP=2（两卡都用），Reflexion 必须等 70B 完成后才能启动
- 70B checkpoint：前 5 episodes 完成后必须检查 per-episode 时间，>30min/ep 则立即切 Qwen2.5-32B-Instruct 释放一张卡
- 论文真源在本地 workspace（`projects/simgate-modular-routing/docs/paper/`），远程只是编译副本
- MATH N=795 是验证过的正确数字（math_clean_800.jsonl 含 960 条未去重记录，去重后 795）
- 不要使用 level-split worker 的结果（bug：读了未去重文件，internal_acc == code_acc 是 artifact）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com), user=root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/
- 模型下载中：Qwen2.5-72B-Instruct-AWQ via modelscope（~25min ETA at last check）
- vLLM 配置：TP=2, AWQ quantization, gpu_memory_utilization=0.95
- 活跃 tmux：70B 下载 + episode 收集脚本（具体 session name 需 Agent 确认）
- Death-risk routing analysis worker 在 CPU 上运行中

### 3. 📊 当前状态
三线并行实验刚启动（用户要求做 70B/Reflexion/death-risk routing 加固论文）：
- `backbone-scaling-70b`: RUNNING — 模型下载中，下载完后自动启动 episode collection（11 types × 20 eps）
- `reflexion-internal-baseline`: 排队 — 等 70B 完成释放 GPU（或 70B 太慢切 32B 后并行）
- `death-risk-routing-analysis`: RUNNING (CPU) — threshold routing simulation，应 <1h 完成
- `math-extension-n800`: DONE (success) — N=795 confirmed null, p=0.81, 已写入论文
- `plan-008-v4-4b-e2e`: DONE (negative) — 4B router -10.72, 已写入 Appendix

论文状态：R11 全部修复完成，正文 8 页，Abstract 163 words，编译 clean。待新实验结果写入后最终提交。

### 4. 📋 待办
- Death-risk routing worker 完成 → 分析结果，如果存在 sweet spot 优于 always-det → 写入论文 §4.5 或新 section
- 70B 前 5 episodes 完成 → 检查 per-episode time；>30min → 切 32B + 启动 Reflexion 并行
- 70B 全部完成 → 分析 death rate / DAF / 与 7B 对比；DAF 仍高 → 极强结果写入正文；DAF 大降 → 加 caveat
- 70B 完成后 → 启动 Reflexion (cuda:1 或双卡)
- Reflexion 完成 → 如果 death rate 仍高 → "even with self-correction, death dominates"；如果显著降低 → 调整 claim 为 "holds for single-pass agents"
- 所有实验完成 → Paper Agent 整合结果 → 最终审稿 → ARR 提交

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Findings (DDL 5/25)，当前 R11 weak accept
- 用户明确要求按最高质量推进（不急着提交），做 70B + Reflexion + death-risk routing 三个加固实验
- 核心结论：ScienceWorld 中 78.9% routing labels 由 death asymmetry 驱动，DAF=90.4%@P=100
- 决策链：D101 (Findings track) → D102 (MATH N=795 confirmed null)
- **最容易判断错的事**：70B 结果解读。如果 72B death rate 大幅降低（如 <15%）且 DAF 降到 <50%，这不是 "论文失败"——这是验证了论文自己的 prediction，可以 reframe 为 "framework correctly predicts capability-dependence"。不要 panic。
- **容易踩的坑**：(1) 72B AWQ 行为可能与 FP16 不同，异常结果先怀疑量化 artifact (2) Reflexion 实现需要修改现有 episode runner，确保 reflection context 正确 prepend (3) 不要用 math_clean_800.jsonl 的 raw 960 条做分析，必须去重到 795
- Manager 之前要求 hypothesis-driven 实验，所有新实验都有明确 hypothesis + parent chain


---
