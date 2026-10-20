# diagnose westd 34685 batch failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-34685-batch-failure_20260522T072750_result.json`
- **Structured JSON:** [`a382710983816b10b193.json`](../../sessions/a3/a382710983816b10b193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**根因**：`/root/autodl-tmp` 磁盘 100% 满（350G/350G，仅剩 300K）。checkpoints 目录占 329G。三个实验在保存 checkpoint 时同时触发 `No space left on device (os error 28)`：
- `depth_s0`/`depth_s1`：step 15000 保存 merged model 时失败
- `cutoff_s1`：step 2500 保存 merged model 时失败

具体崩溃位置：`finetune.py:731` → `save_training_checkpoint` → `merged_vla.save_pretrained` → safetensors 序列化写盘失败。

**cutoff_s0 状态**：仍在 GPU 0 运行（step ~2805），但它下一次保存 checkpoint（step 5000）时也会因磁盘满而崩溃。

**影响范围**：4 个实验全部受影响（3 已死，1 即将死）。

**可以直接重跑**：不是代码 bug，是磁盘空间不足。需要先清理 `/root/autodl-tmp/checkpoints/` 下的旧 checkpoint（如之前的 occ_s0/s1/s2 实验数据），释放空间后重跑。depth_s0/s1 可从 step 12500 checkpoint 恢复（最后成功保存的），cutoff_s1 需从头跑。

---
