# ops collect mask divergence 30pct 64samples

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029.jsonl`
- **Structured JSON:** [`f84d78aaa64826a5e6e1.json`](../../sessions/f8/f84d78aaa64826a5e6e1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-19T12:22:39.484030+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T12:22:39.484568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T12:22:39.484957+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/figures/mask_stats_30pct_64samples.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/figures/mask_stats_30pct_64samples.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T12:22:39.485191+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/distill_sparse_swiglu/figures/mask_stats_30pct_64samples.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T12:22:39.485346+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "ls /root/distill_sparse_swiglu/figures/mask_stats*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "ls /root/distill_sparse_swiglu/figures/mask_stats*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T12:22:39.485491+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/distill_sparse_swiglu/figures/mask_stats*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T12:22:39.485621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"*mask*divergence*\" -o -name \"*jaccard*\" -o -name \"*mask_stats*py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu -name \"*mask*divergence*\" -o -name \"*jaccard*\" -o -name \"*mask_stats*py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T12:22:39.485905+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/analyze_mask_divergence.py\\n/root/distill_sparse_swiglu/logs/mask_divergence_analysis.log\\n/root/distill_sparse_swiglu/artifacts/mask_divergence_heatmap.pdf\\n/root/distill_sparse_swiglu/artifacts/mask_divergence_heatmap.png\\n/root/distill_sparse_swiglu/results/qwen14b_mask_divergence_30pct.json\\n/root/distill_sparse_swiglu/results/llama8b_mask_divergence_30pct.json\\n/root/distill_sparse_swiglu/figures/mask_divergence_heatmap.pdf\\n/root/distill_sparse_swiglu/figures/mask_divergence_heatmap.png\\n/root/distill_sparse_swiglu/run_mask_divergence.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T12:22:39.486130+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/qwen14b_mask_divergence_30pct.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/results/qwen14b_mask_divergence_30pct.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T12:22:39.486522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"qwen14b\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/models/qwen2.5-14b\\\",\\n  \\\"predictor_path\\\": \\\"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\\\",\\n  \\\"sparsity\\\": 0.3,\\n  \\\"num_layers\\\": 48,\\n  \\\"calib_samples\\\": 32,\\n  \\\"seq_len\\\": 2048,\\n  \\\"per_layer_jaccard\\\": {\\n    \\\"0\\\": 0.440174,\\n    \\\"1\\\": 0.349983,\\n    \\\"2\\\": 0.415829,\\n    \\\"3\\\": 0.189449,\\n    \\\"4\\\": 0.062731,\\n    \\\"5\\\": 0.163983,\\n    \\\"6\\\": 0.243672,\\n    \\\"7\\\": 0.402755,\\n    \\\"8\\\": 0.422423,\\n    \\\"9\\\": 0.442071,\\n    \\\"10\\\": 0.431889,\\n    \\\"11\\\": 0.445985,\\n    \\\"12\\\": 0.442165,\\n    \\\"13\\\": 0.43257,\\n    \\\"14\\\": 0.441256,\\n    \\\"15\\\": 0.430561,\\n    \\\"16\\\": 0.429698,\\n    \\\"17\\\": 0.435564,\\n    \\\"18\\\": 0.437998,\\n    \\\"19\\\": 0.436176,\\n    \\\"20\\\": 0.435023,\\n    \\\"21\\\": 0.435793,\\n    \\\"22\\\": 0.434663,\\n    \\\"23\\\": 0.42607,\\n    \\\"24\\\": 0.436156,\\n    \\\"25\\\": 0.438693,\\n    \\\"26\\\": 0.431254,\\n    \\\"27\\\": 0.420053,\\n    \\\"28\\\": 0.425974,\\n    \\\"29\\\": 0.418998,\\n    \\\"30\\\": 0.418045,\\n    \\\"31\\\": 0.41011,\\n    \\\"32\\\": 0.418114,\\n    \\\"33\\\": 0.410631,\\n    \\\"34\\\": 0.402751,\\n    \\\"35\\\": 0.393927,\\n    \\\"36\\\": 0.404501,\\n    \\\"37\\\": 0.40688,\\n    \\\"38\\\": 0.40284,\\n    \\\"39\\\": 0.410379,\\n    \\\"40\\\": 0.414962,\\n    \\\"41\\\": 0.414954,\\n    \\\"42\\\": 0.43519,\\n    \\\"43\\\": 0.425312,\\n    \\\"44\\\": 0.423825,\\n    \\\"45\\\": 0.429706,\\n    \\\"46\\\": 0.425693,\\n    \\\"47\\\": 0.428908\\n  },\\n  \\\"per_layer_kl_retention\\\": {\\n    \\\"0\\\": 0.699942,\\n    \\\"1\\\": 0.699942,\\n    \\\"2\\\": 0.699942,\\n    \\\"3\\\": 0.699942,\\n    \\\"4\\\": 0.699942,\\n    \\\"5\\\": 0.699942,\\n    \\\"6\\\": 0.699942,\\n    \\\"7\\\": 0.699942,\\n   
…[truncated 2978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T12:22:39.486877+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/llama8b_mask_divergence_30pct.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/results/llama8b_mask_divergence_30pct.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T12:22:39.487170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"llama8b\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n  \\\"predictor_path\\\": \\\"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\\\",\\n  \\\"sparsity\\\": 0.3,\\n  \\\"num_layers\\\": 32,\\n  \\\"calib_samples\\\": 32,\\n  \\\"seq_len\\\": 2048,\\n  \\\"per_layer_jaccard\\\": {\\n    \\\"0\\\": 0.481837,\\n    \\\"1\\\": 0.464394,\\n    \\\"2\\\": 0.45435,\\n    \\\"3\\\": 0.432342,\\n    \\\"4\\\": 0.420608,\\n    \\\"5\\\": 0.423578,\\n    \\\"6\\\": 0.426048,\\n    \\\"7\\\": 0.419732,\\n    \\\"8\\\": 0.398376,\\n    \\\"9\\\": 0.394603,\\n    \\\"10\\\": 0.395016,\\n    \\\"11\\\": 0.391773,\\n    \\\"12\\\": 0.384019,\\n    \\\"13\\\": 0.371818,\\n    \\\"14\\\": 0.352754,\\n    \\\"15\\\": 0.359296,\\n    \\\"16\\\": 0.366561,\\n    \\\"17\\\": 0.372498,\\n    \\\"18\\\": 0.37408,\\n    \\\"19\\\": 0.363083,\\n    \\\"20\\\": 0.361961,\\n    \\\"21\\\": 0.372153,\\n    \\\"22\\\": 0.371735,\\n    \\\"23\\\": 0.383133,\\n    \\\"24\\\": 0.385783,\\n    \\\"25\\\": 0.382824,\\n    \\\"26\\\": 0.400016,\\n    \\\"27\\\": 0.401046,\\n    \\\"28\\\": 0.390482,\\n    \\\"29\\\": 0.385376,\\n    \\\"30\\\": 0.364203,\\n    \\\"31\\\": 0.360514\\n  },\\n  \\\"per_layer_kl_retention\\\": {\\n    \\\"0\\\": 0.699986,\\n    \\\"1\\\": 0.699986,\\n    \\\"2\\\": 0.699986,\\n    \\\"3\\\": 0.699986,\\n    \\\"4\\\": 0.699986,\\n    \\\"5\\\": 0.699986,\\n    \\\"6\\\": 0.699986,\\n    \\\"7\\\": 0.699986,\\n    \\\"8\\\": 0.699986,\\n    \\\"9\\\": 0.699986,\\n    \\\"10\\\": 0.699986,\\n    \\\"11\\\": 0.699986,\\n    \\\"12\\\": 0.699986,\\n    \\\"13\\\": 0.699986,\\n    \\\"14\\\": 0.699986,\\n    \\\"15\\\": 0.699986,\\n    \\\"16\\\": 0.699986,\\n    \\\"17\\\": 0.699986,\\n    \\\"18\\\": 0.699986,\\n    \\\"19\\\": 0.699986,\\n    \\\"20\\\": 0.699986,\\n    \\\"21\\\": 0.699986,\\n    \\\"22\\\": 0.699986,\\n    \\\"23\\\": 0.699986
…[truncated 1645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T12:22:39.487465+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "head -80 /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "head -80 /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T12:22:39.487610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "ls /root/distill_sparse_swiglu/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "ls /root/distill_sparse_swiglu/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T12:22:39.487788+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-layer Jaccard divergence between KL-predicted and magnitude-based masks.\\n\\nUsage:\\n  cd /root/distill_sparse_swiglu\\n  HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache \\\\\\n    python3 src/analyze_mask_divergence.py \\\\\\n      --model_path /root/autodl-tmp/models/qwen2.5-14b \\\\\\n      --predictor_path checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt \\\\\\n      --model_name qwen14b --sparsity 0.3 --device cuda:0\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport importlib.util\\nimport json\\nimport os\\nimport sys\\n\\nimport torch\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom predictor import SparsityPredictor\\nfrom data_utils import get_eval_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n\\ndef _best_attn_impl():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\n\\n@torch.no_grad()\\ndef get_magnitude_scores(model, calib_ids, batch_size=1):\\n    \\\"\\\"\\\"Per-neuron mean |act(gate)*up| across calibration data.\\\"\\\"\\\"\\n    accum = {}\\n    n_batches = 0\\n    saved = {}\\n\\n    for li, layer in enumerate(model.model.layers):\\n        saved[li] = layer.mlp.forward\\n        mlp = layer.mlp\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n        def _make(idx, _gp, _up, _dp, _af):\\n            def fwd(x):\\n                h = _af(_gp(x)) * _up(x)\\n                mag = h.abs().mean(dim=(0, 1))\\n                if idx in accum:\\n                    accum[idx] = accum[idx] + mag\\n                else:\\n                    accum[idx] = mag\\n                return _dp(h)\\n            return fwd\\n        layer.mlp.forward = _make(li, gp, up, dp, af)\\n\\n    for start in range(0, calib_ids.size(0), batch_size):\\n        model(calib_ids[start:start + batch_si
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T12:22:39.487960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"benchmark\\nbenchmark_latency.json\\nc4_ood_ppl.json\\ncuda1_diagnosis_report.txt\\ndryrun\\nllama8b_mask_divergence_30pct.json\\nlm_eval\\nlm_eval_dense.log\\nlm_eval_dense_final.log\\nlm_eval_dense_gpu1.log\\nlm_eval_dense_test.log\\nlm_eval_dense_v2.log\\nlm_eval_dense_v3.log\\nlm_eval_full.log\\nper_layer_allocation_s42_vs_s123.json\\nplan_006_reeval\\nplan_007\\nplan_007_all_ppl_fixed.json\\nplan_007_fixed\\nplan_007_fixed_p2\\nplan_007_fixed_p3\\nplan_007_fixed_p4\\nplan_007_fixed_remaining.json\\nplan_007_sparsity70.json\\nplan_009_mistral\\nqwen14b_mask_divergence_30pct.json\\nsubsumption_test\\nuniform_30pct_dryrun\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T12:22:39.488266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"*mask_stats*\" -o -name \"*64sample*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "find /root/distill_sparse_swiglu -name \"*mask_stats*\" -o -name \"*64sample*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T12:22:39.488637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T12:22:39.488787+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -n \"calib_samples\\|n_samples\\|num_samples\\|argparse\" /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -n \"calib_samples\\|n_samples\\|num_samples\\|argparse\" /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T12:22:39.488930+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T12:22:39.489134+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/run_mask_divergence.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "cat /root/distill_sparse_swiglu/run_mask_divergence.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T12:22:39.489303+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\nset -e\\ncd /root/distill_sparse_swiglu\\nexport PATH=\\\"/root/miniconda3/bin:$PATH\\\"\\nexport HF_HUB_OFFLINE=1\\nexport TRANSFORMERS_OFFLINE=1\\nexport HF_HOME=/root/autodl-tmp/.hf_cache\\nexport CUDA_VISIBLE_DEVICES=1\\n\\necho \\\"==========================================\\\"\\necho \\\"Phase 1: Qwen-14B mask divergence analysis\\\"\\necho \\\"==========================================\\\"\\npython3 src/analyze_mask_divergence.py \\\\\\n  --model_path /root/autodl-tmp/models/qwen2.5-14b \\\\\\n  --predictor_path checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt \\\\\\n  --model_name qwen14b \\\\\\n  --sparsity 0.3 \\\\\\n  --calib_samples 32 \\\\\\n  --device cuda:0 \\\\\\n  --output_dir results\\n\\necho \\\"\\\"\\necho \\\"==========================================\\\"\\necho \\\"Phase 2: LLaMA-8B mask divergence analysis\\\"\\necho \\\"==========================================\\\"\\npython3 src/analyze_mask_divergence.py \\\\\\n  --model_path /root/autodl-tmp/models/llama-3.1-8b \\\\\\n  --predictor_path checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \\\\\\n  --model_name llama8b \\\\\\n  --sparsity 0.3 \\\\\\n  --calib_samples 32 \\\\\\n  --device cuda:0 \\\\\\n  --output_dir results\\n\\necho \\\"\\\"\\necho \\\"==========================================\\\"\\necho \\\"Both analyses complete!\\\"\\necho \\\"==========================================\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T12:22:39.489473+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -rn \"mask_stats\" /root/distill_sparse_swiglu/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "grep -rn \"mask_stats\" /root/distill_sparse_swiglu/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T12:22:39.489596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "tail -80 /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "tail -80 /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T12:22:39.489826+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/src/evaluate.py:177:def _print_mask_stats(name, masks):\\n/root/distill_sparse_swiglu/src/evaluate.py:511:        _print_mask_stats(\\\"TEAL-predictor\\\", global_masks)\\n/root/distill_sparse_swiglu/src/evaluate.py:540:                _print_mask_stats(\\\"Vanilla-TEAL\\\", masks)\\n/root/distill_sparse_swiglu/src/evaluate.py:549:                _print_mask_stats(\\\"WINA\\\", masks)\\n/root/distill_sparse_swiglu/src/evaluate.py:559:                _print_mask_stats(\\\"R-Sparse\\\", masks)\\n/root/distill_sparse_swiglu/src/evaluate.py:568:                _print_mask_stats(\\\"TEAL-greedy\\\", masks)\\n/root/distill_sparse_swiglu/src/evaluate.py:577:                _print_mask_stats(\\\"WINA-greedy\\\", masks)\\n/root/distill_sparse_swiglu/src/benchmark_eval.py:36:    _print_mask_stats,\\n/root/distill_sparse_swiglu/src/benchmark_eval.py:351:        _print_mask_stats(args.baseline_mode, masks)\\n/root/distill_sparse_swiglu/src/benchmark_eval.py:376:            _print_mask_stats(\\\"TEAL-predictor\\\", masks)\\n/root/distill_sparse_swiglu/src/run_baselines_sweep.py:12:    _print_mask_stats,\\n/root/distill_sparse_swiglu/src/run_baselines_sweep.py:68:        model_sp = _print_mask_stats(f\\\"TEAL-{sp_key}\\\", masks)\\n/root/distill_sparse_swiglu/src/run_baselines_sweep.py:77:            model_sp_w = _print_mask_stats(f\\\"WINA-{sp_key}\\\", masks_w)\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py:119:def print_mask_stats(name, masks):\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py:218:        print_mask_stats(\\\"TEAL-global\\\", global_masks)\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py:219:        print_mask_stats(\\\"TEAL-uniform\\\", uniform_masks)\\n/root/distill_sparse_swiglu/src/lm_eval_sparse.py:227:        actual_sp = print_mask_stats(f\\\"TEAL-{args.allocation_strategy}\\\", masks)\\n/root/distill_sparse_swiglu/src/lm_eval_teal.py:86:def print_mask_stats(nam
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T12:22:39.490112+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    sparsity = args.sparsity\\n    print(f\\\"\\\\nComputing per-layer Jaccard distance at {sparsity*100:.0f}% sparsity...\\\")\\n    per_layer_jaccard = {}\\n    per_layer_kl_retention = {}\\n    per_layer_mag_retention = {}\\n\\n    for li in range(num_layers):\\n        kl_mask = scores_to_mask(kl_scores[li], sparsity)\\n        mag_mask = scores_to_mask(mag_scores[li], sparsity)\\n        jd = jaccard_distance(kl_mask, mag_mask)\\n        kl_ret = kl_mask.float().mean().item()\\n        mag_ret = mag_mask.float().mean().item()\\n        per_layer_jaccard[li] = round(jd, 6)\\n        per_layer_kl_retention[li] = round(kl_ret, 6)\\n        per_layer_mag_retention[li] = round(mag_ret, 6)\\n\\n    jaccard_vals = list(per_layer_jaccard.values())\\n    mean_jd = sum(jaccard_vals) / len(jaccard_vals)\\n    std_jd = (sum((v - mean_jd)**2 for v in jaccard_vals) / len(jaccard_vals)) ** 0.5\\n    max_layer = max(per_layer_jaccard, key=per_layer_jaccard.get)\\n    min_layer = min(per_layer_jaccard, key=per_layer_jaccard.get)\\n\\n    first_q = jaccard_vals[:num_layers//4]\\n    last_q = jaccard_vals[3*num_layers//4:]\\n    mid = jaccard_vals[num_layers//4:3*num_layers//4]\\n\\n    results = {\\n        \\\"model_name\\\": args.model_name,\\n        \\\"model_path\\\": args.model_path,\\n        \\\"predictor_path\\\": args.predictor_path,\\n        \\\"sparsity\\\": sparsity,\\n        \\\"num_layers\\\": num_layers,\\n        \\\"calib_samples\\\": n,\\n        \\\"seq_len\\\": args.seq_len,\\n        \\\"per_layer_jaccard\\\": {str(k): v for k, v in per_layer_jaccard.items()},\\n        \\\"per_layer_kl_retention\\\": {str(k): v for k, v in per_layer_kl_retention.items()},\\n        \\\"per_layer_mag_retention\\\": {str(k): v for k, v in per_layer_mag_retention.items()},\\n        \\\"summary\\\": {\\n            \\\"mean_jaccard\\\": round(mean_jd, 6),\\n            \\\"std_jaccard\\\": round(std_jd, 6),\\n         
…[truncated 2111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T12:22:39.490533+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34887",
  "command": "head -120 /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34887",
    "command": "head -120 /root/distill_sparse_swiglu/src/analyze_mask_divergence.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T12:22:39.490749+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-layer Jaccard divergence between KL-predicted and magnitude-based masks.\\n\\nUsage:\\n  cd /root/distill_sparse_swiglu\\n  HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache \\\\\\n    python3 src/analyze_mask_divergence.py \\\\\\n      --model_path /root/autodl-tmp/models/qwen2.5-14b \\\\\\n      --predictor_path checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt \\\\\\n      --model_name qwen14b --sparsity 0.3 --device cuda:0\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport importlib.util\\nimport json\\nimport os\\nimport sys\\n\\nimport torch\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom predictor import SparsityPredictor\\nfrom data_utils import get_eval_dataset\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\n\\n\\ndef _best_attn_impl():\\n    if importlib.util.find_spec(\\\"flash_attn\\\"):\\n        return \\\"flash_attention_2\\\"\\n    return \\\"sdpa\\\"\\n\\n\\n@torch.no_grad()\\ndef get_magnitude_scores(model, calib_ids, batch_size=1):\\n    \\\"\\\"\\\"Per-neuron mean |act(gate)*up| across calibration data.\\\"\\\"\\\"\\n    accum = {}\\n    n_batches = 0\\n    saved = {}\\n\\n    for li, layer in enumerate(model.model.layers):\\n        saved[li] = layer.mlp.forward\\n        mlp = layer.mlp\\n        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn\\n        def _make(idx, _gp, _up, _dp, _af):\\n            def fwd(x):\\n                h = _af(_gp(x)) * _up(x)\\n                mag = h.abs().mean(dim=(0, 1))\\n                if idx in accum:\\n                    accum[idx] = accum[idx] + mag\\n                else:\\n                    accum[idx] = mag\\n                return _dp(h)\\n            return fwd\\n        layer.mlp.forward = _make(li, gp, up, dp, af)\\n\\n    for start in range(0, calib_ids.size(0), batch_size):\\n        model(calib_ids[start:start + batch_si
…[truncated 2442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T12:22:39.491096+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T12:22:39.491251+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 93985 MiB, 97887 MiB, 98 %\\n1, 93985 MiB, 97887 MiB, 100 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T12:22:39.491427+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "ps aux | grep -E \"mask_divergence|jaccard|analyze_mask\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "ps aux | grep -E \"mask_divergence|jaccard|analyze_mask\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T12:22:39.491569+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "nvidia-smi | head -40",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "nvidia-smi | head -40",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T12:22:39.491701+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'ps aux | grep -E \\\"mask_divergence|jaccard|analyze_mask\\\" | grep -v grep'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T12:22:39.491851+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 19 20:22:12 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |                  Off |\\n| N/A   84C    P0            600W /  600W |   93985MiB /  97887MiB |    100%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:C8:00.0 Off |                  Off |\\n| N/A   84C    P0            599W /  600W |   93985MiB /  97887MiB |    100%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T12:22:39.492009+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34887",
  "command": "ps aux | grep -E \"100842|100070\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34887",
    "command": "ps aux | grep -E \"100842|100070\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T12:22:39.492430+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     100070  100  0.3 133321536 4018640 pts/0 Rl 19:21  61:19 python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s456_eval_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s456/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\\nroot     100842  100  0.3 133323272 4019568 pts/1 Rl 19:25  56:52 python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T12:22:39.492653+00:00_

Both GPUs are running Qwen-14B benchmark evals. No mask divergence computation is running, and 64-sample computation can't start now.

However, 32-sample results already exist for both models. Here are the results:

**LLaMA-8B 30% Sparsity Mask Divergence (32 samples):**
- Mean Jaccard Distance: 0.3939 (39.39%)
- Min: 0.3528 (layer 14)
- Max: 0.4818 (layer 0)
- Std: 0.0314

**Qwen-14B 30% Sparsity Mask Divergence (32 samples):**
- Mean Jaccard Distance: 0.4016 (40.16%)
- Min: 0.0627 (layer 4) — anomalously low
- Max: 0.4460 (layer 11)
- Std: 0.0756

**Comparison with 50% reference (64 samples):**
- 50%: Mean=0.6824 → 30% LLaMA: 0.3939, 30% Qwen: 0.4016
- As expected, 30% is substantially lower than 50% (~42% relative drop)

**Status of 64-sample run:** Cannot run now — both cuda:0 and cuda:1 are occupied by `benchmark_eval.py` jobs (qwen14b_kl30_s456_eval_v2 and qwen14b_kl30_s123_eval_v4, both running ~1hr). The script supports `--calib_samples 64` but needs a free GPU. The 32→64 sample increase would reduce variance but likely won't shift means significantly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029"
}
```

</details>

---
