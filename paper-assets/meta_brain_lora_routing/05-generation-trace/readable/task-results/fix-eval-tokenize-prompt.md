# fix eval tokenize prompt

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_tokenize_prompt_20260516T143615_result.json`
- **Structured JSON:** [`de4f19e2d5450323071b.json`](../../sessions/de/de4f19e2d5450323071b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fix is complete and verified. Summary of changes to `/root/meta_brain_lora_routing/phase1/meta_brain_assembly.py`:

1. **Added import**: `import openpi.transforms as _transforms` (line 48)

2. **Added model transforms init** in `__init__` (after `self._tokenizer`):
   ```python
   self._model_transforms = [
       _transforms.ResizeImages(224, 224),
       _transforms.TokenizePrompt(self._tokenizer),
       _transforms.PadStatesAndActions(PI0_STATE_DIM),
   ]
   ```

3. **Rewrote `infer()`**: Instead of the fragile `jax.tree.map` on a mixed-type dict (which crashes on string prompt), the new flow:
   - Builds numpy data dict in openpi format (uint8 images, normalized state, string prompt)
   - Applies model transforms (ResizeImages → TokenizePrompt → PadStatesAndActions)
   - After transforms, `"prompt"` is gone — all values are numeric numpy arrays
   - `jax.tree.map` safely converts everything to batched torch tensors
   - Permutes images HWC→CHW, then `Observation.from_dict` handles uint8→float conversion

4. **Removed `_preprocess_real_obs`** — no longer needed, its logic is now handled by the openpi transforms.

---
