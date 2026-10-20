# Research conversation: <project_context> # 项目: distrib_canary_collapse ## 运行环境 - 服务器名: westd-19828 - SSH 账户: root（调用 ssh_execute / submit_train

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/73842314-3ca4-45a0-a352-92fd62b21080.jsonl`
- **Structured JSON:** [`2df17e7ebb05bed74f4c.json`](../../sessions/2d/2df17e7ebb05bed74f4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T10:58:27.420Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T10:58:27.420Z",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "content": "&lt;project_context>\n# 项目: distrib_canary_collapse\n\n## 运行环境\n- 服务器名: westd-19828\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh westd-19828  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/distrib_canary_collapse\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C002**: 论文真源为 docs/paper/，禁止直接编辑 artifacts/_project/paper/。需要同步时从 docs/paper/ 复制覆盖。（原因：两目录已分叉，artifacts 版本落后且缺内容，独立维护导致 Reviewer 误报和数字不一致风险。） [来自 D046]\n- **C003**: 禁止引用 α≤0.50 的 TY Granger 显著率作为支撑证据——3-seed 已确认 TY 在低 α 下种子不稳定（d_max 跨 seed 0→1→2，df_resid 从 7 降至 1）（原因：C001 multi-seed 验证完成：0/8 pairs 在 3 seed 一致显著，根因是 T=11 下 ADF 积分阶数不稳定。TY 只在 α=1.0 (4-seed pooled) 可用。）\n- **C004**: 禁止任何 Agent session 在未确认实验状态的情况下 kill 正在运行的训练进程或 rm -rf 实验输出目录。操作前必须先 SSH 检查进程存活 + 目录 generation 进度。（原因：2026-05-16 并发 Agent session 误杀已运行 7h 的 a075_s43/s44 实验，导致 ~14 GPU-hours 浪费。根因是另一 session 未检查实验进度就执行了 kill + rm -rf + 重启。）\n- **C005**: EXIT_CODE=129 (SIGHUP) 不等于实验失败——必须先检查 gen 目录和 all_metrics.json 完整性再判定（原因：M015: 连续三次误判（C4 α=0.50、α=0.60、GPT-2m s43），浪费诊断 Worker + GPU 空转时间） [来自 M015]\n- **C007**: M031: 提交实验前必须 df -h 确认目标服务器剩余空间 ≥ 实验预估大小 2x。大模型(≥3B)优先分配到大容量服务器。19828 仅 250G 总容量，谨慎使用（原因：smollm3_s43 因 19828 磁盘满失败（250G/250G），4.21h GPU 时间浪费） [来自 M031]\n- **C008**: K 值计算 threshold 投票必须使用 registry `threshold_onset_3sigma` 字段，禁止使用 JSON 的 `3x_sigma_drift` 或 `significant`。D105+D111 必须联合应用，禁止独立 patch 叠加。（原因：M034: Worker 两次使用错误 threshold 标准（regular significant 和 3x_sigma_drift），导致 K 值系统性虚高。3x_sigma_drift 是简单幅值检查，D105 true 3sigma 是带 FDR 校正的统计检验，中等信号时差异 0/8 vs 8/8。） [来自 D116]\n- **C009**: M035: D111 direction filter 已修正 peak_lag > 0 → peak_lag < 0。xcorr 约定: lag<0 = canary leads downstream (forward causation)。所有分析脚本必须使用 peak_lag < 0 作为 forward direction 判定条件。（原因：M035 sign reversal bug: D111 原 filter `peak_lag > 0` 实为反向因果。修正后 K≥3 从 ~0/8 恢复至 ≥5/8 in 11/13 experiments。D116 \"K≥3 collapse\" 确认为 bug artifact (D117)。） [来自 D117]\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## Task\n\nWrite compressed Experiments/Results section (4 subsections ONLY) for the paper \"A Detection Phase Transition in Iterative Model Collapse\" (EMNLP 2026, 8-page limit). Current Results is ~474 lines; target is ~70 lines of prose + 2 compact tables + 2 figure floats, fitting ~3 pages in dual-column format.\n\n## Setup (do these first)\n\n1. `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n2. `Read /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex` — reference for exact numbers\n\n## Output\n\nWrite to: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex`\n\nInclude ONLY the 4 results subsections below. Do NOT include `\\section{Experiments}`, `\\subsection{Experimental Setup}`, or any preamble/packages. Start directly with `\\subsection{Detection Phase Transition}`.\n\n---\n\n## §5.1 Detection Phase Transition (\\label{sec:regime}) — ~20 lines prose\n\nHero section establishing the core discovery. Include ALL of:\n\n1. Despite ubiquitous diversity collapse at all α (distinct-1: -14.1% at α=0.0 to -40.3±0.3% at α=0.25), causal detectability is sharply regime-dependent\n2. PermG: 0/8 FDR-significant from α=0.00 through α=0.45; jumps to 6/8 at α=0.50 (2 fp32 seeds, consistent)\n3. Cumulative contamination barely changes: C=1-(1-α)^10 gives 99.75% (α=0.45) vs 99.90% (α=0.50), 0.15pp difference\n4. Sigmoid regression: α_c=0.476, k≥200, Δα≈0.02, R²=0.969 (vs power-law R²=0.808, ΔAIC=18.2)\n5. First-differencing scopes the claim: canary→diversity 24/24→24/24 survives; canary→perplexity F≈0, p=0.99 (spurious). Canary claim scoped to diversity only\n6. At α=1.0: 24/24 forward, 0/24 reverse (4 seeds) — directional asymmetry confirmed\n7. Sub-threshold at α=0.45: PermG FDR p=0.059 (s43), 0.091 (s42), consistent with power-threshold interpretation (\\S\\ref{sec:theory})\n8. Spec curve: 1,160 specs confirm phase transition is specification-invariant (ONE sentence)\n9. Canary blind spot at α=0.10: distinct-1 -39.6% but entropy indistinguishable from null (-5.3% vs -4.6±0.4%)\n\nFigure float: `\\begin{figure}[t]\\centering\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\\caption{...}\\label{fig:metric_trajectory}\\end{figure}` — compact caption showing one-generation canary lead at α=1.0 across 4 seeds.\n\n---\n\n## §5.2 Dose-Response and the $S \\times R$ Framework (\\label{sec:dose_response}) — ~20 lines prose\n\nContent:\n\n1. Four regimes: blind (α≤0.45, 0/8), onset (α≈0.50, 6/8), synchronous dip (α≈0.60, s42:3/8, s43:0/8, dual-seed), detection (α≥0.75, 5-6/8 per seed, 3 seeds; α=1.0, 6/8, 4 seeds)\n2. S×R framework: S(α) rises monotonically; R(α) drops at α≈0.60 when relaxation time matches observation interval; product S×R is non-monotonic, explaining the dip\n3. Method sensitivity (brief): method choice swings significance 100%→37.5%; inter-method κ=0.185; spurious rate ≥62.5%. PermG: zero null-control FPR + consistent detection at α≥0.50 (Table~\\ref{tab:method_comparison})\n4. T=20 predictions from Power(α,T) = Φ(S·R·√T/σ): (i) α_c left-shift, (ii) transition smoothing, (iii) method-dependent α_c. Under empirical verification\n\nFigure float: `figures/fig_dose_response.pdf`, label `fig:regime_map`, compact caption with 4 regimes annotated.\n\nTable 1 float (method comparison, COMPACT, single-column width):\n\nData matrix (forward-direction FDR significance %, Pythia-410M, seed 42, fp32, direction-checked):\n| Method | α=0.0 | α=0.25 | α=0.50 | α=0.75 | α=1.0 | FPR_null |\n|--------|-------|--------|--------|--------|-------|----------|\n| Naive XCorr | 75 | 12.5 | 37.5 | 87.5 | 0 | 75 |\n| Diff. XCorr | 0 | 37.5 | 87.5 | 75 | 75 | 0 |\n| Threshold (3σ) | --- | 0 | 50 | 0 | 0 | --- |\n| Perm. Granger | 0 | 0 | 75 | 75 | 75 | 0 |\n| Toda-Yamamoto | --- | 0 | 37.5 | 37.5 | 50 | --- |\n\nLabel: `tab:method_comparison`. Caption: \"Forward-direction FDR significance rates (%) across contamination levels (Pythia-410M, fp32, direction-checked). Each cell: fraction of 8 validated pairs reaching BH-corrected significance. PermG achieves zero null-control FPR with consistent detection at α≥0.50.\"\nUse \\small, booktabs, fit in one column.\n\n---\n\n## §5.3 Cross-Architecture Generalization (\\label{sec:generalization}) — ~15 lines prose\n\nContent:\n\n1. 15 model-seed combinations, 6 families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), 345M-6.9B, 2 domains\n2. PermG fwd ≥6/8 in 13/15 (87%)\n3. Two exceptions: Pythia-1.4B s42 Wiki (2/8, seed-dependent, recovers to 6/8 in s43) and SmolLM3-3B (3/8, ECE-only canary)\n4. C4 domain: Pythia-1.4B 8/8 on C4 vs 2/8 on Wiki at same scale, recovering to 7/8 at Pythia-6.9B. Dataset characteristics modulate detection power independently of model capacity\n5. C4 bidirectionality: PermG reverse 7/8 at α=0.50 vs 0/24 on WikiText — domain-dependent directionality\n6. α_c≈0.50 boundary is architecture-independent\n\nTable 2 float (cross-architecture, COMPACT, 1 row per model config):\n\n| Model | Params | Domain | PermG fwd |\n|-------|--------|--------|-----------|\n| Pythia-410M | 410M | Wiki | 6/8 |\n| Pythia-1.4B | 1.4B | Wiki | 2--6/8† |\n| Pythia-6.9B | 6.9B | Wiki | 7/8* |\n| GPT-2-medium | 345M | Wiki | 6/8 |\n| OPT-1.3B | 1.3B | Wiki | 6/8 |\n| Qwen3.5-0.8B | 0.8B | Wiki | 8/8 |\n| SmolLM3-3B | 3.0B | Wiki | 3/8‡ |\n| Padding-410M | 410M | Wiki | 6/8 |\n| Pythia-1B | 1.0B | C4 | 7--8/8 |\n| Pythia-1.4B | 1.4B | C4 | 8/8 |\n\nFootnotes: †Seed-dependent (s42: 2/8, s43: 6/8). *bf16 (exceeds single-GPU fp32). ‡ECE-only canary (entropy 0/4).\nMulti-seed models (range shown): Pythia-410M, Pythia-1.4B Wiki, GPT-2-medium, OPT-1.3B, Pythia-1B C4 (2 seeds each). Others: single seed. Total: 15 combinations.\nCaption: \"Cross-architecture PermG forward detection (α=1.0). Detection (≥6/8) confirmed in 13/15 conditions (87%) spanning six model families.\"\nLabel: `tab:generalization`. Use \\small, booktabs, single-column width.\n\n---\n\n## §5.4 Canary-Based Early Intervention (\\label{sec:intervention}) — ~15 lines prose\n\nContent:\n\n1. Predictive cessation: switch α to 0.0 when entropy drops >15% relative to generation 0\n2. Fires generation 1 (both Pythia-410M and 1.4B), one generation before reactive baseline (distinct-1 >10%)\n3. Peak perplexity reduction: 58% pooled (bootstrap 95% CI: 29-64%). Specific: s42 fp32 56.99 vs 157.09\n4. Recovery generation 2 (predictive) vs generation 4 (reactive)\n5. Scale-independent: identical trigger, recovery, convergence across 3.4× scale gap (410M to 1.4B)\n6. Four-layer detection taxonomy: dimensionality collapse (α≥0.10), distributional variance (α≥0.25), causal coupling (α≥0.50), dynamical stability (α≥0.50)\n\nNo display item in this subsection.\n\n---\n\n## ACTIVE CONSTRAINTS (violations = rejection)\n\n- D131: \"steep onset\" and \"detection phase transition\" (NEVER \"near-discontinuous\")\n- D141: All α_c mentions MUST include \"at T=10\". Power Theory: \"consistent with\" (NEVER \"confirms\"/\"validates\")\n- D142: NO CSD data in Results (CSD = Discussion only)\n- D143: NO TY=7/8 evidence (retracted, d_max artifact)\n- D145: C4 wording: \"dataset characteristics modulate detection power independently of model capacity\"\n- M037: Dose-response uses PermG only; K≥3 column NOT in Table 2\n- D079: fp32 main axis; bf16 only in Pythia-6.9B footnote\n\n## WRITING RULES (from paper-writing-norms, strictly enforced)\n\n- NO em-dashes (—) or explanatory en-dashes ( – ). Use commas, parentheses, or split into two sentences\n- NO -ing clause endings (\"..., demonstrating that...\", \"..., confirming that...\")\n- NO \"Furthermore\"/\"Moreover\"/\"Additionally\" chains\n- NO \"It is worth noting\"/\"Notably\"/\"Interestingly\"\n- NO \"leverage\"/\"utilize\"/\"delve\"/\"facilitate\"/\"myriad\"/\"plethora\"\n- Paragraphs: natural length (5-8 sentences), not 2-3 sentence fragments\n- Every number must serve the narrative; no data dumping\n- Table captions self-contained; above the table\n- booktabs only (\\toprule/\\midrule/\\bottomrule), no \\hline, no vertical lines |\n\n## CROSS-REFERENCES\n\n- Phase transition figure in Introduction: Figure~\\ref{fig:phase_transition}\n- S×R theory section: \\S\\ref{sec:theory}\n- Detailed drift table (now Appendix): Appendix~\\ref{app:robustness} or \"Appendix\"\n- SmolLM3 details: Appendix\n- Consensus validation: Appendix\n- TY limitation details: Appendix\n- Method sensitivity details: \\S\\ref{sec:method_sensitivity} (will be in Methods or Appendix)\n- Distinct-3 results: Appendix~\\ref{app:distinct3}"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T10:58:27.424Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T10:58:27.424Z",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-20T10:58:27.479Z_

&lt;project_context>
# 项目: distrib_canary_collapse

## 运行环境
- 服务器名: westd-19828
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh westd-19828  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/distrib_canary_collapse

## ⚠️ 活跃约束（必须遵守）

- **C002**: 论文真源为 docs/paper/，禁止直接编辑 artifacts/_project/paper/。需要同步时从 docs/paper/ 复制覆盖。（原因：两目录已分叉，artifacts 版本落后且缺内容，独立维护导致 Reviewer 误报和数字不一致风险。） [来自 D046]
- **C003**: 禁止引用 α≤0.50 的 TY Granger 显著率作为支撑证据——3-seed 已确认 TY 在低 α 下种子不稳定（d_max 跨 seed 0→1→2，df_resid 从 7 降至 1）（原因：C001 multi-seed 验证完成：0/8 pairs 在 3 seed 一致显著，根因是 T=11 下 ADF 积分阶数不稳定。TY 只在 α=1.0 (4-seed pooled) 可用。）
- **C004**: 禁止任何 Agent session 在未确认实验状态的情况下 kill 正在运行的训练进程或 rm -rf 实验输出目录。操作前必须先 SSH 检查进程存活 + 目录 generation 进度。（原因：2026-05-16 并发 Agent session 误杀已运行 7h 的 a075_s43/s44 实验，导致 ~14 GPU-hours 浪费。根因是另一 session 未检查实验进度就执行了 kill + rm -rf + 重启。）
- **C005**: EXIT_CODE=129 (SIGHUP) 不等于实验失败——必须先检查 gen 目录和 all_metrics.json 完整性再判定（原因：M015: 连续三次误判（C4 α=0.50、α=0.60、GPT-2m s43），浪费诊断 Worker + GPU 空转时间） [来自 M015]
- **C007**: M031: 提交实验前必须 df -h 确认目标服务器剩余空间 ≥ 实验预估大小 2x。大模型(≥3B)优先分配到大容量服务器。19828 仅 250G 总容量，谨慎使用（原因：smollm3_s43 因 19828 磁盘满失败（250G/250G），4.21h GPU 时间浪费） [来自 M031]
- **C008**: K 值计算 threshold 投票必须使用 registry `threshold_onset_3sigma` 字段，禁止使用 JSON 的 `3x_sigma_drift` 或 `significant`。D105+D111 必须联合应用，禁止独立 patch 叠加。（原因：M034: Worker 两次使用错误 threshold 标准（regular significant 和 3x_sigma_drift），导致 K 值系统性虚高。3x_sigma_drift 是简单幅值检查，D105 true 3sigma 是带 FDR 校正的统计检验，中等信号时差异 0/8 vs 8/8。） [来自 D116]
- **C009**: M035: D111 direction filter 已修正 peak_lag > 0 → peak_lag < 0。xcorr 约定: lag<0 = canary leads downstream (forward causation)。所有分析脚本必须使用 peak_lag < 0 作为 forward direction 判定条件。（原因：M035 sign reversal bug: D111 原 filter `peak_lag > 0` 实为反向因果。修正后 K≥3 从 ~0/8 恢复至 ≥5/8 in 11/13 experiments。D116 "K≥3 collapse" 确认为 bug artifact (D117)。） [来自 D117]


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## Task

Write compressed Experiments/Results section (4 subsections ONLY) for the paper "A Detection Phase Transition in Iterative Model Collapse" (EMNLP 2026, 8-page limit). Current Results is ~474 lines; target is ~70 lines of prose + 2 compact tables + 2 figure floats, fitting ~3 pages in dual-column format.

## Setup (do these first)

1. `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`
2. `Read /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex` — reference for exact numbers

## Output

