# director / loop_3.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`283f6abf049c3ffff177.json`](../../sessions/28/283f6abf049c3ffff177.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T10:08:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-37397 的 cuda:0 和 cuda:1（项目配置白名单，无其他卡）
- Table 1/2/3 数据**必须统一用 standard profiling**（D033/D034），hires profiling 只能作为独立 ablation 展示，禁止混入主表对比 heuristic baselines
- Mistral MCKP 参考值必须用 k=16 的 7.3106（D035/D036），禁止引用 k=18 的 7.3231
- C4 calibration 数据已被确认污染（实为 WikiText，D032），任何涉及 C4 的旧实验结果无效，必须用真 C4 重跑
- 投稿 ARR May 25, 2026（距今 11 天），不得 fallback 到低级别会议

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397 (connect.westd.seetacloud.com)，2× RTX PRO 6000 96GB (cuda:0 + cuda:1)
- 工作目录：/root/ratekv
- Python/conda：未详细探查，Agent 此前已配好可直接用
- 审稿群（Group C）已激活：review_chat_id=oc_ec66209ede0ea4e3bda924778c210d8e
- Paper Agent 已激活，writing_plan.yaml 已审批（D031）
- 无 W&B 配置，无弹性 GPU

### 3. 📊 当前状态
**刚做完**：D032-D036 系列数据一致性修正（C4 污染确认、Table 统一 standard profiling、Mistral k=16 修正）。所有 make-or-break 条件已在 D030 解除。

**Agent 队列**：depth=2，正在处理 Mistral k=16 PPL 不一致排查指令 + 1 个 worker:done 回调 + 1 个 D035 修正指令。idle 663s。

**实验状态**：
- RUNNING: multi_seed_error_bars（plan_017，统计可信度）
- PREPARING: c4_rerun_d032（真 C4 重跑）、cross_domain_calibration_v2（plan_010 用真 C4）、greedy_constrained_ablation（plan_016 补充）
- 47 个实验总计，24 success / 9 negative / 6 failed / 剩余 killed 或 PREPARING

**写作**：Paper Agent 已启动，writing_plan.yaml 审批通过（Option 2 问句标题），正在写作中。

### 4. 📋 待办（条件触发式）
- Agent 消化完当前 queue（depth→0）→ 检查 multi_seed_error_bars 进度 + c4_rerun_d032 是否启动
- multi_seed_error_bars 完成 → 检查 3-seed error bars 是否足够窄支撑 claim，更新 paper_framing.md
- c4_rerun_d032 完成 → 验证真 C4 cross-domain 结果，plan_007 + plan_010 数据更新
- Paper Agent 汇报写作进展 → 审查 claim 与最新数据（特别是 standard profiling 一致性）是否对齐
- 收到审稿报告 `[审稿报告]` → 按 review-report-action skill 走 Holistic Pass + Action Matrix
- P1 实验 kv_separation (plan_014) 和 downstream_eval (plan_012 补跑) 完成 → 评估是否扩充论文

### 5. 🎯 战略上下文
**核心结论链**：D005 MSE falsified → D007 pivot to quant-only → D009 constrained MCKP → D010 MVP PASS (11.23 vs 15.45) → D019/D021 solver equivalence (greedy=MCKP, Δ=0.0000) → D022/D023 两层贡献 (constraint 防灾难 + profiling 微调) → D030 所有条件解除。

**论文核心 narrative**："cardinality constraint 是 THE contribution"——一个简单约束让任何 solver 在 {2,4,8,16} 上都能找到最优解；heterogeneity 分析告诉你什么时候值得做非均匀分配。

**易踩的坑**：
1. 不要把 hires profiling (10.91) 和 standard profiling (11.23) 数字混用——Table 3 heuristic baselines 全在 standard profiling 下，MCKP 必须用 11.23 对比
2. Mistral 是 genuine negative（profiler zero-signal，total_distortion=0.0），不是 k 选择问题——不要试图通过调 k 来"修复"
3. C4 旧数据全部无效（实为 WikiText），任何引用旧 C4 结果的分析需要等真 C4 重跑
4. Solver equivalence Δ=0.0000（不是 0.0012，那是旧的四舍五入 artifact）
5. Paper Agent 和 Main Agent 不直接通信——需要补实验数据时 Paper Agent 报给你，你再派 Main Agent


---
