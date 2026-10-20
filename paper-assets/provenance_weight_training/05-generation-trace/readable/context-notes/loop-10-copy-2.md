# agent / loop_10.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`d82689ce2b27d15a08fb.json`](../../sessions/d8/d82689ce2b27d15a08fb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T21:57:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0/1/2/3（westd-47453），不可用其他设备
- submit_training_job 禁止 bash for-loop 带 `$var`——变量会被外层 shell 展开为空（grid_b_low 连续 3 次踩坑，r3 改用独立 shell 脚本）
- 训练脚本禁止 inline eval，评估一律用 post-hoc `eval_perplexity.py`
- seed456 b≥2.0 数据因 checkpoint resume artifact 系统性偏高 +0.16~0.25，Table 1 这些格只报 2 seeds（seed42+seed123）
- τ 不能 claim "proportion-free 理论推导"——定位是 empirical HP with theoretical motivation（D025 定论）
- τ sweep 不能说"τ 不敏感"，正确表述："wide safe range [0.5, 0.8] with principled default τ=0.8"
- n_min 与 batch_size 耦合：n_min = max(2, batch_size//2)。bs=4→n_min=2, bs=8→需手动 override 为 2（否则默认 4 会导致 b*=0）
- aml-train 镜像用 conda（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453，4× RTX 6000 Pro 96G
- 工作目录：`/root/provenance_weight_training`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：Qwen3-0.6B（continued pretraining, 非 from scratch）
- 数据：ρ=0.4 FineWeb subset 132M+ tokens（默认）；ρ=0.6 数据集已生成（371,499 行, 907MB, 在服务器上）
- W&B：项目 `provenance_weight_training`
- 活跃进程：
  - `bs8_nmin2_seed42_r2` — PID 238714, cuda:2, cron 监控中
  - `contamination_60_uniform_seed42` — PID 250074, cuda:1, cron 监控中
  - `contamination_60_grid_b0_5_seed42` — PID 255781, cuda:3, cron 监控中
- cuda:0 当前空闲（ess_only_seed123/456 刚完成）

### 3. 📊 当前状态
**刚完成**：ess_only_seed123 和 ess_only_seed456 训练完成（both success）。正在被 Worker 分析和 eval。

**RUNNING（3）**：
| exp_id | GPU | 说明 |
|--------|-----|------|
| bs8_nmin2_seed42_r2 | cuda:2 | batch_size=8, n_min=2, 验证大 batch 泛化 |
| contamination_60_uniform_seed42 | cuda:1 | ρ=0.6 uniform baseline |
| contamination_60_grid_b0_5_seed42 | cuda:3 | ρ=0.6 grid-best b=0.5 baseline |

**活跃 Worker（3）**：
- `worker_analysis_ess_only_seed456` — 分析 ess_only_seed456 结果
- `worker_eval_ess_only_seed123_seed456` — 跑 eval perplexity
- `worker_submit_grid_b_low_split` — 准备 grid_b_low 拆分提交（r3，独立脚本方式）

**等待中**：
- grid_b_low_seed42_r3: QUEUED，等 GPU（cuda:0 刚空出来，Worker 正在处理）
- adaptive_v2_seed42/123/456: PREPARING 但已被 D012 取消（conclusion=killed），实际是僵尸条目，不会执行

**Registry 总计**：51 实验，success 34 / negative 2 / failed 5 / killed 6

### 4. 📋 待办（条件触发式）
- Worker `eval_ess_only_seed123_seed456` 完成 → 更新 registry metrics → Claim 1 多 seed 验证完成（3/3 seeds）→ 汇报 Director "Claim 1 fully supported"
- Worker `analysis_ess_only_seed456` 完成 → 整合分析到 report.md
- Worker `submit_grid_b_low_split` 完成 → grid_b_low_r3 应在 cuda:0 上启动，确认 cron 注册
- bs8_nmin2_seed42_r2 cron 回调（预计 ~3.8h）→ spawn Worker eval → 结果决定 batch_size 泛化叙事
- contamination_60_uniform/grid 两个 cron 回调 → spawn Worker eval → 对比 adaptive（还没提交 contamination_60_adaptive，需要等 baseline 出来后决定是否提交）
- 上述全部完成 + contamination_60_adaptive 完成 → 满足 dream_simulate(review_mode="full") 条件 → 评估论文初稿启动
- D038 已批准 writing_plan.yaml，Paper Agent Full Draft 可以启动（但需实验数据齐全）

### 5. 🎯 战略上下文
**投稿目标**：EMNLP 2026 ARR May 25（距今 10 天）。GPU 预算已消耗 ~140h，剩余 ~40h，P0 余量紧张。

**核心结论链**：
- D019: MVP PASS — adaptive ≈ grid-best（aggregate 88.6% recovery）
- D023: dual-constraint 框架确立（α_eff 下界 + ESS 上界）
- D029: ESS-only PPL=17.728 > uniform — max-intervention 退化，min-intervention 优越性确认
- D035/D036: τ sweep 6 点完成，safe range [0.5, 0.8]，τ=0.8 最优
- D037: bs8 配置修正（n_min=4→2）
- D038: writing_plan.yaml 批准
- D039: 论文描述修正为 "continued pretraining"

**Claim 证据覆盖**：
- Claim 1 (dual > ESS-only): 1/3 seeds done，seed123/456 正在 eval（即将完成）
- Claim 2 (adaptive ≈ grid): ✅ 3 seeds complete
- Claim 3 (unknown proportion): ✅ τ sweep complete
- n_min robustness: 3/4 points（n_min=4 即 bs8_nmin2_r2 运行中）
- batch_size 泛化: 0/1（bs8_nmin2_r2 运行中）
- contamination 泛化 (ρ=0.6): 0/3（2 个 baseline 运行中，adaptive 待提交）

**易错点**：
- 不要把 adaptive_v2 系列当活跃实验——它们是 D012 已取消的僵尸条目
- cuda:0 刚空出来，grid_b_low_r3 Worker 正在处理提交，不要重复提交
- contamination_60 系列还缺 adaptive 实验，但需要先等 uniform+grid baseline 出来
- Golden Ratio oracle PPL=17.654 ≈ adaptive 17.650，说明 adaptive 已达理论上界，后续不应追求更低 PPL
- 论文用 ratio of means（89.9%）而非 mean of ratios（91.0%）报告 recovery ratio


---
