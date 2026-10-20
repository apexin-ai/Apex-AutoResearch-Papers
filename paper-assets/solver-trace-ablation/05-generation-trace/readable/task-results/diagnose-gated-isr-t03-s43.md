# diagnose gated isr t03 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gated-isr-t03-s43_20260516T144126_result.json`
- **Structured JSON:** [`023870c3a1a510f1a45d.json`](../../sessions/02/023870c3a1a510f1a45d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根本原因：磁盘满 (No space left on device)

数据盘 `/root/autodl-tmp` **250G/250G 已满（100%）**，仅剩 1.5MB。

### 关键错误信息

**gated-isr-t03-s43**：在 step 100 checkpoint 保存时崩溃：
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

**gated-isr-t03-s42**：日志在 step 90 处截断，无 traceback——进程被磁盘满静默杀死（同一根因）。

### 磁盘占用分析

`/root/autodl-tmp/outputs/` 总计 **211GB**，主要大户：

| 目录 | 大小 | 说明 |
|------|------|------|
| `sweep_exec_only_s45` | 31G | 旧 sweep |
| `sweep_exec_only_s46` | 31G | 旧 sweep |
| `gated_isr_t03_s43` | 20G | 本次失败实验 |
| `gated_isr_t03_s42` | 15G | 本次失败实验 |
| `plan001_exec_only_s43_1000_r2` | 16G | |
| `plan001_exec_only_s44_1000_r2` | 16G | |
| `plan018_additive_random_b01_s44_r2` | 16G | |
| `sweep_isr_b02_*` (×3) | 48G | 旧 sweep |
| `w2_1.7b_*` (×2) | 26G | width 实验 |

这是 C003 约束（save_total_limit + 磁盘保护）的又一次违反。两个实验同时运行，各自保存 checkpoint（每个 ~15-20GB），叠加已有的 ~180GB 输出直接撑爆磁盘。

### 建议修复方案

1. **清理磁盘**：确认哪些旧实验的 checkpoint 可以删除（特别是 `sweep_exec_only_s45/s46` 共 62GB，如果已完成评估则可清理）
2. **重跑前**确保磁盘至少有 50GB 余量（两个实验各需 ~20GB checkpoint 空间）
3. **确认训练配置中 `save_total_limit=1`** 已生效，避免保留多份 checkpoint

---
