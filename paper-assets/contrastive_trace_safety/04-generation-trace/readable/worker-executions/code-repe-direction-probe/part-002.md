# code repe direction probe — Part 2 of 2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-repe-direction-probe.md) · [Structured JSON](../../../sessions/9f/9f5171f17528315d5304.json)

## Round 2

### Assistant

_source line 223_

<details><summary>Logged reasoning block</summary>

```text
Now I have the LR results for all models. Let me compile the data I need:

**R1-8B LR results (from exp_007_window_ablation):**
- W=1: bal_acc=0.7783, coverage=0.7209, precp_fpr=0.0965, lead=13.84, precision=0.6926
- W=3: bal_acc=0.7902, coverage=0.6977, precp_fpr=0.085, lead=12.07, precision=0.7228
- W=5: bal_acc=0.781, coverage=0.6512, precp_fpr=0.0809, lead=8.25, precision=0.7258


- W=10: bal_acc=0.7925, coverage=0.5581, precp_fpr=0.0761, lead=10.04, precision=0.7431
- W=15: bal_acc=0.8017, coverage=0.5116, precp_fpr=0.0639, lead=7.23, precision=0.7767

Now looking at the R1-32B results, which show a different pattern with lower balanced accuracy but higher coverage at W=1, and I'm continuing to gather the remaining window sizes for this model. Generating performance metrics table... Looking at the performance metrics across different window sizes, W=3 gives the best balanced accuracy. Now I'm laying out the probe script structure: I'll load the model checkpoints, split the data consistently, compute the direction vector as the difference between mean hidden states for unsafe versus safe steps at the optimal layer, then project each step onto that direction and apply temporal windowing before tuning the decision threshold on validation data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "729d68c0-effa-4bf8-8d26-b758f4a321f3",
  "uuid": "f1795ec2-be09-4c40-92ca-bf70fc352409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJh9b7xg1J18oDXTg2e4RE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3094,
      "cache_read_input_tokens": 81294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3094
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

_source line 224_

I have all the information needed. Now I'll write the RepE direction probe script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "729d68c0-effa-4bf8-8d26-b758f4a321f3",
  "uuid": "13556f04-c578-4efc-b8e3-c166da26274c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QJh9b7xg1J18oDXTg2e4RE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3094,
      "cache_read_input_tokens": 81294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3094
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
