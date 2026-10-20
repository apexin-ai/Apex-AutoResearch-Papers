# diagnose sweep random b005 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sweep-random-b005-s43_20260517T084554_result.json`
- **Structured JSON:** [`bc4eb2df2aa663ca8552.json`](../../sessions/bc/bc4eb2df2aa663ca8552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

问题很清楚了。磁盘 250G/250G 已满。有多个 31G 的旧实验目录占满了空间。

## 诊断报告

### 根因

**磁盘满 (No space left on device)**。Step 50 保存 checkpoint 时触发：

```
safetensors_rust.SafetensorError: Error while serializing: 
I/O error: No space left on device (os error 28)
```

磁盘状态：`/dev/md0 250G 250G 3.1M 100%`

### 训练进度

- 跑了 **50/500 steps**（10%），在 step 50 首次保存 checkpoint 时崩溃
- `checkpoint-50/` 目录存在但只有 53M（不完整，正常应 ~16G）
- `reward_log.jsonl` 已记录 50 步数据

### 是否可重试

**Deterministic failure**——不清磁盘就必然再次失败。

### 磁盘占用分析

`/root/autodl-tmp/outputs/` 共 211G，其中 6 个旧实验各占 ~31G：

| 目录 | 大小 |
|------|------|
| `plan001_exec_only_s43_1000_r2` | 31G |
| `plan001_exec_only_s46` | 31G |
| `plan002_additive_b01_s45` | 31G |
| `plan002_additive_b01_s46` | 31G |
| `plan018_random_b01_s45` | 31G |
| `plan018_random_b01_s46` | 31G |
| `sweep_random_b005_s42` | 31G |

### 修复建议

1. **清理不再需要的旧实验目录**。上述 6 个 31G 目录（plan001/plan002/plan018 系列）如果已完成评估且不再需要 checkpoint，可以释放 ~186G。**清理前必须遵守 C010/C011 约束**：检查 registry 中这些实验是否标记为 `needs-re-eval`，确认后再删除。
2. 删除失败的 `sweep_random_b005_s43/checkpoint-50/`（不完整，53M，无用）。
3. 清理后重跑同一命令即可，配置本身没有问题（同配置 s42 成功完成了 500 步）。

---
