# analysis exp 028 postprocess — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-exp-028-postprocess.md) · [Structured JSON](../../../sessions/1d/1dac022fe27561437f98.json)

## Before a recorded user message

### Tool call

_source line 435_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011tawQFbG9oqqNWgBDGUbQp`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -A100 \"1\\\\. Degeneracy\" /root/autodl-tmp/struct_self_consist_ie/logs/exp_028_postprocess.log 2>/dev/null | strings | head -80",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "e27c46b0-b02b-46d2-bfbe-b8a31c1916ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnxFuRSskaoU9PhSwxay25",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 123412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 330
      },
      "output_tokens": 64,
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

_source line 436 · 2026-05-17T20:24:40.410Z_

<details><summary>↩ Tool result · `toolu_011tawQFbG9oqqNWgBDGUbQp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "83947c84-1d1e-48ab-b8dc-f73c9dc3e76a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 437_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01KQcbRegAkLyKNKBC7GMxob`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep \"Degeneracy\\|Greedy\\|Oracle\\|LP sel\\|within\\|rho\\|Verdict\\|Conclusion\\|delta\" /root/autodl-tmp/struct_self_consist_ie/logs/exp_028_postprocess.log 2>/dev/null | strings | head -30",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "c7b7e879-db79-436f-bc6d-838106fddfb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H52WBk9KsXzknQWQS4xS7b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 123742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 224
      },
      "output_tokens": 67,
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

_source line 438 · 2026-05-17T20:24:57.521Z_

<details><summary>↩ Tool result · `toolu_01KQcbRegAkLyKNKBC7GMxob`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "1052009b-e338-4f2b-8699-5aa2dc0f0897",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 439_

<details><summary>Logged reasoning block</summary>

```text
The log might have binary content or the analysis output is at the very end. Let me try a different approach - the JSON results file already has all the key metrics. Let me now compile the report and register it as an artifact.

Summary of findings:

**Training:**
- Completed: 5 epochs, 41180 steps
- Final train loss: 0.0189
- Final eval loss: 0.0311 (best model at checkpoint-32000, epoch ~3.9)
- Eval loss curve: decreased until epoch 3 (0.0321), then increased to 0.04+ (overfitting)


- Best model selection: load_best_model_at_end chose epoch ~3.9 checkpoint

Now I'm looking at the post-processing results comparing the 3-epoch and 5-epoch models. The 5-epoch model shows significantly higher degeneracy at 31.33% versus 11.08%, a concerning 20-point increase, while greedy F1 improved slightly to 0.7773. The LP selection F1 metric appears incomplete in the data.

Looking at the full metrics table, the 5-epoch model's degeneracy far exceeds the 20% threshold, which is a major red flag. Despite some improvements in F1 scores and oracle performance, the dramatic rise in degeneracy suggests the longer training is causing the model to collapse into degenerate solutions rather than learning meaningful representations.

The key insight here is that Few-NERD's apparent low degeneracy at 3 epochs wasn't actually a strength of the dataset—it was just under-convergence masking the problem. Once the model trains longer, the degeneracy explodes, revealing that the dataset has structural vulnerabilities. This fundamentally changes how I need to frame the paper's narrative around Few-NERD's properties. The LP selection mechanism also becomes less effective as degeneracy increases, which makes sense since there's less room for improvement when more instances are identical. The overfitting pattern in the loss curves confirms the model is memorizing rather than generalizing, and this needs to reshape my conclusions about what's actually happening during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "05960e87-98f1-4373-8a09-6a52aed333fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZxpPqSUA2D3LThnNMEKzo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 123966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 440_

所有数据收集完毕。现在整理报告并注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "9202cefb-ba74-470c-a355-3ab2376aefc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZxpPqSUA2D3LThnNMEKzo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 123966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 441_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01H2p5NYm63AizCVDvZnjpW7`</summary>

