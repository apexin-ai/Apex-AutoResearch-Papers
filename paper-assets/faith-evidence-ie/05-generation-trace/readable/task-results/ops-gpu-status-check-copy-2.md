# ops gpu status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260519T165157_result.json`
- **Structured JSON:** [`224aea8a8eedb1ca053d.json`](../../sessions/22/224aea8a8eedb1ca053d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 显存占用 | 利用率 | 实验 | 状态 | 详情 |
|-----|---------|--------|------|------|------|
| **cuda:0** | 18943/32607 MiB | 62% | 8B RSFT no-evidence eval r2 (PID 698772) | **RUNNING** | 228/247 batches (~92%), 运行 ~2h57m |
| **cuda:1** | 10887/32607 MiB | 48% | d112 no-evidence eval r3 (PID 706326) | **RUNNING** | 108/247 batches (~44%), 运行 ~1h05m |
| **cuda:2** | 0/32607 MiB | 0% | D112 bf16 eval (PID 693535) | **COMPLETED** | 进程已退出，EXIT_CODE=0 |
| **cuda:3** | 6635/32607 MiB | 48% | 1.7B no-evidence eval 2048 (PID 702837) | **RUNNING** | 93/247 batches (~38%), 运行 ~2h02m |

### D112 bf16 eval 结果 (COMPLETED)

```
F1:              0.5274
Ign-F1:          0.5152
Evi-F1(DREEAM):  0.4277
Evi-F1(TP):      0.8175
EDCR:            0.5987
Format OK:       984/985 (99.9%)
Truncated:       182/985
Predictions:     15050
```

### 预计剩余时间

- **8B no-evidence (cuda:0)**: ~19 batches 剩余，约 15-16 分钟完成
- **d112 no-evidence (cuda:1)**: ~139 batches 剩余，约 1h30m-1h40m
- **1.7B 2048 (cuda:3)**: ~154 batches 剩余，约 3h20m（~80s/batch，速度较慢）

---
