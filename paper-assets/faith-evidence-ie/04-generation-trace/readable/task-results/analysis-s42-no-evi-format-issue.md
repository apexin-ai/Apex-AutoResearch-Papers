# analysis s42 no evi format issue

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s42-no-evi-format-issue_20260520T151608_result.json`
- **Structured JSON:** [`e7507c6b2c2dd0e7ae5d.json`](../../sessions/e7/e7507c6b2c2dd0e7ae5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### Format Failure 原因

111 个 format failure 分为两类，**零 evidence leakage**：

| 类型 | 数量 | 原因 |
|------|------|------|
| 截断 | 46 | `max_new_tokens=1024` 不够，JSON 被截断 |
| 畸形 JSON key | 65 | 模型输出 `"tail:` 而非 `"tail":`（key 缺少闭引号） |

Regex 修复潜力：85/111 (76.6%) 可修复（55/65 非截断 + 30/46 截断）。

### Fair Comparison（关键发现）

**原来报告的 evidence tax = -1.65pp 是不公平比较的产物**：

| 子集 | No-evi ign_f1 | With-evi ign_f1 | Tax |
|------|--------------|----------------|-----|
| 全集 985 docs（不公平） | 0.5219 | 0.5384 | **-1.65pp** |
| Fair 874 docs（no-evi format OK） | 0.5575 | 0.5440 | **+1.35pp** |
| Fair 873 docs（双方 format OK） | 0.5577 | 0.5443 | **+1.34pp** |

**方向反转**：在公平子集上，no-evidence 反而**优于** with-evidence +1.35pp。原来的 -1.65pp 完全因为 111 个 format failure 的 predictions 得到 0 credit，拉低了 no-evidence 均值。

### 根因

- 111 个 failed docs 更难（avg 13.9 gold triples vs 12.3），输出更长（avg 2393 chars vs 1596）
- 更长的输出导致更高的截断率和 JSON 畸形率
- No-evidence 模型实际 RE 能力不比 with-evidence 差，问题在于**格式鲁棒性**（88.7% vs 99.5%）

### 建议

1. **短期**：在 evaluator 的 `parse_model_output` 中添加 regex 修复 malformed keys 的逻辑，可恢复 ~55 个 doc
2. **短期**：对长文档考虑增大 `max_new_tokens`（如 1536 或 2048）减少截断
3. **论文报告**：用 fair comparison（873-874 docs）报告 evidence tax，而非不公平的全集比较

---
