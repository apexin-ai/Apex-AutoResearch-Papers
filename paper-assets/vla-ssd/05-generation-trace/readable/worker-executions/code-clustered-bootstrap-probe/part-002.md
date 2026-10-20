# code clustered bootstrap probe — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-clustered-bootstrap-probe.md) · [Structured JSON](../../../sessions/a3/a31b109b7db3db38da79.json)

## Before a recorded user message

### Tool call

_source line 239_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018DgJ4yrAUJYSEyyqBze5Fd`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep \"Saved\" /tmp/bootstrap_dryrun.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "7ab8e64b-16a0-4aab-b2e1-b91f745147ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Yp3Nt3EtMSE3c6fopzWyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 159480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 240 · 2026-05-22T14:37:58.956Z_

<details><summary>↩ Tool result · `toolu_018DgJ4yrAUJYSEyyqBze5Fd`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "a76a9605-f42d-4e27-a950-4ac28124d900",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 241_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BHiHVSkt3eCk6YaUyx6f9M`</summary>

```json
{
  "server": "westd-19183",
  "command": "grep \"Traceback\" /tmp/bootstrap_dryrun.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "ac05bf6c-4f88-4f82-bdfc-80759c300ea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Yp3Nt3EtMSE3c6fopzWyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 159480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 242 · 2026-05-22T14:37:59.556Z_

<details><summary>↩ Tool result · `toolu_01BHiHVSkt3eCk6YaUyx6f9M`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "a91c01d5-92fc-478b-95fb-bcc7a46e9e98",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 243_

<details><summary>Logged reasoning block</summary>

```text
No "Saved" yet, and no "Traceback". The bootstrap is still running. Let me wait a bit more and check again. The bootstrap should be fast on 20 samples (4 demos × 5 timesteps × 2 tasks). The issue might be that with only 4 demos and a 3/1 split, the Ridge fits are very fast but there are 100 iterations × 32 layers. Each Ridge fit on 15 samples × 4096 features should be instant. Let me wait a bit.

Actually, with only 4 demos, the bootstrap will try to resample 4 demos with replacement, then split 3/1. 

With just 1 test demo, the R² computation could be noisy, but it should still complete. Let me give it a few more seconds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "5e56a948-4608-4a92-b847-2b47d1ae685f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAJCSmNSoQy1c2VpVFNHvH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 159726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 399
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

_source line 244_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EYXXPyXm3cQmNBvbKt6swq`</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /tmp/bootstrap_dryrun.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "2e6e673e-3423-4327-86a2-c28f76884139",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAJCSmNSoQy1c2VpVFNHvH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 159726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 399
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

_source line 245 · 2026-05-22T14:38:08.598Z_

<details><summary>↩ Tool result · `toolu_01EYXXPyXm3cQmNBvbKt6swq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"35 /tmp/bootstrap_dryrun.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "257a5042-d2b2-4cce-a4c5-4cc6c668a273",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"35 /tmp/bootstrap_dryrun.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"35 /tmp/bootstrap_dryrun.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 246_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GG2DraxQ3eLf6wNRmNDD1n`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -5 /tmp/bootstrap_dryrun.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "22f8f055-63a6-4e17-91e7-04ef97072887",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LucGR2B1TjAWJFqiZ67VWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 387,
      "cache_read_input_tokens": 160125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 387
      },
      "output_tokens": 71,
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

_source line 247 · 2026-05-22T14:38:12.522Z_

<details><summary>↩ Tool result · `toolu_01GG2DraxQ3eLf6wNRmNDD1n`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[22:37:27]   Extraction done: 20 samples, 4 demos\\n[22:37:27] Extraction: 2.3s\\n[22:37:27]   4 demos, split 3/1\\n[22:37:27]   Canonical split -- fitting RidgeCV per layer...\\n[22:37:27]   Bootstrap (100 iterations)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "1e9a9e5c-678c-4e85-970d-74dd25d806e0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[22:37:27]   Extraction done: 20 samples, 4 demos\\\\n[22:37:27] Extraction: 2.3s\\\\n[22:37:27]   4 demos, split 3/1\\\\n[22:37:27]   Canonical split -- fitting RidgeCV per layer...\\\\n[22:37:27]   Bootstrap (100 iterations)...\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[22:37:27]   Extraction done: 20 samples, 4 demos\\n[22:37:27] Extraction: 2.3s\\n[22:37:27]   4 demos, split 3/1\\n[22:37:27]   Canonical split -- fitting RidgeCV per layer...\\n[22:37:27]   Bootstrap (100 iterations)...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 248_

<details><summary>Logged reasoning block</summary>

```text
The log hasn't changed since the last check. The bootstrap started at 22:37:27 and it's been a few minutes. With 100 iterations × 32 layers on tiny data (20 samples), it should be instant (< 1 second).

Something is wrong. Let me check if the process is stuck or has crashed. The parent bash is still running, but maybe the Python process has died.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "c484d7d4-5276-4617-9cea-336d86da5721",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mDZHtPG8ZT1F9xTQdtN2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 160512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 249_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01P6TTwyuW828Yg2st3dgF8t`</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux --forest -q 669279 && echo \"---\" && pgrep -P 669279 -a",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "e315e8b5-c7a4-409d-bc59-32d59cfaaefd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mDZHtPG8ZT1F9xTQdtN2K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 160512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 250 · 2026-05-22T14:38:18.766Z_

<details><summary>↩ Tool result · `toolu_01P6TTwyuW828Yg2st3dgF8t`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"q/-q/--quick-pid cannot be used together with forest type listings.\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "4a438721-33ae-4ce1-aeae-d24d5e95aecd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"q/-q/--quick-pid cannot be used together with forest type listings.\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"q/-q/--quick-pid cannot be used together with forest type listings.\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 251_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Rdt1fZD9bNYPkCXUETn9zk`</summary>

```json
{
  "server": "westd-19183",
  "command": "pgrep -a -P 669279 && echo \"---\" && pgrep -a \"clustered_bootstrap\"",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "48dec2e5-98e8-407e-ac4c-1eefd6fbd547",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3GCwS91puEsPPu4rEngYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 160781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
      },
      "output_tokens": 65,
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

_source line 252 · 2026-05-22T14:38:36.098Z_

<details><summary>↩ Tool result · `toolu_01Rdt1fZD9bNYPkCXUETn9zk`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"669285 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100\\n---\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.48}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "0c31d1a8-85d8-4fe3-ad45-ad393bbe0c46",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"669285 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100\\\\n---\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.48}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"669285 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100\\n---\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.48}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 253_

<details><summary>Logged reasoning block</summary>

```text
The Python process (PID 669285) is still running. But the log hasn't changed - the bootstrap started but no progress. Let me check if there's a hang. Maybe there's an issue with the RidgeCV or the bootstrap loop.

With only 4 demos split 3/1:
- Train: 3 demos × 5 timesteps = 15 samples
- Test: 1 demo × 5 timesteps = 5 samples

RidgeCV with 15 samples and 4096 features: N < D. The RidgeCV might be slow on underdetermined systems... but it should still work.


Actually, RidgeCV uses leave-one-out cross-validation which computes the SVD of the 15×4096 matrix - that should be fast. But maybe the bottleneck is the matrix solve operations happening repeatedly in the bootstrap loop itself.

With only 15 training samples and D=4096, the XtX matrix is 4096×4096 with rank at most 15. Even with regularization making it well-conditioned, each solve takes O(D³/3) operations - roughly 23 billion for D=4096, which translates to about 2.3 seconds per solve on a single core. Running 100 bootstraps across 32 layers means 3200 solves total, pushing the runtime to around 2 hours. That's the real problem here.

Even with full-size data where N >> D, the cubic scaling becomes prohibitive - 10000 bootstraps would take over a week. I need to switch strategies entirely. The dual form using the kernel trick would solve in N×N space instead, making a 15×15 system trivial. Alternatively, I could pre-compute XtX per demo to avoid redundant calculations, or apply PCA to reduce dimensionality first. For the dry run with smaller N_train, let me explore which approach makes the most sense.

The dual form is the way forward - I'm computing the kernel matrix between training samples, solving a much smaller system, then using kernel products with test data to generate predictions.

For the full dataset with 4000 training samples and 4096 dimensions, both approaches have similar computational costs around 21-23 billion operations, but the real bottleneck is actually the initial kernel computation itself, not the solve step.

The pre-computation strategy looks more promising: I'd compute the full 5000×5000 kernel matrix once upfront (about 100 billion operations), store it in memory (200 MB per layer), then for each bootstrap just index into that matrix for the train/test split and solve.

Writing bootstrap implementation... I'm realizing the Cholesky decomposition is the real bottleneck here—even at 0.43 seconds per solve, running it across 32 layers and 10,000 bootstraps balloons to over 137,000 seconds, which is completely infeasible. I need to find a way to reduce either the number of bootstraps, the dimensionality of the kernel matrix, or the number of layers being processed.

The actual issue with the current code is that it's solving a 4096×4096 system repeatedly across 3,200 iterations, which takes about 2 seconds per solve—totaling roughly 1.8 hours just for the dry run. The solution is to switch to the dual form when the number of training samples is smaller than the feature dimension, which would dramatically reduce the matrix size I'm working with.

Implementing the dual form approach... Writing the prediction step...

The dual form is much faster for the dry run since the 15×15 matrix solve is nearly instant, and even for the full dataset with ~4000 samples, both approaches take similar time around 0.4 seconds. The real optimization comes from precomputing the full kernel matrix once across all samples, then indexing into it for each bootstrap iteration rather than recomputing X_tr @ X_tr.T repeatedly.

Looking at the computational costs for the full run: precomputing the kernel across 32 layers costs around 64 seconds, but then each bootstrap solve is only 0.43 seconds. However, running 10000 bootstraps across all 32 layers still adds up to roughly 137,600 seconds total, which is still quite expensive.

The Cholesky factorization of the training kernel is the real bottleneck here since the training indices change with each bootstrap, so I can't precompute it. Let me reconsider the problem with the actual NORA setup—100 demos split 80/20 gives about 4000 training timesteps, and the 4000×4000 Cholesky takes around 0.4 seconds per bootstrap. With multiprocessing across layers, I might be able to speed this up, though the fundamental solve cost remains the limiting factor.

For now, I should focus on getting the dry run working by switching to the dual form when N < D, and let the user know they can run the full computation overnight or on a cluster if needed. Let me update the script to implement this fix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "326f4315-d682-42b8-9c90-e3b9c8840b8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pMq5jRriGTyBZaLyWRhkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 161109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 250
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

_source line 254_

找到问题：20 samples 对 4096 维做 primal Ridge 太慢。改用 dual form（小 N 时效率更高），并预计算 kernel matrix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "20c30280-e396-4fe9-a4ef-eb7c07141659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pMq5jRriGTyBZaLyWRhkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 161109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 250
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

_source line 255_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JT9Ui4WjiPUHzpkTfBzQ6B`</summary>

```json
{
  "server": "westd-19183",
  "command": "kill 669279 669285 2>/dev/null; echo \"killed\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "8bbf564f-8083-48ed-9565-7e73b2a5caad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pMq5jRriGTyBZaLyWRhkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 161109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 250
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

_source line 256 · 2026-05-22T14:39:39.899Z_

<details><summary>↩ Tool result · `toolu_01JT9Ui4WjiPUHzpkTfBzQ6B`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"killed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "f0640e24-7bce-41af-937a-5b6d1b60f56c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"killed\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"killed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 257_

用预计算 kernel + dual form 优化 bootstrap 循环。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "392f031f-1ede-4503-a5f0-ea43e84cd976",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SSwReTvv3XMAxW7NFuGg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3221,
      "cache_read_input_tokens": 161359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3221
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01YFgnjAsn6BPX99wR9iT8oY`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat > /tmp/fix5.py << 'PYEOF'\nwith open(\"/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\") as f:\n    content = f.read()\n\nold_bootstrap = '''    log(f\"  Bootstrap ({n_bootstrap} iterations)...\")\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\n    rng2 = np.random.RandomState(seed + 1)\n    report_every = max(1, n_bootstrap // 10)\n\n    for b in range(n_bootstrap):\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\n        tr_demos = resampled[:n_train]\n        te_demos = resampled[n_train:]\n\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\n\n        if len(te_idx) == 0:\n            continue\n\n        y_tr = actions[tr_idx]\n        y_te = actions[te_idx]\n        y_te_mean = y_te.mean(axis=0)\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\n        if ss_tot < 1e-10:\n            continue\n\n        for l in range(n_layers):\n            X_tr = features[l][tr_idx]\n            X_te = features[l][te_idx]\n            D = X_tr.shape[1]\n            XtX = X_tr.T @ X_tr\n            XtX[np.diag_indices(D)] += best_alpha[l]\n            Xty = X_tr.T @ y_tr\n            try:\n                beta = np.linalg.solve(XtX, Xty)\n                pred = X_te @ beta\n                ss_res = np.sum((y_te - pred) ** 2)\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\n            except np.linalg.LinAlgError:\n                boot_r2[b, l] = 0.0\n\n        if (b + 1) % report_every == 0:\n            log(f\"    {b+1}/{n_bootstrap}\")'''\n\nnew_bootstrap = '''    # Precompute kernel matrices per layer for efficient bootstrap\n    log(\"  Precomputing kernel matrices...\")\n    N = len(actions)\n    kernels = {}\n    for l in range(n_layers):\n        kernels[l] = features[l] @ features[l].T  # (N, N)\n\n    log(f\"  Bootstrap ({n_bootstrap} iterations)...\")\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\n    rng2 = np.random.RandomState(seed + 1)\n    report_every = max(1, n_bootstrap // 10)\n\n    for b in range(n_bootstrap):\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\n        tr_demos = resampled[:n_train]\n        te_demos = resampled[n_train:]\n\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\n\n        if len(te_idx) == 0:\n            continue\n\n        y_tr = actions[tr_idx]\n        y_te = actions[te_idx]\n        y_te_mean = y_te.mean(axis=0)\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\n        if ss_tot < 1e-10:\n            continue\n\n        n_tr = len(tr_idx)\n        for l in range(n_layers):\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\n            try:\n                w = np.linalg.solve(K_tr, y_tr)\n                pred = K_te_tr @ w\n                ss_res = np.sum((y_te - pred) ** 2)\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\n            except np.linalg.LinAlgError:\n                boot_r2[b, l] = 0.0\n\n        if (b + 1) % report_every == 0:\n            log(f\"    {b+1}/{n_bootstrap}\")'''\n\ncontent = content.replace(old_bootstrap, new_bootstrap)\n\nwith open(\"/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\", \"w\") as f:\n    f.write(content)\nprint(\"PATCHED\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/fix5.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "2923452b-2092-4b6f-843a-8e9644f627d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SSwReTvv3XMAxW7NFuGg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3221,
      "cache_read_input_tokens": 161359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3221
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

_source line 259 · 2026-05-22T14:39:58.878Z_

<details><summary>↩ Tool result · `toolu_01YFgnjAsn6BPX99wR9iT8oY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"PATCHED\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "97df3adc-11fd-4a8c-b28e-e7b716a55c02",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"PATCHED\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"PATCHED\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 260_

重新运行 dry-run。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "57e5029f-ef83-4864-93bd-be749c876e66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjWMquFLxtdkJ11m12dHSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 164580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1502
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015pbYgSpYLcsgDsRC8m2yxG`</summary>

```json
{
  "server": "westd-19183",
  "command": "cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c 'CUDA_VISIBLE_DEVICES=0 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100' > /tmp/bootstrap_dryrun2.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "45419f5d-f0b9-432e-bd3b-22ca22fce057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FjWMquFLxtdkJ11m12dHSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 164580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1502
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

_source line 262 · 2026-05-22T14:40:34.937Z_

<details><summary>↩ Tool result · `toolu_015pbYgSpYLcsgDsRC8m2yxG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=0 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100\\\\' > /tmp/bootstrap_dryrun2.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=669838\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "708f654b-bccc-4fa8-821c-f8b02d4441bc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Command did not complete within 30 seconds!\\\\n\\\\nCommand: 'cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c \\\\\\\\'CUDA_VISIBLE_DEVICES=0 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100\\\\\\\\' > /tmp/bootstrap_dryrun2.log 2>&1 & echo \\\\\\\"PID=$!\\\\\\\"'\\\\n\\\\nStdout:\\\\n\\\\nPID=669838\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 30.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=0 python scripts/clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --gpu 0 --dry_run --n_bootstrap 100\\\\' > /tmp/bootstrap_dryrun2.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=669838\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 263_

<details><summary>Logged reasoning block</summary>

```text
Got PID 669838. Let me wait about 2 minutes for the model to load and the dry run to complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "62208894-f841-4c5f-9663-56780f492be9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m5outoTDauTNoszv2dtRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 166082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 438
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

_source line 264_

等待模型加载和 bootstrap 完成（~2分钟）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "ef6f058d-ef5e-40d8-a59a-8fcaf07a82b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m5outoTDauTNoszv2dtRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 166082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 438
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

_source line 265_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SQnUYLUSH1X3UMnwqTHLdD`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -10 /tmp/bootstrap_dryrun2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "4a9c027c-72fc-47ad-a417-8a21a0fb5006",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m5outoTDauTNoszv2dtRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 166082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 438
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

_source line 266 · 2026-05-22T14:40:41.785Z_

<details><summary>↩ Tool result · `toolu_01SQnUYLUSH1X3UMnwqTHLdD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[transformers] `use_return_dict` is deprecated! Use `return_dict` instead!\\n[22:40:40]   Task 1/2: open_the_top_drawer_and_put_the_bowl_inside\\n[22:40:41]   Extraction done: 20 samples, 4 demos\\n[22:40:41] Extraction: 3.3s\\n[22:40:41]   4 demos, split 3/1\\n[22:40:41]   Canonical split -- fitting RidgeCV per layer...\\n[22:40:41]   Precomputing kernel matrices...\\n[22:40:41]   Bootstrap (100 iterations)...\\n[22:40:41]     10/100\\n[22:40:41]     20/100\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "a638d16a-8f84-45ee-b7e8-b6cb6c9e9a0b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[transformers] `use_return_dict` is deprecated! Use `return_dict` instead!\\\\n[22:40:40]   Task 1/2: open_the_top_drawer_and_put_the_bowl_inside\\\\n[22:40:41]   Extraction done: 20 samples, 4 demos\\\\n[22:40:41] Extraction: 3.3s\\\\n[22:40:41]   4 demos, split 3/1\\\\n[22:40:41]   Canonical split -- fitting RidgeCV per layer...\\\\n[22:40:41]   Precomputing kernel matrices...\\\\n[22:40:41]   Bootstrap (100 iterations)...\\\\n[22:40:41]     10/100\\\\n[22:40:41]     20/100\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.87}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[transformers] `use_return_dict` is deprecated! Use `return_dict` instead!\\n[22:40:40]   Task 1/2: open_the_top_drawer_and_put_the_bowl_inside\\n[22:40:41]   Extraction done: 20 samples, 4 demos\\n[22:40:41] Extraction: 3.3s\\n[22:40:41]   4 demos, split 3/1\\n[22:40:41]   Canonical split -- fitting RidgeCV per layer...\\n[22:40:41]   Precomputing kernel matrices...\\n[22:40:41]   Bootstrap (100 iterations)...\\n[22:40:41]     10/100\\n[22:40:41]     20/100\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.87}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 267_

运行中了，进展很快。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "7e435dc5-880a-407d-8402-42b35c082d5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSV8JVmsapEAh9cG7t1kup",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 166520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 433
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

_source line 268_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0134TmQZ7wo7g1awXZ2TMwhc`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -15 /tmp/bootstrap_dryrun2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "16f6ae3a-8486-48c1-821f-b68c76b12a2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSV8JVmsapEAh9cG7t1kup",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 166520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 433
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

_source line 269 · 2026-05-22T14:40:47.694Z_

<details><summary>↩ Tool result · `toolu_0134TmQZ7wo7g1awXZ2TMwhc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[22:40:41]     10/100\\n[22:40:41]     20/100\\n[22:40:41]     30/100\\n[22:40:41]     40/100\\n[22:40:41]     50/100\\n[22:40:41]     60/100\\n[22:40:41]     70/100\\n[22:40:41]     80/100\\n[22:40:41]     90/100\\n[22:40:41]     100/100\\n[22:40:41] Bootstrap: 0.2s\\n[22:40:41] Saved: /root/autodl-tmp/vla-ssd/results/clustered_bootstrap/openvla_goal/trained.json\\n[22:40:41] Peak R2=-0.7551 @ L28\\n[22:40:41] Exit R2=-0.9913 @ L31\\n[22:40:41] Delta=0.2362  CI95=[0.0, 1.4872]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "7888261b-de76-49f4-a277-45640bc3df98",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[22:40:41]     10/100\\\\n[22:40:41]     20/100\\\\n[22:40:41]     30/100\\\\n[22:40:41]     40/100\\\\n[22:40:41]     50/100\\\\n[22:40:41]     60/100\\\\n[22:40:41]     70/100\\\\n[22:40:41]     80/100\\\\n[22:40:41]     90/100\\\\n[22:40:41]     100/100\\\\n[22:40:41] Bootstrap: 0.2s\\\\n[22:40:41] Saved: /root/autodl-tmp/vla-ssd/results/clustered_bootstrap/openvla_goal/trained.json\\\\n[22:40:41] Peak R2=-0.7551 @ L28\\\\n[22:40:41] Exit R2=-0.9913 @ L31\\\\n[22:40:41] Delta=0.2362  CI95=[0.0, 1.4872]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[22:40:41]     10/100\\n[22:40:41]     20/100\\n[22:40:41]     30/100\\n[22:40:41]     40/100\\n[22:40:41]     50/100\\n[22:40:41]     60/100\\n[22:40:41]     70/100\\n[22:40:41]     80/100\\n[22:40:41]     90/100\\n[22:40:41]     100/100\\n[22:40:41] Bootstrap: 0.2s\\n[22:40:41] Saved: /root/autodl-tmp/vla-ssd/results/clustered_bootstrap/openvla_goal/trained.json\\n[22:40:41] Peak R2=-0.7551 @ L28\\n[22:40:41] Exit R2=-0.9913 @ L31\\n[22:40:41] Delta=0.2362  CI95=[0.0, 1.4872]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---


### System

_source line 270_

```json
{
  "type": "system",
  "subtype": "status",
  "status": "compacting",
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "9cf0d179-86b3-4946-8c2e-31b2a8b5640b"
}
```

---


### System

_source line 271_

```json
{
  "type": "system",
  "subtype": "status",
  "status": null,
  "compact_result": "success",
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "34a01078-70ce-4100-8b29-94d88b3e58c0"
}
```

---


### System

_source line 272_

```json
{
  "type": "system",
  "subtype": "compact_boundary",
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "793b3b25-0be8-4c26-865f-94abf1ad0278",
  "compact_metadata": {
    "trigger": "auto",
    "pre_tokens": 167252,
    "post_tokens": 2549,
    "duration_ms": 87105
  }
}
```

---


## Round 1

## Round 1

43 recorded events


### User

_source line 273 · 2026-05-22T14:42:14.804Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   Write `clustered_bootstrap_probe.py` that fixes temporal leakage (same demo timesteps across train/test) in R² probing by using demo-level clustered bootstrap. Deploy to server westd-19183 and dry-run on openvla/goal/trained condition. The script must support 3 VLA architectures (OpenVLA, TracVLA, NORA), extract last_preaction hidden states, do demo-level RidgeCV, then clustered bootstrap ×10000 to compute R² Δ (peak - exit) with 95% CI. Output JSON with per-layer R², peak/exit R², delta, CI, and bootstrap summary.

2. Key Technical Concepts:
   - Clustered bootstrap: resample unique demos with replacement, 80/20 demo-level split, avoiding temporal leakage
   - Ridge regression probing: RidgeCV to determine best alpha, then fixed-alpha Ridge for bootstrap
   - Dual form (kernel trick) for Ridge: when N < D, solve N×N system instead of D×D — critical for performance
   - Precomputed kernel matrices: `K = X @ X.T` computed once per layer, reused across bootstrap iterations
   - Three VLA architectures with different model classes, processors, prompt formats, and hidden dimensions
   - HDF5 data format with demo-level organization
   - transformers 5.9.0 compatibility: multiple breaking changes from 4.40.1 (removed AutoModelForVision2Seq, moved PaddingStrategy, changed tie_weights signature, deprecated torch_dtype)

3. Files and Code Sections:
   - `/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py` (on server westd-19183, ~420 lines)
     - The main deliverable script. Deployed via multiple `ssh_execute` calls with heredoc + Python patching scripts.
     - Key architecture decisions:
       - OpenVLA loaded via fake package (`_openvla_pkg`) with source-level patching for transformers 5.x compat
       - TracVLA loaded via `AutoModelForCausalLM`
       - NORA loaded via `AutoModelForImageTextToText`
       - Tasks discovered dynamically from HDF5 files in data directory
       - Bootstrap uses precomputed kernel matrices + dual form Ridge for efficiency

   - `/root/autodl-tmp/vla-ssd/scripts/libero_goal_full_pipeline.py` (existing, read-only)
     - OpenVLA probing pipeline. Key patterns copied: model loading with `processing_prismatic.py`, prompt format, `output_hidden_states=True`, `hs[-1]` for last_preaction, HDF5 data access pattern (`data/demo_{i}/obs/agentview_rgb[t]`, `data/demo_{i}/actions[t]`)

   - `/root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py` (existing, read-only)
     - TracVLA probing pipeline. Key patterns: `AutoModelForCausalLM`, Phi-3 chat prompt format, `find_token_regions` with negative image token IDs

   - `/root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py` (existing, read-only)
     - NORA probing pipeline. Key patterns: `AutoModelForImageTextToText`, Qwen2.5-VL chat template, `vision_start_token_id`/`vision_end_token_id` for token regions

   - Checkpoint paths confirmed:
     - OpenVLA trained: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-{goal,spatial,object}/`
     - OpenVLA untrained: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`
     - TracVLA trained: `/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/`
     - TracVLA untrained: `/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/`
     - NORA trained: `/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-{goal,spatial}/`
     - NORA untrained: `/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/`

   - Key function: `_load_openvla_modules(ckpt_path)` — creates fake package, reads source files, applies source-level patches (import fixes + tie_weights fix), compiles and execs in module namespace
   
   - Key function: `clustered_bootstrap_r2()` — precomputes kernel matrices `K[l] = features[l] @ features[l].T`, then for each bootstrap iteration uses dual form: `K_tr = K[np.ix_(tr_idx, tr_idx)]`, solve `K_tr w = y_tr`, predict via `K_te_tr @ w`

   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py` (local copy, initial version before patches — NOT the deployed version)

4. Errors and fixes:
   - **`AutoModelForVision2Seq` ImportError** (transformers 5.9.0 removed it):
     - First tried replacing with `AutoModelForImageTextToText` — failed because OpenVLA's config.json auto_map only registers `AutoModelForVision2Seq`
     - Fixed by directly loading model class via `importlib.util` from checkpoint's `modeling_prismatic.py`
   
   - **Relative import error** (`from .configuration_prismatic import ...`):
     - importlib.util loaded modules lack parent package context
     - Fixed by creating fake package `_openvla_pkg = types.ModuleType(pkg_name)` with `__path__` and `__package__` set, registering submodules in `sys.modules` with both full and short names
   
   - **`PaddingStrategy` ImportError** (moved from `transformers.tokenization_utils` to `transformers.utils` in 5.x):
     - Initial sys.modules patching approach failed because processing_prismatic.py loaded from HF cache (unpatched copy)
     - Fixed with two-pronged approach: (1) source-level string replacement when loading from ckpt_path, (2) `sys.modules["transformers.tokenization_utils"]` attribute patching before `from_pretrained` call for HF cache loading
   
   - **`torch_dtype` deprecated warning**: Changed to `dtype` parameter
   
   - **`tie_weights()` TypeError** (`got unexpected keyword argument 'recompute_mapping'`):
     - transformers 5.9.0 passes `recompute_mapping=False` to `tie_weights()`
     - Fixed via source-level patch: `def tie_weights(self) -> None:` → `def tie_weights(self, **kwargs) -> None:`
   
   - **Bootstrap hanging** (3200 iterations of 4096×4096 matrix solve):
     - With dry_run's 20 samples, primal Ridge solves 4096×4096 system per iteration (~2s each)
     - Fixed by switching to dual form with precomputed kernel matrices: `K_full[l] = features[l] @ features[l].T` (20×20 for dry_run), then solve 15×15 system per bootstrap — instant

5. Problem Solving:
   - All errors resolved. Dry-run completed successfully.
   - Output JSON saved to `/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/openvla_goal/trained.json`
   - Results (dry_run, 20 samples): Peak R2=-0.7551 @ L28, Exit R2=-0.9913 @ L31, Delta=0.2362, CI95=[0.0, 1.4872]
   - Negative R² expected with tiny sample size (4 demos, 3/1 split)

6. All user messages:
   - **Message 1** (the only explicit user message): Detailed multi-step request to write `clustered_bootstrap_probe.py` with specific requirements for architecture adaptation, core flow (6 steps), CLI interface, checkpoint path mapping, data paths, hidden state extraction pattern, output JSON format, and performance considerations. Includes 4 steps: (1) read existing code, (2) write script, (3) deploy, (4) dry-run and verify.

7. Pending Tasks:
   - The dry-run completed successfully. The user asked to "汇报输出结果" (report output results) if dry-run succeeds, which has not yet been reported to the user.
   - The local artifact file at `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py` is the INITIAL version and does NOT match the deployed version (which has all the patches). It should be updated to match.

8. Current Work:
   The dry-run just completed successfully. The last output showed:
   ```
   [22:40:41] Bootstrap: 0.2s
   [22:40:41] Saved: /root/autodl-tmp/vla-ssd/results/clustered_bootstrap/openvla_goal/trained.json
   [22:40:41] Peak R2=-0.7551 @ L28
   [22:40:41] Exit R2=-0.9913 @ L31
   [22:40:41] Delta=0.2362  CI95=[0.0, 1.4872]
   ```
   The script is deployed and working at `/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py` on westd-19183.

9. Optional Next Step:
   Report the dry-run results to the user. The user's instructions said: "如果 dry-run 成功，汇报输出结果。如果失败，修复问题。" The dry-run succeeded, so the next step is to report the results, noting that negative R² values are expected with the tiny dry-run sample size (20 samples, 4 demos) and that the pipeline (model loading → hidden state extraction → demo-level split → clustered bootstrap → JSON output) is verified working. Optionally read the actual output JSON to show the full result. The local artifact file should also be synced to match the deployed version.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/7ae68de3-16ab-4110-8f59-0311deda7143.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "1140296d-3dac-4c87-a2fe-b3f63a9bc88c",
  "isSynthetic": true
}
```

</details>

---


### Assistant

_source line 274_

<details><summary>Logged reasoning block</summary>

```text
The dry-run completed successfully. I need to:
1. Read the output JSON to show full results
2. Report to the user
3. Sync the local artifact file with the deployed version

