# analysis r14 taskD entity ordering

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_taskD_entity_ordering_20260520T201720_result.json`
- **Structured JSON:** [`544a9778a1be0c11d507.json`](../../sessions/54/544a9778a1be0c11d507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**Entity-before-relation ordering 保持率：所有设置下均为 100%**

| Setting | Section Ordering | Triple Key Ordering | Total Triples |
|---------|-----------------|--------------------:|---------------|
| SciERC Qwen ZS | 100% (551/551) | 100% (1725/1725) | 1,725 |
| SciERC Llama ZS | 100% (550/550) | 100% (1304/1304) | 1,304 |
| DocRED Qwen ZS | 100%* (989/998) | 100% (17341/17341) | 17,341 |
| DocRED Llama ZS | 100%* (995/998) | 100% (16368/16368) | 16,368 |
| SciERC Qwen FT | 100% (551/551) | 100% (1128/1128) | 1,128 |
| SciERC Llama FT | 100% (551/551) | 100% (1081/1081) | 1,081 |
| DocRED Qwen FT | 100% (998/998) | 100% (15563/15563) | 15,563 |
| DocRED Llama FT | 100% (998/998) | 100% (16074/16074) | 16,074 |

\*DocRED ZS 的 9/3 个非完整 case 是 max_tokens 截断（entities 已生成但 relations section 被截断），不是顺序违反。

**原因**：EBNF grammar 定义 `root ::= { entities-section , relations-section }`，结构性保证了 entities 在 relations 之前。每个 relation triple 内部 key 顺序（head → tail → type → head_type → tail_type）也由 XGrammar JSON schema 强制。

结果已保存到 `/root/autodl-tmp/schema_outputs/r14_entity_ordering.json`。

---
