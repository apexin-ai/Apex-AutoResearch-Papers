# code nli reranking script

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli-reranking-script_20260512T115028_result.json`
- **Structured JSON:** [`98a7823613c81899ea8d.json`](../../sessions/98/98a7823613c81899ea8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 和参数解析正常，`--help` 输出所有参数及默认值。

脚本实现了：
- **NLI-filter**: 按 4 个阈值 (0.3/0.5/0.7/0.9) 扫描，移除低分 evidence span，报告 Evi F1/Precision/Recall/Attribution Precision/retention rate
- **NLI-rerank**: top-1 和 top-3 两个变体（纯重排不改变 set-based Evi F1，所以做了 top-k 截断）
- **NLI-oracle**: 对 gold evidence 计算 NLI 分数分布作为上限参考
- 支持 `--predictions_file` 跳过生成直接 rerank；生成后自动释放 GPU 再加载 NLI 模型

---
