# registry reconcile running experiments — Part 2 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../registry-reconcile-running-experiments.md) · [Structured JSON](../../../sessions/8a/8aa33825bec9f3dfdf7a.json)

## Before a recorded user message

### Tool result

_source line 189 · 2026-05-28T06:46:29.489Z_

<details><summary>↩ Tool result · `toolu_01MxfBhXKkodP6KVoRV4pF5y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T03:10:08.749Z\", \"updated_at\": \"2026-05-28T06:46:23.110Z\", \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s44. Third seed for Table 2 Object row.\", \"parent\": \"pi05-crm-always-on-object-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"511001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log\", \"submitted_at\": \"2026-05-28T03:12:00.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2707}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "e2a3ec4a-e8cf-4c11-9dcb-6e999c7d3fd7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"pi05-crm-always-on-object-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T03:10:08.749Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:46:23.110Z\\\", \\\"hypothesis\\\": \\\"Pi05 CRM always-on (τ=0.001) on Object suite s44. Third seed for Table 2 Object row.\\\", \\\"parent\\\": \\\"pi05-crm-always-on-object-s42\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"511001\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:12:00.314Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2707}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"pi05-crm-always-on-object-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T03:10:08.749Z\", \"updated_at\": \"2026-05-28T06:46:23.110Z\", \"hypothesis\": \"Pi05 CRM always-on (τ=0.001) on Object suite s44. Third seed for Table 2 Object row.\", \"parent\": \"pi05-crm-always-on-object-s42\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"511001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log\", \"submitted_at\": \"2026-05-28T03:12:00.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2707}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-28T06:46:32.452Z_

<details><summary>↩ Tool result · `toolu_01F49dAvnEy3UTrdJqRNKdc8`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 2.9492}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "c3189483-46ce-417d-a122-4e818e720ea1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Eval experiment requires additional spec fields: ['checkpoint_source']. Eval spec must include: ['checkpoint_source', 'eval_data']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.9492}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 2.9492}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-28T06:46:41.903Z_

<details><summary>↩ Tool result · `toolu_01AZFgJMyPM7fXTrWqurSzjk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-object-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:26.027Z\", \"updated_at\": \"2026-05-28T06:46:35.397Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550841\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\", \"parent\": \"eval-ksweep-k20-obs-object-s43\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4371}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "8bf2ff04-bb67-46b0-8856-9ef8f9700b3d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-ksweep-k20-obs-object-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:26.027Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:46:35.397Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"550841\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:22.258Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\\\", \\\"parent\\\": \\\"eval-ksweep-k20-obs-object-s43\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4371}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-object-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:26.027Z\", \"updated_at\": \"2026-05-28T06:46:35.397Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550841\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"K=20 obs_only CRM on Object seed44. Third seed for K-sweep analysis justifying K=10 design choice.\", \"parent\": \"eval-ksweep-k20-obs-object-s43\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4371}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-28T06:46:51.309Z_

<details><summary>↩ Tool result · `toolu_01VL572YxzHbH5VquWQ1D27t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T05:00:53.917Z\", \"updated_at\": \"2026-05-28T06:46:44.925Z\", \"hypothesis\": \"plan_601 P0: K-sweep K=20 obs-only Object s43. Tests effect of sample budget on CRM refinement quality with larger candidate set.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.05 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"558360\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-obj-s43.log\", \"submitted_at\": \"2026-05-28T05:01:35.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3938}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "7403eddf-5022-4a69-906d-293fa993370b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-ksweep-k20-obs-obj-s43\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T05:00:53.917Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:46:44.925Z\\\", \\\"hypothesis\\\": \\\"plan_601 P0: K-sweep K=20 obs-only Object s43. Tests effect of sample budget on CRM refinement quality with larger candidate set.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.05 --benchmark object --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"558360\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-obj-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:01:35.230Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3938}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-ksweep-k20-obs-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T05:00:53.917Z\", \"updated_at\": \"2026-05-28T06:46:44.925Z\", \"hypothesis\": \"plan_601 P0: K-sweep K=20 obs-only Object s43. Tests effect of sample budget on CRM refinement quality with larger candidate set.\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.05 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"558360\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-obj-s43.log\", \"submitted_at\": \"2026-05-28T05:01:35.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3938}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-28T06:47:01.264Z_

<details><summary>↩ Tool result · `toolu_01GAMUrHguiVrE2mgM3Ak39G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau025-spatial-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:34.861Z\", \"updated_at\": \"2026-05-28T06:46:54.310Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"112969\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:31.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9404}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "7bd08b44-aad9-4847-99d9-fc078293fa7b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-tau025-spatial-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:34.861Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:46:54.310Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"112969\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:31.846Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}, \\\"hypothesis\\\": \\\"SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.9404}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau025-spatial-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:34.861Z\", \"updated_at\": \"2026-05-28T06:46:54.310Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"112969\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:31.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.25 on Spatial s42. Fills critical tau-sweep gap — spatial s42 missing tau025 data point for sweep curve.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9404}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-28T06:47:11.649Z_

<details><summary>↩ Tool result · `toolu_01MKzFbmLdgaB8KfHeP2mZ2V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau020-spatial-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:43.384Z\", \"updated_at\": \"2026-05-28T06:47:04.930Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"113251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:40.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3707}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "2f51b43d-015f-4dee-a917-473685166eb4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-tau020-spatial-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:43.384Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:47:04.930Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"113251\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:40.430Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}, \\\"hypothesis\\\": \\\"SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.3707}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-tau020-spatial-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:43.384Z\", \"updated_at\": \"2026-05-28T06:47:04.930Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"113251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:40.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"hypothesis\": \"SmolVLA adaptive conformal CRM τ=0.20 on Spatial s42. Second spatial tau-sweep gap fill for denser sweep curve around optimal range.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3707}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-28T06:47:21.014Z_

<details><summary>↩ Tool result · `toolu_014ewvEwTzMTZrLkpPJkEtwZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-28T06:47:14.635Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\", \"reproduce\": {\"finished_at\": \"2026-05-24T05:13:17.230Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-24T05:13:08.597Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:13:37.611636+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 46 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"295725\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s46.log\", \"submitted_at\": \"2026-05-28T05:21:25.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3485}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "567d1c8f-6b79-48ff-ba8e-938c70573b54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T00:32:53.028Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:47:14.635Z\\\", \\\"hypothesis\\\": \\\"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-24T05:13:17.230Z\\\"}, \\\"failure_reason\\\": \\\"\\\", \\\"completed_at\\\": \\\"2026-05-24T05:13:08.597Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-24T05:13:37.611636+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 60.5, \\\"successes\\\": 121, \\\"total\\\": 200, \\\"source\\\": \\\"reviewer_manual_check\\\"}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 46 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"295725\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:21:25.022Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3485}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-28T06:47:14.635Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\", \"reproduce\": {\"finished_at\": \"2026-05-24T05:13:17.230Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-24T05:13:08.597Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:13:37.611636+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 46 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"295725\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s46.log\", \"submitted_at\": \"2026-05-28T05:21:25.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3485}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 196_

<details><summary>Logged reasoning block</summary>