Write to: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex`

Include ONLY the 4 results subsections below. Do NOT include `\section{Experiments}`, `\subsection{Experimental Setup}`, or any preamble/packages. Start directly with `\subsection{Detection Phase Transition}`.

---

## §5.1 Detection Phase Transition (\label{sec:regime}) — ~20 lines prose

Hero section establishing the core discovery. Include ALL of:

1. Despite ubiquitous diversity collapse at all α (distinct-1: -14.1% at α=0.0 to -40.3±0.3% at α=0.25), causal detectability is sharply regime-dependent
2. PermG: 0/8 FDR-significant from α=0.00 through α=0.45; jumps to 6/8 at α=0.50 (2 fp32 seeds, consistent)
3. Cumulative contamination barely changes: C=1-(1-α)^10 gives 99.75% (α=0.45) vs 99.90% (α=0.50), 0.15pp difference
4. Sigmoid regression: α_c=0.476, k≥200, Δα≈0.02, R²=0.969 (vs power-law R²=0.808, ΔAIC=18.2)
5. First-differencing scopes the claim: canary→diversity 24/24→24/24 survives; canary→perplexity F≈0, p=0.99 (spurious). Canary claim scoped to diversity only
6. At α=1.0: 24/24 forward, 0/24 reverse (4 seeds) — directional asymmetry confirmed
7. Sub-threshold at α=0.45: PermG FDR p=0.059 (s43), 0.091 (s42), consistent with power-threshold interpretation (\S\ref{sec:theory})
8. Spec curve: 1,160 specs confirm phase transition is specification-invariant (ONE sentence)
9. Canary blind spot at α=0.10: distinct-1 -39.6% but entropy indistinguishable from null (-5.3% vs -4.6±0.4%)

Figure float: `\begin{figure}[t]\centering\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}\caption{...}\label{fig:metric_trajectory}\end{figure}` — compact caption showing one-generation canary lead at α=1.0 across 4 seeds.

---

## §5.2 Dose-Response and the $S \times R$ Framework (\label{sec:dose_response}) — ~20 lines prose

Content:

1. Four regimes: blind (α≤0.45, 0/8), onset (α≈0.50, 6/8), synchronous dip (α≈0.60, s42:3/8, s43:0/8, dual-seed), detection (α≥0.75, 5-6/8 per seed, 3 seeds; α=1.0, 6/8, 4 seeds)
2. S×R framework: S(α) rises monotonically; R(α) drops at α≈0.60 when relaxation time matches observation interval; product S×R is non-monotonic, explaining the dip
3. Method sensitivity (brief): method choice swings significance 100%→37.5%; inter-method κ=0.185; spurious rate ≥62.5%. PermG: zero null-control FPR + consistent detection at α≥0.50 (Table~\ref{tab:method_comparison})
4. T=20 predictions from Power(α,T) = Φ(S·R·√T/σ): (i) α_c left-shift, (ii) transition smoothing, (iii) method-dependent α_c. Under empirical verification

Figure float: `figures/fig_dose_response.pdf`, label `fig:regime_map`, compact caption with 4 regimes annotated.

Table 1 float (method comparison, COMPACT, single-column width):

Data matrix (forward-direction FDR significance %, Pythia-410M, seed 42, fp32, direction-checked):
| Method | α=0.0 | α=0.25 | α=0.50 | α=0.75 | α=1.0 | FPR_null |
|--------|-------|--------|--------|--------|-------|----------|
| Naive XCorr | 75 | 12.5 | 37.5 | 87.5 | 0 | 75 |
| Diff. XCorr | 0 | 37.5 | 87.5 | 75 | 75 | 0 |
| Threshold (3σ) | --- | 0 | 50 | 0 | 0 | --- |
| Perm. Granger | 0 | 0 | 75 | 75 | 75 | 0 |
| Toda-Yamamoto | --- | 0 | 37.5 | 37.5 | 50 | --- |

Label: `tab:method_comparison`. Caption: "Forward-direction FDR significance rates (%) across contamination levels (Pythia-410M, fp32, direction-checked). Each cell: fraction of 8 validated pairs reaching BH-corrected significance. PermG achieves zero null-control FPR with consistent detection at α≥0.50."
Use \small, booktabs, fit in one column.

---

## §5.3 Cross-Architecture Generalization (\label{sec:generalization}) — ~15 lines prose

Content:

1. 15 model-seed combinations, 6 families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), 345M-6.9B, 2 domains
2. PermG fwd ≥6/8 in 13/15 (87%)
3. Two exceptions: Pythia-1.4B s42 Wiki (2/8, seed-dependent, recovers to 6/8 in s43) and SmolLM3-3B (3/8, ECE-only canary)
4. C4 domain: Pythia-1.4B 8/8 on C4 vs 2/8 on Wiki at same scale, recovering to 7/8 at Pythia-6.9B. Dataset characteristics modulate detection power independently of model capacity
5. C4 bidirectionality: PermG reverse 7/8 at α=0.50 vs 0/24 on WikiText — domain-dependent directionality
6. α_c≈0.50 boundary is architecture-independent

Table 2 float (cross-architecture, COMPACT, 1 row per model config):

| Model | Params | Domain | PermG fwd |
|-------|--------|--------|-----------|
| Pythia-410M | 410M | Wiki | 6/8 |
| Pythia-1.4B | 1.4B | Wiki | 2--6/8† |
| Pythia-6.9B | 6.9B | Wiki | 7/8* |
| GPT-2-medium | 345M | Wiki | 6/8 |
| OPT-1.3B | 1.3B | Wiki | 6/8 |
| Qwen3.5-0.8B | 0.8B | Wiki | 8/8 |
| SmolLM3-3B | 3.0B | Wiki | 3/8‡ |
| Padding-410M | 410M | Wiki | 6/8 |
| Pythia-1B | 1.0B | C4 | 7--8/8 |
| Pythia-1.4B | 1.4B | C4 | 8/8 |

Footnotes: †Seed-dependent (s42: 2/8, s43: 6/8). *bf16 (exceeds single-GPU fp32). ‡ECE-only canary (entropy 0/4).
Multi-seed models (range shown): Pythia-410M, Pythia-1.4B Wiki, GPT-2-medium, OPT-1.3B, Pythia-1B C4 (2 seeds each). Others: single seed. Total: 15 combinations.
Caption: "Cross-architecture PermG forward detection (α=1.0). Detection (≥6/8) confirmed in 13/15 conditions (87%) spanning six model families."
Label: `tab:generalization`. Use \small, booktabs, single-column width.

---

## §5.4 Canary-Based Early Intervention (\label{sec:intervention}) — ~15 lines prose

Content:

1. Predictive cessation: switch α to 0.0 when entropy drops >15% relative to generation 0
2. Fires generation 1 (both Pythia-410M and 1.4B), one generation before reactive baseline (distinct-1 >10%)
3. Peak perplexity reduction: 58% pooled (bootstrap 95% CI: 29-64%). Specific: s42 fp32 56.99 vs 157.09
4. Recovery generation 2 (predictive) vs generation 4 (reactive)
5. Scale-independent: identical trigger, recovery, convergence across 3.4× scale gap (410M to 1.4B)
6. Four-layer detection taxonomy: dimensionality collapse (α≥0.10), distributional variance (α≥0.25), causal coupling (α≥0.50), dynamical stability (α≥0.50)

No display item in this subsection.

---

## ACTIVE CONSTRAINTS (violations = rejection)

- D131: "steep onset" and "detection phase transition" (NEVER "near-discontinuous")
- D141: All α_c mentions MUST include "at T=10". Power Theory: "consistent with" (NEVER "confirms"/"validates")
- D142: NO CSD data in Results (CSD = Discussion only)
- D143: NO TY=7/8 evidence (retracted, d_max artifact)
- D145: C4 wording: "dataset characteristics modulate detection power independently of model capacity"
- M037: Dose-response uses PermG only; K≥3 column NOT in Table 2
- D079: fp32 main axis; bf16 only in Pythia-6.9B footnote

## WRITING RULES (from paper-writing-norms, strictly enforced)

- NO em-dashes (—) or explanatory en-dashes ( – ). Use commas, parentheses, or split into two sentences
- NO -ing clause endings ("..., demonstrating that...", "..., confirming that...")
- NO "Furthermore"/"Moreover"/"Additionally" chains
- NO "It is worth noting"/"Notably"/"Interestingly"
- NO "leverage"/"utilize"/"delve"/"facilitate"/"myriad"/"plethora"
- Paragraphs: natural length (5-8 sentences), not 2-3 sentence fragments
- Every number must serve the narrative; no data dumping
- Table captions self-contained; above the table
- booktabs only (\toprule/\midrule/\bottomrule), no \hline, no vertical lines |

## CROSS-REFERENCES

- Phase transition figure in Introduction: Figure~\ref{fig:phase_transition}
- S×R theory section: \S\ref{sec:theory}
- Detailed drift table (now Appendix): Appendix~\ref{app:robustness} or "Appendix"
- SmolLM3 details: Appendix
- Consensus validation: Appendix
- TY limitation details: Appendix
- Method sensitivity details: \S\ref{sec:method_sensitivity} (will be in Methods or Appendix)
- Distinct-3 results: Appendix~\ref{app:distinct3}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "694508ff-a291-43df-9e7f-4abfbbd1deda",
  "type": "user",
  "uuid": "2b54296e-d26c-496b-a04c-fb10420d1335",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T10:58:27.478Z_

```json
{
  "parentUuid": "2b54296e-d26c-496b-a04c-fb10420d1335",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "44015d5f-43cd-4b15-9a2d-c84b7b473ba1",
  "timestamp": "2026-05-20T10:58:27.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T10:58:27.478Z_

```json
{
  "parentUuid": "44015d5f-43cd-4b15-9a2d-c84b7b473ba1",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "297b8d15-147d-4450-9d13-b7ea281ba537",
  "timestamp": "2026-05-20T10:58:27.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T10:58:27.478Z_

```json
{
  "parentUuid": "297b8d15-147d-4450-9d13-b7ea281ba537",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6bff37c3-66ab-44c8-97cc-1d893617bb3b",
  "timestamp": "2026-05-20T10:58:27.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "leafUuid": "6bff37c3-66ab-44c8-97cc-1d893617bb3b",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Compress results section for EMNLP paper",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Assistant

_source line 9 · 2026-05-20T10:58:30.209Z_

I'll start by reading the required files, then write the compressed section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bff37c3-66ab-44c8-97cc-1d893617bb3b",
  "isSidechain": false,
  "requestId": "req_011CbDhhhdZXJqJum66KSCx7",
  "type": "assistant",
  "uuid": "c90bbc6f-8281-4acc-95f0-41062d34b4b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYAaYAASCTvcyiowbXgR4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15940,
      "cache_read_input_tokens": 11841,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15940
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T10:58:30.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_012RauXo5ghzg1aqdbEE94Uk`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c90bbc6f-8281-4acc-95f0-41062d34b4b2",
  "isSidechain": false,
  "requestId": "req_011CbDhhhdZXJqJum66KSCx7",
  "type": "assistant",
  "uuid": "3111bc9e-c239-4451-b533-2fd8d04aaa33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYAaYAASCTvcyiowbXgR4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15940,
      "cache_read_input_tokens": 11841,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15940
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T10:58:30.745Z_

<details><summary>↩ Tool result · `toolu_012RauXo5ghzg1aqdbEE94Uk`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "3111bc9e-c239-4451-b533-2fd8d04aaa33",
  "isSidechain": false,
  "promptId": "694508ff-a291-43df-9e7f-4abfbbd1deda",
  "type": "user",
  "uuid": "82e7d2ee-9f85-4ada-b8c9-0077a773a421",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "3111bc9e-c239-4451-b533-2fd8d04aaa33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 12 · 2026-05-20T10:58:31.052Z_

<details open><summary>🔧 Tool call — Read · `toolu_0147aCQuwiyR1r6Sz6Bof89o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82e7d2ee-9f85-4ada-b8c9-0077a773a421",
  "isSidechain": false,
  "requestId": "req_011CbDhhhdZXJqJum66KSCx7",
  "type": "assistant",
  "uuid": "646dd7f8-1eb1-4c04-9c36-3dbe13b0a86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYAaYAASCTvcyiowbXgR4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15940,
      "cache_read_input_tokens": 11841,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15940
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T10:58:31.563Z_

<details><summary>↩ Tool result · `toolu_0147aCQuwiyR1r6Sz6Bof89o`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.10$ uses a single seed (42, preliminary).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.
21	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
22	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
23	Code and data will be released upon publication.
24	
25	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
26	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
27	Cross-correlation analysis uses a maximum lag of 5 generations.
28	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
34	\label{tab:drift_summary}
35	\begin{tabular}{lccccc}
36	\toprule
37	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38	\midrule
39	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
40	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
41	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
42	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
43	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
44	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	
50	\subsection{Method Sensitivity Analysis}
51	\label{sec:method_sensitivity}
52	
53	We open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.
54	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
55	
56	\paragraph{Five-method ablation.}
57	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
58	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{5/16} (31.3\%; moderate supplementary, \S\ref{sec:ty_limitation}).
59	Method choice alone swings significance from \textbf{100\% to 37.5\%} among the primary methods: 50--57\% of pairs classified as significant under one method flip to non-significant under another.
60	The spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is at least \textbf{62.5\%} across the primary methods.
61	Table~\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.
62	
63	\paragraph{First-differencing diagnostic.}
64	A single preprocessing decision can eliminate an entire analysis channel.
65	For canary$\to$diversity pairs at $\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.
66	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
67	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
68	Notably, at $\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.
69	
70	\paragraph{Augmentation order sensitivity.}
71	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
72	After correcting the statsmodels API incompatibility (\S\ref{sec:ty_limitation}), TY achieves moderate detection (3--4/8 at $\alpha{\geq}0.50$) at the default $d_{\max}{=}1$; however, the qualitative finding that this single hyperparameter can swing conclusions between near-universal significance and near-universal non-significance remains, consistent with known properties of the Toda--Yamamoto procedure~\cite{toda1995statistical}.
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\linewidth]{figures/differencing_dmax.pdf}
77	\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\alpha{=}1.0$, 4~seeds). \textbf{(a)}~First-differencing eliminates the canary$\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\to$diversity pairs retain significance after differencing (24/24$\to$24/24). \textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\max}$; after correcting the implementation (\S\ref{sec:ty_limitation}), TY achieves moderate detection at the default $d_{\max}{=}1$, but the qualitative sensitivity to this hyperparameter persists.}
78	\label{fig:differencing_dmax}
79	\end{figure}
80	
81	\paragraph{Inter-method agreement.}
82	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\alpha{=}0.0$ through $\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.
83	Cross-architecture validation on GPT-2-medium (12 canary$\to$downstream pairs) yields Fleiss' $\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.
84	Restricting to three informative methods (excluding naive cross-correlation, which anchors the permissive extreme, and Toda--Yamamoto, which provides moderate supplementary signal) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
85	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
86	Direction checking (D111) itself constitutes a sensitivity dimension beyond the five statistical methods: restricting to forward-direction associations inverts naive cross-correlation's profile from uniformly high (${\approx}100\%$ undirected) to regime-dependent, revealing that much of its apparent signal was reverse-directional.
87	At $\alpha{=}0.0$ (null control), naive cross-correlation still finds \textbf{75\%} (6/8) of forward-direction pairs significant---lower than the undirected 100\%, but still a substantial FPR.
88	Permutation Granger correctly finds 0\%, achieving perfect null-control specificity.
89	At $\alpha{=}0.50$ (fp32), permutation Granger finds 75\% (6/8), while naive finds 37.5\% (Figure~\ref{fig:consensus_heatmap}; Table~\ref{tab:method_comparison}).
90	
91	\paragraph{Method$\times$regime interaction.}
92	Table~\ref{tab:method_comparison} reveals that direction checking reshapes the method hierarchy across contamination levels.
93	At $\alpha{=}0.25$, naive cross-correlation drops to 12.5\% while permutation Granger remains at 0\%, narrowing the gap visible in undirected analysis.
94	At $\alpha{\geq}0.75$, naive rises to 87.5\% while permutation Granger reaches 75\%; both methods detect, but naive's persistent 75\% null-control FPR means its high-$\alpha$ detections cannot be distinguished from false positives without the consensus framework.
95	This regime-dependent reversal, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
96	
97	\paragraph{Why permutation Granger succeeds.}
98	The systematic comparison identifies PermG as the only method combining zero null-control FPR with consistent detection across all regimes where signal exists ($\alpha{\geq}0.50$).
99	Three properties explain this outcome.
100	First, the nonparametric permutation procedure inherently controls FPR by constructing the null distribution from the observed data rather than from distributional assumptions, making it robust to the non-stationarity that inflates false positives in correlation-based methods.
101	Second, Granger tests are directional by construction: they test whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history, naturally filtering the reverse-directional associations that inflate naive cross-correlation's FPR.
102	Third, PermG does not require threshold calibration or augmentation order selection, avoiding the hyperparameter sensitivity observed in Toda--Yamamoto (Figure~\ref{fig:differencing_dmax}b; \S\ref{sec:ty_limitation}) and the power limitations that reduce threshold onset to near-zero detection under $3\sigma$ calibration (\S\ref{sec:threshold_limitation}).
103	By contrast, differenced cross-correlation retains 100\% FDR significance in both forward \emph{and} reverse directions at $\alpha{=}0.75$, failing to distinguish genuine directional precedence from shared dynamics; and Toda--Yamamoto, while achieving moderate detection (3--4/8 at $\alpha{\geq}0.50$), remains sensitive to the augmentation order $d_{\max}$ (\S\ref{sec:ty_limitation}).
104	These complementary failures, exposed through the MMCT evaluation framework, converge on a single recommendation: for short iterative training series ($T{\leq}20$), permutation Granger causality should be the primary detection method.
105	
106	\begin{figure}[t]
107	\centering
108	\includegraphics[width=\linewidth]{figures/consensus_heatmap.pdf}
109	\caption{Method$\times$regime consensus heatmap (Pythia-410M, fp32, 12 contamination levels, direction-checked). Each cell shows the forward-direction detection rate (\% of 8 pairs reaching FDR significance) for five individual methods (top) and two consensus thresholds (bottom, separated by white line). Direction checking dramatically reshapes method profiles: naive cross-correlation drops from near-100\% (undirected) to regime-dependent rates with persistent 75\% null-control FPR. Permutation Granger achieves FPR${=}$0\% in the blind zone (green dashed box) and detects only at $\alpha{\geq}0.50$. The onset boundary ($\alpha{\approx}0.45$--$0.50$) is where method divergence is sharpest (Pitfall~3). \emph{Note: figure will be regenerated with D120 canonical data including corrected TY rates (\S\ref{sec:ty_limitation}).}}
110	\label{fig:consensus_heatmap}
111	\end{figure}
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{Forward-direction FDR significance rates (\%) for five lead-lag methods across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Direction checking reshapes method profiles: naive cross-correlation drops from near-100\% (undirected) to regime-dependent rates (75\% at the null, 12.5\% at $\alpha{=}0.25$, rising to 87.5\% at $\alpha{=}0.75$). Each cell reports the fraction of 8 validated canary$\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$) in the forward direction. $^\dagger$Moderate supplementary method (\S\ref{sec:ty_limitation}); FPR$_\text{null}$ pending (null condition not yet run through corrected pipeline). $^a$Seed-42 null-control rate under D105 $3\sigma$ calibration pending; 3-seed range 12.5--37.5\%.}
117	\label{tab:method_comparison}
118	\begin{tabular}{lcccccc}
119	\toprule
120	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
121	\midrule
122	Naive XCorr     & 75    & 12.5 & 37.5 & 87.5  & 0     & 75   \\
123	Diff.\ XCorr    & 0     & 37.5 & 87.5 & 75    & 75    & 0    \\
124	Threshold ($3\sigma$)$^a$ & ---   & 0    & 50   & 0     & 0     & ---  \\
125	Perm.\ Granger  & 0     & 0    & 75   & 75    & 75    & 0    \\
126	Toda--Yamamoto$^\dagger$  & ---   & 0    & 37.5 & 37.5  & 50    & ---  \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	
132	\subsection{Regime-Dependent Detectability}
133	\label{sec:regime}
134	
135	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
136	We present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.
137	
138	\paragraph{Raw drift.}
139	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
140	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets).
141	A single-seed observation at $\alpha{=}0.10$ reveals a steep diversity cliff: distinct-1 drops by 39.6\%, nearly matching the 3-seed mean at $\alpha{=}0.25$ ($-40.3{\pm}0.3\%$); distinct-2 shows a comparable jump ($-56.4\%$ vs.\ $-56.4{\pm}0.7\%$ at $\alpha{=}0.25$).
142	Token entropy at $\alpha{=}0.10$, however, differs from the null by less than 1 percentage point ($-5.3\%$ vs.\ $-4.6{\pm}0.4\%$), constituting a canary blind spot in which diversity has already collapsed but no canary metric responds.
143	At higher contamination, distinct-1 decline continues: $-37.1{\pm}0.4\%$ ($\alpha{=}0.50$), $-32.3{\pm}0.5\%$ ($\alpha{=}0.75$), and $-27.8{\pm}1.6\%$ ($\alpha{=}1.0$).
144	The non-monotonic pattern (diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$) is confirmed by 3-seed replication at $\alpha{=}0.25$ (std${=}0.3\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=\linewidth]{figures/fig_dose_response.pdf}
149	\caption{Dose-response profile of permutation Granger forward detection rate (Pythia-410M, fp32, 12 contamination levels, direction-checked).
150	Four regimes emerge: blind ($\alpha{\leq}0.45$, 0/8), onset ($\alpha{=}0.50$, 75\%), synchronous dip ($\alpha{=}0.60$, 37.5\%; orange diamond), and detection ($\alpha{\geq}0.75$, 62.5--75\%).
151	The $\alpha{=}0.60$ dip is dual-seed confirmed (s42: 3/8, s43: 0/8).
152	Per-method comparison is in Figure~\ref{fig:consensus_heatmap}.}
153	\label{fig:regime_map}
154	\end{figure}
155	
156	\paragraph{Granger-precedence detectability.}
157	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
158	Permutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$ (including $\alpha{=}0.25$ where a faint single-pair signal appears at FDR $p{=}0.053$ but aggregate detection remains null, and $\alpha{=}0.35$/$0.40$/$0.45$ which confirm PermG fwd${=}$0/8), \textbf{6/8} at $\alpha{=}0.50$ (2~fp32 seeds, consistent), \textbf{3/8} and \textbf{0/8} at $\alpha{=}0.60$ (s42 and s43 respectively; dual-seed confirmed non-monotonic dip), and \textbf{6/8} at $\alpha{=}1.0$.
159	At $\alpha{=}0.75$ (3~seeds), permutation Granger finds 20/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.
160	Under Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.
161	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
162	Permutation Granger forward significance is the primary detection indicator (Figure~\ref{fig:regime_map}): it reaches 6/8 at $\alpha{=}0.50$, dips to 3/8 at $\alpha{=}0.60$ (synchronous collapse zone; see below), and recovers to 5--6/8 at $\alpha{\geq}0.75$.
163	The onset boundary lies at $\alpha{\approx}0.45$--$0.50$: finer-grained probing at $\alpha{=}0.35$, $0.40$, and $0.45$ yields PermG fwd${=}$0/8 at all three levels, extending the blind spot through $\alpha{=}0.45$.
164	A faint signal first appears at $\alpha{=}0.25$ (best-pair FDR $p{=}0.053$) but does not translate to aggregate detection; reliable detection begins at $\alpha{=}0.50$ (6/8, 2~seeds).
165	This steep onset is consistent with theoretical expectations about signal-to-noise limits in short time series~\cite{boettiger2012limits}.
166	PermG $p$-values at $\alpha{=}0.45$ reveal sub-threshold signal: the minimum FDR-corrected $p$ reaches 0.059 (seed~43, 18\% above the $q{=}0.05$ threshold) and 0.091 (seed~42; Appendix~\ref{app:robustness}).
167	This gradient is consistent with the power-threshold interpretation of $\alpha_c$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
168	Sensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\ref{app:robustness}).
169	Cross-architecture validation on GPT-2-medium confirms this boundary: at $\alpha{=}0.25$, at most 1/8 pairs reach $K{\geq}3$ ($3\sigma$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\%$ vs.\ Pythia $-4.7{\pm}0.5\%$), while at $\alpha{=}1.0$ all 6 canary$\to$diversity pairs reach significance (\S\ref{sec:discussion}).
170	Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
171	At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
172	
173	\begin{table}[t]
174	\centering
175	\small
176	\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods (or $K{\geq}3$ of 4 effective methods; \S\ref{sec:threshold_limitation}); Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.45$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
177	\label{tab:cross_arch_regime}
178	\begin{tabular}{llcccccc}
179	\toprule
180	$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
181	\midrule
182	0.25 & Pythia-410M  & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & 0/8 & 0/8 \\
183	0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\
184	\midrule
185	1.00 & Pythia-410M  & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & 6/8 & 6/8 \\
186	1.00 & GPT-2-medium & \multicolumn{6}{c}{(reported in \S\ref{sec:discussion}; 6/8 canary$\to$downstream pairs at Tier~3)} \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\paragraph{Detectability at $\alpha{=}0.50$ and the transition zone.}
192	Under fp32 precision, $\alpha{=}0.50$ is reliably detected: permutation Granger finds 6/8 pairs FDR-significant across both seeds (Table~\ref{tab:method_comparison}).
193	The transition from sub-threshold to reliably detectable occurs between $\alpha{=}0.45$ and $\alpha{=}0.50$: finer-grained probing confirms PermG fwd${=}$0/8 at $\alpha{=}0.35$, $0.40$, and $0.45$, while $\alpha{=}0.50$ achieves 6/8 (2~seeds).
194	A faint single-pair signal first appears at $\alpha{=}0.25$ (entropy$\to$distinct-1: raw $p{=}0.007$, FDR-corrected $p{=}0.053$), but all aggregate indicators remain null through $\alpha{=}0.45$, placing the onset boundary at $\alpha{\approx}0.45$--$0.50$.
195	At $\alpha{=}0.50$, canary sensitivity remains metric-dependent: ECE achieves significance in both fp32 seeds, while token entropy remains below the FDR threshold ($p_{\text{fdr}}{\geq}0.086$), identifying ECE as the more sensitive canary near the onset boundary.
196	Figure~\ref{fig:consensus_heatmap} visualizes the method$\times\alpha$ interaction, revealing a block structure that separates correlation-based methods from causal methods as a function of regime.
197	
198	\paragraph{Quantifying the onset boundary.}
199	Sigmoid regression across the 12-point $\alpha$ grid quantifies the sharp onset observed above.
200	Fitting $P(\alpha) = 1/(1 + \exp(-k(\alpha - \alpha_c)))$ to the PermG forward detection rate yields a critical threshold $\alpha_c = 0.476$ with steepness $k \geq 200$ and transition width $\Delta\alpha \approx 0.02$ (Figure~\ref{fig:phase_transition}).
201	The sigmoid model explains 96.9\% of variance ($R^2 = 0.969$), substantially outperforming a power-law alternative ($R^2 = 0.808$; $\Delta\text{AIC} = 18.2$), confirming that the onset is steep rather than gradual.
202	This transition is striking because effective contamination barely changes across the boundary: after 10 generations of iterative training, both $\alpha{=}0.45$ and $\alpha{=}0.50$ drive the cumulative synthetic fraction above 99\% ($C = 1{-}(1{-}\alpha)^{10}$: $99.75\%$ vs.\ $99.90\%$)---a difference of 0.15 percentage points---yet causal detectability jumps from 0/8 to 6/8.
203	We term this a \emph{detection phase transition}: causal coupling emerges abruptly at a critical contamination threshold ($\alpha_c{=}0.476$, $\Delta\alpha{\approx}0.02$) rather than scaling smoothly with contamination dose.
204	Within the $S \times R$ framework (\S\ref{sec:theory}), $\alpha_c{=}0.476$ localizes the point at which signal strength $S(\alpha)$ first crosses the detection floor, while the high steepness ($k \geq 200$) indicates that temporal resolution $R(\alpha)$ remains large at onset---the entropy--diversity lag has not yet begun to compress.
205	Cross-architecture comparison reveals no monotonic relationship between model scale and onset sensitivity (Qwen-0.8B $\approx$ Pythia-6.9B $>$ Pythia-410M $>$ Pythia-1.4B $>$ SmolLM3-3B), suggesting that architecture and pre-training data exert stronger influence than parameter count on detection onset.
206	
207	\begin{figure}[t]
208	\centering
209	% TODO: transfer fig_phase_transition.pdf from westd-17855
210	%\includegraphics[width=\linewidth]{figures/fig_phase_transition.pdf}
211	\caption{Sigmoid fit to the PermG forward detection rate across 12 contamination levels.
212	The fitted critical threshold $\alpha_c = 0.476$ with steepness $k \geq 200$ indicates a steep onset of causal detectability.
213	Sigmoid $R^2 = 0.969$ vs.\ power-law $R^2 = 0.808$ ($\Delta\text{AIC} = 18.2$).}
214	\label{fig:phase_transition}
215	\end{figure}
216	
217	\paragraph{Specification curve robustness.}
218	To verify that the detection phase transition is not an artifact of analytical choices, we conduct a specification curve analysis spanning 1{,}160 analytical specifications across 29 experimental conditions.
219	Specifications vary lag order, differencing strategy, significance threshold, FDR correction method, and permutation count.
220	PermG maintains a 0\% false-positive rate at the null ($\alpha{=}0.00$) across all 1{,}160 specifications, while naive cross-correlation reaches 100\% regardless of specification---confirming that the FPR separation between methods is robust to analytical degrees of freedom.
221	The phase transition itself is specification-invariant: PermG detection rate remains near zero below $\alpha{=}0.50$ (${\sim}0\%$), rises to 81.2\% at $\alpha{=}0.50$, and reaches 87.5\% at $\alpha{=}0.75$ across all specifications.
222	This demonstrates that the onset at $\alpha_c{\approx}0.50$ is a property of the data-generating process, not a consequence of researcher degrees of freedom in method configuration.
223	
224	\paragraph{Non-monotonic dose-response: the synchronous collapse zone.}
225	Dual-seed replication at $\alpha{=}0.60$ reveals a non-monotonic dose-response in Granger detectability: PermG fwd drops to 3/8 (s42) and 0/8 (s43), below both $\alpha{=}0.50$ (6/8, 2~seeds) and $\alpha{=}0.75$ (5--6/8 per seed, 3~seeds).
226	This creates a four-regime structure in the dose-response profile: \emph{blind} ($\alpha{\leq}0.45$, 0/8), \emph{onset} ($\alpha{\approx}0.50$, 6/8), \emph{synchronous dip} ($\alpha{\approx}0.60$, 0--3/8), and \emph{detection} ($\alpha{\geq}0.75$, 5--6/8 per seed; 6/8 at $\alpha{=}1.0$).
227	The dip confirms the non-monotonic prediction of the $S \times R$ framework (\S\ref{sec:theory}): at $\alpha{=}0.60$, signal strength $S$ continues rising but temporal resolution $R$ drops sharply due to relaxation time matching, producing a local minimum in detectability.
228	The synchronous zone is mechanistically distinct from the blind spot: in the blind spot, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.
229	Toda--Yamamoto achieves moderate detection across this range (3--4/8 at $\alpha{\geq}0.50$; \S\ref{sec:ty_limitation}), with its detection at $\alpha{=}0.60$ suggesting partial inter-method complementarity in the synchronous collapse zone where PermG drops to 0--3/8.
230	This non-monotonicity also implies that simple threshold-based triggers (such as the 15\% entropy criterion in \S\ref{sec:intervention}) may outperform formal Granger tests at intermediate contamination levels.
231	
232	\paragraph{Predictions for longer generation chains.}
233	The statistical power interpretation (\S\ref{sec:theory}) generates three testable predictions for $T{=}20$.
234	Since $\mathrm{Power}(\alpha, T) = \Phi\bigl(S(\alpha) \cdot R(\alpha) \cdot \sqrt{T} \,/\, \sigma_{\mathrm{noise}}\bigr)$, increasing $T$ raises power at every $\alpha$:
235	(i)~$\alpha_c$ should \emph{left-shift}---the detection threshold decreases because $\sqrt{20}/\sqrt{10} \approx 1.41$ multiplies the power argument uniformly, so contamination levels currently below threshold (e.g., $\alpha{=}0.45$, where $T{=}10$ yields PermG 0/8 with sub-threshold $p$-values of 0.059--0.091) may cross into detectability;
236	(ii)~the transition should \emph{smooth}---the $\sqrt{T}$ scaling broadens the power curve across $\alpha$, making the onset less step-like (the synchronous dip at $\alpha{=}0.60$ should also attenuate as finer temporal sampling resolves sub-generation lags);
237	(iii)~different methods should exhibit \emph{different} $\alpha_c$ values, since each method has its own power curve---empirical validation of this prediction awaits $T{=}20$ replication.
238	These predictions are currently under empirical verification with extended ($T{=}20$) generation protocols.
239	
240	
241	\subsection{Case Study: Canary Prediction of Diversity Collapse}
242	\label{sec:case_study}
243	
244	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
245	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
246	
247	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
248	Token entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \S\ref{sec:discussion}).
249	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.
250	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
251	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
252	Reverse-direction tests (downstream$\to$canary) on WikiText-103 find \textbf{0/24} FDR-significant (all $p{>}0.49$), establishing directional asymmetry in this domain.\footnote{C4 exhibits domain-dependent directionality: at $\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling (\S\ref{sec:discussion}).}
253	
254	\begin{figure}[t]
255	\centering
256	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
257	\caption{Metric trajectories across 10 generations at $\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}
258	\label{fig:metric_trajectory}
259	\end{figure}
260	
261	\paragraph{High contamination ($\alpha{=}0.75$, 3 seeds).}
262	Directional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 20/24 forward pairs FDR-significant, 0/24 reverse).
263	However, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\alpha{=}0.75$ squarely in the transitional detection regime.
264	Differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\S\ref{sec:pitfalls}).
265	
266	\paragraph{ECE as a conditional secondary canary.}
267	ECE's forward consensus matches token entropy (both achieve PermG\_fwd 6/8 across all conditions), but the reverse profile diverges sharply.
268	Across 7 validated conditions at $\alpha{=}1.0$ (3 architectures $\times$ 2 scales $\times$ 2 domains), token entropy reverse direction yields \textbf{0/28} FDR-significant pairs (consistent with unidirectional forward causation at full synthetic replacement; domain-dependent bidirectionality emerges at lower $\alpha$, \S\ref{sec:discussion}), while ECE reverse direction yields \textbf{13/28} significant pairs, with 5/7 conditions containing at least one reverse-significant pair, all in the distinct$\to$ECE direction.
269	This bidirectional coupling is the core reason ECE is classified as a secondary canary: ECE and diversity exhibit mutual feedback, and the interpretability of ECE's causal direction is correspondingly limited.
270	This result also instantiates Claim~3 (method sensitivity): when only forward significance is considered, the two canary types appear equivalent; incorporating reverse-direction tests separates them. The choice of analysis dimension alters the canary classification itself.
271	
272	\paragraph{Failed canary candidates.}
273	Not all metrics serve as canaries.
274	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
275	Effective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\alpha{=}0.25$ it \emph{increases} from 2.37 to 8.48 (+258\%).
276	The GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.
277	This opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\S\ref{sec:discussion}).
278	
279	\paragraph{Consensus filtering.}
280	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline (PermG fwd ${\geq}6/8$, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
281	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
282	The consensus framework reduces the naive 75\% forward-direction FPR to 0\%, matching the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
283	
284	
285	\subsection{Consensus Framework Validation}
286	\label{sec:consensus_validation}
287	
288	We validate the consensus framework's calibration using built-in experimental controls.
289	
290	\paragraph{False positive rate.}
291	At $\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.
292	Individual-method forward-direction FPR ranges from \textbf{75\%} (naive cross-correlation: 6/8) through 37.5\% (threshold) down to \textbf{0\%} (permutation Granger and differenced cross-correlation); Toda--Yamamoto's null-control FPR has not yet been evaluated through the corrected pipeline (\S\ref{sec:ty_limitation}).
293	The multi-method consensus at $K{\geq}3$ ($3\sigma$) achieves \textbf{FPR${=}$0\%} (0/24 pairs, three independent seeds), matching the best individual method (permutation Granger) while providing a formal benchmark for method reliability (Table~\ref{tab:fpr_fnr}).
294	
295	\paragraph{False negative rate.}
296	At $\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\geq}3\times$ the $\alpha{=}0.0$ baseline (entropy $11.93\times$, ECE $73.12\times$) and canary onset strictly preceding downstream onset by ${\geq}1$ generation (\S\ref{sec:calibration}).
297	FNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\geq}3/4$, $S{\geq}3/4$, all~6 are recovered (\textbf{FNR${=}$0\%}).
298	Toda--Yamamoto's individual FNR is 50\% (4/8 detected at $\alpha{=}1.0$, seed~42), consistent with its moderate supplementary classification (\S\ref{sec:ty_limitation}).
299	Both FPR and FNR are validated on the joint method${\times}$seed dimension (FPR: 3~seeds at $\alpha{=}0.0$; FNR: 4~seeds at $\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\geq}3$).
300	Table~\ref{tab:fpr_fnr} reports the calibration results.
301	Table~\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\alpha$ including the null control, while permutation Granger achieves correct verdicts at all levels with zero FPR.
302	
303	\begin{table}[t]
304	\centering
305	\caption{Single-method inference errors across contamination levels.
306	Each cell shows the verdict (significant or not) based on multi-seed majority ($\geq$2/3 seeds with $\geq$4/8 pairs significant).
307	\checkmark\ = correct, \textcolor{red}{FP} = false positive, \textcolor{blue}{FN} = false negative, $\circ$ = ambiguous ground truth (either verdict plausible).
308	Naive XCorr produces false positives at \emph{every} $\alpha$ including the null control. Permutation Granger achieves correct verdicts at all levels with zero FPR. $^\dagger$Rows marked pending have cross-script inconsistencies under audit.}
309	\label{tab:single-method-errors}
310	\resizebox{\columnwidth}{!}{%
311	\begin{tabular}{lccccc}
312	\toprule
313	 & \multicolumn{2}{c}{\textit{No signal}} & \textit{Ambiguous} & \multicolumn{2}{c}{\textit{Causal signal}} \\
314	\cmidrule(lr){2-3} \cmidrule(lr){4-4} \cmidrule(lr){5-6}
315	Method & $\alpha{=}0.00$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.00$ \\
316	\midrule
317	Naive XCorr
318	  & \textcolor{red}{FP}{\scriptsize\ 8,7,8}
319	  & \textcolor{red}{FP}{\scriptsize\ 8,8}
320	  & $\circ${\scriptsize\ 8,8,8}
321	  & \checkmark{\scriptsize\ 8,8,8}
322	  & \checkmark{\scriptsize\ 8,8,8} \\
323	Diff XCorr (FDR)$^\dagger$
324	  & --- & --- & --- & --- & --- \\
325	Threshold Onset$^\dagger$
326	  & --- & --- & --- & --- & --- \\
327	Perm Granger (FDR)
328	  & \checkmark{\scriptsize\ 0,0,0}
329	  & \checkmark{\scriptsize\ 0,0}
330	  & $\circ${\scriptsize\ 0,6,3}
331	  & \checkmark{\scriptsize\ 8,5,6}
332	  & \checkmark{\scriptsize\ 6,6,6} \\
333	TY Granger$^\dagger$
334	  & --- & --- & --- & --- & --- \\
335	\midrule
336	\textbf{Consensus ($K{\geq}3$)}$^\dagger$
337	  & --- & --- & --- & --- & --- \\
338	\bottomrule
339	\multicolumn{6}{l}{\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\
340	\multicolumn{6}{l}{\footnotesize Seeds: $\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\alpha{=}0.25$: 43, 44; $\alpha{=}1.00$: 42, 43, 45.} \\
341	\end{tabular}%
342	}
343	\end{table}
344	
345	\paragraph{Bootstrap power analysis.}
346	To quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\alpha{=}1.0$).
347	Permutation Granger achieves power${=}1.0$ on genuine pairs (canary$\to$diversity) and power${=}0.0$ on spurious pairs (canary$\to$perplexity), providing clean separation.
348	Toda--Yamamoto achieves power${=}0.50$ on genuine pairs (4/8 detected at $\alpha{=}1.0$), consistent with its moderate supplementary classification (\S\ref{sec:ty_limitation}).
349	We note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\beta{=}0.3$).
350	
351	\begin{table}[t]
352	\centering
353	\small
354	\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\geq}3$ ($3\sigma$, excluding threshold onset; \S\ref{sec:threshold_limitation}) achieves FPR${=}$0\% and FNR${=}$0\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration of any single method. FPR: $\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds). $^\dagger$Moderate supplementary method (\S\ref{sec:ty_limitation}); FPR pending (null condition not yet run through corrected pipeline); FNR from single-seed $\alpha{=}1.0$ (4/8 detected).}
355	\label{tab:fpr_fnr}
356	\begin{tabular}{lcc}
357	\toprule
358	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
359	\midrule
360	Naive XCorr              & 100\%              & 0\%  \\
361	Differenced XCorr        & 37.5\%             & 0\%  \\
362	Threshold Onset          & 20.8\% (12.5--37.5) & 0\%  \\
363	Permutation Granger      & 0\%                & 0\%  \\
364	Toda--Yamamoto$^\dagger$  & ---                & 50\%   \\
365	\midrule
366	Consensus ($K{\geq}3$, $3\sigma$)      & 0\%    & 0\%  \\
367	Consensus ($K{\geq}3$, $S{\geq}3/4$)   & 0\%    & 0\%  \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	
373	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
374	\label{sec:generalization}
375	
376	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
377	To test whether these findings transfer, we evaluate the lead-lag pattern along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
378	All conditions use $\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.
379	
380	\begin{table}[t]
381	\centering
382	\small
383	\caption{Cross-architecture lead-lag detectability ($\alpha{=}1.0$, D105 unified pipeline, $3\sigma$ calibration, M035 direction-corrected).
384	PermG~fwd: permutation Granger forward-direction FDR-significant pairs (out of 8).
385	$K{\geq}3$: pairs where ${\geq}3$ of 5 methods reach FDR significance (direction-checked, $3\sigma$).
386	PermG~fwd ${\geq}6/8$ in 13/15 confirmed conditions; $K{\geq}3$ ${\geq}6/8$ in 10/14 with known consensus (Padding-410M and Pythia-1.4B C4 pending audit).
387	Exceptions: Pythia-1.4B (s42: 1/8$^\dagger$, s43: 3/8) and SmolLM3-3B (3/8$^\ddagger$).
388	Rows marked ``---'' are running experiments; final values will be filled without format changes.}
389	\label{tab:generalization}
390	\begin{tabular}{lrclcc}
391	\toprule
392	Model & Params & Seed & Domain & PermG (fwd) & $K{\geq}3$ \\
393	\midrule
394	\multicolumn{6}{l}{\emph{Baseline}} \\
395	Pythia-410M       & 410M & s42 & Wiki & 6/8            & 6/8            \\
396	Pythia-410M       & 410M & s43 & Wiki & 6/8            & 6/8            \\
397	\addlinespace
398	\multicolumn{6}{l}{\emph{Scale}} \\
399	Pythia-1.4B       & 1.4B & s42 & Wiki & \textbf{2/8}$^\dagger$ & \textbf{1/8}$^\dagger$  \\
400	Pythia-1.4B       & 1.4B & s43 & Wiki & 6/8            & 3/8     \\
401	Pythia-6.9B       & 6.9B & s42 & Wiki & 7/8$^*$        & 6/8            \\
402	Pythia-6.9B       & 6.9B & s43 & Wiki & ---            & ---            \\
403	\addlinespace
404	\multicolumn{6}{l}{\emph{Architecture}} \\
405	GPT-2-medium      & 345M & s42 & Wiki & 6/8            & 6/8            \\
406	GPT-2-medium      & 345M & s43 & Wiki & 6/8            & 6/8            \\
407	OPT-1.3B          & 1.3B & s42 & Wiki & 6/8            & 6/8            \\
408	OPT-1.3B          & 1.3B & s43 & Wiki & 6/8            & 6/8            \\
409	Qwen3.5-0.8B      & 0.8B & s42 & Wiki & 8/8            & 6/8            \\
410	Qwen3.5-0.8B      & 0.8B & s43 & Wiki & ---            & ---            \\
411	SmolLM3-3B        & 3.0B & s42 & Wiki & \textbf{3/8}$^\ddagger$ & \textbf{3/8}$^\ddagger$ \\
412	SmolLM3-3B        & 3.0B & s43 & Wiki & ---            & ---            \\
413	\addlinespace
414	\multicolumn{6}{l}{\emph{Tokenization}} \\
415	Padding-410M      & 410M & s42 & Wiki & 6/8            & 6/8$^{\S}$     \\
416	\addlinespace
417	\multicolumn{6}{l}{\emph{Domain}} \\
418	Pythia-1B         & 1.0B & s42 & C4   & 8/8            & 7/8            \\
419	Pythia-1B         & 1.0B & s43 & C4   & 7/8            & 6/8            \\
420	Pythia-1.4B       & 1.4B & s42 & C4   & 8/8            & ---            \\
421	\bottomrule
422	\multicolumn{6}{l}{\footnotesize $^\dagger$Seed-sensitive: PermG s42 2/8, s43 6/8; $K{\geq}3$ s42 1/8, s43 3/8. Likely stochastic instability at this scale (\S\ref{sec:discussion}).} \\
423	\multicolumn{6}{l}{\footnotesize $^\ddagger$Canary metric splitting: only ECE$\to$downstream pairs detected (3/4); entropy$\to$downstream 0/4 (\S\ref{sec:smollm3}).} \\
424	\multicolumn{6}{l}{\footnotesize $^*$bf16 precision (model exceeds single-GPU fp32 capacity).} \\
425	\multicolumn{6}{l}{\footnotesize $^{\S}$Padding-410M $K{\geq}3$ pending supplementary audit (expected stable at 6/8).} \\
426	\multicolumn{6}{l}{\footnotesize Full method-level breakdown ($K{\geq}4$) in Appendix~\ref{app:cross_arch}.} \\
427	\end{tabular}
428	\end{table}
429	
430	\paragraph{Cross-condition robustness.}
431	Table~\ref{tab:generalization} confirms that the entropy-leads-diversity pattern is robust across 15 confirmed conditions (3 pending) spanning six model families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B, and two training domains (WikiText-103, C4).
432	Permutation Granger forward significance reaches ${\geq}6/8$ in 13 of 15 conditions (86.7\%), with two exceptions: Pythia-1.4B seed~42 (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs are detected (see below).
433	$K{\geq}3$ multi-method consensus reaches ${\geq}6/8$ in 10 of 14 conditions with known consensus (Padding-410M and Pythia-1.4B C4 pending audit), with exceptions Pythia-1.4B (s42: 1/8, s43: 3/8) and SmolLM3-3B (3/8).
434	The concordance between PermG and $K{\geq}3$ confirms that multi-method consensus is robust across architectures.
435	The onset threshold $\alpha_c{\approx}0.50$ is robust across all six families: every architecture that achieves detection does so at or above $\alpha{=}0.50$, while none achieves reliable detection below this threshold, suggesting that the detection phase transition boundary is architecture-independent even though detection power above onset varies with model family.
436	With threshold onset power-limited and Toda--Yamamoto providing moderate supplementary signal (3--4/8 at $\alpha{\geq}0.50$; \S\ref{sec:ty_limitation}), $K{\geq}3$ draws on four contributing methods---a stronger standard than simple majority (\S\ref{sec:consensus}).
437	
438	\paragraph{Scale generalization.}
439	Scaling from 410M to 6.9B parameters confirms that the lead-lag pattern persists across a $17\times$ parameter range.
440	Pythia-6.9B achieves PermG fwd~7/8 (bf16), the strongest single-seed detection.
441	Within the Pythia family, 1.4B shows seed dependence: s42 yields only 2/8 (the sole outlier across all conditions), while s43 recovers to 6/8.
442	Qwen3.5-0.8B (PermG~fwd~8/8) extends the finding beyond the Pythia/GPT-2/OPT decoder-only family to an independently trained architecture with a different tokenizer.
443	
444	\paragraph{Domain generalization.}
445	Replacing WikiText-103 with C4 yields the strongest forward detection: Pythia-1B achieves PermG~fwd~8/8 in both seeds at $\alpha{=}1.0$, confirming that the lead-lag pattern is not an artifact of narrow topical distribution.
446	The domain effect is scale-dependent: Pythia-1.4B achieves PermG~fwd~8/8 on C4 ($\alpha{=}1.0$), compared with 2/8 on WikiText at the same scale, recovering to 7/8 at Pythia-6.9B---suggesting that dataset characteristics modulate detection power independently of model capacity.
447	However, directional asymmetry does not transfer fully across domains.
448	At $\alpha{=}0.50$ (Pythia-410M, C4, s42 fp32), PermG reverse reaches 7/8 (compared to 0/8 in all WikiText conditions), indicating near-symmetric bidirectional coupling between canary and downstream metrics.
449	This domain-dependent directionality suggests that the unidirectional forward causation observed in WikiText may partly reflect domain-specific dynamics rather than a universal property of collapse; implications are discussed in \S\ref{sec:discussion}.
450	
451	\paragraph{Canary metric sensitivity: the SmolLM3-3B case.}
452	\label{sec:smollm3}
453	SmolLM3-3B (PermG fwd 3/8) reveals that canary metric choice is itself a dimension of method sensitivity.
454	Decomposing by canary type: ECE$\to$downstream achieves 3/4 significant pairs, while token entropy$\to$downstream achieves 0/4.
455	The root cause is that SmolLM3's token entropy exhibits non-monotonic oscillations across generations, violating the monotonic decline pattern that Granger tests exploit; ECE, by contrast, maintains its monotonic upward trajectory.
456	Multi-method consensus confirms the severity: entropy pairs activate only via naive and differenced cross-correlation (per-pair $K{=}2$), ECE pairs activate only via differenced cross-correlation and permutation Granger (per-pair $K{=}2$), and no pair exceeds two-method agreement---illustrating that even within a single architecture, the method panel fragments along canary metric boundaries.
457	This architecture-dependent canary sensitivity complements the finding that effective rank direction is model-dependent (\S\ref{sec:case_study}): no single canary metric is universally optimal across all architectures, enriching Claim~3 by adding canary metric selection as a further source of analytic variability.
458	
459	\subsection{Canary-Based Early Intervention}
460	\label{sec:intervention}
461	
462	To test whether the lead-lag relationship translates into practical utility, we implement a predictive cessation protocol: training with synthetic data ($\alpha{=}1.0$) continues until token entropy drops ${>}15\%$ relative to generation~0, at which point $\alpha$ is switched to $0.0$ (pure real data).
463	We compare against a reactive baseline that triggers only when distinct-1 drops ${>}10\%$---a downstream metric that, by the lead-lag hypothesis, should respond later.
464	
465	\paragraph{Pythia-410M.}
466	The predictive trigger fires at generation~1 in both seed-precision pairs tested (s42 fp32: entropy $3.234{\to}1.918$, ${\downarrow}40.7\%$; s43 bf16: $3.257{\to}2.523$, ${\downarrow}22.5\%$).
467	The reactive baseline triggers one generation later (generation~2, distinct-1 ${\downarrow}15.6\%$).
468	Predictive intervention reduces peak perplexity by 63\% relative to reactive ($56.99$ vs.\ $157.09$, s42 fp32) and achieves full recovery by generation~2 versus generation~4 for reactive.
469	The bf16 pair shows a milder perturbation (peak perplexity $24.65$ vs.\ $56.99$) consistent with stochastic rounding regularization, but the structural pattern---generation~1 trigger, generation~2 recovery---is identical.
470	Both conditions converge to the $\alpha{=}0.0$ baseline by generation~10.
471	
472	\paragraph{Cross-scale validation: Pythia-1.4B.}
473	Pythia-1.4B (s42 fp32) replicates the 410M pattern: token entropy drops $51.9\%$ at generation~1 ($2.946{\to}1.418$), exceeding the 15\% threshold, and recovers to $2.892$ by generation~2 ($98.2\%$ of baseline).
474	Perplexity spikes from $19.68$ to $65.37$ at the trigger generation and recovers to $17.44$ by generation~2 (stable at $17.60$ through generation~10).
475	The trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\times$ scale gap (410M to 1.4B), confirming that the canary-based intervention mechanism is scale-independent: the 15\% entropy threshold generalizes without recalibration across model sizes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "646dd7f8-1eb1-4c04-9c36-3dbe13b0a86a",
  "isSidechain": false,
  "promptId": "694508ff-a291-43df-9e7f-4abfbbd1deda",
  "type": "user",
  "uuid": "b774285f-8c58-406d-a14b-3aa5dda46ccb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\nPythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\S\\ref{sec:method_sensitivity}, \\S\\ref{sec:regime}, and \\S\\ref{sec:discussion}.\nTraining data is drawn from WikiText-103 \\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\n\nOur protocol follows the replace paradigm of \\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\alpha{<}1.0$.\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$.\nThe $\\alpha{=}1.0$ condition uses four random seeds $\\{42, 43, 44, 45\\}$; $\\alpha \\in \\{0.00, 0.25, 0.50, 0.75\\}$ each use three seeds $\\{42, 43, 44\\}$; $\\alpha{=}0.10$ uses a single seed (42, preliminary).\n\nWe track two \\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\cite{scheffer2009early}) and three \\emph{downstream metrics}.\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\nToken entropy is the mean next-token prediction entropy $H(p_\\theta | \\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\S\\ref{sec:case_study}).\nResults for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\nCode and data will be released upon publication.\n\nAll hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}.\nCross-correlation analysis uses a maximum lag of 5 generations.\nTable~\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $^\\dagger$$\\alpha{=}0.10$: single seed (seed~42, preliminary). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.10$^\\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Method Sensitivity Analysis}\n\\label{sec:method_sensitivity}\n\nWe open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.\nIf different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.\n\n\\paragraph{Five-method ablation.}\nWe apply five lead-lag detection methods to the $\\alpha{=}1.0$ condition (4~seeds, 16 canary$\\to$downstream pairs).\nThe fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{5/16} (31.3\\%; moderate supplementary, \\S\\ref{sec:ty_limitation}).\nMethod choice alone swings significance from \\textbf{100\\% to 37.5\\%} among the primary methods: 50--57\\% of pairs classified as significant under one method flip to non-significant under another.\nThe spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is at least \\textbf{62.5\\%} across the primary methods.\nTable~\\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.\n\n\\paragraph{First-differencing diagnostic.}\nA single preprocessing decision can eliminate an entire analysis channel.\nFor canary$\\to$diversity pairs at $\\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.\nFor canary$\\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \\textbf{zero} significant pairs ($F{\\approx}0$, $p{=}0.99$; Figure~\\ref{fig:differencing_dmax}a).\nThe apparent canary$\\to$perplexity relationship is entirely an artifact of co-trending.\nNotably, at $\\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.\n\n\\paragraph{Augmentation order sensitivity.}\nToda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nAfter correcting the statsmodels API incompatibility (\\S\\ref{sec:ty_limitation}), TY achieves moderate detection (3--4/8 at $\\alpha{\\geq}0.50$) at the default $d_{\\max}{=}1$; however, the qualitative finding that this single hyperparameter can swing conclusions between near-universal significance and near-universal non-significance remains, consistent with known properties of the Toda--Yamamoto procedure~\\cite{toda1995statistical}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/differencing_dmax.pdf}\n\\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\\alpha{=}1.0$, 4~seeds). \\textbf{(a)}~First-differencing eliminates the canary$\\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\\to$diversity pairs retain significance after differencing (24/24$\\to$24/24). \\textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\\max}$; after correcting the implementation (\\S\\ref{sec:ty_limitation}), TY achieves moderate detection at the default $d_{\\max}{=}1$, but the qualitative sensitivity to this hyperparameter persists.}\n\\label{fig:differencing_dmax}\n\\end{figure}\n\n\\paragraph{Inter-method agreement.}\nCohen's $\\kappa$, averaged over all method pairs, is \\textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\\alpha{=}0.0$ through $\\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.\nCross-architecture validation on GPT-2-medium (12 canary$\\to$downstream pairs) yields Fleiss' $\\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.\nRestricting to three informative methods (excluding naive cross-correlation, which anchors the permissive extreme, and Toda--Yamamoto, which provides moderate supplementary signal) raises $\\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.\nTable~\\ref{tab:method_comparison} extends the analysis across contamination levels.\nDirection checking (D111) itself constitutes a sensitivity dimension beyond the five statistical methods: restricting to forward-direction associations inverts naive cross-correlation's profile from uniformly high (${\\approx}100\\%$ undirected) to regime-dependent, revealing that much of its apparent signal was reverse-directional.\nAt $\\alpha{=}0.0$ (null control), naive cross-correlation still finds \\textbf{75\\%} (6/8) of forward-direction pairs significant---lower than the undirected 100\\%, but still a substantial FPR.\nPermutation Granger correctly finds 0\\%, achieving perfect null-control specificity.\nAt $\\alpha{=}0.50$ (fp32), permutation Granger finds 75\\% (6/8), while naive finds 37.5\\% (Figure~\\ref{fig:consensus_heatmap}; Table~\\ref{tab:method_comparison}).\n\n\\paragraph{Method$\\times$regime interaction.}\nTable~\\ref{tab:method_comparison} reveals that direction checking reshapes the method hierarchy across contamination levels.\nAt $\\alpha{=}0.25$, naive cross-correlation drops to 12.5\\% while permutation Granger remains at 0\\%, narrowing the gap visible in undirected analysis.\nAt $\\alpha{\\geq}0.75$, naive rises to 87.5\\% while permutation Granger reaches 75\\%; both methods detect, but naive's persistent 75\\% null-control FPR means its high-$\\alpha$ detections cannot be distinguished from false positives without the consensus framework.\nThis regime-dependent reversal, combined with the block structure visible in Figure~\\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \\S\\ref{sec:regime}.\n\n\\paragraph{Why permutation Granger succeeds.}\nThe systematic comparison identifies PermG as the only method combining zero null-control FPR with consistent detection across all regimes where signal exists ($\\alpha{\\geq}0.50$).\nThree properties explain this outcome.\nFirst, the nonparametric permutation procedure inherently controls FPR by constructing the null distribution from the observed data rather than from distributional assumptions, making it robust to the non-stationarity that inflates false positives in correlation-based methods.\nSecond, Granger tests are directional by construction: they test whether past values of $X$ improve prediction of $Y$ beyond $Y$'s own history, naturally filtering the reverse-directional associations that inflate naive cross-correlation's FPR.\nThird, PermG does not require threshold calibration or augmentation order selection, avoiding the hyperparameter sensitivity observed in Toda--Yamamoto (Figure~\\ref{fig:differencing_dmax}b; \\S\\ref{sec:ty_limitation}) and the power limitations that reduce threshold onset to near-zero detection under $3\\sigma$ calibration (\\S\\ref{sec:threshold_limitation}).\nBy contrast, differenced cross-correlation retains 100\\% FDR significance in both forward \\emph{and} reverse directions at $\\alpha{=}0.75$, failing to distinguish genuine directional precedence from shared dynamics; and Toda--Yamamoto, while achieving moderate detection (3--4/8 at $\\alpha{\\geq}0.50$), remains sensitive to the augmentation order $d_{\\max}$ (\\S\\ref{sec:ty_limitation}).\nThese complementary failures, exposed through the MMCT evaluation framework, converge on a single recommendation: for short iterative training series ($T{\\leq}20$), permutation Granger causality should be the primary detection method.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/consensus_heatmap.pdf}\n\\caption{Method$\\times$regime consensus heatmap (Pythia-410M, fp32, 12 contamination levels, direction-checked). Each cell shows the forward-direction detection rate (\\% of 8 pairs reaching FDR significance) for five individual methods (top) and two consensus thresholds (bottom, separated by white line). Direction checking dramatically reshapes method profiles: naive cross-correlation drops from near-100\\% (undirected) to regime-dependent rates with persistent 75\\% null-control FPR. Permutation Granger achieves FPR${=}$0\\% in the blind zone (green dashed box) and detects only at $\\alpha{\\geq}0.50$. The onset boundary ($\\alpha{\\approx}0.45$--$0.50$) is where method divergence is sharpest (Pitfall~3). \\emph{Note: figure will be regenerated with D120 canonical data including corrected TY rates (\\S\\ref{sec:ty_limitation}).}}\n\\label{fig:consensus_heatmap}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Forward-direction FDR significance rates (\\%) for five lead-lag methods across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Direction checking reshapes method profiles: naive cross-correlation drops from near-100\\% (undirected) to regime-dependent rates (75\\% at the null, 12.5\\% at $\\alpha{=}0.25$, rising to 87.5\\% at $\\alpha{=}0.75$). Each cell reports the fraction of 8 validated canary$\\to$downstream pairs reaching BH-corrected significance ($q{=}0.05$) in the forward direction. $^\\dagger$Moderate supplementary method (\\S\\ref{sec:ty_limitation}); FPR$_\\text{null}$ pending (null condition not yet run through corrected pipeline). $^a$Seed-42 null-control rate under D105 $3\\sigma$ calibration pending; 3-seed range 12.5--37.5\\%.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr     & 75    & 12.5 & 37.5 & 87.5  & 0     & 75   \\\\\nDiff.\\ XCorr    & 0     & 37.5 & 87.5 & 75    & 75    & 0    \\\\\nThreshold ($3\\sigma$)$^a$ & ---   & 0    & 50   & 0     & 0     & ---  \\\\\nPerm.\\ Granger  & 0     & 0    & 75   & 75    & 75    & 0    \\\\\nToda--Yamamoto$^\\dagger$  & ---   & 0    & 37.5 & 37.5  & 50    & ---  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Regime-Dependent Detectability}\n\\label{sec:regime}\n\nBeyond method choice, the contamination level~$\\alpha$ determines whether a temporal lead exists to detect.\nWe present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.\n\n\\paragraph{Raw drift.}\nTable~\\ref{tab:drift_summary} shows that diversity collapse occurs at \\emph{all} contamination levels, not only under full synthetic replacement.\nDistinct-1 declines by 13.8\\% even at $\\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets).\nA single-seed observation at $\\alpha{=}0.10$ reveals a steep diversity cliff: distinct-1 drops by 39.6\\%, nearly matching the 3-seed mean at $\\alpha{=}0.25$ ($-40.3{\\pm}0.3\\%$); distinct-2 shows a comparable jump ($-56.4\\%$ vs.\\ $-56.4{\\pm}0.7\\%$ at $\\alpha{=}0.25$).\nToken entropy at $\\alpha{=}0.10$, however, differs from the null by less than 1 percentage point ($-5.3\\%$ vs.\\ $-4.6{\\pm}0.4\\%$), constituting a canary blind spot in which diversity has already collapsed but no canary metric responds.\nAt higher contamination, distinct-1 decline continues: $-37.1{\\pm}0.4\\%$ ($\\alpha{=}0.50$), $-32.3{\\pm}0.5\\%$ ($\\alpha{=}0.75$), and $-27.8{\\pm}1.6\\%$ ($\\alpha{=}1.0$).\nThe non-monotonic pattern (diversity declining \\emph{more} at moderate~$\\alpha$ than at extreme~$\\alpha$) is confirmed by 3-seed replication at $\\alpha{=}0.25$ (std${=}0.3\\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response profile of permutation Granger forward detection rate (Pythia-410M, fp32, 12 contamination levels, direction-checked).\nFour regimes emerge: blind ($\\alpha{\\leq}0.45$, 0/8), onset ($\\alpha{=}0.50$, 75\\%), synchronous dip ($\\alpha{=}0.60$, 37.5\\%; orange diamond), and detection ($\\alpha{\\geq}0.75$, 62.5--75\\%).\nThe $\\alpha{=}0.60$ dip is dual-seed confirmed (s42: 3/8, s43: 0/8).\nPer-method comparison is in Figure~\\ref{fig:consensus_heatmap}.}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\paragraph{Granger-precedence detectability.}\nDespite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\\ref{fig:regime_map}).\nPermutation Granger tests (first-differenced, BH-corrected) find 0/8 pairs FDR-significant from $\\alpha{=}0.00$ through $\\alpha{=}0.45$ (including $\\alpha{=}0.25$ where a faint single-pair signal appears at FDR $p{=}0.053$ but aggregate detection remains null, and $\\alpha{=}0.35$/$0.40$/$0.45$ which confirm PermG fwd${=}$0/8), \\textbf{6/8} at $\\alpha{=}0.50$ (2~fp32 seeds, consistent), \\textbf{3/8} and \\textbf{0/8} at $\\alpha{=}0.60$ (s42 and s43 respectively; dual-seed confirmed non-monotonic dip), and \\textbf{6/8} at $\\alpha{=}1.0$.\nAt $\\alpha{=}0.75$ (3~seeds), permutation Granger finds 20/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.\nUnder Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.\nWithin-$\\alpha$ multi-seed analysis at $\\alpha{=}1.0$ yields \\textbf{24/24} canary$\\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.\nPermutation Granger forward significance is the primary detection indicator (Figure~\\ref{fig:regime_map}): it reaches 6/8 at $\\alpha{=}0.50$, dips to 3/8 at $\\alpha{=}0.60$ (synchronous collapse zone; see below), and recovers to 5--6/8 at $\\alpha{\\geq}0.75$.\nThe onset boundary lies at $\\alpha{\\approx}0.45$--$0.50$: finer-grained probing at $\\alpha{=}0.35$, $0.40$, and $0.45$ yields PermG fwd${=}$0/8 at all three levels, extending the blind spot through $\\alpha{=}0.45$.\nA faint signal first appears at $\\alpha{=}0.25$ (best-pair FDR $p{=}0.053$) but does not translate to aggregate detection; reliable detection begins at $\\alpha{=}0.50$ (6/8, 2~seeds).\nThis steep onset is consistent with theoretical expectations about signal-to-noise limits in short time series~\\cite{boettiger2012limits}.\nPermG $p$-values at $\\alpha{=}0.45$ reveal sub-threshold signal: the minimum FDR-corrected $p$ reaches 0.059 (seed~43, 18\\% above the $q{=}0.05$ threshold) and 0.091 (seed~42; Appendix~\\ref{app:robustness}).\nThis gradient is consistent with the power-threshold interpretation of $\\alpha_c$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\nSensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\\ref{app:robustness}).\nCross-architecture validation on GPT-2-medium confirms this boundary: at $\\alpha{=}0.25$, at most 1/8 pairs reach $K{\\geq}3$ ($3\\sigma$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\\%$ vs.\\ Pythia $-4.7{\\pm}0.5\\%$), while at $\\alpha{=}1.0$ all 6 canary$\\to$diversity pairs reach significance (\\S\\ref{sec:discussion}).\nTable~\\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.\nAt $\\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\\geq}4/5$) and 7/8 at Tier~2 ($K{\\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\\alpha{=}0.25$ and $\\alpha{=}1.0$. Tier~3: $K{\\geq}4/5$ methods (or $K{\\geq}3$ of 4 effective methods; \\S\\ref{sec:threshold_limitation}); Tier~2: $K{\\geq}3/5$. Drift is generation~0$\\to$10. GPT-2-medium $\\alpha{=}0.25$: single seed (seed=42); Pythia $\\alpha{=}0.25$: 3-seed mean${\\pm}$std. The onset boundary ($\\alpha{\\approx}0.45$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}\n\\label{tab:cross_arch_regime}\n\\begin{tabular}{llcccccc}\n\\toprule\n$\\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\\ Granger & Tier~3 \\\\\n\\midrule\n0.25 & Pythia-410M  & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & 0/8 & 0/8 \\\\\n0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\\\\n\\midrule\n1.00 & Pythia-410M  & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & 6/8 & 6/8 \\\\\n1.00 & GPT-2-medium & \\multicolumn{6}{c}{(reported in \\S\\ref{sec:discussion}; 6/8 canary$\\to$downstream pairs at Tier~3)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Detectability at $\\alpha{=}0.50$ and the transition zone.}\nUnder fp32 precision, $\\alpha{=}0.50$ is reliably detected: permutation Granger finds 6/8 pairs FDR-significant across both seeds (Table~\\ref{tab:method_comparison}).\nThe transition from sub-threshold to reliably detectable occurs between $\\alpha{=}0.45$ and $\\alpha{=}0.50$: finer-grained probing confirms PermG fwd${=}$0/8 at $\\alpha{=}0.35$, $0.40$, and $0.45$, while $\\alpha{=}0.50$ achieves 6/8 (2~seeds).\nA faint single-pair signal first appears at $\\alpha{=}0.25$ (entropy$\\to$distinct-1: raw $p{=}0.007$, FDR-corrected $p{=}0.053$), but all aggregate indicators remain null through $\\alpha{=}0.45$, placing the onset boundary at $\\alpha{\\approx}0.45$--$0.50$.\nAt $\\alpha{=}0.50$, canary sensitivity remains metric-dependent: ECE achieves significance in both fp32 seeds, while token entropy remains below the FDR threshold ($p_{\\text{fdr}}{\\geq}0.086$), identifying ECE as the more sensitive canary near the onset boundary.\nFigure~\\ref{fig:consensus_heatmap} visualizes the method$\\times\\alpha$ interaction, revealing a block structure that separates correlation-based methods from causal methods as a function of regime.\n\n\\paragraph{Quantifying the onset boundary.}\nSigmoid regression across the 12-point $\\alpha$ grid quantifies the sharp onset observed above.\nFitting $P(\\alpha) = 1/(1 + \\exp(-k(\\alpha - \\alpha_c)))$ to the PermG forward detection rate yields a critical threshold $\\alpha_c = 0.476$ with steepness $k \\geq 200$ and transition width $\\Delta\\alpha \\approx 0.02$ (Figure~\\ref{fig:phase_transition}).\nThe sigmoid model explains 96.9\\% of variance ($R^2 = 0.969$), substantially outperforming a power-law alternative ($R^2 = 0.808$; $\\Delta\\text{AIC} = 18.2$), confirming that the onset is steep rather than gradual.\nThis transition is striking because effective contamination barely changes across the boundary: after 10 generations of iterative training, both $\\alpha{=}0.45$ and $\\alpha{=}0.50$ drive the cumulative synthetic fraction above 99\\% ($C = 1{-}(1{-}\\alpha)^{10}$: $99.75\\%$ vs.\\ $99.90\\%$)---a difference of 0.15 percentage points---yet causal detectability jumps from 0/8 to 6/8.\nWe term this a \\emph{detection phase transition}: causal coupling emerges abruptly at a critical contamination threshold ($\\alpha_c{=}0.476$, $\\Delta\\alpha{\\approx}0.02$) rather than scaling smoothly with contamination dose.\nWithin the $S \\times R$ framework (\\S\\ref{sec:theory}), $\\alpha_c{=}0.476$ localizes the point at which signal strength $S(\\alpha)$ first crosses the detection floor, while the high steepness ($k \\geq 200$) indicates that temporal resolution $R(\\alpha)$ remains large at onset---the entropy--diversity lag has not yet begun to compress.\nCross-architecture comparison reveals no monotonic relationship between model scale and onset sensitivity (Qwen-0.8B $\\approx$ Pythia-6.9B $>$ Pythia-410M $>$ Pythia-1.4B $>$ SmolLM3-3B), suggesting that architecture and pre-training data exert stronger influence than parameter count on detection onset.\n\n\\begin{figure}[t]\n\\centering\n% TODO: transfer fig_phase_transition.pdf from westd-17855\n%\\includegraphics[width=\\linewidth]{figures/fig_phase_transition.pdf}\n\\caption{Sigmoid fit to the PermG forward detection rate across 12 contamination levels.\nThe fitted critical threshold $\\alpha_c = 0.476$ with steepness $k \\geq 200$ indicates a steep onset of causal detectability.\nSigmoid $R^2 = 0.969$ vs.\\ power-law $R^2 = 0.808$ ($\\Delta\\text{AIC} = 18.2$).}\n\\label{fig:phase_transition}\n\\end{figure}\n\n\\paragraph{Specification curve robustness.}\nTo verify that the detection phase transition is not an artifact of analytical choices, we conduct a specification curve analysis spanning 1{,}160 analytical specifications across 29 experimental conditions.\nSpecifications vary lag order, differencing strategy, significance threshold, FDR correction method, and permutation count.\nPermG maintains a 0\\% false-positive rate at the null ($\\alpha{=}0.00$) across all 1{,}160 specifications, while naive cross-correlation reaches 100\\% regardless of specification---confirming that the FPR separation between methods is robust to analytical degrees of freedom.\nThe phase transition itself is specification-invariant: PermG detection rate remains near zero below $\\alpha{=}0.50$ (${\\sim}0\\%$), rises to 81.2\\% at $\\alpha{=}0.50$, and reaches 87.5\\% at $\\alpha{=}0.75$ across all specifications.\nThis demonstrates that the onset at $\\alpha_c{\\approx}0.50$ is a property of the data-generating process, not a consequence of researcher degrees of freedom in method configuration.\n\n\\paragraph{Non-monotonic dose-response: the synchronous collapse zone.}\nDual-seed replication at $\\alpha{=}0.60$ reveals a non-monotonic dose-response in Granger detectability: PermG fwd drops to 3/8 (s42) and 0/8 (s43), below both $\\alpha{=}0.50$ (6/8, 2~seeds) and $\\alpha{=}0.75$ (5--6/8 per seed, 3~seeds).\nThis creates a four-regime structure in the dose-response profile: \\emph{blind} ($\\alpha{\\leq}0.45$, 0/8), \\emph{onset} ($\\alpha{\\approx}0.50$, 6/8), \\emph{synchronous dip} ($\\alpha{\\approx}0.60$, 0--3/8), and \\emph{detection} ($\\alpha{\\geq}0.75$, 5--6/8 per seed; 6/8 at $\\alpha{=}1.0$).\nThe dip confirms the non-monotonic prediction of the $S \\times R$ framework (\\S\\ref{sec:theory}): at $\\alpha{=}0.60$, signal strength $S$ continues rising but temporal resolution $R$ drops sharply due to relaxation time matching, producing a local minimum in detectability.\nThe synchronous zone is mechanistically distinct from the blind spot: in the blind spot, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.\nToda--Yamamoto achieves moderate detection across this range (3--4/8 at $\\alpha{\\geq}0.50$; \\S\\ref{sec:ty_limitation}), with its detection at $\\alpha{=}0.60$ suggesting partial inter-method complementarity in the synchronous collapse zone where PermG drops to 0--3/8.\nThis non-monotonicity also implies that simple threshold-based triggers (such as the 15\\% entropy criterion in \\S\\ref{sec:intervention}) may outperform formal Granger tests at intermediate contamination levels.\n\n\\paragraph{Predictions for longer generation chains.}\nThe statistical power interpretation (\\S\\ref{sec:theory}) generates three testable predictions for $T{=}20$.\nSince $\\mathrm{Power}(\\alpha, T) = \\Phi\\bigl(S(\\alpha) \\cdot R(\\alpha) \\cdot \\sqrt{T} \\,/\\, \\sigma_{\\mathrm{noise}}\\bigr)$, increasing $T$ raises power at every $\\alpha$:\n(i)~$\\alpha_c$ should \\emph{left-shift}---the detection threshold decreases because $\\sqrt{20}/\\sqrt{10} \\approx 1.41$ multiplies the power argument uniformly, so contamination levels currently below threshold (e.g., $\\alpha{=}0.45$, where $T{=}10$ yields PermG 0/8 with sub-threshold $p$-values of 0.059--0.091) may cross into detectability;\n(ii)~the transition should \\emph{smooth}---the $\\sqrt{T}$ scaling broadens the power curve across $\\alpha$, making the onset less step-like (the synchronous dip at $\\alpha{=}0.60$ should also attenuate as finer temporal sampling resolves sub-generation lags);\n(iii)~different methods should exhibit \\emph{different} $\\alpha_c$ values, since each method has its own power curve---empirical validation of this prediction awaits $T{=}20$ replication.\nThese predictions are currently under empirical verification with extended ($T{=}20$) generation protocols.\n\n\n\\subsection{Case Study: Canary Prediction of Diversity Collapse}\n\\label{sec:case_study}\n\nHaving established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).\nWe scope this claim precisely: canary metrics predict \\emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.\n\n\\paragraph{Full synthetic replacement ($\\alpha{=}1.0$, 4 seeds).}\nToken entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \\S\\ref{sec:discussion}).\nCross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.\nFigure~\\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.\nPermutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nReverse-direction tests (downstream$\\to$canary) on WikiText-103 find \\textbf{0/24} FDR-significant (all $p{>}0.49$), establishing directional asymmetry in this domain.\\footnote{C4 exhibits domain-dependent directionality: at $\\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling (\\S\\ref{sec:discussion}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories across 10 generations at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\\paragraph{High contamination ($\\alpha{=}0.75$, 3 seeds).}\nDirectional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 20/24 forward pairs FDR-significant, 0/24 reverse).\nHowever, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\\alpha{=}0.75$ squarely in the transitional detection regime.\nDifferenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\\S\\ref{sec:pitfalls}).\n\n\\paragraph{ECE as a conditional secondary canary.}\nECE's forward consensus matches token entropy (both achieve PermG\\_fwd 6/8 across all conditions), but the reverse profile diverges sharply.\nAcross 7 validated conditions at $\\alpha{=}1.0$ (3 architectures $\\times$ 2 scales $\\times$ 2 domains), token entropy reverse direction yields \\textbf{0/28} FDR-significant pairs (consistent with unidirectional forward causation at full synthetic replacement; domain-dependent bidirectionality emerges at lower $\\alpha$, \\S\\ref{sec:discussion}), while ECE reverse direction yields \\textbf{13/28} significant pairs, with 5/7 conditions containing at least one reverse-significant pair, all in the distinct$\\to$ECE direction.\nThis bidirectional coupling is the core reason ECE is classified as a secondary canary: ECE and diversity exhibit mutual feedback, and the interpretability of ECE's causal direction is correspondingly limited.\nThis result also instantiates Claim~3 (method sensitivity): when only forward significance is considered, the two canary types appear equivalent; incorporating reverse-direction tests separates them. The choice of analysis dimension alters the canary classification itself.\n\n\\paragraph{Failed canary candidates.}\nNot all metrics serve as canaries.\nEffective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.\nEffective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\\alpha{=}0.25$ it \\emph{increases} from 2.37 to 8.48 (+258\\%).\nThe GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.\nThis opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\\S\\ref{sec:discussion}).\n\n\\paragraph{Consensus filtering.}\nOf 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline (PermG fwd ${\\geq}6/8$, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).\nThe 10 eliminated pairs comprise all canary$\\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).\nThe consensus framework reduces the naive 75\\% forward-direction FPR to 0\\%, matching the most conservative individual methods (Figure~\\ref{fig:consensus_workflow}).\n\n\n\\subsection{Consensus Framework Validation}\n\\label{sec:consensus_validation}\n\nWe validate the consensus framework's calibration using built-in experimental controls.\n\n\\paragraph{False positive rate.}\nAt $\\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.\nIndividual-method forward-direction FPR ranges from \\textbf{75\\%} (naive cross-correlation: 6/8) through 37.5\\% (threshold) down to \\textbf{0\\%} (permutation Granger and differenced cross-correlation); Toda--Yamamoto's null-control FPR has not yet been evaluated through the corrected pipeline (\\S\\ref{sec:ty_limitation}).\nThe multi-method consensus at $K{\\geq}3$ ($3\\sigma$) achieves \\textbf{FPR${=}$0\\%} (0/24 pairs, three independent seeds), matching the best individual method (permutation Granger) while providing a formal benchmark for method reliability (Table~\\ref{tab:fpr_fnr}).\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\\geq}3\\times$ the $\\alpha{=}0.0$ baseline (entropy $11.93\\times$, ECE $73.12\\times$) and canary onset strictly preceding downstream onset by ${\\geq}1$ generation (\\S\\ref{sec:calibration}).\nFNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\\geq}3/4$, $S{\\geq}3/4$, all~6 are recovered (\\textbf{FNR${=}$0\\%}).\nToda--Yamamoto's individual FNR is 50\\% (4/8 detected at $\\alpha{=}1.0$, seed~42), consistent with its moderate supplementary classification (\\S\\ref{sec:ty_limitation}).\nBoth FPR and FNR are validated on the joint method${\\times}$seed dimension (FPR: 3~seeds at $\\alpha{=}0.0$; FNR: 4~seeds at $\\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\\geq}3$).\nTable~\\ref{tab:fpr_fnr} reports the calibration results.\nTable~\\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\\alpha$ including the null control, while permutation Granger achieves correct verdicts at all levels with zero FPR.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-method inference errors across contamination levels.\nEach cell shows the verdict (significant or not) based on multi-seed majority ($\\geq$2/3 seeds with $\\geq$4/8 pairs significant).\n\\checkmark\\ = correct, \\textcolor{red}{FP} = false positive, \\textcolor{blue}{FN} = false negative, $\\circ$ = ambiguous ground truth (either verdict plausible).\nNaive XCorr produces false positives at \\emph{every} $\\alpha$ including the null control. Permutation Granger achieves correct verdicts at all levels with zero FPR. $^\\dagger$Rows marked pending have cross-script inconsistencies under audit.}\n\\label{tab:single-method-errors}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textit{No signal}} & \\textit{Ambiguous} & \\multicolumn{2}{c}{\\textit{Causal signal}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-4} \\cmidrule(lr){5-6}\nMethod & $\\alpha{=}0.00$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.00$ \\\\\n\\midrule\nNaive XCorr\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,7,8}\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,8}\n  & $\\circ${\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nDiff XCorr (FDR)$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\nThreshold Onset$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\nPerm Granger (FDR)\n  & \\checkmark{\\scriptsize\\ 0,0,0}\n  & \\checkmark{\\scriptsize\\ 0,0}\n  & $\\circ${\\scriptsize\\ 0,6,3}\n  & \\checkmark{\\scriptsize\\ 8,5,6}\n  & \\checkmark{\\scriptsize\\ 6,6,6} \\\\\nTY Granger$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\n\\midrule\n\\textbf{Consensus ($K{\\geq}3$)}$^\\dagger$\n  & --- & --- & --- & --- & --- \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\\\\n\\multicolumn{6}{l}{\\footnotesize Seeds: $\\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\\alpha{=}0.25$: 43, 44; $\\alpha{=}1.00$: 42, 43, 45.} \\\\\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Bootstrap power analysis.}\nTo quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\\alpha{=}1.0$).\nPermutation Granger achieves power${=}1.0$ on genuine pairs (canary$\\to$diversity) and power${=}0.0$ on spurious pairs (canary$\\to$perplexity), providing clean separation.\nToda--Yamamoto achieves power${=}0.50$ on genuine pairs (4/8 detected at $\\alpha{=}1.0$), consistent with its moderate supplementary classification (\\S\\ref{sec:ty_limitation}).\nWe note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\beta{=}0.3$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\geq}3$ ($3\\sigma$, excluding threshold onset; \\S\\ref{sec:threshold_limitation}) achieves FPR${=}$0\\% and FNR${=}$0\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration of any single method. FPR: $\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds). $^\\dagger$Moderate supplementary method (\\S\\ref{sec:ty_limitation}); FPR pending (null condition not yet run through corrected pipeline); FNR from single-seed $\\alpha{=}1.0$ (4/8 detected).}\n\\label{tab:fpr_fnr}\n\\begin{tabular}{lcc}\n\\toprule\nCriterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\n\\midrule\nNaive XCorr              & 100\\%              & 0\\%  \\\\\nDifferenced XCorr        & 37.5\\%             & 0\\%  \\\\\nThreshold Onset          & 20.8\\% (12.5--37.5) & 0\\%  \\\\\nPermutation Granger      & 0\\%                & 0\\%  \\\\\nToda--Yamamoto$^\\dagger$  & ---                & 50\\%   \\\\\n\\midrule\nConsensus ($K{\\geq}3$, $3\\sigma$)      & 0\\%    & 0\\%  \\\\\nConsensus ($K{\\geq}3$, $S{\\geq}3/4$)   & 0\\%    & 0\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\n\\label{sec:generalization}\n\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\nTo test whether these findings transfer, we evaluate the lead-lag pattern along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\nAll conditions use $\\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture lead-lag detectability ($\\alpha{=}1.0$, D105 unified pipeline, $3\\sigma$ calibration, M035 direction-corrected).\nPermG~fwd: permutation Granger forward-direction FDR-significant pairs (out of 8).\n$K{\\geq}3$: pairs where ${\\geq}3$ of 5 methods reach FDR significance (direction-checked, $3\\sigma$).\nPermG~fwd ${\\geq}6/8$ in 13/15 confirmed conditions; $K{\\geq}3$ ${\\geq}6/8$ in 10/14 with known consensus (Padding-410M and Pythia-1.4B C4 pending audit).\nExceptions: Pythia-1.4B (s42: 1/8$^\\dagger$, s43: 3/8) and SmolLM3-3B (3/8$^\\ddagger$).\nRows marked ``---'' are running experiments; final values will be filled without format changes.}\n\\label{tab:generalization}\n\\begin{tabular}{lrclcc}\n\\toprule\nModel & Params & Seed & Domain & PermG (fwd) & $K{\\geq}3$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Baseline}} \\\\\nPythia-410M       & 410M & s42 & Wiki & 6/8            & 6/8            \\\\\nPythia-410M       & 410M & s43 & Wiki & 6/8            & 6/8            \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Scale}} \\\\\nPythia-1.4B       & 1.4B & s42 & Wiki & \\textbf{2/8}$^\\dagger$ & \\textbf{1/8}$^\\dagger$  \\\\\nPythia-1.4B       & 1.4B & s43 & Wiki & 6/8            & 3/8     \\\\\nPythia-6.9B       & 6.9B & s42 & Wiki & 7/8$^*$        & 6/8            \\\\\nPythia-6.9B       & 6.9B & s43 & Wiki & ---            & ---            \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Architecture}} \\\\\nGPT-2-medium      & 345M & s42 & Wiki & 6/8            & 6/8            \\\\\nGPT-2-medium      & 345M & s43 & Wiki & 6/8            & 6/8            \\\\\nOPT-1.3B          & 1.3B & s42 & Wiki & 6/8            & 6/8            \\\\\nOPT-1.3B          & 1.3B & s43 & Wiki & 6/8            & 6/8            \\\\\nQwen3.5-0.8B      & 0.8B & s42 & Wiki & 8/8            & 6/8            \\\\\nQwen3.5-0.8B      & 0.8B & s43 & Wiki & ---            & ---            \\\\\nSmolLM3-3B        & 3.0B & s42 & Wiki & \\textbf{3/8}$^\\ddagger$ & \\textbf{3/8}$^\\ddagger$ \\\\\nSmolLM3-3B        & 3.0B & s43 & Wiki & ---            & ---            \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Tokenization}} \\\\\nPadding-410M      & 410M & s42 & Wiki & 6/8            & 6/8$^{\\S}$     \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\emph{Domain}} \\\\\nPythia-1B         & 1.0B & s42 & C4   & 8/8            & 7/8            \\\\\nPythia-1B         & 1.0B & s43 & C4   & 7/8            & 6/8            \\\\\nPythia-1.4B       & 1.4B & s42 & C4   & 8/8            & ---            \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Seed-sensitive: PermG s42 2/8, s43 6/8; $K{\\geq}3$ s42 1/8, s43 3/8. Likely stochastic instability at this scale (\\S\\ref{sec:discussion}).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Canary metric splitting: only ECE$\\to$downstream pairs detected (3/4); entropy$\\to$downstream 0/4 (\\S\\ref{sec:smollm3}).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^*$bf16 precision (model exceeds single-GPU fp32 capacity).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^{\\S}$Padding-410M $K{\\geq}3$ pending supplementary audit (expected stable at 6/8).} \\\\\n\\multicolumn{6}{l}{\\footnotesize Full method-level breakdown ($K{\\geq}4$) in Appendix~\\ref{app:cross_arch}.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-condition robustness.}\nTable~\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern is robust across 15 confirmed conditions (3 pending) spanning six model families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B, and two training domains (WikiText-103, C4).\nPermutation Granger forward significance reaches ${\\geq}6/8$ in 13 of 15 conditions (86.7\\%), with two exceptions: Pythia-1.4B seed~42 (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs are detected (see below).\n$K{\\geq}3$ multi-method consensus reaches ${\\geq}6/8$ in 10 of 14 conditions with known consensus (Padding-410M and Pythia-1.4B C4 pending audit), with exceptions Pythia-1.4B (s42: 1/8, s43: 3/8) and SmolLM3-3B (3/8).\nThe concordance between PermG and $K{\\geq}3$ confirms that multi-method consensus is robust across architectures.\nThe onset threshold $\\alpha_c{\\approx}0.50$ is robust across all six families: every architecture that achieves detection does so at or above $\\alpha{=}0.50$, while none achieves reliable detection below this threshold, suggesting that the detection phase transition boundary is architecture-independent even though detection power above onset varies with model family.\nWith threshold onset power-limited and Toda--Yamamoto providing moderate supplementary signal (3--4/8 at $\\alpha{\\geq}0.50$; \\S\\ref{sec:ty_limitation}), $K{\\geq}3$ draws on four contributing methods---a stronger standard than simple majority (\\S\\ref{sec:consensus}).\n\n\\paragraph{Scale generalization.}\nScaling from 410M to 6.9B parameters confirms that the lead-lag pattern persists across a $17\\times$ parameter range.\nPythia-6.9B achieves PermG fwd~7/8 (bf16), the strongest single-seed detection.\nWithin the Pythia family, 1.4B shows seed dependence: s42 yields only 2/8 (the sole outlier across all conditions), while s43 recovers to 6/8.\nQwen3.5-0.8B (PermG~fwd~8/8) extends the finding beyond the Pythia/GPT-2/OPT decoder-only family to an independently trained architecture with a different tokenizer.\n\n\\paragraph{Domain generalization.}\nReplacing WikiText-103 with C4 yields the strongest forward detection: Pythia-1B achieves PermG~fwd~8/8 in both seeds at $\\alpha{=}1.0$, confirming that the lead-lag pattern is not an artifact of narrow topical distribution.\nThe domain effect is scale-dependent: Pythia-1.4B achieves PermG~fwd~8/8 on C4 ($\\alpha{=}1.0$), compared with 2/8 on WikiText at the same scale, recovering to 7/8 at Pythia-6.9B---suggesting that dataset characteristics modulate detection power independently of model capacity.\nHowever, directional asymmetry does not transfer fully across domains.\nAt $\\alpha{=}0.50$ (Pythia-410M, C4, s42 fp32), PermG reverse reaches 7/8 (compared to 0/8 in all WikiText conditions), indicating near-symmetric bidirectional coupling between canary and downstream metrics.\nThis domain-dependent directionality suggests that the unidirectional forward causation observed in WikiText may partly reflect domain-specific dynamics rather than a universal property of collapse; implications are discussed in \\S\\ref{sec:discussion}.\n\n\\paragraph{Canary metric sensitivity: the SmolLM3-3B case.}\n\\label{sec:smollm3}\nSmolLM3-3B (PermG fwd 3/8) reveals that canary metric choice is itself a dimension of method sensitivity.\nDecomposing by canary type: ECE$\\to$downstream achieves 3/4 significant pairs, while token entropy$\\to$downstream achieves 0/4.\nThe root cause is that SmolLM3's token entropy exhibits non-monotonic oscillations across generations, violating the monotonic decline pattern that Granger tests exploit; ECE, by contrast, maintains its monotonic upward trajectory.\nMulti-method consensus confirms the severity: entropy pairs activate only via naive and differenced cross-correlation (per-pair $K{=}2$), ECE pairs activate only via differenced cross-correlation and permutation Granger (per-pair $K{=}2$), and no pair exceeds two-method agreement---illustrating that even within a single architecture, the method panel fragments along canary metric boundaries.\nThis architecture-dependent canary sensitivity complements the finding that effective rank direction is model-dependent (\\S\\ref{sec:case_study}): no single canary metric is universally optimal across all architectures, enriching Claim~3 by adding canary metric selection as a further source of analytic variability.\n\n\\subsection{Canary-Based Early Intervention}\n\\label{sec:intervention}\n\nTo test whether the lead-lag relationship translates into practical utility, we implement a predictive cessation protocol: training with synthetic data ($\\alpha{=}1.0$) continues until token entropy drops ${>}15\\%$ relative to generation~0, at which point $\\alpha$ is switched to $0.0$ (pure real data).\nWe compare against a reactive baseline that triggers only when distinct-1 drops ${>}10\\%$---a downstream metric that, by the lead-lag hypothesis, should respond later.\n\n\\paragraph{Pythia-410M.}\nThe predictive trigger fires at generation~1 in both seed-precision pairs tested (s42 fp32: entropy $3.234{\\to}1.918$, ${\\downarrow}40.7\\%$; s43 bf16: $3.257{\\to}2.523$, ${\\downarrow}22.5\\%$).\nThe reactive baseline triggers one generation later (generation~2, distinct-1 ${\\downarrow}15.6\\%$).\nPredictive intervention reduces peak perplexity by 63\\% relative to reactive ($56.99$ vs.\\ $157.09$, s42 fp32) and achieves full recovery by generation~2 versus generation~4 for reactive.\nThe bf16 pair shows a milder perturbation (peak perplexity $24.65$ vs.\\ $56.99$) consistent with stochastic rounding regularization, but the structural pattern---generation~1 trigger, generation~2 recovery---is identical.\nBoth conditions converge to the $\\alpha{=}0.0$ baseline by generation~10.\n\n\\paragraph{Cross-scale validation: Pythia-1.4B.}\nPythia-1.4B (s42 fp32) replicates the 410M pattern: token entropy drops $51.9\\%$ at generation~1 ($2.946{\\to}1.418$), exceeding the 15\\% threshold, and recovers to $2.892$ by generation~2 ($98.2\\%$ of baseline).\nPerplexity spikes from $19.68$ to $65.37$ at the trigger generation and recovers to $17.44$ by generation~2 (stable at $17.60$ through generation~10).\nThe trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\\times$ scale gap (410M to 1.4B), confirming that the canary-based intervention mechanism is scale-independent: the 15\\% entropy threshold generalizes without recalibration across model sizes.",
      "numLines": 475,
      "startLine": 1,
      "totalLines": 475
    }
  },
  "sourceToolAssistantUUID": "646dd7f8-1eb1-4c04-9c36-3dbe13b0a86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "leafUuid": "b774285f-8c58-406d-a14b-3aa5dda46ccb",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Compress results section for EMNLP paper",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Assistant

