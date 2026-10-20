# agent / loop_9.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`f6e5811822c86436df2e.json`](../../sessions/f6/f6e5811822c86436df2e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-16T01:16:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单**仅** `westd-11235:cuda:0` 和 `westd-11235:cuda:1`，无例外
- DeepSeek 系列实验必须用**旧代码**（无 `load_best_model_at_end`），已注释为 `# TEMP_DISABLED`，不可取消注释——保证 DeepSeek 组内 checkpoint selection 一致
- 论文中 VOTA 叙事必须说 **"trace content truncation"**（91.7% 样本 trace 输入被截断），**禁止说 "label truncation/corruption"**（to_chat_text 保留 labels，D030/D034 已确认）
- 同一张表禁止混用 paired/unpaired bootstrap（Qwen=paired, DeepSeek 部分条件仍缺 `--save_predictions`=unpaired）；补齐 predictions 前不要在论文表中放 DeepSeek CI
- exception_only 99.83% 是**表征理论上限**，irreducible errors = id=901/905（GeneratorExit 误标记），不要试图"优化"这个数字

### 2. 🖥️ 基础设施快照
- 服务器：**westd-11235**，项目目录 `/root/trace-verdict-study`
- Python：检测镜像 `aml-train` → `/root/miniconda3/bin/python`（conda base，不是 venv）
- 模型：Qwen-2.5-Coder-7B + DeepSeek-Coder-6.7B（路径在各实验 spec 中，HF cache 位置需 SSH 确认）
- W&B：项目内已配置，run 名与 exp_id 一致
- 活跃进程：
  - `full_trace_1024tok_seed42`：PID 212643，cron 监控中，cuda:0（推测）
  - `debugbench_exception_only_seed42`：PID 216806，cron 监控中，cuda:1
- 活跃 Workers（3 个，均为 paper 修正任务）：
  - `worker_paper_fix_table1_deepseek_ft` — 修 Table 1 DeepSeek full_trace 数据
  - `worker_paper_fix_vota_token_count` — 修 VOTA token count 叙事
  - `worker_verify_deepseek_predictions` — 验证 DeepSeek predictions 文件

### 3. 📊 当前状态
**刚完成的关键事件：**
- `deepseek_full_trace_seed42_v3` DONE (success, acc=0.7916) — DeepSeek 4 条件终于齐了
- `debugbench_no_trace_seed42` DONE (success, acc=0.9671) — DebugBench no_trace 完成
- D030 CLOSED, paper framing v3.0 定稿，3 个 Paper Agent Workers 正在修正叙事

**RUNNING（2 个，占满 2 张 GPU）：**
- `full_trace_1024tok_seed42` — plan_006 trace length ablation 第 3 点（256/512 已完成）
- `debugbench_exception_only_seed42` — plan_005 DebugBench 最后一个条件

**QUEUED（1 个）：**
- `full_trace_2048tok_seed42` — plan_006 第 4 点，等 GPU 释放

**等待中：**
- 2 个 cron 回调（上述 RUNNING 实验完成时触发）
- 3 个 Worker 完成回调（paper 修正任务）

### 4. 📋 待办（条件触发式）
- `full_trace_1024tok_seed42` cron 回调 → 分析结果 + 更新 registry + 立即提交 `full_trace_2048tok_seed42` 到释放的 GPU
- `debugbench_exception_only_seed42` cron 回调 → 分析结果 → plan_005 DebugBench 三角完成（VOTA 99.77% / no_trace 96.71% / exception_only ?）→ 汇报 Director + 更新论文 generalization section
- plan_006 全部 4 点完成（256/512/1024/2048）→ 绘制 accuracy vs trace length 曲线 + 相邻条件 paired bootstrap/McNemar → 更新论文 Claim 2 evidence
- 3 个 paper Worker 返回 → 整合修正内容到论文草稿 → 推进 Reviewer 对抗迭代
- DeepSeek VOTA/no_trace 缺 `--save_predictions` → 补跑后用 paired bootstrap 重算 CI（论文表格需要）
- 256tok/512tok multi-epoch eval 待补（有 epoch 1/2/3 checkpoints 保留）

### 5. 🎯 战略上下文
- **DDL: ARR May 25 = 9 天**，路线图：5/17-18 初稿完成 → 5/19-21 Reviewer 对抗 → 5/24 提交
- **3/3 Core Claims 已确认**：C1 exception dominance (D029 finalized), C2 info density > gradient dilution (D034), C3 two-tier hierarchy
- **核心结论**：verdict prediction 本质是 fault detection，exception event 是最有效信号（99.83%），full trace 反而有害（info overload 贡献 74% of gap）
- **决策链**：D029 Claim1 定稿 → D030 VOTA 84.45% confirmed → D033/D034 叙事修正（trace truncation not label）→ framing v3.0
- **易错点**：
  1. DebugBench no_trace 96.71% 异常高（主实验 no_trace 仅 75.1%），可能因 DebugBench 任务更简单或数据特征不同——汇报时必须解释这个 gap，不要默认假设是 bug
  2. DeepSeek full_trace v3 acc=0.7916（vs Qwen 81.76%），差距小，但要注意这是用了 label-preserving fix 后的结果——和之前 28.5% collapse 完全不同，不要混淆
  3. plan_005 的 registry_id 在 experiment_plan.yaml 中是 null（planned），但实际 DebugBench 实验已在跑——下一个"我"需要手动关联或确认 plan_005 状态
  4. Paper Agent Workers 可能改错东西（特别是 D030 叙事修正涉及多个章节）——Worker 返回后必须 diff 审查，不要盲目 merge


---
