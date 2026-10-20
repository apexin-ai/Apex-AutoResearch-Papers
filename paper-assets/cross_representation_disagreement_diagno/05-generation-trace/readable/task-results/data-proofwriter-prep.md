# data proofwriter prep

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_proofwriter_prep_20260515T060607_result.json`
- **Structured JSON:** [`1170980204fd4cdde908.json`](../../sessions/11/1170980204fd4cdde908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## ProofWriter 数据集准备结果

**数据源**：`renma/ProofWriter` (HuggingFace)，基于 ProofWriter (Tafjord et al., 2021) 的 OWA-D5 子集

**子集选择**：OWA (Open World Assumption) + D5 (depth-5，最长推理链)
- OWA 支持三分类 (True/False/Unknown)，与 FOLIO 一致
- D5 需要最多 5 步推理链，难度最高，更能区分方法优劣

**数据概况**：
| 指标 | 值 |
|------|-----|
| 总样本数 | 600 |
| True | 200 |
| False | 200 |
| Unknown | 200 |
| 格式 | 合成自然语言（事实+规则→结论） |

**产出文件**：
- 数据：`data/proofwriter/proofwriter-OWA-D5-validation.jsonl`
- 适配代码：`src/proofwriter_adapter.py`

**适配格式**（与 FOLIO pipeline 兼容）：
```python
ProofWriterExample(
    id="ProofWriter_AttNoneg-OWA-D5-1041_Q1",
    premises="Bob is cold. Bob is quiet. ...",   # context 字段
    conclusion="Charlie is kind.",                # question 去前缀
    label="True"                                  # A→True, B→False, C→Unknown
)
```

`ProofWriterExample` 与 `FolioExample` 接口一致（`.id`, `.premises`, `.conclusion`, `.label`, `.to_dict()`），`pipeline.py` 的 `process_one()` 可直接使用。

---
