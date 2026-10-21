# director / loop_18.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`10f4265cebfa8d1f4479.json`](../../sessions/10/10f4265cebfa8d1f4479.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-23T20:16:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-41312 的 cuda:0/1/2/3（4卡全分配）
- westd-47453 已下线，checkpoint 不可用，不要尝试连接
- aeff_only 实验命令行必须包含 `--num_train_tokens 200000000`（之前 seed42/123 遗漏此参数，虽然实际恰好跑了 6103 步，但 seed456 必须显式指定）
- 论文 τ=0.7 是标准设置，旧实验用 τ=0.8 的数据不可直接引用（nmin1_seed42 PPL=17.789 已被替换）
- EMNLP 2026：abstract ≤200 words，主正文 ≤8 pages，Limitations 在正文不在 appendix

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312 (connect.westd.seetacloud.com:41312)，user=root
- 工作目录：/root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据盘：/root/autodl-tmp/provenance_weight_training/output/models/（模型输出）
- 训练数据：data/scored_data.jsonl (371,499 examples, ρ=0.4)
- 论文本地路径：projects/provenance_weight_training/docs/paper/
- Registry：projects/provenance_weight_training/registry.yaml
- 活跃进程：bs8_nmin4_adaptive_seed456_r2 (cuda:0, ~78%)，bs8_nmin4_uniform_seed456_r2 (cuda:2, ~78%)

### 3. 📊 当前状态
刚完成全文数据正确性审计（DDL May 25 前底线任务）。修复 4 个数值错误，更新了 results.tex:120 的 n_min=1 ablation 数据（旧 τ=0.8 值 17.789 → 新 τ=0.7 2-seed mean 17.74±0.01 + 交互效应解释）。

**Registry 状态：**
- RUNNING：bs8_nmin4_adaptive_seed456_r2 (cuda:0)，bs8_nmin4_uniform_seed456_r2 (cuda:2) — 预计 ~22:00 UTC 完成
- ANALYZING → DONE：aeff_only_nmin1_seed42 (17.750)，aeff_only_nmin1_seed123 (17.733)
- PREPARING：aeff_only_nmin1_seed456 — 等 GPU 释放

**等待中：**
- Agent 完成 B=8 seed456 eval 后会回调
- Agent 会在 B=8 完成后启动 aeff_only seed456（cuda:0，加 --num_train_tokens）
- Agent 收到了 Figure 2 caption "3.5--5.9" 和 intro "5.8×" 的验证任务

### 4. 📋 待办
- B=8 seed456 训练完成 → eval holdout PPL → 计算 3-seed Δ → 更新 results.tex:122 的 B=8 数据从 "2-seed mean" 到 "3-seed mean ± SD"
- B=8 GPU 释放 → 启动 aeff_only_nmin1_seed456 (cuda:0, --num_train_tokens 200000000 --tau 0.7 --n_min 1)
- aeff_only seed456 完成 → 更新 results.tex:120 的 n_min=1 数据从 "2 seeds" 到 "3 seeds"
- Agent 回报 Figure 2 caption "3.5--5.9" 来源 → 如无法溯源则修正为实际数据（seed means ~3.5）
- Paper Agent 写作修复（R12 action items）完成 → 检查 abstract word count、page limit、wording 调整

### 5. 🎯 战略上下文
**核心发现（3 findings + practical corollary）：**
1. D&R epoch confound：>95% 优势来自多 epoch 曝光
2. Detector 需要 discrimination + calibration 双重要求
3. Minimum intervention 优于 unconstrained maximization
4. Adaptive b* 在 ρ≥0.4 改善（practical corollary）

**关键决策链：** D126（n_min=1 inline expansion）→ D127（2-seed 数据写入，确认交互效应）

**易错点：**
- 旧 nmin1_seed42 (17.789) 用 τ=0.8，与论文标准 τ=0.7 不可比——已替换，不要回退
- Registry 中 hyperparams.contamination_ratio 可能与 CLI 实际参数不一致（aeff_only 命令行未传 --contamination_ratio，registry 写 0.4 但 argparse 默认 0.2）。τ 显式指定时 contamination_ratio 不影响训练，但后续实验务必显式传
- ESS-only b_star_mean 实际 ~3.5（seed42=3.51, seed123=3.55），Figure 2 caption 的 "5.9" 来源未确认
- 审稿 R11-C1（N=3 seeds 统计力不足）是结构性限制，无法短期解决，rebuttal 用多角度论证
- Paper Agent 正在处理 R12 writing fixes（abstract 压缩、§3 压缩、wording 软化），不要重复派单


---
