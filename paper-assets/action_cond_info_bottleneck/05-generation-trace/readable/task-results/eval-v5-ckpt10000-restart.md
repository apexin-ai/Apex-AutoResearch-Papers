# eval v5 ckpt10000 restart

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v5-ckpt10000-restart_20260516T062319_result.json`
- **Structured JSON:** [`fe9b4c9e1c1e414c3547.json`](../../sessions/fe/fe9b4c9e1c1e414c3547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Stopping to report a finding that contradicts the task assumption.**

PID 806823 didn't crash — it ran to completion and exited normally. The eval failed because all 4 suites errored out with the same dtype mismatch:

```
"libero_spatial": {"error": "RuntimeError: mat1 and mat2 must have the same dtype, but got BFloat16 and Float"}
"libero_object":  {"error": "RuntimeError: mat1 and mat2 must have the same dtype, but got BFloat16 and Float"}
"libero_goal":    {"error": "RuntimeError: mat1 and mat2 must have the same dtype, but got BFloat16 and Float"}
"libero_10":      {"error": "RuntimeError: mat1 and mat2 must have the same dtype, but got BFloat16 and Float"}
```

Confirmed at `/root/acib/outputs/acib_v5_div_reg_eval_ckpt10000/summary.json`. The tail in eval.log is just EGL cleanup noise from process exit.

**Root cause** (in `scripts/eval_acib.py` `make_policy_with_acib`, lines ~94–138):
- `base_policy` is loaded as bf16 (SmolVLA stores params in bf16 — training log confirms `dtype: bfloat16`).
- `ACIBPolicy(base_policy, acib_cfg)` initializes `scorer.mlp` (`nn.Linear`) in default **fp32**.
- `policy.load_state_dict(..., strict=False)` copies values into the existing fp32 buffers, so scorer stays fp32.
- `policy.to(target_device)` moves but doesn't change dtype.
- At eval, the connector forward-hook (`acib_policy.py:_connector_hook`) receives bf16 tokens, passes them to a fp32 `self.scorer.mlp` → `Linear` dtype mismatch.

Training never hit this because `torch.autocast(bfloat16)` was active.

**Other notes:**
- Previous run used `--seed 42` (not the script default 1000). The task didn't specify seed.
- Registry has no entry for `acib_v5_div_reg_eval_ckpt10000` (only `acib_v5_div_reg_seed2`). Task said "current is DONE/failed, reset to PREPARING" — that's not the state on disk.
- No live `eval_acib` process on the server (ps via ssh_execute would be cleaner but pgrep/grep-pipes blocked by read-only allowlist; can confirm with ssh_execute if needed).
- `submit_training_job` MCP tool is not available in this session — only `ssh_execute` / `ssh_read_only` / `kill_job` / `update_registry` / etc. Would need to launch via ssh_execute + tmux.

**Proposed minimal fix** — one line in `scripts/eval_acib.py` after `policy.to(target_device)`:

```python
policy.scorer.to(dtype=next(base_policy.parameters()).dtype)
```

This restarts won't work without it. Options:

1. Apply the one-line fix and relaunch (recommended).
2. Skip patch, wrap the hook body in `torch.autocast(device_type="cuda", dtype=torch.bfloat16)` instead — slightly more invasive but matches training.
3. You confirm a different intended fix.

Want me to proceed with option 1?

---