_source line 16 · 2026-05-20T11:03:47.971Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me carefully write the compressed experiments/results section. I need to:

1. Follow all the active constraints (D131, D141, D142, D143, D145, M037, D079, C002-C009)
2. Follow all writing rules (no em-dashes, no -ing endings, no "Furthermore"/"Moreover"/"Additionally", no "Notably"/"Interestingly", no blacklisted words, natural paragraph length, every number serves narrative, booktabs only)
3. Include exactly 4 subsections starting from §5.1
4. Include 2 tables and 2 figure floats as specified


5. Target ~70 lines of prose

Let me draft this carefully, keeping in mind the key constraints: "steep onset" and "detection phase transition" language, all α_c mentions must include "at T=10", Power Theory uses "consistent with", no CSD data in Results, no TY=7/8 evidence, the C4 wording about dataset characteristics modulating detection power, and dose-response uses PermG only.

I also need to remember: K≥3 column stays out of Table 2, fp32 as main axis with bf16 only in Pythia-6.9B footnote, no em-dashes or explanatory en-dashes, no -ing clause endings, and avoiding "Furthermore"/"Moreover"/"Additionally" chains and words like "leverage"/"utilize"/"delve"/"facilitate"/"myriad"/"plethora".

Now I'm structuring the Results section into four subsections: Detection Phase Transition covering the ~20 lines on steep onset behavior, Dose-Response and S×R Framework for ~20 lines on the scaling relationships, Cross-Architecture Generalization for ~15 lines on model generalization, and Canary-Based Early Intervention for ~15 lines on the intervention approach.

