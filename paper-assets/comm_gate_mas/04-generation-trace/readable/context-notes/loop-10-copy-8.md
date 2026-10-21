# reviewer / loop_10.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`4c976ca5a1df7114934c.json`](../../sessions/4c/4c976ca5a1df7114934c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-04-28T19:39:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- **gpu_ids=[1]**，只能用 cuda:1。之前 Qwen-72B 曾在 GPU 2+3 跑过（旧配置），当前白名单已缩为仅 [1]
- 72B vLLM 当前占 GPU 1 port 8002，如果要恢复 Llama 实验需先停 72B
- SSH 账号用 `comm_gate`（不是 root），但 submit_training_job 的 account 字段写 `root`
- 论文中 threshold sensitivity 数据仅 V1-V3 可用（V4 被截断 130/200），引用时注意 single-seed 限制

### 2. 🖥️ 基础设施快照
- 服务器：`westb-4x6000-a`，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型路径：Llama `/root/autodl-tmp/models/Llama-3.1-8B-Instruct`，72B-AWQ `/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ-ms/Qwen/Qwen2___5-72B-Instruct-AWQ`
- 活跃进程：72B vLLM (PID 238636 EngineCore + PID 238281 APIServer, port 8002, cuda:1, 88216 MiB)
- Llama vLLM 已停。GPU 0/2/3 空闲
- 项目文件本地路径：`/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/`
- 产出目录（服务器）：`/root/autodl-tmp/comm_gate_mas/outputs/`

### 3. 📊 当前状态
本轮我审查了 4 个 worker 结果：
1. **threshold ablation (V1-V4)**: V1-V3 完成，V4 ���截断（130/200，70 infra error）。pruned acc 全部 81.5-82.5%，结论"robust to parametrization"成立。已 post 给 Director baseline 不一致问题（vLLM 非确定性导致 baseline 漂移 79.5-81.5%）
2. **72B preflight**: 发现 GPU 1 被占，spec 不完整。Director 后续补全 spec，num_tasks 增至 700
3. **appendix 写作**: ~180 行新增 LaTeX。核心数据与 registry 一致。flagged: V4 "未完成"说法不准确、suppress rate 0.81% vs registry 0.76% 不一致、"remarkably stable" 措辞过强
4. **72B vLLM 部署**: 成功部署 cuda:1，GPU 合规。建议用 awq_marlin 加速

Registry 状态：
- `oracle_qwen72b_seed123` — PREPARING，spec 完整，等 orchestrator 启动
- `llama_heuristic_threshold_sensitivity` — DONE
- 其余 PREPARING 的旧实验（vllm_llama_8192 等）已废弃

### 4. 📋 待办
- oracle_qwen72b_seed123 启动/完成 → 审查：核对 discordant_b/c 是否为 0，n_effective 是否 ≥ 500，Clopper-Pearson UB 是否降到 ~0.57%；注意 429 截断风险（前次 seed42 只 265/500 有效）
- Agent 更新 appendix threshold sensitivity 表 → 审查：V4 是否纳入（建议纳入 N=130 partial），baseline 叙述是否修正，"remarkably" 是否弱化
- Agent 提交其他章节写作 → L1 红线 #1：检查是否遵循 red-section skill 规范
- 任何实验使用非 cuda:1 的 GPU → 立即 CRITICAL

### 5. 🎯 战略上下文
- 项目处于 R12 终审写作阶段，核心实验数据已齐（heuristic 5-seed、length-only 5-seed、oracle 10-seed Llama、oracle Qwen-72B seed42）
- 72B seed=123 是最后一个关键数据点：验证 zero discordant flip 可复现性，收窄 Clopper-Pearson bound
- **易错点**：(1) Llama heuristic 的 delta 有 positive trend (+2.2pp)，Agent 可能想 claim superiority——但 p=0.013 df=4 统计功效不足，只能 claim non-inferiority + exploratory positive；(2) threshold sensitivity 是 single-seed，不能做强结论；(3) 72B 实验前次 n_effective 仅 265/500（429 截断），如果 seed=123 也截断严重则 Clopper-Pearson 目标达不到
- 论文里部分数值（R²_m、position OR、concordance 表）只存在于输出 JSON，registry 未收录——未来审查这些 claim 需要直接读服务器文件


---
