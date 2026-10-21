# submit eval object bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-object-bjb2-28827_20260515T025311_result.json`
- **Structured JSON:** [`788abf58a00be1a5cc88.json`](../../sessions/78/788abf58a00be1a5cc88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 Results

- **SmolVLA fine-tuned model**: READY (`/root/autodl-tmp/models/smolvla_libero/model.safetensors`)
- **SmolVLM2 backbone (HuggingFaceTB/SmolVLM2-500M-Video-Instruct)**: **NOT READY** — HF cache 有 8 个 `.incomplete` blob 文件，下载中断，无进程在继续下载
- **CRM checkpoints**: READY (obs_only + scalar_unc)
- **Code**: READY (`evaluate.py` 含 `max_correction_norm` 参数)
- **eval-vla-only-object**: FAILED — backbone 权重缺失 (`OSError: model.safetensors not found`)
- **eval-acr-object-v4-obs-only-b2**: FAILED — 同上
- **eval-acr-object-v4-scalar-b2**: FAILED — 同上
- **Remaining idle GPUs**: cuda:0-5（全部空闲）

### BLOCKER

`SmolVLM2-500M-Video-Instruct` backbone 下载未完成（8 个 incomplete blobs），`HF_HUB_OFFLINE=1` 阻止在线下载。需要：
1. 先完成 backbone 下载（去掉 `HF_HUB_OFFLINE=1`，或在线环境运行 `huggingface-cli download HuggingFaceTB/SmolVLM2-500M-Video-Instruct --cache-dir /root/autodl-tmp/.hf_cache`）
2. 下载完成后重新启动 eval

按任务指示，不自行下载，等待 Director 指示。

---
