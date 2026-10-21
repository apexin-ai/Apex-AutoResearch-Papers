# audit citation verify byerly dupo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation-verify-byerly-dupo_20260523T141445_result.json`
- **Structured JSON:** [`76ceda451e1e4dafad99.json`](../../sessions/76/76ceda451e1e4dafad99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两条引用均已确认。以下是结果：

---

## 引用 1: byerly2026selfconsistency

**存在性**: 真实存在。arXiv:2411.01101。

**当前 bib 的错误**:
- 作者名错：**Nicholas** Byerly → 应为 **Adam** Byerly
- 年份错：2026 → 初稿 **2024**（arXiv v1: 2024-11-02），但已被 TACL 接收（2026 年发表），所以 year=2026 配合 TACL venue 也可接受
- 标题错：缺少副标题，且主题不是 "Mathematical Reasoning"，而是 **positional bias in long-context problems**

**与我们引用上下文的相关性**: 如果我们引用它是为了说明 self-consistency 在 mathematical reasoning 上的局限性，那**引用上下文需要修正**——这篇论文讨论的是 long-context 场景下 positional bias 导致 SC 失效，不是 mathematical reasoning 的局限性。

**建议**: 保留并修正 bib + 检查正文引用上下文是否准确。

**正确 bibtex**:
```bibtex
@article{byerly2024selfconsistency,
  title={Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems},
  author={Byerly, Adam and Khashabi, Daniel},
  journal={Transactions of the Association for Computational Linguistics},
  year={2025},
  note={arXiv:2411.01101}
}
```
（注：arXiv v1 为 2024，TACL 正式发表页面显示 2025/2026，建议以 TACL 页面标注的年份为准，可用 `year={2025}` 或查 TACL 官方页确认。）

---

## 引用 2: dupo2025

**存在性**: 真实存在。arXiv:2508.14460。

**当前 bib 的错误**:
- 标题错：**Dual Process Optimization** → 应为 **Dual Preference Optimization**
- 副标题错：**Scalable Self-Correction** → 应为 **Enabling Reliable LLM Self-Verification**
- 第一作者错：**Yang, Chenxu** → 应为 **She, Shuaijie**

**与我们引用上下文的相关性**: 论文主题是 LLM self-verification via dual preference optimization，涵盖 translation 和 mathematical reasoning。如果我们引用它是为了说 self-correction/self-verification，主题相关，可保留。

**建议**: 保留并修正。

**正确 bibtex**:
```bibtex
@article{dupo2025,
  title={{DuPO}: Enabling Reliable {LLM} Self-Verification via Dual Preference Optimization},
  author={She, Shuaijie and Bao, Yu and Lu, Yu and Xu, Lu and Li, Tao and Zhu, Wenhao and Huang, Shujian and Cheng, Shanbo and Lu, Lu and Wang, Yuxuan},
  journal={arXiv preprint arXiv:2508.14460},
  year={2025}
}
```

---

**总结**: 两条引用均为真实论文但元数据严重错误（作者名、标题、全称），是典型的 LLM 幻觉式引用错误。已给出修正后的 bibtex。请额外检查正文中引用 byerly 的上下文——该论文讨论的是 long-context positional bias，不是 mathematical reasoning 局限性。

Sources:
- [Self-Consistency Falls Short! (arXiv)](https://arxiv.org/abs/2411.01101)
- [Self-Consistency Falls Short! (TACL)](https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.625/136156/Self-Consistency-Falls-Short-The-Adverse-Effects)
- [DuPO (arXiv)](https://arxiv.org/abs/2508.14460)
- [DuPO (aimodels.fyi)](https://www.aimodels.fyi/papers/arxiv/dupo-enabling-reliable-llm-self-verification-via)

---
