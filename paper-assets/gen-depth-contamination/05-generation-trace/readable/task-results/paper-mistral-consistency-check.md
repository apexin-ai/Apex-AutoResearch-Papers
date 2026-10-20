# paper mistral consistency check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mistral-consistency-check_20260519T114424_result.json`
- **Structured JSON:** [`501cd4a7b3a3a9934001.json`](../../sessions/50/501cd4a7b3a3a9934001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。以下是发现的不一致和需要修改的位置。

---

## 一致性检查结果

### 无问题（已正确录入）

| 位置 | 内容 | 状态 |
|------|------|------|
| `main.tex:72` (Limitations) | "code domain tested with four models (Qwen2.5-1.5B, LLaMA-3.1-8B, and Mistral-7B-v0.3, K*=2; Pythia-1.4B, K*=1)" | ✓ 已更新 |
| `discussion.tex:32` | "Python code K*=2 for three models (K*=1 for capacity-limited Pythia-1.4B)" | ✓ 三模型 = Qwen+LLaMA+Mistral |
| `discussion.tex:34` | "yields K*=2 on code and K*=3 on arXiv" | ✓ Code K*=2 正确 |
| Abstract (`main.tex:40`) | "K*=1--2 for code (Python, model-dependent)" | ✓ 仍准确 |
| Introduction 贡献列表 (`introduction.tex:29`) | "Code (K*=1--2), model-dependent variation" | ✓ |
| `artifacts/code_crossmodel_table.tex` | 4 模型表，含 Mistral-7B-v0.3 K*=2 | ✓ 新表已生成 |
| 空 cite / undefined refs | `grep cite{}` = 0, `grep ?? main.aux` = 0 | ✓ 无问题 |
| Mistral C4=1, arXiv=3, Wiki=1 所有提及 | 全文一致 | ✓ |

---

### 需要修改的位置

#### 1. `experiments_c1.tex:166` — Domain × Model K* 矩阵表

**问题**: Mistral-7B Code 列仍为 `---`，应为 `2`。

```
当前: Mistral-7B   & 1 & --- & 3 & 1 \\
应改: Mistral-7B   & 1 & 2 & 3 & 1 \\
```

#### 2. `experiments_c1.tex:142-143` — Code 段落正文

**问题**: 只提到 3 个模型（Qwen, LLaMA, Pythia），未提及 Mistral-7B-v0.3。

```
当前: yield K*=2 for both Qwen2.5-1.5B ... and LLaMA-3.1-8B ..., but borderline K*=1 for Pythia-1.4B
应改: 加入 Mistral-7B-v0.3 (AUC=0.615, K*=2) 并将 "both" 改为 "three models"
```

同时引用 `Table~\ref{tab:code_crossmodel_kstar}`（该表也需更新，见下条）。

#### 3. `appendix_extended.tex:586-607` — Code crossmodel 表 (`tab:code_crossmodel_kstar`)

**问题**: 表中只有 3 个模型（Qwen, LLaMA, Pythia），缺少 Mistral-7B-v0.3 列。`artifacts/code_crossmodel_table.tex` 已有 4 模型完整版本。

**建议**: 用 artifacts 版本替换当前表，或手动加入 Mistral 列。注意 artifacts 版是 `table*` (双栏)，当前版是 `table` (单栏)，格式需确认。

#### 4. `appendix_extended.tex:589` — 表 caption

**问题**: Caption 说 "Qwen2.5-1.5B and LLaMA-3.1-8B yield K*=2"，缺 Mistral。

```
应改: "Qwen2.5-1.5B, LLaMA-3.1-8B, and Mistral-7B-v0.3 yield K*=2; Pythia-1.4B yields borderline K*=1"
```

#### 5. `appendix_extended.tex:314` — Boundary Cases 段落（中等优先级）

**问题**: "despite K*=1 on both C4 and Wikipedia, it yields K*=3 on arXiv" 只提 C4/Wiki/arXiv，未提 Code K*=2。

**建议**: 扩展为 "despite K*=1 on C4 and Wikipedia, it yields K*=2 on code and K*=3 on arXiv"（与 `discussion.tex:34` 保持一致）。

#### 6. `experiments_c1.tex:154` — Domain × Model 表 caption（低优先级）

**问题**: 表 caption 的脚注只定义了 `$^\ddagger$` (Pythia borderline)，但加入 Mistral Code=2 后，可能需要额外脚注标注 Mistral 的 Code 数据来源（同一 `code_crossmodel_kstar` 表）。

---

### 总结

- **高优先级修改**: 3 处（experiments_c1.tex 表格+正文，appendix_extended.tex 表格+caption）
- **中等优先级**: 1 处（appendix_extended.tex:314 段落）
- **低优先级**: 1 处（表 caption 脚注）
- **Citation 检查**: 无空 cite，无 undefined reference

---
