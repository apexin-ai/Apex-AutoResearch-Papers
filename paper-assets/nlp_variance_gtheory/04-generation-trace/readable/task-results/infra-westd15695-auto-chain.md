# infra westd15695 auto chain

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd15695_auto_chain_20260521T152904_result.json`
- **Structured JSON:** [`6e0370c52cbe0ca5b8c6.json`](../../sessions/6e/6e0370c52cbe0ca5b8c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12,600 lines already — progressing fast. At this rate (~12.6K lines per minute), 86,400 lines will take ~7 minutes. Here's the full status report:

---

**Deployment Status:**

| Component | Status |
|-----------|--------|
| **Yi MMLU** | Complete (86,400 lines) |
| **auto_chain.sh** | Running — OLMo ARC in progress (12,600/86,400 lines) |
| **Items sampled** | GSM8K (200), ARC (200) |
| **HellaSwag items** | Download in progress (5.9MB/~13MB parquet), will generate items when download completes |

**Chain order (4 tasks now, 2 deferred):**
1. OLMo ARC — **running now**
2. OLMo GSM8K — queued
3. Yi ARC — queued
4. Yi GSM8K — queued
5. OLMo HellaSwag — skipped (items file not yet ready)
6. Yi HellaSwag — skipped (items file not yet ready)

**Scripts deployed:**
- `scripts/auto_chain.sh` — main chain, skips benchmarks with missing items files
- `scripts/prepare_and_chain.sh` — wrapper that waits for HellaSwag download
- `scripts/wait_hellaswag_download.sh` — background monitor to create HellaSwag items once parquet download completes (PID 27762)

**Commands used per task:**
```bash
python3 -m src.inference.run_experiment \
    --design results/design_olmo.csv \   # or design_yi.csv
    --items data/arc_items_exp002.json \  # per benchmark
    --benchmark arc \                     # arc/gsm8k/hellaswag
    --output results/exp001_olmo/olmo_arc.jsonl \
    --gpu-id 0 --resume
```

**Notes:**
- No "MATH" benchmark in codebase — supported benchmarks are mmlu, gsm8k, arc, hellaswag
- Non-MMLU benchmarks run zero-shot (no few-shot files available for arc/gsm8k/hellaswag)
- 432 conditions × 200 items = 86,400 expected lines per task
- HellaSwag can be run separately with `--resume` after items file is created — just re-run `auto_chain.sh`

**Time estimate:** ~5-7 min per task × 4 tasks = **20-28 min** for ARC+GSM8K. HellaSwag adds ~10-14 min once items are ready.

---
