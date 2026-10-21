# ssh check unstructured checkpoint

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_unstructured_checkpoint_20260520T183210_result.json`
- **Structured JSON:** [`afc555bf95283634dd23.json`](../../sessions/af/afc555bf95283634dd23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**不存在 Unstructured 20% SFT checkpoint。**

westb-23072 上 `/root/autodl-tmp/recovery_aware_struct_prune/` 下没有任何包含 `unstruct` 的目录。`random` 相关只有一个 `grpo_random_20`（GRPO，非 SFT）。

所有 `sft_*` 目录：

| 目录 | 说明 |
|------|------|
| `sft_standard_25` | Standard 25% |
| `sft_rasp_rlvr_20` | RASP+RLVR 20% |
| `sft_cka_only_20` | CKA-only 20% |
| `sft_standard_20_1p5b` | Standard 20% (1.5B) |
| `sft_cka_only_20_1p5b` | CKA-only 20% (1.5B) |
| `sft_rasp_20_1p5b` | RASP 20% (1.5B) |
| `sft_qwen_math_cka_only_20` | Qwen-Math CKA-only 20% |
| `sft_standard_20_qwen_math` | Qwen-Math Standard 20% |
| `sft_qwen_math_cka_only_20_final` | Qwen-Math CKA-only 20% (final) |
| `sft_standard_20_qwen_math_final` | Qwen-Math Standard 20% (final) |

如需 Unstructured 20% baseline，需要新建剪枝+SFT 流程。

---
