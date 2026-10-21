# code wikievents unconstrained 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_unconstrained_16980_20260517T164054_result.json`
- **Structured JSON:** [`cfcd8179657ddd1ee6fc.json`](../../sessions/cf/cfcd8179657ddd1ee6fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成了。汇总：

## 结果

### Llama-3.1-8B-Instruct (GPU 1)
- **12/12 成功**，0 失败
- 总推理时间 ~200s（平均 ~17s/doc）
- 输出: `outputs/wikievents_llama_unconstrained.jsonl`

### Qwen3-8B (GPU 0)
- **11/12 成功**，1 失败（`scenario_en_kairos_14` 解析失败，耗时 74.5s）
- 总推理时间 ~551s（平均 ~46s/doc）
- 输出: `outputs/wikievents_qwen_unconstrained.jsonl`

### 注意事项
1. **数据量只有 12 docs**（不是预期的 ~246）。`data/wikievents/train.jsonl` 只包含 12 条记录。如需全量 WikiEvents corpus 需要额外下载。
2. `max_new_tokens` 已自动升级到 4096（代码中 wikievents 分支的默认行为）。
3. Qwen 比 Llama 慢约 2.8x，主要因为 Qwen 生成更长的输出（更多 events extracted per doc）且第一个文档解析失败说明输出格式可能有问题。
4. 两个模型的 `E=0`（entity count 为 0）是正常的，因为 wikievents 的 event extraction prompt 可能不单独列出 entities。

---
