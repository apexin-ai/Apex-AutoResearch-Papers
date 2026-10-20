# agent / loop_2.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`587375ba15b51db4abb2.json`](../../sessions/58/587375ba15b51db4abb2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T13:23:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 的 cuda:0 和 cuda:1，不可用其他设备
- 当前 MVP eval 正在跑（PID 170770/170786/170787），**不要 kill 或重启这些进程**
- eval_gsm8k.py 已修复 OverflowError（磁盘上），但当前运行的 eval 用的是旧代码——如果 eval 崩溃需要用修复后代码重跑
- **不要运行 `pip install -r /root/GRASPrune/requirements.txt`**——会降级 torch 从 2.10.0 到 2.7.0 破坏环境
- GRASPrune 同时剪 MLP + attention KV groups（我们 RASP 只剪 MLP），论文对比时必须说明此差异

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072，2× RTX PRO 6000 96GB
- 工作目录：/root/recovery_aware_struct_prune/
- Python：/root/miniconda3/bin/python，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B
- HF cache：HF Hub 不可达，已 fallback 本地缓存
- GRASPrune：/root/GRASPrune/（已 clone、patch data.py 支持 GSM8K、import 验证通过）
- 活跃进程：PID 170770（主 bash wrapper）→ 170786（eval cuda:0）+ 170787（eval cuda:1），tmux session `mvp_rasp_pipeline_v2`
- Cron：mvp_rasp_pipeline_v2 监控中（reconcile 确认 pid=170770 存活）

### 3. 📊 当前状态
**刚完成**：Director 指令的全部并行任务——Algorithm 1 伪代码修复、bib 修复、experiments.tex 框架+Reviewer 修复（citation keys/公式去重/activation shift 描述）、GRASPrune 代码准备+依赖安全+校准数据对齐。

**RUNNING**：
- `mvp_rasp_pipeline_v2`：Step 3.5 GSM8K eval ~6.5% done (~87/1319, ~7s/it)，预计 eval 还需 ~2h，之后自动进入 Step 4 GRPO RLVR (~12-15h)

**DONE (failed)**：
- `mvp_rasp_pipeline`：v1 失败（head 粒度 CKA 不适用 GQA），已用 v2 替代（GQA group 粒度 + MLP-level）

**等待中**：cron 监控 mvp_rasp_pipeline_v2 完成回调。无待处理 Worker。

### 4. 📋 待办
- mvp_rasp_pipeline_v2 Step 3.5 eval 完成 → 自动进入 Step 4 GRPO，cron 继续监控
- mvp_rasp_pipeline_v2 DONE(success) → on-experiment-done skill：分析 Spearman ρ，ρ≥0.4 宣布 MVP pass，立即启动 Phase 2 P1（`bash /root/recovery_aware_struct_prune/src/run_graspune.sh` 已就绪）
- mvp_rasp_pipeline_v2 DONE(negative) → red-section Framing 调整提案，ρ∈[0.3,0.4) 在 25% sparsity 重复验证，ρ<0.3 走 Contingency pivot
- mvp_rasp_pipeline_v2 DONE(failed) → on-experiment-failed skill，检查日志诊断原因，可能需要用修复后的 eval_gsm8k.py 重跑
- eval 崩溃（OverflowError 触发）→ kill 旧进程，用修复后代码从 Step 3.5 resume
- Phase 2 P1 启动后 → 同时派 Worker 写 Introduction + Related Work 初稿

### 5. 🎯 战略上下文
- **核心假设**：CKA functional overlap F(h) 预测结构化剪枝后 RLVR recoverability。MVP 验证 Spearman ρ(F(h), recoverability) ≥ 0.4
- **目标会议**：EMNLP 2026 ARR May 25（距今 11 天）
- **D001**：MVP 接受 35% sparsity 下 MLP-only pruning，不强制 attention pruning
- **v1→v2 教训**：v1 在 head 粒度算 CKA 不适用 GQA 架构（shared KV），v2 改为 GQA group 粒度 + MLP-level correlation
- **易错点**：GRASPrune 剪 MLP+attention 而 RASP 只剪 MLP，对比时 sparsity 含义不同（参数量 vs 结构数）；论文已在 experiments.tex 标注但分析时容易忘
- **Phase 2 骨架**（MVP pass 后）：P1 GRASPrune+RLVR → P2 RLVR vs SFT → P2.5 Scoring ablation → P3 多剪枝率 → P4 Bonsai → P5 扩展评估


---
