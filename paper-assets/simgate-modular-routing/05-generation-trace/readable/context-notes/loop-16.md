# agent / loop_16.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`3da7bb9cfec32b80bea9.json`](../../sessions/3d/3da7bb9cfec32b80bea9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-16T12:48:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13313 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- r7n2 系列实验已确认 negative（数据 scaling 无效），不要再跑更多 scale 变体
- ALFWorld DAF 数字是 tautological（binary env），论文中只引用 qualitative evidence，禁止引用 DAF=100% 的数值
- MATH 结果 p=0.079，只能用 "directional trend" 措辞，不能说 significant
- EMNLP DDL 2026-05-25，剩 9 天，所有决策以此为锚

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，2× RTX 5090
- 工作目录：/root/autodl-tmp/simgate-modular-routing/
- Python：conda base（/root/miniconda3/bin/python）
- 数据：data/plan-004-implicit/implicit_sft.jsonl (1733 samples)
- 活跃进程：llama-cross-model-v2 (PID 961982, tmux 未知, cuda:0, 预计 ~12:00 UTC 完成)
- cuda:1 空闲（r7n2-supplement-100-200 刚失败释放）

### 3. 📊 当前状态
- 刚收到 r7n2-supplement-100-200 失败回调（EXIT_CODE=1），已派 Worker `worker_diagnose_r7n2-supplement-100-200_20260516T073754` 去读日志诊断，**尚未收到回调**
- llama-cross-model-v2 仍在 RUNNING（cuda:0，Llama-3.1-8B 跑 7 task types × 10 eps，预计 12:00 UTC）
- cuda:1 当前空闲 — 失职状态，需要 Director 决策下一步用途
- 用户尚未选定 method 创新方向（A/B/C），这是 main track 的 BLOCKER

### 4. 📋 待办
- Worker 诊断回调到达 → 判断 r7n2-supplement 是否值得重跑（大概率不值得，因为 r7n2-r3 已跑 7/21 含 800% 全部 negative，100%/200% 几乎确定同样 negative）→ 更新 registry notes → 汇报 Director
- llama-cross-model-v2 完成回调 → 分析 cross-model DAF 是否复现 death avoidance pattern → 更新 C3 claim 强度 → 汇报 Director
- Director 选定 method 方向 (A/B/C) → 立即铺对应实验代码到 cuda:1
- cuda:1 空闲需向 Director 汇报，建议用于 method 方向实验或其他 preemptive defense

### 5. 🎯 战略上下文
- 核心发现：ScienceWorld routing signal 90.4% 来自 death avoidance（C1 SOLID，CI [81.6%, 98.8%], r=0.97）
- C2 negative 证据链 COMPLETE：router episode-level 泛化≈随机（cross-split 47.1%, majority-vote 50%, scaling 无效, LOTO 7/11 全 det）
- C3 cross-model 是当前最弱 claim，llama-cross-model-v2 是补强的关键实验
- 论文状态：6 项修正已完成，审稿 issues 全部 action done，等 llama 结果 + method 方向 + Round 8 审稿
- 易错点：r7n2-supplement 失败不影响大局（r7n2-r3 已经给出足够 negative evidence），不要花时间修复重跑，除非 Director 明确要求
- 决策链：D094(C1精确化) → D093(preemptive experiments) → D092(Outcome B confirmed) → D089(C2定调)


---
