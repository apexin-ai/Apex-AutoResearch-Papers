# audit westd38929 full

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd38929_full_20260522T200519_result.json`
- **Structured JSON:** [`45d957eb4028517af377.json`](../../sessions/45/45d957eb4028517af377.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 审计报告

### 四卡状态表

| GPU | VRAM | Util | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 10454 MiB | 37% | 989045 | π0.5 Random k=0.9 Long seed42 (Task 2/10, ~30% SR) |
| 1 | 10464 MiB | 11% | 892027 | π0.5 L2norm k=0.7 Long seed42 (运行中) |
| 2 | 10532 MiB | 5% | 960809 | π0.5 Random k=0.85 Goal seed42 v3 (Task 9/10, ~56% SR, 即将完成) |
| 3 | 10670 MiB | 16% | 59239 | **新部署** π0.5 Random k=0.5 Long seed42 ✅ |

### 新部署

- **GPU 3**: 优先队列 #1 — `eval_pi05_random_k05_long_seed42` (Random k=0.5, libero_10, seed42)
- VRAM 已确认 10670 MiB，模型加载完成
- 已注册 registry

### 收割结果

以下为本服务器已完成的 π0.5 实验（eval_results/ 中有 JSON）：

| 实验 | Suite | Mode | k | SR |
|------|-------|------|---|-----|
| Baseline | Goal | none | 1.0 | **96.4%** |
| Baseline | Long | none | 1.0 | **92.8%** |
| L2norm k=0.95 | Long | l2norm | 0.95 | **86.8%** |
| L2norm k=0.85 | Long | l2norm | 0.85 | **78.0%** |
| Random k=0.95 | Long | random | 0.95 | **61.2%** |
| L2norm k=0.9 | Goal | l2norm | 0.9 | **90.0%** |
| Random k=0.9 | Goal | random | 0.9 | **62.6%** |
| L2norm k=0.7 | Spatial | l2norm | 0.7 | **67.0%** |

### 注意事项

- 6 个旧日志（`_s42` 后缀）全部因 `IndexError: index 50 out of bounds` 在 Task 0 后崩溃，已修复的新代码正常运行
- 无空闲卡剩余，优先队列 #2-4 等待当前实验完成后部署

---
