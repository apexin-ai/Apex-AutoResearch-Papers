# ops audit westd41074 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd41074_v3_20260522T074046_result.json`
- **Structured JSON:** [`23b84875d18d63e46673.json`](../../sessions/23/23b84875d18d63e46673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

二次确认通过。两个 eval 都已占用 GPU 显存（各 10528 MiB）并开始推理。

---

## 审计结果

| GPU | PID | 进程状态 | 显存 | 实验 | 行动 |
|-----|-----|---------|------|------|------|
| 0 | ~~132954~~ → **273012** | ✅ 运行中 (2m) | 10528 MiB | eval_pi05_random_k05_spatial_seed43 | 新部署 |
| 1 | ~~121033/133121~~ → **273085** | ✅ 运行中 (2m) | 10528 MiB | eval_pi05_l2norm_k05_spatial_seed43 | 新部署 |
| 2 | 68539 | ✅ 运行中 (2d4h) | 28555 MiB | train_openvla_sc_m96_seed42 (91.7%, ~4.6h) | 保持 |
| 3 | 59671 | ✅ 运行中 (22h25m) | 27535 MiB | train_openvla_sc_m64_seed42_v6 (46.5%, ~24.8h) | 保持 |

**空闲 GPU**: 0, 1 → 已部署

**新部署**:
- `eval_pi05_random_k05_spatial_seed43` → GPU 0, PID 273012, 二次确认 ✅ (10528 MiB, pruning 128/256 tokens)
- `eval_pi05_l2norm_k05_spatial_seed43` → GPU 1, PID 273085, 二次确认 ✅ (10528 MiB, pruning 128/256 tokens)

**收割 metrics**:

| 实验 | Overall SR | Per-task SR (T0→T9) |
|------|-----------|---------------------|
| eval_pi05_l2norm_k0925_spatial_seed42 | **97.0%** | 100, 98, 98, 94, 92, 94, 100, 98, 100, 96 |
| eval_pi05_l2norm_k0925_spatial_seed43 | **97.0%** | 100, 98, 100, 98, 90, 94, 100, 94, 98, 98 |
| eval_pi05_random_k095_object_seed43 | **72.8%** | 70, 90, 78, 66, 54, 80, 82, 66, 78, 64 |

**待部署队列** (GPU 0/1 完成后):
3. eval_pi05_l2norm_k03_spatial_seed43
4. eval_pi05_random_k03_spatial_seed43

---
