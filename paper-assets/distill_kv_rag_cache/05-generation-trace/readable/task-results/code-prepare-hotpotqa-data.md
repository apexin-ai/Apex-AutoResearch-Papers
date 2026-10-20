# code prepare hotpotqa data

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-hotpotqa-data_20260514T072737_result.json`
- **Structured JSON:** [`06e4892cdc09e4f6b9b2.json`](../../sessions/06/06e4892cdc09e4f6b9b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

传输成功。汇报结果：

**产出汇报**

| 指标 | 值 |
|------|-----|
| 样本数 | 500 条（全部 bridge type） |
| Context 词数 min | 114 |
| Context 词数 max | 2,250 |
| Context 词数 median | 931.5 |
| Context 词数 mean | 952 |
| Context > 512 words | 495/500 (99%) |
| Context > 300 words | 499/500 |
| 空答案 | 0 |

**典型样本**

1. **Q:** What government position was held by the woman who portrayed Corliss Archer in the film Kiss and Tell? **A:** Chief of Protocol — context 831 words
2. **Q:** What science fantasy young adult series, told in first person, has a set of comp... **A:** Animorphs — context 1,061 words
3. **Q:** The director of the romantic comedy "Big Stone Gap" is based in what New York ci... **A:** Greenwich Village, New York City — context 950 words

文件已传输到服务器 `/root/autodl-tmp/compresslink/data/hotpotqa_500.jsonl`，500 行确认无误。99% 样本 context 超过 512 words，在 chunk_size=512 下会产生充足的 multi-chunk 和 boundary tokens。

---
