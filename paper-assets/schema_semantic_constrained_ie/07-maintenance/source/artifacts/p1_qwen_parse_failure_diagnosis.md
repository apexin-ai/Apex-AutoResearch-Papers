# P1 Qwen EE FT Parse Failure Diagnosis

**Date**: 2026-05-18  
**Experiment**: p1_ee_ft_composability_r4  
**Model**: LoRA fine-tuned Qwen3-8B (r=16, alpha=32, lr=2e-4, 3 epochs, merged)  
**Task**: WikiEvents Event Extraction  
**Server**: westd-21461

## Observed Symptoms

| Mode | Total | Parsed | Parse Rate |
|------|-------|--------|------------|
| unconstrained | 20 | 5 | 25% |
| constrained (full_s1) | 20 | 2 | 10% |

## Root Cause 1 (PRIMARY): Severe Repetition Degeneration

The FT model degenerates into extreme repetitive generation in greedy decoding, producing the same event or entity entry 50-100+ times until hitting the `max_new_tokens=4096` limit. The JSON output is truncated mid-field, causing `json.loads()` to fail.

### Evidence

**Unconstrained mode** (15/20 truncated):
- Failed samples average ~100 trigger mentions each (same trigger repeated). Successfully parsed samples have 1-15 triggers.
- Output lengths for failures cluster at 10K-15K chars, all ending mid-JSON (e.g., `"role": "Victim`).
- Successfully parsed samples: 146-3980 chars with complete JSON.

```
Sample 0: len=13415, triggers=102, ends_complete=False  # "killed" x100+
Sample 1: len=12863, triggers=99,  ends_complete=False  # "bombing" x100+
Sample 3: len=3980,  triggers=15,  ends_complete=True   # PARSED OK
```

**Constrained full_s1 mode** (18/20 truncated):
- 292-333 entity entries per sample, 0 triggers in ANY sample. Model never reaches events section.
- Example: `{"text": "Allah", "type": "GPE"}` repeated 200+ times in a single output.

### Contributing Factors
- **Greedy decoding** (`do_sample=False`) with **no repetition penalty** configured
- `max_new_tokens=4096` gives ample runway (training completions: median 2017 chars, max 15239 chars)
- LoRA FT may have degraded the base model's sequence quality/stopping behavior

### Generation Config (from `run_constrained_extraction.py:560`)
```python
gen_kwargs = dict(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
# No repetition_penalty, no length_penalty, no no_repeat_ngram_size
```

## Root Cause 2 (CRITICAL for constrained): Grammar Schema / FT Format Mismatch

### Grammar schema (`compiler/ontology_compiler.py:254-299`)
```json
{
  "type": "object",
  "properties": {
    "entities": {"type": "array", ...},   // <-- REQUIRED
    "events": {"type": "array", ...}      // <-- REQUIRED
  },
  "required": ["entities", "events"]
}
```

### FT training data format (`data/sft/wikievents_sft_train.jsonl`)
```json
{"events": [{"trigger": "...", "event_type": "...", "arguments": [...]}]}
```

**Mismatch**: Grammar forces `{"entities": [...], "events": [...]}` but model was trained to output `{"events": [...]}` only. The xgrammar logits processor forces the model to first generate an `entities` array. The model was never trained to produce entities at the top level, so it hallucinates repetitive entity entries until token exhaustion, never reaching the events portion.

This directly explains why constrained (10%) is WORSE than unconstrained (25%).

### Full_s1 output pattern (ALL samples)
```
{"entities": [{"text": "Taliban", "type": "ORG"}, {"text": "Afghan", "type": "GPE"}, ...x300+
```
Zero triggers in all 20 constrained outputs.

## Root Cause 3 (MINOR): `<think>` Token Prefix Mismatch

### Training data prompt ends with:
```
<|im_start|>assistant
<think>

</think>

{JSON completion starts here}
```

### Inference prompt (`enable_thinking=False`):
```
<|im_start|>assistant
{model generates from here}
```

The model appears to have adapted (raw outputs start with `{"events":` directly, after `skip_special_tokens=True` stripping). However, this distribution shift between training and inference prefix could contribute to degraded generation quality.

## max_new_tokens Setting

- Default: 2048
- WikiEvents auto-bump: 4096 (`run_constrained_extraction.py:818-819`)
- Run script (`scripts/run_p1_ee_ft.sh`): no explicit `--max_new_tokens`, so uses the auto-bumped 4096

## Training Configuration (`scripts/train_lora_wikievents.py`)

| Parameter | Value |
|-----------|-------|
| LoRA r | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | q/k/v/o_proj, gate/up/down_proj |
| Learning rate | 2e-4 |
| Epochs | 3.0 |
| Batch size | 4 x 4 grad_accum = effective 16 |
| Max length | 4096 |
| Optimizer | AdamW cosine |
| Training samples | 194 |
| completion_only_loss | True |

## Suggested Fixes (not executed, priority order)

1. **Add `repetition_penalty=1.2-1.5`** to generation kwargs in `run_single_pass`
2. **Create event-only grammar schema** for FT model: remove `entities` requirement from `compile_event_json_schema()`, or add a new method `compile_event_only_json_schema()` matching FT format
3. **Reduce `max_new_tokens`** to 2048 for quick test (shorter runway = less repetition before truncation, though won't fix root cause)
4. **Try sampling** (`temperature=0.3-0.5`) instead of greedy to break repetition loops
5. **Add `no_repeat_ngram_size=10`** as additional repetition control
6. **Evaluate FT training quality**: check train/eval loss curves, consider reducing to 1-2 epochs or lower LR (2e-4 is aggressive for LoRA)
7. **Align inference prefix**: add empty `<think>\n\n</think>\n\n` to generation prompt, or retrain without think tags in prompt
