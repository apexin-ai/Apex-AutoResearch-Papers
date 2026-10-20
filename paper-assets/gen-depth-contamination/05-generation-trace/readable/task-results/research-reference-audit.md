# research reference audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference_audit_20260520T112725_result.json`
- **Structured JSON:** [`69e287973093b9d73994.json`](../../sessions/69/69e287973093b9d73994.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

该论文已正式发表在 NeurIPS 2024。缺失的 bibtex entry：

```bibtex
@inproceedings{dohmatob2024demystified,
  title={Model Collapse Demystified: The Case of Regression},
  author={Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
  booktitle={Advances in Neural Information Processing Systems},
  year={2024},
  url={https://arxiv.org/abs/2402.07712}
}
```

## 汇总

| # | 论文 | 状态 | 详情 |
|---|------|------|------|
| 1 | Dohmatob et al. "Model Collapse Demystified" | ❌ **缺失** | 需添加上方 entry（NeurIPS 2024，key: `dohmatob2024demystified`） |
| 2 | Seddik et al. "How Bad is Training on Synthetic Data?" | ✅ 已有 | key: `seddik2024how`，line 449 |
| 3 | RADAR (Hu et al.) | ✅ 已有 | key: `hu2023radar`，line 456（注意：作者是 **Hu** 不是 Li） |
| 4 | Tulchinskii et al. "Intrinsic Dimension" | ✅ 已有 | key: `tulchinskii2024intrinsic`，line 463 |

注意：同一作者 Dohmatob 已有两篇在 bib 中（`dohmatob2024model` "A Tale of Tails" 和 `dohmatob2025strong` "Strong Model Collapse"），但 "Model Collapse Demystified" 是第三篇不同的论文，确实缺失。

需要我将该 entry 写入 `references.bib` 吗？

---
