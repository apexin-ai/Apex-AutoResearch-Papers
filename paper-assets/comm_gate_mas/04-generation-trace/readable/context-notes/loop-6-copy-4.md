# agent / loop_6.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`c845049516a65c5fb4ec.json`](../../sessions/c8/c845049516a65c5fb4ec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-04-28T19:09:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（gpu_ids=[1]）。cuda:0/2/3 属其他项目，禁止使用
- 服务器账户是 `comm_gate`（SSH config name），实际 root 登录
- submit_training_job 命令必须自带 conda 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...`
- vLLM 服务驻留在 cuda:1 上，新实验提交前确认 vLLM 是否仍存活（端口 8000）

### 2. 🖥️ 基础设施快照
- 服务器：**westb-4x6000-a**，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base 环境，系统 Python 缺 pyyaml）
- 模型：Llama-3.1-8B-Instruct 通过 vLLM 服务（cuda:1, port 8000）；Qwen2.5-7B 同理
- 输出目录：`/root/autodl-tmp/comm_gate_mas/outputs/`
- 日志目录：`~/runs/comm_gate_mas/`
- 活跃进程：**无**（llama_heuristic_seed789_diag 已完成，无 RUNNING 实验）
- Cron：本项目无活跃 cron（其他项目有 7 个活跃 cron: cn_cifar_*, seed456_standard_vit, ir50_*）

### 3. 📊 当前状态
刚完成 **llama_heuristic_seed789_diag** 分析并推进到 DONE(success)。这是 Llama heuristic 5-seed 扩展的最后一颗种子。

**5-seed 汇总已计算并汇报 Director**：Mean Δ=+2.20±1.44pp, 95% CI=[+0.41, +3.99]（完全正向），non-inf δ=-3pp p<0.001。Registry 已更新，memory.md 已写入关键发现。

**PREPARING 实验**（6 个，均无 GPU 分配/无代码准备，属于积压）：
- vllm_llama_8192_v2, vllm_llama_8192 — vLLM 长上下文测试
- p1_oracle_precompute_llama_gpt4omini_recovery, p1_oracle_precompute_llama_gpt4omini — GPT-4o-mini oracle 预计算
- oracle_qwen_gsm8k — Qwen oracle
- 5run_pruned_rerun — 5-run 重跑

**等待中**：Director 回复（刚汇报了 5-seed 结果 + GPU 释放建议）。无 Worker/Cron 回调待处理。

### 4. 📋 待办
- Director 回复"释放 cuda:1" → 确认 vLLM 进程已 kill，通知 Director GPU 已释放
- Director 回复"写论文" → 读 latex-paper + reference-audit skill，派 CPU Worker 写指定 section
- Director 回复"补充实验 X" → 在 cuda:1 上用现有 vLLM 服务提交
- Director 指定 PREPARING 中某个实验开跑 → 派 Worker 准备代码 + dry-run → 提交审批
- Reviewer 评审结果到达 → 按 rebuttal skill 处理

### 5. 🎯 战略上下文
**核心叙事**（D214）：Dissociation finding — perturbation sensitivity ≠ pruning safety。Ack 消息对扰动最敏感但可安全剪除。

**关键数据已齐备**：
- Llama oracle 10-seed: Δ=+2.1±2.4pp
- Qwen oracle 10-seed: Δ=+0.40±1.02pp, TOST ±1pp p=0.048
- Qwen heuristic 10-seed: Δ=-0.05±0.99pp
- **Llama heuristic 5-seed: Δ=+2.20±1.44pp, CI 完全正向** ← 本轮新增
- Llama length_only 5-seed: Δ=-0.10pp, suppress 仅 0.76%（对比 heuristic 74.88%）

**易错点**：
- Llama heuristic TOST **equivalence** ±3pp FAILS（p=0.14），因为 mean 太正（上界 3.99>3）。但 **non-inferiority** 强通过。不要混淆这两个 claim
- ROADMAP 说"核心数据齐备，等 Reviewer"，不要自作主张跑新实验——除非 Director 明确指示
- P2 oracle（在线 GPT-4o 标注）已全线 fallback（D217），所有 API 路径穷尽，不要再尝试
- NeurIPS 2026 deadline：abstract 5/3-4, paper 5/5-6，写作时间紧迫


---
