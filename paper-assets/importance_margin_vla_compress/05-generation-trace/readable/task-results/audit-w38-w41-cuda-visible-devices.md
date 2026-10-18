# audit w38 w41 cuda visible devices

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_w38_w41_cuda_visible_devices_20260528T003337_result.json`
- **Structured JSON:** [`d8900cabdba610650515.json`](../../sessions/d8/d8900cabdba610650515.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。两台服务器均无 CUDA_VISIBLE_DEVICES bug。

---

## westd-38929

| GPU | UUID (短) | PID | CUDA_VISIBLE_DEVICES | 实验 | 显存 | GPU利用率 |
|-----|-----------|-----|---------------------|------|------|----------|
| 0 | e9ff022e | 672324 | **0** ✓ | attn k=0.85 long seed44 | 10468 MiB | 19% |
| 1 | b42ecc48 | — | — | **空闲** | 1 MiB | 0% |
| 2 | 2b25bd52 | 773760 | **2** ✓ | l2norm k=0.85 long seed44 | 10491 MiB | 32% |
| 3 | d885bcad | 774388 | **3** ✓ | attn k=0.5 long seed44 | 10162 MiB | 30% |

**Bug: 无。** 每个进程的 `CUDA_VISIBLE_DEVICES` 与实际物理 GPU index 一一对应。

**空闲 GPU: 1** — random k=0.7 (PID 672401) 已结束。

**C004 合规: ✓** 三个进程均有 `HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`, `HF_HOME=/root/autodl-tmp/.hf_cache`, `MUJOCO_GL=egl`。

---

## westd-41074

| GPU | UUID (短) | PID | CUDA_VISIBLE_DEVICES | 实验 | 显存 | GPU利用率 |
|-----|-----------|-----|---------------------|------|------|----------|
| 0 | b12dc93c | 383800 | **0** ✓ | l2norm k=0.95 long seed43 | 10346 MiB | 2% |
| 1 | b927bd9e | 374814 | **1** ✓ | attn k=0.7 long seed44 | 10559 MiB | 42% |
| 2 | 754fc39d | 266907 | **2** ✓ | attn k=0.75 long seed44 | 10462 MiB | 31% |
| 3 | 5de49e5a | — | — | **空闲** | 1 MiB | 0% |

**Bug: 无。** 每个进程的 `CUDA_VISIBLE_DEVICES` 与实际物理 GPU index 一一对应。

**空闲 GPU: 3** — attn k=0.95 已结束。

**C004 合规: ✓** 三个进程均有全部 offline flags。

**注意:**
- GPU 1 上实际运行的是 `attn k=0.7`（PID 374814），而非 registry 中的 `random k=0.75`（PID 185640）。random k=0.75 已结束，被替换。
- GPU 0 的 PID 是 383800（非 registry 中的 383791），属于 parent/child PID 偏差，正常。
- GPU 0 利用率仅 2%，可能在 episode 间隔或接近完成。

---

## 总结

| 服务器 | CUDA bug | 空闲GPU | C004合规 |
|--------|----------|---------|---------|
| westd-38929 | **无** | GPU 1 | ✓ |
| westd-41074 | **无** | GPU 3 | ✓ |

两台服务器不存在 cqa1 的 bug。所有运行中实验的 `CUDA_VISIBLE_DEVICES` 均正确设置，一进程一卡，无冲突。两台各有 1 张空闲 GPU 可用于新实验。

---
