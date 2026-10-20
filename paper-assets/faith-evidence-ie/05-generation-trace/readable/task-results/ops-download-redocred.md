# ops download redocred

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_redocred_20260516T063511_result.json`
- **Structured JSON:** [`56f563a66b7d284a807b.json`](../../sessions/56/56f563a66b7d284a807b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

**数据已下载并转换到** `/root/autodl-tmp/data/re-docred/`

### 统计

| Split | 文档数 | 总 Triples | 有 Evidence 的 Triples（保留） |
|-------|--------|------------|-------------------------------|
| train | 3,053 | 85,932 | 47,260 (55%) |
| dev | 500 | 17,284 | 7,473 (43%) |
| test | 500 | 17,448 | 7,547 (43%) |

关系类型：96 种（与 DocRED 完全一致）

### 兼容性

**直接兼容**，无需修改 `DocREDProcessor`。Re-DocRED JSON 结构（`title`, `vertexSet`, `labels[{r, h, t, evidence}]`, `sents`）与 DocRED 完全一致。

唯一差异：
1. **文件名**：`*_revised.json` vs DocRED 的 `train_annotated.json`/`dev.json` — 转换脚本已处理
2. **空 evidence**：约 55% 的 triples evidence 为空（Re-DocRED 修正了 false negative 但未标注 evidence）— 脚本 `evidence_only` 模式已过滤
3. **vertexSet 多余字段**（`global_pos`, `index`）— 已清除

### 产出文件
- 数据：`/root/autodl-tmp/data/re-docred/{train_annotated,dev,test}.json`
- 脚本：`/root/autodl-tmp/freige/scripts/convert_redocred.py`（支持 `--mode full` 保留全部 triples）

---
