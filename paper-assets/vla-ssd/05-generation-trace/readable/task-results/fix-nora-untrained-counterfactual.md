# fix nora untrained counterfactual

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_nora_untrained_counterfactual_20260521T071138_result.json`
- **Structured JSON:** [`f176c3fa135941eb6bd9.json`](../../sessions/f1/f176c3fa135941eb6bd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OK — 1000/5000 at 15:25:22. The "empty" condition is significantly slower (~72s per 200 samples vs ~20s for "wrong"). This is because the empty instruction still requires a full forward pass with the correct instruction, and then another with the empty one — the empty string as input to the processor creates a different tokenization.

At this rate "empty" alone will take ~25 min. Total remaining (3 conditions) could be ~45 min. The process is stable, I'll report the status and let it run.

---

## Updated Status

The counterfactual job is running but slower than expected due to the "empty" condition's processing overhead.

| Condition | Status | Last-layer cos_dist | Cross-task d |
|-----------|--------|--------------------:|-------------:|
| wrong | **Done** | 0.0143 | 7.7111 |
| empty | Running (1000/5000) | — | — |
| shuffled | Pending | — | — |
| paraphrased | Pending | — | — |

**Process**: PID 541450 on cuda:1, running stably via nohup.  
**Rate**: "wrong" was ~20s/200 samples, "empty" is ~72s/200 samples (3.5x slower due to empty instruction tokenization).  
**Revised ETA**: ~16:10 UTC for completion (all 4 conditions).

### Download Status (both complete)
- `nora-libero-spatial`: 7.1G, 2/2 safetensors
- `phi3v-base`: 7.8G, 2/2 safetensors

### Verification Command
```bash
tail -10 /tmp/nora_untrained_cf.log
```

When finished:
```bash
python3 -c "
import json
d = json.load(open('/root/autodl-tmp/vla-ssd/results/nora_goal/untrained/counterfactual_combined.json'))
for k in ['wrong','empty','shuffled','paraphrased']:
    s = d[k]['global_metrics']['last_layer_summary']
    print(f\"{k:12s}  cos_dist={s['mean']:.6f}  cohen_d={s['cohens_d']:.4f}\")
print('Ranking:', [r['condition'] for r in d['ranking_by_cosine_distance']])
"
```

### cuda:1 Next Step
After ~16:10, cuda:1 is free for the next pipeline (NORA Spatial or Phi-3V).

---
