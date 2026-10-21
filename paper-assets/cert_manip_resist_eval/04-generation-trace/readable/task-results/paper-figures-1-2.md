# paper figures 1 2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures-1-2_20260522T210456_result.json`
- **Structured JSON:** [`2c2a94d92cc6172a181f.json`](../../sessions/2c/2c2a94d92cc6172a181f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图都已完成，质量检查通过：

**Fig 1** — Robustness Comparison:
- Grouped bar chart，η_max vs K_eff 在 4 种校正方法下的 FDR 显著 condition 数
- η_max 在所有方法下均保持多数显著（5-11/12），K_eff 在 robust 方法下急剧下降（0-3/12）
- Wild Bootstrap† 和 Clustered SE† 标注为 recommended

**Fig 2** — GAM K_eff 6:6 Split:
- Diverging bar chart，12 conditions 按 K_eff 效应大小排列
- 正向 6 条（蓝，targeted attacks: prompt injection, score manipulation, position bias）— diversity harmful
- 负向 6 条（橙，shared-bias attacks: sycophancy, verbosity bias, authority bias）— diversity protective
- 所有效应在 GAM 中 FDR 显著

文件位置：
- 服务器: `/root/cert_manip_resist_eval/artifacts/figures/fig{1,2}_*.{pdf,png}`
- 本地: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/figures/`

---