For the Detection Phase Transition subsection, I need to cover how diversity collapse occurs uniformly across all α values but causal detectability shows sharp regime dependence—PermG shows zero FDR-significant results from α=0.00 through α=0.45 then jumps to 6/8 at α=0.50, while cumulative contamination only changes marginally between those thresholds (0.15 percentage points), and sigmoid regression fits with α_c=0.476 and k≥200.

The first-differencing analysis reveals the canary→diversity relationship holds robustly across all 24 seeds in both forward and reverse directions, but the canary→perplexity relationship is spurious (F≈0, p=0.99), so the causal claim is scoped specifically to diversity. At α=1.0 I see perfect directional asymmetry with 24/24 forward but 0/24 reverse across four seeds. Just below the threshold at α=0.45, PermG yields marginal p-values (0.059 and 0.091) consistent with a power-law interpretation. The specification curve analysis across 1,160 different specifications confirms the phase transition is robust and invariant to modeling choices.

At the lower bound α=0.10, there's a canary blind spot where distinct-1 drops 39.6% but entropy remains indistinguishable from the null distribution. Now I need to organize the writeup: section 5.1 gets 9 key findings across roughly 20 lines, then 5.2 adds 4 points with a figure and table, 5.3 brings 6 points with another table, and 5.4 closes with 6 points. I should also remember to specify T=10 whenever mentioning the critical threshold α_c=0.476, and use "consistent with" rather than "confirms" when discussing the power theory predictions.

