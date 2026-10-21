# reviewer / loop_1.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`b5bd19a050ce1372bc91.json`](../../sessions/b5/b5bd19a050ce1372bc91.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-22T18:20:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- **rtx6000-4x GPU 白名单**：`gpu_ids=[cuda:0, cuda:1, cuda:2, cuda:3]`，全部合法。GPU 0 跑 exp-009，GPU 1-3 跑 vLLM judge 服务
- **autodl-8gpu GPU 分配**：GPU 0 跑 exp-003b MCMC（tmux=exp003b）。GPU 1-3 的 vLLM judge 已全部停止，当前空闲
- **exp-003 joint_gmfrm R-hat=1.73, ESS=6 — 不可引用任何 joint_gmfrm 数字**（θ、c_n、τ=0.857），直到 exp-003b 收敛确认
- **references.bib 中 zhou2025psnirt**（非 lin2025）— 已更正，不要改回

### 2. 🖥️ 基础设施快照
- **rtx6000-4x**：`/root/gated_mfrm_judge_bias`，Python=系统 python3
  - GPU 0: exp-009 (PID 112923, ~80% done, rho=0.9)
  - GPU 1: qwen vLLM port 8002 (PID 420981, max-model-len=8192)
  - GPU 2: llama vLLM port 8001
  - GPU 3: mistral vLLM port 8003 (PID 421050, max-model-len=16384)
  - 9 个 judge collector 进程在跑（rtx6000 侧），总计 ~30k judgments
- **autodl-8gpu**：`/root/gated_mfrm_judge_bias`，Python=/root/miniconda3/bin/python3，conda base
  - GPU 0: exp-003b (tmux=exp003b, HalfNormal prior rerun, chain 1/4 sampling ~94%)
  - GPU 1-3: 空闲（vLLM judge 已停止）
  - autodl judge 收集也已停止（3.4k-0.6k/9000 per judge），需重启
  - Qwen2.5-7B 下载卡住（orchestrator2 在等它）
- **本地 workspace**：`/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/`
  - 论文：`docs/paper/*.tex`（intro/method/background/related_work 已写，experiments/conclusion/limitations 为空 stub）
  - Registry: `registry.yaml`
  - exp-004 代码已部署到 autodl，results 在 autodl `/root/gated_mfrm_judge_bias/exp004/results/`

### 3. 📊 当前状态
**刚完成**：
- 审查 exp-003 全量结果 → joint_gmfrm 收敛失败（R-hat=1.73），posted CRITICAL
- 审查 exp-004 baseline 对比 → 全部 7 baseline τ=0.786，只有 joint 0.857（但不可信）
- 审查 exp-002 sensitivity → 权重鲁棒 Spearman≥0.992
- 完成 Director 请求的 contingency 分析（τ 回落 worst case）
- 确认论文 5 个 CRITICAL 全部已修复（r-value、Stage 2、prior、propositions count、bib）

**RUNNING 实验**：
- `exp-009`：rtx6000 GPU 0，160/200 (80%)，ETA ~3-4h，OVB bias 单调性验证
- `exp-003b`：autodl GPU 0，HalfNormal prior rerun，chain 1/4 sampling 94%，ETA ~1.5h total
- `exp-002`：registry 仍 RUNNING（实际 exposure scores 已产出，可能未更新 status）

**等待中**：
- exp-003b 完成 → 需要我立即审查收敛诊断（R-hat、ESS）和 τ
- exp-009 完成 → 需要我审查 OVB bias_slope 跨 ρ 的单调性 + bias_corr
- Director 可能下发 paper Phase 2 写作审查请求

### 4. 📋 待办（条件触发式）
- **exp-003b 完成 + R-hat<1.05 + τ≥0.85** → 确认可用，通知 Director 启动 Phase 2 写作 + 消融实验（W7）
- **exp-003b R-hat<1.05 但 τ≈0.786** → 触发 Plan A（diagnostic framing），通知 Director 调整 paper story，参考 mvp_001 null-detection 叙事
- **exp-003b R-hat>1.05** → 建议 Plan B（SVI init + MCMC 或 fix θ/b/d only estimate c_n），这是最坏情况
- **exp-009 完成** → 审查 bias_vs_rho.csv 全量数据，验证 W2 所需的 linear OVB 近似精度（聚合 mean(bias_corr) per ρ）
- **paper Phase 2 章节提交** → 按 §5 审查维度逐条评分（claim 可信度、叙事逻辑、审稿人攻击面），特别注意 c_n 相关 claim 是否有收敛的数据支撑
- **autodl judge 重启** → 检查 GPU 使用是否在白名单内，验证 collector resume 正常

### 5. 🎯 战略上下文
- **项目核心**：G-MFRM 联合估计 judge bias + contamination。理论贡献（OVB + identifiability）已固化。实验贡献取决于 exp-003b。
- **审稿报告 Overall 1.5**（基于空 experiments/conclusion/limitations），reviewer 预测补全后 3.0-3.5。Findings (3.0) 高概率可达，Borderline Conference (3.5) 需 exp-003b positive signal。
- **最容易判断错的事**：
  1. **不要把 horseshoe 版 τ=0.857 当可信数字引用** — ESS=6，R-hat=1.73，只是巧合稳定
  2. **N=8 是根本性功效限制** — 最多 1 个 rank swap，τ 最大改善 0.071。不要期待 "significant improvement"
  3. **mvp_001 在 ρ=0 时 joint ≈ sequential（p=0.48）** — 如果 Arena-Hard contamination 低，τ=0.786 是理论预期的 null detection，不是方法失败。论文应显式引用 mvp_001 支撑此叙事
  4. **exp-003b 仍然命中 max tree depth**（HalfNormal 也是 1023 steps）— 问题不仅是 horseshoe funnel，c_n·e_i 乘法项本身有几何挑战。如果 R-hat 仍差，考虑 conditional estimation（fix θ/b/d, only sample c_n）
  5. **autodl judge 收集已停止** — 如果需要更多 judgment 数据来增加 exp-003 的覆盖率，需要重启 vLLM + collector


---
