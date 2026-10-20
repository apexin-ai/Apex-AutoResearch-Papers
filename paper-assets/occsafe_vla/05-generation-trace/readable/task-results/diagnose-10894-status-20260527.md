# diagnose 10894 status 20260527

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894_status_20260527_20260527T102938_result.json`
- **Structured JSON:** [`669af06fe43d9fd54b8f.json`](../../sessions/66/669af06fe43d9fd54b8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10894 诊断结果 (2026-05-27 ~18:30 UTC)

### GPU 状态 — 4 张全满
| GPU | 利用率 | 实验 | PID | Step | 预计完成 |
|-----|--------|------|-----|------|----------|
| cuda:0 | 67% | full_occ_ln_v2_s1c_r2 | 481426 | 33835/50005 (68%) | ~22:50 UTC |
| cuda:1 | 99% | full_occ_ln_v2_s2_r2 | 481643 | 33974/50005 (68%) | ~22:40 UTC |
| cuda:2 | 99% | detach_ln_v2_s0c_r3 | **543255** | 5421/50005 (11%) | ~06:00 May 28 |
| cuda:3 | 82% | **full_occ_ln_s4** (新!) | 553813 | 3534/50005 (7%) | ~06:40 May 28 |

### 关键发现
- **cuda:3 不是空闲的** — full_occ_ln_s4（seed=46, occ_detach=false）于 ~17:13 UTC 被启动
- **full_occ_ln_v2_s0d 失败原因**：磁盘满 (os error 28)，step 20000 checkpoint 保存时 `backend_tokenizer.save()` 失败
- **磁盘已恢复**：/root/autodl-tmp 从 100% 降到 45%（139G 可用），checkpoints 总计 90G。空间充足
- **所有 4 个实验均在 DDL (May 28 12:00 UTC) 前完成**

---
