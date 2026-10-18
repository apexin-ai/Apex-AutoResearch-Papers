# analysis re none evaluation check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_re_none_evaluation_check_20260521T031735_result.json`
- **Structured JSON:** [`24a57e2cd7d5515922ea.json`](../../sessions/24/24a57e2cd7d5515922ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part A: 代码检查

**核心发现：Gold relation 始终在 candidate set 中。** 所有实验脚本在推理前过滤样本：

```python
batch_samples = [s for s in samples if s["relation_type"] in type_set]
```

这行代码出现在所有 5 个实验文件中（`run_fewrel_formal.py:118`, `run_docred.py:225`, `run_docred_phase2.py:259`, `run_d051_count_curves_25.py:169`, `run_fewrel_v2_bcs.py:283`）。

具体回答：

1. **FewRel/DocRED count-curve**：gold relation 不在 candidate set 时 → **样本被排除**，不参与该 batch 的推理和评测。已验证所有预测文件中 `oos_gt=0`。
2. **Prompt 允许输出 "none"**：是。Prompt 明确写 `If none of the candidate relations apply, output: {"relation": "none"}`，JSON schema enum 也包含 `"none"`。
3. **Accuracy 公式**：`correct/total`，其中 total 包含所有样本。模型输出 "none" 时必然算错（因为 gold 永远不是 "none"）。

### Part B: In-schema-only accuracy

**in_schema_accuracy ≡ original_accuracy**，因为 gold 在设计上就始终在 candidate set 中。

**"none" 预测比例**（值得关注）：
| Count | FewRel none% | DocRED none% |
|-------|-------------|--------------|
| 1     | 14.3%       | 12.0%        |
| 4     | 6.7%        | 17.0%        |
| 8     | 9.2%        | 16.5%        |
| 16    | 7.3%        | 23.3%        |
| 32    | 13.3%       | 25.1%        |
| 64    | 14.3%       | 24.4%        |
| 80/96 | 16.0%       | 18.3%        |

**Trend 一致性判断**：两个数据集都呈现明显的 degradation trend（FewRel: 0.857→0.504, DocRED: 0.880→0.387），不严格单调（存在小幅波动），但整体趋势清晰。

结果已写入 `artifacts/re_none_evaluation_analysis.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "relation": "none"
  }
}
```

</details>

---
