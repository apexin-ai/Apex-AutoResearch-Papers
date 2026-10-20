# Injected Recovery Evaluation Pipeline

## Files
- `eval/injected_eval.py` — main eval script (463 lines)
- `scripts/run_injected_eval.sh` — launcher for all 3 variants

## Design
At a chosen step (default random [2,4]), replaces the model's action with a random wrong action from admissible commands, executes it in the environment, and inserts an error tag matching the model variant's training format:
- **taxei**: `[Error Type: P1_StepOrderSwap]` (taxonomy-specific)
- **random**: `[Error occurred]` (generic)
- **vanilla**: no tag

Operator labels cycle round-robin through P1/P2/C1/C4.

## Usage
```bash
# Single variant
python eval/injected_eval.py --model_path <ckpt> --model_variant taxei --device cuda:0

# All 3 variants in parallel + comparison
bash scripts/run_injected_eval.sh all

# Compare two results
python eval/injected_eval.py --output results_a.json --compare_with results_b.json
```

## Output JSON
```json
{
  "recovery_rate": 0.xxx,
  "by_operator": {...},
  "by_task_type": {...},
  "episodes": [{
    "task_name": "...", "recovered": true/false,
    "inject_step": 2, "original_action": "go to desk 2",
    "injected_action": "take bowl 1 from desk 1",
    "error_tag": "[Error Type: P1_StepOrderSwap]"
  }]
}
```

## Dry-run verified
Vanilla checkpoint, 1 task, cuda:3 — RECOVERED in 13 steps (original: "go to desk 2", injected: "take bowl 1 from desk 1").