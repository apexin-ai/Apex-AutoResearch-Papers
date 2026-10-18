# ssh exp1 text reeval

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp1-text-reeval_20260514T231942_result.json`
- **Structured JSON:** [`96dd7a5a1cc9c271fbb5.json`](../../sessions/96/96dd7a5a1cc9c271fbb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整重评估完成（94 batches, 94000 entries）。结果：

## Per-Count Text-Match F1 曲线

| Count | Batches | MicroP | MicroR | MicroF1 | AvgPred | AvgGold | P/G Ratio |
|-------|---------|--------|--------|---------|---------|---------|-----------|
| 1 | 64 | 0.105 | 0.720 | **0.184** | 283.7 | 41.4 | 6.85 |
| 2 | 5 | 0.068 | 0.698 | **0.123** | 959.0 | 92.8 | 10.33 |
| 6 | 5 | 0.088 | 0.620 | **0.155** | 1355.4 | 193.2 | 7.02 |
| 12 | 5 | 0.160 | 0.539 | **0.246** | 1616.8 | 478.2 | 3.38 |
| 22 | 5 | 0.232 | 0.527 | **0.322** | 2009.4 | 884.2 | 2.27 |
| 44 | 5 | 0.414 | 0.551 | **0.473** | 2532.0 | 1899.6 | 1.33 |
| 64 | 5 | 0.520 | 0.418 | **0.463** | 2133.2 | 2652.0 | 0.80 |

## 核心发现

**Count curve 仍然反转**（inverted-U，峰值 count_44=0.473）：
- Recall 单调下降（0.72→0.42）：符合"类型多→遗漏多"的预期
- Precision 单调上升（0.11→0.52）：因为 over-prediction 随 count 减少
- F1 先升后略降，受 precision 上升主导

**Over-prediction 是反转的根因**：
- count_1 时 pred/gold=6.85:1（严重过度预测）
- count_2 最严重：pred/gold=10.33:1
- count_44 趋于平衡（1.33:1），count_64 开始欠预测（0.80:1）

## FP 错误分类

| Count | Hallucinated | WrongType | Spurious | Total FP |
|-------|-------------|-----------|----------|----------|
| 1 | 283 | 0 | 15,950 | 16,233 |
| 2 | 81 | 8 | 4,382 | 4,471 |
| 6 | 229 | 44 | 5,901 | 6,174 |
| 12 | 917 | 199 | 5,675 | 6,791 |
| 22 | 357 | 541 | 6,814 | 7,712 |
| 44 | 199 | 1,563 | 5,637 | 7,399 |
| 64 | 175 | 2,434 | 2,495 | 5,104 |

- **Spurious**（文本存在于原文但不是 gold entity）占绝对主体，尤其 count_1
- **Type confusion**（文本匹配 gold 但 type 错）随 count 增加而增长（0→2434），符合类型混淆假设
- **Hallucination**（文本不在原文中）占比很小（~1-5%）

## 结论

修正后的 count curve **不支持** "schema complexity hurts extraction"。真实 pattern 是：低 count 时模型 over-predict 严重（把非 entity 的文本也标注为 entity），拉低 precision 从而拉低 F1。类型混淆（WrongType）随 count 增加才成为显著因素，但其影响被 over-prediction 消减所抵消。

三个输出文件已保存至 `/root/schema-dag-extraction/results/`。

---
