# reviewer / loop_11.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`0f38ded7012e2e037a78.json`](../../sessions/0f/0f38ded7012e2e037a78.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-04-28T23:33:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只分配 `cuda:1`（`westb-4x6000-a`）。cuda:0/2/3 属于其他项目或未分配，越界即 CRITICAL。
- `oracle_qwen72b_seed123` registry notes 写了 "port 8002" 但实际 config (`oracle_qwen72b_gsm8k_n500.yaml`) 用的是 **port 8000**。不要被 registry notes 误导去改 config 或启动 8002 端口的 vLLM。
- Pipeline Phase C 会自动恢复 72B-AWQ 到 port 8000。不要在 pipeline 运行期间手动启停 cuda:1 上的 vLLM。

### 2. 🖥️ 基础设施快照
- 服务器：`westb-4x6000-a`，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：`/root/autodl-tmp/models/Llama-3.1-8B-Instruct`、`/root/autodl-tmp/models/Qwen2.5-7B-Instruct`、`/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ-ms/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程（截至 05:28 CST）：
  - vLLM Llama-8B：PID 305967，cuda:1，port 8001
  - Llama StratQA heuristic：PID 319950（~142/200 tasks）
  - Pipeline 协调器：PID 341189（`run_cross_task_pipeline.sh`，Phase A 等待中）
  - tmux session `llama_heuristic_threshold_sensitivity` 仍在（旧实验已完成，壳还在）

### 3. 📊 当前状态
我审查了两个 worker：
1. `worker_gpu_heuristic_pipeline_script` — 部署了 4 实验 pipeline（Llama StratQA/ARC → Qwen StratQA/ARC → 恢复 72B）。发 3 个 warning（registry 未更新、spec 空、端口不一致）。
2. `worker_cpu_port_fix_verification` — 修复了上述 3 个 warning。PASS。

**Registry RUNNING/ALLOCATED/PREPARING：**
- `llama_heuristic_stratqa` — RUNNING（~142/200，Llama+StrategyQA heuristic pruning）
- `llama_heuristic_arc` — ALLOCATED（排队，Llama chain 第二个）
- `qwen_heuristic_stratqa` — ALLOCATED（Pipeline Phase B 第一个）
- `qwen_heuristic_arc` — ALLOCATED（Pipeline Phase B 第二个）
- `oracle_qwen72b_seed123` — PREPARING（等 pipeline Phase C 恢复 72B 后才能跑）

无等待中的 Worker 回调或 Cron。

### 4. 📋 待办（条件触发式）
- Llama StratQA 完成（200/200）→ 核实 `outputs/llama_heuristic_stratqa.json` 存在且指标合理，检查 Llama ARC 是否自动接力启动
- Pipeline Phase A 结束（PID 319949 退出）→ 核实 Phase B 自动切换到 Qwen-7B（port 8001 模型换了、StratQA 开始）
- Pipeline Phase C 恢复 72B → 核实 port 8000 可访问 72B-AWQ，然后 `oracle_qwen72b_seed123` 可以启动
- 任何 heuristic 实验出结果 → 核查 pruned_acc 是否与 GSM8K 基线（82-83%）同量级；cross-task 如果大幅下降（>5pp）需 warning
- `pipeline_sentinel.txt` 出现 "PIPELINE_DONE" → 全部 4 个 heuristic 实验应有结果，触发全面审查

### 5. 🎯 战略上下文
- 项目核心：LLM 多智能体系统中消息功能的实证研究。主要发现：ack 消息 information-sparse 可安全剪枝，但通信功能分化程度 architecture-dependent（D007→D009→D011 决策链）。
- 当前阶段：cross-task generalization 验证（GSM8K 已有 5-seed 结果，现扩展到 StratQA + ARC）。这是论文 claim "generalizes beyond GSM8K" 的关键证据。
- 易错点 1：**不要把 cross-task 的 single-seed (n=200) 结果当作与 GSM8K 5-seed 同等权重的证据**。cross-task 是 exploratory/appendix 级别。
- 易错点 2：**baseline accuracy 在 vLLM 推理下有 ~2pp 非确定性波动**（见 `llama_heuristic_threshold_sensitivity` notes）。审查 delta 时要考虑这个 noise floor，不要对 <2pp 差异过度解读。
- 易错点 3：registry 中有大量历史 FAILED/KILLED 实验（19 个告警），这些是正常迭代残留，不需要逐一审查。


---
