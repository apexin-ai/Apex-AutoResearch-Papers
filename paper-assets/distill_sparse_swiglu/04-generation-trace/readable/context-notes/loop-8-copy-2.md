# agent / loop_8.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`27e907c193f8505cddbb.json`](../../sessions/27/27e907c193f8505cddbb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-16T21:03:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westd-34887 cuda:0 + cuda:1，其他设备号/服务器禁止
- evaluate.py 默认 --sparsity_target 0.5，30%/40%/70% eval 必须显式传参
- KL PPL 论文引用统一用 4-seed mean 12.00±0.07，不用单 seed 最佳 11.91
- BCE framing 禁止"anti-learning"，必须用"objective mismatch"
- SPON framing 禁止"subsumes"，必须用"marginal complement"
- command 必须 bash -c "..." 包裹（tmux 用 sh 不是 bash）
- bench_kl30_global/bench_kl50_global 用的是 --sparsity_mode teal_global，不是 uniform
- LongBench 必须用 --multi_gpu + PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True（单卡 OOM，5 次验证）
- Registry 录入必须交叉验证原始日志（D032 教训：误录 PPL 导致数据污染）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，用户 root，工作目录 /root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：Llama-3.1-8B at /root/autodl-tmp/models/llama-3.1-8b/；Mistral-7B at /root/autodl-tmp/models/mistral-7b/
- Checkpoints：/root/distill_sparse_swiglu/checkpoints/（各实验子目录）
- 日志：~/runs/distill_sparse_swiglu/*.log
- WANDB_MODE=offline（无 API key）
- 活跃进程：longbench_kl30_uniform_v6 PID 250629, tmux=longbench_kl30_uniform_v6, cuda:0+cuda:1 (multi-GPU)
- Cron 监控已就位（reconcile_crons 返回 0）

### 3. 📊 当前状态
**刚做完**：Session-start 初始化 + 向 Director 汇报全部 benchmark 统一评测完成（含 TEAL 30/50 unified、KL 40% global、multi-seed）。清理了 4 个 QUEUED+failed 的 LongBench 旧实验。

**RUNNING/PREPARING (1)**:
- longbench_kl30_uniform_v6 (PREPARING, PID 250629, cuda:0+cuda:1) — LongBench 长文本 KL 30% uniform 评测，multi-GPU。Dense baseline (v6) 已完成。

**Worker 池 (2)**:
1. `worker_ops_longbench-kl30-submit_20260516T165540` — 提交 longbench_kl30_uniform_v6
2. `worker_analysis_benchmark-table-final_20260516T165941` — 更新 benchmark comparison table 最终版（补 TEAL unified + KL 40% global + multi-seed 数据）

### 4. 📋 待办（条件触发式）
- longbench_kl30_uniform_v6 完成回调 → 提取 metrics → update registry → 与 longbench_dense_v6 对比（dense: narrativeqa=7.3, qasper=13.4, gov_report=30.5, multi_news=2.5）→ 判断是否值得入 paper
- analysis worker 回调 → 验证 benchmark_comparison_table.md 完整性 → register_artifact（如未注册）
- Director 回复 → 可能对 40% global>uniform 反转现象给出 framing 指示 → 按指示更新论文 Discussion
- LongBench 完成后两卡释放 → 评估是否还有实验需要跑（可能无——所有标准 benchmark 已完成）→ 如无实验则全力推论文定稿

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May, 2026-05-25（剩 9 天）
- **核心 narrative**: KL distillation 使 SwiGLU sparse prediction 不需要 compensation。两个 story：(1) KL >> all baselines (PPL+downstream)，(2) Phase transition 30%→40%→50%
- **全部标准 benchmark 已完成**，完整对比表就绪。论文进入定稿阶段。
- **最易判断错的事**:
  - 40% global MMLU=38.1% > uniform 30.7%：这是真实结果不是 bug。Uniform 不是银弹，仅在 30% 有效。论文需要讨论这个 nuance（或改 claim 为"30% uniform = recommended"而非"uniform always better"）
  - longbench_kl30_uniform_v6 registry 显示 PREPARING 但实际在跑（submit_training_job 已设 PID，cron 未来得及推进）
  - bench_kl50_uniform 和 d030_kl50_uniform 是同一个实验的不同命名（数据完全一致：PPL=11.96, MMLU=27.77）——不要重复跑
  - LongBench dense v6 结果很低（narrativeqa=7.3）——这可能是 Llama-3.1-8B 在 LongBench 上的正常水平（非 instruction-tuned model），不要误认为是 bug


---
