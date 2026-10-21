# analysis d108 q4q5 answers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d108_q4q5_answers_20260516T074449_result.json`
- **Structured JSON:** [`dc86d487cd6f2beb6750.json`](../../sessions/dc/dc86d487cd6f2beb6750.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。输出文件保存在 `/root/autodl-tmp/struct_self_consist_ie/output/d108_q4q5/`。

**Q4 核心结论** — CoNLL entity-token LP variance ≈ 0 的三个原因：
1. **Entity set 一致性高**：CoNLL mean Jaccard = 0.87（median = 1.0），模型跨 sample 提取几乎相同的 entity set；SciERC 仅 0.66（边界模糊）
2. **Entity token 短且高频**：CoNLL PER/LOC/ORG 平均 2-4 tokens，都是常见专有名词，logprob ≈ 0；SciERC 含稀有科学术语 subword
3. **Per-type tied 率**：CoNLL LOC/ORG 60%+ instances tied（var < 1e-8），SciERC OtherScientificTerm 仅 18%。CoNLL 的 MISC 是异类（36% tied），行为接近 SciERC

**Q5 核心结论**：
- **SciERC**: 4B 比 8B 更 diverse（diversity ratio 0.52 vs 0.43），50% instances 4B 更多样
- **CoNLL**: 归一化后 diversity ratio 几乎相同（0.143 vs 0.142），raw unique 差异仅因 8B 有 16 samples vs 4B 的 8
- **Diversity 与 F1 负相关**：高 diversity instances 的 majority vote F1 低 0.15-0.23，diversity 反映模型不确定性

---
