# director / loop_5.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`6d3eb03576a5c1ec8eab.json`](../../sessions/6d/6d3eb03576a5c1ec8eab.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-16T18:43:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-32608 的 cuda:0（单卡 RTX PRO 6000 Blackwell 98GB）
- Mistral-7B 下载 deadline: May 17 12:00 UTC — 过期则跳过，不阻塞实验链
- exp-013 constraint ablation 不能用 exp-001 的 raw_constraints（pipeline.py 修改时序问题，运行中进程无 hot-reload）— 必须从 traces 重提取或等 exp-002 数据
- 论文 framing 已 pivot (D025): 禁止再用"SICA improves accuracy"叙事，核心是"Capability Trap"分析论文
- exp-001 的 +0.26pp 是最终结论（N=762），D012 的 +3.3pp 已确认为小样本噪声 — 不要基于 D012 数据做任何正面 claim

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608 (connect.westd.seetacloud.com), root, /root/symb_invariant_consensus
- GPU: 1× NVIDIA RTX PRO 6000 Blackwell 98GB, cuda:0
- vLLM: 服务 Qwen2.5-14B-Instruct（exp-001 期间应持续运行）
- 模型路径：/root/autodl-tmp/models/（Qwen-14B, LLaMA-3.1-8B ✓, DeepSeek-R1-LLaMA-8B ✓, Mistral-7B 截断81%）
- 数据：/root/symb_invariant_consensus/data/（strategyqa_200.json ✓, arc_challenge_200.json ✓, math_l45_100.json ✓, expanded datasets ✓）
- 活跃进程：exp-001 PID 181491（应已完成，762/804 at last check ~45min remaining）
- HF cache: /root/autodl-tmp/.hf_cache

### 3. 📊 当前状态
**刚完成**: D025 pivot 全套 — paper_framing.md / experiment_plan.yaml / ROADMAP.md / decisions.yaml 全部更新。Dream 报告 (dream_20260516T054054) 已处理，D024 行动项已落地。用户已通知 pivot 决策。

**等待中**: Agent session 停滞 7h+（idle_seconds=25804），已发 replace_agent_queue 综合恢复指令。Agent 恢复后第一件事：确认 exp-001 完成 → 跑 analyze_expanded.py → 报告 FOLIO per-domain breakdown。

**Registry**: sica_expanded_14b RUNNING（应接近完成或已完成）。其余全部 planned。

### 4. 📋 待办
- Agent 恢复 + exp-001 完成确认 → 检查 FOLIO 子域 gap+p-value（如 gap>3pp 且 p<0.1 → 保留为 sub-finding；否则全域 SICA≈SC confirmed）
- exp-001 analysis 完成 → 立即启动 exp-002 (K={6,8,11,12,16,20}) + exp-013 (CPU, constraint ablation)
- exp-002 完成 → 启动 exp-017 (StrategyQA) + exp-018 (ARC-Challenge)
- Mistral 下载状态确认 → 可用则排 exp-010；May 17 12:00 UTC 不可用则跳过
- 全部 cross-family + cross-domain 完成 → exp-019 (constraint quality correlation) + re-dream 验证 D025 framing
- FOLIO sub-claim confirmed positive → 更新 Story Spine headline result

### 5. 🎯 战略上下文
**决策链**: D016(QwQ fail)→D017(MVP pass)→D019(scope+)→D020(kill dup)→D021(5 exps)→D022(no kill)→D023(contingency)→D024(dream actions)→D025(pivot to Analysis Paper)

**核心结论**: SICA ≈ SC at scale. 论文贡献不再是"方法有效"而是"首次系统揭示 capability trap — 为什么 symbolic consensus 不能 beat voting"。

**易错点**:
1. 不要因为某个 cell 出现 +2-3pp 就回退 pivot — 除非 p<0.05 且跨多个 cell 一致
2. exp-013 数据源：exp-001 没有 raw_constraints cache（时序问题），必须从 traces 重提取或用 exp-002 数据
3. Agent 恢复后可能看到旧 context — 综合指令已包含完整上下文，不需要再发重复消息
4. Dream 三档全 Weak Reject — 即使 pivot 后仍需 re-dream 验证，不能假设 Analysis Paper 自动更好
5. 用户(孙震)反复强调"scope 不足" — StrategyQA + ARC 已加入 plan，但如果全部 SICA≈SC，strong accept 仍极难，重心在分析深度（capability trap formalization）


---
