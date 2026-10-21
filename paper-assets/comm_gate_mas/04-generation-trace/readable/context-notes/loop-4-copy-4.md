# agent / loop_4.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`ae8e1cd8167efbadbfdf.json`](../../sessions/ae/ae8e1cd8167efbadbfdf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-04-27T20:07:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（westb-4x6000-a）。cuda:0/2/3 分配给其他项目，禁止使用
- 72B 结果只能标注为 "single-seed preliminary"（N=265 统计力不足，D205）
- prompt_mod 对比禁止量化（76.2% vs 47.9% 来自不同实验模式 detect_only vs skip），只能方向性论述（D206）
- Heuristic 版本冻结为 v1（无 verbose_ack_patterns），所有论文实验必须用 v1（D198）
- P1 oracle 用 GPT-4o-mini（κ=0.822 > 0.8 阈值），不用 Claude（D199/D201）

### 2. 🖥️ 基础设施快照
- 服务器：**westb-4x6000-a**，4× RTX PRO 6000 Blackwell (96GB)
- 项目路径：服务器上具体路径需 SSH 确认（上一轮未写入 memory）
- 本地 repo：`/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/`
- 论文文件：`artifacts/paper/sections/*.tex`
- 活跃进程：
  - `stochastic_10seed_qwen_t07` PID=859482（cuda:1），cron 监控中，预计 4/28 03:00 UTC 完成
  - 其他 8 个 cron 属于其他项目（tinyimagenet, celeba, vit 等）

### 3. 📊 当前状态
**刚做完**：处理 P1 oracle precompute worker 卡死告警——确认 worker 已 cancelled，重新派发 recovery worker + prompt_mod 写作 worker。

**RUNNING 实验**：
- `stochastic_10seed_qwen_t07`：Qwen2.5-7B t=0.7 10-seed 复现（cuda:1，~8h）

**等待中的 Worker 回调**（2 个）：
- `worker_exp_p1_oracle_precompute_llama_gpt4omini_recovery_20260427T200514` — SSH 检查残留进程，恢复/重启 GPT-4o-mini 标注
- `worker_writing_prompt_mod_paragraph_revision_20260427T200532` — 修订论文 prompt_mod 段落

**Director 未完成指令**：4 项串行写作任务，任务 1 worker 在跑，任务 2-4 待推进：
- 任务 2：Discussion length-only vs heuristic model-dependent 表现
- 任务 3：Oracle 章节骨架（methodology.tex）
- 任务 4：72B 结果全文标注 single-seed preliminary

### 4. 📋 待办
- prompt_mod writing worker 回调 → 验证修改质量 → 汇报 Director → 派 worker 做任务 2（Discussion length-only）
- 任务 2 完成 → 派 worker 做任务 3（Oracle methodology 骨架，数据用占位符）
- 任务 3 完成 → 派 worker 做任务 4（72B 全文标注 preliminary）
- P1 oracle recovery worker 回调 → 检查是否成功启动 precompute → 更新 registry → 汇报 Director
- stochastic_10seed cron 回调（~4/28 03:00 UTC）→ 按 on-experiment-done 分析 → TOST 非劣效检验 → 汇报 Director
- stochastic 完成后 → cuda:1 排期：llama_length_only_gsm8k_5seed → P2 oracle_online_llama

### 5. 🎯 战略上下文
- **核心叙事**（D200）：Dissociation finding — perturbation sensitivity ≠ pruning safety，ack messages 最敏感但可安全剪枝
- **NeurIPS 2026 DDL**：abstract 5/3-4，paper 5/5-6。4/29 是 P2 硬限
- **双 backbone 复现已到位**：Llama Δ=+2.1±2.4pp, Qwen Δ=+0.40±1.02pp，non-inf 均 p<0.001
- **已知叙事漏洞**：Qwen length-only ≈ heuristic 统计不可区分，但 Llama length-only suppress 仅 0.81%（Qwen 42.2%），50x 差异 → Discussion 必须主动讨论 model-dependent 现象（任务 2）
- **易错点**：
  - P1 oracle precompute 之前 worker 反复卡死，可能是 API key 问题或脚本路径问题，新 worker 需要先排查环境
  - prompt_mod 数据千万不要量化对比（实验模式不同），只能说"方向性证据"
  - stochastic 完成后 GPU 排期紧张（3 个任务排队），不要漏掉 llama_length_only


---
