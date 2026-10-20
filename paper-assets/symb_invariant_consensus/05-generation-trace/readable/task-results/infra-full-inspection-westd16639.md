# infra full inspection westd16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-inspection-westd16639_20260521T190435_result.json`
- **Structured JSON:** [`3dcf26d609cf73854da4.json`](../../sessions/3d/3dcf26d609cf73854da4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cross-model SICA: 165/204 problems done. Now compiling the full status table.

## westd-16639 巡检结果 (2026-05-22 03:05 UTC)

### GPU 状态

| GPU | 型号 | 显存 (used/total) | 利用率 |
|-----|------|-------------------|--------|
| 0 | RTX PRO 6000 Blackwell | 84.2/97.9 GB | **0%** |
| 1 | RTX PRO 6000 Blackwell | 83.6/97.9 GB | **100%** |
| 2 | RTX PRO 6000 Blackwell | 88.1/97.9 GB | **100%** |
| 3 | RTX PRO 6000 Blackwell | 87.9/97.9 GB | **100%** |

### vLLM 服务

| 端口 | 模型 | GPU | 状态 |
|------|------|-----|------|
| 8000 | Mistral-7B-v0.3 | cuda:0 | UP |
| 8001 | Qwen3-14B | cuda:1 | UP |
| 8002 | Qwen2.5-72B-AWQ | cuda:2 | UP |
| 8004 | Mistral-7B-v0.3 (第二实例) | cuda:3 | UP |

### 实验状态

| # | 实验 | PID | 状态 | 进度 | ETA |
|---|------|-----|------|------|-----|
| 1 | **o3 Mistral extraction** | 473361 | **✅ 完成** | 196/196 (100%) | — |
| 2 | **Qwen3→Mistral fix** (reextract) | 473120 | 🔄 运行中 | 70/152 files (46%) | ~60 min |
| 3 | **70B SICA original** (FOLIO) | 436077 | 🔄 运行中 | 25/204 (12%) | **~2709 min (~45h)** |
| 4 | **Cross-model SICA 2×2** (PW) | 414515 | 🔄 运行中 | 165/204 (81%) | ~4-5h |

### 详情

**1. o3 Mistral extraction** — 已完成。Cross-model SICA = 82.65%, Wall time 46.5min。结果在 `results/exp_d135_frontier_scb/o3/cross_model/cross_model_mistral.json`。

**2. Qwen3→Mistral reextract fix** — 进行中，70/152 files，success rate 99.0%，avg 11 constraints/file。每 10 files ~7min，剩 82 files，ETA ~57min。用 Qwen3(8001) 做 extraction。

**3. 70B SICA (FOLIO)** — 极慢，25/204 problems，avg ~908s/problem。179 remaining × 908s ≈ **45 小时**。瓶颈是 72B-AWQ 在单卡上推理慢（k=12 traces × 4096 tokens）。

**4. Cross-model SICA 2×2 (ProofWriter)** — 165/204 done (81%)，用 Mistral(8000) + Qwen3(8001)。每 problem 有 4 路 extraction，剩 39 problems，ETA ~4-5h。

### 空闲 GPU

**GPU 0 利用率 0%** — Mistral-7B 8000 端口的 vLLM 加载了但当前无活跃推理（cross-model SICA 间歇调用）。实质上没有空闲 GPU，4 张卡都有 vLLM 实例占用显存。

### 关注点

- **70B SICA 还需 ~45h** — 这是最慢的实验，远超其他。如果有时间压力需要考虑是否值得等。
- **o3 extraction 已完成** — 进程还活着但已输出 `CROSS_MODEL_DONE`，可以释放 cuda:3 上的 Mistral 8004 实例。

---
