# ops fig asr violin

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig-asr-violin_20260525T150501_result.json`
- **Structured JSON:** [`564167211a8b09a99e18.json`](../../sessions/56/564167211a8b09a99e18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出文件：
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures/fig_asr_distribution.pdf`
- **PNG**: 同目录 `fig_asr_distribution.png`
- **脚本**: 同目录 `gen_fig_asr_distribution.py`

关键发现：
- Position Bias ASR 最高（~0.49），增加 K 几乎不降低 — 说明 position bias 是系统性的，多数模型共享该偏好
- Prompt Injection 分布最宽（K=3 时 0.003–0.73），K 增大显著压缩方差
- Score Manipulation / Verbosity / Authority / Sycophancy 的 ASR 均 <0.1，K↑ 趋势稳定下降

---