For the narrative structure, I'm planning three paragraphs: the first covers the core discovery of ubiquitous collapse with regime-dependent detectability, the sharp sigmoid transition, and the sub-threshold p-values that align with power-threshold logic. The second addresses the scope of the claim and directional asymmetry. The third handles the blind spot phenomenon. Let me draft this keeping each paragraph to natural length—5 to 8 sentences—and weave the findings together fluidly rather than listing them. I'm organizing the results into a structured narrative. The phase transition is the core finding, so I'll lead with diversity collapse across all contamination levels, the sharp regime-dependence of causal detectability, and how the sigmoid regression pinpoints the critical threshold. Then I'll note that first-differencing isolates the effect to diversity alone, mention the perfect detection at high contamination, and flag the blind spot at low contamination. I'm fitting a sigmoid model to the contamination levels that reveals a sharp critical threshold around α = 0.476, with an extremely steep transition (k ≥ 200) spanning only about 0.02 in α-space—this sigmoid fits far better than a power law, suggesting the detection onset reflects a genuine phase transition rather than gradual signal emergence. The p-values just below this threshold remain sub-significant but close to detection, confirming that we're observing PermG's power curve crossing the statistical floor.

A specification curve analysis across over a thousand analytical choices confirms this phase transition holds robustly. When I apply first-differencing to isolate causal relationships, the canary-to-diversity signal remains unanimously significant across all seeds and specifications, but the canary-to-perplexity association vanishes entirely—revealing it was just a shared trend artifact. The directional asymmetry is stark: at α = 1.0, all forward-direction pairs show FDR significance while reverse pairs show none, and this pattern holds consistently across WikiText conditions. However, the mechanism has a limitation at lower contamination levels.

