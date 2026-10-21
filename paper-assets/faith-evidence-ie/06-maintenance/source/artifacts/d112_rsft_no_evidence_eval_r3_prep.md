# D112 RSFT No-Evidence Eval r3 — Pre-submission Check

## Script
- **Path**: `/root/autodl-tmp/freige/scripts/seed_expansion/eval_4b_rsft_no_evidence.sh`
- **Status**: EXISTS (796 bytes, modified 2026-05-19 21:02)

## Checkpoint & Dependencies
| Resource | Path | Exists |
|----------|------|--------|
| RSFT adapter (bf16) | `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16` | YES |
| SFT adapter | `/root/autodl-tmp/sft_output_seed44/` | YES |
| Base model | `/root/autodl-tmp/models/Qwen3-4B` | YES |
| Data | `/root/autodl-tmp/data/docred` | YES |

## Script Config
- `--no_evidence` flag: **PRESENT** (C005 satisfied)
- `--no-quantize`: bf16 full precision
- `--batch_size 4`, `--max_new_tokens 1024`, `--seed 42`
- Output: `/root/autodl-tmp/eval_outputs/eval_4b_rsft_s44_no_evidence`
- HF offline mode enabled

## GPU Status
| GPU | Memory Used | Total | Util |
|-----|-------------|-------|------|
| cuda:0 | 18881 MiB | 32607 MiB | 62% |
| cuda:1 | **0 MiB** | 32607 MiB | 0% |
| cuda:2 | 11425 MiB | 32607 MiB | 53% |
| cuda:3 | 6635 MiB | 32607 MiB | 46% |

- **Target GPU**: cuda:1 — **CLEAR** (0 MiB, C001 satisfied)

## Disk
- `/root/autodl-tmp/`: 65G available (75% used of 250G) — sufficient

## Recommended Submit Command
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/freige/scripts/seed_expansion/eval_4b_rsft_no_evidence.sh
```

## Ready to Submit
**YES** — script exists with correct path, all checkpoints/data present, `--no_evidence` flag set, cuda:1 free, disk sufficient.
