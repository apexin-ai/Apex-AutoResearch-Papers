# eval test eval 4b rsft s42 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_test_eval_4b_rsft_s42_r2_20260521T183419_result.json`
- **Structured JSON:** [`c534cd87b55b44889e13.json`](../../sessions/c5/c534cd87b55b44889e13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 使用 53.7GB，训练正常运行。

## 报告

**原失败原因**：4B RSFT s42 checkpoint (`/root/autodl-tmp/rsft_output/checkpoint-510`) 已从服务器删除。`test_inference.py` 尝试从该路径加载 tokenizer/model 失败，回退到 HF Hub 查找也失败（本地路径不是合法 repo id）。

**修复方案**：使用相同训练数据和参数重训 4B RSFT s42。
- 数据：`/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` (2718 CED k=1 样本)
- 参数：bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, seed=42
- 输出：`/root/autodl-tmp/rsft_output_ced_s42/` (遵循命名规范)

**当前状态**：
- `retrain_4b_rsft_ced_s42` 在 cuda:0 训练中 (PID 126855)，step 3/510，~7.87s/step，预计 ~66 分钟完成
- 训练完成后需提交 `test_eval_4b_rsft_s42_r2`，使用新 checkpoint 路径 `/root/autodl-tmp/rsft_output_ced_s42/checkpoint-510`

**下一步**：训练完成后（约 ~1h），提交 test set eval 到空闲 GPU，registry ID `test_eval_4b_rsft_s42_r2`。

---
