# agent / loop_17.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`3d5eaa0a1f7c677f9b6c.json`](../../sessions/3d/3d5eaa0a1f7c677f9b6c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-16T18:58:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13313 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- r7n2 系列实验已确认 negative（数据 scaling 无效），不要再跑更多 scale 变体
- ALFWorld DAF 数字是 tautological（binary env），论文中只引用 qualitative evidence，禁止引用 DAF=100% 的数值
- MATH 结果 p=0.079，只能用 "directional trend" 措辞，不能说 significant
- EMNLP DDL 2026-05-25，剩 9 天

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，2× RTX 5090
- 工作目录：/root/autodl-tmp/simgate-modular-routing/
- Python：conda base（/root/miniconda3/bin/python），不要假设 .venv 存在
- 数据：data/plan-004-implicit/implicit_sft.jsonl (1733 samples)
- 活跃进程：无（两块 GPU 全空闲）
- 无活跃 cron

### 3. 📊 当前状态
- 全部 87 个实验已完成，registry 中无 RUNNING/PREPARING/PENDING/ALLOCATED
- 刚向 Director 汇报了 llama-cross-model-v2 完成（C3 强确认）+ 两块 GPU 空闲 + 请求 A/B/C 方向决策
- 3 个 Worker 在跑（全是 CPU 任务，无 GPU）：
  - `worker_exp_capacity-scaling-episode-eval_20260516T124153`：R8-W3 episode-level eval，turn 33，收集 0.6B 多 seed 数据
  - `worker_fix_r8-m1-bib-orphan_20260516T125206`：清理 bib orphan entries
  - `worker_fix_r8-w6-reasoning-depth-n_20260516T125215`：补充 reasoning depth n 值
- 等待 Director 回复 A/B/C method 方向选择（main track BLOCKER）

### 4. 📋 待办
- R8-W3 Worker 回调 → 更新 registry，整合 episode-level eval 结果到论文
- R8-m1 Worker 回调 → 确认 bib 清理结果，检查是否误删
- R8-W6 Worker 回调 → 确认 n 值补充正确
- Director 回复 A/B/C 选择 → 立即铺对应实验代码到 cuda:0+1，spawn worker 开干
- 如果 Director 长时间未回复 → 再次 ping，强调 GPU 空闲 + DDL 紧迫
- R8-W1/W2/W4/W5/W7 文字修改需 Paper Agent 完成（不是我的 scope，但需 track）

### 5. 🎯 战略上下文
- 核心发现：ScienceWorld routing signal 90.4% 来自 death avoidance（C1 SOLID，CI [81.6%, 98.8%], r=0.97）
- C2 negative 证据链 COMPLETE：router episode-level 泛化≈随机（cross-split 47.1%, majority-vote 50%, scaling 无效, LOTO 7/11 全 det）
- C3 cross-model 现在也 SOLID：Llama-3.1-8B 复现 death avoidance（int_preferred=0 across ALL 7 tasks，比 Qwen 更极端）
- 论文状态：Round 8 borderline 3.25/5 推荐 Findings track，reviewer 认为 main track 需 method 创新
- 决策链：D094(C1精确化) → D093(preemptive experiments) → D092(Outcome B confirmed) → D089(C2定调)
- 易错点：不要在 Director 未选定方向前自行启动 method 实验；不要花时间修复 r7n2 系列（已死）；llama-cross-model-v2 的 int_preferred=0 是合法的（det NEVER dies，所以 router 从不 prefer internal）


---
