# Anonymous Repo Cleanup Report

**Date**: 2026-05-23
**Repo**: `/tmp/anon_repo/` -> `github.com/anonymous-nlp-2026-2/faith-evidence-ie`
**Commit**: 30aaafe

## Scan Results

| Pattern | Matches |
|---|---|
| `/root/autodl-tmp` | 0 |
| `autodl` (case-insensitive) | 0 |
| `seetacloud\|bjb2\|westd` | 0 |
| `@*.com\|@*.edu` | 0 |
| wandb entity/project identifiers | **5** |

## Fixes Applied

**5 files, 5 replacements:**

| File | Line | Old | New |
|---|---|---|---|
| `freige/training/sft_trainer.py` | 130 | `default="freige-sft"` | `default="your-project"` |
| `freige/training/rsft_trainer.py` | 272 | `default="freige-rsft"` | `default="your-project"` |
| `freige/training/grpo_trainer.py` | 398 | `default="freige-grpo"` | `default="your-project"` |
| `freige/training/dpo_trainer.py` | 147 | `default="freige-dpo"` | `default="your-project"` |
| `freige/eval/ced_reranker.py` | 311 | `project="freige"` | `project="your-project"` |

## Post-fix Verification

All verification scans returned **zero matches**:
- `/root/` paths: 0
- `autodl|seetacloud`: 0
- email addresses: 0
- original wandb project names: 0

## Notes

- No `/root/autodl-tmp` paths, `sys.path.insert` hacks, HF cache snapshot paths, server identifiers, or email addresses were present — the repo was already partially cleaned before this pass.
- `cross_method_table.py` already uses relative paths (`./outputs`).
- All model references already use HF hub IDs (e.g., `Qwen/Qwen3-4B`).
