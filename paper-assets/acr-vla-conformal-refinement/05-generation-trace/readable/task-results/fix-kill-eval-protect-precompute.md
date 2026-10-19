# fix kill eval protect precompute

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-eval-protect-precompute_20260522T202737_result.json`
- **Structured JSON:** [`0ab3fbbb9b1157475c68.json`](../../sessions/0a/0ab3fbbb9b1157475c68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收齐。

---

## 结果汇总

### 1. Eval 进程 Kill ✅
- Killed PID 116273 (GPU 0, spatial_seed43 eval) 和 PID 116278 (GPU 1, goal_seed43 eval)
- 所有 forkserver workers (GPU 0 上 20 个, GPU 1 上 20 个) 随主进程自动退出
- GPU 0: 22978→9884 MiB，GPU 1: 20993→9884 MiB，释放成功

### 2. Kill 后 Precompute 速度变化
| Benchmark | Before kill (100 samples) | After kill (200 samples) | 变化 |
|-----------|--------------------------|--------------------------|------|
| object | 2.29 s/sample | 2.19 s/sample | -4.4% |
| spatial | 2.32 s/sample | 2.23 s/sample | -3.9% |
| goal | 2.29 s/sample | 2.16 s/sample | -5.7% |
| long | 2.13 s/sample | (尚未更新) | — |

**结论：Kill eval 后提速微乎其微（~5%）**，说明瓶颈不是 GPU 内存/算力争抢。

### 3. 速度慢的根因

逐层拆解每个 sample 的计算量：

```
get_obs_features_and_samples(sample):
  1. preprocess_obs()           → 图片 resize、state 离散化、tokenize
  2. encode_prefix()            → 1× PaliGemma 2B full forward（VLM prefix encoding）
  3. generate_k_samples(K=10):
     for k in range(10):        → 10 次独立采样
       for step in range(10):   → 每次 10 步 flow-matching 去噪
         denoise_step()          → 1× transformer forward（带 KV cache，较轻）
```

**每个 sample = 1 次 VLM 全量前向 + 10×10 = 100 次 denoise_step**

代码中 pi05 path（`train_crm.py:175-180`）对 batch 内每个 sample 逐个调 `get_obs_features_and_samples`，**完全没有 batch 化**（SmolVLA path 有 `get_obs_features_and_samples_batch`，但 pi05 没有对应实现）。

**~2.2s/sample 分解估算：**
- encode_prefix（PaliGemma 2B）: ~0.1-0.2s
- 100 次 denoise_step: ~0.02s × 100 = ~2.0s
- 关键瓶颈是 **K=10 × 10 denoising steps = 100 次 sequential transformer forward**

### 4. 加速建议

| 方案 | 预估加速 | 难度 | 说明 |
|------|---------|------|------|
| **Batch K samples**：将 K=10 noise 沿 batch 维 stack，一次 denoise 处理 10 个 sample | **~5-8×** | 中 | 需要改 `generate_k_samples` 把 K 折叠到 batch 维，KV cache 需 expand/repeat。4090 24GB 内存够（当前只用 9.9GB） |
| **减少 K**：K=10→K=5 | **2×** | 低 | 精度可能略降，但 conformal 理论上 K=5 也够 |
| **减少 denoising steps**：10→5 | **~2×** | 低 | 需验证 flow-matching 5 步的采样质量 |
| **Batch samples + Batch K**：同时 batch 多个 obs 和 K | **~10-20×** | 高 | 内存限制可能需要 gradient checkpointing |
| **fp16 推理**：当前可能是 fp32 | **~1.5-2×** | 低 | 检查 model dtype |

**最高 ROI 方案：Batch K samples**。当前每个 sample 的 10 个 K 是 sequential for-loop，改成 batch 维并行可以将 100 次 denoise 变成 10 次（每次 batch=10），且 4090 内存有 ~14GB 空余完全够用。预估可将 2.2s/sample 降到 ~0.3-0.5s/sample，整体耗时从 ~44h 降到 ~6-10h。

### 当前预估完成时间

按 2.2s/sample，4 个 benchmark 并行：
- object: 72507 samples → ~44h
- spatial: 60250 → ~37h
- goal: 61728 → ~37h
- long: 136090 → ~83h

**long benchmark 是瓶颈，约 83 小时（~3.5 天）**。其他三个 ~44h 内完成。

---
