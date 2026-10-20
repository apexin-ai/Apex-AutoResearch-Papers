# Anonymization Audit — Code Repository

**Date**: 2026-05-23
**Scope**: `/root/schema_semantic_constrained_ie/` on `westd-16980`
**Targets**: author names, institutions, emails, identifiable W&B/GitHub URLs
**Method**: `ssh_read_only` only (no file modifications)

## Command Outputs

### 1. Email addresses

Command:
```
grep -rn --include=*.py --include=*.sh --include=*.yaml --exclude-dir=.git --exclude-dir=.venv \
  -E "[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}" /root/schema_semantic_constrained_ie/
```
Result: **exit 1, no matches** — no email addresses found in code.

### 2. W&B entity / project

Command:
```
grep -rn --include=*.py --include=*.sh --include=*.yaml --exclude-dir=.git --exclude-dir=.venv \
  -e WANDB_ENTITY -e WANDB_PROJECT -e wandb.entity -e wandb.project -e entity= /root/schema_semantic_constrained_ie/
```
Result (10 hits — all `WANDB_PROJECT` only; **no `WANDB_ENTITY` anywhere**):
```
scripts/train_lora_scierc.py:73:        p.add_argument("--wandb_project", default="schema_semantic_constrained_ie")
scripts/train_lora_scierc.py:114:       os.environ.setdefault("WANDB_PROJECT", args.wandb_project)
scripts/train_lora_llama_scierc.py:63:  p.add_argument("--wandb_project", default="schema_semantic_constrained_ie")
scripts/train_lora_llama_scierc.py:122: os.environ.setdefault("WANDB_PROJECT", args.wandb_project)
scripts/train_lora_docred.py:78:        p.add_argument("--wandb_project", default="schema_semantic_constrained_ie")
scripts/train_lora_docred.py:117:       os.environ.setdefault("WANDB_PROJECT", args.wandb_project)
scripts/train_lora_docred_llama.py:65:  p.add_argument("--wandb_project", default="schema_semantic_constrained_ie")
scripts/train_lora_docred_llama.py:98:  os.environ.setdefault("WANDB_PROJECT", args.wandb_project)
scripts/train_lora_wikievents.py:40:    p.add_argument("--wandb_project", default="schema_semantic_constrained_ie")
scripts/train_lora_wikievents.py:70:    os.environ.setdefault("WANDB_PROJECT", args.wandb_project)
```

### 3. GitHub URLs

Commands:
```
grep -rn --include=*.py --include=*.sh --include=*.yaml --include=*.md --exclude-dir=.git --exclude-dir=.venv "github.com/" ...
grep -rln ... "github.com" ...
```
Result: **exit 1, no matches** — no `github.com` URLs in `.py/.sh/.yaml/.md`.

### 4. README / pyproject / setup

- `pyproject.toml`, `setup.py`, `setup.cfg`: **none exist** at any depth (`find -maxdepth 3` returns empty).
- README files present:
  - `README_evaluation.md` (top-level) — content is purely a description of `violation_checker.py` vs `violation_checker_docred.py`. **No author info.**
  - `.pytest_cache/README.md` — pytest auto-generated, no author info.

### 5. `author` field

Command:
```
grep -rn --include=*.py --include=*.cfg --include=*.toml --exclude-dir=.git --exclude-dir=.venv \
  -e "author" -e "Author" /root/schema_semantic_constrained_ie/
```
Result: **exit 1, no matches**.

### 6. Additional sweeps (defense in depth)

- `Copyright / Affiliation / University / institute / Institute` across `.py/.sh/.yaml/.md`:
  - Only hit: `scripts/ontology_scalability_benchmark.py:41` lists `'University'` as an **ontology entity-type label**, not author info.
- `huggingface.co/` and `wandb.ai/` URLs in `.py/.sh/.yaml/.md`: **none**.
- `.env`, `.gitconfig`, `.ini` files: **none present**.

## Summary of Findings

| Category | Status | Notes |
|----------|--------|-------|
| Email addresses | Clean | 0 hits |
| W&B entity | Clean | 0 hits (no `WANDB_ENTITY` set) |
| W&B project name | Borderline | Default = `schema_semantic_constrained_ie` (10 occurrences in `scripts/train_lora_*.py`) |
| GitHub URLs | Clean | 0 hits |
| Huggingface / wandb.ai URLs | Clean | 0 hits |
| `author=` field | Clean | 0 hits (no `pyproject.toml`/`setup.py`) |
| README author info | Clean | Only descriptive README, no names |
| Affiliation / institute strings | Clean | Single "University" hit is ontology label |

## Verdict — Fixes Needed?

**No mandatory fixes.** The repository contains no author names, no email addresses, no institutional affiliations, no GitHub/W&B/HuggingFace personal URLs, and no `author=` metadata.

**One optional consideration**:
- The default `WANDB_PROJECT` value `"schema_semantic_constrained_ie"` in the 5 training scripts is the repository/topic name — it does not identify authors. No entity is hardcoded. Safe under ARR rules.

No edits required prior to ARR submission.
