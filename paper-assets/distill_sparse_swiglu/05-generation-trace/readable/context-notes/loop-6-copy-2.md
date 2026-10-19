# agent / loop_6.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`d97750c1ef336291fdd9.json`](../../sessions/d9/d97750c1ef336291fdd9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-16T11:39:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westd-34887 cuda:0 + cuda:1，其他设备号/服务器禁止
- evaluate.py 默认 --sparsity_target 0.5，30%/40%/70% eval 必须显式传参，否则拿到的 PPL 是错的
- KL PPL 论文引用统一用 4-seed mean 12.00±0.07，不用单 seed 最佳 11.91
- BCE framing 禁止"anti-learning"，必须用"objective mismatch"
- SPON framing 禁止"subsumes"，必须用"marginal complement"
- command 必须 bash -c "..." 包裹（tmux 用 sh 不是 bash）
- Registry 录入必须交叉验证原始日志（D032 教训：误录 PPL 导致数据污染）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，用户 root，工作目录 /root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型（Llama-3.1-8B）：HF cache 默认位置
- Mistral-7B：/root/autodl-tmp/models/mistral-7b/
- Checkpoints：/root/distill_sparse_swiglu/checkpoints/（各实验子目录）
- 日志：~/runs/distill_sparse_swiglu/*.log
- W&B：项目配置里有（load_project_config 可查 entity/project）
- 活跃进程：
  - eval_bce_v3_s42: PID 211431, cuda:1, tmux=eval_bce_v3_s42
  - bench_dense 已退出（PID 209887 was cuda:0）

### 3. 📊 当前状态
**刚做完**：收到 bench_dense (Dense baseline benchmark, plan_007) ANALYZING 回调。

**已派发但未收到回调的 Worker**：
1. `worker_analysis_bench_dense_results_20260516T061410` — SSH 读 bench_dense.log 提取 Dense baseline 指标（ARC-c/WG/MMLU/GSM8K/PPL），更新 registry→DONE
2. `worker_submit_eval_kl30_teal_30pct_20260516T061535` — 在 cuda:0 提交 D034（KL 30% predictor @ sparsity_target=0.3 的真实 TEAL PPL）
3. `worker_eval_bce_v3_eval_pipeline_20260516T055435` — BCE v3 iso-compute 评测管道（cuda:1 上跑 eval_bce_v3_s42）

**Registry 关键状态**：
- ANALYZING: bench_dense（等 Worker 1 回写）
- RUNNING: eval_bce_v3_s42 (cuda:1, D031 Reviewer Concern #2 defense)
- QUEUED: d030_kl40_uniform (D033: 40% threshold), eval_kl30_teal_30pct（正在被 Worker 2 提交到 cuda:0）

**尚未向 Director 汇报** bench_dense 结果——等 Worker 1 回写 metrics 后再汇报。

### 4. 📋 待办（条件触发式）
- Worker 1 (bench_dense analysis) 回调 → 读 metrics → update report.md → 向 Director 汇报 Dense baseline 数据 + 与 sparse 条件对比（plan_007 完成情况）
- Worker 2 (eval_kl30_teal_30pct) 回调 → 确认 cuda:0 提交成功 → 若失败则诊断重试
- eval_kl30_teal_30pct 完成 → 提取 30% 真实 TEAL PPL → 更新论文 sparsity sweep 表 → cuda:0 空出后立即提交 d030_kl40_uniform (D033: 40% uniform)
- eval_bce_v3_s42 完成 → BCE v3 iso-compute 与 KL 1000步对比 → Reviewer Concern #2 defense 数据就绪 → 汇报 Director → 更新 paper_framing.md
- d030_kl40_uniform 完成 → 40% MMLU 结果 + 30%(40.61%) + 50%(27.77%) 三点画 threshold 曲线 → Claim 3 验证

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May, 2026-05-25（剩 9 天）
- **核心 narrative (A+C 混合)**：PPL-Downstream Disconnect + Sparsity Threshold。KL 在 PPL 上碾压所有 baseline，但 downstream 存在非线性崩溃 cliff（50%）。30% 以下 uniform allocation 可修复 MMLU，50% 不可修复。
- **Claim 1**: KL >> baselines PPL ✅（但 PPL ≠ downstream 安全）
- **Claim 2**: PPL-downstream disconnect 系统性 ⚠️（BCE v3 iso-compute 进行中验证）
- **Claim 3**: Sparsity threshold ⚠️（30% OK / 50% FAIL / 40% 是 key data point = d030_kl40_uniform）
- **Claim 4**: Cross-architecture (Llama+Mistral) ✅
- **最易判断错的事**：
  - bench_dense 是 few-shot baseline（ARC-c=25, WG=5, MMLU=5, GSM8K=8），之前所有 sparse eval 是 0-shot。这正是 D029 要解决的 benchmark 不一致问题——拿到 dense few-shot 数据后，sparse 条件也需要统一用 benchmark_eval.py 重跑 few-shot 才能公平对比
  - d030_kl40_uniform 原 notes 说"排在 BCE v3 后用 cuda:1"，但 cuda:0 空了就应该立即用 cuda:0，不要死守原计划
  - 50% uniform 实验已证明无效（+1.86pp MMLU），不要再在 50% 上浪费 GPU 时间


---
