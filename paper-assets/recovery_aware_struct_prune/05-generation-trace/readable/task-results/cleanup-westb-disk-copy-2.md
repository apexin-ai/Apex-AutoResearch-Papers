# cleanup westb disk

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_westb_disk_20260522T113449_result.json`
- **Structured JSON:** [`6ee0c01f5b1aa1da6062.json`](../../sessions/6e/6ee0c01f5b1aa1da6062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 清理前 ===
磁盘使用: 250G / 250G (100%)

=== 清理后 ===
磁盘使用: 222G / 250G (89%)
释放空间: ~28G

=== 剩余大目录 (top 20) ===
38G   grpo_qwen_math_cka_only_20
12G   grpo_cka_only_20
12G   grpo_cka_only_20_seed123
12G   pruned_cka_only_20_qwen_math
12G   pruned_rasp_alpha3p0_20
12G   pruned_rasp_rlvr_20
12G   pruned_standard_20_qwen_math
12G   sft_cka_only_20
12G   sft_qwen_math_cka_only_20_final
12G   sft_rasp_alpha3p0_20
12G   sft_rasp_rlvr_20
12G   sft_standard_20_qwen_math_final
11G   pruned_standard_25
3.4G  models
2.9G  grpo_alpha4_20_eval
2.8G  grpo_cka_only_20_1p5b
2.8G  grpo_rasp_20_1p5b
2.8G  grpo_standard_20_1p5b
2.8G  pruned_cka_only_20_1p5b
2.8G  pruned_rasp_20_1p5b
```

释放 28G，可用空间从 3.3M 恢复到 29G。

---
