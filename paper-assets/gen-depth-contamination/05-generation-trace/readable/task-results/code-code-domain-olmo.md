# code code domain olmo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_code_domain_olmo_20260524T091908_result.json`
- **Structured JSON:** [`c7d2a0998b5f3011f0ef.json`](../../sessions/c7/c7d2a0998b5f3011f0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动，正在 GPU 1 上运行：

- **PID**: 167297
- **状态**: Phase 1 — OLMo-1B 正在生成 depth 1（5500 docs, batch_size=16, ~3-4s/batch）
- **预计**: 5 个 depth × ~344 batches × ~3s ≈ ~85 分钟完成 Phase 1，Phase 2 (Qwen cross-scoring) 另需约 30-40 分钟
- **日志**: `results/exp_code_olmo.log`
- **输出**: `data/exp_code_olmo/` (depth chain) + `results/exp_code_olmo/` (analysis)

工作流：
1. OLMo-1B 生成 depth 0→5 chain (continuation, nucleus p=0.95 T=1.0)
2. 删除 OLMo self-scored features
3. Qwen2.5-1.5B-Instruct cross-score → 15D features → OBD AUC + bootstrap CI

---
