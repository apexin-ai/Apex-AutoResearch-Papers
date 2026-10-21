# research paper framing update d078 d083

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-framing-update-d078-d083_20260516T154301_result.json`
- **Structured JSON:** [`535429c83409dab987aa.json`](../../sessions/53/535429c83409dab987aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。主要变更：

**结构性变更:**
- 新增 **Claim 5 (Scaling)**: Evidence Tax U-shape pattern（1.7B +6.2pp / 4B -7.9pp / 8B ≈0 / LLaMA-8B -0.7pp）
- 新增三个子表：D076 rel_f1 统一协议、Evidence Tax Scaling、Cross-Dataset Validation

**C1 更新:** evidence tax 从固定 "~7pp" 改为 pointer 到 C5 的 scale-dependent 叙事；写入 D076 最终数字、LLaMA cross-family 和 Re-DocRED cross-dataset 结果

**C3 降级:** 标题改为 "CED 与 flat-NLI 统计不可区分（D078）"；写入 p=0.44、Δ=0.0008；叙事改为 "NLI-based scoring 是关键，CED 因可解释性作为默认推荐"

**Story Arc:** 第 3 点改为 scale-dependent 叙事，新增第 10 点 scaling & generalization

**RC 更新:** RC3 标记已解决，RC12 新增 D079/D083 弹药（1.7B evidence 有益与 SAIS 方向一致），RC13 三项泛化实验全标记完成

**优先级:** seed 实验标记为不再需要，三项泛化实验标记完成，Publishability Threshold 更新

---
