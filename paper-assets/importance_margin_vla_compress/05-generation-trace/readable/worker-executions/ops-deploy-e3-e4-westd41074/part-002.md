# ops deploy e3 e4 westd41074 — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ops-deploy-e3-e4-westd41074.md) · [Structured JSON](../../../sessions/c2/c266f1ef800c882fbcb4.json)

## Before a recorded user message

### Tool result

_source line 303 · 2026-05-23T07:26:30.949Z_

<details><summary>↩ Tool result · `toolu_01Gjos519EoxJsz2YkUZaW7c`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 15:21:21 [INFO] Pi0.5 k=1.00: 67.02±1.15 ms, 768→768 tok, 9500 MB\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n   PID STAT     ELAPSED\\n495949 S          12:57\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "ddc96f1e-f0ca-4329-9ce5-ea08615f085d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-23 15:21:21 [INFO] Pi0.5 k=1.00: 67.02±1.15 ms, 768→768 tok, 9500 MB\\\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\\\n   PID STAT     ELAPSED\\\\n495949 S          12:57\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 25.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-23 15:21:21 [INFO] Pi0.5 k=1.00: 67.02±1.15 ms, 768→768 tok, 9500 MB\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n   PID STAT     ELAPSED\\n495949 S          12:57\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 304_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JhT72AwutzuhExhEYeLJT4`</summary>

```json
{
  "server": "westd-41074",
  "command": "sleep 25 && grep \"INFO.*Pi0.5 k=\\|saved\\|Results\\|CSV\\|JSON\" /root/autodl-tmp/importance_margin_vla_compress/logs/e4_inference_latency_smolvla_pi05.log && ps -p 495949 -o pid,stat,etime 2>&1",
  "account": "root",
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
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "9f5f8cad-ed6b-49f4-87fa-87c81dd15ae9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDrpxRjNy1h6P3ZbQFixFf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 127711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 875
      },
      "output_tokens": 69,
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

_source line 305 · 2026-05-23T07:26:59.712Z_

<details><summary>↩ Tool result · `toolu_01JhT72AwutzuhExhEYeLJT4`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"2026-05-23 15:21:21 [INFO] Pi0.5 k=1.00: 67.02±1.15 ms, 768→768 tok, 9500 MB\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n2026-05-23 15:26:31 [INFO] Pi0.5 k=0.50: 64.31±0.79 ms, 768→384 tok, 9499 MB\\n   PID STAT     ELAPSED\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 25.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "1f36a6a6-d15f-4d96-bb6d-3837f30676e0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-23 15:21:21 [INFO] Pi0.5 k=1.00: 67.02±1.15 ms, 768→768 tok, 9500 MB\\\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\\\n2026-05-23 15:26:31 [INFO] Pi0.5 k=0.50: 64.31±0.79 ms, 768→384 tok, 9499 MB\\\\n   PID STAT     ELAPSED\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 25.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"2026-05-23 15:21:21 [INFO] Pi0.5 k=1.00: 67.02±1.15 ms, 768→768 tok, 9500 MB\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n2026-05-23 15:26:31 [INFO] Pi0.5 k=0.50: 64.31±0.79 ms, 768→384 tok, 9499 MB\\n   PID STAT     ELAPSED\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 25.45}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 306_

<details><summary>Logged reasoning block</summary>

```text
E4 seems to have finished! π0.5 k=0.50 is done: 64.31±0.79 ms, 384 tokens, 9499 MB.

PID 495949 is no longer running (ps returned exit code 1 - process not found). Let me check the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "53bb8e51-ef8e-4a97-89e5-09506ff36aed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZW1KtDp1cY4gRqkM3fB9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 128586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 548
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

_source line 307_

E4 完成。查看最终产出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "eadada59-6d3d-4b33-88a9-120ae9d44b1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZW1KtDp1cY4gRqkM3fB9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 128586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 548
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

