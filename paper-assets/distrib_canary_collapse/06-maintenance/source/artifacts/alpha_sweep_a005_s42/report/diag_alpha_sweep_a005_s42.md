# Diagnosis: alpha_sweep_a005_s42

**Date**: 2026-05-18
**Server**: westd-17855
**Status**: FAILED (EXIT_CODE=127)

## Root Cause (one sentence)

Conda not initialized in `.bashrc` on westd-17855, causing `python: command not found` in non-interactive shell.

## Key Log (entire log — only 2 lines)

```
bash: line 1: python: command not found
EXIT_CODE=127
```

## Environment Investigation

| Check | Result |
|-------|--------|
| `/root/miniconda3/bin/python` | EXISTS (Python 3.12) |
| torch installed | YES (`site-packages/torch/` present) |
| conda init in .bashrc | NO (grep returns empty) |
| .bash_profile | Does not exist |
| PATH in .bashrc | No PATH entries |
| Disk space | 12G/30G used (40%) — OK |
| conda envs | Empty (base only) |

## Can Retry Directly?

**YES**, after fixing PATH. The underlying Python env and packages are intact.

## Fix Steps

1. SSH to westd-17855
2. Run: `/root/miniconda3/bin/conda init bash`
3. Source: `source ~/.bashrc`
4. Verify: `python --version` → should show 3.12.x
5. Re-launch experiment

No code changes needed. The experiment script itself is correct.
