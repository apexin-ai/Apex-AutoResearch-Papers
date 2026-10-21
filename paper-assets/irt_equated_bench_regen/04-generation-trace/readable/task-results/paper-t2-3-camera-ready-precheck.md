# paper t2 3 camera ready precheck

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_t2_3_camera_ready_precheck_20260523T030037_result.json`
- **Structured JSON:** [`a8043d02f09827d4d5bf.json`](../../sessions/a8/a8043d02f09827d4d5bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Camera-Ready 预检报告

### 1. 页数
**[FAIL]** Main text 溢出到第 9 页。

Page 8 右栏：§5 Discussion 开始（§5.1 + §5.2），§5.2 末尾溢出到 Page 9 左栏（~2 行），Conclusion 标题和正文（~2 行）也在 Page 9。尽管 `discussion.tex:3` 已有 `\enlargethispage*{10\baselineskip}`，仍有约 4–5 行 main text 溢到第 9 页。Limitations/References 紧跟其后在同一页。

**需要压缩约 4–5 行才能让 Conclusion 结尾在第 8 页。**

### 2. Undefined References
**[PASS]** 编译日志中无 undefined reference 警告，无 `??` 输出。

### 3. E1-E3 Label 交叉引用

| Label | `\label` 定义 | `\Cref`/`\ref` 引用 | 状态 |
|---|---|---|---|
| `app:k3_power` | appendix.tex:50 ✓ | **无引用** | **[FAIL]** |
| `app:interaction` | appendix.tex:76 ✓ | discussion.tex:13 ✓ | [PASS] |
| `app:mixed_mechanism` | appendix.tex:80 ✓ | discussion.tex:13 ✓ | [PASS] |
| `tab:k3_power` | appendix.tex:56 ✓ | discussion.tex:20, appendix.tex:51 ✓ | [PASS] |

`app:k3_power` 只定义了 label 但从未被引用。`tab:k3_power`（对应表格）有引用，但段落级 label 是孤立的。

### 4. 数据一致性
**[PASS]** 所有跨文件数字一致：

| 数字 | discussion.tex | appendix.tex | 一致性 |
|---|---|---|---|
| OR=4.24 | line 13: `OR=4.24, p<10⁻²²⁵` | line 77: `OR=4.24, p<10⁻²²⁵` | ✓ |
| OR=4.75 | — | line 77: `OR=4.75, p<10⁻¹⁸⁸` | 仅 appendix |
| ρ=-0.302 | line 13: `best: ρ=-0.302` | line 81: `ρ_instruct=-0.302±0.090` | ✓ |
| AUC=0.905 | — | line 51: `AUC=0.905 at N=100` | 仅 appendix |
| TPR=0.571 | — | line 51 | 仅 appendix |
| TPR=0.454 | — | line 51 | 仅 appendix |
| χ²=634 | — (observed 562.7 in line 13) | line 81: `634±184 vs observed 562.7` | ✓ |

**[WARN]** appendix.tex:51 段落文字引用 |Δ_MH|≥1.4 的数字（TPR=0.454/0.571, AUC=0.905），但 `\Cref{tab:k3_power}` 指向的表格标题是 |Δ_MH|≥1.0 且不含 N=100 行。数字本身不矛盾（不同 threshold），但读者查表时可能困惑。

### 5. 其他常见问题
**[PASS]** 无 TODO/FIXME/XXX 注释
**[PASS]** 无空 `\cite{}` 或 `\Cref{}`
**[WARN]** 4 个 Overfull hbox 警告（均在 appendix 表格，lines 58–220）

---

**需修复：**
1. **页数溢出**：压缩 discussion/conclusion 约 4–5 行，或调整 spacing
2. **`app:k3_power` 无引用**：在 discussion.tex §5.2 中补一个 `\Cref{app:k3_power}`，或删除该 label

---
