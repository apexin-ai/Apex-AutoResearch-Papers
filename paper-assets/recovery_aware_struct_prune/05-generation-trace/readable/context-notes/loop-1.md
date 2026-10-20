# director / loop_1.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`044e46729ef756d9a906.json`](../../sessions/04/044e46729ef756d9a906.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T06:15:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅 westb-23072 的 cuda:0 和 cuda:1，禁止使用其他 GPU
- 35% sparsity 下全局排序自然只剪 MLP（0 attention groups），这是 D001 决策：不强制 attention 配额，MLP-level correlation 验证假设
- RASP 公式 S(h) = I(h) × (1-F(h))^α 中 MLP overlap (0.88-0.99) 远高于 attention (0.19-0.69)，导致 RASP 优先剪 MLP — 这是理论的正确行为，不要试图"修复"
- 剪枝必须按 GQA group 粒度（7 Q heads + 1 KV head = 1 group），不能按单 Q head — v1 就是因此崩溃的

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/recovery_aware_struct_prune
- Python：conda base (/root/miniconda3/bin/python)，Python 3.12
- 模型：/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B（symlink from 项目 models/）
- 代码：/root/recovery_aware_struct_prune/src/（cka_overlap.py, importance_score.py, prune.py, train_grpo.py, eval_gsm8k.py, correlation_analysis.py, run_mvp.sh）
- 论文：/root/recovery_aware_struct_prune/paper/（method.tex, related_work.tex 初稿已完成）
- W&B：未配置（report_to="none"，本地日志 /root/recovery_aware_struct_prune/logs/）
- HuggingFace Hub：不可达（Network unreachable），所有数据从本地 cache 加载
- 活跃进程：mvp_rasp_pipeline_v2（PID 161827，tmux session mvp_rasp_pipeline_v2，cuda:0+cuda:1）

### 3. 📊 当前状态
MVP v2 pipeline 正在运行。v1 因 GQA 约束违反崩溃，修复后 v2 已启动。

7 步流水线：Step 0 baseline eval → Step 1+2 CKA+importance 并行 → Step 3 prune → Step 3.5 post-prune eval → Step 4 GRPO RLVR recovery（关键路径 ~12-15h）→ Step 5 post-recovery eval → Step 6 correlation analysis

**注意**：Reviewer 最后一条 warning 指出 run_mvp.sh 可能仍缺 baseline eval（Step 0 未剪枝模型 eval）。v2 启动前 Agent 说加了 Step 3.5 post-prune eval，但 baseline eval 状态不确定。接手后需核实。

Registry：mvp_rasp_pipeline_v2 RUNNING；mvp_rasp_pipeline DONE/failed

论文：Method + Related Work 初稿完成。Reviewer 指出 SparseGPT 缺引、self-calibration claim 与代码不匹配、Algorithm 1 伪代码按结构数而非参数量计算 sparsity — 这些在实验结果出后统一校准。

### 4. 📋 待办
- mvp_rasp_pipeline_v2 完成回调 → 读 correlation_results.json：combined ρ ≥ 0.4 → PASS → complete_mvp() 进入 research → 走 post-mvp-kickoff skill（paper_framing.md → experiment_plan.yaml → dream_simulate → update_roadmap）
- combined ρ ∈ [0.3, 0.4) → 在 25% sparsity 重复验证再判定
- combined ρ < 0.3 → FAIL → pivot 到纯实证 pruning×recovery interaction benchmark（contingency plan 在 ROADMAP）
- MVP pass 后 Phase 2 P1 优先跑 GRASPrune+RLVR（35%）— 验证 CKA 假设在 SOTA 方法上是否成立
- 50% sparsity 实验放 Phase 2 P3 — 获取 attention-level recoverability 数据
- W&B API key 待用户提供，Phase 2 长训练需要监控
- 论文修正待 MVP 结果出后统一处理：self-calibration claim、Algorithm 1 sparsity 计算、SparseGPT 引用、F(h) 分布偏差讨论

### 5. 🎯 战略上下文
- 项目核心假设：CKA functional overlap 预测 RLVR recoverability。理论基础来自 "RL Squeezes, SFT Expands" (ICLR 2026)
- D001：接受 35% 下 MLP-only pruning，不强制 attention 配额。这意味着 MVP verdict 基于 MLP-level correlation
- 最容易判断错的事：看到 "0 attention heads pruned" 不要以为是 bug — 这是 D001 的预期行为。如果 Phase 2 需要 attention 数据，用 50% sparsity 而不是改公式
- ARR May 25 截稿距今 11 天，GRPO 训练是最大的 wall-clock 瓶颈（每次 12-15h）。Phase 2 有 6 个优先级层级（P1-P5 + P2.5 scoring ablation），必须严格按优先级串/并行安排
- RTX PRO 6000 Blackwell 的训练吞吐未校准（IDEA_BRIEF 估算基于 H100）— GRPO 首 epoch step/s 是校准全量预算的关键数据，结果出来后必须重算 timeline


---
