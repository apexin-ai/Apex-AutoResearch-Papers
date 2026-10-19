# eval wina greedy

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_wina_greedy_20260515T192120_result.json`
- **Structured JSON:** [`c859f7d3ea497ab0a3b4.json`](../../sessions/c8/c859f7d3ea497ab0a3b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已正常退出。

## 报告：WINA Greedy Baseline 评估 — 已验证（已重跑复现）

**状态：已重跑，结果与 registry 一致**

| 指标 | Registry 值 | 重跑值 |
|------|-------------|--------|
| dense_ppl | 6.12 | 6.12 |
| wina_greedy_ppl | 2126.03 | **2126.03** |
| model_level_sparsity | 0.5 | 0.500 |

**Greedy Per-Layer Allocation（重跑确认）：**
- Layers 0-11: 0.90（最高 sparsity，浅层 reconstruction error 低）
- Layer 12: 0.85, Layer 13: 0.80, Layer 14: 0.70
- Layer 15: 0.55, Layer 16: 0.50
- Layers 17-20: 0.30-0.35
- Layers 21-24: 0.05-0.15
- Layers 25-31: 0.00（深层完全保留，error 最大）

**结论：** 原始结果通过标准流程 `evaluate.py --baseline_mode wina_greedy` 复现，PPL=2126.03 精确匹配。日志已保存至 `/root/runs/distill_sparse_swiglu/training_free_wina_greedy.log`。

**注：** 首次运行因未 source `setup_env.sh` 导致 HF 数据集下载失败（缺少 `HF_HOME` 环境变量），修正后成功完成。

---
