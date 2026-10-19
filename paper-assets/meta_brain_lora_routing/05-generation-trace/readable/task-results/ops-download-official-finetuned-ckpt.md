# ops download official finetuned ckpt

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_official_finetuned_ckpt_20260516T161001_result.json`
- **Structured JSON:** [`54b175928d8757e74b63.json`](../../sessions/54/54b175928d8757e74b63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**pi0_libero checkpoint 已经存在，无需下载。**

## 结果

| 项目 | 详情 |
|------|------|
| **状态** | 已存在（之前已下载成功） |
| **路径** | `/root/.cache/openpi/openpi-assets/checkpoints/pi0_libero/` |
| **大小** | 1.9 GB |
| **格式** | JAX/Orbax checkpoint（OCDBT 格式，非 safetensors） |
| **内容** | `params/` — 模型参数（Orbax OCDBT shards）&lt;br>`assets/physical-intelligence/libero/norm_stats.json` — 归一化统计 |
| **模型结构** | PaliGemma (img encoder + llm) + action heads (`action_in_proj`, `action_out_proj`, `action_time_mlp_in/out`, `state_proj`) |

这个 checkpoint 来源于 `gs://openpi-assets/checkpoints/pi0_libero`，是 openpi 框架的标准 fine-tuned checkpoint，可直接用 `openpi` 的 config `pi0_libero` 加载。

---
