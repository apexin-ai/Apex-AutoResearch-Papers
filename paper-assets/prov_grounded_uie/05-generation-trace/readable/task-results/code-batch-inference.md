# code batch inference

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch-inference_20260512T200713_result.json`
- **Structured JSON:** [`ddf53f2075302b508b04.json`](../../sessions/dd/ddf53f2075302b508b04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都已验证，改动正确。

## 改动摘要

### evaluate.py

| 位置 | 变更 |
|------|------|
| 文件头 docstring | 添加 batch generation 说明 |
| `main()` L126-128 | 新增 `tokenizer.padding_side = "left"` + 注释说明 why |
| `main()` L154-222 | **核心变更**：将逐条 `model.generate()` 重写为 batch 循环。先预处理所有 prompt/gold 数据到列表，再按 `eval_args.batch_size` 分批 tokenize（`padding=True`）→ `model.generate` → 按 `prompt_len` 切生成部分 → 逐条解码评估。进度日志改为每 50 条 batch 边界打印 |

输出格式（`eval_results.json` 的 `metrics` + `predictions` 结构）**完全不变**。

### rerank_nli.py

| 位置 | 变更 |
|------|------|
| 文件头 docstring | 添加 batch generation 说明 |
| `generate_predictions()` L67-170 | 同上模式改为 batch 推理：预处理 prompt + metadata → 分批 generate → 逐条解码。保留 GPU 释放逻辑 |
| `--predictions_file` 逻辑 | **已确认完整正确**：`load_predictions()` 读取 `eval_results.json`，合并 dataset 元数据，`main()` 中正确分支跳过 generate 直接进 NLI 评分。无需修改 |
| NLI 评分 | `_batch_nli_scores` 已经是 batch 调用，无需修改 |

---
