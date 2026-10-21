## exp029 Seed 6 OOD Eval v2

**Fix**: `get_special_tokens()` in `ctx_manager.py:28` matches model type via `tokenizer.name_or_path.lower()`. HF checkpoint path `/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf` didn't contain "qwen". Created symlink:
```
/root/autodl-tmp/checkpoints/qwen_exp029_seed6_step15_hf -> /root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf
```
Updated `_alfworld_exp029_seed6_ood_eval.yaml` model_path accordingly.

**Server**: westd-47453, cuda:2
**PID**: 342378 (main), 348931 (TaskRunner), 349550 (WorkerDict)
**Config**: 134 OOD tasks, val_only, group_size=1
**Log**: /tmp/exp029_seed6_ood_eval_v2.log