```text
10 out of 11 succeeded. The one that failed is `eval-random-selection-object-seed43-v2` — it needs `checkpoint_source` because it's an eval experiment (has parent). But random_selection mode doesn't use a CRM checkpoint. Let me just add a dummy checkpoint_source.

Status so far:
- 10/11 from PREPARING group → RUNNING ✓
- 1 failed: eval-random-selection-object-seed43-v2 (needs checkpoint_source)
- 9 DONE experiments → PREPARING ✓ (need to continue through PENDING → QUEUED → ALLOCATED → RUNNING)


- For the failed eval experiment, I'll set checkpoint_source to "none (random selection baseline)" to satisfy the registry requirement even though random selection doesn't actually use a checkpoint.
- Now I need to advance the 9 DONE experiments through the remaining four state transitions, which means batching 36 API calls total — starting with moving all 9 from PREPARING to PENDING.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ca0182e5-c523-432d-81a5-640100ad7c8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 197_

10/11 → RUNNING 成功。`eval-random-selection-object-seed43-v2` 需要 `checkpoint_source`。修复它，同时推进 9 个 DONE→PREPARING 到 PENDING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "fd49e323-e1ec-4181-a99a-f95bbd1bb111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 198_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01PbgEEcp1xN7hWWoPeYTLAs`</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed43-v2",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20",
    "server": "bjb1-32546",
    "gpu": [
      "cuda:3"
    ],
    "pid": "550561",
    "model_name": "smolvla",
    "seed": 43,
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "none (random selection baseline)",
    "eval_data": "LIBERO-Object"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "025b2c5b-2c6e-4a52-b226-612a9a7c4b90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 199_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01BdswcWxZfHENrwdXWYZPAz`</summary>

```json
{
  "exp_id": "eval-k2-tau045-spatial-s42-bjb2",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "c2cf0ab0-b79a-4323-a25d-3f024dd80575",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 200_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TZ5Cg7JLVJYm2SVvLiekep`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s46",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "c17e3046-8fc1-468f-a8ca-acc4c02b94d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 201_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01SDko8Cp7HY1iiK3Rp4vYt5`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s42",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "3b5a8742-106d-4b21-b21d-d92c9ec7d503",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 202_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_0168kyCJeCX4CSD4HZgufH9t`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s44",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ae957b97-238f-4385-a0e5-731311b2b7ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 203_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01KnxnmFczFahsz9bMxTGix4`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s42-cqa1",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "1beff2e0-b4e7-4337-be79-7dbb5f190e10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 204_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01MU8gya5EVsXtaKaCntHTVP`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s43-cqa1",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "555602af-e7c6-44d3-a552-7edb600e2fc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 205_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_018zMv5yH53Xrh3E7wYzvKZg`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s44-cqa1",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "6599169c-d3d0-4a16-bb57-20c76c51bd8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 206_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TQ65PfZ3GnkAu2u3tpA22L`</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s47",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "4e1e9ea5-d214-4f62-8367-dc182ff02378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 207_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01JXtz8tsePmrxmsx9yQ2JQj`</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s47",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "78d55a8b-06e7-4f0d-b49a-f7883a9d1769",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3zvpWsYJao5HSG4APkJAW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91078,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91078
      },
      "output_tokens": 29,
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

_source line 208 · 2026-05-28T06:47:44.464Z_

<details><summary>↩ Tool result · `toolu_01PbgEEcp1xN7hWWoPeYTLAs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed43-v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:16.507Z\", \"updated_at\": \"2026-05-28T06:47:37.683Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550561\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"none (random selection baseline)\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\", \"parent\": \"eval-random-selection-object-seed44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7364}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "cf75fce4-cb8b-428f-8c44-61bdcbb62b8a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-random-selection-object-seed43-v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-28T04:45:16.507Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:47:37.683Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"550561\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:13.541Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"none (random selection baseline)\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\\\", \\\"parent\\\": \\\"eval-random-selection-object-seed44\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.7364}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-random-selection-object-seed43-v2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-28T04:45:16.507Z\", \"updated_at\": \"2026-05-28T06:47:37.683Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550561\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"none (random selection baseline)\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on Object seed43. Ablation isolating conformal ranking contribution — if random pick ≈ VLA-only, conformal scoring is the key ingredient.\", \"parent\": \"eval-random-selection-object-seed44\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7364}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-28T06:47:53.694Z_

<details><summary>↩ Tool result · `toolu_01BdswcWxZfHENrwdXWYZPAz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:47:47.486Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2133}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "c0cca740-0147-453d-a7b7-76f6f17b663f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-k2-tau045-spatial-s42-bjb2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T17:02:42.801Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:47:47.486Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:59:18.996Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.081, \\\"mean_uncertainty\\\": 0.195, \\\"total_steps\\\": 28928, \\\"crm_applied_steps\\\": 2329}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2133}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:47:47.486Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2133}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-28T06:48:03.491Z_

<details><summary>↩ Tool result · `toolu_01TZ5Cg7JLVJYm2SVvLiekep`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:47:56.656Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7799}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ec88fc5f-dfdb-41a8-a3ca-f4f77883796c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-spatial-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:47:56.656Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"failure_reason\\\": \\\"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\\\", \\\"completed_at\\\": \\\"2026-05-24T08:27:00.000Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.7799}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:47:56.656Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7799}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-28T06:48:13.808Z_

<details><summary>↩ Tool result · `toolu_01SDko8Cp7HY1iiK3Rp4vYt5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:48:07.042Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.2969}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "12440a90-938b-4335-93a2-112ac52b7922",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T09:25:38.707Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:48:07.042Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\\\", \\\"completed_at\\\": \\\"2026-05-23T14:13:45.028Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.58, \\\"successes\\\": 116, \\\"total\\\": 200}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.2969}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:48:07.042Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.2969}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-28T06:48:23.124Z_

<details><summary>↩ Tool result · `toolu_0168kyCJeCX4CSD4HZgufH9t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:48:16.772Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2941}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "6f1cdf74-c97e-4bdf-bfc4-b9ccff4a7784",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T14:36:41.287Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:48:16.772Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\\\", \\\"completed_at\\\": \\\"2026-05-23T20:09:40.603Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2941}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:48:16.772Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2941}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-28T06:48:32.386Z_

<details><summary>↩ Tool result · `toolu_01KnxnmFczFahsz9bMxTGix4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:48:26.111Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2467}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "e5801614-01ab-4ddb-a678-18723e9c305e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s42-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:41.848Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:48:26.111Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:11.021Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"trigger_rate\\\": 0.171, \\\"mean_correction_norm\\\": 0.171, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35583, \\\"crm_applied_steps\\\": 6096}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2467}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:48:26.111Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2467}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-28T06:48:41.656Z_

<details><summary>↩ Tool result · `toolu_01MU8gya5EVsXtaKaCntHTVP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:48:35.357Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2564}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "525da7bb-eb5b-4ab6-a05b-127cfd4204da",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s43-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:47.612Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:48:35.357Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:30.494Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.174, \\\"mean_correction_norm\\\": 0.168, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35858, \\\"crm_applied_steps\\\": 6239}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2564}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:48:35.357Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2564}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-28T06:48:51.241Z_

