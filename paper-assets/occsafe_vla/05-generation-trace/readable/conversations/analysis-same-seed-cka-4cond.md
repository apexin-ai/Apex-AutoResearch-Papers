# analysis same seed cka 4cond

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_analysis_same_seed_cka_4cond_20260525T050056.jsonl`
- **Structured JSON:** [`ce133b7eaf2705530322.json`](../../sessions/ce/ce133b7eaf2705530322.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-25T05:04:14.060257+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T05:04:14.060785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T05:04:14.061049+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "find /root/occsafe_vla/openvla-oft -name \"cka_analysis.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "find /root/occsafe_vla/openvla-oft -name \"cka_analysis.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T05:04:14.061259+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/checkpoints/vanilla_retrain_s0/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/checkpoints/vanilla_retrain_s0/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T05:04:14.061482+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T05:04:14.061725+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T05:04:14.061950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/checkpoints/full_occ_retrain_s0/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/checkpoints/full_occ_retrain_s0/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T05:04:14.062170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T05:04:14.062387+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T05:04:14.062619+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug\\nopenvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T05:04:14.062860+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/autodl-tmp/checkpoints/full_occ_ln_s0/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/autodl-tmp/checkpoints/full_occ_ln_s0/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T05:04:14.063100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug\\nopenvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T05:04:14.063361+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "find /root/occsafe_vla -name \"*cka*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "find /root/occsafe_vla -name \"*cka*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T05:04:14.063574+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/occsafe_vla/analysis/cka_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T05:04:14.063804+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ls /root/occsafe_vla/openvla-oft/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ls /root/occsafe_vla/openvla-oft/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T05:04:14.064007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ablation_diagnostic.py\\noutput\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T05:04:14.064259+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "head -150 /root/occsafe_vla/analysis/cka_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "head -150 /root/occsafe_vla/analysis/cka_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T05:04:14.064603+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nCKA (Centered Kernel Alignment) analysis for OccSafe-VLA.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport gc\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, \\\"/root/occsafe_vla/openvla-oft\\\")\\n\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\n\\ndef log(msg):\\n    print(f\\\"[{time.strftime('%H:%M:%S')}] {msg}\\\", flush=True)\\n\\n\\ndef parse_args():\\n    parser = argparse.ArgumentParser()\\n    parser.add_argument(\\\"--pretrained_path\\\", type=str, required=True)\\n    parser.add_argument(\\\"--checkpoint_paths\\\", type=str, nargs=\\\"+\\\", required=True)\\n    parser.add_argument(\\\"--condition_names\\\", type=str, nargs=\\\"+\\\", required=True)\\n    parser.add_argument(\\\"--libero_data_dir\\\", type=str, required=True)\\n    parser.add_argument(\\\"--num_samples\\\", type=int, default=200)\\n    parser.add_argument(\\\"--batch_size\\\", type=int, default=8)\\n    parser.add_argument(\\\"--gpu\\\", type=int, default=0)\\n    parser.add_argument(\\\"--output_dir\\\", type=str, required=True)\\n    return parser.parse_args()\\n\\n\\ndef load_libero_images(data_dir, num_images=200):\\n    images = []\\n    hdf5_files = sorted(Path(data_dir).glob(\\\"*.hdf5\\\"))\\n    if not hdf5_files:\\n        raise FileNotFoundError(f\\\"No HDF5 files in {data_dir}\\\")\\n    for hdf5_file in hdf5_files:\\n        if len(images) >= num_images:\\n            break\\n        with h5py.File(hdf5_file, \\\"r\\\") as f:\\n            for demo_key in sorted(f[\\\"data\\\"].keys()):\\n                if len(images) >= num_images:\\n                    break\\n                rgb = f[\\\"data\\\"][demo_key][\\\"obs\\\"][\\\"agentview_rgb\\\"]\\n                n_frames = rgb.shape[0]\\n                step = max(1, n_frames // 4
…[truncated 3447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T05:04:14.064890+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -150 /root/occsafe_vla/analysis/cka_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -150 /root/occsafe_vla/analysis/cka_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T05:04:14.065250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    with torch.no_grad():\\n        for batch_idx, pv in enumerate(pixel_values_batches):\\n            pv = pv.to(device, dtype=torch.bfloat16)\\n            try:\\n                _ = vb(pv)\\n            except Exception as e:\\n                log(f\\\"  ERROR in forward pass batch {batch_idx}: {e}\\\")\\n                raise\\n            del pv\\n            if (batch_idx + 1) % 5 == 0:\\n                log(f\\\"  Batch {batch_idx + 1}/{len(pixel_values_batches)} done\\\")\\n\\n    torch.cuda.synchronize(device)\\n    log(\\\"  Forward pass complete\\\")\\n\\n    for h in hooks:\\n        h.remove()\\n\\n    result = {}\\n    for name, feat_list in features.items():\\n        if feat_list:\\n            result[name] = torch.cat(feat_list, dim=0)\\n\\n    del vb\\n    torch.cuda.empty_cache()\\n    gc.collect()\\n    log(f\\\"  Cleaned up, GPU cache cleared\\\")\\n\\n    return result\\n\\n\\ndef main():\\n    args = parse_args()\\n    assert len(args.checkpoint_paths) == len(args.condition_names)\\n\\n    device = torch.device(f\\\"cuda:{args.gpu}\\\")\\n    os.makedirs(args.output_dir, exist_ok=True)\\n\\n    log(f\\\"Using GPU {args.gpu}\\\")\\n    log(f\\\"Loading {args.num_samples} images from {args.libero_data_dir}\\\")\\n    images = load_libero_images(args.libero_data_dir, args.num_samples)\\n    log(f\\\"Loaded {len(images)} images\\\")\\n\\n    processor = AutoProcessor.from_pretrained(args.pretrained_path, trust_remote_code=True)\\n    pixel_values_batches = []\\n    for i in range(0, len(images), args.batch_size):\\n        batch_imgs = images[i:i + args.batch_size]\\n        pv = processor.image_processor(batch_imgs, return_tensors=\\\"pt\\\")[\\\"pixel_values\\\"]\\n        pixel_values_batches.append(pv.cpu())\\n    del images, processor\\n    gc.collect()\\n\\n    total_samples = sum(pv.shape[0] for pv in pixel_values_batches)\\n    log(f\\\"Preprocessed {total_samples} samples, shape:
…[truncated 4544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T05:04:14.065577+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T05:04:14.065823+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T05:04:14.066077+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "hypothesis",
  "value": "Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "hypothesis",
    "value": "Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T05:04:14.066304+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:01:59.870Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5807}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T05:04:14.066521+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "status",
  "value": "RUNNING",
  "project": "occsafe_vla",
  "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths ... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "status",
    "value": "RUNNING",
    "project": "occsafe_vla",
    "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths ... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T05:04:14.066803+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.3653}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T05:04:14.067017+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "status",
  "value": "QUEUED",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "status",
    "value": "QUEUED",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T05:04:14.067237+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:02:10.130Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0298}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T05:04:14.067461+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "status",
  "value": "RUNNING",
  "project": "occsafe_vla",
  "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "status",
    "value": "RUNNING",
    "project": "occsafe_vla",
    "spec": "{'command': \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", 'server': 'westd-10894', 'data_path': '/root/autodl-tmp/libero_datasets/libero_spatial', 'data_count': 200, 'model_name': 'openvla-7b', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T05:04:14.067741+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:02:17.083Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0819}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-25T05:04:14.068008+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-10894",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && mkdir -p /root/autodl-tmp/analysis/cka_same_seed && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py \\\n  --pretrained_path /root/autodl-tmp/models/openvla-7b \\\n  --checkpoint_paths \\\n    /root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n    /root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n    /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n    /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n  --condition_names \"Vanilla\" \"Full OCC (BN)\" \"Detach+BN\" \"Full OCC (LN)\" \\\n  --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \\\n  --output_dir /root/autodl-tmp/analysis/cka_same_seed \\\n  --gpu 0 \\\n  --num_samples 200' > /root/autodl-tmp/analysis/cka_same_seed/run.log 2>&1 &\necho \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-10894",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && mkdir -p /root/autodl-tmp/analysis/cka_same_seed && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py \\\n  --pretrained_path /root/autodl-tmp/models/openvla-7b \\\n  --checkpoint_paths \\\n    /root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n    /root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n    /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n    /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n  --condition_names \"Vanilla\" \"Full OCC (BN)\" \"Detach+BN\" \"Full OCC (LN)\" \\\n  --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \\\n  --output_dir /root/autodl-tmp/analysis/cka_same_seed \\\n  --gpu 0 \\\n  --num_samples 200' > /root/autodl-tmp/analysis/cka_same_seed/run.log 2>&1 &\necho \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-25T05:04:14.068281+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && mkdir -p /root/autodl-tmp/analysis/cka_same_seed && nohup bash -c \\\\'CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py \\\\\\\\\\\\n  --pretrained_path /root/autodl-tmp/models/openvla-7b \\\\\\\\\\\\n  --checkpoint_paths \\\\\\\\\\\\n    /root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\\\\\\\\\\n    /root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\\\\\\\\\\n    /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\\\\\\\\\\n    /root/autodl-tmp/checkpoints/full_occ_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\\\\\\\\\\n  --condition_names \\\"Vanilla\\\" \\\"Full OCC (BN)\\\" \\\"Detach+BN\\\" \\\"Full OCC (LN)\\\" \\\\\\\\\\\\n  --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \\\\\\\\\\\\n  --output_dir /root/autodl-tmp/analysis/cka_same_seed \\\\\\\\\\\\n  --gpu 0 \\\\\\\\\\\\n  --num_samples 200\\\\' > /root/autodl-tmp/analysis/cka_same_seed/run.log 2>&1 &\\\\necho \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=37266\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-25T05:04:14.068556+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "ps -p 37266 -o pid,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "ps -p 37266 -o pid,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T05:04:14.068794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "tail -20 /root/autodl-tmp/analysis/cka_same_seed/run.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "tail -20 /root/autodl-tmp/analysis/cka_same_seed/run.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T05:04:14.069002+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID     ELAPSED CMD\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-25T05:04:14.069224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[13:02:57]   Batch 25/25 done\\n[13:02:57]   Forward pass complete\\n[13:02:57]   Cleaned up, GPU cache cleared\\n[13:02:57]   Result: 51 layers x 200 samples\\n[13:02:57] Computing CKA...\\n[13:02:59] Saved: /root/autodl-tmp/analysis/cka_same_seed/cka_results.json\\n[13:02:59] Generating plots...\\n[13:03:00] Saved: cka_analysis.pdf, cka_analysis.png\\n[13:03:00] \\n[13:03:00] =================================================================\\n[13:03:00] CKA Summary (higher = more similar to pretrained)\\n[13:03:00] =================================================================\\n[13:03:00] Condition         DINOv2 mean  DINOv2 min   SigLIP mean  SigLIP min\\n[13:03:00] -----------------------------------------------------------------\\n[13:03:00] Vanilla                0.9676      0.8993        0.9530      0.8425\\n[13:03:00] Full OCC (BN)          0.9594      0.8422        0.9593      0.8799\\n[13:03:00] Detach+BN              0.9635      0.8895        0.9532      0.8292\\n[13:03:00] Full OCC (LN)          0.6404      0.2558        0.9497      0.8479\\n[13:03:00] =================================================================\\n[13:03:00] DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-25T05:04:14.069494+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "metrics",
  "value": "{'Vanilla': {'dinov2_mean_cka': 0.9676, 'dinov2_min_cka': 0.8993, 'siglip_mean_cka': 0.953, 'siglip_min_cka': 0.8425}, 'Full OCC (BN)': {'dinov2_mean_cka': 0.9594, 'dinov2_min_cka': 0.8422, 'siglip_mean_cka': 0.9593, 'siglip_min_cka': 0.8799}, 'Detach+BN': {'dinov2_mean_cka': 0.9635, 'dinov2_min_cka': 0.8895, 'siglip_mean_cka': 0.9532, 'siglip_min_cka': 0.8292}, 'Full OCC (LN)': {'dinov2_mean_cka': 0.6404, 'dinov2_min_cka': 0.2558, 'siglip_mean_cka': 0.9497, 'siglip_min_cka': 0.8479}}",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "metrics",
    "value": "{'Vanilla': {'dinov2_mean_cka': 0.9676, 'dinov2_min_cka': 0.8993, 'siglip_mean_cka': 0.953, 'siglip_min_cka': 0.8425}, 'Full OCC (BN)': {'dinov2_mean_cka': 0.9594, 'dinov2_min_cka': 0.8422, 'siglip_mean_cka': 0.9593, 'siglip_min_cka': 0.8799}, 'Detach+BN': {'dinov2_mean_cka': 0.9635, 'dinov2_min_cka': 0.8895, 'siglip_mean_cka': 0.9532, 'siglip_min_cka': 0.8292}, 'Full OCC (LN)': {'dinov2_mean_cka': 0.6404, 'dinov2_min_cka': 0.2558, 'siglip_mean_cka': 0.9497, 'siglip_min_cka': 0.8479}}",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-25T05:04:14.069814+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:03:22.632Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"metrics\": {\"Vanilla\": {\"dinov2_mean_cka\": 0.9676, \"dinov2_min_cka\": 0.8993, \"siglip_mean_cka\": 0.953, \"siglip_min_cka\": 0.8425}, \"Full OCC (BN)\": {\"dinov2_mean_cka\": 0.9594, \"dinov2_min_cka\": 0.8422, \"siglip_mean_cka\": 0.9593, \"siglip_min_cka\": 0.8799}, \"Detach+BN\": {\"dinov2_mean_cka\": 0.9635, \"dinov2_min_cka\": 0.8895, \"siglip_mean_cka\": 0.9532, \"siglip_min_cka\": 0.8292}, \"Full OCC (LN)\": {\"dinov2_mean_cka\": 0.6404, \"dinov2_min_cka\": 0.2558, \"siglip_mean_cka\": 0.9497, \"siglip_min_cka\": 0.8479}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5655}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-25T05:04:14.070058+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "conclusion",
  "value": "Full OCC (LN) causes severe DINOv2 representation drift (mean CKA=0.64, min=0.26), while SigLIP is preserved (~0.95). Vanilla/Full OCC (BN)/Detach+BN all preserve both backbones well (>0.95 mean CKA). LN variant selectively disrupts DINOv2 while leaving SigLIP intact.",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "conclusion",
    "value": "Full OCC (LN) causes severe DINOv2 representation drift (mean CKA=0.64, min=0.26), while SigLIP is preserved (~0.95). Vanilla/Full OCC (BN)/Detach+BN all preserve both backbones well (>0.95 mean CKA). LN variant selectively disrupts DINOv2 while leaving SigLIP intact.",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-25T05:04:14.070273+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'Full OCC (LN) causes severe DINOv2 representation drift (mean CKA=0.64, min=0.26), while SigLIP is preserved (~0.95). Vanilla/Full OCC (BN)/Detach+BN all preserve both backbones well (>0.95 mean CKA). LN variant selectively disrupts DINOv2 while leaving SigLIP intact.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.3624}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-25T05:04:14.070482+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "status",
  "value": "DONE",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "status",
    "value": "DONE",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-25T05:04:14.070724+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.3274}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-25T05:04:14.070930+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/analysis/cka_same_seed",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/analysis/cka_same_seed",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-25T05:04:14.071181+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:03:29.411Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"metrics\": {\"Vanilla\": {\"dinov2_mean_cka\": 0.9676, \"dinov2_min_cka\": 0.8993, \"siglip_mean_cka\": 0.953, \"siglip_min_cka\": 0.8425}, \"Full OCC (BN)\": {\"dinov2_mean_cka\": 0.9594, \"dinov2_min_cka\": 0.8422, \"siglip_mean_cka\": 0.9593, \"siglip_min_cka\": 0.8799}, \"Detach+BN\": {\"dinov2_mean_cka\": 0.9635, \"dinov2_min_cka\": 0.8895, \"siglip_mean_cka\": 0.9532, \"siglip_min_cka\": 0.8292}, \"Full OCC (LN)\": {\"dinov2_mean_cka\": 0.6404, \"dinov2_min_cka\": 0.2558, \"siglip_mean_cka\": 0.9497, \"siglip_min_cka\": 0.8479}}, \"checkpoint_path\": \"/root/autodl-tmp/analysis/cka_same_seed\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5536}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-25T05:04:14.071447+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "log_path",
  "value": "/root/autodl-tmp/analysis/cka_same_seed/run.log",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "log_path",
    "value": "/root/autodl-tmp/analysis/cka_same_seed/run.log",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-25T05:04:14.071723+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:03:30.543Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"metrics\": {\"Vanilla\": {\"dinov2_mean_cka\": 0.9676, \"dinov2_min_cka\": 0.8993, \"siglip_mean_cka\": 0.953, \"siglip_min_cka\": 0.8425}, \"Full OCC (BN)\": {\"dinov2_mean_cka\": 0.9594, \"dinov2_min_cka\": 0.8422, \"siglip_mean_cka\": 0.9593, \"siglip_min_cka\": 0.8799}, \"Detach+BN\": {\"dinov2_mean_cka\": 0.9635, \"dinov2_min_cka\": 0.8895, \"siglip_mean_cka\": 0.9532, \"siglip_min_cka\": 0.8292}, \"Full OCC (LN)\": {\"dinov2_mean_cka\": 0.6404, \"dinov2_min_cka\": 0.2558, \"siglip_mean_cka\": 0.9497, \"siglip_min_cka\": 0.8479}}, \"checkpoint_path\": \"/root/autodl-tmp/analysis/cka_same_seed\", \"log_path\": \"/root/autodl-tmp/analysis/cka_same_seed/run.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5696}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-25T05:04:14.071962+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "conclusion",
  "value": "success",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "conclusion",
    "value": "success",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-25T05:04:14.072211+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:03:34.116Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"metrics\": {\"Vanilla\": {\"dinov2_mean_cka\": 0.9676, \"dinov2_min_cka\": 0.8993, \"siglip_mean_cka\": 0.953, \"siglip_min_cka\": 0.8425}, \"Full OCC (BN)\": {\"dinov2_mean_cka\": 0.9594, \"dinov2_min_cka\": 0.8422, \"siglip_mean_cka\": 0.9593, \"siglip_min_cka\": 0.8799}, \"Detach+BN\": {\"dinov2_mean_cka\": 0.9635, \"dinov2_min_cka\": 0.8895, \"siglip_mean_cka\": 0.9532, \"siglip_min_cka\": 0.8292}, \"Full OCC (LN)\": {\"dinov2_mean_cka\": 0.6404, \"dinov2_min_cka\": 0.2558, \"siglip_mean_cka\": 0.9497, \"siglip_min_cka\": 0.8479}}, \"checkpoint_path\": \"/root/autodl-tmp/analysis/cka_same_seed\", \"log_path\": \"/root/autodl-tmp/analysis/cka_same_seed/run.log\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5648}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-25T05:04:14.072462+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "cka_same_seed_4cond",
  "field": "status",
  "value": "DONE",
  "project": "occsafe_vla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "cka_same_seed_4cond",
    "field": "status",
    "value": "DONE",
    "project": "occsafe_vla"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-25T05:04:14.072789+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"cka_same_seed_4cond\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:01:59.870Z\", \"updated_at\": \"2026-05-25T05:03:39.860Z\", \"hypothesis\": \"Same-seed (seed=42) CKA analysis of 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained. Controls for seed to isolate normalization and gradient flow effects on representation preservation. Complements cross-seed CKA results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/occsafe_vla/analysis/cka_analysis.py --pretrained_path /root/autodl-tmp/models/openvla-7b --checkpoint_paths /root/autodl-tmp/checkpoints/vanilla_retrain_s0/... /root/autodl-tmp/checkpoints/full_occ_retrain_s0/... /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/... /root/autodl-tmp/checkpoints/full_occ_ln_s0/... --condition_names Vanilla 'Full OCC (BN)' 'Detach+BN' 'Full OCC (LN)' --output_dir /root/autodl-tmp/analysis/cka_same_seed --gpu 0 --num_samples 200\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/libero_datasets/libero_spatial\", \"data_count\": 200, \"model_name\": \"openvla-7b\", \"seed\": 42}, \"metrics\": {\"Vanilla\": {\"dinov2_mean_cka\": 0.9676, \"dinov2_min_cka\": 0.8993, \"siglip_mean_cka\": 0.953, \"siglip_min_cka\": 0.8425}, \"Full OCC (BN)\": {\"dinov2_mean_cka\": 0.9594, \"dinov2_min_cka\": 0.8422, \"siglip_mean_cka\": 0.9593, \"siglip_min_cka\": 0.8799}, \"Detach+BN\": {\"dinov2_mean_cka\": 0.9635, \"dinov2_min_cka\": 0.8895, \"siglip_mean_cka\": 0.9532, \"siglip_min_cka\": 0.8292}, \"Full OCC (LN)\": {\"dinov2_mean_cka\": 0.6404, \"dinov2_min_cka\": 0.2558, \"siglip_mean_cka\": 0.9497, \"siglip_min_cka\": 0.8479}}, \"checkpoint_path\": \"/root/autodl-tmp/analysis/cka_same_seed\", \"log_path\": \"/root/autodl-tmp/analysis/cka_same_seed/run.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T05:03:39.860Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-25T05:04:14.073063+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Same-Seed 4-Condition Analysis",
  "type": "chart",
  "description": "CKA similarity plots (DINOv2 + SigLIP) for 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained, all seed=42",
  "project": "occsafe_vla",
  "exp_id": "cka_same_seed_4cond",
  "source_path": "/root/autodl-tmp/analysis/cka_same_seed/cka_analysis.pdf",
  "tags": "['cka', 'same-seed', 'vision-encoder', 'representation-analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Same-Seed 4-Condition Analysis",
    "type": "chart",
    "description": "CKA similarity plots (DINOv2 + SigLIP) for 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained, all seed=42",
    "project": "occsafe_vla",
    "exp_id": "cka_same_seed_4cond",
    "source_path": "/root/autodl-tmp/analysis/cka_same_seed/cka_analysis.pdf",
    "tags": "['cka', 'same-seed', 'vision-encoder', 'representation-analysis']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-25T05:04:14.073286+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/analysis/cka_same_seed/cka_analysis.pdf\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-25T05:04:14.073493+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Same-Seed Results JSON",
  "type": "data",
  "description": "Per-layer CKA values for 4 conditions vs pretrained (seed=42), JSON format",
  "project": "occsafe_vla",
  "exp_id": "cka_same_seed_4cond",
  "source_path": "/root/autodl-tmp/analysis/cka_same_seed/cka_results.json",
  "tags": "['cka', 'same-seed', 'data']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Same-Seed Results JSON",
    "type": "data",
    "description": "Per-layer CKA values for 4 conditions vs pretrained (seed=42), JSON format",
    "project": "occsafe_vla",
    "exp_id": "cka_same_seed_4cond",
    "source_path": "/root/autodl-tmp/analysis/cka_same_seed/cka_results.json",
    "tags": "['cka', 'same-seed', 'data']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-25T05:04:14.073732+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/analysis/cka_same_seed/cka_results.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-25T05:04:14.073994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-10894",
  "command": "cat /root/autodl-tmp/analysis/cka_same_seed/cka_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-10894",
    "command": "cat /root/autodl-tmp/analysis/cka_same_seed/cka_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-25T05:04:14.074436+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Vanilla\\\": {\\n    \\\"dinov2.block.0\\\": 0.989965,\\n    \\\"dinov2.block.1\\\": 0.899322,\\n    \\\"dinov2.block.2\\\": 0.930596,\\n    \\\"dinov2.block.3\\\": 0.962441,\\n    \\\"dinov2.block.4\\\": 0.967445,\\n    \\\"dinov2.block.5\\\": 0.982936,\\n    \\\"dinov2.block.6\\\": 0.980496,\\n    \\\"dinov2.block.7\\\": 0.981951,\\n    \\\"dinov2.block.8\\\": 0.967395,\\n    \\\"dinov2.block.9\\\": 0.971888,\\n    \\\"dinov2.block.10\\\": 0.98459,\\n    \\\"dinov2.block.11\\\": 0.984193,\\n    \\\"dinov2.block.12\\\": 0.98743,\\n    \\\"dinov2.block.13\\\": 0.987309,\\n    \\\"dinov2.block.14\\\": 0.984249,\\n    \\\"dinov2.block.15\\\": 0.980123,\\n    \\\"dinov2.block.16\\\": 0.972966,\\n    \\\"dinov2.block.17\\\": 0.965508,\\n    \\\"dinov2.block.18\\\": 0.968179,\\n    \\\"dinov2.block.19\\\": 0.968574,\\n    \\\"dinov2.block.20\\\": 0.962056,\\n    \\\"dinov2.block.21\\\": 0.9603,\\n    \\\"dinov2.block.22\\\": 0.945481,\\n    \\\"dinov2.block.23\\\": 0.937465,\\n    \\\"siglip.block.0\\\": 0.924229,\\n    \\\"siglip.block.1\\\": 0.952941,\\n    \\\"siglip.block.2\\\": 0.982861,\\n    \\\"siglip.block.3\\\": 0.984511,\\n    \\\"siglip.block.4\\\": 0.9831,\\n    \\\"siglip.block.5\\\": 0.96701,\\n    \\\"siglip.block.6\\\": 0.970062,\\n    \\\"siglip.block.7\\\": 0.978567,\\n    \\\"siglip.block.8\\\": 0.977089,\\n    \\\"siglip.block.9\\\": 0.97818,\\n    \\\"siglip.block.10\\\": 0.979363,\\n    \\\"siglip.block.11\\\": 0.975534,\\n    \\\"siglip.block.12\\\": 0.976823,\\n    \\\"siglip.block.13\\\": 0.974918,\\n    \\\"siglip.block.14\\\": 0.976313,\\n    \\\"siglip.block.15\\\": 0.968826,\\n    \\\"siglip.block.16\\\": 0.958716,\\n    \\\"siglip.block.17\\\": 0.951912,\\n    \\\"siglip.block.18\\\": 0.949991,\\n    \\\"siglip.block.19\\\": 0.938536,\\n    \\\"siglip.block.20\\\": 0.935572,\\n    \\\"siglip.block.21\\\": 0.932642,\\n    \\\"siglip.block.22\\\": 0.931993,\\n    \\\"siglip.blo
…[truncated 6557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-25T05:04:14.074746+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "CKA Same-Seed 4-Condition Analysis",
  "type": "data",
  "description": "Per-layer CKA values for 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained, all seed=42. Remote: /root/autodl-tmp/analysis/cka_same_seed/ on westd-10894",
  "project": "occsafe_vla",
  "exp_id": "cka_same_seed_4cond",
  "content": "Remote server: westd-10894\nOutput directory: /root/autodl-tmp/analysis/cka_same_seed/\nFiles: cka_results.json, cka_analysis.pdf, cka_analysis.png, run.log",
  "content_filename": "cka_same_seed_4cond_info.txt",
  "tags": "['cka', 'same-seed', 'vision-encoder', 'representation-analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "CKA Same-Seed 4-Condition Analysis",
    "type": "data",
    "description": "Per-layer CKA values for 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained, all seed=42. Remote: /root/autodl-tmp/analysis/cka_same_seed/ on westd-10894",
    "project": "occsafe_vla",
    "exp_id": "cka_same_seed_4cond",
    "content": "Remote server: westd-10894\nOutput directory: /root/autodl-tmp/analysis/cka_same_seed/\nFiles: cka_results.json, cka_analysis.pdf, cka_analysis.png, run.log",
    "content_filename": "cka_same_seed_4cond_info.txt",
    "tags": "['cka', 'same-seed', 'vision-encoder', 'representation-analysis']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-25T05:04:14.075003+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_b5f8a1\", \"name\": \"CKA Same-Seed 4-Condition Analysis\", \"type\": \"data\", \"description\": \"Per-layer CKA values for 4 conditions (Vanilla, Full OCC BN, Detach+BN, Full OCC LN) vs pretrained, all seed=42. Remote: /root/autodl-tmp/analysis/cka_same_seed/ on westd-10894\", \"path\": \"projects/occsafe_vla/artifacts/cka_same_seed_4cond/data/cka_same_seed_4cond_info.txt\", \"url\": null, \"project\": \"occsafe_vla\", \"exp_id\": \"cka_same_seed_4cond\", \"skill\": \"\", \"created_at\": \"2026-05-25T05:04:00.887199+00:00\", \"tags\": [\"cka\", \"same-seed\", \"vision-encoder\", \"representation-analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-25T05:04:14.075284+00:00_

CKA 分析完成。实验 `cka_same_seed_4cond` 已注册为 DONE。

## Same-Seed CKA 结果（seed=42, 200 samples, vs pretrained）

| Condition | DINOv2 mean CKA | DINOv2 min CKA | SigLIP mean CKA | SigLIP min CKA |
|---|---|---|---|---|
| **Vanilla** | 0.9676 | 0.8993 | 0.9530 | 0.8425 |
| **Full OCC (BN)** | 0.9594 | 0.8422 | 0.9593 | 0.8799 |
| **Detach+BN** | 0.9635 | 0.8895 | 0.9532 | 0.8292 |
| **Full OCC (LN)** | **0.6404** | **0.2558** | 0.9497 | 0.8479 |

关键发现：
- **Full OCC (LN) 严重破坏 DINOv2 表征**：mean CKA 仅 0.64（其余三个 >0.95），最低 block 降至 0.26（block 23）。早期 block 2-3 也仅 ~0.31。
- **SigLIP 全部条件均保持良好**（mean ~0.95），LN 对 SigLIP 无显著影响。
- **Vanilla / Full OCC (BN) / Detach+BN 三者 DINOv2 CKA 接近**（0.96-0.97），说明 BN 和梯度 detach 均能有效保护 DINOv2 表征。
- LN 的破坏具有选择性：只影响 DINOv2，不影响 SigLIP，说明 LN 归一化统计量与 DINOv2 的 pre-norm 结构存在冲突。

产出位于 `westd-10894:/root/autodl-tmp/analysis/cka_same_seed/`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_same_seed_cka_4cond_20260525T050056"
}
```

</details>

---
