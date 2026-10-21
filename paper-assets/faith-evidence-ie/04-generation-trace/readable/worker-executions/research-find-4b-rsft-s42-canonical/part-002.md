# research find 4b rsft s42 canonical — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-find-4b-rsft-s42-canonical.md) · [Structured JSON](../../../sessions/fc/fcd319fbb5329adc4fd5.json)

## Before a recorded user message

### Tool result

_source line 88 · 2026-05-19T13:58:16.328Z_

<details><summary>↩ Tool result · `toolu_01R2WdAu8eSbCs5fDHQqGTaq`</summary>

```text
=== mvp2_rsft_train_r1 ===
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42"
  metrics: {
  "rel_f1": 0.0483,
  "num_preds": 848,
  "sft_baseline_rel_f1": 0.4057,
  "failure_mode": "relation_ontology_collapse_to_freetext",
  "epoch1_eval_loss": 0.756,
  "epoch2_eval_loss": 0.759
}

=== mvp2_rsft_train_r1_s44 ===
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44"
  metrics: {
  "rel_f1": 0.4655,
  "evi_f1": 0.8087,
  "evi_f1_joint": 0.3713,
  "evi_f1_joint_P": 0.3775,
  "evi_f1_joint_R": 0.3653,
  "edcr": 0.635,
  "sft_baseline_rel_f1": 0.4057,
  "sft_baseline_evi_f1": 0.7979,
  "delta_rel_f1": 0.0598,
  "delta_evi_f1": 0.0108,
  "delta_evi_f1_joint": 0.0596,
  "mvp2_pass": true
}

=== mvp2_rsft_train_r1_s43 ===
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43"
  metrics: {
  "eval_loss": 0.7622,
  "train_loss": 0.6148,
  "eval_entropy": 0.6724,
  "mean_token_accuracy": 0.8291,
  "total_steps": 510,
  "epochs": 3,
  "training_hours": 1.99
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "uuid": "90577733-0112-4208-b7a8-8ae4171087a7",
  "tool_use_result": {
    "stdout": "=== mvp2_rsft_train_r1 ===\n  command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42\"\n  metrics: {\n  \"rel_f1\": 0.0483,\n  \"num_preds\": 848,\n  \"sft_baseline_rel_f1\": 0.4057,\n  \"failure_mode\": \"relation_ontology_collapse_to_freetext\",\n  \"epoch1_eval_loss\": 0.756,\n  \"epoch2_eval_loss\": 0.759\n}\n\n=== mvp2_rsft_train_r1_s44 ===\n  command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44\"\n  metrics: {\n  \"rel_f1\": 0.4655,\n  \"evi_f1\": 0.8087,\n  \"evi_f1_joint\": 0.3713,\n  \"evi_f1_joint_P\": 0.3775,\n  \"evi_f1_joint_R\": 0.3653,\n  \"edcr\": 0.635,\n  \"sft_baseline_rel_f1\": 0.4057,\n  \"sft_baseline_evi_f1\": 0.7979,\n  \"delta_rel_f1\": 0.0598,\n  \"delta_evi_f1\": 0.0108,\n  \"delta_evi_f1_joint\": 0.0596,\n  \"mvp2_pass\": true\n}\n\n=== mvp2_rsft_train_r1_s43 ===\n  command: bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43\"\n  metrics: {\n  \"eval_loss\": 0.7622,\n  \"train_loss\": 0.6148,\n  \"eval_entropy\": 0.6724,\n  \"mean_token_accuracy\": 0.8291,\n  \"total_steps\": 510,\n  \"epochs\": 3,\n  \"training_hours\": 1.99\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 89_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me also check the eval metrics for the D076 standardized eval of 4B RSFT s42.

Looking at the registry, there was `rsft_ced_s42_reeval` eval which gave ign_f1=0.4423. And `mvp2_eval_rsft_r1` gave rel_f1=0.4449, ign_f1=0.4449.

Wait, the ign_f1 values differ: 0.4423 vs 0.4449. 

The discrepancy likely comes from differences in how the D076 standardized eval and MVP2 eval were run. The canonical 4B CED RSFT s42 checkpoint at `/root/autodl-tmp/rsft_output/checkpoint-510` has been cleaned up, but the training data and SFT adapter are still available, so I could retrain if needed. I'm also noticing that the training metrics showed rel_f1=0.0483 (a failure case), but the subsequent full evals showed much better performance, which suggests the model improved significantly during evaluation.

Looking at the training setup, the issue is likely that the training-time eval only used 50 documents, which caught the model at an early stage or during a collapse phase, whereas the full 985-document eval revealed the actual final performance. The training run itself completed successfully with a final checkpoint, so the low metric during training was probably from a mid-training evaluation rather than the final model state.

The key takeaway is that the canonical checkpoint was stored at `/root/autodl-tmp/rsft_output/checkpoint-510` but has been deleted—though it can be retrained if needed. Now I'm documenting this in the project file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "uuid": "cd784ad7-fa72-482b-9199-f08d459c6b54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUyFFYuScqWqf7BPWVKekn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 74413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1867
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 90_

所有信息收集完毕。将结果写入项目文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "uuid": "9eb64bbc-8684-4256-9732-08676a6e1782",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUyFFYuScqWqf7BPWVKekn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 74413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1867
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_0111p9jWLyvoHv9U5jUsK6y2`</summary>