<details><summary>↩ Tool result · `toolu_018zMv5yH53Xrh3E7wYzvKZg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:48:44.874Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5725}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "be01c404-01ec-4e89-a567-b3685a390ee2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s44-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:59.424Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:48:44.874Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:47.655Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.735, \\\"trigger_rate\\\": 0.168, \\\"mean_correction_norm\\\": 0.169, \\\"mean_uncertainty\\\": 0.11, \\\"total_steps\\\": 36287, \\\"crm_applied_steps\\\": 6090}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.5725}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:48:44.874Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5725}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-28T06:49:00.593Z_

<details><summary>↩ Tool result · `toolu_01TQ65PfZ3GnkAu2u3tpA22L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:48:54.192Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3395}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "d2a2f360-88eb-4898-8ab1-96bac3d18da0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-adapt-tau025-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:50.342Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:48:54.192Z\\\", \\\"hypothesis\\\": \\\"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:28:20.472Z\\\", \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"total_successes\\\": 158, \\\"total_trials\\\": 200, \\\"mean_uncertainty\\\": 0.1835, \\\"trigger_rate\\\": 0.188, \\\"tau\\\": 0.25, \\\"total_steps\\\": 28642, \\\"crm_applied_steps\\\": 5381}, \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3395}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:48:54.192Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3395}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-28T06:49:11.040Z_

<details><summary>↩ Tool result · `toolu_01JXtz8tsePmrxmsx9yQ2JQj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:49:03.577Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.4336}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "9197227e-f70a-4365-9426-7e512922045a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-k2mean-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:53.820Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:49:03.577Z\\\", \\\"hypothesis\\\": \\\"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:23:58.227Z\\\", \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.82, \\\"total_successes\\\": 164, \\\"total_trials\\\": 200, \\\"note\\\": \\\"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\\\"}, \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.4336}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:49:03.577Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.4336}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 218_

<details><summary>Logged reasoning block</summary>

```text
All 11 from PREPARING group are now RUNNING. All 9 from DONE group are now PENDING.

Now continue 9 DONE→PENDING → QUEUED.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "a628492c-396b-4345-98f2-f8adfb9e5909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 219_

11 个全部 → RUNNING，9 个 → PENDING。继续 PENDING → QUEUED：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "831a07bc-7ee1-456d-a560-630d21d50081",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 220_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01WD3zZmHK94CVJh5Uixt6cZ`</summary>

```json
{
  "exp_id": "eval-k2-tau045-spatial-s42-bjb2",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "42e4c54a-2b50-4592-a224-2aba4a2c08ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 221_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017vcvNvG73wF962BubTG3S4`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s46",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "9560810e-e6c1-4c7d-b387-86ad2ea012e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 222_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01W6bVuKVhXuaseKHES637jG`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s42",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "68f66330-be86-46c2-b08f-a0ba50a75d8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 223_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_013FB4DzxCbZtpTGqxHMkG3t`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s44",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "239cce15-8865-4065-999c-e738bd85c955",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 224_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019P9iCAEuNWhghJfrYpvcfq`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s42-cqa1",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "44389b5e-1c58-4dff-8e60-10f0e954612a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 225_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01YKNfLsFRNe8GBdiuAsuYxr`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s43-cqa1",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "3097e61d-6f79-4b2a-9cba-eb262745f30b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 226_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01LVqsSN6aDMzQgpAKZ3GNMB`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s44-cqa1",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "dae50af9-3cbb-49fe-8e79-c763daecadeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 227_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016nQRwRp2RB9K3bQVmzLsb2`</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s47",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "bf905466-8257-46c8-8239-32bd82b69b21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 228_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_0131ASVeLTxbZMpCYrfNDBhY`</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s47",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "0329511e-7515-4a6c-8a17-d861287db2a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTBCkoEE2bcMnSzsDbh2My",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5866,
      "cache_read_input_tokens": 102529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5866
      },
      "output_tokens": 27,
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

_source line 229 · 2026-05-28T06:49:26.745Z_

<details><summary>↩ Tool result · `toolu_01WD3zZmHK94CVJh5Uixt6cZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:49:20.323Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4625}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "9f0fa61a-a762-4a1b-8d93-a4e02e503e89",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-k2-tau045-spatial-s42-bjb2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T17:02:42.801Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:49:20.323Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:59:18.996Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.081, \\\"mean_uncertainty\\\": 0.195, \\\"total_steps\\\": 28928, \\\"crm_applied_steps\\\": 2329}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4625}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:49:20.323Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4625}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-28T06:49:36.090Z_

<details><summary>↩ Tool result · `toolu_017vcvNvG73wF962BubTG3S4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:49:29.671Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3281}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "103b605e-b731-47e8-855b-3e2bf535ab5f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-spatial-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:49:29.671Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"failure_reason\\\": \\\"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\\\", \\\"completed_at\\\": \\\"2026-05-24T08:27:00.000Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3281}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:49:29.671Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3281}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-28T06:49:45.601Z_

<details><summary>↩ Tool result · `toolu_01W6bVuKVhXuaseKHES637jG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:49:39.006Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4969}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "4499d59c-c3ac-4f50-b18c-ffcab966f2ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T09:25:38.707Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:49:39.006Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\\\", \\\"completed_at\\\": \\\"2026-05-23T14:13:45.028Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.58, \\\"successes\\\": 116, \\\"total\\\": 200}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4969}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:49:39.006Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4969}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-28T06:49:54.893Z_

<details><summary>↩ Tool result · `toolu_013FB4DzxCbZtpTGqxHMkG3t`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:49:48.591Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2792}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "c8c15a35-09ca-4a8f-8e74-08306028fdb1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T14:36:41.287Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:49:48.591Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\\\", \\\"completed_at\\\": \\\"2026-05-23T20:09:40.603Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2792}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:49:48.591Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2792}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-28T06:50:04.163Z_

<details><summary>↩ Tool result · `toolu_019P9iCAEuNWhghJfrYpvcfq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:49:57.823Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2574}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "1145934a-9c75-4c8f-81cd-a40763254aee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s42-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:41.848Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:49:57.823Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:11.021Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"trigger_rate\\\": 0.171, \\\"mean_correction_norm\\\": 0.171, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35583, \\\"crm_applied_steps\\\": 6096}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2574}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:49:57.823Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2574}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-28T06:50:14.888Z_

<details><summary>↩ Tool result · `toolu_01YKNfLsFRNe8GBdiuAsuYxr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:50:07.187Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.7126}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "1be4f12d-f1db-435c-89ec-1214679a746a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s43-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:47.612Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:50:07.187Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:30.494Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.174, \\\"mean_correction_norm\\\": 0.168, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35858, \\\"crm_applied_steps\\\": 6239}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.7126}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:50:07.187Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.7126}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-28T06:50:24.354Z_

