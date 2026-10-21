# diagnose object failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_object_failures_20260528T015248_result.json`
- **Structured JSON:** [`98bab16ba2ce2e2f84f9.json`](../../sessions/98/98bab16ba2ce2e2f84f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**诊断总结：**

| 实验 | 服务器 | 根因 | 训练进度 |
|------|--------|------|----------|
| detach_bn_object_s0 | westd-10894 | step 5000 checkpoint 损坏：只有 1/4 safetensors shard，缺 index 文件，`from_pretrained` 无法加载 | 0（启动即崩） |
| full_occ_bn_object_s0 | westd-10894 | 同上：3/4 shard 但缺 index 文件 | 0（启动即崩） |
| vanilla_object_s0 | westd-34685 | checkpoint 轮转在保存 20000 时删除了 10000_chkpt，保存 25000 时 `save_training_checkpoint` 试图从已删除的 10000_chkpt 加载 base model 失败 | ~4.2h，训练到 step ~25000 |

**共同根因**：finetune.py 的 checkpoint 管理有两个 bug——(1) safetensors 保存缺 index 文件导致不完整 checkpoint 不可恢复；(2) checkpoint 轮转删除了 `save_training_checkpoint` 依赖的 resume 源。

**修复路径**：
- westd-10894 两个实验：5000 checkpoint 已损坏，无法 resume，需从 pretrained 从头训练
- westd-34685 vanilla：可从 20000_chkpt resume，但需先修复 `save_training_checkpoint` 中 base_model_path 的硬编码问题

---
