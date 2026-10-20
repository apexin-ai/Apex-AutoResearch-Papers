# diagnose dev eval 4b rsft v2 cascade

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dev-eval-4b-rsft-v2-cascade_20260522T104633_result.json`
- **Structured JSON:** [`cf421d39a2ae4323e5d9.json`](../../sessions/cf/cf421d39a2ae4323e5d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**dev_eval_4b_rsft_ced_s42_v2** — 已完成 ✓
- **ign_f1 = 0.4388**（期望 0.4517，差 -1.29pp，在 ±2pp 范围内）
- evi_f1 = 0.8069, format_compliance = 100%, 143/985 truncated
- Registry 已更新为 DONE/success

**test_eval_4b_rsft_s42_v2_reeval** — 已提交 ✓
- PID: **176927**，运行在 **cuda:2**（13GB 已占用）
- 500 test documents, 推理进度 0/32 batches
- 预计运行 ~6 小时（参考 dev eval 985 docs 用了 ~6h）

**GPU 状态**：
| GPU | 显存占用 |
|-----|---------|
| 0 | 0 MiB / 97887 MiB (空闲) |
| 1 | 0 MiB / 97887 MiB (空闲) |
| 2 | 12989 MiB / 97887 MiB (test eval 运行中) |
| 3 | 0 MiB / 97887 MiB (空闲) |

---