<details><summary>↩ Tool result · `toolu_01LVqsSN6aDMzQgpAKZ3GNMB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:50:17.930Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4498}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "3c0d8581-8278-421a-8ffa-c6ee6ea01d0d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s44-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:59.424Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:50:17.930Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:47.655Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.735, \\\"trigger_rate\\\": 0.168, \\\"mean_correction_norm\\\": 0.169, \\\"mean_uncertainty\\\": 0.11, \\\"total_steps\\\": 36287, \\\"crm_applied_steps\\\": 6090}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4498}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:50:17.930Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4498}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-28T06:50:33.567Z_

<details><summary>↩ Tool result · `toolu_016nQRwRp2RB9K3bQVmzLsb2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:50:27.356Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1946}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ca6fdb05-5ede-4b97-bbcc-ccee7f8c35a6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-adapt-tau025-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:50.342Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:50:27.356Z\\\", \\\"hypothesis\\\": \\\"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:28:20.472Z\\\", \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"total_successes\\\": 158, \\\"total_trials\\\": 200, \\\"mean_uncertainty\\\": 0.1835, \\\"trigger_rate\\\": 0.188, \\\"tau\\\": 0.25, \\\"total_steps\\\": 28642, \\\"crm_applied_steps\\\": 5381}, \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.1946}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:50:27.356Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.1946}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-28T06:50:43.070Z_

<details><summary>↩ Tool result · `toolu_0131ASVeLTxbZMpCYrfNDBhY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:50:36.582Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4872}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "03699cfe-30db-455e-8834-d51cdff42fb0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-k2mean-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:53.820Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:50:36.582Z\\\", \\\"hypothesis\\\": \\\"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:23:58.227Z\\\", \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.82, \\\"total_successes\\\": 164, \\\"total_trials\\\": 200, \\\"note\\\": \\\"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\\\"}, \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4872}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:50:36.582Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4872}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 238_

9 个 → QUEUED。继续 QUEUED → ALLOCATED：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "3479beac-a686-4f36-997f-46579ba380f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 239_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012FPVu5jMJF7W4W6wSaZ7mC`</summary>

```json
{
  "exp_id": "eval-k2-tau045-spatial-s42-bjb2",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "cfacf124-61bf-46c6-82bc-c84b40162b31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 240_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01PLAGgEsnTsu8zJTHtP7fhh`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s46",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "a4d29c52-1052-437a-b019-47eada1c477e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 241_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017Gr8fKwRUwTGryLJs2uuXS`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s42",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "48fd5c0c-9957-42e8-8a09-0c17bda911c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 242_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01K2FcVn8Nz4PCvYFpepxjz1`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s44",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "70694511-8c2a-4dae-90fb-ef0393483f1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 243_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Hz9yaGLm8oRSn53xK9uobC`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s42-cqa1",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "35a3ae88-cd0f-4448-b7d7-97adc376ecea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 244_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TgNVGzDGoNEMyx7s7AeaHG`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s43-cqa1",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "7d8b391b-9334-46bd-991f-79d9b30b5166",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 245_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_014nYMJcziWFSpDpqZmM36qa`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s44-cqa1",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "634b4175-c0f2-48ba-b63e-792a3fb9aefe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 246_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01LqfA5XYFgLom1tvqdE8WuP`</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s47",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "953f1e8e-f6ef-4632-a142-7ec74628faed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 247_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_011Uv4jNiRkSTi8U8yMf4PC3`</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s47",
  "field": "status",
  "value": "ALLOCATED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "e43d0030-ce97-4aca-a76b-0494fef248ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeNqPXVVpHfzzSwXUeho3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4835,
      "cache_read_input_tokens": 108395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4835
      },
      "output_tokens": 1,
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

_source line 248 · 2026-05-28T06:50:56.499Z_

<details><summary>↩ Tool result · `toolu_012FPVu5jMJF7W4W6wSaZ7mC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:50:50.034Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4209}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "5d3c9ea0-7054-4261-87a4-0cc1ad052bb1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-k2-tau045-spatial-s42-bjb2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T17:02:42.801Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:50:50.034Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:59:18.996Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.081, \\\"mean_uncertainty\\\": 0.195, \\\"total_steps\\\": 28928, \\\"crm_applied_steps\\\": 2329}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4209}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:50:50.034Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4209}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-28T06:51:05.936Z_

<details><summary>↩ Tool result · `toolu_01PLAGgEsnTsu8zJTHtP7fhh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:50:59.520Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4244}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "2819c921-57ca-4fe8-ad4e-2db17db36912",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-spatial-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:50:59.520Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"failure_reason\\\": \\\"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\\\", \\\"completed_at\\\": \\\"2026-05-24T08:27:00.000Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4244}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:50:59.520Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4244}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-28T06:51:16.586Z_

<details><summary>↩ Tool result · `toolu_017Gr8fKwRUwTGryLJs2uuXS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:51:08.891Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.637}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "1b3bcf34-05eb-4a34-b0f1-238e12e3e1c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T09:25:38.707Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:51:08.891Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\\\", \\\"completed_at\\\": \\\"2026-05-23T14:13:45.028Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.58, \\\"successes\\\": 116, \\\"total\\\": 200}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.637}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:51:08.891Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.637}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-28T06:51:25.958Z_

<details><summary>↩ Tool result · `toolu_01K2FcVn8Nz4PCvYFpepxjz1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:51:19.637Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3601}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "70c956b3-0727-4cca-b4fd-cf79d65503c7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T14:36:41.287Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:51:19.637Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\\\", \\\"completed_at\\\": \\\"2026-05-23T20:09:40.603Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3601}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:51:19.637Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3601}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-28T06:51:35.241Z_

<details><summary>↩ Tool result · `toolu_01Hz9yaGLm8oRSn53xK9uobC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:51:28.891Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2706}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ab09bc56-1c86-4179-8ed1-efab4429db67",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s42-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:41.848Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:51:28.891Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:11.021Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"trigger_rate\\\": 0.171, \\\"mean_correction_norm\\\": 0.171, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35583, \\\"crm_applied_steps\\\": 6096}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2706}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:51:28.891Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2706}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-28T06:51:44.783Z_

<details><summary>↩ Tool result · `toolu_01TgNVGzDGoNEMyx7s7AeaHG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:51:38.158Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5283}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "b8213c0b-665f-4866-a95b-2fda9afb0abd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s43-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:47.612Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:51:38.158Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:30.494Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.174, \\\"mean_correction_norm\\\": 0.168, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35858, \\\"crm_applied_steps\\\": 6239}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.5283}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:51:38.158Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5283}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-28T06:51:53.998Z_

<details><summary>↩ Tool result · `toolu_014nYMJcziWFSpDpqZmM36qa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:51:47.787Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2017}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "fd01e6bc-8cab-4743-9a86-a6049b32df91",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s44-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:59.424Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:51:47.787Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:47.655Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.735, \\\"trigger_rate\\\": 0.168, \\\"mean_correction_norm\\\": 0.169, \\\"mean_uncertainty\\\": 0.11, \\\"total_steps\\\": 36287, \\\"crm_applied_steps\\\": 6090}}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2017}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:51:47.787Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2017}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-28T06:52:03.362Z_

<details><summary>↩ Tool result · `toolu_01LqfA5XYFgLom1tvqdE8WuP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:51:56.975Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3501}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ec86c372-18a4-4ef6-a9fa-a20d9c574d61",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-adapt-tau025-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:50.342Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:51:56.975Z\\\", \\\"hypothesis\\\": \\\"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:28:20.472Z\\\", \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"total_successes\\\": 158, \\\"total_trials\\\": 200, \\\"mean_uncertainty\\\": 0.1835, \\\"trigger_rate\\\": 0.188, \\\"tau\\\": 0.25, \\\"total_steps\\\": 28642, \\\"crm_applied_steps\\\": 5381}, \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3501}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:51:56.975Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3501}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-28T06:52:13.738Z_

