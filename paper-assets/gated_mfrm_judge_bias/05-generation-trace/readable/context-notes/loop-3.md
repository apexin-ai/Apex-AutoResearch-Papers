# director / loop_3.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`f958d6c86966d7b2f0ee.json`](../../sessions/f9/f958d6c86966d7b2f0ee.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-25T03:21:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：需通过 `get_project_status` 确认当前分配的 GPU IDs，不可使用未分配的卡
- EMNLP 2026 正文限 8 页（不含 Limitations 和 References），当前约 9.5 页，**后续必须压缩**
- Abstract 不超过 200 词（当前 ~193 词，已达标）
- 项目已进入审稿阶段（review_chat_id: `oc_4ec7f5464e5f8985d29c475e59d2f3f6`），论文格式/投稿由 Group C 负责
- experiments.tex 中 N=17 列数据全为 TBD，等 MCMC Phase 1 完成后回填

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/`
- 图表目录：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/`
- 编译：`cd docs/paper && latexmk -pdf -interaction=nonstopmode main.tex`（需先 `rm main.aux main.bbl` 等辅助文件触发完整重编译）
- MCMC Phase 1：PID 614592，GPU 0 运行中（667 MiB），预计 ~22:30-00:30 UTC 完成
- MCMC 完成后 cron 自动触发 post-MCMC 分析 pipeline（4 个脚本已就绪）
- DeepSeek 采集：16,257/18,000 (90.3%)，接近完成
- Judge 数据：LLaMA ✅ / Qwen local ✅ / Qwen3 ✅ / DeepSeek 🔄 / Sonnet ⛔ partial / Gemini ⛔ partial

### 3. 📊 当前状态
刚完成论文 5 项排版修改并已汇报用户：
1. Introduction 缩短（~650→~380 词）✅
2. Related Work 扩充（+11 条新引用）✅
3. Framework 主图移到 page 2 ✅
4. 从 appendix 提升 3 个图到正文（fig4_bias_vs_rho, fig5_cn_recovery, error prop 表）✅
5. 图表布局：pages 2-9 每页顶部至少一个图/表 ✅

MCMC Phase 1 自主运行中，无需干预。完成后 cron 回调会触发 post-MCMC pipeline。

### 4. 📋 待办
- MCMC Phase 1 完成（cron 回调）→ post-MCMC 分析自动运行 → 拿到 N=17 结果后回填 experiments.tex 中所有 TBD → 重新编译
- N=17 结果回填后 → 论文正文需从 9.5 页压到 8 页（优先压缩 experiments.tex 长段落，其次 background.tex）
- 压页完成后 → `submit_paper_to_review` 提交新一轮审稿
- DeepSeek 采集完成 → 确认是否需要追加到 MCMC 重跑

### 5. 🎯 战略上下文
- 核心 claim：G-MFRM 联合建模 judge bias + contamination 优于 sequential pipeline（OVB 理论 + 合成数据 51.2% RMSE↓ + Arena-Hard 实证）
- N=8 结果 Δτ 不显著（CI 包含零），N=17 是关键——power analysis 预测 N≈17 可达 80% power，这是当前最重要的待验证点
- 易错判断：不要因为 N=8 Δτ 不显著就弱化 claim——LOO-ELPD（Δ=-55.7, |Δ/SE|=5.9）已强烈支持 G-MFRM 预测拟合优势，ranking improvement 只是 power 不足
- 论文从 appendix 提升了 fig4_bias_vs_rho 和 fig5_cn_recovery 到正文——appendix 中对应位置已改为文字引用主文图，不要重复添加
- 表格编号已变：error prop table 现在是 Table 1（在 method.tex），main results 是 Table 2（在 experiments.tex）


---