Let me first read the output JSON from the server, and also read the deployed version to sync locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "cc2977d7-43ec-471f-a0f1-0730c81d185b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M58Xiz3nMroVeD8VXiZHte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
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

_source line 275_

Let me fetch the full output JSON and the deployed script version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "443f2d9a-9cd6-4965-b85b-0a3c14ebddb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M58Xiz3nMroVeD8VXiZHte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
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

_source line 276_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018itgtvKhwC3H4b3Ma3CWXF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "888dab13-a4c1-4506-b9dd-25e00e713755",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M58Xiz3nMroVeD8VXiZHte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
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

_source line 277 · 2026-05-22T14:42:20.809Z_

<details><summary>↩ Tool result · `toolu_018itgtvKhwC3H4b3Ma3CWXF`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "e3a913cb-d172-47b9-90c7-2ee83a92a50f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Tool call

_source line 278_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01N5fTbet6vzdtsGz552bsm7`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/clustered_bootstrap/openvla_goal/trained.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "f22567b3-bf8b-4504-a5a6-9db698fc350a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2Y2SAfVGAETFZMYvA9HXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 24478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 519
      },
      "output_tokens": 59,
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

_source line 279_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GzG8y2ccgxtyJWkPrHfGJz`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "03cf1799-4608-482a-b9cc-b27a91f1e13f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2Y2SAfVGAETFZMYvA9HXk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 24478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 519
      },
      "output_tokens": 59,
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

_source line 280 · 2026-05-22T14:42:27.697Z_

