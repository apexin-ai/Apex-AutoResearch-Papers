# code exp44 investigate

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp44_investigate_20260522T053303_result.json`
- **Structured JSON:** [`7139cf9ca93c3de6e22e.json`](../../sessions/71/7139cf9ca93c3de6e22e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

47/50 now. Here's the report:

---

## exp44 Investigation Report

### 1. Llama conversations status
| Family | Count | Path |
|--------|-------|------|
| FITD | **47/50** (actively generating, PID 26918) | `data/cross_llm/fitd_llama.jsonl` |
| DD | 50 | `data/cross_llm/dd_llama.jsonl` |
| AA | 50 | `data/cross_llm/aa_llama.jsonl` |
| Crescendo | 251 | `data/llama_conversations/crescendo_jailbreak_llama.jsonl` |
| Benign | 250 | `data/llama_conversations/benign_llama_250.jsonl` |

PID 26918 is **still alive** and actively writing FITD data (~1 conv every 2-3 min). It should finish the remaining 3 within ~10 minutes.

### 2. Llama model
Downloaded at `/root/autodl-tmp/hf_cache/meta-llama/Llama-3.1-8B-Instruct/`. Currently loaded by PID 26918 using 18GB on GPU 0.

### 3. Script ready?
Yes. `scripts/exp44_full_pipeline.py` (1025 lines) is uploaded and verified:
- All imports pass
- Syntax compiles cleanly
- Both DeBERTa and Llama model paths verified

### 4. Exact run command
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/persuasion_turn_jailbreak_detect && CUDA_VISIBLE_DEVICES=0 python scripts/exp44_full_pipeline.py
```

**Important**: PID 26918 is still using GPU 0. Wait for it to finish (or kill it — the FITD data is already saved incrementally), then run the pipeline. The pipeline will detect the existing 50 FITD conversations and skip generation entirely.

### 5. Estimated runtime
- **If FITD generation complete (50/50)**: ~1.5-2h (data mixing + 3 seed training + evaluation)
- **If FITD generation incomplete**: add ~3-5 min per missing conversation for generation, plus Llama load time (~2 min)

---
