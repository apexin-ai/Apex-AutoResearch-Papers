# agent / loop_5.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`c50bbb263575652eca34.json`](../../sessions/c5/c50bbb263575652eca34.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-04-28T00:39:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目**只能用 cuda:1**，cuda:0/2/3 分配给其他项目，严禁使用
- 服务器 SSH 账户是 `root`（不是项目配置里的 `comm_gate`，之前 P1 oracle 因此卡在 PREPARING）
- P1 oracle precompute 是**本地 API 调用任务**，不要提交到服务器
- Heuristic 版本冻结为 v1（无 verbose_ack_pattern），所有论文实验必须用 v1（D198）
- 72B 结果只能标注为 "preliminary evidence of scale consistency"，不能说 "scale-stable"（D205）

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a（4× RTX PRO 6000 Blackwell 96GB）
- 工作目录：`/root/comm_gate_mas/`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen2.5-7B-Instruct via vLLM（PID 856695，运行 ~3h）
- 数据：`outputs/oracle_labels/llama_n300_traces.jsonl`（297 tasks, 1782 msgs）
- GPT-4o oracle 已完成：`outputs/oracle_labels/llama_n300_oracle.json`（1760/1782 entries）
- GPT-4o-mini checkpoint：`outputs/oracle_labels/llama_n300_oracle_gpt4omini.json.ckpt`（510/1782, 28.6%）
- 活跃进程：stochastic 10-seed（PID 859482, cuda:1），vLLM 服务（PID 856695, cuda:1）
- Cron：`stochastic_10seed_qwen_t07` 监控中

### 3. 📊 当前状态
刚处理了两个 Worker 回调：
1. **监控 Worker**：stochastic 10-seed 5/10 seeds 完成（seed_42/123/456/789/1024），seed_2048 进行中，ETA ~00:00-00:30 UTC（比原估 03:00 UTC 提前 ~2.5h）
2. **P1 诊断 Worker**：诊断出 P1 三次失败根因（旧 key 过期 + SSH 账户不匹配 + 服务器无 API key），发现本地已有完整 GPT-4o oracle

**Registry RUNNING**：`stochastic_10seed_qwen_t07` — Qwen2.5-7B t=0.7 10-seed 复现，验证 stochastic decoding 不降低 pruning safety

**等待中**：
- stochastic_10seed_qwen_t07 cron 完成回调（ETA ~00:00-00:30 UTC）
- **Director 决策**：P1 是用现有 GPT-4o oracle（免跑）还是继续 GPT-4o-mini precompute（需 API key，~53 min）——已通过 `main_agent_post_to_director` 提交，等回复

### 4. 📋 待办（条件触发式）
- stochastic cron 回调到达 → spawn worker 分析 10-seed 结果（TOST non-inferiority δ=-3pp）→ 更新 registry → 汇报 Director
- stochastic TOST 通过 → 立即启动 `llama_length_only_gsm8k_5seed`（cuda:1，已有 3-seed 数据扩到 5-seed）
- stochastic TOST 失败 → 走 red-section framing 调整提案流程，禁止默默跑下一个
- Director 回复 P1 决策 = 选项 A（用 GPT-4o oracle）→ 跳过 P1，stochastic 完成后直接排 P2 `oracle_online_llama`
- Director 回复 P1 决策 = 选项 B（GPT-4o-mini）→ `request_secret("comm_gate_mas", "openai_key")` 获取 API key → 本地跑 precompute ~53 min

### 5. 🎯 战略上下文
**核心叙事**：Dissociation finding — perturbation sensitivity ≠ pruning safety，ack messages 扰动敏感但可安全剪枝。NeurIPS 2026 投稿（abstract 5/3-4, paper 5/5-6）。

**关键决策链**：D200 维持 dissociation 主线 → D201 κ>0.8 选 GPT-4o-mini oracle → D205 72B 降级 preliminary → D206 prompt_mod v2 有效支持 emergent behavior

**已有数据**：双 backbone 10-seed（Llama Δ=+2.1±2.4pp, Qwen Δ=+0.40±1.02pp），heuristic/length-only/prompt_mod 结果齐全。Stochastic 10-seed 是最后一个关键数据点。

**易错点**：
- P1 oracle 是本地任务，不要再提交到服务器（已失败 3 次）
- length-only Qwen vs Llama 50x 差异（suppress 42.2% vs 0.81%）是已知 model-dependent 现象，不是 bug，Discussion 已写
- prompt_mod 47.9% 参考值来自不同实验模式（skip），论文 framing 是方向性论述不是量化对比
- vLLM 服务（PID 856695）是 stochastic 实验的依赖，不要 kill


---
