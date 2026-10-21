# code gemma rp11 held out logo

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-rp11-held-out-logo_20260516T160859_result.json`
- **Structured JSON:** [`60360a9977f2fd5b8637.json`](../../sessions/60/60360a9977f2fd5b8637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/gemma_rp11_held_out_logo.json`。

**结果摘要：**

| Task | Macro F1 | Per-class F1 |
|------|----------|-------------|
| **3-class** | **0.6319** | gen0=0.995, gen1=0.048, gen2+=0.853 |
| **Binary** (gen1 vs gen2+) | **0.4553** | gen1=0.059, gen2+=0.852 |

**关键发现：**
- 3-class macro F1 = 0.632，在预期范围 (0.5–0.7) 内
- 分类器几乎无法区分 gen-1 和 gen-2+：990 中有 964 个 gen-1 被错分为 gen-2+，说明 rp=1.1 使 gen-1 的特征已经非常接近 gen-2+
- Binary F1 = 0.455，远低于 0.70 gate 阈值，**rp-LOFO gate 未通过**（比 Llama proxy 的 0.582 更差）
- 混淆矩阵显示 gen-0 完美分离，但模型在 rp=1.1 条件下无法有效区分浅层和深层生成

---
