# agent / loop_7.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`b0ccd074f051218624a5.json`](../../sessions/b0/b0ccd074f051218624a5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T12:37:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-47453 的 cuda:0/1/2/3（共 4 张 RTX 6000 Pro 96G），不可用其他卡
- grid_b2_0_seed456 用了 bf16 训练（其他 seed42/seed123 的 grid 实验是 fp32），PPL 对比时必须标注精度差异
- seed456 grid 系列从 checkpoint-3000/3500 恢复训练（因首次 eval overhead 超时），不是从头跑的——如果出现异常指标先排查恢复点兼容性
- WANDB_MODE=disabled 全局关闭，所有指标来源只有训练日志 + post-hoc eval_perplexity.py，不要去查 W&B
- 投稿目标 EMNLP 2026 ARR May 25（距今 10 天），GPU 预算剩 ~85h / 180h，余量紧

### 2. 🖥️ 基础设施快照
- 服务器: westd-47453，工作目录 `/root/provenance_weight_training`
- Python: `/root/miniconda3/bin/python`，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型: `models/Qwen/Qwen3-0.6B`（本地缓存）
- 训练数据: `data/scored_data.jsonl`（371499 条，含 q-score）；eval 数据: `data/human/eval_holdout.jsonl`
- Eval 脚本: `eval_perplexity.py`（sliding window, stride=1024, max_docs=5000, fp16）
- 活跃进程: ess_only_seed42 PID=189240, cuda:1, tmux 管理, cron 监控中
- HF_HOME 无特殊设置（本地服务器，非 AutoDL）

### 3. 📊 当前状态
**刚做完**: 收到 grid_b3_0_seed456 CRON 完成回调，同时发现 grid_b5_0_seed456 也完成。两个都在 ANALYZING，派了 Worker `worker_eval_grid_b3_0_b5_0_seed456_20260515T093346` 跑 post-hoc eval。

**等待中的回调**:
- `worker_eval_grid_b3_0_b5_0_seed456_20260515T093346` — 两个实验的 eval 结果（预计 ~10min）
- `worker_code_verify_queued_scripts_20260515T093452` — 验证 golden_ratio 和 nmin1 脚本就绪性
- ess_only_seed42 CRON — 训练中，cuda:1，预计还需数小时

**Registry 关键状态**:
- RUNNING: ess_only_seed42 (cuda:1)
- ANALYZING: grid_b3_0_seed456, grid_b5_0_seed456 (等 eval Worker 回调)
- QUEUED: golden_ratio_seed42, nmin1_seed42, detector_modernbert
- DONE(success): 22 个; DONE(failed): grid_b_low_seed42 (SIGTERM 被杀两次，原因未查明)

**已向 Director 汇报**: 请求 cuda:0/2/3 分配给排队实验（golden_ratio → cuda:0, nmin1 → cuda:2），等待 Director 回复。

### 4. 📋 待办
- eval Worker 回调到 → 用 metrics 更新 registry（status=DONE, conclusion=success）→ 刷新 report.md → 补充汇报 Director 完整 seed456 grid 曲线
- 脚本验证 Worker 回调到 → 确认 golden_ratio / nmin1 命令可用 → 等 Director 分配 GPU 后立即 submit_on_allocated
- Director 回复 GPU 分配 → 立即提交 golden_ratio_seed42 (cuda:0) + nmin1_seed42 (cuda:2 或 cuda:3)
- ess_only_seed42 完成 → post-hoc eval → 与 adaptive_fix 三 seed 对比（核心 claim: min-intervention > max-intervention）
- grid_b_low_seed42 两次 SIGTERM 失败未查明 → 如果 Director 要求可以重查，但优先级低
- seed456 全部 grid eval 完成后 → 聚合三 seed 结果表，确认 b=0.5 跨 seed 最优

### 5. 🎯 战略上下文
- **核心方向**: Dual-constrained adaptive b*（α_eff 下界 + ESS 上界 → 最小干预准则），替代 Drayson 的 validation-based grid search
- **关键决策链**: D019(MVP PASS) → D021(α_eff 退化风险) → D023(修正过度修正，dual-constraint 框架恢复) → D024(GPU 预算，Llama-3B 降 P1) → D025(τ 降级为 empirical hyperparameter)
- **Grid 曲线一致性**: 三 seed 均显示 b↑ → PPL↑，b=0.5 最优。adaptive_fix 三 seed PPL ≈ 17.64-17.66，介于 grid b=0.5(17.64-17.65) 和 b=1.0(17.67-17.69) 之间——adaptive 接近最优但未超越，story 需要强调"无需 grid search 即可接近最优"
- **易错点**: 不要把 bf16 训练的 grid_b2_0_seed456 (PPL=17.989) 与 fp32 训练的同 b 值实验直接比较——这个偏高值是精度差异，不是方法差异。汇报时必须标注
- **ESS-only baseline 是关键**: ess_only_seed42 正在跑，如果 PPL 明显差于 adaptive → 证明 min-intervention > max-intervention，这是论文核心 claim 之一


---
