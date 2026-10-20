# director / loop_2.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`10b99ad775f14e4ae172.json`](../../sessions/10/10b99ad775f14e4ae172.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T04:23:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 98GB）
- GPU 0 当前有 ~49GB 孤儿显存未释放，plan_002 因此 OOM 过。启动新实验前必须确认显存已清理
- VOTA 数据中 actual/expected 值对构成准泄漏（模型可能做 string comparison 而非 behavioral understanding），所有涉及 VOTA accuracy 的 claim 必须等 plan_001 ablation 结果才能定论
- format_training_data.py 截断 trace 时必须预留 CHAT_TEMPLATE_OVERHEAD=32 tokens，否则 TRL max_length=2048 会右截断 label（已踩坑两次：v1-v3 + v4）
- v4 checkpoint 已被 v5 覆盖（同路径），不可回溯

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 `/root/autodl-tmp/trace-verdict-study/`（推测，需确认）
- Python：`/root/miniconda3/bin/python`（aml-train 镜像，conda base）
- 模型 base：Qwen2.5-Coder-7B-Instruct
- Checkpoint 路径：`/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- 数据路径：`/root/autodl-tmp/trace-verdict-study/data/` 下 `{condition}_train.jsonl` / `{condition}_test.jsonl`
- W&B：未配置（`/root/.wandb_api_key` 不存在），训练日志走 tensorboard
- 活跃进程（handoff 时刻）：
  - plan_001 vota_no_ae_seed42: PID 953133, cuda:1（最关键实验）
  - plan_002 full_trace_label_only_seed42: cuda:0（可能仍在跑或已 OOM，需确认）
- Cron：v5 实验注册过 cron 监控，plan_001/002 的 cron 状态需确认

### 3. 📊 当前状态
**刚完成**：v5 重训三条件（修复 chat template overhead），结果确认三层梯度 no_trace 75.1% < full_trace 81.8% < VOTA 99.2%。项目已进入 research 阶段（D003 MVP PASS）。paper_framing.md + experiment_plan.yaml + Dream 模拟均已完成。

**正在运行**：
- `vota_no_ae_seed42`（plan_001）：cuda:1，去除 actual/expected 的 VOTA ablation，~2-3h 训练。**这是论文 make-or-break 实验。**
- `full_trace_label_only_seed42`（plan_002）：cuda:0，状态不确定（之前 OOM 过，Agent 报告已重新提交但 cuda:0 有孤儿显存）

**等待中**：plan_001 训练完成 cron 回调 → 评估 → 汇报 Director

### 4. 📋 待办
- plan_001 训练完成 → 跑 evaluate.py + bootstrap_compare 评估 → 汇报 Director 结果
  - acc >80% → "genuine behavioral understanding"，Claim 1 强 framing
  - acc ~75% → "trivial string comparison"，Claim 1 需降级为 "structured answer-key delivery"
  - 介于 75-80% → actual/expected 是主要贡献者但非唯一，median scenario
- plan_002 状态确认 → 如果 OOM 未恢复，清理 cuda:0 显存后重启
- plan_002 完成 → 评估 label-only loss 是否缩小 full_trace(81.8%) 与 VOTA 的差距
- plan_001 结论出来后 → 启动 plan_003（VOTA component ablation，4 sub-conditions）
- Registry 清理：plan_mvp_fulltrace 的 registry_id 应更新为 full_trace_seed42_v5；vota_seed42_v5 metrics 需从 eval_results.json 补全
- report.md 清理：待处理列表有废弃实验（vota_v2, no_trace_v2 等），需移除

### 5. 🎯 战略上下文
- **决策链**：D001（MVP 标准 ≥2pp+CI）→ D002（v1-v3 无效，match泄漏+截断）→ D003（MVP PASS, VOTA 95.63%）→ D004（full_trace collapse 是 chat template 截断）→ D005（v5 确认 full_trace 81.8%，Claim 2 从 "hurt" 改为 "VOTA 更优"）
- **最容易判断错的事**：
  1. eval_results.json 可能是旧文件（时间戳早于当前 checkpoint）。**永远用 bootstrap_compare.py 做新鲜推理评估**，不要信残留的 eval_results.json
  2. 训练 eval metrics（eval_loss, token_accuracy）不能预测分类 accuracy——trace tokens 占 99%+ 主导了这些指标
  3. VOTA v5 = 99.16% 看起来很好但 fail_recall=100% 是 leakage 红旗。不要在 plan_001 出结果前向用户/论文 claim "genuine understanding"
- **投稿目标**：EMNLP 2026 ARR，deadline May 25（还有 ~9 天）
- **paper_framing.md 已有完整 contingency**：Claim 1 两种结果 + Claim 2 三种结果都有对应 framing。Dream median 预测 plan_001 后 82%（+6.9pp）


---
