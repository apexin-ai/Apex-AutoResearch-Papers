# paper arr precheck suppl checklist

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_arr_precheck_suppl_checklist_20260522T072522_result.json`
- **Structured JSON:** [`56532bbc3f3cbb0a17c1.json`](../../sessions/56/56532bbc3f3cbb0a17c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 2. Supplementary Material

**a) Appendix sections**: 25 个 section（A–Y），全部在 main.pdf 内。覆盖：cross-model validation（8B/70B/Gemini）、SDGD 协议、factorial analysis/TOST、centrality confound 控制、prompt sensitivity（4 变体）、BCS aggregation、format independence、SCS ablation、Monte Carlo 模拟、error taxonomy、renaming experiment、relaxed matching 等。

**b) Independent supplementary**: **需要操作** — `artifacts/anonymous_github/` 已准备好（42 scripts + 24 auxiliary + data + requirements.txt），但尚未上传到 anonymous.4open.science。论文中仅写 "Code and data will be released upon acceptance"（introduction 脚注 + checklist C4），无匿名 URL。

**c) Data/code citations**: **PASS** — 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）+ 4 个模型 + vLLM + MiniLM 均有正确 citation。

### 3. ARR Checklist

所有项目均已正确填写：
- **A1–A4**: YES（Limitations 6 项 + 2 段，risks 已讨论，AI 使用已声明）
- **B1–B6**: YES/N-A（全部 artifact 已 cite，license 已讨论）
- **C1–C4**: YES（72 GPU-hours，seed=42，vLLM v0.20.2，bootstrap CIs）
- **D1–D5**: N/A
- **E1**: YES

### 需要修复的项

| 优先级 | 项目 | 建议 |
|--------|------|------|
| 🔴 | Anonymous GitHub 未上传 | 上传 `artifacts/anonymous_github/` 到 anonymous.4open.science，链接填入 OpenReview supplementary 字段 |
| 🟡 | 上传前检查路径泄露 | `grep -r '/root/' artifacts/anonymous_github/` |
| 🟢 | Gemini API cost 未量化 | C1 中补充 API 费用或标注 "API cost not reported" |
| 🟢 | OpenReview form 填写 | 按 `arr_checklist_final.md` 逐项填入 |

---
