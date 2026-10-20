# reviewer / loop_3.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`cca66d6dcae98e5c66ba.json`](../../sessions/cc/cca66d6dcae98e5c66ba.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-24T03:08:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- gpu_ids: [cuda:0, cuda:1, cuda:2, cuda:3] 全部在白名单内，但当前 4 张 GPU 全部空闲——无需 GPU 边界检查
- Llama clean baseline 已确定：mean=+0.262, SD=1.542（n=10）。**绝对不能**再用 V0 hardcoded baseline (mean=-0.312, SD=0.840)——这个已被证明来自废弃的 eval 代码
- ctrl_contam_llama (item seed=999) 和 ctrl_contam_pilot (item seed=42) 的结果**不可混放**在同一表格。论文 Table 1/2 用的是 ctrl_contam_llama 数据，registry 里的 Llama multi-seed expansion 来自 ctrl_contam_pilot
- Mistral clean baseline (mean=4.024, std=2.052) 已审计通过，但 s4-s7 的 checkpoint 随旧服务器丢失不可恢复

### 2. 🖥️ 基础设施快照
- 服务器：westd-35694 (root)，4× RTX PRO 6000 Blackwell (96GB)
- 工作目录：/root/autodl-tmp/（ctrl_contam_llama/, ctrl_contam_pilot/, ctrl_contam_mistral/）
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct 等
- 论文 workspace：/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/
- Anon repo：anonymous-nlp-2026-2/irt_personfit_contam（最新 commit 2421ca8）
- 活跃进程：无。4 张 GPU 全部空闲，0 MiB 占用

### 3. 📊 当前状态
论文已完成最终 polish 并推送到 anon repo（commit 2421ca8）。DDL 2026-05-25。

**已完成的审查链**：
1. Llama clean baseline 危机：发现 V0 hardcoded 错误 → 10 seeds re-eval → 确认 mean=+0.262 → 全部 d 值重算 → 论文/figures/registry 全部更新
2. 跨 pipeline 差异诊断：确认 item selection seed 不同 (999 vs 42) 是根因
3. Mistral baseline 审计：通过（eval 始终是 V1，6/10 值验证一致）
4. 数字审计：9 处不一致全部修复（0.3→0.4×, ARC-C 89.7%, CI 值, leaderboard appendix 标注等）
5. 最终论文质量审查：PASS（story 完整，negative results 恰当，limitations 充分）
6. Polish commit 快速审查：PASS

Registry: 大量实验处于 PREPARING/ANALYZING 状态（multi-seed expansion），但论文不依赖这些——论文数据来自已完成的 ctrl_contam_llama + Qwen + Mistral 实验。

### 4. 📋 待办
- Director 决定提交 → 无需 Reviewer 进一步动作，论文已 review-ready
- 如果 Director 要求补 Mistral 5%/25% → 我已建议不补（风险 > 收益），但如果他坚持：训练+eval ~70min/condition 可并行，然后需更新 Table 1/2/3 + 两个 figure + prose
- 如果 Director 转发新的章节审查请求 → 按 Mode B 审查，注意先检 Agent 是否读过 red-section skill
- contam_5_s3 |d|=1.44 outlier → 已报告为 warning，论文 appendix tab:llama_multiseed 已包含此值，不需额外动作

### 5. 🎯 战略上下文
- 论文核心结论：IRT person-fit (lz*) 可检测 SFT 污染，但价值在诊断而非检测（acc z-score 检测力更强）。三个 behavior boundaries：θ-shift dynamics, detection-diagnosis tradeoff, non-monotonic dose-response
- 投稿目标：EMNLP 2026 Main Conference（ARR 统一审稿，8 页限制，当前 7 页）
- **最容易判断错的事**：看到 registry 里 Llama d 值 |d|>5 不要以为是最终值——那些全部用了错误的 V0 baseline，正确值是 |d|≈2-3。论文里的值才是对的
- **容易踩的坑**：ctrl_contam_pilot 和 ctrl_contam_llama 的 contam_25 s1 lz* 差 64%（-4.616 vs -2.805），不是 bug 而是 item selection seed 不同。不要试图"统一"它们
- Appendix §baseline_meaning (line 130) 仍用 leaderboard Mistral 值 (acc=0.514, lz*=+5.42) 而非 controlled experiment 值——已加标注 "distinct from our controlled experiments" 但仍是最弱的 appendix section


---