<details><summary>↩ Tool result · `toolu_011Uv4jNiRkSTi8U8yMf4PC3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:52:06.303Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3599}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "f80c5a2c-9693-49be-983b-1e08fb531a7e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-k2mean-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:53.820Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:52:06.303Z\\\", \\\"hypothesis\\\": \\\"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:23:58.227Z\\\", \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.82, \\\"total_successes\\\": 164, \\\"total_trials\\\": 200, \\\"note\\\": \\\"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\\\"}, \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\"}}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.3599}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:52:06.303Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3599}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 257_

9 个 → ALLOCATED。最后一步 ALLOCATED → RUNNING：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "0427bbb8-c6cf-4f54-9c10-c75231121cc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 258_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012voinVSribHxKPCKgrMSeA`</summary>

```json
{
  "exp_id": "eval-k2-tau045-spatial-s42-bjb2",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20",
    "server": "bjb2-28827",
    "gpu": [
      "cuda:0"
    ],
    "pid": "120283",
    "model_name": "smolvla",
    "seed": 42,
    "data_path": "LIBERO-Spatial",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Spatial"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "281126ed-d6a8-4ec4-a3f6-06d821db3875",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 259_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_013SxEmcJo9a5nqMyLYXDGRf`</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-spatial-s46",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20",
    "server": "bjb2-28827",
    "gpu": [
      "cuda:1"
    ],
    "pid": "121287",
    "model_name": "smolvla",
    "seed": 46,
    "data_path": "LIBERO-Spatial",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Spatial"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "a13bca5a-b855-4152-9b9d-249135d201b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 260_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_015JNHXPBBrmmpMYWw8m54he`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s42",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20",
    "server": "bjb2-28827",
    "gpu": [
      "cuda:2"
    ],
    "pid": "123017",
    "model_name": "smolvla",
    "seed": 42,
    "data_path": "LIBERO-Long",
    "data_count": 200,
    "eval_data": "LIBERO-Long"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "39731eb2-23f1-4c0a-9624-fd8ae5319fd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 261_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01GAzAZc7nain3pze3jr31Gr`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s44",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20",
    "server": "bjb2-28827",
    "gpu": [
      "cuda:3"
    ],
    "pid": "124427",
    "model_name": "smolvla",
    "seed": 44,
    "data_path": "LIBERO-Long",
    "data_count": 200,
    "eval_data": "LIBERO-Long"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "e34852da-5745-4217-8649-6ab12cc98bb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 262_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EHfTvzJ32qUMEsr1KHpG4X`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s42-cqa1",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20",
    "server": "cqa1-32758",
    "gpu": [
      "cuda:0"
    ],
    "pid": "276842",
    "model_name": "smolvla",
    "seed": 42,
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "112f900c-ae96-4919-870b-e489df112bb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 263 · 2026-05-28T06:52:31.836Z_

<details><summary>↩ Tool result · `toolu_012voinVSribHxKPCKgrMSeA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:52:25.441Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"120283\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3677}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "4332744f-1e77-4daf-8c53-6848d27d51c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-k2-tau045-spatial-s42-bjb2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T17:02:42.801Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:52:25.441Z\\\", \\\"hypothesis\\\": \\\"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:59:18.996Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.081, \\\"mean_uncertainty\\\": 0.195, \\\"total_steps\\\": 28928, \\\"crm_applied_steps\\\": 2329}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"120283\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.3677}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-k2-tau045-spatial-s42-bjb2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T17:02:42.801Z\", \"updated_at\": \"2026-05-28T06:52:25.441Z\", \"hypothesis\": \"K=2 τ-sweep: τ=0.45 Adaptive Conformal on Spatial s42. Higher threshold → less correction → closer to VLA-only. Paper appendix tau sensitivity.\", \"completed_at\": \"2026-05-27T00:59:18.996Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.081, \"mean_uncertainty\": 0.195, \"total_steps\": 28928, \"crm_applied_steps\": 2329}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"120283\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.3677}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 264_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01JKkcB7G8CzpJBt5kG9ojz7`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s43-cqa1",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20",
    "server": "cqa1-32758",
    "gpu": [
      "cuda:1"
    ],
    "pid": "277118",
    "model_name": "smolvla",
    "seed": 43,
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "2063ba8c-6074-4dd4-ba2c-07d8d1f9f6ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 265_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012boJAF9jPVydFMSC65zb32`</summary>

```json
{
  "exp_id": "smolvla-adapt-tau015-object-s44-cqa1",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20",
    "server": "cqa1-32758",
    "gpu": [
      "cuda:2"
    ],
    "pid": "278891",
    "model_name": "smolvla",
    "seed": 44,
    "data_path": "LIBERO-Object",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Object"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "63047c97-1f54-46d4-9add-2981b5df659e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 266_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019n7Gu5uC9N1by8x3Ucq2bZ`</summary>

```json
{
  "exp_id": "eval-supp-spatial-adapt-tau025-s47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20",
    "server": "cqa1-32758",
    "gpu": [
      "cuda:3"
    ],
    "pid": "280038",
    "model_name": "smolvla",
    "seed": 47,
    "data_path": "LIBERO-Spatial",
    "data_count": 200,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt",
    "eval_data": "LIBERO-Spatial"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ee4955c4-01e3-4962-ae53-16b2980b4c42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 267_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TGzq2bHnAPzCiAx53bnGEo`</summary>

```json
{
  "exp_id": "eval-supp-spatial-k2mean-s47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20",
    "server": "cqa1-32758",
    "gpu": [
      "cuda:4"
    ],
    "pid": "281459",
    "model_name": "smolvla",
    "seed": 47,
    "data_path": "LIBERO-Spatial",
    "data_count": 200,
    "eval_data": "LIBERO-Spatial"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "b0c7f382-af84-4a02-98cc-6fc4f2a2f0a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VuybMbfaq7NX51EgBTWRG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4750,
      "cache_read_input_tokens": 113230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4750
      },
      "output_tokens": 1,
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

_source line 268 · 2026-05-28T06:52:41.446Z_

<details><summary>↩ Tool result · `toolu_013SxEmcJo9a5nqMyLYXDGRf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:52:34.942Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"121287\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5964}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "781b1375-9c0e-4f32-bcb8-905da33ae187",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-adapt-tau025-spatial-s46\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:52:34.942Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"failure_reason\\\": \\\"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\\\", \\\"completed_at\\\": \\\"2026-05-24T08:27:00.000Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\"}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"121287\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.5964}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-spatial-s46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-28T06:52:34.942Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"failure_reason\": \"Ghost entry — GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Never actually started despite RUNNING status. No pid, no log_path, no output.\", \"completed_at\": \"2026-05-24T08:27:00.000Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"121287\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5964}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-28T06:52:51.020Z_

