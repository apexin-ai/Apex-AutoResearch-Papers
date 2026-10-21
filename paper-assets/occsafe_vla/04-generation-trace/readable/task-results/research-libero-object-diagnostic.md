# research libero object diagnostic

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero_object_diagnostic_20260528T044203_result.json`
- **Structured JSON:** [`5568c9b229e8f6fcd6ec.json`](../../sessions/55/5568c9b229e8f6fcd6ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. LIBERO-Object 训练数据

| 服务器 | 状态 | 详情 |
|--------|------|------|
| westd-10894 | ✅ 存在 | 32 tfrecord shards + 3 metadata files |
| westd-34685 | ✅ 存在 | 同上，完全一致 |

### 2. OCC Labels

**两台服务器均无 OCC labels。** `find` 在 `libero_object_no_noops/` 下未找到任何 `*occ*` 或 `*occupancy*` 文件。

→ **只能跑 `vanilla_object`**（`--use_occ_head False`）。`full_occ_bn_object` 和 `detach_bn_object` 无法产出有意义结果（无标签，occ_loss=0 或报错）。

### 3. 可 Resume 的 Checkpoint

| 实验 | 服务器 | 最新可用 checkpoint | 完整性 |
|------|--------|-------------------|--------|
| **vanilla_object_s0** | westd-34685 | **20000 step** | ✅ 完整（4 model shards + action_head + proprio_projector + lora_adapter） |
| vanilla_object_s0 | westd-34685 | 25000 step | ❌ 不完整（无 model shards，kill 时正在写） |
| **vanilla_object_s1** | westd-10894 | **40000 step** | ✅ 完整（4 model shards + action_head + proprio_projector + lora_adapter） |
| vanilla_object_s1 | westd-10894 | 35000 step | ✅ 完整 |
| full_occ_bn_object_s0 | westd-10894 | 5000 step | ❌ 不完整（model-00003 仅 24KB，model-00004 缺失）+ **无 OCC labels，无意义** |
| detach_bn_object_s0 | westd-10894 | 5000 step | ❌ 不完整（model-00001 仅 4GB partial，02/03/04 缺失）+ **无 OCC labels，无意义** |
| vanilla_object_s0 | westd-10894 | — | 无 checkpoint 目录 |
| vanilla_object_s1 | westd-34685 | — | 无 checkpoint 目录 |

### 4. 结论

**关键阻断：LIBERO-Object 没有 OCC labels。** 跨 benchmark 实验中，OCC 相关实验（full_occ、detach）不可行。

**可执行的方案：**
- **vanilla_object_s1**：在 westd-10894 从 step 40000 resume（假设目标 ~50k steps，还需约 10k steps）
- **vanilla_object_s0**：在 westd-34685 从 step 20000 resume（还需约 30k steps）
- full_occ / detach 实验：需先生成 LIBERO-Object 的 OCC labels 才可行，时间上可能来不及（C003 deadline: 今天 20:00 北京时间）

---
