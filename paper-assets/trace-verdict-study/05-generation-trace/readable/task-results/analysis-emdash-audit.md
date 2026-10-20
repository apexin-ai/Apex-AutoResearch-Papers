# analysis emdash audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_emdash_audit_20260519T083659_result.json`
- **Structured JSON:** [`a92ef0c5043f9427469d.json`](../../sessions/a9/a92ef0c5043f9427469d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### Em-dash（—）
**0 处匹配。已全部清零。**

### En-dash（–）
**0 处匹配。** 包括解释性用法（` – `）和所有其他用法均为零。数字范围在 LaTeX 中使用的是 `--` 语法（如 `1.5B--13B`），不是 Unicode en-dash 字符，符合规范。

### -ing 分词短语
**2 处匹配，均为误报（无需修改）：**

| 文件 | 行号 | 匹配内容 | 判定 |
|------|------|----------|------|
| `experiments.tex` | 49 | `...99.83\% ceiling, spanning only 0.50pp.` | "ceiling," 是名词，非 -ing 分词短语 |
| `introduction.tex` | 28 | `...99.83\% ceiling, while the no-trace...` | 同上，"ceiling," 是名词 |

### 总结

| 类别 | 总数 | 需删除 |
|------|------|--------|
| em-dash（—） | 0 | 0 |
| en-dash（–） | 0 | 0 |
| -ing 分词短语 | 0（2处为名词误报） | 0 |

**Patch 19 的清理已确认完成，全文无 AI 风格 dash 残留。**

---
