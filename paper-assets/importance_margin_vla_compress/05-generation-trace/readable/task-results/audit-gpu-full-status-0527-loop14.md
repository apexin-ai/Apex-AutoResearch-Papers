# audit gpu full status 0527 loop14

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_full_status_0527_loop14_20260527T040513_result.json`
- **Structured JSON:** [`71ca0d26c61d722f7c30.json`](../../sessions/71/71ca0d26c61d722f7c30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full audit:

---

## westd-41074 (4×RTX PRO 6000, 98GB)

| GPU | Mem | Util% | PID | Experiment | Progress |
|-----|-----|-------|-----|-----------|----------|
| 0 | 15.9GB | 74% | 32184 | OV Random k=0.95 Long | T4/10, ep20 (~6h left) |
| 1 | 15.9GB | 74% | 856656 | OV Random k=0.75 Long | **T10/10 starting (~1h left)** |
| 2 | 10.9GB | 24% | 94308 | **π0.5 Attn k=0.9 Long strict** | T1/10 (T0: 36%, T1: ep10 90%) ~3h left |
| 3 | 10.2GB | 0% | 94384 | **π0.5 Attn k=0.85 Long strict** | T1/10 starting (T0: **14%**) ~3h left |

空闲 GPU: 无

**已完成（新）:**
- OV Random k=0.95 Object → **SR=67.4%** (10:15)
- OV Random k=0.75 Object → **SR=50.4%** (08:18)

---

## westd-38929 (4×RTX PRO 6000, 98GB)

| GPU | Mem | Util% | PID | Experiment | Progress |
|-----|-----|-------|-----|-----------|----------|
| 0 | 16.0GB | 0% | 949253 | OV Attn k=0.95 Goal | T6/10, ep20 (~2h) |
| 1 | 15.8GB | 0% | 949447 | OV L2norm k=0.95 Long | T3/10, ep10 (~7h) |
| 2 | 32.1GB | 0% | 965423+968309 | ⚠️ OV Attn k=0.75 Goal + OV L2norm k=0.75 Long | T3/10 + T2/10 |
| 3 | 15.8GB | 9% | 950007 | OV Attn k=0.95 Long | T3/10, ep10 (~7h) |

空闲 GPU: 无

⚠️ **GPU2 有 2 个实验共用**，所有 GPU util 0-9%（可能是 nvidia-smi 采样间隙，但 GPU2 双进程需关注）

**已完成（新）:**
- OV L2norm k=0.5 Long → **SR=16.4%** (09:01)
- OV Random k=0.85 Long → **SR=45.0%** (08:43)
- OV Random k=0.75 Goal → **SR=72.0%** (08:37)

---

## westd-27271 (2×RTX PRO 6000, 98GB)

| GPU | Mem | Util% | PID | Experiment | Progress |
|-----|-----|-------|-----|-----------|----------|
| 0 | 1MB | 0% | - | **IDLE** | - |
| 1 | 16.0GB | 73% | 638225 | OV Attn k=0.95 Object | T7/10, ep20 (~1.5h) |

**空闲 GPU: GPU0**

**已完成（新）:**
- OV L2norm k=0.95 Goal → **SR=75.2%** (11:53)
- OV Attn k=0.5 Long → **SR=14.6%** (09:17)
- OV Attn k=0.75 Goal → **SR=67.4%** (08:20)

---

## cqa1-33015 (4×RTX 4090D, 24GB)

| GPU | Mem | Util% | PID | Experiment | Progress |
|-----|-----|-------|-----|-----------|----------|
| 0 | 15.7GB | 62% | 896333 | OV Random k=0.95 Goal | T4/10 starting (~3h) |
| 1 | 15.7GB | 53% | 898055 | OV Attn k=0.95 Goal | T4/10 starting (~3h) |
| 2 | 10.6GB | 19% | 938642 | **π0.5 Attn k=0.95 Long strict** | T0/10, ep20 (90%) ~3.5h left |
| 3 | 15.7GB | 56% | 897100 | OV Attn k=0.5 Goal | T3/10, ep10 (~5h) |

空闲 GPU: 无

⚠️ `eval_pi05_attn_k095_long_seed42_strict.log` 之前 **失败**（`ModuleNotFoundError: transformers.models.qwen2_5_vl`），当前运行的是重启版本 `eval_pi05_attn_k095_long_strict.log`

**已完成（新）:**
- π0.5 L2norm k=0.85 Long → **SR=77.8%** (09:56)
- π0.5 Random k=0.70 Long → **SR=62.4%** (08:59)

---

## 总览

| 指标 | 值 |
|------|------|
| 总在跑 | **13 experiments / 14 GPUs** (westd-38929 GPU2 两个共用) |
| 空闲 GPU | **westd-27271 GPU0** (1台, 98GB) |
| 距截止 | ~24h (截止 2026-05-28 12:00 UTC) |

**需关注:**
1. **westd-27271 GPU0 空闲** — 可以立即调度新实验
2. **westd-38929 GPU2 双进程** — OV Attn k=0.75 Goal + OV L2norm k=0.75 Long 共用一张卡，可能互相拖慢
3. **cqa1 GPU0/1 与 westd-38929 GPU0 存在重复**：OV Random/Attn k=0.95 Goal 在两台机器上同时跑
4. **π0.5 Attn k=0.85 strict T0=14%** — 显著低于 k=0.9 (36%) 和 k=0.95 (90%)，符合预期的 k 降低性能下降趋势
5. **westd-41074 GPU1** OV Random k=0.75 Long 即将完成（~1h），可准备下一个实验

---
