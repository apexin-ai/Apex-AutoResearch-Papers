# agent / loop_10.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`55a1cfceabd4628455e5.json`](../../sessions/55/55a1cfceabd4628455e5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T12:33:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `westc-26893` 只有 1 块 GPU，exp-004 7B 正在跑，**不要在 exp-004 完成前启动任何 GPU 任务**
- EXP-D OBD 评估必须用 **v2 逻辑**（6-class argmax，无 capping 无概率合并）+ `random_state=42`。概率合并版已被 Director 降级为 appendix sensitivity，不能作为主报告数字
- McNemar p=0.081/0.069 **不显著**，这是 Director 期望的结果——支撑 discussion.tex "not statistically significant" 措辞。不要试图"修复"为显著
- K* 定义已统一为 **95% CI lower bound**（非 point estimate），所有文本/图表/代码必须一致。draw_kstar_theta.py 中的 AUC_DATA 已是 CI lower bounds

### 2. 🖥️ 基础设施快照
- 服务器：`westc-26893`，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，Python 在 `/root/miniconda3/bin/python`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 已有模型：Qwen2.5-1.5B-Instruct, Pythia-1.4B, OLMo-1B（均在 HF cache 中），Qwen2.5-7B 正在被 exp-004 使用
- 数据目录：`data/`(Qwen-rw), `data_exp001_pythia/`, `data_exp002_olmo/`, `data_exp017_qwen_cont/`，每个含 depth_0~5.jsonl + features.csv
- 活跃进程：exp-004 7B（tmux: `exp004`, cuda:0），ETA ~2026-05-16 06:00 UTC
- Cron：exp-004 监控已注册（westc-26893, 300s interval），但当前 session 的 CronList 为空（session 切换时 cron 重建）——**新 session 需要 reconcile_crons**

### 3. 📊 当前状态
刚完成的工作：
- EXP-D 最终修复：v2 逻辑+seed42 → 38.0%，McNemar 不显著（p=0.081/0.069），5 种子 std=0.0。`artifacts/rebuttal/exp_D_mcnemar_final.json` 已保存，registry 已更新
- K* 定义统一：fig_kstar_theta.pdf 重绘（CI lower bounds），experiments_c1.tex / appendix_extended.tex / main.tex 三文件已修正
- EXP-E 15-pair pairwise significance 已发 Director（MMLU 10/15 sig, HellaSwag 9/15 sig）
- Cross-scorer table (`tab_crossscorer.tex`) 已写入 paper
- exp-012 代码准备中（Worker `worker_code_exp_012_prep_20260515T123155` 正在服务器上写 Binoculars + log-perplexity 脚本）

Registry 摘要：
- RUNNING: `exp_004_7b_crossscale`（7B scale validation, ETA ~05-16 06:00）
- PREPARING: `exp_012_binary_confidence`（等 exp-004 完成后提交）
- DONE: 其余 17 个实验全部完成（含 EXP-A~E rebuttal 补充实验）

等待中：
- Worker `worker_code_exp_012_prep` 回调（代码 + dry-run）
- exp-004 cron 完成回调

### 4. 📋 待办（条件触发式）
- `worker_code_exp_012_prep` 完成 → 验证脚本 dry-run 通过，确认 Binoculars 实现正确
- exp-004 cron 回调（完成/失败）→ 按 on-experiment-done skill 处理：分析结果、更新 registry、汇报 Director。K*=2 → 强化 narrative；K*>2 → 需讨论 scale effect
- exp-004 完成 + exp-012 代码就绪 → 立即 `submit_on_allocated` 提交 exp-012（3 GPU·h）
- exp-012 完成 → 分析 Spearman ρ，汇报 Director。如时间允许，排 exp-008 retrain-chain（8 GPU·h）
- Director 要求写 rebuttal → 加载 rebuttal skill，用 EXP-A~E + exp-004 结果逐条回应

### 5. 🎯 战略上下文
- **核心结论**：K*=2 across all ≤1.5B configurations（8 configs, θ=0.60）。这是论文的 central claim
- **决策链**：D031 confirmed K*=1 cross-scorer 不需要 framing 调整（scorer-sensitive boundary ≠ claim violation）；EXP-D McNemar 不显著 → 支撑 "OBD nominal advantage not statistically significant" 措辞
- **投稿目标**：EMNLP 2026 ARR May 2026，deadline May 25
- **Reviewer 关键 concerns 已全部有实验覆盖**：FR-2 Critical(scorer)→EXP-A, FR-3 Critical(self_BLEU)→EXP-B, FR-5(significance)→EXP-E, FR-11(permutation)→EXP-C, FR-12(OBD vs LLM)→EXP-D, R2 Critical(scale)→exp-004
- **易踩坑**：
  1. 概率合并版 OBD accuracy=44.4% 看起来"更好"但 d4=80% 偏倚，Director 已明确否决作为主报告
  2. K*(θ) 图和文本中的数值必须用 CI lower bounds，不要回退到 point estimates（之前 "K*=3 uniformly at θ=0.55" 是错的，只有 Qwen-rw 和 Qwen-cont 到 3）
  3. exp-004 cron 在 session 切换后需要 reconcile——不要假设上个 session 的 cron 还活着
  4. `xcolor` 包由 acl.sty 加载，不需要手动加到 main.tex


---
