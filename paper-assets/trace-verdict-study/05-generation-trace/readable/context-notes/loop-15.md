# agent / loop_15.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`f6f6d5a75cbb86928967.json`](../../sessions/f6/f6f6d5a75cbb86928967.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-18T01:39:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 westd-11235 cuda:0 和 cuda:1**，其他设备号严禁使用
- CodeLlama-13B 必须 `--gradient_checkpointing`（13B 显存紧张）
- 训练命令必须用 `/root/miniconda3/bin/python`（绝对路径），不可用 `python` 或 conda activate
- 每个实验 output_dir 必须独立：`/root/autodl-tmp/trace-verdict-study-checkpoints/{exp_id}/`
- `--max_steps` 控制训练长度（没有 `--epochs` 参数），默认 -1 = 全量（444 steps ≈ 3 epochs）

### 2. 🖥️ 基础设施快照
- 服务器：**westd-11235**，account=root，工作目录 `/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`
- 模型路径：
  - Qwen-7B: `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`
  - CodeLlama-13B: `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/`
  - DeepSeek-6.7B: `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- Checkpoints: `/root/autodl-tmp/trace-verdict-study-checkpoints/{exp_id}/`
- 活跃进程：codellama13b_full_trace_head2048_seed42, PID=391743, cuda:1
- Cron 活跃：监控 codellama13b_full_trace_head2048_seed42

### 3. 📊 当前状态
- **RUNNING (1)**: `codellama13b_full_trace_head2048_seed42` — CodeLlama-13B head-2048，验证跨 4 模型 signal positional concentration
- **ANALYZING (1)**: `qwen15b_full_trace_tail1024_seed42` — 等待分析（1.5B tail-1024 non-monotonicity 验证）
- **PREPARING (2)**: `codellama13b_full_trace_tail256_seed42`, `codellama13b_full_trace_tail1024_seed42` — Worker `worker_code_codellama13b_tail256_20260518T013828` 正在为 tail-256 准备代码
- **QUEUED (7)**: CodeLlama vota/no_trace/exception_only + Qwen-1.5B 全套 4 条件 — 等待 GPU 释放
- **Paper Agent patch 进行中**：budget curve + head-tail 跨模型数据写入论文
- **Round 6 审稿**：审批卡 pending 用户确认

### 4. 📋 待办（条件触发式）
- `codellama13b_full_trace_head2048_seed42` cron 回调 → 分析 head-2048 accuracy（预期 75-82%），更新 registry，与 3 模型 head-2048 对比汇报 Director
- `qwen15b_full_trace_tail1024_seed42` ANALYZING 状态 → 需立即 spawn Worker 做分析（可能是上个 session 遗留）
- Worker `codellama13b_tail256` 完成 → 提交 tail-256 实验到 cuda:0（当前空闲）
- head-2048 + tail-256 都跑完 → 提交 tail-1024（完成 CodeLlama budget curve 最后一格）
- CodeLlama budget curve 全部完成 → 提交 QUEUED 里的 CodeLlama vota/no_trace/exception_only（rebuttal 储备）
- Round 6 审稿用户确认 → 触发 Reviewer 审查新 budget curve 结果

### 5. 🎯 战略上下文
- **核心结论**: Exception events 是 test verdict prediction 的 minimal sufficient signal，跨 4 模型 3 架构 1.5B-13B 达 ≥99.33% accuracy
- **Budget curve 叙事**: 256→512 phase transition (+14.7~+23pp, architecture-invariant), tail-512 收敛 93-96%, tail-1024 收敛 96.5-96.6%
- **CodeLlama-13B 实验目的**: rebuttal 储备 + 证明跨 scale (1.5B→13B) universality
- **Non-monotonicity 修正**: 仅 DeepSeek tail 1024→2048 下降 1.5pp，不是 universal 现象（D066 已修正叙事）
- **易错点**: 
  - `qwen15b_full_trace_tail1024_seed42` 在 ANALYZING 但没被处理——可能是上轮 session 中断导致，接手后优先处理
  - cuda:0 当前应该空闲（只有 cuda:1 在跑 head-2048），可以立即提交 tail-256
  - QUEUED 的 7 个实验没有 hypothesis——提交前必须补
  - Reviewer 系统性 API Error 400 未修复，审稿流程可能受阻


---
