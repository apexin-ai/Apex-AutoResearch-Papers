# director / loop_2.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`b6440422a5654b6ac5f6.json`](../../sessions/b6/b6440422a5654b6ac5f6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T01:58:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-16980 的 cuda:0 和 cuda:1（2× A100 80GB），不得使用其他 GPU
- Cron PID 追踪已导致 4 次假失败→cleanup worker 误杀合法进程的恶性循环。**所有 cron 已清除，禁止为当前实验重新创建 cron 监控**。实验完成判断改用手动 `wc -l` 输出文件行数（SciERC=551, DocRED=998）
- Registry 中 semantic_only 和 full_s1 状态为 DONE(failed) 是假失败（EXIT_CODE=129 来自 cleanup worker 误杀），实际 _v2 干净数据已跑完 551/551。完成后需手动 update_registry conclusion=success
- full_s2 registry 也是 DONE(failed)，实际进程 PID 144858 仍在运行。同理需手动更新
- CF violation 数据（full_s1 = 9.9%）**必须在论文中主动报告**，不得隐藏

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/schema_semantic_constrained_ie
- 输出目录：/root/schema_semantic_constrained_ie/outputs/
- 模型：Qwen3-8B（路径需 SSH 确认，应在 /root/autodl-tmp/ 或类似位置）
- 活跃进程（截至 handoff 前）：
  - full_s2: PID 144858, cuda:1, ~415/551（预计已完成或接近完成）
  - DocRED Phase 2 grammar_only: 应已在 cuda:0 启动（Agent 有指令）
  - semantic_only_v2 和 full_s1_v2: 已完成 551/551
  - docred_schema: 已完成 998/998
- W&B / Git: 未配置
- Cron: 全部清除，0 个活跃

### 3. 📊 当前状态
**刚完成**：Phase 2 SciERC 核心结果确认 + paper_framing.md 全面更新（集成 Reviewer 的 3 个 framing 修正）+ ROADMAP 更新 + D006 决策记录

**Registry 实验状态**：
- phase2_scierc_unconstrained: DONE(success) — baseline DR=15.37%
- phase2_scierc_grammar_only: DONE(success) — DR=14.84%, RV/ET=0%
- phase2_scierc_semantic_only: DONE(failed) — 实际已完成，DR=11.65%（需更新 registry）
- phase2_scierc_full_s1: DONE(failed) — 实际已完成，DR=0.93%（需更新 registry）
- phase2_scierc_full_s2: DONE(failed) — 进程可能仍在运行或刚完成（需确认）
- phase2_scierc_full_s2: PREPARING — 可能有重复注册
- mvp_phase0_docred_schema: DONE(success) — DocRED schema-informed DR=12.8%

**等待中**：
- Agent 回复：DocRED Phase 2 grammar_only 启动状态 + full_s2 完成后的 violation_checker 结果
- 无活跃 cron / worker 回调

### 4. 📋 待办
- full_s2 完成（wc -l = 551）→ 跑 violation_checker + F1 → 对比 S1 vs S2 trade-off（特别关注 CF violation 是否比 S1 低）→ 更新 registry
- semantic_only / full_s1 registry 仍为 DONE(failed) → 让 Agent update_registry conclusion=success + metrics（基于 _v2 干净数据）
- DocRED Phase 2 grammar_only 完成 → violation_checker → 接着跑 DocRED full_s1 → 跨数据集验证核心 claim
- S2 CF violation < S1 → 考虑 S2 作为推荐策略；S2 CF ≈ S1 → CF 是约束方法的固有 limitation
- 所有 Phase 2 数据齐全后 → 启动 Paper Agent（Full Draft 模式，投 EMNLP 2026 ARR May 25）
- 如有 GPU 空窗 → Evaluate-for 残留 error case 分析（抽 10 个案例看模式）

### 5. 🎯 战略上下文
**核心结论链**：D001-D006。最重要的是 D006：Full S1 DR↓94% F1-neutral 已确认。

**paper_framing.md 刚做的 3 个关键修正**（Reviewer 建议，已写入文件）：
1. "协同效应" → "complementary with enabling dependency"（grammar 是 semantic 的前提条件，不是双向增强）
2. F1 +0.13pp 不可声称改进 → 只能说 "F1-neutral"（单 seed 无 CI，~1-2 TP 差异）
3. CF violation 9.9% 作为新 Reviewer Concern C7 加入，defense 策略：DR 是结构性错误 vs CF 是标注不一致

**易错点**：
- 不要把 registry DONE(failed) 当成实验真的失败了 — semantic_only/full_s1/full_s2 都是 cron 假失败
- 不要重新创建 cron 监控 — 改用手动 wc -l 轮询
- DocRED Phase 2 代码已就绪（零修改 `run_constrained_extraction.py --dataset docred`），但 DocRED 998 样本比 SciERC 551 慢，预留更多时间
- EMNLP ARR DDL May 25，距今 11 天，还需完成：DocRED Phase 2 + S2 分析 + CF 分析 + 论文写作


---
