# ssh gpu audit 35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-audit-35694_20260521T130954_result.json`
- **Structured JSON:** [`90ad78318c32da9ae28f.json`](../../sessions/90/90ad78318c32da9ae28f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成，报告已写入 `artifacts/gpu_audit_35694.md`。

**摘要：**

| GPU | 任务 | 进度 |
|-----|------|------|
| 0 | Llama clean s8 | 380/939 (40%), ~10min 后完成 |
| 1 | Llama clean s9 | 379/939 (40%), ~10min 后完成 |
| 2 | GRPO v3 | 469/3000 (15.6%), ETA ~2h25m |
| 3 | Llama clean s10 | 380/939 (40%), ~10min 后完成 |

- **旧进程全部已死**，无 zombie，无需 kill
- **Llama clean s2-s7**: 训练+eval 全部完成
- **Qwen s10**: 训练+eval 完成 (acc=0.676, lz*=8.15)
- **空闲 GPU**: 当前无，s8/s9/s10 完成后 GPU 0/1/3 将释放
- **磁盘充裕**: 根分区 5%，数据盘 34%

---
