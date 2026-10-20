# reviewer / loop_19.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`0f8b89637753e222212c.json`](../../sessions/0f/0f8b89637753e222212c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-23T20:01:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 上只能用 cuda:0/1/2/3（4 卡全在白名单内，但越界即 CRITICAL）
- 14B dev eval 用 batch_size=1（与 s42 一致）；14B test eval 存在 batch_size confound（s42 用 bs=1，s43 用 bs=16），已报告为 warning，跨 seed 绝对值不可直接比，但 within-pair tax 有效
- Evidence tax 定义：tax = ign_f1(no_evi) − ign_f1(with_evi)，正=evidence hurts，负=evidence helps
- Abstract claim "approximately neutral at ≥4B" 指的是 **training-time tax**（SFT with-evi vs no-evi），不是 inference-time RSFT tax——不要搞混

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，工作目录 /root/autodl-tmp/freige/
- Python：/root/miniconda3/bin/python（conda base）
- 模型路径：/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,4B,8B,14B}，/root/autodl-tmp/models/meta-llama/Llama-3.1-8B
- RSFT checkpoints：/root/autodl-tmp/rsft_output_14b_s43（最新），/root/autodl-tmp/rsft_output 等
- 数据：/root/autodl-tmp/data/docred/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/
- 活跃进程：plan017_14b_rsft_s43_eval (PID 260785, tmux=plan017_14b_rsft_s43_eval, cuda:0, with-evi dev, ~88% done)
- 已完成：plan017_14b_rsft_s43_no_evi_eval (cuda:2, exit 0, Ign-F1=57.13)

### 3. 📊 当前状态
**刚完成**：
- 审查了 3 个 final audit workers（abstract-crosscheck、figure-appendix、table-registry-trace），均已报告 Director
- 审查了 anon-repo-integrity + anon-repo-cleanup workers，发现 wandb project name 泄露已修复，`/root/autodl-tmp/` 硬编码路径在匿名仓库中已清理
- 14B s43 dev no-evi eval 完成：**Ign-F1 = 57.13**（s42 was 54.32，差 +2.81pp）

**等待中**：
- plan017_14b_rsft_s43_eval (with-evi dev, cuda:0) — 约 88% 完成，预计 ~30-60min
- 完成后可计算 14B s43 dev evidence tax 和 2-seed dev variance compression

**已报告给 Director 的未修复问题**：
1. 31× vs 32.6×（experiments.tex:63 vs appendix tab:variance_ci:132）
2. DREEAM Evi-F1 54.01% vs 54.15（experiments.tex:110 vs appendix.tex:306）
3. EDCR 0.654 vs 0.6487（experiments.tex:104 vs tab:main:29）
4. 4-seed std 0.49 与表中 per-seed 值不自洽（appendix.tex:42）
5. LLaMA test 行混用 v1/v3 eval（truncation 56.6% vs 60.0%）
6. 8B RSFT s42 跨表用不同 checkpoint

### 4. 📋 待办
- plan017_14b_rsft_s43_eval cron 回调 → 读 Ign-F1 → 计算 s43 dev tax = 57.13 − with_evi → 与 s42 dev tax (−4.54pp) 对比 → 计算 2-seed dev mean tax ± std → 报告 Director
- Agent 更新 tab:scaling / appendix 的 14B dev 数据 → 审查更新后的数字一致性
- Director 回复 6 个数字不一致修复方案 → 验证修复
- Round 3 review 触发 → 按 §5 审查模式 B 执行全文对抗审查（先 Read paper-quality-lessons.skill.md）

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Main via ARR July cycle（~54 天）
- Round 2 评分 3.0 (Findings)，升级路径 3.0→3.5→4.0
- 3 个核心贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Evidence tax + variance compression
- 14B 是唯一 dev-test tax 方向反转的 scale（dev −4.54pp vs test +0.43±0.49pp），s43 dev 结果将进一步确认/修正这个叙事
- s43 no-evi dev Ign-F1=57.13 远高于 s42 的 54.32（+2.81pp），预示 seed variance 在 no-evi 条件下较大——如果 with-evi 也高（接近 s42 的 58.86），则 2-seed dev tax 可能比 s42 单独的 −4.54pp 小很多
- 易错点：不要把 training-time tax（SFT with vs no evidence）和 inference-time tax（RSFT model with vs without evidence output）混为一谈——abstract 和 §4.3 用前者，§4.4 和 fig_evidence_tax 用后者


---
