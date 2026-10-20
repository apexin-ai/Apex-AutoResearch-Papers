# exp plan006 trace length ablation setup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan006_trace_length_ablation_setup_20260515T222214_result.json`
- **Structured JSON:** [`802a818e443b2aed11d0.json`](../../sessions/80/802a818e443b2aed11d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 代码修改
在 `train/train_sft.py` 中添加了：
- **`truncate_traces(items, tokenizer, max_trace_tokens)`** 函数（第 72-97 行）：按 "Execution trace:\n" 和 "\n\nDoes this code pass all tests? Answer: " 标记定位 trace 部分，tokenize 后保留前 N tokens，decode 回文本。原地修改，打印截断统计。
- **`--max_trace_tokens`** 参数：默认 None（不截断，与现有行为完全兼容）
- main() 中在 dataset 创建前调用截断

### 2. Dry-run 验证
- 20 个样本全部正确截断到 256 tokens
- 原始 trace 长度 mean=1811, max=1912, min=1713 tokens
- 截断后结构完整（Execution trace 标记 + 问题后缀均保留）

### 3. 4 个实验注册
全部 PREPARING 状态：`full_trace_256tok_seed42`, `full_trace_512tok_seed42`, `full_trace_1024tok_seed42`, `full_trace_2048tok_seed42`

### 4. cuda:1 被占用 — 无法提交 256tok

`deepseek_full_trace_v3`（PID 163109）仍在 cuda:1 运行，epoch 2/3 完成（checkpoint-296, 6:25 保存），预计 epoch 3 约在 7:10 左右完成（每 epoch ~44 分钟）。

**需要等它跑完再提交。** 要我 ~45 分钟后回来检查并自动提交 256tok，还是你来通知我？

---
