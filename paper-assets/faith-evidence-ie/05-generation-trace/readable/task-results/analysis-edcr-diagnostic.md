# analysis edcr diagnostic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_diagnostic_20260515T234346_result.json`
- **Structured JSON:** [`2115cc0497c43109a904.json`](../../sessions/21/2115cc0497c43109a904.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EDCR diagnostic 完成。14 个方法全部成功分析，registry 已更新为 DONE。

**结果摘要（viable methods, rel_f1>0.4）：**

| Method | rel_f1 | evi_f1 | EDCR |
|---|---|---|---|
| **GRPO bf16 ckpt100** | 0.4549 | 0.8086 | **0.6318** (最低) |
| RSFT-CED s44 | 0.4655 | 0.8087 | 0.6350 |
| RSFT-CED s43 | 0.4683 | 0.8156 | 0.6388 |
| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 |
| RSFT-CED s42 | 0.4449 | 0.8187 | 0.6565 |
| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 (最高) |

GRPO bf16 ckpt100 的 EDCR 最低（0.6318）且 per-doc std 最小（0.2743），evidence 质量最稳定。SFT no-evidence 的 EDCR=0 符合预期（无 evidence 输出）。DPO-CED 1ep / RSFT-flatNLI s43 / GRPO QLoRA lr5e6 的 EDCR≈1.0 是因为 rel_f1<0.02，模型退化导致几乎所有 citation 都是 distractor。

---
