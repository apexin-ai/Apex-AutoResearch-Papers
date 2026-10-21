# reviewer / loop_12.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`c25edd5b40734c5f5907.json`](../../sessions/c2/c25edd5b40734c5f5907.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-04-29T02:55:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目在 westb-4x6000-a 上历史一致使用 cuda:1，其余 GPU 未见分配记录。越界使用其他 GPU 需先确认 project config 的 gpu_ids 白名单。
- SSH 服务器名是 `westb-4x6000-a`（不是 `westb-4x6000-a(comm_gate)`，后者会报 unknown server）。
- ARC 实验（llama_heuristic_arc / qwen_heuristic_arc）已标记 INVALID（D226），extract_arc_answer() regex 在 round-robin 格式下失效，baseline 准确率在 floor（10-16%）。**不要引用这两个实验的数据**，等 v2 修复后重跑。

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python3`（conda base 环境）
- 模型：`/root/autodl-tmp/models/Llama-3.1-8B-Instruct`（8B），Qwen2.5-7B / 72B-AWQ 同目录
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃 vLLM：PID 519262（父）→ 519538（EngineCore），Llama-3.1-8B on port 8001, cuda:1, `--max-model-len 4096 --gpu-memory-utilization 0.90`
- 活跃实验：`scripts/run_stratqa_3seed.sh` 正在跑 seed=0（截至 08:51 CST 已完成 42/200）
- 输出目录：`outputs/llama_heuristic_stratqa_3seed/`（run.log + 未来 seed_0/1/2.json）

### 3. 📊 当前状态
我刚完成 worker_check_stratqa_3seed_status 的审查，已发送 WARNING 级报告给 Director。

**核心发现**：
- 实验实际在运行但 registry 状态卡在 PREPARING（retry_count=2），bookkeeping 未更新。
- vLLM max-model-len=4096 导致 task 26（strategyqa_0025）400 Bad Request 被跳过，错误率 1/42=2.4%。
- GPU1 88% util，无越界。

**Registry RUNNING/PREPARING**：
- `llama_heuristic_stratqa_3seed`（PREPARING）— 实际在跑 seed=0, ~42/200, ETA 每 seed ~53min
- `oracle_qwen72b_seed123`（PREPARING）— 72B oracle 复现，未启动
- 其余 PREPARING 实验（vllm_llama_8192_v2 等）长期搁置

### 4. 📋 待办（条件触发式）
- llama_heuristic_stratqa_3seed 完成 → 检查每 seed 的 infra_error 数。若任一 seed >10/200（>5%），severity 升级为 CRITICAL，建议增大 max-model-len 重跑。
- llama_heuristic_stratqa_3seed 完成 → 交叉验证 3 seed 的 delta_pp 与原 seed=42（+6.5pp）的一致性。CI 是否排除 0 是核心 hypothesis。
- ARC v2 实验出现 → 重点审查 extract_arc_answer() 修复是否解决 regex 问题，baseline acc 应 ~54%（非 10-16%）。
- Agent 更新 registry 状态为 RUNNING → 确认 bookkeeping 已修复。

### 5. 🎯 战略上下文
- 项目核心：LLM 多智能体系统中通信功能的实证研究。heuristic ack pruning 是核心方法——去除 acknowledgment 消息不伤准确率（Llama GSM8K +2.2pp CI[0.41,3.99], Llama StratQA +6.5pp）。
- 3-seed StratQA 是关键复现实验：如果 CI 不排除 0，+6.5pp 单 seed 结论不可信。
- ARC 跨任务泛化目前 INVALID（D226 answer extraction bug），是已知缺口。
- 易错点：vLLM `--gpu-memory-utilization 0.90` 导致 8B 模型占 88GB 显存，**这不是模型错配**，是 vLLM 预分配行为。不要因此误判。
- 易错点：pipeline.log 最后记录了 72B-AWQ 在 port 8000，但该进程已被 kill，当前仅 Llama-8B 在 port 8001。不要假设 72B 仍在运行。


---
