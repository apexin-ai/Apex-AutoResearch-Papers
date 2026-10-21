# ops emergency disk cleanup 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_35807_20260523T061808_result.json`
- **Structured JSON:** [`e3fd6ca38db857cb5e30.json`](../../sessions/e3/e3fd6ca38db857cb5e30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**Step 1 — 磁盘清理 ✅**：删除 baseline_object_pudding (76GB) + baseline_spatial_bowl (76GB)，可用空间从 54GB → **204GB**。

**Step 2 — 训练健康检查**：
- 4 个训练进程全部存活，step ~6850-6868，速度 1.20 s/it
- GPU 利用率 100%，loss 正常下降

**🔴 异常：Phase 2 转换未生效。** 4 个 GPU 均为 19GB（Phase 1），而非预期的 ~27GB（Phase 2）。Resume 从 step 6000 开始，跳过了 step 5000 的 Phase 2 触发点。当前仅 SDF decoder + EE extractor (~660K 参数) 在训练，33.47M LoRA 参数仍冻结 — **主策略网络没有在 fine-tune**。

**建议 P0 操作**：修复 Phase 2 激活逻辑（`step >= phase1_warmup_steps` 而非 `==`），从 step 6000 checkpoint 重启。

---