<details><summary>↩ Tool result · `toolu_01N5fTbet6vzdtsGz552bsm7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_layer_r2\\\": {\\n    \\\"L0\\\": -2.3638,\\n    \\\"L1\\\": -2.0341,\\n    \\\"L2\\\": -1.414,\\n    \\\"L3\\\": -1.2663,\\n    \\\"L4\\\": -1.3981,\\n    \\\"L5\\\": -1.0162,\\n    \\\"L6\\\": -0.9528,\\n    \\\"L7\\\": -0.9837,\\n    \\\"L8\\\": -1.1556,\\n    \\\"L9\\\": -1.3026,\\n    \\\"L10\\\": -1.4575,\\n    \\\"L11\\\": -1.7242,\\n    \\\"L12\\\": -1.8956,\\n    \\\"L13\\\": -1.846,\\n    \\\"L14\\\": -1.8771,\\n    \\\"L15\\\": -1.8277,\\n    \\\"L16\\\": -1.2781,\\n    \\\"L17\\\": -1.2289,\\n    \\\"L18\\\": -1.1917,\\n    \\\"L19\\\": -1.252,\\n    \\\"L20\\\": -1.2631,\\n    \\\"L21\\\": -1.1918,\\n    \\\"L22\\\": -1.1497,\\n    \\\"L23\\\": -1.1922,\\n    \\\"L24\\\": -1.1571,\\n    \\\"L25\\\": -1.0105,\\n    \\\"L26\\\": -0.8327,\\n    \\\"L27\\\": -0.8327,\\n    \\\"L28\\\": -0.7551,\\n    \\\"L29\\\": -0.8158,\\n    \\\"L30\\\": -0.8434,\\n    \\\"L31\\\": -0.9913\\n  },\\n  \\\"peak_r2\\\": -0.7551,\\n  \\\"peak_layer\\\": \\\"L28\\\",\\n  \\\"exit_r2\\\": -0.9913,\\n  \\\"exit_layer\\\": \\\"L31\\\",\\n  \\\"delta\\\": 0.2362,\\n  \\\"delta_ci_95\\\": [\\n    0.0,\\n    1.4872\\n  ],\\n  \\\"bootstrap_deltas_summary\\\": {\\n    \\\"mean\\\": 0.1911,\\n    \\\"std\\\": 0.4205,\\n    \\\"median\\\": 0.0\\n  },\\n  \\\"arch\\\": \\\"openvla\\\",\\n  \\\"suite\\\": \\\"goal\\\",\\n  \\\"condition\\\": \\\"trained\\\",\\n  \\\"n_demos\\\": 4,\\n  \\\"n_total_samples\\\": 20,\\n  \\\"n_bootstrap\\\": 100,\\n  \\\"dry_run\\\": true\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "446bab1e-8b52-43c4-b72f-da8a30474192",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"per_layer_r2\\\\\\\": {\\\\n    \\\\\\\"L0\\\\\\\": -2.3638,\\\\n    \\\\\\\"L1\\\\\\\": -2.0341,\\\\n    \\\\\\\"L2\\\\\\\": -1.414,\\\\n    \\\\\\\"L3\\\\\\\": -1.2663,\\\\n    \\\\\\\"L4\\\\\\\": -1.3981,\\\\n    \\\\\\\"L5\\\\\\\": -1.0162,\\\\n    \\\\\\\"L6\\\\\\\": -0.9528,\\\\n    \\\\\\\"L7\\\\\\\": -0.9837,\\\\n    \\\\\\\"L8\\\\\\\": -1.1556,\\\\n    \\\\\\\"L9\\\\\\\": -1.3026,\\\\n    \\\\\\\"L10\\\\\\\": -1.4575,\\\\n    \\\\\\\"L11\\\\\\\": -1.7242,\\\\n    \\\\\\\"L12\\\\\\\": -1.8956,\\\\n    \\\\\\\"L13\\\\\\\": -1.846,\\\\n    \\\\\\\"L14\\\\\\\": -1.8771,\\\\n    \\\\\\\"L15\\\\\\\": -1.8277,\\\\n    \\\\\\\"L16\\\\\\\": -1.2781,\\\\n    \\\\\\\"L17\\\\\\\": -1.2289,\\\\n    \\\\\\\"L18\\\\\\\": -1.1917,\\\\n    \\\\\\\"L19\\\\\\\": -1.252,\\\\n    \\\\\\\"L20\\\\\\\": -1.2631,\\\\n    \\\\\\\"L21\\\\\\\": -1.1918,\\\\n    \\\\\\\"L22\\\\\\\": -1.1497,\\\\n    \\\\\\\"L23\\\\\\\": -1.1922,\\\\n    \\\\\\\"L24\\\\\\\": -1.1571,\\\\n    \\\\\\\"L25\\\\\\\": -1.0105,\\\\n    \\\\\\\"L26\\\\\\\": -0.8327,\\\\n    \\\\\\\"L27\\\\\\\": -0.8327,\\\\n    \\\\\\\"L28\\\\\\\": -0.7551,\\\\n    \\\\\\\"L29\\\\\\\": -0.8158,\\\\n    \\\\\\\"L30\\\\\\\": -0.8434,\\\\n    \\\\\\\"L31\\\\\\\": -0.9913\\\\n  },\\\\n  \\\\\\\"peak_r2\\\\\\\": -0.7551,\\\\n  \\\\\\\"peak_layer\\\\\\\": \\\\\\\"L28\\\\\\\",\\\\n  \\\\\\\"exit_r2\\\\\\\": -0.9913,\\\\n  \\\\\\\"exit_layer\\\\\\\": \\\\\\\"L31\\\\\\\",\\\\n  \\\\\\\"delta\\\\\\\": 0.2362,\\\\n  \\\\\\\"delta_ci_95\\\\\\\": [\\\\n    0.0,\\\\n    1.4872\\\\n  ],\\\\n  \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n    \\\\\\\"mean\\\\\\\": 0.1911,\\\\n    \\\\\\\"std\\\\\\\": 0.4205,\\\\n    \\\\\\\"median\\\\\\\": 0.0\\\\n  },\\\\n  \\\\\\\"arch\\\\\\\": \\\\\\\"openvla\\\\\\\",\\\\n  \\\\\\\"suite\\\\\\\": \\\\\\\"goal\\\\\\\",\\\\n  \\\\\\\"condition\\\\\\\": \\\\\\\"trained\\\\\\\",\\\\n  \\\\\\\"n_demos\\\\\\\": 4,\\\\n  \\\\\\\"n_total_samples\\\\\\\": 20,\\\\n  \\\\\\\"n_bootstrap\\\\\\\": 100,\\\\n  \\\\\\\"dry_run\\\\\\\": true\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_layer_r2\\\": {\\n    \\\"L0\\\": -2.3638,\\n    \\\"L1\\\": -2.0341,\\n    \\\"L2\\\": -1.414,\\n    \\\"L3\\\": -1.2663,\\n    \\\"L4\\\": -1.3981,\\n    \\\"L5\\\": -1.0162,\\n    \\\"L6\\\": -0.9528,\\n    \\\"L7\\\": -0.9837,\\n    \\\"L8\\\": -1.1556,\\n    \\\"L9\\\": -1.3026,\\n    \\\"L10\\\": -1.4575,\\n    \\\"L11\\\": -1.7242,\\n    \\\"L12\\\": -1.8956,\\n    \\\"L13\\\": -1.846,\\n    \\\"L14\\\": -1.8771,\\n    \\\"L15\\\": -1.8277,\\n    \\\"L16\\\": -1.2781,\\n    \\\"L17\\\": -1.2289,\\n    \\\"L18\\\": -1.1917,\\n    \\\"L19\\\": -1.252,\\n    \\\"L20\\\": -1.2631,\\n    \\\"L21\\\": -1.1918,\\n    \\\"L22\\\": -1.1497,\\n    \\\"L23\\\": -1.1922,\\n    \\\"L24\\\": -1.1571,\\n    \\\"L25\\\": -1.0105,\\n    \\\"L26\\\": -0.8327,\\n    \\\"L27\\\": -0.8327,\\n    \\\"L28\\\": -0.7551,\\n    \\\"L29\\\": -0.8158,\\n    \\\"L30\\\": -0.8434,\\n    \\\"L31\\\": -0.9913\\n  },\\n  \\\"peak_r2\\\": -0.7551,\\n  \\\"peak_layer\\\": \\\"L28\\\",\\n  \\\"exit_r2\\\": -0.9913,\\n  \\\"exit_layer\\\": \\\"L31\\\",\\n  \\\"delta\\\": 0.2362,\\n  \\\"delta_ci_95\\\": [\\n    0.0,\\n    1.4872\\n  ],\\n  \\\"bootstrap_deltas_summary\\\": {\\n    \\\"mean\\\": 0.1911,\\n    \\\"std\\\": 0.4205,\\n    \\\"median\\\": 0.0\\n  },\\n  \\\"arch\\\": \\\"openvla\\\",\\n  \\\"suite\\\": \\\"goal\\\",\\n  \\\"condition\\\": \\\"trained\\\",\\n  \\\"n_demos\\\": 4,\\n  \\\"n_total_samples\\\": 20,\\n  \\\"n_bootstrap\\\": 100,\\n  \\\"dry_run\\\": true\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-22T14:42:28.284Z_

<details><summary>↩ Tool result · `toolu_01GzG8y2ccgxtyJWkPrHfGJz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(a\\n\\n... [截断: 输出过长，省略 9082 字符] ...\\n\\nlayers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    data_dir = os.path.join(DATA_ROOT, f\\\"libero_{args.suite}\\\")\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "92905624-6f77-4f32-b34b-7153a389aaa6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(a\\\\n\\\\n... [截断: 输出过长，省略 9082 字符] ...\\\\n\\\\nlayers - 1\\\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\\\n    exit_r2_boot = boot_r2[:, exit_l]\\\\n    deltas = peak_r2_boot - exit_r2_boot\\\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\\\n\\\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\\\n\\\\n    return {\\\\n        \\\\\\\"per_layer_r2\\\\\\\": {f\\\\\\\"L{l}\\\\\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\\\n        \\\\\\\"peak_r2\\\\\\\": round(canon_r2[canon_peak_l], 4),\\\\n        \\\\\\\"peak_layer\\\\\\\": f\\\\\\\"L{canon_peak_l}\\\\\\\",\\\\n        \\\\\\\"exit_r2\\\\\\\": round(canon_r2[exit_l], 4),\\\\n        \\\\\\\"exit_layer\\\\\\\": f\\\\\\\"L{exit_l}\\\\\\\",\\\\n        \\\\\\\"delta\\\\\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\\\n        \\\\\\\"delta_ci_95\\\\\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\\\n        \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(deltas)), 4),\\\\n            \\\\\\\"std\\\\\\\": round(float(np.std(deltas)), 4),\\\\n            \\\\\\\"median\\\\\\\": round(float(np.median(deltas)), 4),\\\\n        },\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--arch\\\\\\\", required=True, choices=[\\\\\\\"openvla\\\\\\\", \\\\\\\"tracvla\\\\\\\", \\\\\\\"nora\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", required=True, choices=[\\\\\\\"goal\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"object\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--condition\\\\\\\", required=True, choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--n_bootstrap\\\\\\\", type=int, default=10000)\\\\n    p.add_argument(\\\\\\\"--n_demos\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--n_timesteps\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\",\\\\n                   default=\\\\\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    args = p.parse_args()\\\\n\\\\n    if args.dry_run:\\\\n        args.n_demos = 2\\\\n        args.n_timesteps = 5\\\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\\\n\\\\n    if args.suite not in CKPT.get(args.arch, {}):\\\\n        log(f\\\\\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n    if args.condition not in CKPT[args.arch][args.suite]:\\\\n        log(f\\\\\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = f\\\\\\\"cuda:{args.gpu}\\\\\\\"\\\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\\\n    data_dir = os.path.join(DATA_ROOT, f\\\\\\\"libero_{args.suite}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\\\\\")\\\\n    log(f\\\\\\\"Checkpoint: {ckpt_path}\\\\\\\")\\\\n    log(f\\\\\\\"Data: {data_dir}\\\\\\\")\\\\n    log(f\\\\\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\\\\\")\\\\n    if args.dry_run:\\\\n        log(\\\\\\\"DRY RUN\\\\\\\")\\\\n\\\\n    tasks, instructions = discover_tasks(data_dir)\\\\n    if args.dry_run:\\\\n        tasks = tasks[:2]\\\\n        instructions = instructions[:2]\\\\n    log(f\\\\\\\"Tasks: {len(tasks)}\\\\\\\")\\\\n\\\\n    model, processor = load_model(args.arch, ckpt_path, device)\\\\n\\\\n    t0 = time.time()\\\\n    features, actions, demo_ids = extract_features(\\\\n        args.arch, model, processor, tasks, instructions, data_dir,\\\\n        device, args.n_demos, args.n_timesteps)\\\\n    log(f\\\\\\\"Extraction: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    del model, processor\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    n_layers = ARCH_INFO[args.arch][\\\\\\\"n_layers\\\\\\\"]\\\\n    result = clustered_bootstrap_r2(\\\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\\\n    log(f\\\\\\\"Bootstrap: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    result[\\\\\\\"arch\\\\\\\"] = args.arch\\\\n    result[\\\\\\\"suite\\\\\\\"] = args.suite\\\\n    result[\\\\\\\"condition\\\\\\\"] = args.condition\\\\n    result[\\\\\\\"n_demos\\\\\\\"] = int(len(np.unique(demo_ids)))\\\\n    result[\\\\\\\"n_total_samples\\\\\\\"] = int(len(actions))\\\\n    result[\\\\\\\"n_bootstrap\\\\\\\"] = args.n_bootstrap\\\\n    result[\\\\\\\"dry_run\\\\\\\"] = args.dry_run\\\\n\\\\n    out_dir = os.path.join(args.output_dir, f\\\\\\\"{args.arch}_{args.suite}\\\\\\\")\\\\n    os.makedirs(out_dir, exist_ok=True)\\\\n    out_path = os.path.join(out_dir, f\\\\\\\"{args.condition}.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    log(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.58}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(a\\n\\n... [截断: 输出过长，省略 9082 字符] ...\\n\\nlayers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    data_dir = os.path.join(DATA_ROOT, f\\\"libero_{args.suite}\\\")\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 282_

<details><summary>Logged reasoning block</summary>

```text
Good, I have both the output JSON and the deployed script. Let me now sync the local artifact file with the deployed version, and report the results.

Let me first read the full deployed script (it was truncated in the output). Let me check how much was truncated.

The output says "截断: 输出过长，省略 9082 字符" - so a large chunk was truncated. Let me get the parts that were cut off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "f4118cab-239e-464c-a831-1f287f3cc44b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8dkcRZNa3fsLufmxEUq8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4959,
      "cache_read_input_tokens": 24997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4959
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

_source line 283_

The output was truncated. Let me get the middle section of the deployed script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "5f459d47-6c1a-48f5-a2c7-523a224b8de8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8dkcRZNa3fsLufmxEUq8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4959,
      "cache_read_input_tokens": 24997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4959
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

_source line 284_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SNYNS5johcmExrx267A7B9`</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "ad6ec199-798a-4b86-a149-9d38c0ebbd8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8dkcRZNa3fsLufmxEUq8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4959,
      "cache_read_input_tokens": 24997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4959
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

_source line 285 · 2026-05-22T14:42:38.106Z_

<details><summary>↩ Tool result · `toolu_01SNYNS5johcmExrx267A7B9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"430 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "82bad3dc-27b8-4a33-a29d-c5401d24fbac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"430 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"430 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 286_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GEvEVa5v6Ec7pHgBEJtrXT`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -215 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "63ac3312-f4ae-4982-aaa5-daf62b1e960a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4BJxR6VWaSY2B1GgmVgzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 29956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 346
      },
      "output_tokens": 65,
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

_source line 287 · 2026-05-22T14:42:41.258Z_

<details><summary>↩ Tool result · `toolu_01GEvEVa5v6Ec7pHgBEJtrXT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(a\\n\\n... [截断: 输出过长，省略 1022 字符] ...\\n\\nessor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n        inputs[\\\"input_ids\\\"] = ids\\n        return inputs\\n\\n    elif arch == \\\"tracvla\\\":\\n        prompt = (\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n                  f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n                  \\\"<|assistant|>\\\\n\\\")\\n        inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        return inputs\\n\\n    elif arch == \\\"nora\\\":\\n        messages = [{\\\"role\\\": \\\"user\\\", \\\"content\\\": [\\n            {\\\"type\\\": \\\"image\\\", \\\"image\\\": image},\\n            {\\\"type\\\": \\\"text\\\", \\\"text\\\": instruction},\\n        ]}]\\n        text = processor.apply_chat_template(\\n            messages, tokenize=False, add_generation_prompt=True)\\n        inputs = processor(text=[text], images=[image], return_tensors=\\\"pt\\\", padding=True)\\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\\n                for k, v in inputs.items()}\\n\\n\\ndef discover_tasks(data_dir):\\n    tasks = []\\n    for f in sorted(os.listdir(data_dir)):\\n        if f.endswith(\\\"_demo.hdf5\\\"):\\n            tasks.append(f.replace(\\\"_demo.hdf5\\\", \\\"\\\"))\\n    instructions = [t.replace(\\\"_\\\", \\\" \\\") for t in tasks]\\n    return tasks, instructions\\n\\n\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\n                     device, n_demos, n_timesteps):\\n    info = ARCH_INFO[arch]\\n    n_layers = info[\\\"n_layers\\\"]\\n    hidden = info[\\\"hidden\\\"]\\n    total = len(tasks) * n_demos * n_timesteps\\n\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\n    actions = np.zeros((total, 7), dtype=np.float32)\\n    demo_ids = np.zeros(total, dtype=np.int64)\\n\\n    idx = 0\\n    gd = 0\\n\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\n        hdf5_path = os.path.join(data_dir, f\\\"{task}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{len(tasks)}: {task}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo_key = f\\\"data/demo_{di}\\\"\\n                if demo_key not in hf:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "e8d61d76-7800-4528-8266-126abebdbe30",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(a\\\\n\\\\n... [截断: 输出过长，省略 1022 字符] ...\\\\n\\\\nessor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n        ds_path = os.path.join(ckpt_path, \\\\\\\"dataset_statistics.json\\\\\\\")\\\\n        if os.path.exists(ds_path):\\\\n            with open(ds_path) as f:\\\\n                ds_stats = json.load(f)\\\\n            for k, v in ds_stats.items():\\\\n                if k not in model.norm_stats:\\\\n                    model.norm_stats[k] = v\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\\\n        model = AutoModelForCausalLM.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\\\n        model = AutoModelForImageTextToText.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    log(f\\\\\\\"  Loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n    return model, processor\\\\n\\\\n\\\\ndef prepare_inputs(arch, processor, instruction, image, device):\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        prompt = f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n        inputs = processor(prompt, image).to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n        if not torch.all(ids[:, -1] == 29871):\\\\n            ids = torch.cat(\\\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\\\n            if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n                inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                    (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)),\\\\n                    dim=1)\\\\n        inputs[\\\\\\\"input_ids\\\\\\\"] = ids\\\\n        return inputs\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        prompt = (\\\\\\\"<|user|>\\\\\\\\n<|image_1|>\\\\\\\\n\\\\\\\"\\\\n                  f\\\\\\\"What action should the robot take to {instruction}?<|end|>\\\\\\\\n\\\\\\\"\\\\n                  \\\\\\\"<|assistant|>\\\\\\\\n\\\\\\\")\\\\n        inputs = processor(prompt, [image], return_tensors=\\\\\\\"pt\\\\\\\").to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        return inputs\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        messages = [{\\\\\\\"role\\\\\\\": \\\\\\\"user\\\\\\\", \\\\\\\"content\\\\\\\": [\\\\n            {\\\\\\\"type\\\\\\\": \\\\\\\"image\\\\\\\", \\\\\\\"image\\\\\\\": image},\\\\n            {\\\\\\\"type\\\\\\\": \\\\\\\"text\\\\\\\", \\\\\\\"text\\\\\\\": instruction},\\\\n        ]}]\\\\n        text = processor.apply_chat_template(\\\\n            messages, tokenize=False, add_generation_prompt=True)\\\\n        inputs = processor(text=[text], images=[image], return_tensors=\\\\\\\"pt\\\\\\\", padding=True)\\\\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\\\\n                for k, v in inputs.items()}\\\\n\\\\n\\\\ndef discover_tasks(data_dir):\\\\n    tasks = []\\\\n    for f in sorted(os.listdir(data_dir)):\\\\n        if f.endswith(\\\\\\\"_demo.hdf5\\\\\\\"):\\\\n            tasks.append(f.replace(\\\\\\\"_demo.hdf5\\\\\\\", \\\\\\\"\\\\\\\"))\\\\n    instructions = [t.replace(\\\\\\\"_\\\\\\\", \\\\\\\" \\\\\\\") for t in tasks]\\\\n    return tasks, instructions\\\\n\\\\n\\\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\\\n                     device, n_demos, n_timesteps):\\\\n    info = ARCH_INFO[arch]\\\\n    n_layers = info[\\\\\\\"n_layers\\\\\\\"]\\\\n    hidden = info[\\\\\\\"hidden\\\\\\\"]\\\\n    total = len(tasks) * n_demos * n_timesteps\\\\n\\\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\\\n    actions = np.zeros((total, 7), dtype=np.float32)\\\\n    demo_ids = np.zeros(total, dtype=np.int64)\\\\n\\\\n    idx = 0\\\\n    gd = 0\\\\n\\\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\\\n        hdf5_path = os.path.join(data_dir, f\\\\\\\"{task}_demo.hdf5\\\\\\\")\\\\n        log(f\\\\\\\"  Task {ti}/{len(tasks)}: {task}\\\\\\\")\\\\n\\\\n        with h5py.File(hdf5_path, \\\\\\\"r\\\\\\\") as hf:\\\\n            for di in range(n_demos):\\\\n                demo_key = f\\\\\\\"data/demo_{di}\\\\\\\"\\\\n                if demo_key not in hf:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(a\\n\\n... [截断: 输出过长，省略 1022 字符] ...\\n\\nessor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n        inputs[\\\"input_ids\\\"] = ids\\n        return inputs\\n\\n    elif arch == \\\"tracvla\\\":\\n        prompt = (\\\"<|user|>\\\\n<|image_1|>\\\\n\\\"\\n                  f\\\"What action should the robot take to {instruction}?<|end|>\\\\n\\\"\\n                  \\\"<|assistant|>\\\\n\\\")\\n        inputs = processor(prompt, [image], return_tensors=\\\"pt\\\").to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        return inputs\\n\\n    elif arch == \\\"nora\\\":\\n        messages = [{\\\"role\\\": \\\"user\\\", \\\"content\\\": [\\n            {\\\"type\\\": \\\"image\\\", \\\"image\\\": image},\\n            {\\\"type\\\": \\\"text\\\", \\\"text\\\": instruction},\\n        ]}]\\n        text = processor.apply_chat_template(\\n            messages, tokenize=False, add_generation_prompt=True)\\n        inputs = processor(text=[text], images=[image], return_tensors=\\\"pt\\\", padding=True)\\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\\n                for k, v in inputs.items()}\\n\\n\\ndef discover_tasks(data_dir):\\n    tasks = []\\n    for f in sorted(os.listdir(data_dir)):\\n        if f.endswith(\\\"_demo.hdf5\\\"):\\n            tasks.append(f.replace(\\\"_demo.hdf5\\\", \\\"\\\"))\\n    instructions = [t.replace(\\\"_\\\", \\\" \\\") for t in tasks]\\n    return tasks, instructions\\n\\n\\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\\n                     device, n_demos, n_timesteps):\\n    info = ARCH_INFO[arch]\\n    n_layers = info[\\\"n_layers\\\"]\\n    hidden = info[\\\"hidden\\\"]\\n    total = len(tasks) * n_demos * n_timesteps\\n\\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\\n    actions = np.zeros((total, 7), dtype=np.float32)\\n    demo_ids = np.zeros(total, dtype=np.int64)\\n\\n    idx = 0\\n    gd = 0\\n\\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\\n        hdf5_path = os.path.join(data_dir, f\\\"{task}_demo.hdf5\\\")\\n        log(f\\\"  Task {ti}/{len(tasks)}: {task}\\\")\\n\\n        with h5py.File(hdf5_path, \\\"r\\\") as hf:\\n            for di in range(n_demos):\\n                demo_key = f\\\"data/demo_{di}\\\"\\n                if demo_key not in hf:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 288_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016RCD6NwThZMTE6WHMPhMEb`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +216 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "db351be5-fb26-4ce5-8338-c768e0b4eb42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HB39ecwrYdGiqpv2Z6GUz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3545,
      "cache_read_input_tokens": 30302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3545
      },
      "output_tokens": 40,
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

_source line 289 · 2026-05-22T14:42:48.403Z_

<details><summary>↩ Tool result · `toolu_016RCD6NwThZMTE6WHMPhMEb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"                    gd += 1\\n                    continue\\n                n_avail = hf[demo_key][\\\"actions\\\"].shape[0]\\n\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo_key}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo_key}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\n                    with torch.no_grad():\\n                        out = model(**inputs, output_hidden_states=True)\\n\\n                    for l in range(n_layers):\\n                        hs = out.hidden_states[l + 1][0]\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\n\\n                    actions[idx] = act\\n                    demo_ids[idx] = gd\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 50 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total} samples\\\")\\n\\n                gd += 1\\n\\n    log(f\\\"  Extraction done: {idx} samples, {gd} demos\\\")\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\n    return features, actions[:idx], demo_ids[:idx]\\n\\n\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\n    unique_demos = np.unique(demo_ids)\\n    n_total = len(unique_demos)\\n    n_train = int(0.8 * n_total)\\n    log(f\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\")\\n\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\n\\n    rng = np.random.RandomState(seed)\\n    canon_perm = rng.permutation(unique_demos)\\n    canon_train = set(canon_perm[:n_train].tolist())\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\n    test_mask = ~train_mask\\n\\n    y_tr_canon = actions[train_mask]\\n    y_te_canon = actions[test_mask]\\n\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\n    best_alpha = {}\\n    canon_r2 = {}\\n\\n    log(\\\"  Canonical split -- fitting RidgeCV per layer...\\\")\\n    for l in range(n_layers):\\n        probe = RidgeCV(alphas=alphas_list)\\n        probe.fit(features[l][train_mask], y_tr_canon)\\n        best_alpha[l] = float(probe.alpha_)\\n        pred = probe.predict(features[l][test_mask])\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n    # Precompute kernel matrices per layer for efficient bootstrap\\n    log(\\\"  Precomputing kernel matrices...\\\")\\n    N = len(actions)\\n    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\n\\n        if len(te_idx) == 0:\\n            continue\\n\\n        y_tr = actions[tr_idx]\\n        y_te = actions[te_idx]\\n        y_te_mean = y_te.mean(axis=0)\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\n        if ss_tot < 1e-10:\\n            continue\\n\\n        n_tr = len(tr_idx)\\n        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\\n        if (b + 1) % report_every == 0:\\n\\n\\n... [截断: 输出过长，省略 60 字符] ...\\n\\nlayers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    data_dir = os.path.join(DATA_ROOT, f\\\"libero_{args.suite}\\\")\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "8d09fb4e-4c72-44f0-955e-30e84ea77302",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"                    gd += 1\\\\n                    continue\\\\n                n_avail = hf[demo_key][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo_key}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo_key}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\\\n                    with torch.no_grad():\\\\n                        out = model(**inputs, output_hidden_states=True)\\\\n\\\\n                    for l in range(n_layers):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\\\n\\\\n                    actions[idx] = act\\\\n                    demo_ids[idx] = gd\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 50 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total} samples\\\\\\\")\\\\n\\\\n                gd += 1\\\\n\\\\n    log(f\\\\\\\"  Extraction done: {idx} samples, {gd} demos\\\\\\\")\\\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\\\n    return features, actions[:idx], demo_ids[:idx]\\\\n\\\\n\\\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\\\n    unique_demos = np.unique(demo_ids)\\\\n    n_total = len(unique_demos)\\\\n    n_train = int(0.8 * n_total)\\\\n    log(f\\\\\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\\\\\")\\\\n\\\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\\\n\\\\n    rng = np.random.RandomState(seed)\\\\n    canon_perm = rng.permutation(unique_demos)\\\\n    canon_train = set(canon_perm[:n_train].tolist())\\\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\\\n    test_mask = ~train_mask\\\\n\\\\n    y_tr_canon = actions[train_mask]\\\\n    y_te_canon = actions[test_mask]\\\\n\\\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\\\n    best_alpha = {}\\\\n    canon_r2 = {}\\\\n\\\\n    log(\\\\\\\"  Canonical split -- fitting RidgeCV per layer...\\\\\\\")\\\\n    for l in range(n_layers):\\\\n        probe = RidgeCV(alphas=alphas_list)\\\\n        probe.fit(features[l][train_mask], y_tr_canon)\\\\n        best_alpha[l] = float(probe.alpha_)\\\\n        pred = probe.predict(features[l][test_mask])\\\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\n\\\\n    # Precompute kernel matrices per layer for efficient bootstrap\\\\n    log(\\\\\\\"  Precomputing kernel matrices...\\\\\\\")\\\\n    N = len(actions)\\\\n    kernels = {}\\\\n    for l in range(n_layers):\\\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\\\n\\\\n    log(f\\\\\\\"  Bootstrap ({n_bootstrap} iterations)...\\\\\\\")\\\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\\\n    rng2 = np.random.RandomState(seed + 1)\\\\n    report_every = max(1, n_bootstrap // 10)\\\\n\\\\n    for b in range(n_bootstrap):\\\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\\\n        tr_demos = resampled[:n_train]\\\\n        te_demos = resampled[n_train:]\\\\n\\\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\\\n\\\\n        if len(te_idx) == 0:\\\\n            continue\\\\n\\\\n        y_tr = actions[tr_idx]\\\\n        y_te = actions[te_idx]\\\\n        y_te_mean = y_te.mean(axis=0)\\\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\\\n        if ss_tot < 1e-10:\\\\n            continue\\\\n\\\\n        n_tr = len(tr_idx)\\\\n        for l in range(n_layers):\\\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\\\n            try:\\\\n                w = np.linalg.solve(K_tr, y_tr)\\\\n                pred = K_te_tr @ w\\\\n                ss_res = np.sum((y_te - pred) ** 2)\\\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\\\n            except np.linalg.LinAlgError:\\\\n                boot_r2[b, l] = 0.0\\\\n\\\\n        if (b + 1) % report_every == 0:\\\\n\\\\n\\\\n... [截断: 输出过长，省略 60 字符] ...\\\\n\\\\nlayers - 1\\\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\\\n    exit_r2_boot = boot_r2[:, exit_l]\\\\n    deltas = peak_r2_boot - exit_r2_boot\\\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\\\n\\\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\\\n\\\\n    return {\\\\n        \\\\\\\"per_layer_r2\\\\\\\": {f\\\\\\\"L{l}\\\\\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\\\n        \\\\\\\"peak_r2\\\\\\\": round(canon_r2[canon_peak_l], 4),\\\\n        \\\\\\\"peak_layer\\\\\\\": f\\\\\\\"L{canon_peak_l}\\\\\\\",\\\\n        \\\\\\\"exit_r2\\\\\\\": round(canon_r2[exit_l], 4),\\\\n        \\\\\\\"exit_layer\\\\\\\": f\\\\\\\"L{exit_l}\\\\\\\",\\\\n        \\\\\\\"delta\\\\\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\\\n        \\\\\\\"delta_ci_95\\\\\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\\\n        \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(deltas)), 4),\\\\n            \\\\\\\"std\\\\\\\": round(float(np.std(deltas)), 4),\\\\n            \\\\\\\"median\\\\\\\": round(float(np.median(deltas)), 4),\\\\n        },\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--arch\\\\\\\", required=True, choices=[\\\\\\\"openvla\\\\\\\", \\\\\\\"tracvla\\\\\\\", \\\\\\\"nora\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", required=True, choices=[\\\\\\\"goal\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"object\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--condition\\\\\\\", required=True, choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--n_bootstrap\\\\\\\", type=int, default=10000)\\\\n    p.add_argument(\\\\\\\"--n_demos\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--n_timesteps\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\",\\\\n                   default=\\\\\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    args = p.parse_args()\\\\n\\\\n    if args.dry_run:\\\\n        args.n_demos = 2\\\\n        args.n_timesteps = 5\\\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\\\n\\\\n    if args.suite not in CKPT.get(args.arch, {}):\\\\n        log(f\\\\\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n    if args.condition not in CKPT[args.arch][args.suite]:\\\\n        log(f\\\\\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = f\\\\\\\"cuda:{args.gpu}\\\\\\\"\\\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\\\n    data_dir = os.path.join(DATA_ROOT, f\\\\\\\"libero_{args.suite}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\\\\\")\\\\n    log(f\\\\\\\"Checkpoint: {ckpt_path}\\\\\\\")\\\\n    log(f\\\\\\\"Data: {data_dir}\\\\\\\")\\\\n    log(f\\\\\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\\\\\")\\\\n    if args.dry_run:\\\\n        log(\\\\\\\"DRY RUN\\\\\\\")\\\\n\\\\n    tasks, instructions = discover_tasks(data_dir)\\\\n    if args.dry_run:\\\\n        tasks = tasks[:2]\\\\n        instructions = instructions[:2]\\\\n    log(f\\\\\\\"Tasks: {len(tasks)}\\\\\\\")\\\\n\\\\n    model, processor = load_model(args.arch, ckpt_path, device)\\\\n\\\\n    t0 = time.time()\\\\n    features, actions, demo_ids = extract_features(\\\\n        args.arch, model, processor, tasks, instructions, data_dir,\\\\n        device, args.n_demos, args.n_timesteps)\\\\n    log(f\\\\\\\"Extraction: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    del model, processor\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    n_layers = ARCH_INFO[args.arch][\\\\\\\"n_layers\\\\\\\"]\\\\n    result = clustered_bootstrap_r2(\\\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\\\n    log(f\\\\\\\"Bootstrap: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    result[\\\\\\\"arch\\\\\\\"] = args.arch\\\\n    result[\\\\\\\"suite\\\\\\\"] = args.suite\\\\n    result[\\\\\\\"condition\\\\\\\"] = args.condition\\\\n    result[\\\\\\\"n_demos\\\\\\\"] = int(len(np.unique(demo_ids)))\\\\n    result[\\\\\\\"n_total_samples\\\\\\\"] = int(len(actions))\\\\n    result[\\\\\\\"n_bootstrap\\\\\\\"] = args.n_bootstrap\\\\n    result[\\\\\\\"dry_run\\\\\\\"] = args.dry_run\\\\n\\\\n    out_dir = os.path.join(args.output_dir, f\\\\\\\"{args.arch}_{args.suite}\\\\\\\")\\\\n    os.makedirs(out_dir, exist_ok=True)\\\\n    out_path = os.path.join(out_dir, f\\\\\\\"{args.condition}.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    log(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"                    gd += 1\\n                    continue\\n                n_avail = hf[demo_key][\\\"actions\\\"].shape[0]\\n\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo_key}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo_key}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\n                    with torch.no_grad():\\n                        out = model(**inputs, output_hidden_states=True)\\n\\n                    for l in range(n_layers):\\n                        hs = out.hidden_states[l + 1][0]\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\n\\n                    actions[idx] = act\\n                    demo_ids[idx] = gd\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 50 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total} samples\\\")\\n\\n                gd += 1\\n\\n    log(f\\\"  Extraction done: {idx} samples, {gd} demos\\\")\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\n    return features, actions[:idx], demo_ids[:idx]\\n\\n\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\n    unique_demos = np.unique(demo_ids)\\n    n_total = len(unique_demos)\\n    n_train = int(0.8 * n_total)\\n    log(f\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\")\\n\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\n\\n    rng = np.random.RandomState(seed)\\n    canon_perm = rng.permutation(unique_demos)\\n    canon_train = set(canon_perm[:n_train].tolist())\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\n    test_mask = ~train_mask\\n\\n    y_tr_canon = actions[train_mask]\\n    y_te_canon = actions[test_mask]\\n\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\n    best_alpha = {}\\n    canon_r2 = {}\\n\\n    log(\\\"  Canonical split -- fitting RidgeCV per layer...\\\")\\n    for l in range(n_layers):\\n        probe = RidgeCV(alphas=alphas_list)\\n        probe.fit(features[l][train_mask], y_tr_canon)\\n        best_alpha[l] = float(probe.alpha_)\\n        pred = probe.predict(features[l][test_mask])\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n    # Precompute kernel matrices per layer for efficient bootstrap\\n    log(\\\"  Precomputing kernel matrices...\\\")\\n    N = len(actions)\\n    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\n\\n        if len(te_idx) == 0:\\n            continue\\n\\n        y_tr = actions[tr_idx]\\n        y_te = actions[te_idx]\\n        y_te_mean = y_te.mean(axis=0)\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\n        if ss_tot < 1e-10:\\n            continue\\n\\n        n_tr = len(tr_idx)\\n        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\\n        if (b + 1) % report_every == 0:\\n\\n\\n... [截断: 输出过长，省略 60 字符] ...\\n\\nlayers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    data_dir = os.path.join(DATA_ROOT, f\\\"libero_{args.suite}\\\")\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 290_

<details><summary>Logged reasoning block</summary>

```text
I have the full script now. There are still some truncated parts. Let me get lines 100-215 to fill the gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "9f937891-4c01-40c2-8c8e-d7eca72727a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxzYvt18EQAGRmAjNP26gM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3643,
      "cache_read_input_tokens": 33847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3643
      },
      "output_tokens": 9,
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

_source line 291_

Let me get the missing middle section (the `load_model` function that was truncated).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "a58d303d-1d08-4748-afd1-68a6590923be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxzYvt18EQAGRmAjNP26gM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3643,
      "cache_read_input_tokens": 33847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3643
      },
      "output_tokens": 9,
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

_source line 292_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013LLPqTdvpN3W4BBTqrPWMp`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -115 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "f5361779-b99a-4ff4-85f6-0f3f6479b311",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxzYvt18EQAGRmAjNP26gM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3643,
      "cache_read_input_tokens": 33847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3643
      },
      "output_tokens": 9,
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

_source line 293 · 2026-05-22T14:43:01.289Z_

<details><summary>↩ Tool result · `toolu_013LLPqTdvpN3W4BBTqrPWMp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "57f70229-94ce-4c57-b210-bb37b8a4f0de",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(arch, ckpt_path, device):\\\\n    log(f\\\\\\\"Loading {arch} from {ckpt_path}\\\\\\\")\\\\n    t0 = time.time()\\\\n\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        _load_openvla_modules(ckpt_path)\\\\n        config_cls = sys.modules[\\\\\\\"configuration_prismatic\\\\\\\"].OpenVLAConfig\\\\n        model_cls = sys.modules[\\\\\\\"modeling_prismatic\\\\\\\"].OpenVLAForActionPrediction\\\\n        proc_cls = sys.modules[\\\\\\\"processing_prismatic\\\\\\\"].PrismaticProcessor\\\\n\\\\n        config = config_cls.from_pretrained(ckpt_path)\\\\n        model = model_cls.from_pretrained(\\\\n            ckpt_path, config=config, dtype=torch.bfloat16\\\\n        ).to(device).eval()\\\\n        # Patch transformers.tokenization_utils for HF cache loading\\\\n        import transformers.tokenization_utils_base as _tub\\\\n        from transformers.utils import PaddingStrategy as _PS\\\\n        _tu = sys.modules[\\\\\\\"transformers.tokenization_utils\\\\\\\"]\\\\n        _tu.PaddingStrategy = _PS\\\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 294_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0179T8jzFirxKtvA9PVuVaXs`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -160 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "7dc67ed4-021b-4a40-93bf-c0b12d0557c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015iJ6nShnBMnFhfVzUbQTD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 37490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2482
      },
      "output_tokens": 40,
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

_source line 295 · 2026-05-22T14:43:05.217Z_

<details><summary>↩ Tool result · `toolu_0179T8jzFirxKtvA9PVuVaXs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n        _tu.TextInput = _tub.TextInput\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "2f24718b-b2cc-4d57-9ce3-c840ece9a8f1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(arch, ckpt_path, device):\\\\n    log(f\\\\\\\"Loading {arch} from {ckpt_path}\\\\\\\")\\\\n    t0 = time.time()\\\\n\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        _load_openvla_modules(ckpt_path)\\\\n        config_cls = sys.modules[\\\\\\\"configuration_prismatic\\\\\\\"].OpenVLAConfig\\\\n        model_cls = sys.modules[\\\\\\\"modeling_prismatic\\\\\\\"].OpenVLAForActionPrediction\\\\n        proc_cls = sys.modules[\\\\\\\"processing_prismatic\\\\\\\"].PrismaticProcessor\\\\n\\\\n        config = config_cls.from_pretrained(ckpt_path)\\\\n        model = model_cls.from_pretrained(\\\\n            ckpt_path, config=config, dtype=torch.bfloat16\\\\n        ).to(device).eval()\\\\n        # Patch transformers.tokenization_utils for HF cache loading\\\\n        import transformers.tokenization_utils_base as _tub\\\\n        from transformers.utils import PaddingStrategy as _PS\\\\n        _tu = sys.modules[\\\\\\\"transformers.tokenization_utils\\\\\\\"]\\\\n        _tu.PaddingStrategy = _PS\\\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\\\n        _tu.TextInput = _tub.TextInput\\\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n        ds_path = os.path.join(ckpt_path, \\\\\\\"dataset_statistics.json\\\\\\\")\\\\n        if os.path.exists(ds_path):\\\\n            with open(ds_path) as f:\\\\n                ds_stats = json.load(f)\\\\n            for k, v in ds_stats.items():\\\\n                if k not in model.norm_stats:\\\\n                    model.norm_stats[k] = v\\\\n\\\\n    elif arch == \\\\\\\"tracvla\\\\\\\":\\\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\\\n        model = AutoModelForCausalLM.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    elif arch == \\\\\\\"nora\\\\\\\":\\\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\\\n        model = AutoModelForImageTextToText.from_pretrained(\\\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\\\n        ).to(device).eval()\\\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\\\n\\\\n    log(f\\\\\\\"  Loaded in {time.time()-t0:.1f}s\\\\\\\")\\\\n    return model, processor\\\\n\\\\n\\\\ndef prepare_inputs(arch, processor, instruction, image, device):\\\\n    if arch == \\\\\\\"openvla\\\\\\\":\\\\n        prompt = f\\\\\\\"In: What action should the robot take to {instruction}?\\\\\\\\nOut:\\\\\\\"\\\\n        inputs = processor(prompt, image).to(device)\\\\n        if \\\\\\\"pixel_values\\\\\\\" in inputs:\\\\n            inputs[\\\\\\\"pixel_values\\\\\\\"] = inputs[\\\\\\\"pixel_values\\\\\\\"].to(torch.bfloat16)\\\\n        ids = inputs[\\\\\\\"input_ids\\\\\\\"]\\\\n        if not torch.all(ids[:, -1] == 29871):\\\\n            ids = torch.cat(\\\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\\\n            if \\\\\\\"attention_mask\\\\\\\" in inputs:\\\\n                inputs[\\\\\\\"attention_mask\\\\\\\"] = torch.cat(\\\\n                    (inputs[\\\\\\\"attention_mask\\\\\\\"],\\\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\\\\\"attention_mask\\\\\\\"].dtype)),\\\\n                    dim=1)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(arch, ckpt_path, device):\\n    log(f\\\"Loading {arch} from {ckpt_path}\\\")\\n    t0 = time.time()\\n\\n    if arch == \\\"openvla\\\":\\n        _load_openvla_modules(ckpt_path)\\n        config_cls = sys.modules[\\\"configuration_prismatic\\\"].OpenVLAConfig\\n        model_cls = sys.modules[\\\"modeling_prismatic\\\"].OpenVLAForActionPrediction\\n        proc_cls = sys.modules[\\\"processing_prismatic\\\"].PrismaticProcessor\\n\\n        config = config_cls.from_pretrained(ckpt_path)\\n        model = model_cls.from_pretrained(\\n            ckpt_path, config=config, dtype=torch.bfloat16\\n        ).to(device).eval()\\n        # Patch transformers.tokenization_utils for HF cache loading\\n        import transformers.tokenization_utils_base as _tub\\n        from transformers.utils import PaddingStrategy as _PS\\n        _tu = sys.modules[\\\"transformers.tokenization_utils\\\"]\\n        _tu.PaddingStrategy = _PS\\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\\n        _tu.TextInput = _tub.TextInput\\n        _tu.TruncationStrategy = _tub.TruncationStrategy\\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n        ds_path = os.path.join(ckpt_path, \\\"dataset_statistics.json\\\")\\n        if os.path.exists(ds_path):\\n            with open(ds_path) as f:\\n                ds_stats = json.load(f)\\n            for k, v in ds_stats.items():\\n                if k not in model.norm_stats:\\n                    model.norm_stats[k] = v\\n\\n    elif arch == \\\"tracvla\\\":\\n        from transformers import AutoModelForCausalLM, AutoProcessor\\n        model = AutoModelForCausalLM.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    elif arch == \\\"nora\\\":\\n        from transformers import AutoModelForImageTextToText, AutoProcessor\\n        model = AutoModelForImageTextToText.from_pretrained(\\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\\n        ).to(device).eval()\\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\\n\\n    log(f\\\"  Loaded in {time.time()-t0:.1f}s\\\")\\n    return model, processor\\n\\n\\ndef prepare_inputs(arch, processor, instruction, image, device):\\n    if arch == \\\"openvla\\\":\\n        prompt = f\\\"In: What action should the robot take to {instruction}?\\\\nOut:\\\"\\n        inputs = processor(prompt, image).to(device)\\n        if \\\"pixel_values\\\" in inputs:\\n            inputs[\\\"pixel_values\\\"] = inputs[\\\"pixel_values\\\"].to(torch.bfloat16)\\n        ids = inputs[\\\"input_ids\\\"]\\n        if not torch.all(ids[:, -1] == 29871):\\n            ids = torch.cat(\\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\\n            if \\\"attention_mask\\\" in inputs:\\n                inputs[\\\"attention_mask\\\"] = torch.cat(\\n                    (inputs[\\\"attention_mask\\\"],\\n                     torch.ones(1, 1, device=device, dtype=inputs[\\\"attention_mask\\\"].dtype)),\\n                    dim=1)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 296_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the content. Let me also get the lines around the truncation point (around line 310) to capture the report_every line.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "34afc9d2-dde2-4590-a620-b9cafc0c8012",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUbasYVfp7zJFiTuYPVc7F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 39972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3036
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

_source line 297_

Now I have the full script content. Let me also get the one truncated line around line 310.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "a4f0256f-e3ee-40be-ab52-830b3c8e4dfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUbasYVfp7zJFiTuYPVc7F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 39972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3036
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

_source line 298_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0179W2Ebv7jmsm3fSifpPzH1`</summary>

```json
{
  "server": "westd-19183",
  "command": "head -320 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "72201916-edcf-4f73-9127-1646790b84a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUbasYVfp7zJFiTuYPVc7F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 39972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3036
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

_source line 299 · 2026-05-22T14:43:14.924Z_

<details><summary>↩ Tool result · `toolu_0179W2Ebv7jmsm3fSifpPzH1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(a\\n\\n... [截断: 输出过长，省略 4981 字符] ...\\n\\n\\\"\\n                if demo_key not in hf:\\n                    gd += 1\\n                    continue\\n                n_avail = hf[demo_key][\\\"actions\\\"].shape[0]\\n\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo_key}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo_key}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\n                    with torch.no_grad():\\n                        out = model(**inputs, output_hidden_states=True)\\n\\n                    for l in range(n_layers):\\n                        hs = out.hidden_states[l + 1][0]\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\n\\n                    actions[idx] = act\\n                    demo_ids[idx] = gd\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 50 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total} samples\\\")\\n\\n                gd += 1\\n\\n    log(f\\\"  Extraction done: {idx} samples, {gd} demos\\\")\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\n    return features, actions[:idx], demo_ids[:idx]\\n\\n\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\n    unique_demos = np.unique(demo_ids)\\n    n_total = len(unique_demos)\\n    n_train = int(0.8 * n_total)\\n    log(f\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\")\\n\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\n\\n    rng = np.random.RandomState(seed)\\n    canon_perm = rng.permutation(unique_demos)\\n    canon_train = set(canon_perm[:n_train].tolist())\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\n    test_mask = ~train_mask\\n\\n    y_tr_canon = actions[train_mask]\\n    y_te_canon = actions[test_mask]\\n\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\n    best_alpha = {}\\n    canon_r2 = {}\\n\\n    log(\\\"  Canonical split -- fitting RidgeCV per layer...\\\")\\n    for l in range(n_layers):\\n        probe = RidgeCV(alphas=alphas_list)\\n        probe.fit(features[l][train_mask], y_tr_canon)\\n        best_alpha[l] = float(probe.alpha_)\\n        pred = probe.predict(features[l][test_mask])\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n    # Precompute kernel matrices per layer for efficient bootstrap\\n    log(\\\"  Precomputing kernel matrices...\\\")\\n    N = len(actions)\\n    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\n\\n        if len(te_idx) == 0:\\n            continue\\n\\n        y_tr = actions[tr_idx]\\n        y_te = actions[te_idx]\\n        y_te_mean = y_te.mean(axis=0)\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\n        if ss_tot < 1e-10:\\n            continue\\n\\n        n_tr = len(tr_idx)\\n        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "3d32ee65-4776-45ed-ab8c-fcba71feab29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse, json, os, sys, time, types\\\\nos.environ[\\\\\\\"HDF5_USE_FILE_LOCKING\\\\\\\"] = \\\\\\\"FALSE\\\\\\\"\\\\n\\\\nimport numpy as np\\\\nimport h5py\\\\nimport torch\\\\nfrom PIL import Image\\\\nfrom sklearn.linear_model import RidgeCV\\\\nimport importlib.util\\\\n\\\\n\\\\ndef log(msg):\\\\n    print(f\\\\\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\\\\\", flush=True)\\\\n\\\\n\\\\nCKPT = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n        \\\\\\\"object\\\\\\\":  {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\\\\\"},\\\\n    },\\\\n    \\\\\\\"nora\\\\\\\": {\\\\n        \\\\\\\"goal\\\\\\\":    {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n        \\\\\\\"spatial\\\\\\\": {\\\\\\\"trained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\\\\\",\\\\n                    \\\\\\\"untrained\\\\\\\": \\\\\\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\\\\\"},\\\\n    },\\\\n}\\\\n\\\\nARCH_INFO = {\\\\n    \\\\\\\"openvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 4096},\\\\n    \\\\\\\"tracvla\\\\\\\": {\\\\\\\"n_layers\\\\\\\": 32, \\\\\\\"hidden\\\\\\\": 3072},\\\\n    \\\\\\\"nora\\\\\\\":    {\\\\\\\"n_layers\\\\\\\": 36, \\\\\\\"hidden\\\\\\\": 2048},\\\\n}\\\\n\\\\nDATA_ROOT = \\\\\\\"/root/autodl-tmp/vla-ssd/data/libero\\\\\\\"\\\\n\\\\n\\\\ndef _load_openvla_modules(ckpt_path):\\\\n    pkg_name = \\\\\\\"_openvla_pkg\\\\\\\"\\\\n    pkg = types.ModuleType(pkg_name)\\\\n    pkg.__path__ = [ckpt_path]\\\\n    pkg.__package__ = pkg_name\\\\n    sys.modules[pkg_name] = pkg\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        # Fix transformers 5.x import changes\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        mod = types.ModuleType(full)\\\\n        mod.__file__ = fpath\\\\n        mod.__package__ = pkg_name\\\\n        sys.modules[full] = mod\\\\n        sys.modules[name] = mod\\\\n        setattr(pkg, name, mod)\\\\n\\\\n    for name in [\\\\\\\"configuration_prismatic\\\\\\\", \\\\\\\"modeling_prismatic\\\\\\\", \\\\\\\"processing_prismatic\\\\\\\"]:\\\\n        full = f\\\\\\\"{pkg_name}.{name}\\\\\\\"\\\\n        fpath = os.path.join(ckpt_path, f\\\\\\\"{name}.py\\\\\\\")\\\\n        with open(fpath) as f:\\\\n            src = f.read()\\\\n        src = src.replace(\\\\n            \\\\\\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\",\\\\n            \\\\\\\"from transformers.utils import PaddingStrategy\\\\\\\\n\\\\\\\"\\\\n            \\\\\\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\\\\\"\\\\n        )\\\\n        src = src.replace(\\\\n            \\\\\\\"def tie_weights(self) -> None:\\\\\\\",\\\\n            \\\\\\\"def tie_weights(self, **kwargs) -> None:\\\\\\\"\\\\n        )\\\\n        code = compile(src, fpath, \\\\\\\"exec\\\\\\\")\\\\n        exec(code, sys.modules[full].__dict__)\\\\n\\\\n\\\\ndef load_model(a\\\\n\\\\n... [截断: 输出过长，省略 4981 字符] ...\\\\n\\\\n\\\\\\\"\\\\n                if demo_key not in hf:\\\\n                    gd += 1\\\\n                    continue\\\\n                n_avail = hf[demo_key][\\\\\\\"actions\\\\\\\"].shape[0]\\\\n\\\\n                for t in range(min(n_timesteps, n_avail)):\\\\n                    img = Image.fromarray(hf[f\\\\\\\"{demo_key}/obs/agentview_rgb\\\\\\\"][t])\\\\n                    act = np.array(hf[f\\\\\\\"{demo_key}/actions\\\\\\\"][t], dtype=np.float32)\\\\n\\\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\\\n                    with torch.no_grad():\\\\n                        out = model(**inputs, output_hidden_states=True)\\\\n\\\\n                    for l in range(n_layers):\\\\n                        hs = out.hidden_states[l + 1][0]\\\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\\\n\\\\n                    actions[idx] = act\\\\n                    demo_ids[idx] = gd\\\\n                    idx += 1\\\\n\\\\n                    del out, inputs\\\\n                    if idx % 50 == 0:\\\\n                        torch.cuda.empty_cache()\\\\n                        log(f\\\\\\\"    {idx}/{total} samples\\\\\\\")\\\\n\\\\n                gd += 1\\\\n\\\\n    log(f\\\\\\\"  Extraction done: {idx} samples, {gd} demos\\\\\\\")\\\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\\\n    return features, actions[:idx], demo_ids[:idx]\\\\n\\\\n\\\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\\\n    unique_demos = np.unique(demo_ids)\\\\n    n_total = len(unique_demos)\\\\n    n_train = int(0.8 * n_total)\\\\n    log(f\\\\\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\\\\\")\\\\n\\\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\\\n\\\\n    rng = np.random.RandomState(seed)\\\\n    canon_perm = rng.permutation(unique_demos)\\\\n    canon_train = set(canon_perm[:n_train].tolist())\\\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\\\n    test_mask = ~train_mask\\\\n\\\\n    y_tr_canon = actions[train_mask]\\\\n    y_te_canon = actions[test_mask]\\\\n\\\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\\\n    best_alpha = {}\\\\n    canon_r2 = {}\\\\n\\\\n    log(\\\\\\\"  Canonical split -- fitting RidgeCV per layer...\\\\\\\")\\\\n    for l in range(n_layers):\\\\n        probe = RidgeCV(alphas=alphas_list)\\\\n        probe.fit(features[l][train_mask], y_tr_canon)\\\\n        best_alpha[l] = float(probe.alpha_)\\\\n        pred = probe.predict(features[l][test_mask])\\\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\\\n\\\\n    # Precompute kernel matrices per layer for efficient bootstrap\\\\n    log(\\\\\\\"  Precomputing kernel matrices...\\\\\\\")\\\\n    N = len(actions)\\\\n    kernels = {}\\\\n    for l in range(n_layers):\\\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\\\n\\\\n    log(f\\\\\\\"  Bootstrap ({n_bootstrap} iterations)...\\\\\\\")\\\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\\\n    rng2 = np.random.RandomState(seed + 1)\\\\n    report_every = max(1, n_bootstrap // 10)\\\\n\\\\n    for b in range(n_bootstrap):\\\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\\\n        tr_demos = resampled[:n_train]\\\\n        te_demos = resampled[n_train:]\\\\n\\\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\\\n\\\\n        if len(te_idx) == 0:\\\\n            continue\\\\n\\\\n        y_tr = actions[tr_idx]\\\\n        y_te = actions[te_idx]\\\\n        y_te_mean = y_te.mean(axis=0)\\\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\\\n        if ss_tot < 1e-10:\\\\n            continue\\\\n\\\\n        n_tr = len(tr_idx)\\\\n        for l in range(n_layers):\\\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\\\n            try:\\\\n                w = np.linalg.solve(K_tr, y_tr)\\\\n                pred = K_te_tr @ w\\\\n                ss_res = np.sum((y_te - pred) ** 2)\\\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\\\n            except np.linalg.LinAlgError:\\\\n                boot_r2[b, l] = 0.0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\\\"\\\"\\\"\\n\\nimport argparse, json, os, sys, time, types\\nos.environ[\\\"HDF5_USE_FILE_LOCKING\\\"] = \\\"FALSE\\\"\\n\\nimport numpy as np\\nimport h5py\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import RidgeCV\\nimport importlib.util\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\nCKPT = {\\n    \\\"openvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"},\\n    },\\n    \\\"tracvla\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n        \\\"object\\\":  {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\\\"},\\n    },\\n    \\\"nora\\\": {\\n        \\\"goal\\\":    {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n        \\\"spatial\\\": {\\\"trained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\\\",\\n                    \\\"untrained\\\": \\\"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\\\"},\\n    },\\n}\\n\\nARCH_INFO = {\\n    \\\"openvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 4096},\\n    \\\"tracvla\\\": {\\\"n_layers\\\": 32, \\\"hidden\\\": 3072},\\n    \\\"nora\\\":    {\\\"n_layers\\\": 36, \\\"hidden\\\": 2048},\\n}\\n\\nDATA_ROOT = \\\"/root/autodl-tmp/vla-ssd/data/libero\\\"\\n\\n\\ndef _load_openvla_modules(ckpt_path):\\n    pkg_name = \\\"_openvla_pkg\\\"\\n    pkg = types.ModuleType(pkg_name)\\n    pkg.__path__ = [ckpt_path]\\n    pkg.__package__ = pkg_name\\n    sys.modules[pkg_name] = pkg\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        # Fix transformers 5.x import changes\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        mod = types.ModuleType(full)\\n        mod.__file__ = fpath\\n        mod.__package__ = pkg_name\\n        sys.modules[full] = mod\\n        sys.modules[name] = mod\\n        setattr(pkg, name, mod)\\n\\n    for name in [\\\"configuration_prismatic\\\", \\\"modeling_prismatic\\\", \\\"processing_prismatic\\\"]:\\n        full = f\\\"{pkg_name}.{name}\\\"\\n        fpath = os.path.join(ckpt_path, f\\\"{name}.py\\\")\\n        with open(fpath) as f:\\n            src = f.read()\\n        src = src.replace(\\n            \\\"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\\\",\\n            \\\"from transformers.utils import PaddingStrategy\\\\n\\\"\\n            \\\"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\\\"\\n        )\\n        src = src.replace(\\n            \\\"def tie_weights(self) -> None:\\\",\\n            \\\"def tie_weights(self, **kwargs) -> None:\\\"\\n        )\\n        code = compile(src, fpath, \\\"exec\\\")\\n        exec(code, sys.modules[full].__dict__)\\n\\n\\ndef load_model(a\\n\\n... [截断: 输出过长，省略 4981 字符] ...\\n\\n\\\"\\n                if demo_key not in hf:\\n                    gd += 1\\n                    continue\\n                n_avail = hf[demo_key][\\\"actions\\\"].shape[0]\\n\\n                for t in range(min(n_timesteps, n_avail)):\\n                    img = Image.fromarray(hf[f\\\"{demo_key}/obs/agentview_rgb\\\"][t])\\n                    act = np.array(hf[f\\\"{demo_key}/actions\\\"][t], dtype=np.float32)\\n\\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\\n                    with torch.no_grad():\\n                        out = model(**inputs, output_hidden_states=True)\\n\\n                    for l in range(n_layers):\\n                        hs = out.hidden_states[l + 1][0]\\n                        features[l][idx] = hs[-1].float().cpu().numpy()\\n\\n                    actions[idx] = act\\n                    demo_ids[idx] = gd\\n                    idx += 1\\n\\n                    del out, inputs\\n                    if idx % 50 == 0:\\n                        torch.cuda.empty_cache()\\n                        log(f\\\"    {idx}/{total} samples\\\")\\n\\n                gd += 1\\n\\n    log(f\\\"  Extraction done: {idx} samples, {gd} demos\\\")\\n    features = {l: features[l][:idx] for l in range(n_layers)}\\n    return features, actions[:idx], demo_ids[:idx]\\n\\n\\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\\n    unique_demos = np.unique(demo_ids)\\n    n_total = len(unique_demos)\\n    n_train = int(0.8 * n_total)\\n    log(f\\\"  {n_total} demos, split {n_train}/{n_total - n_train}\\\")\\n\\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\\n\\n    rng = np.random.RandomState(seed)\\n    canon_perm = rng.permutation(unique_demos)\\n    canon_train = set(canon_perm[:n_train].tolist())\\n    train_mask = np.array([d in canon_train for d in demo_ids])\\n    test_mask = ~train_mask\\n\\n    y_tr_canon = actions[train_mask]\\n    y_te_canon = actions[test_mask]\\n\\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\\n    best_alpha = {}\\n    canon_r2 = {}\\n\\n    log(\\\"  Canonical split -- fitting RidgeCV per layer...\\\")\\n    for l in range(n_layers):\\n        probe = RidgeCV(alphas=alphas_list)\\n        probe.fit(features[l][train_mask], y_tr_canon)\\n        best_alpha[l] = float(probe.alpha_)\\n        pred = probe.predict(features[l][test_mask])\\n        ss_res = np.sum((y_te_canon - pred) ** 2)\\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\\n\\n    # Precompute kernel matrices per layer for efficient bootstrap\\n    log(\\\"  Precomputing kernel matrices...\\\")\\n    N = len(actions)\\n    kernels = {}\\n    for l in range(n_layers):\\n        kernels[l] = features[l] @ features[l].T  # (N, N)\\n\\n    log(f\\\"  Bootstrap ({n_bootstrap} iterations)...\\\")\\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\\n    rng2 = np.random.RandomState(seed + 1)\\n    report_every = max(1, n_bootstrap // 10)\\n\\n    for b in range(n_bootstrap):\\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\\n        tr_demos = resampled[:n_train]\\n        te_demos = resampled[n_train:]\\n\\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\\n\\n        if len(te_idx) == 0:\\n            continue\\n\\n        y_tr = actions[tr_idx]\\n        y_te = actions[te_idx]\\n        y_te_mean = y_te.mean(axis=0)\\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\\n        if ss_tot < 1e-10:\\n            continue\\n\\n        n_tr = len(tr_idx)\\n        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 300_

<details><summary>Logged reasoning block</summary>

```text
I still have a truncation. Let me get lines 310-320 specifically to see the report_every and exit_l lines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "57b867f3-f9c5-4ba1-82ed-e00a8b945d80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnMMAuqZj84qpS335Xuv8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3662,
      "cache_read_input_tokens": 43008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3662
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

_source line 301_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YNKwfpgRG9JTgPv5EcgawG`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +310 /root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "0bad8848-87c1-4e2e-ae58-dff3ad1b0573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MnMMAuqZj84qpS335Xuv8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3662,
      "cache_read_input_tokens": 43008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3662
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

_source line 302 · 2026-05-22T14:43:42.895Z_

<details><summary>↩ Tool result · `toolu_01YNKwfpgRG9JTgPv5EcgawG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\\n        if (b + 1) % report_every == 0:\\n            log(f\\\"    {b+1}/{n_bootstrap}\\\")\\n\\n    exit_l = n_layers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    data_dir = os.path.join(DATA_ROOT, f\\\"libero_{args.suite}\\\")\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "4eafd5a2-3f24-4c66-805b-c07ee30c16e6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"        for l in range(n_layers):\\\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\\\n            try:\\\\n                w = np.linalg.solve(K_tr, y_tr)\\\\n                pred = K_te_tr @ w\\\\n                ss_res = np.sum((y_te - pred) ** 2)\\\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\\\n            except np.linalg.LinAlgError:\\\\n                boot_r2[b, l] = 0.0\\\\n\\\\n        if (b + 1) % report_every == 0:\\\\n            log(f\\\\\\\"    {b+1}/{n_bootstrap}\\\\\\\")\\\\n\\\\n    exit_l = n_layers - 1\\\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\\\n    exit_r2_boot = boot_r2[:, exit_l]\\\\n    deltas = peak_r2_boot - exit_r2_boot\\\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\\\n\\\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\\\n\\\\n    return {\\\\n        \\\\\\\"per_layer_r2\\\\\\\": {f\\\\\\\"L{l}\\\\\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\\\n        \\\\\\\"peak_r2\\\\\\\": round(canon_r2[canon_peak_l], 4),\\\\n        \\\\\\\"peak_layer\\\\\\\": f\\\\\\\"L{canon_peak_l}\\\\\\\",\\\\n        \\\\\\\"exit_r2\\\\\\\": round(canon_r2[exit_l], 4),\\\\n        \\\\\\\"exit_layer\\\\\\\": f\\\\\\\"L{exit_l}\\\\\\\",\\\\n        \\\\\\\"delta\\\\\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\\\n        \\\\\\\"delta_ci_95\\\\\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\\\n        \\\\\\\"bootstrap_deltas_summary\\\\\\\": {\\\\n            \\\\\\\"mean\\\\\\\": round(float(np.mean(deltas)), 4),\\\\n            \\\\\\\"std\\\\\\\": round(float(np.std(deltas)), 4),\\\\n            \\\\\\\"median\\\\\\\": round(float(np.median(deltas)), 4),\\\\n        },\\\\n    }\\\\n\\\\n\\\\ndef main():\\\\n    p = argparse.ArgumentParser()\\\\n    p.add_argument(\\\\\\\"--arch\\\\\\\", required=True, choices=[\\\\\\\"openvla\\\\\\\", \\\\\\\"tracvla\\\\\\\", \\\\\\\"nora\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--suite\\\\\\\", required=True, choices=[\\\\\\\"goal\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"object\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--condition\\\\\\\", required=True, choices=[\\\\\\\"trained\\\\\\\", \\\\\\\"untrained\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--gpu\\\\\\\", type=int, default=0)\\\\n    p.add_argument(\\\\\\\"--n_bootstrap\\\\\\\", type=int, default=10000)\\\\n    p.add_argument(\\\\\\\"--n_demos\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--n_timesteps\\\\\\\", type=int, default=50)\\\\n    p.add_argument(\\\\\\\"--output_dir\\\\\\\",\\\\n                   default=\\\\\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--dry_run\\\\\\\", action=\\\\\\\"store_true\\\\\\\")\\\\n    args = p.parse_args()\\\\n\\\\n    if args.dry_run:\\\\n        args.n_demos = 2\\\\n        args.n_timesteps = 5\\\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\\\n\\\\n    if args.suite not in CKPT.get(args.arch, {}):\\\\n        log(f\\\\\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n    if args.condition not in CKPT[args.arch][args.suite]:\\\\n        log(f\\\\\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    device = f\\\\\\\"cuda:{args.gpu}\\\\\\\"\\\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\\\n    data_dir = os.path.join(DATA_ROOT, f\\\\\\\"libero_{args.suite}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\\\\\")\\\\n    log(f\\\\\\\"Checkpoint: {ckpt_path}\\\\\\\")\\\\n    log(f\\\\\\\"Data: {data_dir}\\\\\\\")\\\\n    log(f\\\\\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\\\\\")\\\\n    if args.dry_run:\\\\n        log(\\\\\\\"DRY RUN\\\\\\\")\\\\n\\\\n    tasks, instructions = discover_tasks(data_dir)\\\\n    if args.dry_run:\\\\n        tasks = tasks[:2]\\\\n        instructions = instructions[:2]\\\\n    log(f\\\\\\\"Tasks: {len(tasks)}\\\\\\\")\\\\n\\\\n    model, processor = load_model(args.arch, ckpt_path, device)\\\\n\\\\n    t0 = time.time()\\\\n    features, actions, demo_ids = extract_features(\\\\n        args.arch, model, processor, tasks, instructions, data_dir,\\\\n        device, args.n_demos, args.n_timesteps)\\\\n    log(f\\\\\\\"Extraction: {time.time()-t0:.1f}s\\\\\\\")\\\\n\\\\n    del model, processor\\\\n    torch.cuda.empty_cache()\\\\n\\\\n    t1 = time.time()\\\\n    n_layers = ARCH_INFO[args.arch][\\\\\\\"n_layers\\\\\\\"]\\\\n    result = clustered_bootstrap_r2(\\\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\\\n    log(f\\\\\\\"Bootstrap: {time.time()-t1:.1f}s\\\\\\\")\\\\n\\\\n    result[\\\\\\\"arch\\\\\\\"] = args.arch\\\\n    result[\\\\\\\"suite\\\\\\\"] = args.suite\\\\n    result[\\\\\\\"condition\\\\\\\"] = args.condition\\\\n    result[\\\\\\\"n_demos\\\\\\\"] = int(len(np.unique(demo_ids)))\\\\n    result[\\\\\\\"n_total_samples\\\\\\\"] = int(len(actions))\\\\n    result[\\\\\\\"n_bootstrap\\\\\\\"] = args.n_bootstrap\\\\n    result[\\\\\\\"dry_run\\\\\\\"] = args.dry_run\\\\n\\\\n    out_dir = os.path.join(args.output_dir, f\\\\\\\"{args.arch}_{args.suite}\\\\\\\")\\\\n    os.makedirs(out_dir, exist_ok=True)\\\\n    out_path = os.path.join(out_dir, f\\\\\\\"{args.condition}.json\\\\\\\")\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2)\\\\n    log(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n\\\\n    log(f\\\\\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\\\\\")\\\\n    log(f\\\\\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"        for l in range(n_layers):\\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\\n            try:\\n                w = np.linalg.solve(K_tr, y_tr)\\n                pred = K_te_tr @ w\\n                ss_res = np.sum((y_te - pred) ** 2)\\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\\n            except np.linalg.LinAlgError:\\n                boot_r2[b, l] = 0.0\\n\\n        if (b + 1) % report_every == 0:\\n            log(f\\\"    {b+1}/{n_bootstrap}\\\")\\n\\n    exit_l = n_layers - 1\\n    peak_r2_boot = np.max(boot_r2, axis=1)\\n    exit_r2_boot = boot_r2[:, exit_l]\\n    deltas = peak_r2_boot - exit_r2_boot\\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\\n\\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\\n\\n    return {\\n        \\\"per_layer_r2\\\": {f\\\"L{l}\\\": round(canon_r2[l], 4) for l in range(n_layers)},\\n        \\\"peak_r2\\\": round(canon_r2[canon_peak_l], 4),\\n        \\\"peak_layer\\\": f\\\"L{canon_peak_l}\\\",\\n        \\\"exit_r2\\\": round(canon_r2[exit_l], 4),\\n        \\\"exit_layer\\\": f\\\"L{exit_l}\\\",\\n        \\\"delta\\\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\\n        \\\"delta_ci_95\\\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\\n        \\\"bootstrap_deltas_summary\\\": {\\n            \\\"mean\\\": round(float(np.mean(deltas)), 4),\\n            \\\"std\\\": round(float(np.std(deltas)), 4),\\n            \\\"median\\\": round(float(np.median(deltas)), 4),\\n        },\\n    }\\n\\n\\ndef main():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--arch\\\", required=True, choices=[\\\"openvla\\\", \\\"tracvla\\\", \\\"nora\\\"])\\n    p.add_argument(\\\"--suite\\\", required=True, choices=[\\\"goal\\\", \\\"spatial\\\", \\\"object\\\"])\\n    p.add_argument(\\\"--condition\\\", required=True, choices=[\\\"trained\\\", \\\"untrained\\\"])\\n    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    p.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    p.add_argument(\\\"--n_demos\\\", type=int, default=10)\\n    p.add_argument(\\\"--n_timesteps\\\", type=int, default=50)\\n    p.add_argument(\\\"--output_dir\\\",\\n                   default=\\\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\\\")\\n    p.add_argument(\\\"--dry_run\\\", action=\\\"store_true\\\")\\n    args = p.parse_args()\\n\\n    if args.dry_run:\\n        args.n_demos = 2\\n        args.n_timesteps = 5\\n        args.n_bootstrap = min(args.n_bootstrap, 100)\\n\\n    if args.suite not in CKPT.get(args.arch, {}):\\n        log(f\\\"ERROR: no checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n    if args.condition not in CKPT[args.arch][args.suite]:\\n        log(f\\\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\\\")\\n        sys.exit(1)\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\\n    data_dir = os.path.join(DATA_ROOT, f\\\"libero_{args.suite}\\\")\\n\\n    log(f\\\"=== {args.arch} / {args.suite} / {args.condition} ===\\\")\\n    log(f\\\"Checkpoint: {ckpt_path}\\\")\\n    log(f\\\"Data: {data_dir}\\\")\\n    log(f\\\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\\\")\\n    if args.dry_run:\\n        log(\\\"DRY RUN\\\")\\n\\n    tasks, instructions = discover_tasks(data_dir)\\n    if args.dry_run:\\n        tasks = tasks[:2]\\n        instructions = instructions[:2]\\n    log(f\\\"Tasks: {len(tasks)}\\\")\\n\\n    model, processor = load_model(args.arch, ckpt_path, device)\\n\\n    t0 = time.time()\\n    features, actions, demo_ids = extract_features(\\n        args.arch, model, processor, tasks, instructions, data_dir,\\n        device, args.n_demos, args.n_timesteps)\\n    log(f\\\"Extraction: {time.time()-t0:.1f}s\\\")\\n\\n    del model, processor\\n    torch.cuda.empty_cache()\\n\\n    t1 = time.time()\\n    n_layers = ARCH_INFO[args.arch][\\\"n_layers\\\"]\\n    result = clustered_bootstrap_r2(\\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\\n    log(f\\\"Bootstrap: {time.time()-t1:.1f}s\\\")\\n\\n    result[\\\"arch\\\"] = args.arch\\n    result[\\\"suite\\\"] = args.suite\\n    result[\\\"condition\\\"] = args.condition\\n    result[\\\"n_demos\\\"] = int(len(np.unique(demo_ids)))\\n    result[\\\"n_total_samples\\\"] = int(len(actions))\\n    result[\\\"n_bootstrap\\\"] = args.n_bootstrap\\n    result[\\\"dry_run\\\"] = args.dry_run\\n\\n    out_dir = os.path.join(args.output_dir, f\\\"{args.arch}_{args.suite}\\\")\\n    os.makedirs(out_dir, exist_ok=True)\\n    out_path = os.path.join(out_dir, f\\\"{args.condition}.json\\\")\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2)\\n    log(f\\\"Saved: {out_path}\\\")\\n\\n    log(f\\\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\\\")\\n    log(f\\\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\\\")\\n    log(f\\\"Delta={result['delta']}  CI95={result['delta_ci_95']}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 303_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full deployed script. Let me write it to the local artifact file. I need to reconstruct the full file from all the pieces I've read. Let me piece it together carefully.

Lines 1-115 from the first head -115 call.
Lines 116-160 from the head -160 call (but that was truncated too).
Then lines 116-215 from head -215 (also truncated).

Actually, let me try a different approach. Let me read the file in two halves.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "5b9730e4-3af3-42ea-9902-3bbf7a9d4abd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWGpCXZWjdoXqVfT9ttU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 46670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2326
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

_source line 304_

Now let me write the full deployed version to the local artifact. I have all the pieces from the multiple reads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "d46bc72e-e15d-4031-8e46-b53fafdd54f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWGpCXZWjdoXqVfT9ttU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 46670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2326
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

_source line 305_

<details open><summary>🔧 Tool call — Read · `toolu_01Y9sYBPJ1MXaZSexx7CTrEY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "df586124-4e9f-409c-a1ac-2510208f519e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWGpCXZWjdoXqVfT9ttU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2326,
      "cache_read_input_tokens": 46670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2326
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

_source line 306 · 2026-05-22T14:43:53.308Z_

<details><summary>↩ Tool result · `toolu_01Y9sYBPJ1MXaZSexx7CTrEY`</summary>

```text
1	#!/usr/bin/env python3
2	"""Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.
3	
4	For each (arch, suite, condition) cell:
5	  1. Load model + processor
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "641c10fe-2220-47e5-b965-e59d97d92b95",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\n\nFor each (arch, suite, condition) cell:\n  1. Load model + processor",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 382
    }
  }
}
```

</details>

---


### Tool call

_source line 307_

<details open><summary>🔧 Tool call — Write · `toolu_01JtjDEceQStXWuTJBuTzPFG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\"\"\"\n\nimport argparse, json, os, sys, time, types\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport numpy as np\nimport h5py\nimport torch\nfrom PIL import Image\nfrom sklearn.linear_model import RidgeCV\nimport importlib.util\n\n\ndef log(msg):\n    print(f\"[{time.strftime('%H:%M:%S')}] {msg}\", flush=True)\n\n\nCKPT = {\n    \"openvla\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n        \"object\":  {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n    },\n    \"tracvla\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n        \"object\":  {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n    },\n    \"nora\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\"},\n    },\n}\n\nARCH_INFO = {\n    \"openvla\": {\"n_layers\": 32, \"hidden\": 4096},\n    \"tracvla\": {\"n_layers\": 32, \"hidden\": 3072},\n    \"nora\":    {\"n_layers\": 36, \"hidden\": 2048},\n}\n\nDATA_ROOT = \"/root/autodl-tmp/vla-ssd/data/libero\"\n\n\ndef _load_openvla_modules(ckpt_path):\n    pkg_name = \"_openvla_pkg\"\n    pkg = types.ModuleType(pkg_name)\n    pkg.__path__ = [ckpt_path]\n    pkg.__package__ = pkg_name\n    sys.modules[pkg_name] = pkg\n\n    for name in [\"configuration_prismatic\", \"modeling_prismatic\", \"processing_prismatic\"]:\n        full = f\"{pkg_name}.{name}\"\n        fpath = os.path.join(ckpt_path, f\"{name}.py\")\n        with open(fpath) as f:\n            src = f.read()\n        # Fix transformers 5.x import changes\n        src = src.replace(\n            \"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\",\n            \"from transformers.utils import PaddingStrategy\\n\"\n            \"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\"\n        )\n        mod = types.ModuleType(full)\n        mod.__file__ = fpath\n        mod.__package__ = pkg_name\n        sys.modules[full] = mod\n        sys.modules[name] = mod\n        setattr(pkg, name, mod)\n\n    for name in [\"configuration_prismatic\", \"modeling_prismatic\", \"processing_prismatic\"]:\n        full = f\"{pkg_name}.{name}\"\n        fpath = os.path.join(ckpt_path, f\"{name}.py\")\n        with open(fpath) as f:\n            src = f.read()\n        src = src.replace(\n            \"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\",\n            \"from transformers.utils import PaddingStrategy\\n\"\n            \"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\"\n        )\n        src = src.replace(\n            \"def tie_weights(self) -> None:\",\n            \"def tie_weights(self, **kwargs) -> None:\"\n        )\n        code = compile(src, fpath, \"exec\")\n        exec(code, sys.modules[full].__dict__)\n\n\ndef load_model(arch, ckpt_path, device):\n    log(f\"Loading {arch} from {ckpt_path}\")\n    t0 = time.time()\n\n    if arch == \"openvla\":\n        _load_openvla_modules(ckpt_path)\n        config_cls = sys.modules[\"configuration_prismatic\"].OpenVLAConfig\n        model_cls = sys.modules[\"modeling_prismatic\"].OpenVLAForActionPrediction\n        proc_cls = sys.modules[\"processing_prismatic\"].PrismaticProcessor\n\n        config = config_cls.from_pretrained(ckpt_path)\n        model = model_cls.from_pretrained(\n            ckpt_path, config=config, dtype=torch.bfloat16\n        ).to(device).eval()\n        # Patch transformers.tokenization_utils for HF cache loading\n        import transformers.tokenization_utils_base as _tub\n        from transformers.utils import PaddingStrategy as _PS\n        _tu = sys.modules[\"transformers.tokenization_utils\"]\n        _tu.PaddingStrategy = _PS\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\n        _tu.TextInput = _tub.TextInput\n        _tu.TruncationStrategy = _tub.TruncationStrategy\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\n\n        ds_path = os.path.join(ckpt_path, \"dataset_statistics.json\")\n        if os.path.exists(ds_path):\n            with open(ds_path) as f:\n                ds_stats = json.load(f)\n            for k, v in ds_stats.items():\n                if k not in model.norm_stats:\n                    model.norm_stats[k] = v\n\n    elif arch == \"tracvla\":\n        from transformers import AutoModelForCausalLM, AutoProcessor\n        model = AutoModelForCausalLM.from_pretrained(\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n\n    elif arch == \"nora\":\n        from transformers import AutoModelForImageTextToText, AutoProcessor\n        model = AutoModelForImageTextToText.from_pretrained(\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef prepare_inputs(arch, processor, instruction, image, device):\n    if arch == \"openvla\":\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n        inputs = processor(prompt, image).to(device)\n        if \"pixel_values\" in inputs:\n            inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n        ids = inputs[\"input_ids\"]\n        if not torch.all(ids[:, -1] == 29871):\n            ids = torch.cat(\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\n            if \"attention_mask\" in inputs:\n                inputs[\"attention_mask\"] = torch.cat(\n                    (inputs[\"attention_mask\"],\n                     torch.ones(1, 1, device=device, dtype=inputs[\"attention_mask\"].dtype)),\n                    dim=1)\n        inputs[\"input_ids\"] = ids\n        return inputs\n\n    elif arch == \"tracvla\":\n        prompt = (\"<|user|>\\n<|image_1|>\\n\"\n                  f\"What action should the robot take to {instruction}?<|end|>\\n\"\n                  \"<|assistant|>\\n\")\n        inputs = processor(prompt, [image], return_tensors=\"pt\").to(device)\n        if \"pixel_values\" in inputs:\n            inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n        return inputs\n\n    elif arch == \"nora\":\n        messages = [{\"role\": \"user\", \"content\": [\n            {\"type\": \"image\", \"image\": image},\n            {\"type\": \"text\", \"text\": instruction},\n        ]}]\n        text = processor.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True)\n        inputs = processor(text=[text], images=[image], return_tensors=\"pt\", padding=True)\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\n                for k, v in inputs.items()}\n\n\ndef discover_tasks(data_dir):\n    tasks = []\n    for f in sorted(os.listdir(data_dir)):\n        if f.endswith(\"_demo.hdf5\"):\n            tasks.append(f.replace(\"_demo.hdf5\", \"\"))\n    instructions = [t.replace(\"_\", \" \") for t in tasks]\n    return tasks, instructions\n\n\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\n                     device, n_demos, n_timesteps):\n    info = ARCH_INFO[arch]\n    n_layers = info[\"n_layers\"]\n    hidden = info[\"hidden\"]\n    total = len(tasks) * n_demos * n_timesteps\n\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\n    actions = np.zeros((total, 7), dtype=np.float32)\n    demo_ids = np.zeros(total, dtype=np.int64)\n\n    idx = 0\n    gd = 0\n\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\n        hdf5_path = os.path.join(data_dir, f\"{task}_demo.hdf5\")\n        log(f\"  Task {ti}/{len(tasks)}: {task}\")\n\n        with h5py.File(hdf5_path, \"r\") as hf:\n            for di in range(n_demos):\n                demo_key = f\"data/demo_{di}\"\n                if demo_key not in hf:\n                    gd += 1\n                    continue\n                n_avail = hf[demo_key][\"actions\"].shape[0]\n\n                for t in range(min(n_timesteps, n_avail)):\n                    img = Image.fromarray(hf[f\"{demo_key}/obs/agentview_rgb\"][t])\n                    act = np.array(hf[f\"{demo_key}/actions\"][t], dtype=np.float32)\n\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\n                    with torch.no_grad():\n                        out = model(**inputs, output_hidden_states=True)\n\n                    for l in range(n_layers):\n                        hs = out.hidden_states[l + 1][0]\n                        features[l][idx] = hs[-1].float().cpu().numpy()\n\n                    actions[idx] = act\n                    demo_ids[idx] = gd\n                    idx += 1\n\n                    del out, inputs\n                    if idx % 50 == 0:\n                        torch.cuda.empty_cache()\n                        log(f\"    {idx}/{total} samples\")\n\n                gd += 1\n\n    log(f\"  Extraction done: {idx} samples, {gd} demos\")\n    features = {l: features[l][:idx] for l in range(n_layers)}\n    return features, actions[:idx], demo_ids[:idx]\n\n\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\n    unique_demos = np.unique(demo_ids)\n    n_total = len(unique_demos)\n    n_train = int(0.8 * n_total)\n    log(f\"  {n_total} demos, split {n_train}/{n_total - n_train}\")\n\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\n\n    rng = np.random.RandomState(seed)\n    canon_perm = rng.permutation(unique_demos)\n    canon_train = set(canon_perm[:n_train].tolist())\n    train_mask = np.array([d in canon_train for d in demo_ids])\n    test_mask = ~train_mask\n\n    y_tr_canon = actions[train_mask]\n    y_te_canon = actions[test_mask]\n\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\n    best_alpha = {}\n    canon_r2 = {}\n\n    log(\"  Canonical split -- fitting RidgeCV per layer...\")\n    for l in range(n_layers):\n        probe = RidgeCV(alphas=alphas_list)\n        probe.fit(features[l][train_mask], y_tr_canon)\n        best_alpha[l] = float(probe.alpha_)\n        pred = probe.predict(features[l][test_mask])\n        ss_res = np.sum((y_te_canon - pred) ** 2)\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\n\n    # Precompute kernel matrices per layer for efficient bootstrap\n    log(\"  Precomputing kernel matrices...\")\n    N = len(actions)\n    kernels = {}\n    for l in range(n_layers):\n        kernels[l] = features[l] @ features[l].T  # (N, N)\n\n    log(f\"  Bootstrap ({n_bootstrap} iterations)...\")\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\n    rng2 = np.random.RandomState(seed + 1)\n    report_every = max(1, n_bootstrap // 10)\n\n    for b in range(n_bootstrap):\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\n        tr_demos = resampled[:n_train]\n        te_demos = resampled[n_train:]\n\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\n\n        if len(te_idx) == 0:\n            continue\n\n        y_tr = actions[tr_idx]\n        y_te = actions[te_idx]\n        y_te_mean = y_te.mean(axis=0)\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\n        if ss_tot < 1e-10:\n            continue\n\n        n_tr = len(tr_idx)\n        for l in range(n_layers):\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\n            try:\n                w = np.linalg.solve(K_tr, y_tr)\n                pred = K_te_tr @ w\n                ss_res = np.sum((y_te - pred) ** 2)\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\n            except np.linalg.LinAlgError:\n                boot_r2[b, l] = 0.0\n\n        if (b + 1) % report_every == 0:\n            log(f\"    {b+1}/{n_bootstrap}\")\n\n    exit_l = n_layers - 1\n    peak_r2_boot = np.max(boot_r2, axis=1)\n    exit_r2_boot = boot_r2[:, exit_l]\n    deltas = peak_r2_boot - exit_r2_boot\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\n\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\n\n    return {\n        \"per_layer_r2\": {f\"L{l}\": round(canon_r2[l], 4) for l in range(n_layers)},\n        \"peak_r2\": round(canon_r2[canon_peak_l], 4),\n        \"peak_layer\": f\"L{canon_peak_l}\",\n        \"exit_r2\": round(canon_r2[exit_l], 4),\n        \"exit_layer\": f\"L{exit_l}\",\n        \"delta\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\n        \"delta_ci_95\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\n        \"bootstrap_deltas_summary\": {\n            \"mean\": round(float(np.mean(deltas)), 4),\n            \"std\": round(float(np.std(deltas)), 4),\n            \"median\": round(float(np.median(deltas)), 4),\n        },\n    }\n\n\ndef main():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--arch\", required=True, choices=[\"openvla\", \"tracvla\", \"nora\"])\n    p.add_argument(\"--suite\", required=True, choices=[\"goal\", \"spatial\", \"object\"])\n    p.add_argument(\"--condition\", required=True, choices=[\"trained\", \"untrained\"])\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--n_bootstrap\", type=int, default=10000)\n    p.add_argument(\"--n_demos\", type=int, default=10)\n    p.add_argument(\"--n_timesteps\", type=int, default=50)\n    p.add_argument(\"--output_dir\",\n                   default=\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\")\n    p.add_argument(\"--dry_run\", action=\"store_true\")\n    args = p.parse_args()\n\n    if args.dry_run:\n        args.n_demos = 2\n        args.n_timesteps = 5\n        args.n_bootstrap = min(args.n_bootstrap, 100)\n\n    if args.suite not in CKPT.get(args.arch, {}):\n        log(f\"ERROR: no checkpoint for {args.arch}/{args.suite}\")\n        sys.exit(1)\n    if args.condition not in CKPT[args.arch][args.suite]:\n        log(f\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\")\n        sys.exit(1)\n\n    device = f\"cuda:{args.gpu}\"\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\n    data_dir = os.path.join(DATA_ROOT, f\"libero_{args.suite}\")\n\n    log(f\"=== {args.arch} / {args.suite} / {args.condition} ===\")\n    log(f\"Checkpoint: {ckpt_path}\")\n    log(f\"Data: {data_dir}\")\n    log(f\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\")\n    if args.dry_run:\n        log(\"DRY RUN\")\n\n    tasks, instructions = discover_tasks(data_dir)\n    if args.dry_run:\n        tasks = tasks[:2]\n        instructions = instructions[:2]\n    log(f\"Tasks: {len(tasks)}\")\n\n    model, processor = load_model(args.arch, ckpt_path, device)\n\n    t0 = time.time()\n    features, actions, demo_ids = extract_features(\n        args.arch, model, processor, tasks, instructions, data_dir,\n        device, args.n_demos, args.n_timesteps)\n    log(f\"Extraction: {time.time()-t0:.1f}s\")\n\n    del model, processor\n    torch.cuda.empty_cache()\n\n    t1 = time.time()\n    n_layers = ARCH_INFO[args.arch][\"n_layers\"]\n    result = clustered_bootstrap_r2(\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\n    log(f\"Bootstrap: {time.time()-t1:.1f}s\")\n\n    result[\"arch\"] = args.arch\n    result[\"suite\"] = args.suite\n    result[\"condition\"] = args.condition\n    result[\"n_demos\"] = int(len(np.unique(demo_ids)))\n    result[\"n_total_samples\"] = int(len(actions))\n    result[\"n_bootstrap\"] = args.n_bootstrap\n    result[\"dry_run\"] = args.dry_run\n\n    out_dir = os.path.join(args.output_dir, f\"{args.arch}_{args.suite}\")\n    os.makedirs(out_dir, exist_ok=True)\n    out_path = os.path.join(out_dir, f\"{args.condition}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    log(f\"Saved: {out_path}\")\n\n    log(f\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\")\n    log(f\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\")\n    log(f\"Delta={result['delta']}  CI95={result['delta_ci_95']}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "67e864bc-9a6c-4989-8ad0-cf9f1bcd210a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLayTgGm2WaUdnAcKEEKus",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 48996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 337
      },
      "output_tokens": 65,
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

_source line 308 · 2026-05-22T14:45:10.351Z_

<details><summary>↩ Tool result · `toolu_01JtjDEceQStXWuTJBuTzPFG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "1171b3cb-3ed4-44c2-b469-f208f97dd478",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/clustered_bootstrap_probe.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\"\"\"\n\nimport argparse, json, os, sys, time, types\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport numpy as np\nimport h5py\nimport torch\nfrom PIL import Image\nfrom sklearn.linear_model import RidgeCV\nimport importlib.util\n\n\ndef log(msg):\n    print(f\"[{time.strftime('%H:%M:%S')}] {msg}\", flush=True)\n\n\nCKPT = {\n    \"openvla\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n        \"object\":  {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n    },\n    \"tracvla\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n        \"object\":  {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n    },\n    \"nora\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\"},\n    },\n}\n\nARCH_INFO = {\n    \"openvla\": {\"n_layers\": 32, \"hidden\": 4096},\n    \"tracvla\": {\"n_layers\": 32, \"hidden\": 3072},\n    \"nora\":    {\"n_layers\": 36, \"hidden\": 2048},\n}\n\nDATA_ROOT = \"/root/autodl-tmp/vla-ssd/data/libero\"\n\n\ndef _load_openvla_modules(ckpt_path):\n    pkg_name = \"_openvla_pkg\"\n    pkg = types.ModuleType(pkg_name)\n    pkg.__path__ = [ckpt_path]\n    pkg.__package__ = pkg_name\n    sys.modules[pkg_name] = pkg\n\n    for name in [\"configuration_prismatic\", \"modeling_prismatic\", \"processing_prismatic\"]:\n        full = f\"{pkg_name}.{name}\"\n        fpath = os.path.join(ckpt_path, f\"{name}.py\")\n        with open(fpath) as f:\n            src = f.read()\n        # Fix transformers 5.x import changes\n        src = src.replace(\n            \"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\",\n            \"from transformers.utils import PaddingStrategy\\n\"\n            \"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\"\n        )\n        mod = types.ModuleType(full)\n        mod.__file__ = fpath\n        mod.__package__ = pkg_name\n        sys.modules[full] = mod\n        sys.modules[name] = mod\n        setattr(pkg, name, mod)\n\n    for name in [\"configuration_prismatic\", \"modeling_prismatic\", \"processing_prismatic\"]:\n        full = f\"{pkg_name}.{name}\"\n        fpath = os.path.join(ckpt_path, f\"{name}.py\")\n        with open(fpath) as f:\n            src = f.read()\n        src = src.replace(\n            \"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\",\n            \"from transformers.utils import PaddingStrategy\\n\"\n            \"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\"\n        )\n        src = src.replace(\n            \"def tie_weights(self) -> None:\",\n            \"def tie_weights(self, **kwargs) -> None:\"\n        )\n        code = compile(src, fpath, \"exec\")\n        exec(code, sys.modules[full].__dict__)\n\n\ndef load_model(arch, ckpt_path, device):\n    log(f\"Loading {arch} from {ckpt_path}\")\n    t0 = time.time()\n\n    if arch == \"openvla\":\n        _load_openvla_modules(ckpt_path)\n        config_cls = sys.modules[\"configuration_prismatic\"].OpenVLAConfig\n        model_cls = sys.modules[\"modeling_prismatic\"].OpenVLAForActionPrediction\n        proc_cls = sys.modules[\"processing_prismatic\"].PrismaticProcessor\n\n        config = config_cls.from_pretrained(ckpt_path)\n        model = model_cls.from_pretrained(\n            ckpt_path, config=config, dtype=torch.bfloat16\n        ).to(device).eval()\n        # Patch transformers.tokenization_utils for HF cache loading\n        import transformers.tokenization_utils_base as _tub\n        from transformers.utils import PaddingStrategy as _PS\n        _tu = sys.modules[\"transformers.tokenization_utils\"]\n        _tu.PaddingStrategy = _PS\n        _tu.PreTokenizedInput = _tub.PreTokenizedInput\n        _tu.TextInput = _tub.TextInput\n        _tu.TruncationStrategy = _tub.TruncationStrategy\n        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)\n\n        ds_path = os.path.join(ckpt_path, \"dataset_statistics.json\")\n        if os.path.exists(ds_path):\n            with open(ds_path) as f:\n                ds_stats = json.load(f)\n            for k, v in ds_stats.items():\n                if k not in model.norm_stats:\n                    model.norm_stats[k] = v\n\n    elif arch == \"tracvla\":\n        from transformers import AutoModelForCausalLM, AutoProcessor\n        model = AutoModelForCausalLM.from_pretrained(\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n\n    elif arch == \"nora\":\n        from transformers import AutoModelForImageTextToText, AutoProcessor\n        model = AutoModelForImageTextToText.from_pretrained(\n            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef prepare_inputs(arch, processor, instruction, image, device):\n    if arch == \"openvla\":\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n        inputs = processor(prompt, image).to(device)\n        if \"pixel_values\" in inputs:\n            inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n        ids = inputs[\"input_ids\"]\n        if not torch.all(ids[:, -1] == 29871):\n            ids = torch.cat(\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\n            if \"attention_mask\" in inputs:\n                inputs[\"attention_mask\"] = torch.cat(\n                    (inputs[\"attention_mask\"],\n                     torch.ones(1, 1, device=device, dtype=inputs[\"attention_mask\"].dtype)),\n                    dim=1)\n        inputs[\"input_ids\"] = ids\n        return inputs\n\n    elif arch == \"tracvla\":\n        prompt = (\"<|user|>\\n<|image_1|>\\n\"\n                  f\"What action should the robot take to {instruction}?<|end|>\\n\"\n                  \"<|assistant|>\\n\")\n        inputs = processor(prompt, [image], return_tensors=\"pt\").to(device)\n        if \"pixel_values\" in inputs:\n            inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n        return inputs\n\n    elif arch == \"nora\":\n        messages = [{\"role\": \"user\", \"content\": [\n            {\"type\": \"image\", \"image\": image},\n            {\"type\": \"text\", \"text\": instruction},\n        ]}]\n        text = processor.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True)\n        inputs = processor(text=[text], images=[image], return_tensors=\"pt\", padding=True)\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\n                for k, v in inputs.items()}\n\n\ndef discover_tasks(data_dir):\n    tasks = []\n    for f in sorted(os.listdir(data_dir)):\n        if f.endswith(\"_demo.hdf5\"):\n            tasks.append(f.replace(\"_demo.hdf5\", \"\"))\n    instructions = [t.replace(\"_\", \" \") for t in tasks]\n    return tasks, instructions\n\n\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\n                     device, n_demos, n_timesteps):\n    info = ARCH_INFO[arch]\n    n_layers = info[\"n_layers\"]\n    hidden = info[\"hidden\"]\n    total = len(tasks) * n_demos * n_timesteps\n\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\n    actions = np.zeros((total, 7), dtype=np.float32)\n    demo_ids = np.zeros(total, dtype=np.int64)\n\n    idx = 0\n    gd = 0\n\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\n        hdf5_path = os.path.join(data_dir, f\"{task}_demo.hdf5\")\n        log(f\"  Task {ti}/{len(tasks)}: {task}\")\n\n        with h5py.File(hdf5_path, \"r\") as hf:\n            for di in range(n_demos):\n                demo_key = f\"data/demo_{di}\"\n                if demo_key not in hf:\n                    gd += 1\n                    continue\n                n_avail = hf[demo_key][\"actions\"].shape[0]\n\n                for t in range(min(n_timesteps, n_avail)):\n                    img = Image.fromarray(hf[f\"{demo_key}/obs/agentview_rgb\"][t])\n                    act = np.array(hf[f\"{demo_key}/actions\"][t], dtype=np.float32)\n\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\n                    with torch.no_grad():\n                        out = model(**inputs, output_hidden_states=True)\n\n                    for l in range(n_layers):\n                        hs = out.hidden_states[l + 1][0]\n                        features[l][idx] = hs[-1].float().cpu().numpy()\n\n                    actions[idx] = act\n                    demo_ids[idx] = gd\n                    idx += 1\n\n                    del out, inputs\n                    if idx % 50 == 0:\n                        torch.cuda.empty_cache()\n                        log(f\"    {idx}/{total} samples\")\n\n                gd += 1\n\n    log(f\"  Extraction done: {idx} samples, {gd} demos\")\n    features = {l: features[l][:idx] for l in range(n_layers)}\n    return features, actions[:idx], demo_ids[:idx]\n\n\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\n    unique_demos = np.unique(demo_ids)\n    n_total = len(unique_demos)\n    n_train = int(0.8 * n_total)\n    log(f\"  {n_total} demos, split {n_train}/{n_total - n_train}\")\n\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\n\n    rng = np.random.RandomState(seed)\n    canon_perm = rng.permutation(unique_demos)\n    canon_train = set(canon_perm[:n_train].tolist())\n    train_mask = np.array([d in canon_train for d in demo_ids])\n    test_mask = ~train_mask\n\n    y_tr_canon = actions[train_mask]\n    y_te_canon = actions[test_mask]\n\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\n    best_alpha = {}\n    canon_r2 = {}\n\n    log(\"  Canonical split -- fitting RidgeCV per layer...\")\n    for l in range(n_layers):\n        probe = RidgeCV(alphas=alphas_list)\n        probe.fit(features[l][train_mask], y_tr_canon)\n        best_alpha[l] = float(probe.alpha_)\n        pred = probe.predict(features[l][test_mask])\n        ss_res = np.sum((y_te_canon - pred) ** 2)\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\n\n    # Precompute kernel matrices per layer for efficient bootstrap\n    log(\"  Precomputing kernel matrices...\")\n    N = len(actions)\n    kernels = {}\n    for l in range(n_layers):\n        kernels[l] = features[l] @ features[l].T  # (N, N)\n\n    log(f\"  Bootstrap ({n_bootstrap} iterations)...\")\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\n    rng2 = np.random.RandomState(seed + 1)\n    report_every = max(1, n_bootstrap // 10)\n\n    for b in range(n_bootstrap):\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\n        tr_demos = resampled[:n_train]\n        te_demos = resampled[n_train:]\n\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\n\n        if len(te_idx) == 0:\n            continue\n\n        y_tr = actions[tr_idx]\n        y_te = actions[te_idx]\n        y_te_mean = y_te.mean(axis=0)\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\n        if ss_tot < 1e-10:\n            continue\n\n        n_tr = len(tr_idx)\n        for l in range(n_layers):\n            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]\n            K_tr[np.diag_indices(n_tr)] += best_alpha[l]\n            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]\n            try:\n                w = np.linalg.solve(K_tr, y_tr)\n                pred = K_te_tr @ w\n                ss_res = np.sum((y_te - pred) ** 2)\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\n            except np.linalg.LinAlgError:\n                boot_r2[b, l] = 0.0\n\n        if (b + 1) % report_every == 0:\n            log(f\"    {b+1}/{n_bootstrap}\")\n\n    exit_l = n_layers - 1\n    peak_r2_boot = np.max(boot_r2, axis=1)\n    exit_r2_boot = boot_r2[:, exit_l]\n    deltas = peak_r2_boot - exit_r2_boot\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\n\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\n\n    return {\n        \"per_layer_r2\": {f\"L{l}\": round(canon_r2[l], 4) for l in range(n_layers)},\n        \"peak_r2\": round(canon_r2[canon_peak_l], 4),\n        \"peak_layer\": f\"L{canon_peak_l}\",\n        \"exit_r2\": round(canon_r2[exit_l], 4),\n        \"exit_layer\": f\"L{exit_l}\",\n        \"delta\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\n        \"delta_ci_95\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\n        \"bootstrap_deltas_summary\": {\n            \"mean\": round(float(np.mean(deltas)), 4),\n            \"std\": round(float(np.std(deltas)), 4),\n            \"median\": round(float(np.median(deltas)), 4),\n        },\n    }\n\n\ndef main():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--arch\", required=True, choices=[\"openvla\", \"tracvla\", \"nora\"])\n    p.add_argument(\"--suite\", required=True, choices=[\"goal\", \"spatial\", \"object\"])\n    p.add_argument(\"--condition\", required=True, choices=[\"trained\", \"untrained\"])\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--n_bootstrap\", type=int, default=10000)\n    p.add_argument(\"--n_demos\", type=int, default=10)\n    p.add_argument(\"--n_timesteps\", type=int, default=50)\n    p.add_argument(\"--output_dir\",\n                   default=\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\")\n    p.add_argument(\"--dry_run\", action=\"store_true\")\n    args = p.parse_args()\n\n    if args.dry_run:\n        args.n_demos = 2\n        args.n_timesteps = 5\n        args.n_bootstrap = min(args.n_bootstrap, 100)\n\n    if args.suite not in CKPT.get(args.arch, {}):\n        log(f\"ERROR: no checkpoint for {args.arch}/{args.suite}\")\n        sys.exit(1)\n    if args.condition not in CKPT[args.arch][args.suite]:\n        log(f\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\")\n        sys.exit(1)\n\n    device = f\"cuda:{args.gpu}\"\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\n    data_dir = os.path.join(DATA_ROOT, f\"libero_{args.suite}\")\n\n    log(f\"=== {args.arch} / {args.suite} / {args.condition} ===\")\n    log(f\"Checkpoint: {ckpt_path}\")\n    log(f\"Data: {data_dir}\")\n    log(f\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\")\n    if args.dry_run:\n        log(\"DRY RUN\")\n\n    tasks, instructions = discover_tasks(data_dir)\n    if args.dry_run:\n        tasks = tasks[:2]\n        instructions = instructions[:2]\n    log(f\"Tasks: {len(tasks)}\")\n\n    model, processor = load_model(args.arch, ckpt_path, device)\n\n    t0 = time.time()\n    features, actions, demo_ids = extract_features(\n        args.arch, model, processor, tasks, instructions, data_dir,\n        device, args.n_demos, args.n_timesteps)\n    log(f\"Extraction: {time.time()-t0:.1f}s\")\n\n    del model, processor\n    torch.cuda.empty_cache()\n\n    t1 = time.time()\n    n_layers = ARCH_INFO[args.arch][\"n_layers\"]\n    result = clustered_bootstrap_r2(\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\n    log(f\"Bootstrap: {time.time()-t1:.1f}s\")\n\n    result[\"arch\"] = args.arch\n    result[\"suite\"] = args.suite\n    result[\"condition\"] = args.condition\n    result[\"n_demos\"] = int(len(np.unique(demo_ids)))\n    result[\"n_total_samples\"] = int(len(actions))\n    result[\"n_bootstrap\"] = args.n_bootstrap\n    result[\"dry_run\"] = args.dry_run\n\n    out_dir = os.path.join(args.output_dir, f\"{args.arch}_{args.suite}\")\n    os.makedirs(out_dir, exist_ok=True)\n    out_path = os.path.join(out_dir, f\"{args.condition}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    log(f\"Saved: {out_path}\")\n\n    log(f\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\")\n    log(f\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\")\n    log(f\"Delta={result['delta']}  CI95={result['delta_ci_95']}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 15,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " #!/usr/bin/env python3",
          "-\"\"\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.",
          "+\"\"\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\"\"\"",
          " ",
          "-For each (arch, suite, condition) cell:",
          "-  1. Load model + processor",
          "-  2. Extract last_preaction hidden states from all layers, tracking demo IDs",
          "-  3. Demo-level RidgeCV to determine best alpha per layer",
          "-  4. Clustered bootstrap (resample demos with replacement) for R2 CI",
          "-  5. Output per-layer R2, delta (peak - exit), and 95% CI",
          "-\"\"\"",
          "-",
          "-import argparse, json, os, sys, time",
          "+import argparse, json, os, sys, time, types",
          " os.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"",
          " ",
          " import numpy as np"
        ]
      },
      {
        "oldStart": 17,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " import torch",
          " from PIL import Image",
          " from sklearn.linear_model import RidgeCV",
          "+import importlib.util",
          " ",
          " ",
          " def log(msg):"
        ]
      },
      {
        "oldStart": 57,
        "oldLines": 22,
        "newStart": 50,
        "newLines": 73,
        "lines": [
          " DATA_ROOT = \"/root/autodl-tmp/vla-ssd/data/libero\"",
          " ",
          " ",
          "+def _load_openvla_modules(ckpt_path):",
          "+    pkg_name = \"_openvla_pkg\"",
          "+    pkg = types.ModuleType(pkg_name)",
          "+    pkg.__path__ = [ckpt_path]",
          "+    pkg.__package__ = pkg_name",
          "+    sys.modules[pkg_name] = pkg",
          "+",
          "+    for name in [\"configuration_prismatic\", \"modeling_prismatic\", \"processing_prismatic\"]:",
          "+        full = f\"{pkg_name}.{name}\"",
          "+        fpath = os.path.join(ckpt_path, f\"{name}.py\")",
          "+        with open(fpath) as f:",
          "+            src = f.read()",
          "+        # Fix transformers 5.x import changes",
          "+        src = src.replace(",
          "+            \"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\",",
          "+            \"from transformers.utils import PaddingStrategy\\n\"",
          "+            \"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\"",
          "+        )",
          "+        mod = types.ModuleType(full)",
          "+        mod.__file__ = fpath",
          "+        mod.__package__ = pkg_name",
          "+        sys.modules[full] = mod",
          "+        sys.modules[name] = mod",
          "+        setattr(pkg, name, mod)",
          "+",
          "+    for name in [\"configuration_prismatic\", \"modeling_prismatic\", \"processing_prismatic\"]:",
          "+        full = f\"{pkg_name}.{name}\"",
          "+        fpath = os.path.join(ckpt_path, f\"{name}.py\")",
          "+        with open(fpath) as f:",
          "+            src = f.read()",
          "+        src = src.replace(",
          "+            \"from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy\",",
          "+            \"from transformers.utils import PaddingStrategy\\n\"",
          "+            \"from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy\"",
          "+        )",
          "+        src = src.replace(",
          "+            \"def tie_weights(self) -> None:\",",
          "+            \"def tie_weights(self, **kwargs) -> None:\"",
          "+        )",
          "+        code = compile(src, fpath, \"exec\")",
          "+        exec(code, sys.modules[full].__dict__)",
          "+",
          "+",
          " def load_model(arch, ckpt_path, device):",
          "     log(f\"Loading {arch} from {ckpt_path}\")",
          "     t0 = time.time()",
          " ",
          "     if arch == \"openvla\":",
          "-        from transformers import AutoModelForVision2Seq",
          "-        import importlib.util",
          "-        model = AutoModelForVision2Seq.from_pretrained(",
          "-            ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True",
          "+        _load_openvla_modules(ckpt_path)",
          "+        config_cls = sys.modules[\"configuration_prismatic\"].OpenVLAConfig",
          "+        model_cls = sys.modules[\"modeling_prismatic\"].OpenVLAForActionPrediction",
          "+        proc_cls = sys.modules[\"processing_prismatic\"].PrismaticProcessor",
          "+",
          "+        config = config_cls.from_pretrained(ckpt_path)",
          "+        model = model_cls.from_pretrained(",
          "+            ckpt_path, config=config, dtype=torch.bfloat16",
          "         ).to(device).eval()",
          "-        proc_path = os.path.join(ckpt_path, \"processing_prismatic.py\")",
          "-        spec = importlib.util.spec_from_file_location(\"processing_prismatic\", proc_path)",
          "-        mod = importlib.util.module_from_spec(spec)",
          "-        sys.modules[\"processing_prismatic\"] = mod",
          "-        spec.loader.exec_module(mod)",
          "-        processor = mod.PrismaticProcessor.from_pretrained(ckpt_path, trust_remote_code=True)",
          "+        # Patch transformers.tokenization_utils for HF cache loading",
          "+        import transformers.tokenization_utils_base as _tub",
          "+        from transformers.utils import PaddingStrategy as _PS",
          "+        _tu = sys.modules[\"transformers.tokenization_utils\"]",
          "+        _tu.PaddingStrategy = _PS",
          "+        _tu.PreTokenizedInput = _tub.PreTokenizedInput",
          "+        _tu.TextInput = _tub.TextInput",
          "+        _tu.TruncationStrategy = _tub.TruncationStrategy",
          "+        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)",
          "+",
          "         ds_path = os.path.join(ckpt_path, \"dataset_statistics.json\")",
          "         if os.path.exists(ds_path):",
          "             with open(ds_path) as f:"
        ]
      },
      {
        "oldStart": 84,
        "oldLines": 14,
        "newStart": 128,
        "newLines": 14,
        "lines": [
          "     elif arch == \"tracvla\":",
          "         from transformers import AutoModelForCausalLM, AutoProcessor",
          "         model = AutoModelForCausalLM.from_pretrained(",
          "-            ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True",
          "+            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True",
          "         ).to(device).eval()",
          "         processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)",
          " ",
          "     elif arch == \"nora\":",
          "         from transformers import AutoModelForImageTextToText, AutoProcessor",
          "         model = AutoModelForImageTextToText.from_pretrained(",
          "-            ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True",
          "+            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True",
          "         ).to(device).eval()",
          "         processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)",
          " "
        ]
      },
      {
        "oldStart": 118,
        "oldLines": 9,
        "newStart": 162,
        "newLines": 9,
        "lines": [
          "         return inputs",
          " ",
          "     elif arch == \"tracvla\":",
          "-        prompt = (f\"<|user|>\\n<|image_1|>\\n\"",
          "+        prompt = (\"<|user|>\\n<|image_1|>\\n\"",
          "                   f\"What action should the robot take to {instruction}?<|end|>\\n\"",
          "-                  f\"<|assistant|>\\n\")",
          "+                  \"<|assistant|>\\n\")",
          "         inputs = processor(prompt, [image], return_tensors=\"pt\").to(device)",
          "         if \"pixel_values\" in inputs:",
          "             inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)"
        ]
      },
      {
        "oldStart": 222,
        "oldLines": 7,
        "newStart": 266,
        "newLines": 7,
        "lines": [
          "     best_alpha = {}",
          "     canon_r2 = {}",
          " ",
          "-    log(\"  Canonical split — fitting RidgeCV per layer...\")",
          "+    log(\"  Canonical split -- fitting RidgeCV per layer...\")",
          "     for l in range(n_layers):",
          "         probe = RidgeCV(alphas=alphas_list)",
          "         probe.fit(features[l][train_mask], y_tr_canon)"
        ]
      },
      {
        "oldStart": 232,
        "oldLines": 6,
        "newStart": 276,
        "newLines": 13,
        "lines": [
          "         ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)",
          "         canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0",
          " ",
          "+    # Precompute kernel matrices per layer for efficient bootstrap",
          "+    log(\"  Precomputing kernel matrices...\")",
          "+    N = len(actions)",
          "+    kernels = {}",
          "+    for l in range(n_layers):",
          "+        kernels[l] = features[l] @ features[l].T  # (N, N)",
          "+",
          "     log(f\"  Bootstrap ({n_bootstrap} iterations)...\")",
          "     boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)",
          "     rng2 = np.random.RandomState(seed + 1)"
        ]
      },
      {
        "oldStart": 255,
        "oldLines": 16,
        "newStart": 306,
        "newLines": 14,
        "lines": [
          "         if ss_tot < 1e-10:",
          "             continue",
          " ",
          "+        n_tr = len(tr_idx)",
          "         for l in range(n_layers):",
          "-            X_tr = features[l][tr_idx]",
          "-            X_te = features[l][te_idx]",
          "-            D = X_tr.shape[1]",
          "-            XtX = X_tr.T @ X_tr",
          "-            XtX[np.diag_indices(D)] += best_alpha[l]",
          "-            Xty = X_tr.T @ y_tr",
          "+            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]",
          "+            K_tr[np.diag_indices(n_tr)] += best_alpha[l]",
          "+            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]",
          "             try:",
          "-                beta = np.linalg.solve(XtX, Xty)",
          "-                pred = X_te @ beta",
          "+                w = np.linalg.solve(K_tr, y_tr)",
          "+                pred = K_te_tr @ w",
          "                 ss_res = np.sum((y_te - pred) ** 2)",
          "                 boot_r2[b, l] = 1.0 - ss_res / ss_tot",
          "             except np.linalg.LinAlgError:"
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting.\n\nFor each (arch, suite, condition) cell:\n  1. Load model + processor\n  2. Extract last_preaction hidden states from all layers, tracking demo IDs\n  3. Demo-level RidgeCV to determine best alpha per layer\n  4. Clustered bootstrap (resample demos with replacement) for R2 CI\n  5. Output per-layer R2, delta (peak - exit), and 95% CI\n\"\"\"\n\nimport argparse, json, os, sys, time\nos.environ[\"HDF5_USE_FILE_LOCKING\"] = \"FALSE\"\n\nimport numpy as np\nimport h5py\nimport torch\nfrom PIL import Image\nfrom sklearn.linear_model import RidgeCV\n\n\ndef log(msg):\n    print(f\"[{time.strftime('%H:%M:%S')}] {msg}\", flush=True)\n\n\nCKPT = {\n    \"openvla\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n        \"object\":  {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\"},\n    },\n    \"tracvla\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n        \"object\":  {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base\"},\n    },\n    \"nora\": {\n        \"goal\":    {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-goal\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\"},\n        \"spatial\": {\"trained\": \"/root/autodl-tmp/vla-ssd/checkpoints/nora-libero-spatial\",\n                    \"untrained\": \"/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base\"},\n    },\n}\n\nARCH_INFO = {\n    \"openvla\": {\"n_layers\": 32, \"hidden\": 4096},\n    \"tracvla\": {\"n_layers\": 32, \"hidden\": 3072},\n    \"nora\":    {\"n_layers\": 36, \"hidden\": 2048},\n}\n\nDATA_ROOT = \"/root/autodl-tmp/vla-ssd/data/libero\"\n\n\ndef load_model(arch, ckpt_path, device):\n    log(f\"Loading {arch} from {ckpt_path}\")\n    t0 = time.time()\n\n    if arch == \"openvla\":\n        from transformers import AutoModelForVision2Seq\n        import importlib.util\n        model = AutoModelForVision2Seq.from_pretrained(\n            ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        proc_path = os.path.join(ckpt_path, \"processing_prismatic.py\")\n        spec = importlib.util.spec_from_file_location(\"processing_prismatic\", proc_path)\n        mod = importlib.util.module_from_spec(spec)\n        sys.modules[\"processing_prismatic\"] = mod\n        spec.loader.exec_module(mod)\n        processor = mod.PrismaticProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n        ds_path = os.path.join(ckpt_path, \"dataset_statistics.json\")\n        if os.path.exists(ds_path):\n            with open(ds_path) as f:\n                ds_stats = json.load(f)\n            for k, v in ds_stats.items():\n                if k not in model.norm_stats:\n                    model.norm_stats[k] = v\n\n    elif arch == \"tracvla\":\n        from transformers import AutoModelForCausalLM, AutoProcessor\n        model = AutoModelForCausalLM.from_pretrained(\n            ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n\n    elif arch == \"nora\":\n        from transformers import AutoModelForImageTextToText, AutoProcessor\n        model = AutoModelForImageTextToText.from_pretrained(\n            ckpt_path, torch_dtype=torch.bfloat16, trust_remote_code=True\n        ).to(device).eval()\n        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)\n\n    log(f\"  Loaded in {time.time()-t0:.1f}s\")\n    return model, processor\n\n\ndef prepare_inputs(arch, processor, instruction, image, device):\n    if arch == \"openvla\":\n        prompt = f\"In: What action should the robot take to {instruction}?\\nOut:\"\n        inputs = processor(prompt, image).to(device)\n        if \"pixel_values\" in inputs:\n            inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n        ids = inputs[\"input_ids\"]\n        if not torch.all(ids[:, -1] == 29871):\n            ids = torch.cat(\n                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)\n            if \"attention_mask\" in inputs:\n                inputs[\"attention_mask\"] = torch.cat(\n                    (inputs[\"attention_mask\"],\n                     torch.ones(1, 1, device=device, dtype=inputs[\"attention_mask\"].dtype)),\n                    dim=1)\n        inputs[\"input_ids\"] = ids\n        return inputs\n\n    elif arch == \"tracvla\":\n        prompt = (f\"<|user|>\\n<|image_1|>\\n\"\n                  f\"What action should the robot take to {instruction}?<|end|>\\n\"\n                  f\"<|assistant|>\\n\")\n        inputs = processor(prompt, [image], return_tensors=\"pt\").to(device)\n        if \"pixel_values\" in inputs:\n            inputs[\"pixel_values\"] = inputs[\"pixel_values\"].to(torch.bfloat16)\n        return inputs\n\n    elif arch == \"nora\":\n        messages = [{\"role\": \"user\", \"content\": [\n            {\"type\": \"image\", \"image\": image},\n            {\"type\": \"text\", \"text\": instruction},\n        ]}]\n        text = processor.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True)\n        inputs = processor(text=[text], images=[image], return_tensors=\"pt\", padding=True)\n        return {k: v.to(device) if isinstance(v, torch.Tensor) else v\n                for k, v in inputs.items()}\n\n\ndef discover_tasks(data_dir):\n    tasks = []\n    for f in sorted(os.listdir(data_dir)):\n        if f.endswith(\"_demo.hdf5\"):\n            tasks.append(f.replace(\"_demo.hdf5\", \"\"))\n    instructions = [t.replace(\"_\", \" \") for t in tasks]\n    return tasks, instructions\n\n\ndef extract_features(arch, model, processor, tasks, instructions, data_dir,\n                     device, n_demos, n_timesteps):\n    info = ARCH_INFO[arch]\n    n_layers = info[\"n_layers\"]\n    hidden = info[\"hidden\"]\n    total = len(tasks) * n_demos * n_timesteps\n\n    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}\n    actions = np.zeros((total, 7), dtype=np.float32)\n    demo_ids = np.zeros(total, dtype=np.int64)\n\n    idx = 0\n    gd = 0\n\n    for ti, (task, instr) in enumerate(zip(tasks, instructions)):\n        hdf5_path = os.path.join(data_dir, f\"{task}_demo.hdf5\")\n        log(f\"  Task {ti}/{len(tasks)}: {task}\")\n\n        with h5py.File(hdf5_path, \"r\") as hf:\n            for di in range(n_demos):\n                demo_key = f\"data/demo_{di}\"\n                if demo_key not in hf:\n                    gd += 1\n                    continue\n                n_avail = hf[demo_key][\"actions\"].shape[0]\n\n                for t in range(min(n_timesteps, n_avail)):\n                    img = Image.fromarray(hf[f\"{demo_key}/obs/agentview_rgb\"][t])\n                    act = np.array(hf[f\"{demo_key}/actions\"][t], dtype=np.float32)\n\n                    inputs = prepare_inputs(arch, processor, instr, img, device)\n                    with torch.no_grad():\n                        out = model(**inputs, output_hidden_states=True)\n\n                    for l in range(n_layers):\n                        hs = out.hidden_states[l + 1][0]\n                        features[l][idx] = hs[-1].float().cpu().numpy()\n\n                    actions[idx] = act\n                    demo_ids[idx] = gd\n                    idx += 1\n\n                    del out, inputs\n                    if idx % 50 == 0:\n                        torch.cuda.empty_cache()\n                        log(f\"    {idx}/{total} samples\")\n\n                gd += 1\n\n    log(f\"  Extraction done: {idx} samples, {gd} demos\")\n    features = {l: features[l][:idx] for l in range(n_layers)}\n    return features, actions[:idx], demo_ids[:idx]\n\n\ndef clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):\n    unique_demos = np.unique(demo_ids)\n    n_total = len(unique_demos)\n    n_train = int(0.8 * n_total)\n    log(f\"  {n_total} demos, split {n_train}/{n_total - n_train}\")\n\n    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}\n\n    rng = np.random.RandomState(seed)\n    canon_perm = rng.permutation(unique_demos)\n    canon_train = set(canon_perm[:n_train].tolist())\n    train_mask = np.array([d in canon_train for d in demo_ids])\n    test_mask = ~train_mask\n\n    y_tr_canon = actions[train_mask]\n    y_te_canon = actions[test_mask]\n\n    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]\n    best_alpha = {}\n    canon_r2 = {}\n\n    log(\"  Canonical split — fitting RidgeCV per layer...\")\n    for l in range(n_layers):\n        probe = RidgeCV(alphas=alphas_list)\n        probe.fit(features[l][train_mask], y_tr_canon)\n        best_alpha[l] = float(probe.alpha_)\n        pred = probe.predict(features[l][test_mask])\n        ss_res = np.sum((y_te_canon - pred) ** 2)\n        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)\n        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0\n\n    log(f\"  Bootstrap ({n_bootstrap} iterations)...\")\n    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)\n    rng2 = np.random.RandomState(seed + 1)\n    report_every = max(1, n_bootstrap // 10)\n\n    for b in range(n_bootstrap):\n        resampled = rng2.choice(unique_demos, size=n_total, replace=True)\n        tr_demos = resampled[:n_train]\n        te_demos = resampled[n_train:]\n\n        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])\n        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])\n\n        if len(te_idx) == 0:\n            continue\n\n        y_tr = actions[tr_idx]\n        y_te = actions[te_idx]\n        y_te_mean = y_te.mean(axis=0)\n        ss_tot = np.sum((y_te - y_te_mean) ** 2)\n        if ss_tot < 1e-10:\n            continue\n\n        for l in range(n_layers):\n            X_tr = features[l][tr_idx]\n            X_te = features[l][te_idx]\n            D = X_tr.shape[1]\n            XtX = X_tr.T @ X_tr\n            XtX[np.diag_indices(D)] += best_alpha[l]\n            Xty = X_tr.T @ y_tr\n            try:\n                beta = np.linalg.solve(XtX, Xty)\n                pred = X_te @ beta\n                ss_res = np.sum((y_te - pred) ** 2)\n                boot_r2[b, l] = 1.0 - ss_res / ss_tot\n            except np.linalg.LinAlgError:\n                boot_r2[b, l] = 0.0\n\n        if (b + 1) % report_every == 0:\n            log(f\"    {b+1}/{n_bootstrap}\")\n\n    exit_l = n_layers - 1\n    peak_r2_boot = np.max(boot_r2, axis=1)\n    exit_r2_boot = boot_r2[:, exit_l]\n    deltas = peak_r2_boot - exit_r2_boot\n    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])\n\n    canon_peak_l = max(canon_r2, key=canon_r2.get)\n\n    return {\n        \"per_layer_r2\": {f\"L{l}\": round(canon_r2[l], 4) for l in range(n_layers)},\n        \"peak_r2\": round(canon_r2[canon_peak_l], 4),\n        \"peak_layer\": f\"L{canon_peak_l}\",\n        \"exit_r2\": round(canon_r2[exit_l], 4),\n        \"exit_layer\": f\"L{exit_l}\",\n        \"delta\": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),\n        \"delta_ci_95\": [round(float(ci_lo), 4), round(float(ci_hi), 4)],\n        \"bootstrap_deltas_summary\": {\n            \"mean\": round(float(np.mean(deltas)), 4),\n            \"std\": round(float(np.std(deltas)), 4),\n            \"median\": round(float(np.median(deltas)), 4),\n        },\n    }\n\n\ndef main():\n    p = argparse.ArgumentParser()\n    p.add_argument(\"--arch\", required=True, choices=[\"openvla\", \"tracvla\", \"nora\"])\n    p.add_argument(\"--suite\", required=True, choices=[\"goal\", \"spatial\", \"object\"])\n    p.add_argument(\"--condition\", required=True, choices=[\"trained\", \"untrained\"])\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--n_bootstrap\", type=int, default=10000)\n    p.add_argument(\"--n_demos\", type=int, default=10)\n    p.add_argument(\"--n_timesteps\", type=int, default=50)\n    p.add_argument(\"--output_dir\",\n                   default=\"/root/autodl-tmp/vla-ssd/results/clustered_bootstrap/\")\n    p.add_argument(\"--dry_run\", action=\"store_true\")\n    args = p.parse_args()\n\n    if args.dry_run:\n        args.n_demos = 2\n        args.n_timesteps = 5\n        args.n_bootstrap = min(args.n_bootstrap, 100)\n\n    if args.suite not in CKPT.get(args.arch, {}):\n        log(f\"ERROR: no checkpoint for {args.arch}/{args.suite}\")\n        sys.exit(1)\n    if args.condition not in CKPT[args.arch][args.suite]:\n        log(f\"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}\")\n        sys.exit(1)\n\n    device = f\"cuda:{args.gpu}\"\n    ckpt_path = CKPT[args.arch][args.suite][args.condition]\n    data_dir = os.path.join(DATA_ROOT, f\"libero_{args.suite}\")\n\n    log(f\"=== {args.arch} / {args.suite} / {args.condition} ===\")\n    log(f\"Checkpoint: {ckpt_path}\")\n    log(f\"Data: {data_dir}\")\n    log(f\"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}\")\n    if args.dry_run:\n        log(\"DRY RUN\")\n\n    tasks, instructions = discover_tasks(data_dir)\n    if args.dry_run:\n        tasks = tasks[:2]\n        instructions = instructions[:2]\n    log(f\"Tasks: {len(tasks)}\")\n\n    model, processor = load_model(args.arch, ckpt_path, device)\n\n    t0 = time.time()\n    features, actions, demo_ids = extract_features(\n        args.arch, model, processor, tasks, instructions, data_dir,\n        device, args.n_demos, args.n_timesteps)\n    log(f\"Extraction: {time.time()-t0:.1f}s\")\n\n    del model, processor\n    torch.cuda.empty_cache()\n\n    t1 = time.time()\n    n_layers = ARCH_INFO[args.arch][\"n_layers\"]\n    result = clustered_bootstrap_r2(\n        features, actions, demo_ids, n_layers, args.n_bootstrap)\n    log(f\"Bootstrap: {time.time()-t1:.1f}s\")\n\n    result[\"arch\"] = args.arch\n    result[\"suite\"] = args.suite\n    result[\"condition\"] = args.condition\n    result[\"n_demos\"] = int(len(np.unique(demo_ids)))\n    result[\"n_total_samples\"] = int(len(actions))\n    result[\"n_bootstrap\"] = args.n_bootstrap\n    result[\"dry_run\"] = args.dry_run\n\n    out_dir = os.path.join(args.output_dir, f\"{args.arch}_{args.suite}\")\n    os.makedirs(out_dir, exist_ok=True)\n    out_path = os.path.join(out_dir, f\"{args.condition}.json\")\n    with open(out_path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    log(f\"Saved: {out_path}\")\n\n    log(f\"Peak R2={result['peak_r2']} @ {result['peak_layer']}\")\n    log(f\"Exit R2={result['exit_r2']} @ {result['exit_layer']}\")\n    log(f\"Delta={result['delta']}  CI95={result['delta_ci_95']}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 309_

Now let me register the updated artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "b1c233b8-a35a-49a8-a93f-119a203ef44b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoCw6zCywbhft4ENdgSBPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 49333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6076
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


### Tool call

_source line 310_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012Yf7jeCzJVq3rnBqDUx87b`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "b7a9c580-7cb4-41ed-8a0c-41dd7e4fd729",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoCw6zCywbhft4ENdgSBPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6076,
      "cache_read_input_tokens": 49333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6076
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


### Tool result

_source line 311 · 2026-05-22T14:45:15.800Z_

<details><summary>↩ Tool result · `toolu_012Yf7jeCzJVq3rnBqDUx87b`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "851e2f68-18df-401d-964d-80152b7fe5bf",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Tool call

_source line 312_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GT3Z6Fy5feQ5zCpqmRbQbn`</summary>

```json
{
  "query": "register artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "ebe0f1a5-2229-40e3-86c0-c1f34442fb83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Buqm7m6FqyhiuZAf73g9RV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 112,
      "cache_read_input_tokens": 55409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 112
      },
      "output_tokens": 57,
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

_source line 313 · 2026-05-22T14:45:22.084Z_

<details><summary>↩ Tool result · `toolu_01GT3Z6Fy5feQ5zCpqmRbQbn`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "d18f4fb8-c148-4156-b747-1f4cd501d81c",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Assistant

_source line 314_

Dry-run 结果汇报：

**`clustered_bootstrap_probe.py` — openvla / goal / trained (dry-run)**

| 参数 | 值 |
|------|-----|
| 样本数 | 20 (4 demos × 5 timesteps, 2 tasks) |
| Bootstrap | 100 iterations |
| 模式 | dry_run=true |

**核心指标：**

| 指标 | 值 |
|------|-----|
| Peak R² | **-0.7551** @ L28 |
| Exit R² | **-0.9913** @ L31 |
| Delta (peak - exit) | **0.2362** |
| 95% CI | [0.0, 1.4872] |
| Bootstrap delta mean/std | 0.1911 / 0.4205 |

**Per-layer R² 趋势：** 从 L0 (-2.36) 到 L6 (-0.95) 逐层改善，L7-L15 略有回落，L16 起再次改善，L28 达到 peak (-0.76)，随后 L29-L31 回落至 exit。

**解读：**
- 所有 R² 均为负值，这在 dry-run 的极小样本下（4 demos, 3/1 train/test split）是预期行为——Ridge probe 在如此少的数据上无法学到有意义的映射
- 关键验证点已全部通过：模型加载（含 transformers 5.x 兼容性修复）→ hidden state 提取 → demo-level 聚类分割 → 预计算 kernel 矩阵 → dual-form bootstrap → JSON 输出
- 正式运行（10 demos × 50 timesteps × 10 tasks = 5000 samples, 10000 bootstrap）预期 R² 将为正值

**脚本状态：** 已部署到 `westd-19183:/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py`，本地 artifact 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "uuid": "2a78df16-eb57-4feb-be14-317c36b6c87c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bH439fKVc3vZzkMPNQUSr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 55521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
      },
      "output_tokens": 2,
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

_source line 315_

Dry-run 结果汇报：

**`clustered_bootstrap_probe.py` — openvla / goal / trained (dry-run)**

| 参数 | 值 |
|------|-----|
| 样本数 | 20 (4 demos × 5 timesteps, 2 tasks) |
| Bootstrap | 100 iterations |
| 模式 | dry_run=true |

**核心指标：**

| 指标 | 值 |
|------|-----|
| Peak R² | **-0.7551** @ L28 |
| Exit R² | **-0.9913** @ L31 |
| Delta (peak - exit) | **0.2362** |
| 95% CI | [0.0, 1.4872] |
| Bootstrap delta mean/std | 0.1911 / 0.4205 |

**Per-layer R² 趋势：** 从 L0 (-2.36) 到 L6 (-0.95) 逐层改善，L7-L15 略有回落，L16 起再次改善，L28 达到 peak (-0.76)，随后 L29-L31 回落至 exit。

**解读：**
- 所有 R² 均为负值，这在 dry-run 的极小样本下（4 demos, 3/1 train/test split）是预期行为——Ridge probe 在如此少的数据上无法学到有意义的映射
- 关键验证点已全部通过：模型加载（含 transformers 5.x 兼容性修复）→ hidden state 提取 → demo-level 聚类分割 → 预计算 kernel 矩阵 → dual-form bootstrap → JSON 输出
- 正式运行（10 demos × 50 timesteps × 10 tasks = 5000 samples, 10000 bootstrap）预期 R² 将为正值

**脚本状态：** 已部署到 `westd-19183:/root/autodl-tmp/vla-ssd/scripts/clustered_bootstrap_probe.py`，本地 artifact 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 2160072,
  "duration_api_ms": 1923305,
  "num_turns": 112,
  "stop_reason": "end_turn",
  "session_id": "7ae68de3-16ab-4110-8f59-0311deda7143",
  "total_cost_usd": 8.093741750000003,
  "usage": {
    "input_tokens": 93,
    "cache_creation_input_tokens": 198986,
    "cache_read_input_tokens": 8632728,
    "output_tokens": 93713,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 198986,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 569,
        "cache_read_input_tokens": 55521,
        "cache_creation_input_tokens": 194,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 194
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2995,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0030849999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1687,
      "outputTokens": 97521,
      "cacheReadInputTokens": 8799681,
      "cacheCreationInputTokens": 199097,
      "webSearchRequests": 0,
      "costUSD": 8.090656750000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ee45331e-1135-49b0-bd77-4a7a9241ea48"
}
```

</details>

---