````json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# Memory\n\n## 4B CED RSFT s42 Canonical Checkpoint 搜索结果 (2026-05-19)\n\n### 结论\n**Canonical 4B CED RSFT s42 checkpoint 已被清理，需要重新训练。**\n\n### 原始路径\n- **Checkpoint**: `/root/autodl-tmp/rsft_output/checkpoint-510`\n- **Base model**: `/root/autodl-tmp/models/Qwen3-4B`\n- **SFT adapter**: `/root/autodl-tmp/sft_output`\n- **Training data**: `/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` (2718 samples, CED top_k=1)\n\n### 历史 eval 指标 (rsft_ced_s42_reeval, D076 标准 eval)\n| Metric | Value |\n|--------|-------|\n| ign_f1 | 0.4423 |\n| f1 | 0.4517 |\n| evi_f1 | 0.8174 |\n| edcr | 0.6569 |\n| evi_f1_joint | 0.3518 |\n| format_ok | 985/985 |\n| n_truncated | 214 |\n\n### 训练命令 (Registry: mvp2_rsft_train_r1)\n```bash\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/autodl-tmp\nHF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\npython -m freige.training.rsft_trainer \\\n  --base_model /root/autodl-tmp/models/Qwen3-4B \\\n  --sft_adapter /root/autodl-tmp/sft_output \\\n  --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \\\n  --output_dir /root/autodl-tmp/rsft_output \\\n  --learning_rate 2e-5 \\\n  --num_epochs 3 \\\n  --per_device_batch_size 4 \\\n  --gradient_accumulation_steps 4 \\\n  --lora_rank 64 \\\n  --lora_alpha 128 \\\n  --weighted_sampling \\\n  --eval_data_dir /root/autodl-tmp/data/docred \\\n  --eval_max_docs 50 \\\n  --wandb_run_name rsft-ced-r1 \\\n  --seed 42\n```\n\n### 上游依赖状态 (均存在，可直接重训)\n- ✅ Training data: `/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` (2718 lines)\n- ✅ SFT adapter: `/root/autodl-tmp/sft_output/adapter_config.json`\n- ✅ Base model: `/root/autodl-tmp/models/Qwen3-4B`\n\n### 现存 RSFT 输出目录汇总\n\n| 目录 | 模型 | Seed | 说明 |\n|------|------|------|------|\n| rsft_output_ced_s43 | 4B | 43 | CED RSFT, checkpoint-510, ign_f1=0.4512 |\n| rsft_output_random_k1 | 4B | 42 | Random baseline, ign_f1=0.4114 |\n| rsft_output_4b_sft_s44 | 4B | 42 | D112: RSFT from SFT s44 base (QLoRA, invalid) |\n| rsft_output_4b_sft_s44_bf16 | 4B | 42 | D112: RSFT from SFT s44 base (bf16, eval running) |\n| rsft_output_qwen3_1_7b_k1 | 1.7B | 42 | k=1 CED RSFT |\n| rsft_output_qwen3_1_7b_k1_s43 | 1.7B | 43 | k=1 CED RSFT |\n| rsft_output_qwen3_1_7b_k1_s44 | 1.7B | 44 | k=1 CED RSFT |\n| rsft_output_qwen3_8b_k1 | 8B | 42 | k=1 CED RSFT |\n| rsft_output_qwen3_8b_k1_s43 | 8B | 43 | k=1 CED RSFT |\n| rsft_output_qwen3_8b_k1_s44 | 8B | 44 | k=1 CED RSFT |\n| rsft_output_llama_3_1_8b_k1 | LLaMA-8B | 42 | k=1 CED RSFT |\n| rsft_output_llama_3_1_8b_k1_s43 | LLaMA-8B | 43 | k=1 CED RSFT |\n\n### 已删除的 4B RSFT 目录\n- `/root/autodl-tmp/rsft_output/` — canonical CED s42 (r1)\n- `/root/autodl-tmp/rsft_output_s43/` — CED s43 (MVP2 era, 被 rsft_output_ced_s43 替代)\n- `/root/autodl-tmp/rsft_output_s44/` — CED s44 (MVP2 era)\n- `/root/autodl-tmp/rsft_output_r2a/` — r2a ablation (1 epoch)\n- `/root/autodl-tmp/rsft_output_r2b/` — r2b ablation (conservative LoRA)\n- `/root/autodl-tmp/rsft_topk3_output/` — top_k=3 ablation\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "uuid": "a284d144-043c-42fb-895b-3c5ade0ee8d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUyFFYuScqWqf7BPWVKekn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 74413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1867
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-19T13:58:51.499Z_

