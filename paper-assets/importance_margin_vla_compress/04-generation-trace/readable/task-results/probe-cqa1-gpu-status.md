# probe cqa1 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_cqa1-gpu-status_20260521T224115_result.json`
- **Structured JSON:** [`cfbe4291cd62d2add032.json`](../../sessions/cf/cfbe4291cd62d2add032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报 — cqa1-33015

| GPU | 状态 | PID | 实验 | 运行时间 | 显存 |
|-----|------|-----|------|----------|------|
| **GPU0** | 占用 | 719440 | `random k=0.85 object seed43` | 39min | 10243/24564 MiB |
| **GPU1** | 占用 | 725484 | `l2norm k=0.3 object seed43` | 33min | 10115/24564 MiB |
| **GPU2** | 占用 | 716056 | `l2norm k=0.85 object seed42` | 45min | 10243/24564 MiB |
| **GPU3** | 占用 | 716134 | `random k=0.3 object seed43` | 45min | 10115/24564 MiB |

**空闲 GPU：0 个，全部占满。**

关注项：
- **GPU0**: `eval_pi05_random_k085_object_seed43` (PID 719440) — 活着，运行 ~40min
- **GPU1**: 之前 L2norm k=0.7 seed43 部署失败后，GPU1 现被 **l2norm k=0.3 seed43** (PID 725484) 占用，运行 ~33min。**不空闲**
- **GPU2**: `eval_pi05_l2norm_k085_object_seed42` (PID 716056) — 活着，~45min
- **GPU3**: `eval_pi05_random_k03_object_seed43` (PID 716134) — 活着，~45min
- **eval_smolvla_official_l2norm_k090_object_seed42** — 未在运行
- **eval_smart_compress_m32_official** — 未在运行

---
