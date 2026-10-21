# analysis eval llama sft s42 no evidence 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_sft_s42_no_evidence_2048_20260520T211248_result.json`
- **Structured JSON:** [`1d18adf81b8480626cd7.json`](../../sessions/1d/1d18adf81b8480626cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。摘要：

## eval_llama_sft_s42_no_evidence_2048 结果

**s42 2048 核心指标**: ign_f1=**0.5210**, f1=0.5306, format_ok=874/985 (88.7%), fair_tax=**+1.20pp**

**vs 1024 版**: 2048 对 s42 几乎无影响。format_ok 不变 (874→874)，ign_f1 从 0.5219→0.5210 (-0.09pp)，fair_tax 从 +1.34→+1.20pp (-0.14pp)。s42 的格式失败以 malformed JSON（67/111）为主而非截断（44/111），所以加长 token 限制无法修复。

**vs s44 2048**: 两个 seed 表现差异巨大：
| | s42 | s44 |
|---|---|---|
| ign_f1 | 0.5210 | 0.4373 |
| format_ok | 88.7% | 99.2% |
| fair_tax | **+1.20pp** | **-4.18pp** |

s42 no-evidence 在 fair subset 上反而比 with-evidence 好 1.2pp；s44 则差 4.2pp。方向相反。

**对 3-seed evidence tax 分析的意义**: s42 确认 2048 版与 1024 版实质等价，不存在截断导致的 ign_f1 低估。两个 seed 的 evidence tax 方向相反（s42 正、s44 负），说明 evidence tax 对 seed 高度敏感，需要 s43 2048 数据补齐后才能得出稳健结论。

---
