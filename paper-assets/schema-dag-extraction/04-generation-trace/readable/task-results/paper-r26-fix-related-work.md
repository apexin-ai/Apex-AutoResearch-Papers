# paper r26 fix related work

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_fix_related_work_20260522T043743_result.json`
- **Structured JSON:** [`d11643ad12c251d97bc6.json`](../../sessions/d1/d11643ad12c251d97bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**文件**: `docs/paper/related_work.tex:18`

**插入位置**: "SCS novelty" 段落第一句之后，第二句（"The metric is a means..."）之前。

**新增内容**（1 句）:
> Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy.

覆盖了三个要点：
1. LLM-PEE 用 similarity 做 partition engineering vs. 我们做 prediction/analysis
2. BCS = MEAN（averages all pairwise SCS）
3. 与后续已有文字（"The metric is a means; the empirical findings are the contribution, enabled by ... BCS-controlled batches that isolate confusability from count"）衔接，共同强调贡献是 controlled experimental design 而非 metric 本身

未添加第二句"The contribution is not the metric itself but the controlled batch design..."，因为紧跟的已有文字已表达相同含义，避免冗余。

---
