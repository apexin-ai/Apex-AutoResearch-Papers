# paper mr citations

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mr_citations_20260522T073223_result.json`
- **Structured JSON:** [`9c3105f9c3b45c768fff.json`](../../sessions/9c/9c3105f9c3b45c768fff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，无 undefined citation warning。

---

## 产出汇总

### MR1: Maennel et al. 2020
- **Bib**: `maennel2020random` 已存在（`references.bib:653-658`），NeurIPS 2020，7 位作者完整
- **引用位置**: `conclusion.tex:19` — `~\citep{zhang2021understanding,maennel2020random}`，在 "Regularization mechanism" 段
- **无需修改**

### MR2: JailDAM (Nian et al., COLM 2025)
- **Bib key**: `nian2025jaildam`
- **作者**: Yi Nian, Shenzhe Zhu, Yuehan Qin, Li Li, Ziyi Wang, Chaowei Xiao, Yue Zhao
- **Venue**: Conference on Language Modeling (COLM 2025), arXiv:2504.03770
- **引用位置**: `related_work.tex:9` — 加入 conversation-level systems 列表：`SafeDream~\citep{safedream2026}, JailDAM~\citep{nian2025jaildam})`

### MR3: Anil et al. (NeurIPS 2024)
- **Bib key**: `anil2024manyshot`
- **作者**: Cem Anil, Esin Durmus, Nina Panickssery, Mrinank Sharma 等 34 位（完整列表已入 bib）
- **Venue**: NeurIPS 2024
- **引用位置**: `related_work.tex:6` — 攻击段落中 automated methods 后：`and many-shot attacks~\citep{anil2024manyshot} exploit long-context in-context learning`

### MR4: Jain et al. (2023)
- **Bib key**: `jain2023baseline`
- **作者**: Neel Jain, Avi Schwarzschild, Yuxin Wen, Gowthami Somepalli, John Kirchenbauer, Ping-yeh Chiang, Micah Goldblum, Aniruddha Saha, Jonas Geiping, Tom Goldstein
- **Venue**: arXiv preprint, arXiv:2309.00614
- **引用位置**: `related_work.tex:9` — single-turn defenses 列表：`\citep{robey2024smoothllm,xu2024safedecoding,jain2023baseline}`

### MR5: Activation-based jailbreak detection (2 篇)
1. **Jailbreak Antidote** — `shen2025antidote`
   - 作者: Guobin Shen, Dongcheng Zhao, Yiting Dong, Xiang He, Yi Zeng
   - Venue: ICLR 2025, arXiv:2410.02298
2. **RepE Jailbreak Perspective** — `li2025repejailbreak`
   - 作者: Tianlong Li, Zhenghua Wang, Wenhao Liu, Muling Wu, Shihan Dou, Changze Lv, Xiaohua Wang, Xiaoqing Zheng, Xuanjing Huang
   - Venue: COLING 2025, arXiv:2401.06824
- **引用位置**: `related_work.tex:9` — representation-level approaches 列表末尾：`...,shen2025antidote,li2025repejailbreak}`

### 编译验证
`pdflatex + bibtex + pdflatex×2` 通过，**0 undefined citation warnings**。

---
