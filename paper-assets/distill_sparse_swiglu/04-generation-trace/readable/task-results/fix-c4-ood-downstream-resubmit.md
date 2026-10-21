# fix c4 ood downstream resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c4_ood_downstream_resubmit_20260520T124042_result.json`
- **Structured JSON:** [`23a6f663e2cd74731504.json`](../../sessions/23/23a6f663e2cd74731504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。PID 254228 在 westd-41718:cuda:1 上，arc_challenge 已进行到 ~46%（540/1172），正在使用离线 cache。

- **PID**: 254228
- **GPU**: westd-41718 cuda:1
- **日志**: `/root/distill_sparse_swiglu/logs/c4_ood_downstream_kl30.log`
- **修复**: `HF_HUB_OFFLINE=1` + `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1`，datasets 全部从 `/root/autodl-tmp/.hf_cache/datasets/` 离线加载
- **Sparsity**: uniform 0.3，model-level 实际 0.295
- **6 tasks**: arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa

---
