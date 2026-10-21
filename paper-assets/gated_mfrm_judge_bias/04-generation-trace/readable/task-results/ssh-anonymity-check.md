# ssh anonymity check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_anonymity_check_20260524T071740_result.json`
- **Structured JSON:** [`e0893406d37585b5d250.json`](../../sessions/e0/e0893406d37585b5d250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 匿名性检查报告

### 1. 作者姓名/机构 — **PASS** ✓
- `main.tex:27` → `\author{Anonymous}` — 正确的匿名格式
- 未发现任何真实姓名、大学名称、实验室名称

### 2. 非匿名 URL — **PASS** ✓
- 无 GitHub/GitLab/Bitbucket/HuggingFace 链接
- 无 arXiv 自引链接
- `limitations.tex:7` 使用了 `[anonymized URL]` — 正确做法

### 3. 致谢中的人名 — **PASS** ✓
- 未发现 acknowledge/thank/grateful/funded by/grant 等内容
- 无致谢段落，匿名提交阶段正确

### 4. 匿名宏 — **PASS** ✓
- `main.tex:3` → `\usepackage[review]{acl}` — 正确启用了 review（匿名）模式
- `acl.sty` 中 `review` 选项设置 `\acl@anonymizetrue`，会自动隐藏作者信息并显示行号

### 5. PDF metadata — **PASS** ✓
- `main.tex` 中无 `pdfauthor`/`pdfcreator`/`pdftitle` 设置，不会通过 PDF 元数据泄露作者信息

### 6. 脚注中的泄露 — **PASS** ✓
- 3 个脚注（`background.tex:26`, `method.tex:50`, `method.tex:99`），内容均为技术说明（OVB 近似、收敛诊断、衰减公式假设），无身份信息

### 补充检查
- **API key/token 泄露** — PASS，无 wandb/openai/api_key 等敏感信息
- **隐性自引** ("our lab/group/team") — PASS，未发现
- **匿名占位符** — 正确使用了 `[anonymized URL]` 和 `\author{Anonymous}`

---

**总结：全部 6 项检查通过，论文符合匿名审查要求。**

---