<details><summary>↩ Tool result · `toolu_015JNHXPBBrmmpMYWw8m54he`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:52:44.456Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"123017\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5571}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "f71e6db1-f07f-441b-81bb-3be14855f84d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T09:25:38.707Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:52:44.456Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\\\", \\\"completed_at\\\": \\\"2026-05-23T14:13:45.028Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.58, \\\"successes\\\": 116, \\\"total\\\": 200}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"123017\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.5571}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s42\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T09:25:38.707Z\", \"updated_at\": \"2026-05-28T06:52:44.456Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed42. First Long suite experiment. Establishes baseline for CRM comparison using 4-suite CRM checkpoint.\", \"completed_at\": \"2026-05-23T14:13:45.028Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.58, \"successes\": 116, \"total\": 200}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"123017\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.5571}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-28T06:53:00.321Z_

<details><summary>↩ Tool result · `toolu_01GAzAZc7nain3pze3jr31Gr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:52:53.976Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"124427\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2866}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "6535b7dc-de28-458a-851f-5d4ed6bcf667",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s44\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-23T14:36:41.287Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:52:53.976Z\\\", \\\"hypothesis\\\": \\\"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\\\", \\\"completed_at\\\": \\\"2026-05-23T20:09:40.603Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SR\\\": 0.565}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"124427\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.2866}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s44\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-28T06:52:53.976Z\", \"hypothesis\": \"SmolVLA VLA-only baseline on LIBERO-Long seed 44. Only s42/s43/s46 done; s44 fills missing seed in Long baseline sweep for paired Long Adaptive/CRM comparisons.\", \"completed_at\": \"2026-05-23T20:09:40.603Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.565}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"124427\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.2866}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-28T06:53:09.794Z_

<details><summary>↩ Tool result · `toolu_01EHfTvzJ32qUMEsr1KHpG4X`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:53:03.274Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"276842\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4601}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "4c19db07-26a0-485b-971e-a1673baee8a9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s42-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:41.848Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:53:03.274Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:11.021Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"trigger_rate\\\": 0.171, \\\"mean_correction_norm\\\": 0.171, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35583, \\\"crm_applied_steps\\\": 6096}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"276842\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4601}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s42-cqa1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:41.848Z\", \"updated_at\": \"2026-05-28T06:53:03.274Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:11.021Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.79, \"trigger_rate\": 0.171, \"mean_correction_norm\": 0.171, \"mean_uncertainty\": 0.112, \"total_steps\": 35583, \"crm_applied_steps\": 6096}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"276842\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4601}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 272 · 2026-05-28T06:53:20.580Z_

<details><summary>↩ Tool result · `toolu_01JKkcB7G8CzpJBt5kG9ojz7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:53:12.785Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"277118\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.7726}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "20ad0423-38fb-4369-b47c-c97409455907",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s43-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:47.612Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:53:12.785Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:30.494Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.78, \\\"trigger_rate\\\": 0.174, \\\"mean_correction_norm\\\": 0.168, \\\"mean_uncertainty\\\": 0.112, \\\"total_steps\\\": 35858, \\\"crm_applied_steps\\\": 6239}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"277118\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.7726}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s43-cqa1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:47.612Z\", \"updated_at\": \"2026-05-28T06:53:12.785Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:30.494Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.78, \"trigger_rate\": 0.174, \"mean_correction_norm\": 0.168, \"mean_uncertainty\": 0.112, \"total_steps\": 35858, \"crm_applied_steps\": 6239}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"277118\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.7726}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-28T06:53:30.030Z_

<details><summary>↩ Tool result · `toolu_012boJAF9jPVydFMSC65zb32`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:53:23.653Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"278891\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4352}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "e54b5464-a49b-446f-8503-18546b023a1c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"smolvla-adapt-tau015-object-s44-cqa1\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-26T16:48:59.424Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:53:23.653Z\\\", \\\"hypothesis\\\": \\\"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\\\", \\\"completed_at\\\": \\\"2026-05-27T00:58:47.655Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.735, \\\"trigger_rate\\\": 0.168, \\\"mean_correction_norm\\\": 0.169, \\\"mean_uncertainty\\\": 0.11, \\\"total_steps\\\": 36287, \\\"crm_applied_steps\\\": 6090}}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"278891\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.4352}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"smolvla-adapt-tau015-object-s44-cqa1\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-26T16:48:59.424Z\", \"updated_at\": \"2026-05-28T06:53:23.653Z\", \"hypothesis\": \"Adaptive Conformal CRM with τ=0.15 (lower threshold → higher trigger rate) on SmolVLA LIBERO-Object should yield higher trigger rate than τ=0.25 spatial sweep (~5%) while improving over CRM-always (K=2, ε=0.05) baseline. Tests whether SmolVLA's Object suite benefits from more frequent uncertainty-gated corrections than Spatial.\", \"completed_at\": \"2026-05-27T00:58:47.655Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.735, \"trigger_rate\": 0.168, \"mean_correction_norm\": 0.169, \"mean_uncertainty\": 0.11, \"total_steps\": 36287, \"crm_applied_steps\": 6090}}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"278891\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.4352}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-28T06:53:39.383Z_

<details><summary>↩ Tool result · `toolu_019n7Gu5uC9N1by8x3Ucq2bZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:53:32.988Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"pid\": \"280038\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "271c9d75-4df4-41e6-be22-622a031e9f1e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-adapt-tau025-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:50.342Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:53:32.988Z\\\", \\\"hypothesis\\\": \\\"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:28:20.472Z\\\", \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.79, \\\"total_successes\\\": 158, \\\"total_trials\\\": 200, \\\"mean_uncertainty\\\": 0.1835, \\\"trigger_rate\\\": 0.188, \\\"tau\\\": 0.25, \\\"total_steps\\\": 28642, \\\"crm_applied_steps\\\": 5381}, \\\"notes\\\": \\\"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\\\"}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"280038\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-adapt-tau025-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:50.342Z\", \"updated_at\": \"2026-05-28T06:53:32.988Z\", \"hypothesis\": \"Adaptive conformal CRM gating (tau=0.25) on LIBERO-Spatial at seed 47 extends seed coverage and confirms gating effectiveness on highest-trigger-rate suite.\", \"completed_at\": \"2026-05-24T13:28:20.472Z\", \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\", \"extra\": {\"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.79, \"total_successes\": 158, \"total_trials\": 200, \"mean_uncertainty\": 0.1835, \"trigger_rate\": 0.188, \"tau\": 0.25, \"total_steps\": 28642, \"crm_applied_steps\": 5381}, \"notes\": \"SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4), K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed. Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2, SR=81.5%).\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"pid\": \"280038\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.34}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-28T06:53:49.070Z_

<details><summary>↩ Tool result · `toolu_01TGzq2bHnAPzCiAx53bnGEo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:53:42.345Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"281459\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.6736}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "d843fa8f-d9b2-4512-b8a5-4dd7ba985355",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-spatial-k2mean-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-24T10:58:53.820Z\\\", \\\"updated_at\\\": \\\"2026-05-28T06:53:42.345Z\\\", \\\"hypothesis\\\": \\\"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\\\", \\\"completed_at\\\": \\\"2026-05-24T13:23:58.227Z\\\", \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.82, \\\"total_successes\\\": 164, \\\"total_trials\\\": 200, \\\"note\\\": \\\"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\\\"}, \\\"notes\\\": \\\"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\\\"}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"281459\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.6736}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-spatial-k2mean-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-24T10:58:53.820Z\", \"updated_at\": \"2026-05-28T06:53:42.345Z\", \"hypothesis\": \"K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for seed-extension coverage of the naive averaging baseline.\", \"completed_at\": \"2026-05-24T13:23:58.227Z\", \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.82, \"total_successes\": 164, \"total_trials\": 200, \"note\": \"per-task data lost due to JSON overwrite by vla-only (same output filename bug M083)\"}, \"notes\": \"WARNING: per-task JSON was overwritten by eval-supp-spatial-vla-only-s47 (same output filename bug). SR=82% (164/200) confirmed from earlier harvest log, but per-task breakdown unrecoverable. BUG FIX: evaluate.py patched (commit 63f5c81 on cqa1-32758) — baseline_mode=mean now outputs to eval_{benchmark}_k{K}mean_seed{seed}.json.\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"281459\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.6736}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 276_

