# diagnose test eval field compliance

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_test_eval_field_compliance_20260521T150240_result.json`
- **Structured JSON:** [`eff9c680f0f92154cd52.json`](../../sessions/ef/eff9c680f0f92154cd52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：test_eval_8b_rsft_s42 field_compliance 问题

### 1. 根因：评测脚本 bug + 模型 EOS 行为

**两个独立问题叠加：**

**问题 A — `compute_format_compliance` 使用严格解析器（评测脚本 bug）**
- `evaluator.py:237` 的 `_parse_raw_json_list` 不支持截断修复，而 `parse_model_output`（用于实际 F1 计算）支持
- 模型输出 JSON 数组未闭合时（如 `[{...}, {..."head":`），严格解析器返回 None → 该文档不计入 `n_field_complete`
- 实际 F1/Evi-F1 是从宽松解析器提取的 triples 计算的，**不受此 bug 影响**

**问题 B — 85% 模型输出 JSON 未闭合（模型行为问题）**
- 500 个文档中，仅 74 个输出以 `]` 正确闭合
- 426 个输出在 JSON 数组中间触发了 EOS（非 max_new_tokens 截断，仅 9 个达到 2048 token 上限）
- 宽松解析器成功修复了 499/500 个输出并提取了 triples

### 2. 具体证据

| 指标 | test_eval_8b_rsft_s42 | rsft_s43 (dev) |
|---|---|---|
| 输出以 `]` 闭合 | 74/500 (14.8%) | ~802/985 (81.4%) |
| strict parseable | 74 | ~802 |
| field_compliance_rate | 0.148 | 0.814 |
| format_ok (宽松) | 499/500 | 985/985 |
| 数据集 | Re-DocRED test_revised | DocRED dev |
| gold triples/doc | 34.7 | 12.3 |

非闭合输出特征：
- `truncated=False`（EOS 触发，非 token 限制）
- 平均长度 3250 chars（远低于 max_new_tokens 对应的上限）
- 末尾是合法 JSON 片段但缺少 `]`

### 3. 对 F1=0.3353 的影响

F1 低的原因**不是** field_compliance bug，而是：
- **Re-DocRED test_revised gold 密度高**：17350 gold triples / 500 docs = 34.7/doc（dev 仅 12.3/doc）
- **recall 仅 0.2486**：模型 pred_count=8377，远低于 gold_count=17350
- 模型过早 EOS 导致部分 triples 在修复时丢失，进一步降低 recall
- precision=0.5149 尚可，说明预测质量本身不差

### 4. 是否影响其他 test eval

**是。** 所有使用 `test_inference.py` + `evaluator.py` 的 test eval 都会受 field_compliance 报告 bug 影响：
- `test_eval_14b_rsft_s42`、`test_eval_1_7b_rsft_s42`、`test_eval_4b_rsft_s42`、`test_eval_llama_rsft_s42`（均尚未完成）
- 它们的 `field_compliance_rate` 同样会被严格解析器低估
- 但 **F1 等核心指标不受影响**（使用宽松解析器）

### 5. 建议修复方案

**修复 A（评测脚本）— 优先级高：**
- `evaluator.py` 的 `compute_format_compliance` 方法应使用 `parse_model_output`（带修复）替代 `_parse_raw_json_list`（严格），或对 `_parse_raw_json_list` 增加截断修复逻辑
- 这只影响 compliance 报告指标，不影响 F1 计算

**修复 B（模型 EOS 问题）— 需要调查：**
- 85% 输出未闭合 JSON 是异常比例（dev 仅 19%），可能是 Re-DocRED test_revised 数据特征导致模型提前 EOS
- 可以考虑在推理时增加 `]` 作为 stop token 的负约束，或在 prompt 中强调必须输出完整 JSON 数组
- 但这属于模型层面优化，不是紧急问题

---
