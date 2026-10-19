# data musique download

**verification triggered retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_musique_download_20260517T070050_result.json`
- **Structured JSON:** [`bda8764fdd0e096f64a2.json`](../../sessions/bd/bda8764fdd0e096f64a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出文件：`/root/autodl-tmp/data/musique_dev_200.json`（200 条，2460.7 KB）

数据格式（7 个字段）：

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | str | 样本 ID，如 `2hop__460946_294723` |
| `question` | str | 多跳问题 |
| `answer` | str | 答案 |
| `answer_aliases` | list | 答案别名 |
| `answerable` | bool | 是否可回答 |
| `paragraphs` | list[dict] | 20 个段落，每个含 `idx`, `title`, `paragraph_text`, **`is_supporting`**（标注是否为支持段落） |
| `question_decomposition` | list[dict] | 推理分解步骤，每步含 `question`, `answer`, `paragraph_support_idx` |

支持事实标注齐全：`paragraphs` 中的 `is_supporting` 字段标记了哪些段落是回答问题所需的支持段落，`question_decomposition` 提供了多跳推理的中间步骤和对应段落索引。

---
