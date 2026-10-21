# audit westd 41074 sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-41074-sweep_20260521T144634_result.json`
- **Structured JSON:** [`19b627f3c4ed2ac10bdf.json`](../../sessions/19/19b627f3c4ed2ac10bdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Eval 实验（全部 DONE）

| 实验 | Prune Mode | Keep Ratio | Seed | SR (%) | 状态 |
|------|-----------|------------|------|--------|------|
| eval_pi05_l2norm_k07_object_seed42 | l2norm | 0.7 | 42 | **55.0** | DONE |
| eval_pi05_l2norm_k07_object_seed43 | l2norm | 0.7 | 43 | **56.4** | DONE |
| eval_pi05_random_k07_object_seed43 | random | 0.7 | 43 | **73.8** | DONE |
| eval_pi05_random_k05_object_seed43 | random | 0.5 | 43 | **68.4** | DONE |

注：random k0.5 seed43 结果写在 `pi05_random_k0.50_libero_object.json`（文件名没带 seed43 后缀，但 JSON 内确认 seed=43）。

### Multi-seed 汇总

| 方法 | k | seed42 SR | seed43 SR | 均值 |
|------|---|-----------|-----------|------|
| L2norm | 0.7 | 55.0% | 56.4% | **55.7%** |
| Random | 0.7 | 77.2%* | 73.8% | **75.5%** |
| Random | 0.5 | 69.4%* | 68.4% | **68.9%** |

*seed42 值来自 registry 中已有记录。

### VTC 训练状态

| GPU | 训练 | PID | 状态 | 已运行 |
|-----|------|-----|------|--------|
| GPU2 | M96 | 68539 | **RUNNING** | 1d 11h |
| GPU3 | M64v6 | 59671 | **RUNNING** | 5h 31m |

注：GPU3 现在跑的是 M64 **v6**（`openvla_sc_m64_seed42_v6`），PID 59671，不是原来的 PID 996937。GPU0/GPU1 空闲。

---
