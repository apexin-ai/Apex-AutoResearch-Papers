# analyze 14b rsft field compliance

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_14b-rsft-field-compliance_20260522T002246_result.json`
- **Structured JSON:** [`0c75c02ab6881022c8de.json`](../../sessions/0c/0c75c02ab6881022c8de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。diff 显示关键区别：

**旧版（.bak，eval 时使用的版本）**：
```python
triples = self._parse_raw_json_list(raw_text)
if triples is None:
    continue  # 直接跳过，不修复
```

**新版（当前代码）**：多了 `_repair_truncated_json` 修复截断 JSON。

用新版逻辑模拟得到 499/500，而旧版只能 strict parse 180/500 完整 JSON → 就是 36% 的来源。

---

## field_compliance 分析

### Q1: 跨模型对比

| Model | field_compliance_rate | n_field_complete | n_predictions | n_truncated | ign_f1 |
|-------|----------------------|-----------------|---------------|-------------|--------|
| 8B RSFT | **14.8%** | 74/500 | 14616 | 9 | 0.3353 |
| 1.7B RSFT | **20.2%** | 101/500 | 26098 | 369 | 0.2933 |
| Llama RSFT | **35.2%** | 176/500 | 23330 | 283 | 0.3599 |
| 14B RSFT | **36.0%** | 180/500 | 15835 | 67 | 0.3849 |
| 14B SFT | 99.8% | 499/500 | 22352 | 253 | — |
| 8B SFT | 99.4% | 497/500 | 26988 | 410 | — |

**RSFT 通病，不是 14B 特有。** 8B RSFT 更严重（仅 14.8%）。SFT 全部 ≥99.4%。

### Q2: 代码处理逻辑

**field_compliance_rate=36% 是旧版评测代码的假警报：**
- 旧版 `compute_format_compliance` 对截断 JSON 只做 strict parse，失败直接跳过 → 不计为 field_complete
- 新版已加 `_repair_truncated_json`，修复后 499/500 field_complete
- **缺 evidence 的 prediction 是否计入 ign_f1：是。** `_normalize_triples` 填充 `evidence=[]`，所有恢复的 triple 都参与 F1 计算。**field_compliance_rate 不影响 F1/ign_f1 分数。**

### Q3: 抽样发现

- 320 个"非 compliant"文档的 raw output 都是**截断的 JSON 数组**（缺闭合 `]`，最后一个 triple 被截断到一半）
- 所有可恢复的 complete triple 都有 evidence 字段 — **不是 evidence 缺失问题，是 JSON 截断问题**
- 253 个文档实际截断但 `truncated=False` — truncation 检测有 bug（可能模型生成了 EOS 而非真的 hit max_new_tokens）
- SFT 模型倾向于先闭合 JSON array 再停止，所以即使 truncated=253 也能 strict parse

### 综合判断

1. **ign_f1=0.3849 可信** — F1 计算走 `parse_model_output`（含 repair），不受 field_compliance bug 影响
2. **field_compliance_rate=36% 是虚假警报** — 新版代码已修复，实际为 99.8%
3. **RSFT 的真实问题是 JSON 截断导致 triple 丢失**（14B: 15835 vs SFT 22352 predictions），压低了 recall。如果增大 max_new_tokens 或训练模型正确闭合 JSON，ign_f1 可能进一步提升
4. **对论文 claim 无影响** — 报告的 ign_f1 数字没有被 inflate 或 deflate，只是 RSFT 模型的 recall 受限于 JSON 生成不完整

---