<details><summary>Logged reasoning block</summary>

```text
All 20 experiments are now RUNNING in the registry. Let me verify by querying the registry for RUNNING status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "5e49bbac-30f7-4b73-8762-3edaef0855ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHBzChbdpAgP5dPJg3puVz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8000,
      "cache_read_input_tokens": 117980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8000
      },
      "output_tokens": 25,
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

_source line 277_

全部 20 个实验已成功更新为 RUNNING。验证一下：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "831d8a05-5eb0-4e7c-ae5a-ae5c8197389a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHBzChbdpAgP5dPJg3puVz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8000,
      "cache_read_input_tokens": 117980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8000
      },
      "output_tokens": 25,
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

_source line 278_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EUtvJ4mfMh33HZegnQd8UT`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "exp_id",
    "status",
    "spec"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "3a47cf8c-7a3b-4382-b24f-dc4aca3941c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHBzChbdpAgP5dPJg3puVz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8000,
      "cache_read_input_tokens": 117980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8000
      },
      "output_tokens": 25,
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

_source line 279 · 2026-05-28T06:54:00.052Z_

<details><summary>↩ Tool result · `toolu_01EUtvJ4mfMh33HZegnQd8UT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-k2mean-s47\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"281459\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"pid\": \"280038\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"smolvla-adapt-tau015-object-s44-cqa1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"278891\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"smolvla-adapt-tau015-object-s43-cqa1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"277118\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"smolvla-adapt-tau015-object-s42-cqa1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"276842\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-supp-long-vla-only-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"124427\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}, \"eval-supp-long-vla-only-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"123017\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"121287\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-k2-tau045-spatial-s42-bjb2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"120283\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-random-selection-object-seed43-v2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550561\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"none (random selection baseline)\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 46 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"295725\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s46.log\", \"submitted_at\": \"2026-05-28T05:21:25.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}, \"smolvla-tau020-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"113251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:40.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"smolvla-tau025-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"112969\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:31.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-ksweep-k20-obs-obj-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.05 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"558360\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-obj-s43.log\", \"submitted_at\": \"2026-05-28T05:01:35.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-ksweep-k20-obs-object-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550841\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"pi05-crm-always-on-object-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"511001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log\", \"submitted_at\": \"2026-05-28T03:12:00.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"pi05-crm-always-on-goal-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"510709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log\", \"submitted_at\": \"2026-05-28T03:11:44.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}, \"pi05-crm-always-on-goal-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"510343\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log\", \"submitted_at\": \"2026-05-28T03:11:27.187Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 43, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}, \"pi05-crm-always-on-long-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"983106\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log\", \"submitted_at\": \"2026-05-28T03:11:36.967Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}}, \"pi05-crm-always-on-long-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 43 --n_rollouts 20\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"982389\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log\", \"submitted_at\": \"2026-05-28T03:11:08.339Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 43, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}}}, \"count\": 20, \"total\": 20, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9971}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ccac8471-a520-4614-ac5f-057400b8e22b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-spatial-k2mean-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"281459\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}, \\\"eval-supp-spatial-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"280038\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 47, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}, \\\"smolvla-adapt-tau015-object-s44-cqa1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"278891\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"smolvla-adapt-tau015-object-s43-cqa1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"277118\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"smolvla-adapt-tau015-object-s42-cqa1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"276842\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"124427\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}, \\\"eval-supp-long-vla-only-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"123017\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"121287\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}, \\\"eval-k2-tau045-spatial-s42-bjb2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"120283\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}, \\\"eval-random-selection-object-seed43-v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"550561\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:13.541Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"none (random selection baseline)\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-supp-long-vla-only-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 46 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"295725\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:21:25.022Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}, \\\"smolvla-tau020-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"113251\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:40.430Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}, \\\"smolvla-tau025-spatial-s42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"112969\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:31.846Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}}, \\\"eval-ksweep-k20-obs-obj-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.05 --benchmark object --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"558360\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-obj-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T05:01:35.230Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-ksweep-k20-obs-object-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"550841\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T04:45:22.258Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"pi05-crm-always-on-object-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"511001\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:12:00.314Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"pi05-crm-always-on-goal-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark goal --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"510709\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:11:44.785Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal\\\"}}, \\\"pi05-crm-always-on-goal-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark goal --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"510343\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:11:27.187Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Goal\\\"}}, \\\"pi05-crm-always-on-long-s44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 44 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"983106\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:11:36.967Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 44, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}, \\\"pi05-crm-always-on-long-s43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 43 --n_rollouts 20\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"982389\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log\\\", \\\"submitted_at\\\": \\\"2026-05-28T03:11:08.339Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"pi05\\\", \\\"seed\\\": 43, \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Long\\\"}}}, \\\"count\\\": 20, \\\"total\\\": 20, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.9971}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-spatial-k2mean-s47\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"281459\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-supp-spatial-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"pid\": \"280038\", \"model_name\": \"smolvla\", \"seed\": 47, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"smolvla-adapt-tau015-object-s44-cqa1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"pid\": \"278891\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"smolvla-adapt-tau015-object-s43-cqa1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"pid\": \"277118\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"smolvla-adapt-tau015-object-s42-cqa1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.15 --benchmark object --seed 42 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"pid\": \"276842\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-supp-long-vla-only-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"124427\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}, \"eval-supp-long-vla-only-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"123017\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 46 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"121287\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-k2-tau045-spatial-s42-bjb2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.45 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"120283\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-random-selection-object-seed43-v2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode random_selection --benchmark object --K 10 --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"550561\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43-v2.log\", \"submitted_at\": \"2026-05-28T04:45:13.541Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"none (random selection baseline)\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-supp-long-vla-only-s46\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode vla_only --baseline_mode single --K 1 --benchmark long --seed 46 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"pid\": \"295725\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s46.log\", \"submitted_at\": \"2026-05-28T05:21:25.022Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 46, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\"}}, \"smolvla-tau020-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.20 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"113251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau020-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:40.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"smolvla-tau025-spatial-s42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"112969\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/smolvla-tau025-spatial-s42.log\", \"submitted_at\": \"2026-05-28T04:45:31.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 42, \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}}, \"eval-ksweep-k20-obs-obj-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.05 --benchmark object --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"558360\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-obj-s43.log\", \"submitted_at\": \"2026-05-28T05:01:35.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-ksweep-k20-obs-object-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model smolvla --mode crm_obs_only --K 20 --max_correction_norm 0.2 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"550841\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-ksweep-k20-obs-object-s44.log\", \"submitted_at\": \"2026-05-28T04:45:22.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"smolvla\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"pi05-crm-always-on-object-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark object --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"511001\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-object-s44.log\", \"submitted_at\": \"2026-05-28T03:12:00.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"pi05-crm-always-on-goal-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"510709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s44.log\", \"submitted_at\": \"2026-05-28T03:11:44.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}, \"pi05-crm-always-on-goal-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark goal --seed 43 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"510343\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-goal-s43.log\", \"submitted_at\": \"2026-05-28T03:11:27.187Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 43, \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}, \"pi05-crm-always-on-long-s44\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 44 --n_rollouts 20\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"983106\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s44.log\", \"submitted_at\": \"2026-05-28T03:11:36.967Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}}, \"pi05-crm-always-on-long-s43\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --conformal_threshold 0.001 --benchmark long --seed 43 --n_rollouts 20\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"982389\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/pi05-crm-always-on-long-s43.log\", \"submitted_at\": \"2026-05-28T03:11:08.339Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pi05\", \"seed\": 43, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt\", \"eval_data\": \"LIBERO-Long\"}}}, \"count\": 20, \"total\": 20, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9971}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 280_

Registry 确认 **20 个 RUNNING**。全部补登完成。

## 汇总

| 服务器 | 实验数 | GPU 分配 | exp_id 列表 |
|--------|--------|----------|-------------|
| **bjb1-18228** | 2 | GPU 0, 2 | `pi05-crm-always-on-long-s43` (PID 982389, cuda:0), `pi05-crm-always-on-long-s44` (PID 983106, cuda:2) |
| **bjb1-32546** | 6 | GPU 0-5 | `pi05-crm-always-on-goal-s43` (510343, cuda:0), `pi05-crm-always-on-goal-s44` (510709, cuda:1), `pi05-crm-always-on-object-s44` (511001, cuda:2), `eval-random-selection-object-seed43-v2` (550561, cuda:3), `eval-ksweep-k20-obs-object-s44` (550841, cuda:4), `eval-ksweep-k20-obs-obj-s43` (558360, cuda:5) |
| **bjb2-28827** | 6 | GPU 0-5 | `eval-k2-tau045-spatial-s42-bjb2` (120283, cuda:0), `eval-supp-adapt-tau025-spatial-s46` (121287, cuda:1), `eval-supp-long-vla-only-s42` (123017, cuda:2), `eval-supp-long-vla-only-s44` (124427, cuda:3), `smolvla-tau025-spatial-s42` (112969, cuda:4), `smolvla-tau020-spatial-s42` (113251, cuda:5) |
| **cqa1-32758** | 6 | GPU 0-5 | `smolvla-adapt-tau015-object-s42-cqa1` (276842, cuda:0), `smolvla-adapt-tau015-object-s43-cqa1` (277118, cuda:1), `smolvla-adapt-tau015-object-s44-cqa1` (278891, cuda:2), `eval-supp-spatial-adapt-tau025-s47` (280038, cuda:3), `eval-supp-spatial-k2mean-s47` (281459, cuda:4), `eval-supp-long-vla-only-s46` (295725, cuda:5) |

**合计 20 个实验 / 20 GPU RUNNING**。bjb1-18228 的 GPU 1 和 GPU 3 空闲（共 4 卡只用了 2 张）。11 个从 PREPARING 推进，9 个从 DONE 重置后推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "uuid": "ed965527-4d46-442d-b4b3-7e54225f294f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7tgdQvNQUTXguBbtX9oyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5625,
      "cache_read_input_tokens": 125980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5625
      },
      "output_tokens": 1,
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

_source line 281_

Registry 确认 **20 个 RUNNING**。全部补登完成。

## 汇总

| 服务器 | 实验数 | GPU 分配 | exp_id 列表 |
|--------|--------|----------|-------------|
| **bjb1-18228** | 2 | GPU 0, 2 | `pi05-crm-always-on-long-s43` (PID 982389, cuda:0), `pi05-crm-always-on-long-s44` (PID 983106, cuda:2) |
| **bjb1-32546** | 6 | GPU 0-5 | `pi05-crm-always-on-goal-s43` (510343, cuda:0), `pi05-crm-always-on-goal-s44` (510709, cuda:1), `pi05-crm-always-on-object-s44` (511001, cuda:2), `eval-random-selection-object-seed43-v2` (550561, cuda:3), `eval-ksweep-k20-obs-object-s44` (550841, cuda:4), `eval-ksweep-k20-obs-obj-s43` (558360, cuda:5) |
| **bjb2-28827** | 6 | GPU 0-5 | `eval-k2-tau045-spatial-s42-bjb2` (120283, cuda:0), `eval-supp-adapt-tau025-spatial-s46` (121287, cuda:1), `eval-supp-long-vla-only-s42` (123017, cuda:2), `eval-supp-long-vla-only-s44` (124427, cuda:3), `smolvla-tau025-spatial-s42` (112969, cuda:4), `smolvla-tau020-spatial-s42` (113251, cuda:5) |
| **cqa1-32758** | 6 | GPU 0-5 | `smolvla-adapt-tau015-object-s42-cqa1` (276842, cuda:0), `smolvla-adapt-tau015-object-s43-cqa1` (277118, cuda:1), `smolvla-adapt-tau015-object-s44-cqa1` (278891, cuda:2), `eval-supp-spatial-adapt-tau025-s47` (280038, cuda:3), `eval-supp-spatial-k2mean-s47` (281459, cuda:4), `eval-supp-long-vla-only-s46` (295725, cuda:5) |

**合计 20 个实验 / 20 GPU RUNNING**。bjb1-18228 的 GPU 1 和 GPU 3 空闲（共 4 卡只用了 2 张）。11 个从 PREPARING 推进，9 个从 DONE 重置后推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1298226,
  "duration_api_ms": 449403,
  "num_turns": 123,
  "stop_reason": "end_turn",
  "session_id": "c38b3ed1-4f8e-421c-9cfc-ea7c3dc6a06b",
  "total_cost_usd": 4.124687,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 436010,
    "cache_read_input_tokens": 919537,
    "output_tokens": 37506,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 436010,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 737,
        "cache_read_input_tokens": 125980,
        "cache_creation_input_tokens": 5625,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5625
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2006,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002086,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 37506,
      "cacheReadInputTokens": 919537,
      "cacheCreationInputTokens": 436010,
      "webSearchRequests": 0,
      "costUSD": 4.1226009999999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8325b056-8ef7-41c6-a72d-7c1e3d1277cc"
}
```

</details>

---
