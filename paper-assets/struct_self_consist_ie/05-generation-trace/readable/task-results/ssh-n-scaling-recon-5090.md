# ssh n scaling recon 5090

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n_scaling_recon_5090_20260522T033240_result.json`
- **Structured JSON:** [`d8986e2a0c52ceb8c715.json`](../../sessions/d8/d8986e2a0c52ceb8c715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

侦察完成。

```
GPU_STATUS: 4x RTX 5090 (32GB), 全部空闲 (32110/32607 MiB free)
DISK: 24G 可用 (/root/autodl-tmp, 250G total, 91% used)

SCIERC_MODEL_PATH: /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2
CONLL_MODEL_PATH:  /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged
TOKENIZER_OK: 是（两个 checkpoint 均有 tokenizer_config.json + config.json）

SCIERC_DATA: /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data/test.json
             100 documents（load_scierc 按 sentence 展开为 instances）
CONLL_DATA:  /root/autodl-tmp/struct_self_consist_ie/data/conll2003/test.json
             3453 instances

SCIERC_DATASET_NAME: scierc   (--dataset scierc --data_dir .../data/scierc/processed_data)
CONLL_DATASET_NAME:  conll2003 (--dataset conll2003 --data_dir .../data/conll2003)
```

---
