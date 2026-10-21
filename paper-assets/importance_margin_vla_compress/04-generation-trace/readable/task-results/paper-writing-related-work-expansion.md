# paper writing related work expansion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_expansion_20260521T150123_result.json`
- **Structured JSON:** [`23eec975e261a0a04a62.json`](../../sessions/23/23eec975e261a0a04a62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

**related_work.tex** — 从 ~350 词扩展到 ~550 词（4 段结构保留），预计 0.75-1 页 CoRL 双栏格式：

- **P1 (Vision token efficiency)**: 新增 SparseViT、TokenLearner、A-ViT、AdaViT（ViT 自适应计算）+ FasterVLM、FitPrune、CrossGET（VLM token pruning），按方法类别分组而非逐篇罗列
- **P2 (VLA-specific)**: 无变化，内容已充分
- **P3 (Vision connectors)**: 新增 LLaVA-1.5 引用、InternVL 2.5 + Mini-InternVL（pixel-shuffle 家族扩展）
- **P4 (VLA compression)**: 标题改为 "VLA compression"，各 concurrent work 增加方法描述（不再仅列名）；Don't Run with Scissors 大幅扩展——描述 weight pruning/quantization 发现、GLUESTICK recovery 方法、与本文 vision token deletion 的机制差异

**references.bib** — 新增 10 篇已验证引用：
1. TokenLearner (Ryoo+, NeurIPS 2021)
2. A-ViT (Yin+, CVPR 2022)
3. AdaViT (Meng+, CVPR 2022)
4. SparseViT (Chen+, CVPR 2023)
5. FitPrune (Ye+, AAAI 2025)
6. CrossGET (Shi+, ICML 2024)
7. FasterVLM (Zhang+, arXiv 2024)
8. LLaVA-1.5 (Liu+, CVPR 2024)
9. InternVL 2.5 (Chen+, arXiv 2024)
10. Mini-InternVL (Gao+, arXiv 2024)

---