_source line 308_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Y8DErhzyzA6n2nkVpAj2pk`</summary>

```json
{
  "server": "westd-41074",
  "command": "tail -30 /root/autodl-tmp/importance_margin_vla_compress/logs/e4_inference_latency_smolvla_pi05.log",
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
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "4c28c807-ad5a-47a7-96c3-f32f17c2a7e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZW1KtDp1cY4gRqkM3fB9G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 128586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 548
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

_source line 309 · 2026-05-23T07:27:06.147Z_

<details><summary>↩ Tool result · `toolu_01Y8DErhzyzA6n2nkVpAj2pk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  triton_bmm_12194 0.0184 ms 74.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4\\n  triton_bmm_12198 0.0200 ms 68.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4\\n  triton_bmm_12197 0.0225 ms 61.3% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8\\n  triton_bmm_12206 0.0261 ms 52.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\n  triton_bmm_12201 0.0266 ms 51.7% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4\\n  triton_bmm_12192 0.0284 ms 48.4% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=32, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\n  triton_bmm_12193 0.0285 ms 48.3% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\n  triton_bmm_12196 0.0301 ms 45.6% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4\\n  triton_bmm_12204 0.0302 ms 45.6% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8\\nSingleProcess AUTOTUNE benchmarking takes 0.4141 seconds and 0.0002 seconds precompiling for 18 choices\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n2026-05-23 15:26:31 [INFO] Pi0.5 k=0.50: 64.31±0.79 ms, 768→384 tok, 9499 MB\\n2026-05-23 15:26:32 [INFO] Saved: eval_results/inference_latency_all_models.csv, eval_results/inference_latency_all_models.json\\n2026-05-23 15:26:32 [INFO] \\n==========================================================================================\\n2026-05-23 15:26:32 [INFO] Model           k    tokens  mean±std(ms)     p95(ms)     mem(MB)\\n2026-05-23 15:26:32 [INFO] ------------------------------------------------------------------------------------------\\n2026-05-23 15:26:32 [INFO] smolvla      1.00  128->128   164.77+-5.85     168.86      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.95  128->120   162.25+-2.46     165.58      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.90  128->114   164.46+-3.11     169.61      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.70  128->88    163.01+-2.19     166.00      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.50  128->64    162.98+-1.78     165.52      1264\\n2026-05-23 15:26:32 [INFO] pi05         1.00  768->768    67.02+-1.15      68.69      9500\\n2026-05-23 15:26:32 [INFO] pi05         0.95  768->729    71.95+-0.73      73.09      9636\\n2026-05-23 15:26:32 [INFO] pi05         0.90  768->690    71.55+-0.75      72.81      9501\\n2026-05-23 15:26:32 [INFO] pi05         0.70  768->537    68.59+-2.28      72.00      9500\\n2026-05-23 15:26:32 [INFO] pi05         0.50  768->384    64.31+-0.79      65.69      9499\\n2026-05-23 15:26:32 [INFO] ==========================================================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "8c03333a-6f9a-4fd6-8278-cc188327babf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  triton_bmm_12194 0.0184 ms 74.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4\\\\n  triton_bmm_12198 0.0200 ms 68.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4\\\\n  triton_bmm_12197 0.0225 ms 61.3% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8\\\\n  triton_bmm_12206 0.0261 ms 52.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\\\n  triton_bmm_12201 0.0266 ms 51.7% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4\\\\n  triton_bmm_12192 0.0284 ms 48.4% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=32, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\\\n  triton_bmm_12193 0.0285 ms 48.3% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\\\n  triton_bmm_12196 0.0301 ms 45.6% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4\\\\n  triton_bmm_12204 0.0302 ms 45.6% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8\\\\nSingleProcess AUTOTUNE benchmarking takes 0.4141 seconds and 0.0002 seconds precompiling for 18 choices\\\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\\\n2026-05-23 15:26:31 [INFO] Pi0.5 k=0.50: 64.31±0.79 ms, 768→384 tok, 9499 MB\\\\n2026-05-23 15:26:32 [INFO] Saved: eval_results/inference_latency_all_models.csv, eval_results/inference_latency_all_models.json\\\\n2026-05-23 15:26:32 [INFO] \\\\n==========================================================================================\\\\n2026-05-23 15:26:32 [INFO] Model           k    tokens  mean±std(ms)     p95(ms)     mem(MB)\\\\n2026-05-23 15:26:32 [INFO] ------------------------------------------------------------------------------------------\\\\n2026-05-23 15:26:32 [INFO] smolvla      1.00  128->128   164.77+-5.85     168.86      1264\\\\n2026-05-23 15:26:32 [INFO] smolvla      0.95  128->120   162.25+-2.46     165.58      1264\\\\n2026-05-23 15:26:32 [INFO] smolvla      0.90  128->114   164.46+-3.11     169.61      1264\\\\n2026-05-23 15:26:32 [INFO] smolvla      0.70  128->88    163.01+-2.19     166.00      1264\\\\n2026-05-23 15:26:32 [INFO] smolvla      0.50  128->64    162.98+-1.78     165.52      1264\\\\n2026-05-23 15:26:32 [INFO] pi05         1.00  768->768    67.02+-1.15      68.69      9500\\\\n2026-05-23 15:26:32 [INFO] pi05         0.95  768->729    71.95+-0.73      73.09      9636\\\\n2026-05-23 15:26:32 [INFO] pi05         0.90  768->690    71.55+-0.75      72.81      9501\\\\n2026-05-23 15:26:32 [INFO] pi05         0.70  768->537    68.59+-2.28      72.00      9500\\\\n2026-05-23 15:26:32 [INFO] pi05         0.50  768->384    64.31+-0.79      65.69      9499\\\\n2026-05-23 15:26:32 [INFO] ==========================================================================================\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  triton_bmm_12194 0.0184 ms 74.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=128, BLOCK_M=64, BLOCK_N=32, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4\\n  triton_bmm_12198 0.0200 ms 68.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=128, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=4\\n  triton_bmm_12197 0.0225 ms 61.3% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=8\\n  triton_bmm_12206 0.0261 ms 52.8% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\n  triton_bmm_12201 0.0266 ms 51.7% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=64, BLOCK_M=64, BLOCK_N=128, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=3, num_warps=4\\n  triton_bmm_12192 0.0284 ms 48.4% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=32, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\n  triton_bmm_12193 0.0285 ms 48.3% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=32, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=5, num_warps=8\\n  triton_bmm_12196 0.0301 ms 45.6% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=2, num_warps=4\\n  triton_bmm_12204 0.0302 ms 45.6% ACC_TYPE='tl.float32', ALLOW_TF32=True, BLOCK_K=32, BLOCK_M=64, BLOCK_N=64, EVEN_K=False, GROUP_M=8, USE_FAST_ACCUM=False, num_stages=4, num_warps=8\\nSingleProcess AUTOTUNE benchmarking takes 0.4141 seconds and 0.0002 seconds precompiling for 18 choices\\n2026-05-23 15:24:07 [INFO] Pi0.5 k=0.95: 71.95±0.73 ms, 768→729 tok, 9637 MB\\n2026-05-23 15:24:56 [INFO] Pi0.5 k=0.90: 71.55±0.75 ms, 768→690 tok, 9501 MB\\n2026-05-23 15:25:45 [INFO] Pi0.5 k=0.70: 68.59±2.28 ms, 768→537 tok, 9500 MB\\n2026-05-23 15:26:31 [INFO] Pi0.5 k=0.50: 64.31±0.79 ms, 768→384 tok, 9499 MB\\n2026-05-23 15:26:32 [INFO] Saved: eval_results/inference_latency_all_models.csv, eval_results/inference_latency_all_models.json\\n2026-05-23 15:26:32 [INFO] \\n==========================================================================================\\n2026-05-23 15:26:32 [INFO] Model           k    tokens  mean±std(ms)     p95(ms)     mem(MB)\\n2026-05-23 15:26:32 [INFO] ------------------------------------------------------------------------------------------\\n2026-05-23 15:26:32 [INFO] smolvla      1.00  128->128   164.77+-5.85     168.86      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.95  128->120   162.25+-2.46     165.58      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.90  128->114   164.46+-3.11     169.61      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.70  128->88    163.01+-2.19     166.00      1264\\n2026-05-23 15:26:32 [INFO] smolvla      0.50  128->64    162.98+-1.78     165.52      1264\\n2026-05-23 15:26:32 [INFO] pi05         1.00  768->768    67.02+-1.15      68.69      9500\\n2026-05-23 15:26:32 [INFO] pi05         0.95  768->729    71.95+-0.73      73.09      9636\\n2026-05-23 15:26:32 [INFO] pi05         0.90  768->690    71.55+-0.75      72.81      9501\\n2026-05-23 15:26:32 [INFO] pi05         0.70  768->537    68.59+-2.28      72.00      9500\\n2026-05-23 15:26:32 [INFO] pi05         0.50  768->384    64.31+-0.79      65.69      9499\\n2026-05-23 15:26:32 [INFO] ==========================================================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 310_

两个实验都已完成。

---

## 结果汇总

### E3: Token Cosine Similarity

| Model | CV | #Tokens | MeanCosSim | Std | Min | Max |
|-------|-----|---------|-----------|------|------|------|
| π0.5 | 0.055 | 512 | **0.9545** | 0.0174 | 0.8511 | 0.9992 |
| SmolVLA | 0.314 | 128 | **0.7224** | 0.1413 | 0.1482 | 0.9710 |

验证了核心论点：低 CV → 高 cosine similarity（token 同质化），高 CV → 低 similarity（token 分化）。

产出：`artifacts/token_cosine_similarity.{pdf,png,json,npz}`

### E4: Inference Latency

**SmolVLA** (128 tokens, 1264 MB):
| keep_ratio | tokens | latency (ms) |
|-----------|--------|-------------|
| 1.00 | 128→128 | 164.77±5.85 |
| 0.95 | 128→120 | 162.25±2.46 |
| 0.90 | 128→114 | 164.46±3.11 |
| 0.70 | 128→88 | 163.01±2.19 |
| 0.50 | 128→64 | 162.98±1.78 |

**π0.5** (768 tokens, ~9500 MB):
| keep_ratio | tokens | latency (ms) |
|-----------|--------|-------------|
| 1.00 | 768→768 | 67.02±1.15 |
| 0.95 | 768→729 | 71.95±0.73 |
| 0.90 | 768→690 | 71.55±0.75 |
| 0.70 | 768→537 | 68.59±2.28 |
| 0.50 | 768→384 | **64.31±0.79** |

产出：`eval_results/inference_latency_all_models.{csv,json}`

### 修复记录
1. `smolvla_base/config.json`: `load_vlm_weights` 改为 false（跳过 VLM backbone 下载）
2. HF cache 补全 SmolVLM2-500M-Video-Instruct 的 preprocessor/tokenizer 配置文件
3. `analyze_token_cosine_similarity.py`: 修复 SmolVLA camera key 映射 + 改用 `predict_action_chunk` 触发 connector hook
4. `measure_inference_latency.py`: `make_pre_post_processors` 改为传 `policy.config` 而非 `policy`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "uuid": "26d382c2-c39a-44e0-a2bb-e7f921cfe33e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1PJUcT8v1cB8Wfw1raLRu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2147,
      "cache_read_input_tokens": 129134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2147
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

_source line 311_

两个实验都已完成。

---

## 结果汇总

### E3: Token Cosine Similarity

| Model | CV | #Tokens | MeanCosSim | Std | Min | Max |
|-------|-----|---------|-----------|------|------|------|
| π0.5 | 0.055 | 512 | **0.9545** | 0.0174 | 0.8511 | 0.9992 |
| SmolVLA | 0.314 | 128 | **0.7224** | 0.1413 | 0.1482 | 0.9710 |

验证了核心论点：低 CV → 高 cosine similarity（token 同质化），高 CV → 低 similarity（token 分化）。

产出：`artifacts/token_cosine_similarity.{pdf,png,json,npz}`

### E4: Inference Latency

**SmolVLA** (128 tokens, 1264 MB):
| keep_ratio | tokens | latency (ms) |
|-----------|--------|-------------|
| 1.00 | 128→128 | 164.77±5.85 |
| 0.95 | 128→120 | 162.25±2.46 |
| 0.90 | 128→114 | 164.46±3.11 |
| 0.70 | 128→88 | 163.01±2.19 |
| 0.50 | 128→64 | 162.98±1.78 |

**π0.5** (768 tokens, ~9500 MB):
| keep_ratio | tokens | latency (ms) |
|-----------|--------|-------------|
| 1.00 | 768→768 | 67.02±1.15 |
| 0.95 | 768→729 | 71.95±0.73 |
| 0.90 | 768→690 | 71.55±0.75 |
| 0.70 | 768→537 | 68.59±2.28 |
| 0.50 | 768→384 | **64.31±0.79** |

产出：`eval_results/inference_latency_all_models.{csv,json}`

### 修复记录
1. `smolvla_base/config.json`: `load_vlm_weights` 改为 false（跳过 VLM backbone 下载）
2. HF cache 补全 SmolVLM2-500M-Video-Instruct 的 preprocessor/tokenizer 配置文件
3. `analyze_token_cosine_similarity.py`: 修复 SmolVLA camera key 映射 + 改用 `predict_action_chunk` 触发 connector hook
4. `measure_inference_latency.py`: `make_pre_post_processors` 改为传 `policy.config` 而非 `policy`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 2073759,
  "duration_api_ms": 821825,
  "num_turns": 105,
  "stop_reason": "end_turn",
  "session_id": "2df1aaaa-020d-4e69-93b9-79078af1d61f",
  "total_cost_usd": 5.0827045,
  "usage": {
    "input_tokens": 94,
    "cache_creation_input_tokens": 119440,
    "cache_read_input_tokens": 6729053,
    "output_tokens": 38768,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 119440,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 752,
        "cache_read_input_tokens": 129134,
        "cache_creation_input_tokens": 2147,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2147
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1888,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002008,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 94,
      "outputTokens": 38768,
      "cacheReadInputTokens": 6729053,
      "cacheCreationInputTokens": 119440,
      "webSearchRequests": 0,
      "costUSD": 5.0806965,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "51167a0a-8ec3-4206-9509-76e0086732ac"
}
```

</details>

---
