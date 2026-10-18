# ops restart k03 eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart_k03_eval_20260518T052858_result.json`
- **Structured JSON:** [`6c4461c994cd76c0e4a3.json`](../../sessions/6c/6c4461c994cd76c0e4a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval restarted. Summary:

- **PID 1881** on GPU 1 (16 GB, 85% util), tmux session `eval_k03_restart`
- **Log**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k03_restart.log`
- **Registry**: `eval_openvla_pruning_k03_restart` → RUNNING, parent=`eval_openvla_pruning_k03`
- **No task range support** in the script, so all 10 tasks run from scratch (~5h estimated at ~1.7 eps/min)
- **Partial results saved** to `artifacts/openvla_k03_partial_results.json`: 8/10 tasks, avg SR = 19.25% over 400 eps. The restart will give us a complete independent run to cross-validate.

---
