# diagnose sweep isr b005 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sweep-isr-b005-s43_20260517T084958_result.json`
- **Structured JSON:** [`8bbdebd4780c6f587a6e.json`](../../sessions/8b/8bbdebd4780c6f587a6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因：磁盘满（C003 再犯）

`/dev/md0` → `/root/autodl-tmp` **250G/250G，剩 28K，100% 满**。

两个实验都在 step 50 首次保存 checkpoint 时崩溃，错误完全相同：
```
safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)
```

调用链：`trainer.train()` → `_save_checkpoint` → `save_pretrained` → `safe_save_file`

### 磁盘占用分析

`/root/autodl-tmp/outputs/` 占 **211G**，主要被 7 个 ~31G 的旧 checkpoint 目录占满：

| 目录 | 大小 |
|------|------|
| plan001_exec_only_s43_1000_r2 | 31G |
| plan001_exec_only_s46 | 31G |
| plan002_additive_b01_s45 | 31G |
| plan002_additive_b01_s46 | 31G |
| plan018_random_b01_s45 | 31G |
| plan018_random_b01_s46 | 31G |
| sweep_random_b005_s42 | 31G |

加上 models/ 36G，总计 ~253G 超出 250G 容量。

### 结论

- **同一原因**：两个实验因同一块磁盘满而失败
- **非 code bug**：资源不足，可重试
- **前提**：必须先清理旧 checkpoint 释放空间（清理 2 个 31G 目录即可腾出 ~62G）
- **注意 C010/C011 约束**：清理前需交叉检查 registry，不能删 `conclusion=success` 且标记 `needs-re-eval` 的 checkpoint

需要我检查 registry 状态并制定安全的清理方案吗？

---
