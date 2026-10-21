# analysis error overlap and perclass f1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-overlap-and-perclass-f1_20260512T145117_result.json`
- **Structured JSON:** [`dabfbf6c5ef532c92fb5.json`](../../sessions/da/dabfbf6c5ef532c92fb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Error Overlap (4 pairs, 1890 samples/pair)**
- 94.7% agreement — CLS 和 CWM 在绝大多数样本上一致
- CLS-only correct 3.0% vs CWM-only correct 2.3%，CLS 净优势 +0.7pp
- CLS 优势集中在 **mutation 类型**：variable_swap (+4.5 samples net), operator_swap (+6.5), off_by_one (+10.0)
- CWM 在 **original 代码**上反而更好（-8.5 samples net）
- Both-wrong 样本偏向 pass 类（~130 pass vs ~53 fail），两个模型都对某些 pass 样本有系统性弱点

**Per-class F1**
- CLS 优势来自更高的 **fail recall** (+2.08pp) 和 **pass precision** (+1.88pp)
- Fail F1 差距 (+0.82pp) > Pass F1 差距 (+0.49pp)
- 按 mutation 类型：variable_swap CLS 优势最大 (+5.3pp acc)，original CWM 反而更好 (-2.1pp)

**论文启示**：CLS 优势本质上是 **mutation detection 优势**而非通用 execution simulation 优势。CWM 在理解未修改代码的行为上略胜一筹。这支持 "complexity-dependent advantage" 假说，且为 framing 提供了更精确的角度。

产出文件：
- 服务器：`analysis_error_overlap.py`, `analysis_error_overlap_report.json`, `predictions_cwm_seed789.jsonl`
- Artifact: `art_20260512_9b68a3` (error_overlap_analysis report)

---
