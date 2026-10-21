# infra gpu status and multiseed check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-and-multiseed-check_20260523T123014_result.json`
- **Structured JSON:** [`7bfa30b23259d9eed6ae.json`](../../sessions/7b/7bfa30b23259d9eed6ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_and_multiseed_status.md`。核心发现：

**GPU 状态（8 张 GPU 总览）:**
- 16639: 3 张在跑，cuda:3 空闲（PID 681007 已被 kill ✓）
- 14391: 1 张在跑，但跑的是已完成的 seed123，冗余
- 30973: 3 张全满

**已完成实验（n=600）:**
- LLaMA seed42 ✅, seed123 ✅
- Qwen seed123 ✅

**关键问题:**

1. **14391 冗余运行**: llama8b_pw_seed123 已在 16639 完成，14391 上的副本可以 kill，释放 1 张 GPU
2. **3 组重复实验**: seed456/seed789 的 LLaMA 和 Qwen seed789 同时在 16639 和 30973 跑（v2/v3 版本）。如果 v2/v3 是新版代码，可 kill 16639 上的旧版
3. **Qwen seed456 暂停在 478/600**，当前无进程在跑。16639 cuda:3 空闲，可立即 resume
4. **Qwen Δ 显著小于 LLaMA**（-1.x pp vs -5~7 pp）

---
