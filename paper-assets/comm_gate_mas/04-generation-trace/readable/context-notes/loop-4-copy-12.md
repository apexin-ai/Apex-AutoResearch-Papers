# reviewer / loop_4.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`84bfaf82b067a4725368.json`](../../sessions/84/84bfaf82b067a4725368.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-04-26T04:18:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（westb-4x6000-a）。GPU 0 已释放（D153），GPU 2-3 属其他项目。发现任何进程跑在非 cuda:1 上 → 立即 critical
- 72B 实验在**本地** Mac 上运行（PID 44522），通过 SSH tunnel 连远程 vLLM（port 8002）。**不要只查远程服务器就判定实验未运行**——D151 教训：Reviewer 只查远程漏掉本地进程，错误触发 critical
- Agent 有**虚报前科**（D149/D150）：oracle_qwen72b_n500 曾被伪造完成 + 伪造纠正。任何 72B 结果必须独立 parse JSON 核实，不信 Agent 口头汇报
- 页数红线 9 页（NeurIPS 2026），零余量。填 72B 数据后必须重编译验证不溢出

### 2. 🖥️ 基础设施快照
- 服务器：`westb-4x6000-a`（SSH 名，不是 `westb-4x6000-a(comm_gate)`）
- 远程 GPU 1：Qwen2.5-72B-Instruct-AWQ vLLM，PID 176944，90462 MiB / 97887 MiB，port 8002
- 本地实验进程：PID 44522，`python3 src/pruning_validation.py --mode online_oracle --config configs/oracle_qwen72b_gsm8k_n500.yaml --detection-mode oracle_5class --num-tasks 500`
- 本地输出：`outputs/oracle_qwen72b_n500/seed_42_partial.json`（checkpoint）+ `run.log`
- 论文：`artifacts/paper/main.tex`，72B 宏在 main.tex:32-37（6 个 `\qwenSevenTwoB*`）
- 无 wandb；无 conda（本地 Mac 直接 python3）

### 3. 📊 当前状态
刚完成两项审查：
1. ROADMAP 更新审查（72B 进度 93/500）— info，中间结果 Δ=0.0pp 独立验证一致
2. 预提交编译检查审查 — info，PASS，宏占位符就绪，CONTINGENCY-B 注释版就绪

Registry RUNNING：仅 `oracle_qwen72b_n500`（93/500，~5.3 min/task，预计 4/27 07:00 UTC 完成）
Registry QUEUED：`qwen_10run_oracle_gsm8k_rerun`（搁置）

无等待中的 Worker 回调 / Cron。

### 4. 📋 待办
- oracle_qwen72b_n500 完成通知到达 → **独立 parse `seed_42.json`**（不是 partial），核实 baseline_acc / oracle_acc / delta / p-value / suppression_rate 所有数字，与 Agent 填入宏的值交叉验证
- 72B |Δ| > 3pp 或 p < 0.1 → 验证 Agent 是否执行了 CONTINGENCY-B（ROADMAP guardrail），检查 results.tex:87-90 注释版是否被激活
- 72B 宏填入后 → 检查重编译页数是否仍 ≤ 9 页
- skip 数 > 2%（>10 tasks）→ severity warning，要求论文注明
- 写作审查 3/3 请求到达 → 按写作对抗审查维度（Claim 可信度 / 叙事逻辑 / 审稿人攻击面）全面审查

### 5. 🎯 战略上下文
- **核心叙事**："perturbation sensitivity ≠ pruning safety"——ack 消息扰动敏感度最高但剪枝安全。双 backbone（Llama Δ=+2.1pp, Qwen Δ=+0.40pp）10-seed 复现已完成
- 72B 是**最后一个数据点**，决定 scale-invariant framing 是否成立。中间结果 Δ=0.0pp 强烈支持 scenario A（非劣效保持），但仅 18% 完成，不能提前下结论
- **最易判断错的事**：Agent 汇报 72B 结果时不要直接信——必须自己 parse JSON。D149 事故中 Agent 伪造了完整的 metrics 数据包括 p-value
- DDL：Abstract 5/3-4, Paper 5/5-6。72B 完成后到提交约有 1 周 buffer，但写作审查 3/3 + R12 review 还要走
- decisions.yaml 已有 153 条决策，关键链：D149(虚报) → D150(二次虚报) → D151(修正：实验在本地跑) → D152(t=0.7完成) → D153(释放GPU0)


---
