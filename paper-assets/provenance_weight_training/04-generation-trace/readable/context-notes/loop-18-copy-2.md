# agent / loop_18.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`9c7254caa31cd30f218d.json`](../../sessions/9c/9c7254caa31cd30f218d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-21T13:00:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 on westd-41312，无其他服务器
- 当前占用：cuda:0 = adaptive_tau08_scratch_seed42, cuda:1 = gpt2_adaptive_seed123, cuda:3 = adaptive_1_7b_seed456。只有 cuda:2 空闲（正被 eval Worker 使用）
- WANDB_MODE=disabled（所有 1.7B 实验），指标只能从 eval 脚本 JSON 输出获取，不要查 W&B
- 模型存储在 /root/autodl-tmp/...（数据盘），不要写根分区
- DDL: EMNLP 2026 ARR May 25（~3.5 天）

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312，账号 root
- 工作目录：/root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型输出：/root/autodl-tmp/provenance_weight_training/output/models/{exp_id}/final
- 数据：/root/provenance_weight_training/data/scored_data.jsonl (371499 条), data/human/eval_holdout.jsonl, data/eval_openwebtext.jsonl, data/eval_wikipedia.jsonl
- Eval 脚本：eval_perplexity.py (holdout+OOD), `python -m lm_eval` (downstream 5 tasks)
- 活跃 cron：adaptive_1_7b_seed456 (PID 494706, cuda:3), adaptive_tau08_scratch_seed42 (PID 509768, cuda:0), gpt2_adaptive_seed123 (PID 514246, cuda:1)
- 磁盘：/usr/bin/nvidia-smi 分区 401GB/439GB 可用

### 3. 📊 当前状态
**刚发生**：uniform_1_7b_seed456 训练完成 → ANALYZING。已 spawn Worker (worker_eval_uniform_1_7b_seed456_20260520T205904) 在 cuda:2 跑全套 eval pipeline（holdout + OOD OWT/Wiki + downstream 5 tasks）。第 2 个 Worker (worker_analysis_1_7b_3seed_prep_20260520T205914) 在准备 1.7B 3-seed 对比模板。

**RUNNING (3)**：
- adaptive_1_7b_seed456 (cuda:3)：1.7B adaptive 第 3 seed，与 uniform_1_7b_seed456 配对
- adaptive_tau08_scratch_seed42 (cuda:0)：D110 τ=0.8 from-scratch 补训，消除 OOD 数据不对称
- gpt2_adaptive_seed123 (cuda:1)：D111 detector ablation 第 2 seed

**等待中**：
- 2 个 Worker 回调（eval + 分析模板）
- 3 个 cron 回调（上述 RUNNING 实验）

### 4. 📋 待办
- eval Worker 回调 → 读 metrics → update_registry(uniform_1_7b_seed456, conclusion=success) → 更新 report.md → 汇报 Director 含 3-seed 统计（如果 adaptive seed456 也完成的话）
- adaptive_1_7b_seed456 完成 → spawn eval Worker (cuda:3 或空闲卡) → 跑同样 eval pipeline → 完成后 1.7B 3-seed 全部齐备 → 计算 Δ(adaptive-uniform) 均值±std → 汇报 Director 更新论文 scaling claim
- adaptive_tau08_scratch_seed42 完成 → eval → 与 adaptive_ood_seed123/456 合并为 τ=0.8 3-seed from-scratch OOD → 论文 τ=0.8 OOD 升级为 3-seed
- gpt2_adaptive_seed123 完成 → eval → 与 gpt2_adaptive_seed42 对比确认 detector ablation pattern
- 1.7B 3-seed 全部齐备 → 论文更新（Table/正文）→ 提交 Director 审查
- **关注**：1.7B Wiki OOD seed42 +0.036 vs seed123 +0.010 差异大，seed456 定论（如果 seed456 也偏高 → 高 variance 需要论文中标注）

### 5. 🎯 战略上下文
- 核心范式：detect-and-reweight，用 contamination score 做 adaptive sample weighting
- C1-C3 核心 claims 数据已齐备，当前阶段是补 multi-seed + scaling 的 robustness evidence
- 1.7B scaling claim = "do no harm at scale"（D108），不是说 adaptive 更好，而是说不会变差。Δ 期望接近 0 或略负
- τ claim = "τ ∈ [0.7, 0.8] robust"（D102/D106），τ=0.7 在 OOD 上略优，τ=0.8 OOD-neutral
- 论文已提交 Round 7，等审稿。当前工作是补齐 multi-seed 统计强度
- 易错点：(1) uniform_1_7b_seed123 的 spec 里数据格式和其他 seed 不一致（data_path=data/human, data_count=5000），但实际训练用的是 scored_data.jsonl 371499 条，registry 是历史遗留错误不要据此怀疑实验有效性 (2) 不要把 resume-checkpoint 实验（adaptive_fix_*）和 from-scratch 实验混在同一个 seed 组里做统计 (3) PREPARING 实验很多是历史残留，不要盲目提交


---
