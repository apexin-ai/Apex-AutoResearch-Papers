# analysis exp 001 gt true cases

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_gt_true_cases_20260515T063140_result.json`
- **Structured JSON:** [`8ccea19a43aa13851903.json`](../../sessions/8c/8ccea19a43aa13851903.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已生成。以下是完整分析结果：

---

## GT=True Targeted Repair 反效果：5 案例深度分析

### 统计概览

| 指标 | 数值 |
|------|------|
| GT=True 有 repair 的样本 | 22 |
| Targeted 成功率 | 14/22 (63.6%) |
| Blind 成功率 | 17/22 (77.3%) |
| Targeted 失败 + Blind 成功 | **5 例** |
| 双失败 | 3 例 |

### 失败机制分布

| 机制 | 数量 | 占比 |
|------|------|------|
| **Overcorrection（过度纠正）** | 3 | 60% |
| Misleading diagnosis（误导性诊断） | 1 | 20% |
| Wrong fix direction（修错方向） | 1 | 20% |

---

### 5 个案例详情

**Case 1: folio_validation_1** — Overcorrection
- 结论：Bonnie 的学校参与推导（复合条件句）
- FOL=True(正确), Code=False(错误), 诊断: negation_error/code
- Targeted 两轮都输出 Unknown，Blind 第二轮输出 True
- **机制**：被告知"你说 False，对方说 True，检查否定词"后，模型不敢承诺 True，对冲到 Unknown

**Case 2: folio_validation_110** — Misleading Diagnosis
- 结论：Peter 是否既是美食家又高收入（error_side=both）
- FOL=False(错), Code=Unknown(错), GT=True
- FOL targeted→False, FOL blind→False; **Code blind→True(成功)**
- **机制**：error_side=both 时 targeted repair 告诉 FOL"Code 说 Unknown"作为参考，但 Code 也是错的。参考信号本身就是错的

**Case 3: folio_validation_155** — Wrong Fix Direction
- 结论：Remy 的作息与家庭办公推导
- FOL=True(正确), Code=Unknown(错误), 诊断: logic_error/code
- Targeted 最终输出 False（比原来的 Unknown 更错），Blind 输出 True
- **机制**：模型尝试修复 logic_error 但把逻辑改反了，从 Unknown 翻到了 False

**Case 4: folio_validation_80** — Overcorrection
- 结论："Dried Thai chilies are not a product of Baked by Melissa"
- FOL=True(正确), Code=Unknown(错误), 诊断: logic_error/code
- Targeted 两轮都 Unknown, Blind 第二轮 True
- **机制**：Code 本来就输出 Unknown，被告知"对方说 True"后仍然无法突破，停在 Unknown

**Case 5: folio_validation_87** — Overcorrection
- 结论："Sir Digby's nemesis loses"
- FOL=Unknown(错误), Code=True(正确), 诊断: logic_error/fol
- FOL targeted 两轮 Unknown, FOL blind 第二轮 True
- **机制**：FOL 被告知"Code 说 True，你有 logic_error"，但 logic_error 没有具体 hint（为空），模型无法定位 bug，维持 Unknown

---

### 核心发现

1. **Overcorrection 是主导模式（3/5）**：诊断信息告诉模型"你错了"但 hint 太模糊，模型理性地对冲到 Unknown。对 GT=True 问题来说 Unknown 永远是错的，所以诊断信息反而增加了不确定性。

2. **GT=True 特别脆弱的原因**：正确答案需要 affirm conclusion，这比否定更需要完整的推理链。模型被告知"你错了"后，更容易退缩到 Unknown（安全但错误的对冲）而不是大胆修正到 True。Blind regen 没有这个锚定效应，反而能从零开始正确推导。

3. **error_side=both 是系统性缺陷**：targeted repair 假设"对方是对的"来提供参考信号，当双方都错时参考信号本身就是错的。

### 改进建议

1. **error_side=both 时跳过 targeted repair**，直接 blind regen
2. **弱化诊断信号**：不透露对方的 verdict，只给 error type hint（防止锚定效应）
3. **Hybrid fallback**：targeted 输出 Unknown 时自动 fallback 到 blind regen
4. **Confidence-gated**：stability check 显示"正确方"自身不一致时，优先 blind regen

---

产出文件：
- `src/gt_true_case_study.py` — 分析脚本
- `results/exp001_gt_true_case_study.json` — 完整 JSON（含代码片段）
- `results/exp001_gt_true_case_study.txt` — 可读文本报告

---
