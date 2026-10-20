# paper fig1 architecture v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig1-architecture-v2_20260518T190342_result.json`
- **Structured JSON:** [`8b5d8c3811801619eb3e.json`](../../sessions/8b/8b5d8c3811801619eb3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 生成完成。

**输出文件：**
- PDF: `/root/persuasion_turn_jailbreak_detect/paper/figures/fig1_architecture.pdf` (43.9 KB)
- PNG: `/root/persuasion_turn_jailbreak_detect/paper/figures/fig1_architecture.png` (116.2 KB)

**图表结构：**
- Stage 1 顶部：DeBERTa-v3-base (pretrained) 蓝色主框
- 三路分叉到三个分组框：
  - No Adaptation (灰色)：vanilla
  - MLM Adaptation (黄色)：JB-MLM, wiki-MLM
  - Classification (绿色)：topic, scrambled, binary, 9-class（加粗高亮，标注 2 heads: persuasion(9) + intent(binary)）
- 虚线分隔 "frozen [CLS] embeddings"
- Stage 2：[CLS]₁ [CLS]₂ ··· [CLS]ₖ → BiGRU (h=256, L=2, drop=0.3) → Jailbreak/Benign
- 标注 K-prefix evaluation

单栏宽度 3.25 inches，300 DPI，DejaVu Sans 字体，所有文字 ≥ 4.5pt。

---