```json
{
  "name": "exp_028_analysis_report",
  "type": "report",
  "description": "exp_028 Few-NERD 5-epoch convergence test: full post-processing results with comparison to exp_021 3-epoch baseline",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_028",
  "content": "# exp_028 Post-Processing Report: Few-NERD 5-Epoch Convergence Test\n\n**Date**: 2026-05-18\n**Hypothesis**: Few-NERD's low degeneracy (~11%) at 3 epochs is a structural property of the dataset, not under-convergence.\n**Verdict**: ❌ NEGATIVE — Hypothesis rejected.\n\n---\n\n## 1. Training Summary\n\n| Metric | Value |\n|--------|-------|\n| Epochs completed | 5.0 |\n| Total steps | 41,180 |\n| Final train loss | 0.0189 |\n| Final eval loss (best ckpt) | 0.0311 |\n| Best checkpoint | step 32,000 (epoch ~3.9) |\n| Training runtime | 7h 27m |\n| Model | Qwen3-8B + LoRA |\n| GPUs | 4× RTX 5090 |\n\n### Loss Curve (train loss at epoch boundaries)\n- Epoch 1: 0.0506\n- Epoch 2: 0.0374\n- Epoch 3: 0.0239\n- Epoch 4: 0.0113\n- Epoch 5: 0.0044\n\n### Eval Loss Curve\n- Best eval: 0.0311 at step 32,000 (epoch ~3.9)\n- Epoch 5 eval: 0.0407 (overfitting after epoch ~3)\n- `load_best_model_at_end=true` selected checkpoint-32000\n\n**Key observation**: Train loss continued decreasing through epoch 5, but eval loss increased after epoch 3, confirming the model was overfitting on later epochs. The evaluated model is the best checkpoint (epoch ~3.9).\n\n---\n\n## 2. Core Metrics: 5-Epoch vs 3-Epoch Comparison\n\n| Metric | exp_021 (3-epoch) | exp_028 (5-epoch) | Delta |\n|--------|:-----------------:|:-----------------:|:-----:|\n| **Degeneracy (CF1 gold-filtered)** | **11.08%** | **31.33%** | **+20.25pp** |\n| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |\n| Oracle F1 | 0.8692 | 0.8723 | +0.31pp |\n| Headroom (Oracle - Greedy) | 12.14pp | 9.50pp | -2.64pp |\n| LP selection F1 | 0.7614 | 0.7835 | +2.21pp |\n| LP selection Δ (LP - Greedy) | +1.37pp | +0.62pp | -0.75pp |\n| Within-instance ρ(LP, F1) | 0.6226 | 0.4066 (mean) | -0.2160 |\n\n---\n\n## 3. Detailed Signal Metrics (exp_028)\n\n### QE Signal Performance (global)\n| Signal | Spearman ρ | AUROC | Selection F1 | Selection Δ |\n|--------|:----------:|:-----:|:------------:|:-----------:|\n| LP | 0.4495 | 0.5234 | 0.7835 | +0.62pp |\n| SJ | 0.3777 | 0.4988 | 0.7697 | -0.77pp |\n| FK | 0.3892 | 0.4985 | 0.7693 | -0.80pp |\n| EM | 0.3893 | 0.4951 | 0.7663 | -1.10pp |\n| VC | 0.3585 | 0.5006 | 0.7576 | -1.97pp |\n\n### Within-Instance ρ(LP, F1)\n- Mean: 0.4066\n- Median: 0.6151\n- Std: 0.5506\n- Valid instances: 2988 / 4351 (68.67%)\n\n### LP Range\n- Mean: 0.0514\n- Median: 0.0318\n- Std: 0.0673\n\n### Degeneracy Breakdown\n- Gold-filtered instances: 4,351 / 5,000\n- Constant F1 count: 1,363\n- Rate: 31.33%\n\n---\n\n## 4. Interpretation\n\n### Why degeneracy tripled (11% → 31%)\nThe 5-epoch model (best at epoch ~3.9) learned the Few-NERD patterns better (greedy F1 +2.95pp), making its N=8 samples more concentrated around correct answers. This concentration increases the fraction of instances where all 8 samples produce identical F1 scores (constant F1 = degenerate).\n\n### Implications for paper narrative\n1. **Cannot claim** Few-NERD has \"structural\" low degeneracy — it was under-convergence at 3 epochs.\n2. **LP selection effectiveness drops** as degeneracy increases: +1.37pp → +0.62pp. This is expected — when more samples are identical, selection has less room to improve.\n3. **Greedy F1 improved significantly** (+2.95pp), confirming the model genuinely learned more with additional training.\n4. **Within-instance ρ decreased** (0.6226 → 0.4066 mean), likely because degenerate instances have undefined/noise correlations.\n\n### Threshold assessment\n- ≤15%: Confirms intrinsic property → **NOT MET**\n- 15-20%: Borderline → **NOT MET**  \n- **>20%: Needs narrative revision → MET (31.3%)**\n\n---\n\n## 5. Conclusion\n\n**Hypothesis REJECTED.** Few-NERD's low degeneracy at 3 epochs was an artifact of under-convergence. With better training (5 epochs, best checkpoint at ~epoch 3.9), degeneracy rises to 31.3%, consistent with the pattern seen in other well-trained models. The paper narrative that presents Few-NERD as a structurally low-degeneracy dataset needs revision.\n\n**Recommended actions:**\n- Reframe Few-NERD results: acknowledge convergence-dependence of degeneracy\n- Consider using 5-epoch model as the canonical Few-NERD baseline\n- Update any claims about \"dataset-intrinsic\" degeneracy variation\n",
  "content_filename": "exp_028_analysis_report.md",
  "tags": [
    "exp_028",
    "fewnerd",
    "degeneracy",
    "convergence",
    "negative-result"
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
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "5dfa51b3-b114-429b-9746-da9ec11c4dbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZxpPqSUA2D3LThnNMEKzo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 123966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 442 · 2026-05-17T20:25:45.582Z_

<details><summary>↩ Tool result · `toolu_01H2p5NYm63AizCVDvZnjpW7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_032642\", \"name\": \"exp_028_analysis_report\", \"type\": \"report\", \"description\": \"exp_028 Few-NERD 5-epoch convergence test: full post-processing results with comparison to exp_021 3-epoch baseline\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_028/report/exp_028_analysis_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_028\", \"skill\": \"\", \"created_at\": \"2026-05-17T20:25:45.245244+00:00\", \"tags\": [\"exp_028\", \"fewnerd\", \"degeneracy\", \"convergence\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "2bd0c886-5286-4737-9be8-6921f3cf3037",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260517_032642\\\", \\\"name\\\": \\\"exp_028_analysis_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"exp_028 Few-NERD 5-epoch convergence test: full post-processing results with comparison to exp_021 3-epoch baseline\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/exp_028/report/exp_028_analysis_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": \\\"exp_028\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-17T20:25:45.245244+00:00\\\", \\\"tags\\\": [\\\"exp_028\\\", \\\"fewnerd\\\", \\\"degeneracy\\\", \\\"convergence\\\", \\\"negative-result\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_032642\", \"name\": \"exp_028_analysis_report\", \"type\": \"report\", \"description\": \"exp_028 Few-NERD 5-epoch convergence test: full post-processing results with comparison to exp_021 3-epoch baseline\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_028/report/exp_028_analysis_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_028\", \"skill\": \"\", \"created_at\": \"2026-05-17T20:25:45.245244+00:00\", \"tags\": [\"exp_028\", \"fewnerd\", \"degeneracy\", \"convergence\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 443_

