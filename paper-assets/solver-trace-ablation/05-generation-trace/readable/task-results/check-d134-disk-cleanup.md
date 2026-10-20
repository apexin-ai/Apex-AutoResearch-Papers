# check d134 disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-disk-cleanup_20260518T115548_result.json`
- **Structured JSON:** [`edcdc003afbc36b211f2.json`](../../sessions/ed/edcdc003afbc36b211f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the situation:

```
Disk: 223/250G used (11% free, 28GB available)
s47 post-cleanup size: 31GB
s48 status: training, step ~39/500, ~65 min to completion
```

**Cleanup logic has a critical bug.** The script only deletes files from `${OUT_DIR}/` root but never touches `${OUT_DIR}/checkpoint-500/`:

```bash
# What the script does for non-s47:
rm -f ${OUT_DIR}/model-*.safetensors          # root only
rm -f ${OUT_DIR}/model.safetensors.index.json  # root only
rm -f ${OUT_DIR}/optimizer*.bin ...
rm -rf ${OUT_DIR}/global_step*
# checkpoint-500/ is NEVER cleaned → 16GB orphaned per run
```

**s47 breakdown:**
- Root: ~15GB model safetensors (PRESERVE, correct)
- `checkpoint-500/`: ~16GB **duplicate** model safetensors (never cleaned)
- Total: 31GB instead of expected ~15GB

**Imminent crash projection:**
- s48 at step 500 will try to save checkpoint-500 (~16GB) + final model (~15GB) = ~31GB
- Only 28GB free → **disk full, s48 will crash when training finishes (~65 min)**

**Risk: CRITICAL**

**Required actions (in order of urgency):**

1. **Now**: Delete s47's redundant checkpoint-500 to free 16GB (root already has complete weights)
   ```bash
   rm -rf /root/autodl-tmp/outputs/d134_4b_isr_b01_s47/checkpoint-500
   ```

2. **Fix pipeline script**: Add checkpoint cleanup for all runs:
   ```bash
   # After the existing cleanup block, add for ALL seeds:
   rm -rf ${OUT_DIR}/checkpoint-*
   ```

3. **With both fixes**: s47 = ~15GB, each other run = ~200KB post-cleanup → total ~15.2GB for all 10 runs. No disk risk.

Want me to execute these fixes? s48 finishes in ~65 min so this is time-sensitive.

---