At α = 0.10, distinct-1 has already dropped substantially, yet token entropy shows no meaningful change from baseline—the diversity collapse happens without any detectable signal in the canary metrics below the critical threshold. I'm looking at metric trajectories showing how token entropy drops immediately at generation 1, while distinct-1 begins declining one or two generations later, creating a consistent lead across all seeds that aligns with the directional causality findings.

Now examining the four distinct regimes: blind collapse where no causal signal emerges, an onset phase around α ≈ 0.50, a synchronous dip regime near α ≈ 0.60 where both metrics respond together, and finally detection at higher α values where the causal structure becomes clear. The S×R framework shows signal strength rising monotonically with α while response drops sharply around the synchronous dip point.

Method choice dramatically shifts the significance landscape—swinging from 100% to 37.5% depending on which test is applied—with very low inter-method agreement (κ=0.185) and spurious detection rates exceeding 62.5%. PermG emerges as the most reliable approach, showing zero false positive rate under null control and consistent detection starting at α≥0.50. I'm now checking how the power predictions scale with T=20 observations, expecting the critical α threshold to shift left, transitions to smooth out, and method-dependent effects to emerge under empirical testing. The $S \times R$ framework explains this non-monotonic behavior: signal strength increases with contamination, but temporal resolution degrades when relaxation time aligns with the observation window, causing the product to dip around $\alpha \approx 0.60$ where the canary-to-downstream lag compresses. The synchronous zone differs mechanistically from the blind zone—here both metrics drift substantially but without temporal offset, whereas in the blind zone they're indistinguishable from noise. Method choice introduces substantial variability; at $\alpha = 1.0$, significance rates span from 100% with naive cross-correlation down to 37.5% with PermG, and inter-method agreement is near chance.

PermG stands out as the only method achieving zero false positives while maintaining consistent detection above $\alpha = 0.50$, because it builds its null from the observed data itself, tests directionality inherently, and avoids threshold calibration. I'm now laying out three testable predictions for $T = 20$: the critical contamination level should shift leftward as temporal resolution improves, the transition should smooth with finer sampling, and different methods should show different critical points—all currently under empirical investigation. Generating markdown table... I'm checking the results against the original table and task specification—the Permutation Granger row matches what's expected. Now looking at section 5.3, which covers the broader evaluation across 15 model-seed combinations spanning six families and model sizes from 345M to 6.9B parameters across two domains, showing that Permutation Granger achieves at least 6 out of 8 detections in 13 of those 15 cases (87%), with only two exceptions where it underperforms, though one of those recovers with different seeds. Looking at the dataset effects more closely—Pythia-1.4B shows a dramatic difference between C4 and WikiText at the same scale, suggesting that domain characteristics play a significant role in detection sensitivity independent of model size. The bidirectionality findings further support this, with PermG reverse achieving 7/8 on C4 but complete failure on WikiText, indicating the dataset itself constrains what the phase transition can reveal. reaches 8/8 on C4 versus only 2/8 on WikiText at the same scale, suggesting dataset choice substantially impacts detection reliability. The directional asymmetry also shifts by domain—on C4, reverse causation detection hits 7/8 compared to complete failure across WikiText conditions, indicating that the forward-only pattern I observed might be domain-specific rather than a fundamental property of the collapse mechanism.

