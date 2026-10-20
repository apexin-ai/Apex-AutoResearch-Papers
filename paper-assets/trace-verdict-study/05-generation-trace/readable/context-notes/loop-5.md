# director / loop_5.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`8774aebe42d69082a504.json`](../../sessions/87/8774aebe42d69082a504.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T16:04:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-11235 上的 cuda:0 和 cuda:1（`gpu_constraint: ["westd-11235:cuda:0", "westd-11235:cuda:1"]`）
- DeepSeek exception_only epoch 1 = 99.83%，epoch 3 退化到 99.33%——D017 已确认是过拟合，论文中引用 epoch 1 数据，不要用 epoch 3 final
- ae_only 有 88% fallback 污染（locals dump 非干净 actual/expected），D013 已决定将其定位为"assertion-point 处的任何信息都是强信号"，不要试图做 clean ae_only ablation
- vota_seed123 已 FAILED（plan_008），别再重试同样配置；seed robustness 重心转为 deepseek 跨模型 seed

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，账户 root
- 工作目录：/root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 模型：Qwen-2.5-Coder-7B + DeepSeek-Coder-6.7B-Instruct（具体路径在远程）
- W&B：未配置；calibration 分析用本地 checkpoint logits
- 活跃进程：exception_only_seed123 (cuda:1), deepseek_full_trace_seed42 (cuda:0)——均为 GPU 训练任务，Agent 空闲

### 3. 📊 当前状态
刚完成：Qwen 全组件消融 + calibration 分析 + DeepSeek 4 条件中 3 个（no_trace/VOTA/exception_only）。D013 修正了组件层级（ae_only 99.92% 加入 Tier 1）。D016/D017 确认 exception signal 跨模型 universal。

RUNNING：
- `deepseek_full_trace_seed42` (cuda:0, plan_004 最后一个条件) — DeepSeek full trace 训练
- `exception_only_seed123` (cuda:1, plan_008 seed robustness) — Qwen exception_only seed=123

PREPARING（尚未提交）：
- `vota_seed456`, `exception_only_seed456`, `deepseek_exception_only_seed123`

等待中：deepseek_full_trace 完成后 plan_004 跨模型验证全部到齐 → 更新 paper_framing.md → 启动 Paper Agent Full Draft

### 4. 📋 待办（条件触发式）
- deepseek_full_trace_seed42 完成 → 与 deepseek_no_trace/VOTA/exception_only 汇总 → 更新 paper_framing.md 跨模型 section → 启动 Paper Agent Full Draft（投稿目标 EMNLP 2026 ARR May 25）
- exception_only_seed123 完成 → 检查是否与 seed42 一致（预期 ~99.8%），更新 plan_008 seed robustness 结论
- 两个 RUNNING 完成后 cuda:0/1 空出 → 立即派 seed robustness 剩余实验（vota_seed456, exception_only_seed456, deepseek_exception_only_seed123）填满 GPU
- Paper Agent 启动后 → 写作与 seed robustness 并行跑；plan_005 (DebugBench) 视时间决定

### 5. 🎯 战略上下文
核心发现：verdict prediction 本质是 fault detection。exception events 是近完美判别信号（99.83% 跨两个模型完全一致），VOTA 的 loop/ae 组件是 model-specific 的（Qwen 上 99.2% 但 DeepSeek 上仅 84.45%）。这个 "Tier 1 universal / Tier 2 model-specific" 发现是论文最强卖点。

决策链：D001(MVP 标准) → D003(MVP PASS) → D004(chat template bug) → D005-D006(full_trace 修复 81.8%) → D008(ae 非关键) → D010(exception dominance) → D011(two-tier hierarchy) → D013(ae_only 99.92% 修正层级) → D016-D017(跨模型 universal exception)

易错点：
- 不要把 DeepSeek VOTA 84.45% 当作负面结果——它恰恰证明了 non-exception 组件是 noise for weaker models，强化了 "exception-first" 设计原则
- Claim contingency（D014/D015）已被 D016/D017 解决——exception_only ≥95% 路径已确认，不需要 qualified 版本
- 10 天冲刺路线在 ROADMAP.md，5/24 提交 ARR，Paper Agent 尚未启动
- Review Group C 已 active（review_chat_id 已配置），论文提交走 `submit_paper_to_review`


---
