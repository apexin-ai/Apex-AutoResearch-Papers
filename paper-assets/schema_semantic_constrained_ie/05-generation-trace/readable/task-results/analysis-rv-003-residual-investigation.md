# analysis rv 003 residual investigation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rv_003_residual_investigation_20260516T185739_result.json`
- **Structured JSON:** [`e4f531e5aa8a5a3a3de6.json`](../../sessions/e4/e4f531e5aa8a5a3a3de6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

**结论**: RV=0.03% 是 XGrammar v0.1.33 的 enum 编译 bug。

- 全部 5 个 violation 来自**同一篇文档 "Souvlaki"**，生成了不存在的关系 `"membericipant of"`（"member of" + "participant of" 的 portmanteau）
- **机制**: XGrammar 接受 token "member"(9792) 后，其 byte-level automaton 错误地允许了 token "icipant"(22505)——该 token 是另一个 enum 值 "participant of" 的子串
- **为什么 finetuned 模型没问题**: w8 实验的 finetuned 模型在该 context 下对 token 22505 的概率接近 0，bug 不会触发；phase2 的 base model 熵更高，偶尔命中
- **论文可报**: 可以声明 "RV≈0% under grammar constraint"，脚注标注 5 个 XGrammar tokenizer edge case

---
