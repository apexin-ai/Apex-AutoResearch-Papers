# diagnose bjb1 32546 gpu conflict

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-gpu-conflict_20260521T025803_result.json`
- **Structured JSON:** [`e27cf9d6dae6dd4b199c.json`](../../sessions/e2/e27cf9d6dae6dd4b199c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 实时状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| **0** | 2009MiB | 31% | PID 731912 — norm01-seed51-r3 **仍在运行** (2h19m) |
| **1** | 2MiB | 0% | **空闲** |
| **2** | 5268MiB | 35% | PID 805840 — **不在列表中的新实验** norm005-seed67 (运行 13min) |
| **3** | 2MiB | 0% | **空闲** |
| **4** | 2MiB | 0% | **空闲** |
| **5** | 2MiB | 0% | **空闲** |

### 第一批（00:30 提交）— 全部完成 ✅

| 实验 | GPU | PID | SR |
|------|-----|-----|-----|
| norm003-seed64 | cuda:0 | 723784 (dead) | **0.17** |
| norm003-seed65 | cuda:1 | 725722 (dead) | **0.17** |
| norm01-seed64 | cuda:3 | 726800 (dead) | **0.15** |
| norm01-seed65 | cuda:4 | 728057 (dead) | **0.15** |
| norm005-seed64 | cuda:5 | 729873 (dead) | **0.15** |

### 第二批（00:41 提交）

| 实验 | GPU | PID | 状态 | SR |
|------|-----|-----|------|-----|
| norm01-seed51-r3 | cuda:0 | 731912 | 🔄 **仍在运行** (2h19m) | — |
| norm01-seed52-r3 | cuda:1 | 733203 (dead) | ✅ 完成 | **0.15** |
| norm003-seed62-r2 | cuda:3 | 734631 (dead) | ❌ **失败**（无输出 JSON） | — |
| norm003-seed63-r2 | cuda:4 | 735998 (dead) | ❌ **失败**（无输出 JSON） | — |

### 关键发现

1. **无 GPU 冲突**：第一批 5 个实验已全部跑完释放了 GPU，第二批启动时实际没有冲突（或冲突导致第二批两个失败）
2. **2 个实验失败**：norm003-seed62-r2 和 norm003-seed63-r2，PID 已死且无输出 JSON，需要重跑
3. **cuda:2 不空闲**：有一个不在列表中的新实验 PID 805840 正在跑（norm005-seed67），13 分钟前启动
4. **可用 GPU**：cuda:1, cuda:3, cuda:4, cuda:5 空闲可用

---
