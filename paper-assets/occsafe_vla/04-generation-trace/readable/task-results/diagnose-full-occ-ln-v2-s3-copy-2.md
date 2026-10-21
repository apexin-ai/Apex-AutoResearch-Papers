# diagnose full occ ln v2 s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_v2_s3_20260528T034253_result.json`
- **Structured JSON:** [`6d3ca4d30a9b9c7a7d53.json`](../../sessions/6d/6d3ca4d30a9b9c7a7d53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，结果已写入 memory.md。

### full_occ_ln_v2_s3 失败诊断摘要

| 项目 | 结论 |
|------|------|
| **根因** | `FileNotFoundError`，**非 SIGHUP/OOM**。基础模型目录 `model.safetensors.index.json` 被污染：引用 4-shard 命名但实际文件是 3-shard。Step 40000 保存 checkpoint 时 `from_pretrained` 加载基础模型失败 |
| **污染原因** | `save_training_checkpoint` bug — 合并 LoRA 后将 merged model 的 index.json 回写到共享基础模型目录 |
| **最新完整 checkpoint** | **step 35000**（有 merged model + LoRA adapter + all heads） |
| **40000 checkpoint** | 不完整（仅 lora_adapter + head weights，~370MB，无 merged model） |
| **cuda:2 状态** | 空闲（3 MiB，0%） |
| **可否 resume** | 可以（非 cutoff 实验，C002 不适用） |
| **时间预估** | 从 35000 resume ~3.9h，从 40000 resume ~2.6h（若 resume 支持从 LoRA adapter 恢复） |
| **DDL 影响** | **无法在 12:00 UTC 前完成**，超时 ~2.6-3.9h |

### 修复前提（resume 前必须做）
1. **恢复 `/root/autodl-tmp/models/openvla-7b/model.safetensors.index.json`** 为 3-shard 命名，否则所有实验后续 checkpoint save 都会重复崩溃
2. 同时检查 `config.json` 是否需还原（也在 11:30 被修改）

---