报告已注册。下面是最终结果汇总：

---

## exp_028 结果汇总

### 训练状态: ✅ 正常完成
- 5 epochs, 41180 steps, train_loss=0.0189, eval_loss=0.0311
- Best checkpoint: step 32000 (epoch ~3.9), load_best_model_at_end 选择
- Epoch 3 后 eval loss 上升 (0.032→0.041)，存在 overfitting

### 核心指标对比

| Metric | 3-epoch (exp_021) | 5-epoch (exp_028) | Delta |
|--------|:-:|:-:|:-:|
| **Degeneracy (CF1)** | **11.1%** | **31.3%** | **+20.2pp** |
| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |
| LP sel F1 | 0.7614 | 0.7835 | +2.21pp |
| LP sel Δ | +1.37pp | +0.62pp | -0.75pp |
| Oracle F1 | 0.8692 | 0.8723 | +0.31pp |
| Within-instance ρ | 0.6226 | 0.4066 | -0.22 |

### Verdict: ❌ NEGATIVE

Degeneracy 31.3% 远超 20% 阈值��**Hypothesis rejected**: Few-NERD 3-epoch 低 degeneracy 是 under-convergence 的产物，不是数据集的结构属性。模型训练更充分后，degeneracy 上升到与其他数据集类似的水平。

