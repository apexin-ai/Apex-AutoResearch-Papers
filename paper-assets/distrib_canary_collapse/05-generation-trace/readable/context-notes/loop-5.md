# director / loop_5.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`13d93320f5f970a1eaec.json`](../../sessions/13/13d93320f5f970a1eaec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T04:22:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 / cuda:1（westd-19828，RTX PRO 6000 Blackwell 96GB × 2）
- Agent 反复 idle→reset 循环已出现 4-5 次（过去 ~10 小时），新 session 未正常消费消息队列。发任务后必须验证 Agent 确实在处理，不要发完就等
- ECE 作为 co-primary canary 仅限高 α（≥0.50 待确认），低 α 下 gen 1 反向信号（D021）
- analyze_alpha_sweep.py 的 f² guard 已修复（df_resid<20 输出 "df_too_low"），不要回退
- paper_framing.md 已加到约束 #21，Claim 1 α 适用范围等 a050 数据再定，不要提前改措辞

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base 环境）
- HF cache：/root/autodl-tmp/.hf_cache
- 模型：Pythia-410M（HF 自动下载）
- 数据：/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k
- 活跃进程：a050_s42（cuda:1）和 plan_006_s42（cuda:0）应已完成或接近完成——因 Agent 循环挂机，无人检查最终状态。优先 SSH 确认

### 3. 📊 当前状态
本 session 完成：处理 Reviewer Loop#5 巡检 → 修复 plan_002 orphaned registry + plan_006 registry_id → 审批+分配 a050_s42 → a025_v3 完成分析（dose-response 确认）→ f² guard bug 修复 → 记录 D021（ECE regime 限定）/ D022（Claim 2 reframe + Claim 1 待 a050）→ 更新 paper_framing.md 约束 #20/#21

Registry RUNNING（但可能已完成，需 SSH 确认）：
- alpha_sweep_a050_s42（cuda:1，α=0.50, 10gen，预估 04:30 UTC 完成）
- plan_006_s42（cuda:0，α=1.0, 20gen, 10000 steps/gen，预估 09:00 UTC 完成）

未执行的任务（因 Agent 循环挂机被阻塞）：
- a050 完成分析（三点 a000+a025+a050 analyze_alpha_sweep.py）
- dose-response drift 数据整理（artifacts/dose_response_drift.csv）
- a075/a010 提交（命令上一个 session 已验证，随时可提交）
- plan_006 进度检查和指标趋势

### 4. 📋 待办
- **首要**：SSH 检查 a050_s42 和 plan_006_s42 是否已完成 → 更新 registry → 如已完成立即运行分析
- a050 分析完成 → 差分 Granger 显著？→ 是：Claim 1 = "α ≥ 0.50"（D022 情景 a）；否：Claim 1 限定 "α=1.0 only"（D022 情景 b/c）
- a050 完成 + cuda:1 释放 → 提交下一个 α 点（a010 优先——精确化 regime boundary 下界；如 a050 差分 Granger 不显著则改 a075）
- plan_006 完成 → 跑 analyze_extended.py（diversity lead robustness at T=20）+ permutation Granger at T=20（验证 power 提升）
- plan_006 cuda:0 释放 → 提交 plan_006_s43（第二 seed）或其他 P0/P1 实验
- Reviewer 已收到 a050 gen 1 信号评估请求（entropy -22.2%, ECE +519%），回复后处理

### 5. 🎯 战略上下文
- 决策链：D011-D013（TY 不可靠）→ D014（Dream 5 项修复）→ D015（TY 降级）→ D017（perplexity 伪回归）→ D019（ECE conditional secondary）→ D020（ECE 待升级）→ D021（ECE regime-dependent，高 α only）→ D022（Claim 2 reframe detectability + Claim 1 等 a050）
- **a050 是当前 pivotal experiment**：决定 Claim 1 的 α 适用范围表述和整个论文强度
- Claim 2 已 reframe 为 "detectability varies"（非 "lead time varies"），primary evidence = raw drift magnitude 不依赖统计方法
- Claim 3 升级候选："Method × Regime Interaction"——无论 a050 结果都成立
- **最容易判断错的事**：(1) 不要用 naive_xcorr 做 Claim 2 primary evidence（与 Claim 3 矛盾）；(2) TY 的 sig rate 在 α=0.25 (38%) > α=1.0 (25%)，非单调，不能用 TY 画 dose-response；(3) Agent 发消息后必须验证在处理，本 session 反复出现发消息后 Agent 实际未执行的情况


---
