# paper figures 3 4

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures-3-4_20260522T211221_result.json`
- **Structured JSON:** [`fa1ca5f6596fd0b0ab19.json`](../../sessions/fa/fa1ca5f6596fd0b0ab19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图都修复完成，验证通过：

**Fig 3 — Aggregation Gradient**
- Majority/Weighted/Threshold 的 K_eff β 以正值为主（红点），Bayesian 明显反转为负值（蓝点，1+ 6−）
- Legend 移至右上角，不再遮挡标注
- 每组标注 η 和 K 的 FDR 显著性计数

**Fig 4 — Panel Design**
- min(η_max) 在 10/12 conditions 下 ASR ≈ 0（簇集在底部），显著低于 Random 和 max(K_eff)
- 2 个 position_bias 离群值（~0.47）诚实展示，但 min(η_max) 仍为最低
- 箭头正确指向主簇而非离群值

输出文件：
- 服务器: `/root/cert_manip_resist_eval/artifacts/figures/fig{3,4}_*.{pdf,png}`
- 本地: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/figures/`

---
