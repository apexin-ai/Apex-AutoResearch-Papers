# Anonymous Repo De-identification Audit Report

**Project:** clkc_mech_interp  
**Date:** 2026-05-26  
**Repo:** `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/anonymous_repo/`

---

## 1. Repository Structure

| Item | Status |
|------|--------|
| README.md | ✅ Present |
| requirements.txt | ✅ Present (10 dependencies with version constraints) |
| .gitignore | ✅ Present (comprehensive) |
| LICENSE | ✅ MIT, copyright "Anonymous Authors" |
| src/ (20 .py files) | ✅ Covers full pipeline: data prep, activation collection, probing, bootstrap, steering, CKA, cross-task transfer, controls |
| scripts/ (2 .sh files) | ✅ run_pipeline.sh + run_probes.sh |

## 2. De-identification

### ❌ FIXED: .git/config contained GitHub credentials

- **Username:** `[REDACTED]`
- **PAT:** `[REDACTED]` (personal access token)
- **Remote URL:** `github.com/anonymous-nlp-2026-2/clkc_mech_interp.git`
- **Fix applied:** Removed entire `[remote "origin"]` section

### ❌ FIXED: .git/FETCH_HEAD contained GitHub URL

- **Content:** `branch 'main' of https://github.com/anonymous-nlp-2026-2/clkc_mech_interp`
- **Fix applied:** Emptied file

### ✅ git user config

- name = "Anonymous", email = "anonymous@anonymous.invalid"

### ✅ git log (single commit)

- Author: "Anonymous <anonymous@anonymous.invalid>"
- Message: "Initial commit: anonymous code for EMNLP 2026 submission"

### ✅ Source code (.py, .sh)

- No email addresses
- No personal names or usernames
- No university/institution names
- No Chinese characters that could identify authors
- No hardcoded server paths (/root/, /home/, autodl, etc.)
- No API keys, tokens, or passwords
- No wandb project names or HF usernames
- No TODO/FIXME/author annotations
- Only env var: `CUDA_VISIBLE_DEVICES=""` (benign)

### ✅ README.md

- Citation block uses "Anonymous" author
- Title says "[Title anonymized for review]" in citation
- No author names or affiliations

### ✅ LICENSE

- Copyright "2026 Anonymous Authors"

## 3. README Quality

| Item | Status |
|------|--------|
| Title matches paper topic | ✅ "Cross-Lingual Knowledge Conflict: A Mechanistic Interpretability Study" |
| Installation instructions | ✅ pip install + flash-attn optional |
| Python version specified | ✅ ">= 3.10" |
| CUDA version noted | ✅ ">= 12.1 recommended" |
| Data download instructions | ✅ ConflictQA (HuggingFace link), XNLI (auto-download), model paths |
| Reproduction commands | ✅ Full pipeline + step-by-step |
| Repository structure diagram | ✅ Complete with descriptions |
| Key experiments table | ✅ 7 entries with purpose |

## 4. .gitignore

| Pattern | Status |
|---------|--------|
| `__pycache__/`, `*.pyc` | ✅ |
| `.venv/`, `venv/` | ✅ |
| `*.pt` | ✅ |
| `*.pth` | ⚠️ Was missing, **now added** |
| `*.bin`, `*.safetensors`, `*.ckpt` | ✅ |
| `data/`, `models/`, `results/` | ✅ |
| `wandb/` | ✅ |
| `*.log`, `logs/` | ✅ |
| `.env`, `*.env` | ✅ |
| `.ipynb_checkpoints/` | ✅ |
| Large files tracked | ✅ None found |

## 5. Fixes Applied

1. **`.git/config`**: Removed `[remote "origin"]` section containing GitHub username `[REDACTED]`, PAT `[REDACTED]`, and repo URL
2. **`.git/FETCH_HEAD`**: Emptied file that contained `github.com/anonymous-nlp-2026-2/...` URL
3. **`.gitignore`**: Added `*.pth` pattern (was missing)

## 6. Summary

| Category | Verdict |
|----------|---------|
| Personal info in source code | ✅ Clean |
| Git metadata | ❌→✅ Fixed (credentials + remote URL removed) |
| README completeness | ✅ Good |
| .gitignore coverage | ⚠️→✅ Fixed (added *.pth) |
| Large files tracked | ✅ None |
| Overall | ✅ Ready for anonymous.4open.science after commit |
