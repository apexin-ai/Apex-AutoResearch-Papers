# paper intro polish

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_intro_polish_20260514T081847_result.json`
- **Structured JSON:** [`44bf5fcd4e94530fcfeb.json`](../../sessions/44/44bf5fcd4e94530fcfeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。主要改动：

**结构精简**：6段 + 3条贡献（原5条→3条），每段功能明确：Setup → Setup → Surprise → Lit Gap → Explanation → Contrast → Contributions。

**关键修改**：
- **¶3 (Surprise)**: 加入 "-47% rare n-gram survival"，补齐 C3 的双指标证据
- **¶4 (Literature gap)**: 大幅压缩，从~8行→3句，细节留给 Related Work
- **¶5 (Explanation)**: 删除 dimensional collapse 推测（属 Discussion），聚焦 selection ratio 定义和数值
- **¶6 (Contrast)**: 略微精简，保留 External-only 作为关键对照的论证
- **贡献列表**: 严格对齐 C1/C2-revised/C3：
  1. C1 — selection ratio 量化 alignment gap 逐代恶化
  2. C2 — 失败特异于内部嵌入（正常簇 vs RGDS 异常值）
  3. C3 — 同 budget 下 +72% PPL / -47% rare n-gram + 355M 初步验证

**Novelty framing**: "We identify" → "We trace"，贡献用 "quantify/isolate/establish" 而非 "discover"，避免 overclaim 概念新颖性。

---
