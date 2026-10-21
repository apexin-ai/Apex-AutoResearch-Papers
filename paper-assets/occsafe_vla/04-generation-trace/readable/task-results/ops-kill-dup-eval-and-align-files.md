# ops kill dup eval and align files

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-dup-eval-and-align-files_20260521T205703_result.json`
- **Structured JSON:** [`db0a468fad395795865c.json`](../../sessions/db/db0a468fad395795865c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 1. Kill 确认
- PID 937783/937784 (occ_s0 50K 50r on cuda:2) — **已杀**
- PID 939566/939567 (occ_s2 50K 50r on cuda:3) — **已杀**
- GPU 2/3 已释放（0%, 0 MiB）

### 2. Artifacts 源文件
- occ_s0 50K 50r → `artifacts/safelibero_libero_spatial_20260521_234842.json`
- occ_s2 50K 50r → `artifacts/safelibero_libero_spatial_20260522_002946.json`

### 3. eval_results/ 完整清单

| 文件 | rollouts/task | total_eps |
|------|:---:|:---:|
| `vanilla_s0_50r.json` | 50 | 500 |
| `vanilla_s1_50r.json` | 50 | 500 |
| `occ_s0_47500_50r.json` | 50 | 500 |
| `occ_s0_50000_50r.json` | 50 | 500 |
| `occ_s0_50000.json` | 20 | 200 |
| `occ_s0_final.json` | 20 | 200 |
| `occ_s2_47500_50r.json` | 50 | 500 |
| `occ_s2_50000_50r.json` | 50 | 500 |
| `occ_s2_50000.json` | 20 | 200 |
| `occ_s2_final.json` | 20 | 200 |

6 个 50r 文件齐全（vanilla_s0/s1, occ_s0/s2 47500, occ_s0/s2 50000）。另有 4 个 20r 文件（occ_s0/s2 的 50000 和 final）。

---
