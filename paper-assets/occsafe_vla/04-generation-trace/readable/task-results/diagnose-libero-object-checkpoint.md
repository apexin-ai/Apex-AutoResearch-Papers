# diagnose libero object checkpoint

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_libero_object_checkpoint_20260528T015457_result.json`
- **Structured JSON:** [`25626715f22ac036496d.json`](../../sessions/25/25626715f22ac036496d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture is clear. Here's the diagnosis:

```json
{
  "10894_full_occ_bn_5000_chkpt": {
    "exists": true,
    "has_model_files": "INCOMPLETE - 3/4 shards, shard 3 truncated",
    "files_detail": {
      "model-00001-of-00004.safetensors": "4.9GB ✓",
      "model-00002-of-00004.safetensors": "4.9GB ✓",
      "model-00003-of-00004.safetensors": "24KB ✗ (TRUNCATED, should be ~5GB)",
      "model-00004-of-00004.safetensors": "MISSING",
      "model.safetensors.index.json": "MISSING",
      "action_head--5000_checkpoint.pt": "302MB ✓",
      "proprio_projector--5000_checkpoint.pt": "67MB ✓",
      "occ_head--5000_checkpoint.pt": "2.4MB ✓",
      "lora_adapter/": "exists ✓",
      "config/tokenizer/processor jsons": "all present ✓"
    },
    "crash_log": "OSError: no file named pytorch_model.bin...found in directory ...5000_chkpt (resume attempt at 09:45)"
  },
  "10894_detach_bn_5000_chkpt": {
    "exists": true,
    "has_model_files": "INCOMPLETE - only 1/4 shards",
    "files_detail": {
      "model-00001-of-00004.safetensors": "4.0GB ✓",
      "model-00002-of-00004.safetensors": "MISSING",
      "model-00003-of-00004.safetensors": "MISSING",
      "model-00004-of-00004.safetensors": "MISSING",
      "model.safetensors.index.json": "MISSING",
      "action_head--5000_checkpoint.pt": "302MB ✓",
      "proprio_projector--5000_checkpoint.pt": "67MB ✓",
      "occ_head--5000_checkpoint.pt": "2.4MB ✓",
      "lora_adapter/": "exists ✓"
    },
    "crash_log": "OSError: no file named pytorch_model.bin...found in directory ...5000_chkpt (resume attempt at 09:45)"
  },
  "34685_vanilla_10000_chkpt": {
    "exists": false,
    "has_model_files": false,
    "note": "10000_chkpt directory was NEVER CREATED. Existing checkpoints: 15000 (complete), 20000 (complete), 25000 (INCOMPLETE - crashed during save)",
    "25000_chkpt_status": "Only has action_head, proprio_projector, tokenizer files. NO model safetensors, NO config.json. Process crashed mid-save.",
    "crash_log": "HFValidationError + OSError: save_training_checkpoint() at line 727 tried AutoModelForVision2Seq.from_pretrained('...--10000_chkpt') but 10000_chkpt doesn't exist → crash at 09:51:23"
  },
  "new_experiments_status": {
    "vanilla_object_s1": "RUNNING on westd-10894 cuda:0, step 30483/50005 (61%), ~1.08 it/s. Checkpoints: 20000 ✓ (complete 4/4), 25000 ✓ (complete 4/4), 30000 ✓ (complete 4/4). HEALTHY.",
    "detach_ln_v2_s4": "RUNNING on westd-10894 cuda:1, step 11972/50005 (24%), ~1.10 it/s. Checkpoints: 5000 ✓ (complete 4/4 + index.json), 10000 ✓ (complete 4/4 + index.json). HEALTHY."
  },
  "disk_space": {
    "10894": "250G total, 116G used (47%), 135G free — NOT the cause",
    "34685": "350G total, 168G used (48%), 183G free — NOT the cause"
  },
  "root_cause": "save_training_checkpoint() in finetune.py (line 727) is non-atomic. It writes auxiliary files first (tokenizer, .pt heads, config), then calls AutoModelForVision2Seq.from_pretrained() to load a base model for LoRA merging, then saves safetensors shards sequentially. If the process is interrupted during safetensors writing (or the from_pretrained call fails), the checkpoint is left in a half-written state: auxiliary files present but model safetensors incomplete/missing. For vanilla_object_s0, the save function tried to load from a 10000_chkpt path that was never created → the save at step 25000 crashed. For 10894 experiments, the original training runs produced truncated checkpoints (possibly interrupted during concurrent saves on same disk), and the subsequent resume attempts failed because from_pretrained can't load incomplete safetensors.",
  "fix_recommendation": "1) These 3 experiments (full_occ_bn_object_s0, detach_bn_object_s0, vanilla_object_s0) need to be re-run FROM SCRATCH (from pretrained weights, not resume). 2) Investigate save_training_checkpoint() line 727: the from_pretrained path computation is buggy — for vanilla_object_s0 it referenced a 10000_chkpt that was never saved. The function should load the base model from the original vla_path, not a derived checkpoint path. 3) Consider atomic checkpoint saving (write to temp dir, then rename)."
}
```

**Summary of the 3 failures:**

| Experiment | Server | Failure Mode |
|---|---|---|
| `full_occ_bn_object_s0` | 10894 | 5000_chkpt has truncated shard 3 (24KB) + missing shard 4. Resume crashed. |
| `detach_bn_object_s0` | 10894 | 5000_chkpt has only shard 1/4. Resume crashed. |
| `vanilla_object_s0` | 34685 | `save_training_checkpoint()` tried to load nonexistent 10000_chkpt as base model → process killed at step ~25000. Has usable complete checkpoints at 15000 and 20000. |

**Good news:** `vanilla_object_s1` and `detach_ln_v2_s4` are both running healthy with complete checkpoints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "10894_full_occ_bn_5000_chkpt": {
      "exists": true,
      "has_model_files": "INCOMPLETE - 3/4 shards, shard 3 truncated",
      "files_detail": {
        "model-00001-of-00004.safetensors": "4.9GB ✓",
        "model-00002-of-00004.safetensors": "4.9GB ✓",
        "model-00003-of-00004.safetensors": "24KB ✗ (TRUNCATED, should be ~5GB)",
        "model-00004-of-00004.safetensors": "MISSING",
        "model.safetensors.index.json": "MISSING",
        "action_head--5000_checkpoint.pt": "302MB ✓",
        "proprio_projector--5000_checkpoint.pt": "67MB ✓",
        "occ_head--5000_checkpoint.pt": "2.4MB ✓",
        "lora_adapter/": "exists ✓",
        "config/tokenizer/processor jsons": "all present ✓"
      },
      "crash_log": "OSError: no file named pytorch_model.bin...found in directory ...5000_chkpt (resume attempt at 09:45)"
    },
    "10894_detach_bn_5000_chkpt": {
      "exists": true,
      "has_model_files": "INCOMPLETE - only 1/4 shards",
      "files_detail": {
        "model-00001-of-00004.safetensors": "4.0GB ✓",
        "model-00002-of-00004.safetensors": "MISSING",
        "model-00003-of-00004.safetensors": "MISSING",
        "model-00004-of-00004.safetensors": "MISSING",
        "model.safetensors.index.json": "MISSING",
        "action_head--5000_checkpoint.pt": "302MB ✓",
        "proprio_projector--5000_checkpoint.pt": "67MB ✓",
        "occ_head--5000_checkpoint.pt": "2.4MB ✓",
        "lora_adapter/": "exists ✓"
      },
      "crash_log": "OSError: no file named pytorch_model.bin...found in directory ...5000_chkpt (resume attempt at 09:45)"
    },
    "34685_vanilla_10000_chkpt": {
      "exists": false,
      "has_model_files": false,
      "note": "10000_chkpt directory was NEVER CREATED. Existing checkpoints: 15000 (complete), 20000 (complete), 25000 (INCOMPLETE - crashed during save)",
      "25000_chkpt_status": "Only has action_head, proprio_projector, tokenizer files. NO model safetensors, NO config.json. Process crashed mid-save.",
      "crash_log": "HFValidationError + OSError: save_training_checkpoint() at line 727 tried AutoModelForVision2Seq.from_pretrained('...--10000_chkpt') but 10000_chkpt doesn't exist → crash at 09:51:23"
    },
    "new_experiments_status": {
      "vanilla_object_s1": "RUNNING on westd-10894 cuda:0, step 30483/50005 (61%), ~1.08 it/s. Checkpoints: 20000 ✓ (complete 4/4), 25000 ✓ (complete 4/4), 30000 ✓ (complete 4/4). HEALTHY.",
      "detach_ln_v2_s4": "RUNNING on westd-10894 cuda:1, step 11972/50005 (24%), ~1.10 it/s. Checkpoints: 5000 ✓ (complete 4/4 + index.json), 10000 ✓ (complete 4/4 + index.json). HEALTHY."
    },
    "disk_space": {
      "10894": "250G total, 116G used (47%), 135G free — NOT the cause",
      "34685": "350G total, 168G used (48%), 183G free — NOT the cause"
    },
    "root_cause": "save_training_checkpoint() in finetune.py (line 727) is non-atomic. It writes auxiliary files first (tokenizer, .pt heads, config), then calls AutoModelForVision2Seq.from_pretrained() to load a base model for LoRA merging, then saves safetensors shards sequentially. If the process is interrupted during safetensors writing (or the from_pretrained call fails), the checkpoint is left in a half-written state: auxiliary files present but model safetensors incomplete/missing. For vanilla_object_s0, the save function tried to load from a 10000_chkpt path that was never created → the save at step 25000 crashed. For 10894 experiments, the original training runs produced truncated checkpoints (possibly interrupted during concurrent saves on same disk), and the subsequent resume attempts failed because from_pretrained can't load incomplete safetensors.",
    "fix_recommendation": "1) These 3 experiments (full_occ_bn_object_s0, detach_bn_object_s0, vanilla_object_s0) need to be re-run FROM SCRATCH (from pretrained weights, not resume). 2) Investigate save_training_checkpoint() line 727: the from_pretrained path computation is buggy — for vanilla_object_s0 it referenced a 10000_chkpt that was never saved. The function should load the base model from the original vla_path, not a derived checkpoint path. 3) Consider atomic checkpoint saving (write to temp dir, then rename)."
  }
}
```

</details>

---
