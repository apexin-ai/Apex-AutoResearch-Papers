# code prepare real nq data

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-real-nq-data_20260514T064238_result.json`
- **Structured JSON:** [`394e18ed260529cd8da0.json`](../../sessions/39/394e18ed260529cd8da0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输验证成功。汇报：

1. **数据样本数**：500 条，全部包含有效 question/context/answers
2. **数据质量**：
   - Context tokens：min=64, max=3909, avg=242（GPT-2 tokenizer 计数）
   - 无 HTML 残留，纯文本
   - 所有样本均有非空 short answers
3. **典型样本**：
   - Q: "who sings blame it on the bossa nova" → A: ["Eydie Gormé"], context 84 tokens
   - Q: "who does marge's voice on the simpsons" → A: ["Julie Deborah Kavner"], context ~120 chars
4. **传输**：已成功 scp 到 `autodl-rtx6000:/root/autodl-tmp/compresslink/data/nq_500.jsonl`，服务器端验证 500 行、字段完整

---
