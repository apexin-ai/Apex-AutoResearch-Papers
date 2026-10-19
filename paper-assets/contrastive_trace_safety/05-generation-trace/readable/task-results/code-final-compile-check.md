# code final compile check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_final_compile_check_20260517T223444_result.json`
- **Structured JSON:** [`3f76d5def1c9c80ea8e1.json`](../../sessions/3f/3f76d5def1c9c80ea8e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译完成。最终报告：

---

## 最终编译结果

| 项目 | 结果 |
|------|------|
| 总页数 | 17 |
| 正文结束（不含 Limitations） | 第 7 页上半部分 (~6.5页) |
| Limitations 起始 | 第 7 页中部 |
| References 起始 | 第 7 页下部 |
| Appendix 起始 | 第 9 页 (Checklist) / 第 10 页+ (technical appendix) |
| **正文 ≤ 8 页** | **通过** (约 6.5 页，不含 Limitations) |
| Undefined references | 0 |
| Missing citations | 0 |
| Overfull hbox > 10pt | **0** (修复前 7 处，全部修复) |
| 剩余 overfull hbox | 3 处 (3.8pt, 7.5pt, 0.5pt，均 < 10pt) |
| 其他 warnings | 4 个 float specifier `h` → `ht` (无害)，若干 underfull hbox (正常) |

## 修复内容

1. `experiments.tex` 表格：添加 `\setlength{\tabcolsep}{4pt}` (10.46pt → 消除)
2. `appendix.tex` Holm-Bonferroni 表：缩短表头 + `\tabcolsep` (29.46pt → 消除)
3. `appendix.tex` Window ablation 表：`\resizebox{\columnwidth}{!}{}` (58.59pt → 消除)
4. `appendix.tex` OT-7B layer sweep 表：缩短表头 + `\tabcolsep` (23.16pt → 消除)
5. `appendix.tex` GRU seeds 表：缩短表头 + `\tabcolsep` (35.88pt → 消除)
6. `appendix.tex` CPD sweep 表：缩短 caption 和表头 + `\tabcolsep` (34.68pt → 消除)
7. `appendix.tex` 32B divergence 表：缩短表头 + `\tabcolsep{3pt}` (55.18pt → 0.51pt)

## 交叉引用检查

所有 `app:*` 和 `sec:*` 标签均有对应定义，所有 appendix tables/figures 都有 `\label` 和 `\caption`，PDF 中无 `??` 出现。

---
