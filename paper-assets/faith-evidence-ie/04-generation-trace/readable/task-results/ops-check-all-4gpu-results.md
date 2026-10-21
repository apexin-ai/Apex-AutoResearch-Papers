# ops check all 4gpu results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_4gpu_results_20260517T145145_result.json`
- **Structured JSON:** [`d5f4b14f30b3dbcc7251.json`](../../sessions/d5/d5f4b14f30b3dbcc7251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验仍在运行中，GPU 并非空闲。当前状态：

| # | 实验 | GPU | PID | 进度 | 预计剩余 |
|---|------|-----|-----|------|---------|
| 1 | **8B RSFT eval** (plan_006_qwen3_8b_rsft_eval) | cuda:3 (19GB) | 442383 | 242/247 (98%) | ~4 min |
| 2 | **lead2_ckpt20_eval** | cuda:1 (11GB) | 446829 | 运行 2h15m | 未知 (输出到 `eval_outputs/` 而非 `eval_results/`) |
| 3 | **1.7B seed43 eval** (plan_006_qwen3_1_7b_rsft_seed43_eval) | cuda:2 (5.5GB) | 455637 | ~49/247 (20%) | ~1.5h |
| 4 | **LLaMA training** (plan_006_llama_rsft_seed43) | cuda:0 (28GB) | 450239 | 2048/3312 (62%) | ~1h |

注意事项：
- **8B eval** 即将完成（~4分钟）
- **lead2_ckpt20_eval** 的输出路径是 `/root/autodl-tmp/eval_outputs/lead2_ckpt20_eval`，不在 `eval_results/` 下
- **1.7B seed43 eval** 和 **LLaMA training** 都还需要约 1-1.5 小时
- LLaMA 训练已有 checkpoints: 1850, 1900, 1950, 2000, 2050，最终 checkpoint 尚未产生

建议等 8B eval 完成后（几分钟内）先查看其结果，其余实验需要继续等待。

---