Now I'm catching an issue with my phrasing—I've been ending sentences with gerund clauses, which creates awkward constructions. Let me fix that sentence about SmolLM3's entropy oscillations by restructuring it to avoid the dangling participle, then I'll scan the rest of the paper for similar problems.

I should also verify I haven't overused em-dashes, then move on to drafting Table 2 and the corresponding section.

Generating markdown table... Generating markdown table... The predictive protocol triggers at generation 1 with a 58% perplexity reduction compared to the reactive baseline, recovering by generation 2 versus generation 4, and this pattern holds consistently across both model scales through generation 10 convergence.

Now I'm organizing these findings into a four-layer taxonomy for collapse detection: dimensionality collapse via n-gram diversity at lower contamination thresholds, distributional variance through calibration drift, causal coupling using Granger precedence, and dynamical stability from lag structure analysis. The key insight is that the 15% entropy threshold and trigger timing generalize across the 3.4× scale difference without needing recalibration, suggesting that effective collapse monitoring requires combining multiple detection layers rather than relying on any single metric. I'm checking the line counts across each section—§5.1 and §5.2 are running a bit long at around 24 lines each, while §5.3 and §5.4 are tighter at 15 lines. The total is hovering near 78 lines, so I need to trim it down closer to 70. Let me scan through for constraint violations: checking for em-dashes, -ing endings, and "Furthermore"—so far the text looks clean on those fronts. I'm checking whether the left-shift interpretation for α_c at T=10 is clear enough—it should convey that the observed α_c shifts leftward as T increases from 10 to 20. Now I'm verifying the remaining sections: the dataset characteristics language matches the source, there's no K≥3 column in the table as required, fp32 is the main axis with bf16 only in a footnote for Pythia, and I've excluded CSD data and TY=7/8 evidence as specified. Finally, I need to review the LaTeX formatting and table footnotes to make sure everything looks polished.

I'm double-checking the terminology—"steep onset" and "detection phase transition" are correct per the constraints, never "near-discontinuous." The method_comparison table uses seed 42 with fp32 and direction-checked as specified, and the PermG value at α=0.50 is 75% (6/8), which matches both the original table and task specification. Toda--Yamamoto uses an en-dash between names following standard typographic convention, which is allowed. Now I'm ready to compile everything together, though I should double-check the Table 2 structure—it needs four columns (Model, Params, Domain, PermG fwd) with appropriate alignment, and I need to be careful about when to show ranges versus single values for the multi-seed models. Writing the LaTeX table... I'm verifying the figure references match the task requirements—the metric_trajectory figure goes in §5.1 as a float, while the phase_transition figure with the sigmoid fit was already placed in the Introduction. Now I'm ready to write out the complete section, but first let me confirm §5.2 doesn't use language like "confirms" or "validates" when describing the Power Theory predictions, since those should remain as testable hypotheses rather than validated claims. I need to be consistent with the constraint about Power Theory—using "consistent with" rather than "explains" or "confirms." Let me go through the paper and make sure I'm applying this language correctly throughout section 5, checking each reference to the theoretical framework. I'm verifying that the key findings are all present in section 5.4—the four-layer detection taxonomy and the scale-independence result are both accounted for. Now I need to trim down to around 70 lines by tightening up the earlier sections, particularly paragraph 1 of 5.1 where I can merge some of the sentences about the spec curve and sub-threshold behavior. Let me work through what can be condensed without losing clarity. I'm condensing the PermG advantages into a single sentence that captures the key properties—nonparametric null distribution, built-in directionality, and hyperparameter-free design—then moving into the S×R framework predictions that follow. Method choice drives substantial variability in results—at α=1.0, significance rates span from 100% with naive cross-correlation down to 37.5% with PermG, indicating near-chance agreement between methods and spurious detection rates exceeding 62.5%. PermG stands out as the only approach achieving both zero false positive control and consistent detection above α≥0.50, making it the most reliable across different signal strengths. Finalizing the table formatting with em-dashes for missing data entries. Writing the LaTeX file now... I'm adding spacing between the footnotes in Table 2 using the \par approach, then moving into the Detection Phase Transition section where I'm describing how diversity collapse occurs uniformly across contamination levels but causal detectability shows a sharp regime shift—with permutation Granger tests finding no significant canary-to-downstream pairs until α reaches 0.50. The $p$-values at $\alpha=0.45$ sit just above the detection threshold, supporting the interpretation that this phase transition reflects PermG's statistical power crossing a critical boundary rather than a genuine shift in the underlying signal. A specification curve spanning over a thousand analytical choices confirms this detection threshold is robust across different methodological approaches. First-differencing analysis shows the canary-to-diversity relationship maintains consistent significance regardless of specification. seeds at $\alpha{=}1.0$), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.
All canary claims are therefore scoped to diversity metrics only.
At $\alpha{=}1.0$, all 24/24 forward-direction pairs reach FDR significance with 0/24 in the reverse direction (4~seeds), establishing directional asymmetry.
The canary mechanism also exhibits a blind spot: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).
Below $\alpha_c$ at $T{=}10$, diversity collapse happens without any detectable causal signal in the canary metrics. I'm visualizing the metric trajectories across generations at $\alpha{=}1.0$ to show how token entropy drops first, followed by distinct-1 declining one generation later—a consistent lead across all seeds that aligns with the directional causality pattern. Now moving into the dose-response framework... The choice of statistical method introduces substantial variability—at maximum contamination, detection rates span from 100% down to 37.5% across approaches, with near-chance agreement between methods and spurious rates exceeding 62%. PermG stands out as the only method achieving zero false positives under the null while maintaining consistent detection across moderate contamination levels, thanks to its nonparametric null distribution and built-in directionality. The $S \times R$ framework predicts how detection power scales with observation window length, with testable predictions about the critical contamination threshold at different time horizons.

Generating dose-response figure... Generating markdown table...

Now I'm moving on to evaluate how well the detection phase transition generalizes across different model architectures and random seeds, testing fifteen combinations from six model families. SmolLM3's token entropy shows non-monotonic oscillations across generations that break the monotonic decline assumption required for Granger causality testing. The critical threshold for detection appears consistent across architectures at around α ≈ 0.50, with no reliable detection below this point. Switching from WikiText-103 to C4 dramatically improves detection rates—Pythia-1B achieves perfect detection on C4 while only reaching 2/8 on WikiText—suggesting dataset characteristics independently influence detection strength regardless of model size, and directional asymmetry also shifts depending on the training domain.

Generating markdown table... Generating the table data... I'm checking the phrasing for -ing clause endings and need to rework that section about directional asymmetry. The current version ends with "establishing directional asymmetry" which violates the constraint, so I'll restructure it to say something like "At α=1.0, all 24/24 forward-direction pairs reach significance while 0/24 reverse pairs do, confirming directional asymmetry across WikiText conditions."

For the figure caption, I'm also revising "establishing a one-generation canary lead" to avoid the -ing ending—something like "Token entropy drops at generation 1; distinct-1 declines from generations 2–3, with a consistent one-generation canary lead across all four seeds" works better and keeps the flow intact.

Now I'm going through the remaining sections to check for any lingering -ing constructions: the compression language in §5.2, the pattern violation phrasing in §5.3, and the synthetic data training description in §5.4 all look clean. The taxonomy framing is solid too. I think I've caught the main issues, so I'm ready to write out the file.

Let me reconsider the figure captions though. For the metric trajectory figure, I want something compact that shows the one-generation canary lead at α=1.0 across the four seeds—my current version captures the token entropy drop at generation 1, the distinct-1 decline across generations 2-3, and notes the consistent lead with the inter-seed range shaded, plus the FDR significance counts. That's concise enough.

For the dose response figure, I'm describing the four regimes across contamination levels: the blind zone where detection fails, the onset threshold, the synchronous dip region, and the detection zone where the signal becomes reliable. Two sentences covers it well.

Now I need to finalize the Table 2 footnotes—pulling in the seed-dependent variation for specific conditions, the bfloat16 note about exceeding single-GPU capacity, the ECE-only canary result, and then the multi-seed model list with their seed counts and the single-seed models. That's a lot of detail to pack into footnotes, but it's all necessary context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b774285f-8c58-406d-a14b-3aa5dda46ccb",
  "isSidechain": false,
  "requestId": "req_011CbDhi144Nd7ok33BP7Jjo",
  "type": "assistant",
  "uuid": "58b5c3f0-bbbf-4a2a-8983-8487be7ca028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BnK3H5jf9s8crNi8rQL3q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23983,
      "cache_read_input_tokens": 27781,
      "output_tokens": 17123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17123,
          "cache_read_input_tokens": 27781,
          "cache_creation_input_tokens": 23983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23983
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T11:03:47.973Z_

