# paper page compression

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_page-compression_20260514T211426_result.json`
- **Structured JSON:** [`cbe553df5bc9872f4076.json`](../../sessions/cb/cbe553df5bc9872f4076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：无需压缩

**当前状态**：14 页 PDF，但**正文已在 8 页限制内**，无需压缩。

**分页结构**（pdftotext 验证）：
- p1: Abstract + §1 Introduction
- p2: Introduction 续
- p3: §2 Related Work + §3 Method
- p4: Method + Figure 1（pipeline + STA 示意）
- p5: §4 Experiments
- p6: 主结果表 + Cross-Logic
- p7: §5 Discussion and Conclusion + Figure 3（hacking modes）
- **p8**: Conclusion 末尾（`Interpreting ISR` / `Meta-Goodhart` / `Single-Seed Unreliability`）→ `Limitations and Future Work` → **References 标题（右栏中下部）**
- p9–10: References 续
- p10–14: Appendix（Table 2 hyperparameters / Extended Discussion / Per-seed tables / Cross-Logic figure）

**ARR May 2025 / EMNLP 2026 规则核对**：
- 长文 8 页正文限制，References + Appendix 不计入。
- ACL 2023+ 规定 Limitations 必须存在但不计入页限。
- 本文 Limitations 段落（`conclusion.tex` `\paragraph{Limitations and Future Work.}`）整段位于 p8 右栏上半部，References 标题在同页中下部启动 → 正文（含 Limitations）≤ 8 页，满足限制。

**结论**：源文件未做改动，PDF 未重编译。正文严格符合 EMNLP 2026 ARR 8 页限。

**注**：服务器 `/root/solver-trace-ablation/paper/` 不存在（仅本地路径 `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/` 存在 main.tex 和 main.pdf）；所有检查在本地完成。

---
