# paper embedding tsne

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_embedding-tsne_20260518T232830_result.json`
- **Structured JSON:** [`eaf1b1f9e2614bcdb99c.json`](../../sessions/ea/eaf1b1f9e2614bcdb99c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

t-SNE 可视化生成完成。

**输出文件：**
- PDF: `/root/persuasion_turn_jailbreak_detect/paper/figures/embedding_tsne.pdf` (29 KB)
- PNG: `/root/persuasion_turn_jailbreak_detect/paper/figures/embedding_tsne.png` (265 KB)

**布局：** 3×2 子图
- 行：Vanilla / JB-MLM / 9-Class
- 列：DD OOD / ActorAttack
- 颜色：蓝色 = Benign (38 条), 红色 = Jailbreak (80 条)

**数据维度：** 每个 conversation 的所有 user turn [CLS] embedding (768-dim) 经 mean pooling 压为一个向量，共 118 个点/子图。

**使用的 checkpoints：**
1. Vanilla: `microsoft/deberta-v3-base` 原始预训练权重
2. JB-MLM: `checkpoints/plan_017_mlm/best/` (MLM continued pretraining)
3. 9-Class: `checkpoints/plan_002/deberta_multitask/best/model.pt` (9-class 多任务微调)

---
