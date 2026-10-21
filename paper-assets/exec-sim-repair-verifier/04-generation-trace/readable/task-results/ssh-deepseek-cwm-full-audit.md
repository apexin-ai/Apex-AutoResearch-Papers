# ssh deepseek cwm full audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deepseek-cwm-full-audit_20260520T053758_result.json`
- **Structured JSON:** [`1d8bd9718e9fa8d2cf28.json`](../../sessions/1d/1d8bd9718e9fa8d2cf28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计原始输出

### A. DeepSeek CWM eval 目录清查

**A1: s42 eval dir (seq4096)**
```
DIR_NOT_FOUND
ls: cannot access '/home/sonny/exec-sim-repair-verifier/deepseek_cwm_repo_s42_seq4096/': No such file or directory
```

**A2: s42 eval dir (e3_seq4096)**
```
DIR_NOT_FOUND
ls: cannot access '/home/sonny/exec-sim-repair-verifier/deepseek_cwm_repo_s42_e3_seq4096/': No such file or directory
```

**A3: s123 eval dir**
```
DIR_NOT_FOUND
ls: cannot access '/home/sonny/exec-sim-repair-verifier/deepseek_cwm_repo_s123_seq4096/': No such file or directory
```

**A4: s42 results head (seq4096)**
```
NO_FILE
head: cannot open '/home/sonny/exec-sim-repair-verifier/deepseek_cwm_repo_s42_seq4096/results.jsonl' for reading: No such file or directory
```

**A5: s42 results head (e3_seq4096)**
```
NO_FILE
head: cannot open '/home/sonny/exec-sim-repair-verifier/deepseek_cwm_repo_s42_e3_seq4096/results.jsonl' for reading: No such file or directory
```

**A6: s123 results head**
```
NO_FILE
head: cannot open '/home/sonny/exec-sim-repair-verifier/deepseek_cwm_repo_s123_seq4096/results.jsonl' for reading: No such file or directory
```

**A-补充: find deepseek_cwm / qwen_cwm 目录**
```
find /home/sonny/exec-sim-repair-verifier -maxdepth 1 -type d -name "*deepseek_cwm*" → (empty)
find /home/sonny/exec-sim-repair-verifier -maxdepth 1 -type d -name "*qwen_cwm*" → (empty)
```

---

### B. Checkpoint 溯源

**B1: s42 checkpoint dir**
```
total 20
drwxr-xr-x  5 root root   81 May 17 23:33 .
drwxr-xr-x 70 root root 4096 May 20 13:00 ..
drwxr-xr-x  2 root root 4096 May 17 23:33 best
drwxr-xr-x  2 root root 4096 May 17 23:33 checkpoint-13266
drwxr-xr-x  2 root root 4096 May 17 13:07 checkpoint-8844
```

**B2: s123 checkpoint best dir**
```
total 67852
drwxr-xr-x 2 root root     4096 May 20 10:54 .
drwxr-xr-x 5 root root       80 May 20 10:54 ..
-rw-r--r-- 1 root root     5282 May 20 10:54 README.md
-rw-r--r-- 1 root root     1094 May 20 10:54 adapter_config.json
-rw-r--r-- 1 root root 67143296 May 20 10:54 adapter_model.safetensors
-rw-r--r-- 1 root root     1041 May 20 10:54 chat_template.jinja
-rw-r--r-- 1 root root      462 May 20 10:54 special_tokens_map.json
-rw-r--r-- 1 root root  2289810 May 20 10:54 tokenizer.json
-rw-r--r-- 1 root root     4324 May 20 10:54 tokenizer_config.json
-rw-r--r-- 1 root root     5969 May 20 10:54 training_args.bin
```

**B2 adapter_config.json:**
```json
{
  "alora_invocation_tokens": null,
  "alpha_pattern": {},
  "arrow_config": null,
  "auto_mapping": null,
  "base_model_name_or_path": "/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct",
  "bias": "none",
  "corda_config": null,
  "ensure_weight_tying": false,
  "eva_config": null,
  "exclude_modules": null,
  "fan_in_fan_out": false,
  "inference_mode": true,
  "init_lora_weights": true,
  "layer_replication": null,
  "layers_pattern": null,
  "layers_to_transform": null,
  "loftq_config": {},
  "lora_alpha": 32,
  "lora_bias": false,
  "lora_dropout": 0.05,
  "lora_ga_config": null,
  "megatron_config": null,
  "megatron_core": "megatron.core",
  "modules_to_save": null,
  "peft_type": "LORA",
  "peft_version": "0.19.0",
  "qalora_group_size": 16,
  "r": 16,
  "rank_pattern": {},
  "revision": null,
  "target_modules": ["q_proj", "v_proj", "o_proj", "k_proj"],
  "target_parameters": null,
  "task_type": "CAUSAL_LM",
  "trainable_token_indices": null,
  "use_bdlora": null,
  "use_dora": false,
  "use_qalora": false,
  "use_rslora": false
}
```

---

### C. GPU 2 进程确认

**C1: PID 917649 status**
```
   PID   PPID     ELAPSED CMD
917649 917648       38:30 /root/miniconda3/bin/python train_unified.py --data_dir data/ --task cwm --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456/ --run_name deepseek-cwm-repo-s456 --seed 456 --max_seq_length 2048 --batch_size 2 --grad_accumulation 8 --lr 2e-4 --epochs 3 --no_wandb
```

**C2: GPU compute apps**
```
886278, GPU-fc6e3c91-6d49-c4b1-63c9-3e7082c4ac10, 21246 MiB
917649, GPU-19c6fdd6-dd98-c089-da56-c21260f588cd, 16404 MiB
886352, GPU-02eb6271-cb5b-7542-230f-44000133e276, 31252 MiB
```

---

### D. Qwen CWM s42 eval 输出格式

**D1: Qwen s42 results head**
```
NO_FILE
head: cannot open '/home/sonny/exec-sim-repair-verifier/qwen_cwm_repo_s42_seq4096/results.jsonl' for reading: No such file or directory
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "alora_invocation_tokens": null,
    "alpha_pattern": {},
    "arrow_config": null,
    "auto_mapping": null,
    "base_model_name_or_path": "/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct",
    "bias": "none",
    "corda_config": null,
    "ensure_weight_tying": false,
    "eva_config": null,
    "exclude_modules": null,
    "fan_in_fan_out": false,
    "inference_mode": true,
    "init_lora_weights": true,
    "layer_replication": null,
    "layers_pattern": null,
    "layers_to_transform": null,
    "loftq_config": {},
    "lora_alpha": 32,
    "lora_bias": false,
    "lora_dropout": 0.05,
    "lora_ga_config": null,
    "megatron_config": null,
    "megatron_core": "megatron.core",
    "modules_to_save": null,
    "peft_type": "LORA",
    "peft_version": "0.19.0",
    "qalora_group_size": 16,
    "r": 16,
    "rank_pattern": {},
    "revision": null,
    "target_modules": [
      "q_proj",
      "v_proj",
      "o_proj",
      "k_proj"
    ],
    "target_parameters": null,
    "task_type": "CAUSAL_LM",
    "trainable_token_indices": null,
    "use_bdlora": null,
    "use_dora": false,
    "use_qalora": false,
    "use_rslora": false
  }
}
```

</details>

---
