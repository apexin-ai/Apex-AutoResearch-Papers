# analysis plan019 1 7b rsft no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan019_1_7b_rsft_no_evidence_eval_20260519T144541_result.json`
- **Structured JSON:** [`e21bacc916e349f3f653.json`](../../sessions/e2/e21bacc916e349f3f653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

**总结：**

| 条件 | 值 |
|------|-----|
| No-evidence ign_f1 | 0.4352 |
| With-evidence ign_f1 | 0.5122 |
| **差值** | **-7.70pp** |

Hypothesis rejected。1.7B RSFT 不存在 evidence tax，相反 evidence generation 对 RE 有 +7.70pp 的正面贡献。与 14B SFT 的 ~0.03pp evidence tax 对比，说明小模型更依赖 evidence chain-of-thought 来辅助关系抽取——这为跨尺度 scaling curve 提供了一个重要数据点。

评估脚本确认 `--no_evidence` 正确传入，无错误，无 W&B run。唯一值得注意的是 truncation rate 59.2%，但 format compliance 97.1% 说明模型输出格式基本正确。

---
