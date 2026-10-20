# search 4b sft multi seed adapters

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_search_4b_sft_multi_seed_adapters_20260521T152912_result.json`
- **Structured JSON:** [`6f7523ae3a95c73ae368.json`](../../sessions/6f/6f7523ae3a95c73ae368.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seeds confirmed. Here are the results:

```
4B SFT s42: /root/autodl-tmp/sft_output              (seed=42 confirmed)
4B SFT s43: /root/autodl-tmp/sft_output_seed43        (seed=43 confirmed)
4B SFT s44: /root/autodl-tmp/sft_output_seed44        (seed=44 confirmed)
```

All three adapters share identical configs:
- **base_model**: `/root/autodl-tmp/models/Qwen3-4B`
- **LoRA**: r=64, alpha=128, dropout=0.05, CAUSAL_LM
- **target_modules**: q/k/v/o_proj, gate/up/down_proj
- **epochs**: 3, total steps: 144, checkpoints at step 96 and 144

Best checkpoint metrics:
| Seed | Best step | Best metric |
|------|-----------|-------------|
| 42   | 144       | 0.7201      |
| 43   | 96        | 0.7468      |
| 44   | 96        | 0.7464      |

---
