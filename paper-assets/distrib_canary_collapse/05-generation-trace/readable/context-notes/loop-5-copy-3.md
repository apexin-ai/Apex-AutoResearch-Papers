# reviewer / loop_5.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`11bc35cf3dd93b45bd50.json`](../../sessions/11/11bc35cf3dd93b45bd50.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T04:24:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westd-19828 双卡）。当前 plan_006 占 cuda:0，a050 占 cuda:1。任何新实验必须等其中一张卡释放。
- alpha_sweep 系列（a000/a010/a025/a050/a060/a075）使用 wikitext103_5k + 5000 steps/gen；plan_006 使用 wikitext103 FULL + 10000 steps/gen。**两组实验不可直接做 dose-response 对比**，配置不同。
- a025 分析已发现 f² effect size 在 df_resid<20 时标记为 "df_too_low"（D019）。审查任何新的 Granger 分析结果时，检查是否遵守了这个 guard。

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- 结果目录：`results/alpha_sweep/a{NNN}_s42/` 和 `results/extended_20gen/s42/`
- 分析输出：`results/alpha_sweep/analysis/alpha_sweep_analysis.json`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/`
- 活跃进程（截至 handoff 时）：
  - plan_006_s42: cuda:0, PID 68368, gen 9/20（约 11 gen 剩余，~5.5h）
  - alpha_sweep_a050_s42: cuda:1, gen 7 训练中（~3 gen 剩余，~1-1.5h）
- alpha sweep 尚未启动：a010, a060, a075 状态 PREPARING

### 3. 📊 当前状态
刚提交 a050 中期轨迹分析报告（gen 0-6），发现三个关键问题：
1. **entropy 非单调下降**：a050 entropy 是"阶梯坠落+平台振荡"，一阶差分符号反复翻转 → 差分 Granger 可能仍不显著
2. **distinct_1 dose-response 非单调**：gen 6 时 α=0.25 的 distinct_1 drift (-37.4%) 比 α=0.50 (-33.0%) 更严重
3. **ECE regime transition 确认**：gen 1 ECE 方向在 α=(0.25, 0.50) 区间翻转（-15% → +519%）

等待 Director 对该报告的反馈。两个实验仍在 RUNNING。

### 4. 📋 待办
- a050 训练完成 cron 触发 → 审查完整 10 gen 轨迹 + Granger 分析结果。**重点：差分 Granger 是否显著？ECE→distinct_1 vs entropy→distinct_1 哪个更强？**
- a050 Granger 分析出结果 → 如果差分 Granger 仍不显著 → 立即提 [severity: warning] 建议 Claim 1 从 "Granger-leads" 弱化为 "temporally precedes"
- plan_006 完成 → 审查 20 gen 长程轨迹。注意 distinct_1 在 α=1.0 可能稳定在 ~0.078（gen 5-9 几乎不变），perplexity 指数爆炸（gen 9 已达 1787）。**distinct_1 可能不是极端 α 下的可靠 collapse 指标**
- a010/a060/a075 开始 RUNNING → 核查 GPU 分配合规 + config 参数正确性
- Director 回复中期报告 → 根据反馈调整审查优先级

### 5. 🎯 战略上下文
- **3 个 Core Claims**：(1) Canary Granger-leads diversity (2) Regime-dependent predictability (3) Method selection sensitivity
- **Claim 1 风险最高**：a025 差分 Granger 0/8 FDR 显著（U 型 entropy 导致），如果 a050 差分 Granger 也不显著（平台振荡导致），Claim 1 仅靠 naive xcorr（共趋势）支撑，因果声明站不住
- **Claim 3 反而被强化**：不同 α 产生不同 entropy 轨迹形状（U 型 vs 阶梯），导致同一方法在不同 regime 下表现迥异
- **最易判断错的事**：看到 naive Granger 8/8 显著就认为"canary 领先 diversity 已证实"——naive 不做一阶差分，无法排除共趋势假象。必须看差分/置换方法的结果。
- **dose-response 非单调性**：更多 α 不一定导致更多 distinct_1 下降。这可能是噪声（只有 2 个点），也可能是真实现象。需要 a060/a075 数据确认后再下结论，不要过早写进报告。
- **关键决策链**：D019（f² guard）→ D021（ECE α-regime 限制）→ D022（Claim 2 reframe 为 "detectability varies"）。审查新分析时检查是否遵守这些决策。


---