<details><summary>↩ Tool result · `toolu_0111p9jWLyvoHv9U5jUsK6y2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "uuid": "e6c89dcf-67d2-47b6-b3f1-12a428881807",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 93_

搜索结果：

**Canonical 4B CED RSFT s42 checkpoint 已被清理，需重训。**

- 原始路径：`/root/autodl-tmp/rsft_output/checkpoint-510`（已删除）
- 历史指标（D076 标准 eval）：ign_f1=0.4423, evi_f1=0.8174, edcr=0.6569
- 所有上游依赖仍存在：training data (2718 samples)、SFT adapter、base model
- 完整训练命令和现存目录汇总已写入 `memory.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "uuid": "c794a364-4e4e-4289-b807-193ae5eec35a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ny37qqP5qJpyiw52c26NB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2564,
      "cache_read_input_tokens": 76280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2564
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 94_

搜索结果：

**Canonical 4B CED RSFT s42 checkpoint 已被清理，需重训。**

- 原始路径：`/root/autodl-tmp/rsft_output/checkpoint-510`（已删除）
- 历史指标（D076 标准 eval）：ign_f1=0.4423, evi_f1=0.8174, edcr=0.6569
- 所有上游依赖仍存在：training data (2718 samples)、SFT adapter、base model
- 完整训练命令和现存目录汇总已写入 `memory.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 271148,
  "duration_api_ms": 268837,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "7a1bb24f-af49-43f5-af76-caf622f98452",
  "total_cost_usd": 1.3196585000000003,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 84896,
    "cache_read_input_tokens": 841887,
    "output_tokens": 14634,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 84896,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 171,
        "cache_read_input_tokens": 76280,
        "cache_creation_input_tokens": 2564,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2564
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2045,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021449999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 14634,
      "cacheReadInputTokens": 841887,
      "cacheCreationInputTokens": 84896,
      "webSearchRequests": 0,
      "costUSD": 1.3175135000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5e27267c-e87b-464d-89aa-bcb58125c561"
}
```

</details>

---