Now I'll write the compressed section. Let me verify the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b5c3f0-bbbf-4a2a-8983-8487be7ca028",
  "isSidechain": false,
  "requestId": "req_011CbDhi144Nd7ok33BP7Jjo",
  "type": "assistant",
  "uuid": "ca360db3-c11e-4bce-be27-8d4ce7f1bea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BnK3H5jf9s8crNi8rQL3q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23983,
      "cache_read_input_tokens": 27781,
      "output_tokens": 17123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17123,
          "cache_read_input_tokens": 27781,
          "cache_creation_input_tokens": 23983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23983
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T11:03:48.180Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01256TdMhm2jN5ciF2VRmQ9G`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca360db3-c11e-4bce-be27-8d4ce7f1bea7",
  "isSidechain": false,
  "requestId": "req_011CbDhi144Nd7ok33BP7Jjo",
  "type": "assistant",
  "uuid": "60ba8545-bb27-451e-94ec-9aef3f87aded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BnK3H5jf9s8crNi8rQL3q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23983,
      "cache_read_input_tokens": 27781,
      "output_tokens": 17123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17123,
          "cache_read_input_tokens": 27781,
          "cache_creation_input_tokens": 23983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23983
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T11:03:48.345Z_

<details><summary>↩ Tool result · `toolu_01256TdMhm2jN5ciF2VRmQ9G`</summary>

```text
abstract.tex
appendix.tex
background.tex
conclusion.tex
discussion.tex
ethics.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60ba8545-bb27-451e-94ec-9aef3f87aded",
  "isSidechain": false,
  "promptId": "694508ff-a291-43df-9e7f-4abfbbd1deda",
  "type": "user",
  "uuid": "e8b233a6-09da-457f-81fe-9705f5368cef",
  "toolUseResult": {
    "stdout": "abstract.tex\nappendix.tex\nbackground.tex\nconclusion.tex\ndiscussion.tex\nethics.tex\nexperiments.tex\nfigures\nintroduction.tex\nlimitations.tex\nmain.aux\nmain.bbl\nmain.blg\nmain.fdb_latexmk\nmain.fls\nmain.log\nmain.out\nmain.pdf\nmain.tex\nmethod.tex\nreferences.bib\nrelated_work.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "60ba8545-bb27-451e-94ec-9aef3f87aded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "leafUuid": "e8b233a6-09da-457f-81fe-9705f5368cef",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Compress results section for EMNLP paper",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Tool call

_source line 22 · 2026-05-20T11:04:49.196Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CGkyp3oTFyF8cwMiBteU6Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
  "content": "\\subsection{Detection Phase Transition}\n\\label{sec:regime}\n\nDiversity collapse occurs at every contamination level: distinct-1 declines by $14.1\\%$ at $\\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\\pm}0.3\\%$ at $\\alpha{=}0.25$ (3-seed mean).\nDespite this ubiquitous degradation, causal detectability is sharply regime-dependent.\nPermutation Granger (PermG) tests find 0/8 canary$\\to$downstream pairs FDR-significant from $\\alpha{=}0.00$ through $\\alpha{=}0.45$, then jump to 6/8 at $\\alpha{=}0.50$ (2~fp32 seeds, consistent).\nThis transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\\alpha)^{10}$ yields $99.75\\%$ at $\\alpha{=}0.45$ versus $99.90\\%$ at $\\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.\nSigmoid regression across the 12-point $\\alpha$ grid quantifies this steep onset: $\\alpha_c = 0.476$ at $T{=}10$, steepness $k \\geq 200$, transition width $\\Delta\\alpha \\approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\\Delta\\mathrm{AIC} = 18.2$; Figure~\\ref{fig:phase_transition}).\nAt $\\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\\alpha_c$ at $T{=}10$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\nA specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.\n\nFirst-differencing scopes the canary claim precisely.\nCanary$\\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \\to 24/24$ across 4~seeds at $\\alpha{=}1.0$), while canary$\\to$perplexity collapses entirely ($F \\approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.\nAll canary claims are therefore scoped to diversity metrics only.\nAt $\\alpha{=}1.0$, 24/24 forward-direction pairs reach FDR significance with 0/24 reverse (4~seeds); directional asymmetry is robust across all WikiText conditions.\nThe canary mechanism also exhibits a blind spot: at $\\alpha{=}0.10$, distinct-1 has already dropped by $39.6\\%$, yet token entropy is indistinguishable from the null ($-5.3\\%$ versus $-4.6{\\pm}0.4\\%$ at $\\alpha{=}0.0$).\nBelow $\\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable causal signal in the canary metrics.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\n\\subsection{Dose-Response and the $S \\times R$ Framework}\n\\label{sec:dose_response}\n\nThe PermG dose-response profile (Figure~\\ref{fig:regime_map}) reveals four detection regimes: \\emph{blind} ($\\alpha \\leq 0.45$, 0/8 FDR-significant pairs), \\emph{onset} ($\\alpha \\approx 0.50$, 6/8), \\emph{synchronous dip} ($\\alpha \\approx 0.60$, s42: 3/8, s43: 0/8; dual-seed confirmed), and \\emph{detection} ($\\alpha \\geq 0.75$, 5--6/8 per seed across 3~seeds; $\\alpha{=}1.0$, 6/8 across 4~seeds).\nThe non-monotonic dip at $\\alpha{=}0.60$ is consistent with the $S \\times R$ framework (\\S\\ref{sec:theory}): signal strength $S(\\alpha)$ rises monotonically with contamination, but temporal resolution $R(\\alpha)$ drops when relaxation time approaches the observation interval.\nAt $\\alpha \\approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \\times R$ reaches a local minimum.\nThe synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.\n\nMethod choice is itself a major source of analytic variability.\nAt $\\alpha{=}1.0$, forward-direction significance rates range from 100\\% (naive cross-correlation) to 37.5\\% (PermG), with inter-method $\\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\\%.\nPermG is the only method that combines zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$ (Table~\\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.\nThe $S \\times R$ framework generates three testable predictions for $T{=}20$ via $\\mathrm{Power}(\\alpha, T) = \\Phi(S \\cdot R \\cdot \\sqrt{T}/\\sigma)$: (i)~$\\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\\alpha_c$ values.\nThese predictions are under empirical verification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\caption{PermG forward detection rate across 12 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\\alpha \\leq 0.45$, 0/8), onset ($\\alpha{=}0.50$, 6/8), synchronous dip ($\\alpha{=}0.60$, 0--3/8), and detection ($\\alpha \\geq 0.75$, 5--6/8).}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Forward-direction FDR significance rates (\\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr          & 75   & 12.5 & 37.5 & 87.5 & 0    & 75  \\\\\nDiff.\\ XCorr         & 0    & 37.5 & 87.5 & 75   & 75   & 0   \\\\\nThreshold ($3\\sigma$) & ---  & 0    & 50   & 0    & 0    & --- \\\\\nPerm.\\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\\\\nToda--Yamamoto       & ---  & 0    & 37.5 & 37.5 & 50   & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture Generalization}\n\\label{sec:generalization}\n\nWe evaluate the detection phase transition across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).\nTable~\\ref{tab:generalization} reports PermG forward detection at $\\alpha{=}1.0$.\nPermG forward significance reaches ${\\geq}$6/8 in 13 of 15 conditions (87\\%).\nTwo exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs reach significance while entropy$\\to$downstream pairs fail entirely (0/4; details in Appendix).\nSmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.\nThe onset boundary $\\alpha_c \\approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.\n\nReplacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.\nAt Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.\nDataset characteristics modulate detection power independently of model capacity.\nDirectional asymmetry also varies by domain: at $\\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.\nThis domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\\S\\ref{sec:discussion}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture PermG forward detection ($\\alpha{=}1.0$). Detection (${\\geq}$6/8) confirmed in 13/15 conditions (87\\%) across six model families, scales from 345M to 6.9B, and two domains.}\n\\label{tab:generalization}\n\\begin{tabular}{lrcl}\n\\toprule\nModel & Params & Domain & PermG fwd \\\\\n\\midrule\nPythia-410M    & 410M & Wiki & 6/8 \\\\\nPythia-1.4B    & 1.4B & Wiki & 2--6/8$^\\dagger$ \\\\\nPythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\\\\nGPT-2-medium   & 345M & Wiki & 6/8 \\\\\nOPT-1.3B       & 1.3B & Wiki & 6/8 \\\\\nQwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\\\\nSmolLM3-3B     & 3.0B & Wiki & 3/8$^\\ddagger$ \\\\\nPadding-410M   & 410M & Wiki & 6/8 \\\\\n\\addlinespace\nPythia-1B      & 1.0B & C4   & 7--8/8 \\\\\nPythia-1.4B    & 1.4B & C4   & 8/8 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^\\ddagger$ECE-only canary (entropy 0/4).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\\\\n\\multicolumn{4}{l}{\\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Others: single seed. Total: 15 combinations.} \\\\\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Canary-Based Early Intervention}\n\\label{sec:intervention}\n\nWe implement a predictive cessation protocol: training with synthetic data ($\\alpha{=}1.0$) continues until token entropy drops ${>}15\\%$ relative to generation~0, at which point $\\alpha$ switches to $0.0$ (pure real data).\nA reactive baseline triggers when distinct-1 drops ${>}10\\%$.\nThe predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).\nPeak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\\% reduction (bootstrap 95\\% CI: 29--64\\%).\nRecovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.\nBoth models converge to the $\\alpha{=}0.0$ baseline by generation~10.\n\nThe trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\\times$ scale gap from 410M to 1.4B, and the 15\\% entropy threshold generalizes without recalibration.\nThese results position canary-based detection within a four-layer taxonomy of collapse monitoring: (1)~dimensionality collapse, detectable at $\\alpha \\geq 0.10$ via $n$-gram diversity decline; (2)~distributional variance, detectable at $\\alpha \\geq 0.25$ via calibration drift; (3)~causal coupling, detectable at $\\alpha \\geq 0.50$ via Granger precedence; and (4)~dynamical stability, assessable at $\\alpha \\geq 0.50$ via lag structure.\nEach layer captures a distinct aspect of collapse, and lower layers activate at lower contamination thresholds.\nThe practical implication is that canary monitoring should combine multiple detection layers rather than rely on any single statistical test.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b233a6-09da-457f-81fe-9705f5368cef",
  "isSidechain": false,
  "requestId": "req_011CbDi7MMqPwzcDkHDUAaRo",
  "type": "assistant",
  "uuid": "6bd5406f-c5a4-4656-b6cd-7d08b0482104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JxUq5YuqCU6toVXfLUPFN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17207,
      "cache_read_input_tokens": 51764,
      "output_tokens": 4001,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4001,
          "cache_read_input_tokens": 51764,
          "cache_creation_input_tokens": 17207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17207
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T11:04:49.219Z_

<details><summary>↩ Tool result · `toolu_01CGkyp3oTFyF8cwMiBteU6Y`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bd5406f-c5a4-4656-b6cd-7d08b0482104",
  "isSidechain": false,
  "promptId": "694508ff-a291-43df-9e7f-4abfbbd1deda",
  "type": "user",
  "uuid": "b093805d-96f2-49d7-9b8b-998e2c047302",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
    "content": "\\subsection{Detection Phase Transition}\n\\label{sec:regime}\n\nDiversity collapse occurs at every contamination level: distinct-1 declines by $14.1\\%$ at $\\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\\pm}0.3\\%$ at $\\alpha{=}0.25$ (3-seed mean).\nDespite this ubiquitous degradation, causal detectability is sharply regime-dependent.\nPermutation Granger (PermG) tests find 0/8 canary$\\to$downstream pairs FDR-significant from $\\alpha{=}0.00$ through $\\alpha{=}0.45$, then jump to 6/8 at $\\alpha{=}0.50$ (2~fp32 seeds, consistent).\nThis transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\\alpha)^{10}$ yields $99.75\\%$ at $\\alpha{=}0.45$ versus $99.90\\%$ at $\\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.\nSigmoid regression across the 12-point $\\alpha$ grid quantifies this steep onset: $\\alpha_c = 0.476$ at $T{=}10$, steepness $k \\geq 200$, transition width $\\Delta\\alpha \\approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\\Delta\\mathrm{AIC} = 18.2$; Figure~\\ref{fig:phase_transition}).\nAt $\\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\\alpha_c$ at $T{=}10$ (\\S\\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.\nA specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.\n\nFirst-differencing scopes the canary claim precisely.\nCanary$\\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \\to 24/24$ across 4~seeds at $\\alpha{=}1.0$), while canary$\\to$perplexity collapses entirely ($F \\approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.\nAll canary claims are therefore scoped to diversity metrics only.\nAt $\\alpha{=}1.0$, 24/24 forward-direction pairs reach FDR significance with 0/24 reverse (4~seeds); directional asymmetry is robust across all WikiText conditions.\nThe canary mechanism also exhibits a blind spot: at $\\alpha{=}0.10$, distinct-1 has already dropped by $39.6\\%$, yet token entropy is indistinguishable from the null ($-5.3\\%$ versus $-4.6{\\pm}0.4\\%$ at $\\alpha{=}0.0$).\nBelow $\\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable causal signal in the canary metrics.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\n\\subsection{Dose-Response and the $S \\times R$ Framework}\n\\label{sec:dose_response}\n\nThe PermG dose-response profile (Figure~\\ref{fig:regime_map}) reveals four detection regimes: \\emph{blind} ($\\alpha \\leq 0.45$, 0/8 FDR-significant pairs), \\emph{onset} ($\\alpha \\approx 0.50$, 6/8), \\emph{synchronous dip} ($\\alpha \\approx 0.60$, s42: 3/8, s43: 0/8; dual-seed confirmed), and \\emph{detection} ($\\alpha \\geq 0.75$, 5--6/8 per seed across 3~seeds; $\\alpha{=}1.0$, 6/8 across 4~seeds).\nThe non-monotonic dip at $\\alpha{=}0.60$ is consistent with the $S \\times R$ framework (\\S\\ref{sec:theory}): signal strength $S(\\alpha)$ rises monotonically with contamination, but temporal resolution $R(\\alpha)$ drops when relaxation time approaches the observation interval.\nAt $\\alpha \\approx 0.60$, this compression drives the canary-to-downstream lag toward zero, and the product $S \\times R$ reaches a local minimum.\nThe synchronous zone is mechanistically distinct from the blind spot: in the blind zone, canary drift is indistinguishable from the null; in the synchronous zone, both canary and downstream metrics drift substantially but without temporal offset.\n\nMethod choice is itself a major source of analytic variability.\nAt $\\alpha{=}1.0$, forward-direction significance rates range from 100\\% (naive cross-correlation) to 37.5\\% (PermG), with inter-method $\\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\\%.\nPermG is the only method that combines zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$ (Table~\\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.\nThe $S \\times R$ framework generates three testable predictions for $T{=}20$ via $\\mathrm{Power}(\\alpha, T) = \\Phi(S \\cdot R \\cdot \\sqrt{T}/\\sigma)$: (i)~$\\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\\alpha_c$ values.\nThese predictions are under empirical verification.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\caption{PermG forward detection rate across 12 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\\alpha \\leq 0.45$, 0/8), onset ($\\alpha{=}0.50$, 6/8), synchronous dip ($\\alpha{=}0.60$, 0--3/8), and detection ($\\alpha \\geq 0.75$, 5--6/8).}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Forward-direction FDR significance rates (\\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves zero null-control FPR with consistent detection at $\\alpha \\geq 0.50$.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr          & 75   & 12.5 & 37.5 & 87.5 & 0    & 75  \\\\\nDiff.\\ XCorr         & 0    & 37.5 & 87.5 & 75   & 75   & 0   \\\\\nThreshold ($3\\sigma$) & ---  & 0    & 50   & 0    & 0    & --- \\\\\nPerm.\\ Granger       & 0    & 0    & 75   & 75   & 75   & 0   \\\\\nToda--Yamamoto       & ---  & 0    & 37.5 & 37.5 & 50   & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture Generalization}\n\\label{sec:generalization}\n\nWe evaluate the detection phase transition across 15 model-seed combinations spanning six families (Pythia, GPT-2, OPT, Qwen, SmolLM3, Padding-variant), scales from 345M to 6.9B parameters, and two training domains (WikiText-103, C4).\nTable~\\ref{tab:generalization} reports PermG forward detection at $\\alpha{=}1.0$.\nPermG forward significance reaches ${\\geq}$6/8 in 13 of 15 conditions (87\\%).\nTwo exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs reach significance while entropy$\\to$downstream pairs fail entirely (0/4; details in Appendix).\nSmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.\nThe onset boundary $\\alpha_c \\approx 0.50$ at $T{=}10$ is architecture-independent: every family that achieves detection does so at or above this threshold, and none achieves reliable detection below it.\n\nReplacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.\nAt Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.\nDataset characteristics modulate detection power independently of model capacity.\nDirectional asymmetry also varies by domain: at $\\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.\nThis domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\\S\\ref{sec:discussion}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture PermG forward detection ($\\alpha{=}1.0$). Detection (${\\geq}$6/8) confirmed in 13/15 conditions (87\\%) across six model families, scales from 345M to 6.9B, and two domains.}\n\\label{tab:generalization}\n\\begin{tabular}{lrcl}\n\\toprule\nModel & Params & Domain & PermG fwd \\\\\n\\midrule\nPythia-410M    & 410M & Wiki & 6/8 \\\\\nPythia-1.4B    & 1.4B & Wiki & 2--6/8$^\\dagger$ \\\\\nPythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\\\\nGPT-2-medium   & 345M & Wiki & 6/8 \\\\\nOPT-1.3B       & 1.3B & Wiki & 6/8 \\\\\nQwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\\\\nSmolLM3-3B     & 3.0B & Wiki & 3/8$^\\ddagger$ \\\\\nPadding-410M   & 410M & Wiki & 6/8 \\\\\n\\addlinespace\nPythia-1B      & 1.0B & C4   & 7--8/8 \\\\\nPythia-1.4B    & 1.4B & C4   & 8/8 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Seed-dependent (s42: 2/8, s43: 6/8).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^*$bf16 (exceeds single-GPU fp32 capacity).} \\\\\n\\multicolumn{4}{l}{\\footnotesize $^\\ddagger$ECE-only canary (entropy 0/4).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\\\\n\\multicolumn{4}{l}{\\footnotesize GPT-2-med, OPT-1.3B, Pythia-1B C4 (2 seeds each).} \\\\\n\\multicolumn{4}{l}{\\footnotesize Others: single seed. Total: 15 combinations.} \\\\\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Canary-Based Early Intervention}\n\\label{sec:intervention}\n\nWe implement a predictive cessation protocol: training with synthetic data ($\\alpha{=}1.0$) continues until token entropy drops ${>}15\\%$ relative to generation~0, at which point $\\alpha$ switches to $0.0$ (pure real data).\nA reactive baseline triggers when distinct-1 drops ${>}10\\%$.\nThe predictive trigger fires at generation~1 in both Pythia-410M and Pythia-1.4B (s42 fp32), one generation before the reactive baseline (generation~2).\nPeak perplexity under predictive intervention is $56.99$ versus $157.09$ under reactive (s42 fp32), a 58\\% reduction (bootstrap 95\\% CI: 29--64\\%).\nRecovery occurs at generation~2 under predictive cessation versus generation~4 under reactive.\nBoth models converge to the $\\alpha{=}0.0$ baseline by generation~10.\n\nThe trigger generation, recovery timeline, and convergence behavior are identical across the $3.4\\times$ scale gap from 410M to 1.4B, and the 15\\% entropy threshold generalizes without recalibration.\nThese results position canary-based detection within a four-layer taxonomy of collapse monitoring: (1)~dimensionality collapse, detectable at $\\alpha \\geq 0.10$ via $n$-gram diversity decline; (2)~distributional variance, detectable at $\\alpha \\geq 0.25$ via calibration drift; (3)~causal coupling, detectable at $\\alpha \\geq 0.50$ via Granger precedence; and (4)~dynamical stability, assessable at $\\alpha \\geq 0.50$ via lag structure.\nEach layer captures a distinct aspect of collapse, and lower layers activate at lower contamination thresholds.\nThe practical implication is that canary monitoring should combine multiple detection layers rather than rely on any single statistical test.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "6bd5406f-c5a4-4656-b6cd-7d08b0482104",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T11:04:52.524Z_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the file was written correctly by reading it back, and also do a quick constraint check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b093805d-96f2-49d7-9b8b-998e2c047302",
  "isSidechain": false,
  "requestId": "req_011CbDiBqkFTkqw1gU2QmQka",
  "type": "assistant",
  "uuid": "88267fca-5a6f-4922-aebf-d5253ac7cfcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKFUivvv6Pf2JMPoP96k5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4058,
      "cache_read_input_tokens": 68971,
      "output_tokens": 647,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 647,
          "cache_read_input_tokens": 68971,
          "cache_creation_input_tokens": 4058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T11:04:52.531Z_

Let me verify constraint compliance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88267fca-5a6f-4922-aebf-d5253ac7cfcf",
  "isSidechain": false,
  "requestId": "req_011CbDiBqkFTkqw1gU2QmQka",
  "type": "assistant",
  "uuid": "d01393d9-c944-4e33-99a5-9defe0c05636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKFUivvv6Pf2JMPoP96k5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4058,
      "cache_read_input_tokens": 68971,
      "output_tokens": 647,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 647,
          "cache_read_input_tokens": 68971,
          "cache_creation_input_tokens": 4058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T11:05:02.300Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AWVFN7Rs7bRgQyd32uxp4q`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex\" && echo \"=== Line count ===\" && wc -l \"$FILE\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$FILE\" || echo \"No em-dashes found\" && echo \"=== Explanatory en-dash check ===\" && grep -n \" – \" \"$FILE\" || echo \"No explanatory en-dashes found\" && echo \"=== -ing clause endings ===\" && grep -n \"ing\\.\" \"$FILE\" | grep -v \"\\\\\\\\begin\\|\\\\\\\\end\\|first-differenc\\|train\\|Perm\\.\\|Pad\\|Threshold\\|onset\\|spring\\|string\" | head -10 && echo \"=== Forbidden words ===\" && grep -in \"near-discontinuous\\|notably\\|interestingly\\|furthermore\\|moreover\\|additionally\\|leverage\\|utilize\\|delve\\|facilitate\\|myriad\\|plethora\\|it is worth noting\" \"$FILE\" || echo \"None found\" && echo \"=== confirms/validates with theory ===\" && grep -in \"confirms\\|validates\" \"$FILE\" || echo \"None found\" && echo \"=== CSD check ===\" && grep -in \"CSD\\|critical slowing\" \"$FILE\" || echo \"None found\" && echo \"=== TY=7/8 check ===\" && grep -n \"7/8\" \"$FILE\" | grep -i \"toda\\|TY\\|yamamoto\" || echo \"No TY 7/8\" && echo \"=== K>=3 in Table 2 ===\" && sed -n '/tab:generalization/,/end{table}/p' \"$FILE\" | grep -i \"K\\|consensus\" || echo \"No K>=3 in generalization table\" && echo \"=== \\\\section{Experiments} check ===\" && grep -n \"\\\\\\\\section{Experiments}\" \"$FILE\" || echo \"No section Experiments\" && echo \"=== \\\\subsection{Experimental Setup} check ===\" && grep -n \"\\\\\\\\subsection{Experimental Setup}\" \"$FILE\" || echo \"No Experimental Setup\"",
  "description": "Verify constraint compliance in generated file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01393d9-c944-4e33-99a5-9defe0c05636",
  "isSidechain": false,
  "requestId": "req_011CbDiBqkFTkqw1gU2QmQka",
  "type": "assistant",
  "uuid": "cca4cfdc-908d-4808-ae87-6d73282d6a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SKFUivvv6Pf2JMPoP96k5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4058,
      "cache_read_input_tokens": 68971,
      "output_tokens": 647,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 647,
          "cache_read_input_tokens": 68971,
          "cache_creation_input_tokens": 4058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4058
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T11:05:02.452Z_

<details><summary>↩ Tool result · `toolu_01AWVFN7Rs7bRgQyd32uxp4q`</summary>

```text
=== Line count ===
127 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
=== Em-dash check ===
No em-dashes found
=== Explanatory en-dash check ===
No explanatory en-dashes found
=== -ing clause endings ===
=== Forbidden words ===
None found
=== confirms/validates with theory ===
10:A specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.
=== CSD check ===
None found
=== TY=7/8 check ===
No TY 7/8
=== K>=3 in Table 2 ===
Two exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\to$downstream pairs reach significance while entropy$\to$downstream pairs fail entirely (0/4; details in Appendix).
SmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.
Replacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.
At Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.
Directional asymmetry also varies by domain: at $\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.
This domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\S\ref{sec:discussion}).
Pythia-410M    & 410M & Wiki & 6/8 \\
Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
Pythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\
GPT-2-medium   & 345M & Wiki & 6/8 \\
OPT-1.3B       & 1.3B & Wiki & 6/8 \\
Qwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\
SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
Padding-410M   & 410M & Wiki & 6/8 \\
\multicolumn{4}{l}{\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\
=== \section{Experiments} check ===
No section Experiments
=== \subsection{Experimental Setup} check ===
No Experimental Setup
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cca4cfdc-908d-4808-ae87-6d73282d6a3d",
  "isSidechain": false,
  "promptId": "694508ff-a291-43df-9e7f-4abfbbd1deda",
  "type": "user",
  "uuid": "b78ebba2-9cc8-4d9e-8fe9-eb9cb704187b",
  "toolUseResult": {
    "stdout": "=== Line count ===\n127 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex\n=== Em-dash check ===\nNo em-dashes found\n=== Explanatory en-dash check ===\nNo explanatory en-dashes found\n=== -ing clause endings ===\n=== Forbidden words ===\nNone found\n=== confirms/validates with theory ===\n10:A specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.\n=== CSD check ===\nNone found\n=== TY=7/8 check ===\nNo TY 7/8\n=== K>=3 in Table 2 ===\nTwo exceptions emerge: Pythia-1.4B seed~42 on WikiText (2/8), a seed-dependent outlier that recovers to 6/8 in seed~43, and SmolLM3-3B (3/8), where only ECE$\\to$downstream pairs reach significance while entropy$\\to$downstream pairs fail entirely (0/4; details in Appendix).\nSmolLM3's token entropy exhibits non-monotonic oscillations across generations; this pattern violates the monotonic decline that Granger tests require.\nReplacing WikiText-103 with C4 yields the strongest detection observed: Pythia-1B reaches PermG~fwd 8/8 (2~seeds), and Pythia-1.4B reaches 8/8 on C4 versus 2/8 on WikiText at the same scale.\nAt Pythia-6.9B (bf16), detection recovers to 7/8 on WikiText.\nDirectional asymmetry also varies by domain: at $\\alpha{=}0.50$ on C4, PermG reverse reaches 7/8, compared to 0/24 across all WikiText conditions.\nThis domain-dependent bidirectionality suggests that the unidirectional forward causation observed on WikiText may partly reflect domain-specific dynamics (\\S\\ref{sec:discussion}).\nPythia-410M    & 410M & Wiki & 6/8 \\\\\nPythia-1.4B    & 1.4B & Wiki & 2--6/8$^\\dagger$ \\\\\nPythia-6.9B    & 6.9B & Wiki & 7/8$^*$ \\\\\nGPT-2-medium   & 345M & Wiki & 6/8 \\\\\nOPT-1.3B       & 1.3B & Wiki & 6/8 \\\\\nQwen3.5-0.8B   & 0.8B & Wiki & 8/8 \\\\\nSmolLM3-3B     & 3.0B & Wiki & 3/8$^\\ddagger$ \\\\\nPadding-410M   & 410M & Wiki & 6/8 \\\\\n\\multicolumn{4}{l}{\\footnotesize Multi-seed (range shown): Pythia-410M, -1.4B Wiki,} \\\\\n=== \\section{Experiments} check ===\nNo section Experiments\n=== \\subsection{Experimental Setup} check ===\nNo Experimental Setup",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cca4cfdc-908d-4808-ae87-6d73282d6a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "leafUuid": "b78ebba2-9cc8-4d9e-8fe9-eb9cb704187b",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Compress results section for EMNLP paper",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Assistant

_source line 30 · 2026-05-20T11:05:25.730Z_

<details><summary>Logged reasoning block</summary>

```text
The "confirms" on line 10 is about the spec curve confirming the phase transition is specification-invariant, not about confirming/validating Power Theory. The D141 constraint says "Power Theory: 'consistent with' (NEVER 'confirms'/'validates')". The spec curve confirmation is about the data, not about the theory. So this is fine.

The K≥3 check in Table 2 actually matched prose from §5.3 (not the table itself), which is fine since the constraint M037 says "K≥3 column NOT in Table 2". The table itself has only 4 columns: Model, Params, Domain, PermG fwd. No K≥3 column. ✓


The grep results picked up prose surrounding the generalization table rather than the table content itself—the actual columns are Model, Params, Domain, and PermG fwd, with no K≥3 present.

Now I'm doing a more careful count of the actual sentences across the sections. Section 5.1 has about 13 sentences total split between two paragraphs, and section 5.2 appears to have around 9 sentences, though I should verify that count since it seems lower than expected. I'm verifying that §5.2 P1 has enough content despite only having 4 sentences—each one is densely packed with information, so it should work within the compression constraints, and the overall structure checks out across all sections and floats.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b78ebba2-9cc8-4d9e-8fe9-eb9cb704187b",
  "isSidechain": false,
  "requestId": "req_011CbDiCpEzNY7j7syLCpKiM",
  "type": "assistant",
  "uuid": "232f4bc7-58e8-4445-b48c-d7869bcb06c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GseiSYzeHBHM1uaz9KHPhg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 73029,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 73029,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1451
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-20T11:05:28.240Z_

All constraints pass. The "confirms" on line 10 refers to the spec curve confirming the phase transition is specification-invariant (empirical data, not Power Theory), so D141 is satisfied.

Written to `docs/paper/experiments_reframe.tex`: 127 lines total (4 subsections, ~70 lines of prose, 2 figure floats, 2 compact tables). All active constraints verified clean: no em-dashes, no -ing clause endings, no forbidden words, no CSD data, no TY=7/8, no K>=3 in Table 2, "consistent with" for all theory references, "steep onset"/"detection phase transition" throughout, all $\alpha_c$ mentions include "at $T{=}10$", fp32 main axis with bf16 only in Pythia-6.9B footnote.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "232f4bc7-58e8-4445-b48c-d7869bcb06c2",
  "isSidechain": false,
  "requestId": "req_011CbDiCpEzNY7j7syLCpKiM",
  "type": "assistant",
  "uuid": "47748d4a-d916-4476-baa2-bbf89b00fe91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GseiSYzeHBHM1uaz9KHPhg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 73029,
      "output_tokens": 1088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1088,
          "cache_read_input_tokens": 73029,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1451
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "leafUuid": "47748d4a-d916-4476-baa2-bbf89b00fe91",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Compress results section for EMNLP paper",
  "sessionId": "73842314-3ca4-45a0-a352-92fd62b21080"
}
```

---
