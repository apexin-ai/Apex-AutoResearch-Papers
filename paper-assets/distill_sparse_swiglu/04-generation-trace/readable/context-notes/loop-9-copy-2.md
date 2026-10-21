# agent / loop_9.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`06ba80cd9d0d9c5ff41c.json`](../../sessions/06/06ba80cd9d0d9c5ff41c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-17T10:59:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 + cuda:1 only（westd-34887）
- 30% sparsity 训练必须 `--lambda_max 5000`（不是默认 1000！M004/M005 两次教训）
- KL PPL 引用必须用 4-seed mean 12.00±0.07，禁用单 seed 最佳 11.91
- wikitext-103 必须走本地 fallback `/root/autodl-tmp/data/wikitext103/`（HF 网络不可达）
- 22.51 是 BCE **per-token** PPL，27.97 是 BCE **global** PPL，论文中不可混用 eval mode 对比

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，工作目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：LLaMA-3.1-8B `/root/autodl-tmp/models/llama-3.1-8b/`，Mistral-7B `/root/autodl-tmp/models/mistral-7b/`
- 数据：wikitext-103 本地 `/root/autodl-tmp/data/wikitext103/`，C4 `/root/autodl-tmp/data/c4/`，HF cache `/root/autodl-tmp/.hf_cache/`
- WANDB_MODE=disabled（无 API key）
- 活跃进程：
  - cuda:0: KL 50% multiseed 串行脚本（PID 22258→子进程，日志 `logs/multiseed_kl50.log`，s123 train→eval→s456 train→eval）
  - cuda:1: KL 30% multiseed 修正版（PID 23613→子进程，日志 `logs/multiseed_kl30_fixed.log`，lambda_max=5000，s123 train→eval→s456 train→eval）
- Worker 在跑：`worker_check_multiseed_status_collect_20260517T105807`（检查训练进度）

### 3. 📊 当前状态
收到 Director Round 6 实验清单时正在等 multi-seed 训练完成。已派 Worker 检查进度但还没收到回调。

**今日已完成的分析/实验**（全部 registry DONE）：
- `kl_bce_f1_oracle` (success): BCE F1=0.613 > KL F1=0.540，但 KL PPL 远优
- `global_30pct/50pct/70pct_retention` (success): 三级 progressive starvation pattern
- `reverse_kl_50pct_s42` + `jsd_50pct_s42` (negative): Forward KL 仍最优（+8.6%/+6.4%）
- JSD/Reverse KL C4 OOD eval: Forward KL OOD 优势放大（JSD +42.2%）
- `pertoken_hard_50pct_db256` (success): PPL=8.59，三向退化分解完成
- `gradient_snr_comparison` chart + `per_layer_retention_chart` chart: 已同步本地，artifact 已注册
- `loss_ablation_ood_data.json`: 完整 loss ablation 数据整理完毕
- data_utils.py wikitext-103 本地 fallback 修复
- Registry 卫生清理（steps_curve 系列、kl_bce_f1_oracle 状态修正）

**等待中**：multi-seed 训练完成回调

### 4. 📋 待办（条件触发式）
- `worker_check_multiseed_status_collect` 回调 → 读取结果，对已完成的 seed 注册 registry + 汇报 Director
- 50% multiseed 全部完成（cuda:0 空闲）→ 立即启动 **Step 1: C3 Coupling vs Oracle 实验**（最高优先级新实验，bce_kl_oracle_s42）
- 30% multiseed 全部完成（cuda:1 空闲）→ 立即启动 **Step 2: Mistral 50% PPL 溯源** 或 **Step 3: 30%/40% C4 OOD eval**
- 双卡均空闲 → Step 2 + Step 3 并行
- C3 实验完成 → 根据结果判断：接近 KL = oracle quality 是关键；远差于 KL = gradient coupling 是核心因素。汇报 Director

### 5. 🎯 战略上下文
- DDL: EMNLP 2026 ARR May, 2026-05-25（剩 8 天）
- 论文 framing: A+C 混合，骨架 = PPL-Downstream Disconnect，血肉 = Sparsity Threshold
- **C3 Coupling vs Oracle 是 Round 6 最高价值实验**：验证 KL 优势归因于 gradient coupling（因果机制）还是仅仅 oracle quality（更好的 target）。这直接影响论文 §4.3 的 claim 强度
- d030 = Decision ID 前缀，不是 30% sparsity（已向 Director 澄清，回复审稿人时展示 checkpoint 来源）
- §4.3 的 "22.51 vs 11.79" 混用了 per-token/global eval mode——Director 已知悉，需修正为同一 mode 对比
- 50% uniform 已验证不可修复（MMLU≈random），不要再尝试
- Forward KL 优于 Reverse KL 和 JSD 的原因：mode-covering 特性更适合 sparsity prediction（需要高 recall 覆盖所有重要 neuron）


---
