# agent / loop_7.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`6f6e370ce0f455203168.json`](../../sessions/6f/6f6e370ce0f455203168.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-04-28T22:19:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 **只能用 cuda:1**（westb-4x6000-a）。cuda:0/2/3 分配给其他项目，禁止使用
- NeurIPS 2026 DDL：abstract 5/3-4, paper 5/5-6（AOE）。**剩余 ~8 天**
- cross-task 实验是串行 pipeline：Llama 系列共用 Llama vLLM (port 8000)，Qwen 系列共用 Qwen vLLM (port 8001)。同一端口不能并行跑两个实验
- submit_training_job 命令必须自带 conda 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ...`
- 72B AWQ 模型需要 vLLM 单卡加载（AWQ 量化），启动前必须先杀掉 cuda:1 上的 7B vLLM

### 2. 🖥️ 基础设施快照
- **服务器**: westb-4x6000-a，工作目录 `/root/comm_gate_mas/`（推测，Worker 首次连接需确认）
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，系统 Python 无 pyyaml）
- **模型路径**: Llama-3.1-8B-Instruct / Qwen2.5-7B-Instruct 通过 vLLM 提供（Llama port 8000, Qwen port 8001）；72B-AWQ 路径待确认
- **HF cache**: 大概率 `/root/autodl-tmp/.hf_cache`（AutoDL 规范，但 westb 可能不同）
- **活跃进程**: llama_heuristic_stratqa — PID 341188, cuda:1, cron 监控中
- **Cron**: 8 个 active（其中 llama_heuristic_stratqa 属于本项目，其余属其他项目）；vt_cifar_erc_s123_lam001 进程已消失需 escalation（非本项目）

### 3. 📊 当前状态
**刚完成**: P0+P1+P2 全部论文修改 + 补充分析（title/abstract/contribution/conclusion/discussion 重构 + Gemma-excluded/cascade position/position concordance appendix）。阈值 sensitivity ablation 已完成（4 变体，结果稳健）。Llama heuristic 5-seed aggregated 已完成（Δ=+2.20±1.44pp, CI=[+0.41,+3.99], beneficial）。

**正在跑**:
| exp_id | 状态 | GPU | PID | 摘要 |
|--------|------|-----|-----|------|
| llama_heuristic_stratqa | RUNNING | cuda:1 | 341188 | Llama StrategyQA cross-task, n=200, seed=42 |

**排队等 cuda:1**:
| exp_id | 状态 | 摘要 |
|--------|------|------|
| llama_heuristic_arc | ALLOCATED | Llama ARC-Challenge cross-task |
| qwen_heuristic_stratqa | ALLOCATED | Qwen StrategyQA cross-task（需切 vLLM 到 Qwen port 8001）|
| qwen_heuristic_arc | ALLOCATED | Qwen ARC-Challenge cross-task |
| oracle_qwen72b_seed123 | PREPARING | 72B seed=123 复现（需切 vLLM 到 72B-AWQ）|

**等待中**: 无 pending Worker 回调。llama_heuristic_stratqa 的 cron 会在完成时触发 [CRON] 回调。

### 4. 📋 待办（条件触发式）
- llama_heuristic_stratqa cron 回调 → spawn worker 分析结果 → 如果 non-inferior，立即 submit llama_heuristic_arc（同一 vLLM 实例）
- llama_heuristic_arc 完成 → 切换 vLLM 到 Qwen（port 8001）→ submit qwen_heuristic_stratqa → 完成后 submit qwen_heuristic_arc
- 4 个 cross-task 全部完成 → 汇总结果写入论文 robustness section → 杀 7B vLLM → 启动 72B-AWQ vLLM → submit oracle_qwen72b_seed123
- oracle_qwen72b_seed123 完成 → 0 discordant flips → 考虑 seed 3（UB 1.13%→0.57%）；有 discordant → 停止，调整 "preliminary" 措辞
- 所有实验完成 → PDF 编译验证 → Reviewer 复审 → abstract 提交 (5/3)

### 5. 🎯 战略上下文
**核心结论**: Perturbation sensitivity ≠ pruning safety。Ack 消息扰动敏感性最高但聚合层面可安全剪除。双 backbone (Qwen/Llama) 10-seed oracle + heuristic 验证 non-inferiority。Llama heuristic 实际 beneficial（CI 完全正向）。

**决策链**: D214 叙事重构（heuristic→model-adapted heuristic）→ D219 Llama non-inferiority claim → D220 5-seed final → D221 GPU 冻结令 pivot 到阈值 ablation → D222/D223 审稿报告反审 + action matrix → P0-P2 全部完成。

**易错点**:
- cross-task 实验的 pipeline.sh 分 Phase A (Llama) / Phase B (Qwen)，Phase B 需要 Qwen vLLM 在 port 8001 **先启动**。不要假设 vLLM 已在跑
- 72B AWQ 单卡需要 ~40GB VRAM，A6000 有 48GB 可以放下，但必须先释放 7B 模型
- PREPARING 状态的 vllm_llama_8192/v2、p1_oracle_precompute* 等是历史遗留（已废弃/失败），不需要处理
- Llama +2.2pp beneficial 是 secondary finding，主 claim 仍是 non-inferiority（不要 overclaim）
- 72B 单 seed "scale evidence" 措辞（D222）需保持 preliminary，除非 seed 2 也零翻转


---
