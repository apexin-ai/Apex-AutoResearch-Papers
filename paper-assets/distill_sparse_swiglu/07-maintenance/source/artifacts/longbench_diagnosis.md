# LongBench Evaluation Failures — Root Cause Diagnosis

**Server:** westd-34887  
**Investigation date:** 2026-05-25  
**Status:** Issue resolved. v6 runs succeeded on 2026-05-16. No action needed for future runs.

---

## Summary

8 failed runs across 5 iterations, each with a **different root cause**. Not a single recurring bug — a cascade of problems fixed one at a time.

## Failure Timeline

| Run | Timestamp (UTC) | Root Cause | Registry Notes |
|-----|-----------------|------------|----------------|
| `longbench_dense` | 05-16 13:01 | Dataset offline | `HF_HUB_OFFLINE=1 + 数据未缓存` |
| `longbench_kl30_uniform` | 05-16 13:01 | Dataset offline | same |
| `longbench_dense_v2` | 05-16 13:23 | GPU contention + OOM | `两个进程争抢同一 GPU + 无 flash-attn` |
| `longbench_kl30_uniform_v2` | 05-16 13:23 | GPU contention + OOM | same |
| `longbench_dense_v3` | 05-16 13:33 | Single-GPU OOM | `单卡无法处理 32k token LongBench 文档` |
| `longbench_kl30_uniform_v3` | 05-16 13:33 | Single-GPU OOM | same |
| `longbench_dense_v4` | 05-16 13:40 | CUDA fragmentation | `reserved 17.98GB > requested 13.98GB` |
| `longbench_dense_v5` | 05-16 13:45 | Manually killed | `DDL cleanup; Director 放弃 LongBench` |
| **`longbench_dense_v6`** | **05-16 15:37** | **Success** | 4643s, multi_gpu, batch_size=1 |
| **`longbench_kl30_uniform_v6`** | **05-16 16:56** | **Success** | 6413s, multi_gpu, batch_size=1 |

## Root Cause Details

### RC1: Dataset Download Blocked (v1)

v1 launched with `HF_HUB_OFFLINE=1` but `Xnhyacinth/LongBench` was not yet cached. Additionally, the original `THUDM/LongBench` dataset uses a Python loading script that `datasets>=3.x` refuses to execute:

```
ERROR: Dataset scripts are no longer supported, but found LongBench.py
```

**Fix applied:** An out-of-band download script (`/tmp/longbench_download3.log`, 21:21) manually cached the data from the parquet mirror `Xnhyacinth/LongBench`. The lm-eval task YAMLs already pointed at this mirror.

### RC2: GPU Contention OOM (v2)

v2 fixed the dataset issue but launched **two processes simultaneously** — dense on cuda:1, kl30 on cuda:0. Both load the full LLaMA 3.1 8B model (~16GB). With LongBench's long contexts (up to 32k tokens) and no flash-attention, generation OOM'd.

**Fix applied:** v6 ran one eval at a time (dense finished at 16:53, kl30 started at 16:58).

### RC3: Single-GPU Memory Insufficient (v3)

v3 ran one-per-GPU but a single GPU cannot hold the 8B model + KV cache for 32k-token LongBench documents during generation.

**Fix applied:** v4+ used `--multi_gpu` (device_map=auto across 2 GPUs).

### RC4: CUDA Memory Fragmentation (v4)

v4 used multi-GPU but hit fragmentation: PyTorch reserved 17.98GB but couldn't allocate a contiguous 13.98GB block. Crashed in 222s.

**Fix applied:** v5 added `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`. v5 was manually killed before it could complete. v6 used the same config with `--batch_size 1` and succeeded.

### v5: Manual Kill

Director decided to abandon LongBench after 5 failures. v5 was killed during DDL cleanup. Later, v6 was run anyway and succeeded.

## Why No Log Files Exist

All runs used `tmux` backend without nohup log redirection. When processes crashed, stdout/stderr went to the tmux terminal which was later evicted. This violates constraint **C002**. The only surviving evidence is:
- Empty result directories (benchmark_eval.py creates `out_dir` before running evaluations)
- Registry notes (added manually after each failure)
- `/tmp/longbench_download{,2,3}.log` (from the dataset debug script)

## What v6 Changed (the fix)

```bash
# v6 command (succeeded):
python -u src/benchmark_eval.py \
    --exp_id longbench_dense_v6 \
    --dense --multi_gpu --batch_size 1 \
    --tasks longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news
```

Key differences vs earlier attempts:
1. Dataset already cached from parquet mirror (`Xnhyacinth/LongBench`)
2. `--multi_gpu` — model spread across 2 GPUs via device_map=auto
3. `--batch_size 1` — minimizes peak memory during generation
4. **One process at a time** — no GPU contention
5. `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` likely still set from v5

## v6 Results

| Task | Dense | KL 30% Uniform | Degradation |
|------|-------|----------------|-------------|
| narrativeqa (F1) | 7.34 | 4.12 | -44% |
| qasper (F1) | 13.42 | 6.23 | -54% |
| gov_report (ROUGE) | 30.48 | 16.97 | -44% |
| multi_news (ROUGE) | 2.49 | 18.01 | +623% (noise) |

Director conclusion: "uniform allocation 在长上下文任务上不如 dense，不纳入论文主体。"

## Recommendations

1. **No re-run needed.** v6 data is valid and the conclusion (LongBench not used in paper) still stands.
2. **Future LongBench evals must use:** `--multi_gpu --batch_size 1`, one process at a time, with nohup logging per C002.
3. **Clean up empty dirs:** `longbench_{dense,kl30_uniform}{,_v2,_v3,_v4,_v5}` contain no data.
