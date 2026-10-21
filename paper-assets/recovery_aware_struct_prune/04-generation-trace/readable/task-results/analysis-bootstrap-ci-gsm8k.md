# analysis bootstrap ci gsm8k

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_gsm8k_20260520T055637_result.json`
- **Structured JSON:** [`8f62bc99a515aac73762.json`](../../sessions/8f/8f62bc99a515aac73762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260520_5e4fb8`). 结果汇总：

### Bootstrap 95% CI（18 个模型）

**7B @20%** — CKA-only GRPO 最高：64.37% [61.71, 66.94]，两个 seed 一致（s123=64.22%）。Standard GRPO 59.44%，RASP GRPO 60.88%，ShortGPT GRPO 43.37%。

**7B @25%** — Standard GRPO 51.10%，RASP GRPO 53.15%。CKA-only GRPO 25% 文件缺失。

**1.5B @20%** — CKA-only 远超其他：SFT 35.63% vs Standard 22.90% / RASP 26.91%。

### McNemar's Test（10 对比较）

| 比较 | p-value | 显著性 |
|------|---------|--------|
| CKA-only vs Standard GRPO 7B@20% | 0.0009 | *** |
| CKA-only vs RASP GRPO 7B@20% | 0.0200 | * |
| CKA-only vs ShortGPT GRPO 7B@20% | <0.001 | *** |
| CKA-only vs Standard SFT 7B@20% | 0.0022 | ** |
| RASP vs Standard GRPO 7B@20% | 0.3487 | n.s. |
| Dense vs CKA-only GRPO 7B@20% | <0.001 | *** |
| 1.5B 全部 4 组 CKA-only vs others | <0.001 | *** |

关键发现：CKA-only 在所有比较中显著优于 Standard/RASP/ShortGPT（p<0.05）。RASP vs Standard 差异不显著（p=0.35）。缺失 CKA-only GRPO 7B@25% 文件，无法完成该组对比。

---
