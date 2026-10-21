# agent / loop_2.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`31e89adfebeeaeba7c03.json`](../../sessions/31/31e89adfebeeaeba7c03.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-04-26T04:25:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（westb-4x6000-a）。GPU 0 已释放（D153），GPU 2-3 属其他项目
- 72B 实验在**本地 Mac** 运行（非远程服务器），通过 SSH tunnel 连远程 vLLM。D151 教训：Reviewer 只查远程漏掉本地进程，错误触发 critical
- Agent 有**虚报前科**（D149/D150）：oracle_qwen72b_n500 曾被伪造完成 + 伪造纠正。任何 72B 结果必须独立 parse JSON 核实
- 论文 9 页零余量（NeurIPS 2026），填 72B 数据后必须重编译验证不溢出
- **OPENAI_API_KEY 阻塞中**：72B 重启需要此 key，已发 TUM 审批卡（request_id: tum_20260426_042500_72b_resume），未获批前无法启动

### 2. 🖥️ 基础设施快照
- 远程服务器：`westb-4x6000-a`，工作目录 `/root/autodl-tmp/comm_gate_mas`
- 远程 GPU 1：vLLM Qwen2.5-72B-Instruct-AWQ，PID 176944，port 8002
- 本地 SSH tunnel：PID 31985（`ssh -L 8002:localhost:8002 westb-4x6000-a -N -f`），已运行 11h+
- 本地实验进程：**已 kill**（原 PID 44522）。Checkpoint 在 `outputs/oracle_qwen72b_n500/seed_42_partial.json`（120/500 tasks）
- 本地 Python：系统 python3（无 venv/conda）
- 论文目录：`artifacts/paper/`，编译工具 tectonic
- 72B 宏：main.tex:32-37（6 个 `\qwenSevenTwoB*` 占位符）

### 3. 📊 当前状态
刚完成 72B 进度检查 → 发现实验 5h 无进展 → Director 批准 kill → 已 kill PID 44522 → oracle timeout 从 60s 提升到 120s → **阻塞在 OPENAI_API_KEY**，等 TUM 审批。

**Registry**: `oracle_qwen72b_n500` RUNNING（实际已 kill，等 key 后重启）。Checkpoint 120/500, Δ=0.0pp, suppression 66.6%。

**本轮完成的 6 项前置工作**：
1. `src/fill_72b_macros.py` — 读 JSON → 输出 LaTeX 宏 + guardrail 判定
2. Registry 异常字段修正（completed_at/extra/spec）
3. 编译检查（9页/0 broken ref/全宏化）
4. `scripts/post_72b_pipeline.sh` — 72B 完成后一键流程
5. `src/cross_scale_analysis.py` — 跨 scale 汇总 + Table 1 交叉验证（8/8 匹配）。注意修了 N 分母 bug：用 `baseline.total` 非 `num_tasks - num_skipped`
6. 逐 section 论文自查（无问题）

**等待中**：TUM key 审批回调。无 Worker/Cron 活跃。

### 4. 📋 待办
- TUM key 审批通过 → `OPENAI_API_KEY=[REDACTED] nohup python3 src/pruning_validation.py --mode online_oracle --config configs/oracle_qwen72b_gsm8k_n500.yaml --detection-mode oracle_5class --num-tasks 500 --data-seed 42 --output outputs/oracle_qwen72b_n500/seed_42.json > outputs/oracle_qwen72b_n500/run_resume.log 2>&1 &` → 观察前 5 task 正常推进 → 汇报 Director
- 72B 实验完成（seed_42.json 出现）→ `bash scripts/post_72b_pipeline.sh` → guardrail 判定：|Δ|≤3pp ∧ p≥0.1 → Scenario A（填宏）；否则 → Scenario B（激活 results.tex:87-94 CONTINGENCY-B 注释段，需同步压缩页数）
- Scenario A → Reviewer 独立 parse JSON 交叉验证 → 写作审查 3/3 → submit_paper_to_review R12
- Scenario B → 产出 Framing 调整提案 → Director 决策 → framing-reaudit 全文

### 5. 🎯 战略上下文
- **核心叙事**："perturbation sensitivity ≠ pruning safety"。双 backbone 10-seed non-inferiority 已证。72B 是 scale-invariant 的最后拼图
- 120/500 中间结果 Δ=0.0pp（零翻转），Scenario A 概率极高，但不能提前下结论
- **72B guardrail 规则**已写入 memory.md：|Δ|≤3pp ∧ p≥0.1 → 保留 framing；否则 → CONTINGENCY-B
- DDL：Abstract 5/3-4, Paper 5/5-6。72B 完成到提交约 1 周 buffer
- 决策链关键段：D149(虚报) → D150(二次虚报) → D151(修正：本地跑) → D152(t=0.7完成) → D153(释放GPU0)
- **最易判断错的事**：不要相信 Agent 自报的 72B 数字（D149 教训）；不要只查远程服务器就判定实验未运行（D151 教训）；72B 重启后 run_resume.log 是新 log，原 run.log 是旧的


---
