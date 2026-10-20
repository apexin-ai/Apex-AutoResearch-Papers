# diagnose plan018 s43 failure

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan018-s43-failure_20260514T113407_result.json`
- **Structured JSON:** [`7d57a44b1e78037974b8.json`](../../sessions/7d/7d57a44b1e78037974b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**1. 错误信息：**
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

**2. 失败位置：** Step 200/500，在保存 checkpoint-200 时崩溃。checkpoint-200 只写了 3.5G（正常应 ~15G），写入中途磁盘耗尽。

**3. 根因：** `/root/autodl-tmp/` 磁盘 250G/250G 已满（100%）。各目录占用：

| 目录 | 大小 |
|------|------|
| plan002_additive_b01_s43 | 31G |
| plan002_additive_b01_s44 | 31G |
| plan006_prolog_exec_s42 | 31G |
| plan006_prolog_sta_s42 | 31G |
| plan016_extended_1000_s42 | 31G |
| plan018_additive_random_b01_s42 | 31G |
| plan002_additive_b01_s42 | 16G |
| plan018_additive_random_b01_s43 | 19G |
| plan001_exec_only_s42 | 15G |
| 其他 | ~0 |
| **合计** | **~236G** |

旧实验输出占满了磁盘。尽管 `save_total_limit=1` 限制了单次实验的 checkpoint 数量，但多个已完成实验的 checkpoint 未清理。

**4. 结论：** 这是可重试的瞬态错误，不需要代码修复。清理不再需要的旧实验 output 目录后重跑即可。建议：
- 确认哪些旧实验结果已归档/评估完毕，删除对应的 checkpoint 目录（每个 31G 的目录删一两个就够）
- 删除当前失败 run 的不完整 checkpoint-200（3.5G，不可用）
- 重跑 plan018-additive-random-b01-s43

---
