# infra westd30476 emergency cleanup and resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd30476_emergency_cleanup_and_resubmit_20260520T051622_result.json`
- **Structured JSON:** [`9caa9a9322947821dcbd.json`](../../sessions/9c/9caa9a9322947821dcbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Kill 结果
- 原始 8 个 orphan PID (190057, 190462, 191125, 191693, 190854-190857): **全部已杀死**
- 额外发现 GPU 2/3 上 2 个新 OOD eval 进程 (197197, 197280): **也已杀死**

### 2. GPU 四卡状态（清理后）

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 57807 / 97887 MiB | 99% | uniform_1_7b_seed42_v3 (PID 191550) |
| 1 | 57807 / 97887 MiB | 93% | adaptive_1_7b_seed42_v3 (PID 193988) |
| 2 | 0 / 97887 MiB | 0% | **空闲** |
| 3 | 0 / 97887 MiB | 0% | **空闲** |

### 3. adaptive_1_7b_seed42_v3: **ALIVE** (PID 193983/193988)
- Step 377/6103 (~6%), 2.98s/it, 已跑 ~22 min

### 4. uniform_1_7b_seed42_v3: **ALIVE** (PID 191545/191550)
- Step 419/6103 (~7%), 2.87s/it, 已跑 ~25 min

### 5. GPU 2/3 完全释放，可用于新任务

---
