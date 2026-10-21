# reviewer / loop_1.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`a9c77bd63143d3f8ada7.json`](../../sessions/a9/a9c77bd63143d3f8ada7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T22:04:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（westd-39279 上的 2× RTX PRO 6000 96GB）
- exec-only 跑 CUDA_VISIBLE_DEVICES=0，exec-sta 跑 CUDA_VISIBLE_DEVICES=1（历史约定，r3 因未隔离 OOM 过）
- exec-sta-r5 registry conclusion="success" 是错的——prove_rate=0.1 低于 baseline=0.12，应为 "negative"。Agent 至今未修正，如果你看到 Agent 引用此结论需要 challenge
- ISR 指标跨 reward_mode 不可比：exec-only 用 fast_sta_reward（binary ISR=0/1），exec-sta 用 sta_reward（continuous ISR 0.0-1.0）。不能直接比两组的 mean_isr

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，工作目录 /root/solver-trace-ablation
- Python：/root/miniconda3/bin/python3（conda base 环境，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：/root/autodl-tmp/models/Qwen3-4B
- 数据：/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl（500条训练）+ proofwriter_fol_100.jsonl（100条 baseline）
- 输出：/root/autodl-tmp/outputs/grpo_exec_only/ 和 grpo_exec_sta/
- W&B：no_wandb=true（服务器无 API key）
- 活跃进程：无。两张卡 0% util, 0 MiB（已空闲 >20 分钟）

### 3. 📊 当前状态
我完成了三件事：
1. Phase 1 r5 综合审查——发现 full STA 50/50 权重导致 prove_rate 退化至 baseline 以下，posted to Director
2. ROADMAP "MVP 通过" 审查——指出 Pass Criteria #4/#5 未满足，要求修正标签、增加 Kill Criteria、不等 Dream 启动实验
3. ROADMAP 修正确认——Director 已采纳所有建议（MVP 改"部分通过"、增 Kill Criteria、plan_005 提前）

Registry：12 实验全部 DONE（无 RUNNING）。ROADMAP 说"紧急实验已排队"（低权重 STA + ISR-as-bonus）但实际尚未提交。
等待：Dream dream_20260513T215750 pending（但已决定不等 Dream 启动无依赖实验）

### 4. 📋 待办
- 新实验提交（低权重 STA / plan_004 / plan_009）→ 审查 CUDA_VISIBLE_DEVICES 是否在白名单内 + spec 完整性
- plan_005 weight ablation 结果出来 → **这是 pivotal experiment**：所有权重配比 STA 均 ≤ exec-only → 论文退化为 "STA as monitor"，需立即 post Director
- plan_001/002（500步 3seed）完成 → 审查 prove_rate 是否显著高于 100 步 pilot（15-20%），若仍停滞说明 GRPO 基座本身有问题
- plan_003（held-out eval，统一 ISR 评估）完成 → 核查 exec-only checkpoint 用 full STA 评估后的 ISR/PR 比，这是 "STA 检测 hacking" claim 的关键证据
- Agent 做 Framing 调整提案 → Read negative-framing-review skill，四维度审查
- 任何章节写作审查请求 → 先查 Agent 是否看过 red-section skill

### 5. 🎯 战略上下文
- 决策链：D001(MVP 方案) → D002(100步+kill criteria) → D003(fast_isr 无效→full STA+K=8) → D004(Reviewer 指出 r5 退化)
- 核心矛盾：STA 作为 ISR 度量有区分力（GT=0.56 vs model=0.064），但作为 reward 组件时 50/50 权重惩罚过重导致 prove_rate 崩溃。paper_framing.md 已 pivot 到 "STA detects hacking"（ISR/PR 64%→33%），但这个 claim 尚未独立验证
- 最容易判断错的事：**不要被 "ISR/PR 从 64% 降到 33%" 误导为 ISR 在下降**——实际是 prove_rate 翻倍（8%→15%）而 ISR 持平（5.2%→5.0%），分母变化驱动的比值下降。Agent 可能包装为"STA 成功检测到 hacking 加剧"，但需要 plan_012 的人工标注才能确认
- DDL：EMNLP 2026 ARR May 25（剩 12 天），GPU 预算 30h / 2卡 ≈ 15h wall-clock，算力充足但不能空转


---
