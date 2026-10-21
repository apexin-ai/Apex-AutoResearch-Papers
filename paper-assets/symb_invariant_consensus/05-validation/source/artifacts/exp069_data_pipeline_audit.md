# exp-069 Data Pipeline Audit: LogiQA via --strategyqa-data

**Date**: 2026-05-19
**Verdict**: VALID — data pipeline correctly processes LogiQA through `--strategyqa-data`

## Command Under Review

```bash
python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 \
  --api-base http://localhost:8012/v1 --model auto --seed 42 \
  --strategyqa-data data/logiqa_200.json \
  --folio-data data/empty.json --math-data data/empty.json --pw-data data/empty.json \
  --output results/exp069_llama8b_logiqa200/exp069_results.json --save-intermediates
```

## Analysis

### 1. Data Loading — No Mislabeling

`load_all_problems()` (line 68):
```python
p.setdefault("dataset", "strategyqa")
```

`logiqa_200.json` entries already contain `"dataset": "logiqa"`. `setdefault` only writes when the key is absent — so the dataset field is **preserved as "logiqa"**.

### 2. Domain Switching — Correct Branch Taken

`run_full_mvp.py` lines 252-272:
```python
dataset = prob.get("dataset", "math")   # -> "logiqa"
...
elif dataset == "logiqa":
    extractor.domain = "logic"                    # correct
    pipeline.trace_generator.domain = "multichoice"  # correct
```

This matches `run_logiqa.py`'s explicit settings:
```python
generator.domain = "multichoice"
extractor.domain = "logic"
```

### 3. Prompt Template — Correct for Multi-Choice

With `domain="multichoice"`, the generator uses `MULTICHOICE_SOLVE_PROMPT`:
```
Answer the following multiple-choice question step by step. Show all your reasoning.
At the end, put your final answer letter in \boxed{}, e.g. \boxed{A}.

{problem}
```

Appropriate for LogiQA's A/B/C/D format.

### 4. Answer Extraction — Correct for A/B/C/D

With `domain="multichoice"`, extraction logic:
1. First tries `extract_boxed_answer()` — extracts content from `\boxed{X}`
2. Falls back to `extract_choice_answer()` — regex for "the answer is (A|B|C|D)" or boxed single letter

Both correctly handle LogiQA's single-letter answers.

### 5. Answer Comparison — Works for Single Letters

`is_equiv()` calls `normalize_answer()` which strips whitespace/LaTeX artifacts, then does string comparison. For single letters like "D" vs "D", trivially correct.

### 6. Constraint Extraction — Logic Domain Applied

`extractor.domain = "logic"` activates the logic-specific constraint prompt, same as `run_logiqa.py`.

## Minor Differences vs run_logiqa.py (Non-Impacting)

| Aspect | run_full_mvp.py | run_logiqa.py | Impact |
|--------|----------------|---------------|--------|
| MockLLM init | `MockLLM()` (default domain) | `MockLLM(domain="logic")` | None — exp-069 uses vllm mode |
| Extractor max_tokens | Passes `args.max_tokens` | Not passed (uses default) | Marginal — more tokens available for constraint extraction |

## Conclusion

The `--strategyqa-data` flag is just a CLI parameter name for loading a JSON file. The actual pipeline behavior is driven by the `"dataset"` field within each JSON record. Since `logiqa_200.json` correctly tags entries as `"dataset": "logiqa"`, the full pipeline (prompt template, answer extraction, constraint extraction, answer comparison) follows the LogiQA-appropriate code path.

**No rerun needed.**
