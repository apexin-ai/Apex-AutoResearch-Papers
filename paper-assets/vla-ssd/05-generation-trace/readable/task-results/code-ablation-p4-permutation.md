# code ablation p4 permutation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_p4_permutation_20260516T085748_result.json`
- **Structured JSON:** [`ad1ec844217486dd9be0.json`](../../sessions/ad/ad1ec844217486dd9be0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

| Layer | Observed RSA | Null Mean | Null Max | p-value |
|-------|-------------|-----------|----------|---------|
| 0 | 0.612 | 0.001 | 0.081 | 0.000 *** |
| 8 | 0.619 | -0.000 | 0.092 | 0.000 *** |
| 12 | 0.628 | -0.001 | 0.098 | 0.000 *** |
| 24 | 0.546 | 0.001 | 0.095 | 0.000 *** |
| 32 | 0.422 | 0.000 | 0.104 | 0.000 *** |

所有 5 个层的 observed RSA 均远超 null distribution 最大值（observed 最低 0.42 vs null max 0.10），p < 0.001。Observed 值与原始 unified_rsa_results 完全一致。

脚���：`/root/vla-ssd/scripts/ablations/rsa_permutation_null.py`
结果：`/root/autodl-tmp/vla-ssd/results/ablations/rsa_permutation_null.json`

---
