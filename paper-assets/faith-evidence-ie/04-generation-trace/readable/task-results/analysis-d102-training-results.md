# analysis d102 training results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_training_results_20260518T085001_result.json`
- **Structured JSON:** [`779960e8a0a1296e2a2d.json`](../../sessions/77/779960e8a0a1296e2a2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四个实验的 registry 已全部确认——状态均为 DONE/success，checkpoint_path、metrics 都已就绪（之前的 on_complete hook 已自动更新）。

## 分析结果

| exp_id | 模型 | train_loss | token_acc | steps | checkpoint | 状态 |
|--------|------|-----------|-----------|-------|------------|------|
| d102_8b_rsft_k1_s42 | Qwen3-8B | 0.3877 | 0.858 | 1134 | checkpoint-1134 | 完成 |
| d102_8b_rsft_k1_s43 | Qwen3-8B | 0.3862 | 0.874 | 1134 | checkpoint-1134 | 完成 |
| d102_1_7b_rsft_k1_s42 | Qwen3-1.7B | 0.3063 | 0.873 | 567 | checkpoint-567 | 完成 |
| d102_llama_rsft_k1_s42 | LLaMA-3.1-8B | 0.3698 | 0.888 | 1107 | checkpoint-1107 | 完成 |

**要点**:
- 四个实验全部 epoch=3.0, EXIT_CODE=0, 输出 "RSFT training complete."
- Qwen3-8B 两个 seed 的 train_loss 极为接近 (0.3877 vs 0.3862)，训练稳定
- LLaMA-8B token accuracy 最高 (0.888)，1.7B train_loss 最低 (0.306，因模型小拟合快)
- 所有 output_dir 根目录均保存了最终 adapter，可直接用于 eval

**可以进入 eval 阶段。**

---
