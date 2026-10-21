# debug exp6 vanilla inconsistency — Part 2 of 2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../debug-exp6-vanilla-inconsistency.md) · [Structured JSON](../../../sessions/a4/a432c97a2ce6da98cfc6.json)

## Before a recorded user message

### Tool result

_source line 192 · 2026-05-18T14:59:18.515Z_

<details><summary>↩ Tool result · `toolu_018rd9WR1RGsBZwcrW7i4aBP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp6_actorattack_perturbation\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:37:28.933Z\", \"updated_at\": \"2026-05-18T14:59:18.390Z\", \"hypothesis\": \"Classification-supervised variants (9-class/binary/scrambled) will maintain near-zero perturbation degradation on ActorAttack OOD paraphrased data, while vanilla/MLM variants will show significant degradation, extending Claim 3 perturbation robustness from DD to a second OOD attack type\", \"parent\": \"exp4_dd_ood_perturbation\", \"spec\": {\"command\": \"python src/exp6_actorattack_perturbation.py --skip_perturb\", \"server\": \"westd-33183\", \"data_path\": \"data/actorattack_perturbed/perturbed.jsonl\", \"data_count\": 118, \"model_name\": \"deberta-v3-base (7 variants x 3 seeds)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/ (7 variants x 3 seeds)\", \"eval_data\": \"data/actorattack_perturbed/perturbed.jsonl + data/generated/actorattack_all.jsonl\"}, \"checkpoint_path\": \"results/exp6_actorattack_perturbation.json\", \"log_path\": \"logs/exp6_eval.log\", \"conclusion\": \"negative\", \"metrics\": {\"9class_3seed\": {\"clean_k1\": 0.7728, \"perturbed_k1\": 0.6326, \"delta_k1\": -0.1402, \"clean_k3\": 0.9212, \"perturbed_k3\": 0.7337, \"delta_k3\": -0.1875, \"clean_full\": 0.9719, \"perturbed_full\": 0.7681, \"delta_full\": -0.2038}, \"binary_3seed\": {\"clean_k1\": 0.737, \"perturbed_k1\": 0.6694, \"delta_k1\": -0.0676, \"clean_k3\": 0.9508, \"perturbed_k3\": 0.7035, \"delta_k3\": -0.2473, \"clean_full\": 0.9904, \"perturbed_full\": 0.7405, \"delta_full\": -0.2499}, \"scrambled_3seed\": {\"clean_k1\": 0.7206, \"perturbed_k1\": 0.6164, \"delta_k1\": -0.1042, \"clean_k3\": 0.8931, \"perturbed_k3\": 0.7779, \"delta_k3\": -0.1152, \"clean_full\": 0.9511, \"perturbed_full\": 0.7787, \"delta_full\": -0.1724}, \"jb_mlm_3seed\": {\"clean_k1\": 0.7363, \"perturbed_k1\": 0.6572, \"delta_k1\": -0.079, \"clean_k3\": 0.9446, \"perturbed_k3\": 0.5483, \"delta_k3\": -0.3962, \"clean_full\": 0.8934, \"perturbed_full\": 0.5408, \"delta_full\": -0.3526}, \"wiki_mlm_3seed\": {\"clean_k1\": 0.6559, \"perturbed_k1\": 0.6007, \"delta_k1\": -0.0552, \"clean_k3\": 0.6931, \"perturbed_k3\": 0.5216, \"delta_k3\": -0.1716, \"clean_full\": 0.686, \"perturbed_full\": 0.5454, \"delta_full\": -0.1406}, \"topic_3seed\": {\"clean_k1\": 0.5135, \"perturbed_k1\": 0.5258, \"delta_k1\": 0.0123, \"clean_k3\": 0.5654, \"perturbed_k3\": 0.5413, \"delta_k3\": -0.0241, \"clean_full\": 0.6254, \"perturbed_full\": 0.5767, \"delta_full\": -0.0488}, \"vanilla_3seed\": {\"clean_k1\": 0.3374, \"perturbed_k1\": 0.2694, \"delta_k1\": -0.0681, \"clean_k3\": 0.2844, \"perturbed_k3\": 0.2574, \"delta_k3\": -0.027, \"clean_full\": 0.2575, \"perturbed_full\": 0.2482, \"delta_full\": -0.0093}, \"mcnemar_perturbed_k1\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 2e-05, \"b\": 34, \"c\": 6}, \"seed123\": {\"p\": 1.9e-05, \"b\": 59, \"c\": 20}, \"seed456\": {\"p\": 0, \"b\": 72, \"c\": 19}}}, \"mcnemar_perturbed_full\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 0, \"b\": 44, \"c\": 0}, \"seed123\": {\"p\": 0, \"b\": 75, \"c\": 4}, \"seed456\": {\"p\": 0, \"b\": 78, \"c\": 24}}}, \"mcnemar_clean_k1\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 0, \"b\": 52, \"c\": 4}, \"seed123\": {\"p\": 0, \"b\": 42, \"c\": 3}, \"seed456\": {\"p\": 0, \"b\": 53, \"c\": 0}}}, \"mcnemar_clean_full\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 0, \"b\": 78, \"c\": 0}, \"seed123\": {\"p\": 0, \"b\": 72, \"c\": 0}, \"seed456\": {\"p\": 0, \"b\": 78, \"c\": 0}}}, \"note\": \"CORRECTED 2026-05-18: vanilla seed123/456 GRU checkpoints and binary seed42 DeBERTa+GRU checkpoints were wrong (used different models than exp2). Fixed to match exp2 checkpoints. Clean baselines now consistent with exp2. All variants still degrade under perturbation except topic at K=1. 9class significantly outperforms vanilla on both clean and perturbed (McNemar all p<0.001).\"}, \"completed_at\": \"2026-05-18T14:34:19.399Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5426}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f1928031-eb37-4f7e-8032-2a8b1f2c7474",
  "uuid": "2c48a07f-119a-4734-9ea5-7b74623bed07",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp6_actorattack_perturbation\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T13:37:28.933Z\\\", \\\"updated_at\\\": \\\"2026-05-18T14:59:18.390Z\\\", \\\"hypothesis\\\": \\\"Classification-supervised variants (9-class/binary/scrambled) will maintain near-zero perturbation degradation on ActorAttack OOD paraphrased data, while vanilla/MLM variants will show significant degradation, extending Claim 3 perturbation robustness from DD to a second OOD attack type\\\", \\\"parent\\\": \\\"exp4_dd_ood_perturbation\\\", \\\"spec\\\": {\\\"command\\\": \\\"python src/exp6_actorattack_perturbation.py --skip_perturb\\\", \\\"server\\\": \\\"westd-33183\\\", \\\"data_path\\\": \\\"data/actorattack_perturbed/perturbed.jsonl\\\", \\\"data_count\\\": 118, \\\"model_name\\\": \\\"deberta-v3-base (7 variants x 3 seeds)\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"checkpoints/ (7 variants x 3 seeds)\\\", \\\"eval_data\\\": \\\"data/actorattack_perturbed/perturbed.jsonl + data/generated/actorattack_all.jsonl\\\"}, \\\"checkpoint_path\\\": \\\"results/exp6_actorattack_perturbation.json\\\", \\\"log_path\\\": \\\"logs/exp6_eval.log\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"9class_3seed\\\": {\\\"clean_k1\\\": 0.7728, \\\"perturbed_k1\\\": 0.6326, \\\"delta_k1\\\": -0.1402, \\\"clean_k3\\\": 0.9212, \\\"perturbed_k3\\\": 0.7337, \\\"delta_k3\\\": -0.1875, \\\"clean_full\\\": 0.9719, \\\"perturbed_full\\\": 0.7681, \\\"delta_full\\\": -0.2038}, \\\"binary_3seed\\\": {\\\"clean_k1\\\": 0.737, \\\"perturbed_k1\\\": 0.6694, \\\"delta_k1\\\": -0.0676, \\\"clean_k3\\\": 0.9508, \\\"perturbed_k3\\\": 0.7035, \\\"delta_k3\\\": -0.2473, \\\"clean_full\\\": 0.9904, \\\"perturbed_full\\\": 0.7405, \\\"delta_full\\\": -0.2499}, \\\"scrambled_3seed\\\": {\\\"clean_k1\\\": 0.7206, \\\"perturbed_k1\\\": 0.6164, \\\"delta_k1\\\": -0.1042, \\\"clean_k3\\\": 0.8931, \\\"perturbed_k3\\\": 0.7779, \\\"delta_k3\\\": -0.1152, \\\"clean_full\\\": 0.9511, \\\"perturbed_full\\\": 0.7787, \\\"delta_full\\\": -0.1724}, \\\"jb_mlm_3seed\\\": {\\\"clean_k1\\\": 0.7363, \\\"perturbed_k1\\\": 0.6572, \\\"delta_k1\\\": -0.079, \\\"clean_k3\\\": 0.9446, \\\"perturbed_k3\\\": 0.5483, \\\"delta_k3\\\": -0.3962, \\\"clean_full\\\": 0.8934, \\\"perturbed_full\\\": 0.5408, \\\"delta_full\\\": -0.3526}, \\\"wiki_mlm_3seed\\\": {\\\"clean_k1\\\": 0.6559, \\\"perturbed_k1\\\": 0.6007, \\\"delta_k1\\\": -0.0552, \\\"clean_k3\\\": 0.6931, \\\"perturbed_k3\\\": 0.5216, \\\"delta_k3\\\": -0.1716, \\\"clean_full\\\": 0.686, \\\"perturbed_full\\\": 0.5454, \\\"delta_full\\\": -0.1406}, \\\"topic_3seed\\\": {\\\"clean_k1\\\": 0.5135, \\\"perturbed_k1\\\": 0.5258, \\\"delta_k1\\\": 0.0123, \\\"clean_k3\\\": 0.5654, \\\"perturbed_k3\\\": 0.5413, \\\"delta_k3\\\": -0.0241, \\\"clean_full\\\": 0.6254, \\\"perturbed_full\\\": 0.5767, \\\"delta_full\\\": -0.0488}, \\\"vanilla_3seed\\\": {\\\"clean_k1\\\": 0.3374, \\\"perturbed_k1\\\": 0.2694, \\\"delta_k1\\\": -0.0681, \\\"clean_k3\\\": 0.2844, \\\"perturbed_k3\\\": 0.2574, \\\"delta_k3\\\": -0.027, \\\"clean_full\\\": 0.2575, \\\"perturbed_full\\\": 0.2482, \\\"delta_full\\\": -0.0093}, \\\"mcnemar_perturbed_k1\\\": {\\\"9class_vs_vanilla\\\": {\\\"seed42\\\": {\\\"p\\\": 2e-05, \\\"b\\\": 34, \\\"c\\\": 6}, \\\"seed123\\\": {\\\"p\\\": 1.9e-05, \\\"b\\\": 59, \\\"c\\\": 20}, \\\"seed456\\\": {\\\"p\\\": 0, \\\"b\\\": 72, \\\"c\\\": 19}}}, \\\"mcnemar_perturbed_full\\\": {\\\"9class_vs_vanilla\\\": {\\\"seed42\\\": {\\\"p\\\": 0, \\\"b\\\": 44, \\\"c\\\": 0}, \\\"seed123\\\": {\\\"p\\\": 0, \\\"b\\\": 75, \\\"c\\\": 4}, \\\"seed456\\\": {\\\"p\\\": 0, \\\"b\\\": 78, \\\"c\\\": 24}}}, \\\"mcnemar_clean_k1\\\": {\\\"9class_vs_vanilla\\\": {\\\"seed42\\\": {\\\"p\\\": 0, \\\"b\\\": 52, \\\"c\\\": 4}, \\\"seed123\\\": {\\\"p\\\": 0, \\\"b\\\": 42, \\\"c\\\": 3}, \\\"seed456\\\": {\\\"p\\\": 0, \\\"b\\\": 53, \\\"c\\\": 0}}}, \\\"mcnemar_clean_full\\\": {\\\"9class_vs_vanilla\\\": {\\\"seed42\\\": {\\\"p\\\": 0, \\\"b\\\": 78, \\\"c\\\": 0}, \\\"seed123\\\": {\\\"p\\\": 0, \\\"b\\\": 72, \\\"c\\\": 0}, \\\"seed456\\\": {\\\"p\\\": 0, \\\"b\\\": 78, \\\"c\\\": 0}}}, \\\"note\\\": \\\"CORRECTED 2026-05-18: vanilla seed123/456 GRU checkpoints and binary seed42 DeBERTa+GRU checkpoints were wrong (used different models than exp2). Fixed to match exp2 checkpoints. Clean baselines now consistent with exp2. All variants still degrade under perturbation except topic at K=1. 9class significantly outperforms vanilla on both clean and perturbed (McNemar all p<0.001).\\\"}, \\\"completed_at\\\": \\\"2026-05-18T14:34:19.399Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5426}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp6_actorattack_perturbation\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:37:28.933Z\", \"updated_at\": \"2026-05-18T14:59:18.390Z\", \"hypothesis\": \"Classification-supervised variants (9-class/binary/scrambled) will maintain near-zero perturbation degradation on ActorAttack OOD paraphrased data, while vanilla/MLM variants will show significant degradation, extending Claim 3 perturbation robustness from DD to a second OOD attack type\", \"parent\": \"exp4_dd_ood_perturbation\", \"spec\": {\"command\": \"python src/exp6_actorattack_perturbation.py --skip_perturb\", \"server\": \"westd-33183\", \"data_path\": \"data/actorattack_perturbed/perturbed.jsonl\", \"data_count\": 118, \"model_name\": \"deberta-v3-base (7 variants x 3 seeds)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/ (7 variants x 3 seeds)\", \"eval_data\": \"data/actorattack_perturbed/perturbed.jsonl + data/generated/actorattack_all.jsonl\"}, \"checkpoint_path\": \"results/exp6_actorattack_perturbation.json\", \"log_path\": \"logs/exp6_eval.log\", \"conclusion\": \"negative\", \"metrics\": {\"9class_3seed\": {\"clean_k1\": 0.7728, \"perturbed_k1\": 0.6326, \"delta_k1\": -0.1402, \"clean_k3\": 0.9212, \"perturbed_k3\": 0.7337, \"delta_k3\": -0.1875, \"clean_full\": 0.9719, \"perturbed_full\": 0.7681, \"delta_full\": -0.2038}, \"binary_3seed\": {\"clean_k1\": 0.737, \"perturbed_k1\": 0.6694, \"delta_k1\": -0.0676, \"clean_k3\": 0.9508, \"perturbed_k3\": 0.7035, \"delta_k3\": -0.2473, \"clean_full\": 0.9904, \"perturbed_full\": 0.7405, \"delta_full\": -0.2499}, \"scrambled_3seed\": {\"clean_k1\": 0.7206, \"perturbed_k1\": 0.6164, \"delta_k1\": -0.1042, \"clean_k3\": 0.8931, \"perturbed_k3\": 0.7779, \"delta_k3\": -0.1152, \"clean_full\": 0.9511, \"perturbed_full\": 0.7787, \"delta_full\": -0.1724}, \"jb_mlm_3seed\": {\"clean_k1\": 0.7363, \"perturbed_k1\": 0.6572, \"delta_k1\": -0.079, \"clean_k3\": 0.9446, \"perturbed_k3\": 0.5483, \"delta_k3\": -0.3962, \"clean_full\": 0.8934, \"perturbed_full\": 0.5408, \"delta_full\": -0.3526}, \"wiki_mlm_3seed\": {\"clean_k1\": 0.6559, \"perturbed_k1\": 0.6007, \"delta_k1\": -0.0552, \"clean_k3\": 0.6931, \"perturbed_k3\": 0.5216, \"delta_k3\": -0.1716, \"clean_full\": 0.686, \"perturbed_full\": 0.5454, \"delta_full\": -0.1406}, \"topic_3seed\": {\"clean_k1\": 0.5135, \"perturbed_k1\": 0.5258, \"delta_k1\": 0.0123, \"clean_k3\": 0.5654, \"perturbed_k3\": 0.5413, \"delta_k3\": -0.0241, \"clean_full\": 0.6254, \"perturbed_full\": 0.5767, \"delta_full\": -0.0488}, \"vanilla_3seed\": {\"clean_k1\": 0.3374, \"perturbed_k1\": 0.2694, \"delta_k1\": -0.0681, \"clean_k3\": 0.2844, \"perturbed_k3\": 0.2574, \"delta_k3\": -0.027, \"clean_full\": 0.2575, \"perturbed_full\": 0.2482, \"delta_full\": -0.0093}, \"mcnemar_perturbed_k1\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 2e-05, \"b\": 34, \"c\": 6}, \"seed123\": {\"p\": 1.9e-05, \"b\": 59, \"c\": 20}, \"seed456\": {\"p\": 0, \"b\": 72, \"c\": 19}}}, \"mcnemar_perturbed_full\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 0, \"b\": 44, \"c\": 0}, \"seed123\": {\"p\": 0, \"b\": 75, \"c\": 4}, \"seed456\": {\"p\": 0, \"b\": 78, \"c\": 24}}}, \"mcnemar_clean_k1\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 0, \"b\": 52, \"c\": 4}, \"seed123\": {\"p\": 0, \"b\": 42, \"c\": 3}, \"seed456\": {\"p\": 0, \"b\": 53, \"c\": 0}}}, \"mcnemar_clean_full\": {\"9class_vs_vanilla\": {\"seed42\": {\"p\": 0, \"b\": 78, \"c\": 0}, \"seed123\": {\"p\": 0, \"b\": 72, \"c\": 0}, \"seed456\": {\"p\": 0, \"b\": 78, \"c\": 0}}}, \"note\": \"CORRECTED 2026-05-18: vanilla seed123/456 GRU checkpoints and binary seed42 DeBERTa+GRU checkpoints were wrong (used different models than exp2). Fixed to match exp2 checkpoints. Clean baselines now consistent with exp2. All variants still degrade under perturbation except topic at K=1. 9class significantly outperforms vanilla on both clean and perturbed (McNemar all p<0.001).\"}, \"completed_at\": \"2026-05-18T14:34:19.399Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5426}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 193_

Registry 更新完成。以下是完整排查报告。

---

## 排查报告

### 1. 根因

exp6 脚本 (`src/exp6_actorattack_perturbation.py`) 使用了**错误的 checkpoint**，涉及 3 个 variant-seed 组合：

| variant | seed | exp2 正确路径 | exp6 错误路径 | MD5 不同 |
|---|---|---|---|---|
| vanilla | 123 | `plan_002_seed123/gru/baseline/best.pt` | `vanilla_seed123_gru/best.pt` | ✓ |
| vanilla | 456 | `plan_002_seed456/gru/baseline/best.pt` | `vanilla_seed456_gru/best.pt` | ✓ |
| binary | 42 | `mf1_binary_seed42/` (DeBERTa+GRU) | `plan_013_none_collapse/` (BACKUP) | ✓ |

评估逻辑、数据加载、F1 计算方式完全一致，唯一差异就是 checkpoint 路径。

### 2. 修正范围

**已修正** exp6 脚本和结果文件。修正前后 clean_k1 对比：

| variant | 修正前 | 修正后 | exp2 值 | 一致 |
|---|---|---|---|---|
| vanilla mean | 0.439 | **0.337** | 0.337 | ✓ |
| binary mean | 0.765 | **0.737** | 0.737 | ✓ |
| 其他 5 个变体 | — | 无变化 | — | ✓ |

McNemar 测试也已用正确 checkpoint 重算。

### 3. 定性影响

| 问题 | 结论 |
|---|---|
| "所有变体均退化" | **仍成立**（topic k1 除外，delta +0.012），但 vanilla 和 binary 的退化幅度显著变小 |
| vanilla delta_k1 | -0.146 → **-0.068**（退化减半，因为 baseline 本就很低，floor effect） |
| binary delta_k1 | -0.126 → **-0.068**（seed42 delta 从 -0.176 变为 -0.001） |
| 9class vs vanilla McNemar | **不变**，仍全部 p<0.001，方向 A>B，修正后差距更大 |
| 论文叙事影响 | 需要修正 perturbation table 中的 vanilla 和 binary 行；结论不变但措辞需调整退化幅度 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f1928031-eb37-4f7e-8032-2a8b1f2c7474",
  "uuid": "540b1394-6d83-4f3b-869a-a98b36454e7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161Xo8vAMMh2y1dUeLQnWyq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3395,
      "cache_read_input_tokens": 121000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3395
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

_source line 194_

Registry 更新完成。以下是完整排查报告。

---

## 排查报告

### 1. 根因

exp6 脚本 (`src/exp6_actorattack_perturbation.py`) 使用了**错误的 checkpoint**，涉及 3 个 variant-seed 组合：

| variant | seed | exp2 正确路径 | exp6 错误路径 | MD5 不同 |
|---|---|---|---|---|
| vanilla | 123 | `plan_002_seed123/gru/baseline/best.pt` | `vanilla_seed123_gru/best.pt` | ✓ |
| vanilla | 456 | `plan_002_seed456/gru/baseline/best.pt` | `vanilla_seed456_gru/best.pt` | ✓ |
| binary | 42 | `mf1_binary_seed42/` (DeBERTa+GRU) | `plan_013_none_collapse/` (BACKUP) | ✓ |

评估逻辑、数据加载、F1 计算方式完全一致，唯一差异就是 checkpoint 路径。

### 2. 修正范围

**已修正** exp6 脚本和结果文件。修正前后 clean_k1 对比：

| variant | 修正前 | 修正后 | exp2 值 | 一致 |
|---|---|---|---|---|
| vanilla mean | 0.439 | **0.337** | 0.337 | ✓ |
| binary mean | 0.765 | **0.737** | 0.737 | ✓ |
| 其他 5 个变体 | — | 无变化 | — | ✓ |

McNemar 测试也已用正确 checkpoint 重算。

### 3. 定性影响

| 问题 | 结论 |
|---|---|
| "所有变体均退化" | **仍成立**（topic k1 除外，delta +0.012），但 vanilla 和 binary 的退化幅度显著变小 |
| vanilla delta_k1 | -0.146 → **-0.068**（退化减半，因为 baseline 本就很低，floor effect） |
| binary delta_k1 | -0.126 → **-0.068**（seed42 delta 从 -0.176 变为 -0.001） |
| 9class vs vanilla McNemar | **不变**，仍全部 p<0.001，方向 A>B，修正后差距更大 |
| 论文叙事影响 | 需要修正 perturbation table 中的 vanilla 和 binary 行；结论不变但措辞需调整退化幅度 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 904727,
  "duration_api_ms": 623258,
  "num_turns": 69,
  "stop_reason": "end_turn",
  "session_id": "f1928031-eb37-4f7e-8032-2a8b1f2c7474",
  "total_cost_usd": 3.381874,
  "usage": {
    "input_tokens": 48,
    "cache_creation_input_tokens": 112554,
    "cache_read_input_tokens": 3737603,
    "output_tokens": 32270,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112554,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 740,
        "cache_read_input_tokens": 121000,
        "cache_creation_input_tokens": 3395,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3395
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2530,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00262,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 48,
      "outputTokens": 32270,
      "cacheReadInputTokens": 3737603,
      "cacheCreationInputTokens": 112554,
      "webSearchRequests": 0,
      "costUSD": 3.3792540000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3b60ed7c-382b-4c5c-ad1a-f9388cc1ff83"
}
```

</details>

---
