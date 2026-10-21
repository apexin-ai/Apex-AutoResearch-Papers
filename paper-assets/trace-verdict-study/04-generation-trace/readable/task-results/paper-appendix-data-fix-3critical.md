# paper appendix data fix 3critical

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_data_fix_3critical_20260521T171142_result.json`
- **Structured JSON:** [`34e2006f14d66dd96522.json`](../../sessions/34/34e2006f14d66dd96522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，全部修复完成。

## 修复汇报

### 修复 1（CRITICAL）：Per-class table (tab:per_class) accuracy 列
| 行 | Condition | Before | After |
|---|---|---|---|
| L17 | Full Trace (LO) | 85.94 | **86.22** |
| L18 | VOTA | 99.05 | **99.41** |
| L21 | Loop Only | 86.05 | **85.63** |

附带修复 L738 regex_cross_format 表 VOTA 行：99.05→99.41, +23.50→+23.86（与正文 +23.86pp 对齐）

### 修复 2（CRITICAL）：删除重复 calibration 表 + 校正保留表
- **删除** L774-792（`\subsection{Calibration Analysis}` + tab:calibration_model_level，共 19 行）
- **保留表** tab:calibration_cross（L563）DeepSeek-6.7B 行：ECE 0.0064→**0.0049**，Brier 0.0061→**0.0059**，MCE 0.7756→**0.4692**
- **正文** L549：ECE (0.0064)→(0.0049)，Brier (0.0061)→(0.0059)
- Qwen-1.5B ECE 已为 0.0020，无需修改

### 修复 3（WARNING）：Confusion matrix
- L792 VOTA 行 Accuracy 已为 99.41%（TP=844,FP=0,TN=339,FN=7 → 1183/1190=99.41%）✓ 无需改动

### 编译结果
- **0** "multiply defined" 警告
- **0** LaTeX errors
- PDF MD5: `356c7f244fdb0109f04b3f68f17e365e`
- 页数: **22**

---