**Paper narrative 需要修改**: 不能再将 Few-NERD 作为 "intrinsically low-degeneracy" 的案例。

### W&B
训练未启用 W&B。Loss 曲线从 trainer_state.json 提取（见报告）。

### 产出
- 分析结果 JSON: `/root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch/analysis_results.json`
- Artifact: `artifacts/exp_028/report/exp_028_analysis_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "uuid": "8bbaeff8-4f25-47e9-a15d-a6944b7e78d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjP5tpmubaHYmM9xMrRFys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2966,
      "cache_read_input_tokens": 124213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2966
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

_source line 444_

报告已注册。下面是最终结果汇总：

---

## exp_028 结果汇总

### 训练状态: ✅ 正常完成
- 5 epochs, 41180 steps, train_loss=0.0189, eval_loss=0.0311
- Best checkpoint: step 32000 (epoch ~3.9), load_best_model_at_end 选择
- Epoch 3 后 eval loss 上升 (0.032→0.041)，存在 overfitting

### 核心指标对比

| Metric | 3-epoch (exp_021) | 5-epoch (exp_028) | Delta |
|--------|:-:|:-:|:-:|
| **Degeneracy (CF1)** | **11.1%** | **31.3%** | **+20.2pp** |
| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |
| LP sel F1 | 0.7614 | 0.7835 | +2.21pp |
| LP sel Δ | +1.37pp | +0.62pp | -0.75pp |
| Oracle F1 | 0.8692 | 0.8723 | +0.31pp |
| Within-instance ρ | 0.6226 | 0.4066 | -0.22 |

### Verdict: ❌ NEGATIVE

Degeneracy 31.3% 远超 20% 阈值��**Hypothesis rejected**: Few-NERD 3-epoch 低 degeneracy 是 under-convergence 的产物，不是数据集的结构属性。模型训练更充分后，degeneracy 上升到与其他数据集类似的水平。

**Paper narrative 需要修改**: 不能再将 Few-NERD 作为 "intrinsically low-degeneracy" 的案例。

### W&B
训练未启用 W&B。Loss 曲线从 trainer_state.json 提取（见报告）。

### 产出
- 分析结果 JSON: `/root/autodl-tmp/struct_self_consist_ie/output/exp_028_fewnerd_5epoch/analysis_results.json`
- Artifact: `artifacts/exp_028/report/exp_028_analysis_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1072055,
  "duration_api_ms": 955754,
  "num_turns": 188,
  "stop_reason": "end_turn",
  "session_id": "60d36a05-2223-47ac-9f8c-bd9c55fe36bf",
  "total_cost_usd": 9.559660000000004,
  "usage": {
    "input_tokens": 181,
    "cache_creation_input_tokens": 115338,
    "cache_read_input_tokens": 15792841,
    "output_tokens": 37578,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 115338,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 614,
        "cache_read_input_tokens": 124213,
        "cache_creation_input_tokens": 2966,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2966
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1912,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002022,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 181,
      "outputTokens": 37578,
      "cacheReadInputTokens": 15792841,
      "cacheCreationInputTokens": 115338,
      "webSearchRequests": 0,
      "costUSD": 9.557638000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5945a516-6dd3-4998-b513-e3b807cdeaf5"
}
```

</details>

---
