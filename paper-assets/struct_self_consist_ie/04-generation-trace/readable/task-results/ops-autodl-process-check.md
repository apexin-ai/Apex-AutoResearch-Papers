# ops autodl process check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_autodl_process_check_20260514T142740_result.json`
- **Structured JSON:** [`db61cfc53e26c7483335.json`](../../sessions/db/db61cfc53e26c7483335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新，报告已写入。总结：

**exp_007_llama_inference** (LLaMA-3.1-8B, SciERC joint):
- NER greedy F1=0.660, RE greedy F1=0.434
- NER structural > surface ✅，RE structural < surface ❌
- Verdict: **FAIL** — RE ρ_sj_full=0.299 未达 0.40 阈值，41% RE 样本 F1=0

**exp_003_wnut17_eval** (Qwen3-8B, WNUT17 NER):
- Greedy F1=0.523, oracle headroom +0.141
- Verdict: **FAIL** — structural 未胜出，53.7% 样本 F1=0，logprob full ρ 为负
- 46.5% 实例 gold-empty 被过滤，有效评估只有 689 条

两个实验共同问题：**T=1.0 采样过热**，大量样本 F1=0。建议 T=0.7 重试。

---
