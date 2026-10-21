# reviewer / loop_6.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`270434427ba0f82bf26f.json`](../../sessions/27/270434427ba0f82bf26f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-04-27T12:04:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- **comm_gate_mas 只能用 cuda:1**。cuda:0/2/3 属于其他项目，三次越界事故（D184/D187/D188）已有记录，再犯 Director 直接 CRITICAL
- 所有 vLLM 启动命令必须以 `CUDA_VISIBLE_DEVICES=1` 开头，不能依赖默认值（默认会跑 cuda:0）
- 服务器名是 `westb-4x6000-a`（不是带括号的 `westb-4x6000-a(comm_gate)`，后者会报 unknown server）
- Registry model_name `Qwen3-8B-Instruct` 是错的，官方名称是 `Qwen3-8B`（HF/ModelScope 上无 -Instruct 后缀）

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a，4× RTX PRO 6000 Blackwell **96GB**（不是 A6000 48GB）
- 远程工作目录：/root/autodl-tmp/comm_gate_mas，conda base 环境（/root/miniconda3/bin/python）
- 本地工作目录：/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/
- 模型路径：Llama=/root/autodl-tmp/models/Llama-3.1-8B-Instruct，Qwen3=/root/autodl-tmp/models/Qwen3-8B
- 活跃进程（截至 19:20 UTC 4/27）：vLLM PID 646896 on cuda:1（83.7GB, Llama serving）；P0 实验 tmux `p0_seeds_123_456`
- cuda:0 有 PID 674423（4.5GB, 非本项目）；cuda:2/3 空闲
- Oracle labels 数据：outputs/oracle_labels/llama_n300_traces.jsonl（297 tasks, 1782 msgs）
- GPT-4o 完全被 429 阻塞（precompute.log 确认 0/1782 成功）

### 3. 📊 当前状态
本轮审查了 4 个 worker：
1. **P5 dryrun config** → WARNING（registry model_name 错误、spec 不完整、单 seed 需明确定位）
2. **Claude API feasibility** → WARNING（脚本用 Sonnet 但推荐 Haiku、κ 验证 pipeline 未实现、跨 oracle 论文影响待处理）
3. **R12 weakness prescan** → WARNING（prescan 质量高但遗漏 qwen_10run 元数据矛盾、M3 Qwen length-only 优先级应提升）
4. **R12 text fixes** → PASS（C1 弱化 72B wording + M6 backbone count，6 处修改全部验证通过）

Registry 状态：
- RUNNING：`e2e_llama_gsm8k_n300_clean`（P0 seeds 123+456，seed 123 在 task 15/300）
- PREPARING：`llama_length_only_gsm8k_5seed`（cuda:0 BLOCKED）、`e2e_qwen3_8b_gsm8k`（P5，等 P0 完成）、`oracle_qwen_gsm8k`（非关键路径）、`5run_pruned_rerun`（failed）

### 4. 📋 待办（条件触发式）
- P0 seeds 123+456 完成 → 审查 3-seed 聚合指标（与 seed42 的 +1pp 是否一致），检查 vLLM 是否正常关闭
- P5 启动 → 核实 vLLM 用 `CUDA_VISIBLE_DEVICES=1` 启动 Qwen3-8B，确认 `/no_think` 生效
- Claude κ 验证完成 → 检查 κ 值（>0.8 走方案 A，<0.8 走方案 C），确认用的是最终生产模型而非 smoke test 模型
- D189 checkpoint 4/28 06:00 UTC → 若 P1 oracle precompute 未完成，P2 降级为 limitation
- Qwen length-only baseline 若启动 → 验证 GPU 分配（当前标注 cuda:0 BLOCKED）

### 5. 🎯 战略上下文
- **NeurIPS DDL**: abstract 5/3-4, paper 5/5-6。48h 硬限 4/29 00:00 UTC（D175/D189）
- **核心叙事**：Dual-backbone non-inferiority + scale-stable pruning。Llama +2.1pp vs Qwen +0.4pp，72B 零翻转但单 seed
- **D191 决策树**：Claude oracle (κ>0.8) > limitation > Qwen-7B oracle（否决）。GPT-4o key 完全 429，Claude 是唯一替代
- **易错点**：
  - `Qwen3-8B` 就是 instruct 模型（Qwen3 系列不加 -Instruct 后缀），不要当成 base model
  - qwen_10run_oracle_gsm8k 有两条矛盾的 failure_reason + conclusion:success，数据是对的但元数据需清理
  - P0 的 `run_p0_seeds_123_456.sh` 曾有 CUDA_VISIBLE_DEVICES=0 bug（D188），当前是手动启动绕过的，脚本本身可能仍未修正
  - llama_length_only_gsm8k_5seed 标注 cuda:0 但白名单只有 cuda:1，实验无法启动除非 Director 批准 GPU 扩展


---
