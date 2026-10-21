# investigate exp 018 provenance

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_exp_018_provenance_20260515T060431_result.json`
- **Structured JSON:** [`15ce34c4fb1c6ec5be1e.json`](../../sessions/15/15ce34c4fb1c6ec5be1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心发现：

**溯源结论**：
- **exp_018_qwen_scierc_seed456** — 新推理（今天 13:08，有 run.log 确认）
- **exp_018_qwen_scierc_seed123** — 新推理（无先前 Qwen seed123 数据，缺 run.log）
- **exp_018_llama_scierc_seed456** — **复制自 exp_007_llama_seed456**（MD5 完全一致，run.log 显示输出路径为 exp_007）
- **exp_018_llama_scierc_seed123** — 新推理（MD5 与 exp_007_llama_seed123 不同，指标也不同，缺 run.log）

**3-seed ρ 排序**（mean）：
- Qwen: voting_conf (0.394) > SJ (0.364) > EM (0.310) > FK (0.254) > logprob (0.217)
- LLaMA: voting_conf (0.422) > SJ (0.362) > FK (0.309) > EM (0.303) > logprob (0.190)

**3-seed AUROC 排序**（mean）：
- 两个模型一致：EM (0.76) > voting_conf/SJ (0.70–0.72) > FK (0.63–0.67) > logprob (0.57–0.60)

LLaMA 跨 seed 方差普遍小于 Qwen，信号稳定性更好。完整数据表在报告中。

---
