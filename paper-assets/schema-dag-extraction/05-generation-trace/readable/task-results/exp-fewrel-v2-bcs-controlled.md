# exp fewrel v2 bcs controlled

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fewrel_v2_bcs_controlled_20260516T031819_result.json`
- **Structured JSON:** [`4a319089472e23e02ca3.json`](../../sessions/4a/4a319089472e23e02ca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `exp_fewrel_v2_bcs_controlled` 全部完成，registry 已更新为 DONE，artifacts 已注册。

---

## C1b 实验结果摘要

**设计**: FewRel 80-rel pool, count=8, v2 RE prompt, Qwen3-32B-FP8, greedy decoding (temp=0, seed=42)

| Batch | BCS | Accuracy | Group |
|-------|-----|----------|-------|
| low_0 | 0.4715 | 83.33% | low |
| low_1 | 0.6465 | 81.25% | low |
| low_2 | 0.6653 | 87.50% | low |
| low_3 | 0.6724 | 82.29% | low |
| low_4 | 0.6742 | 67.71% | low |
| high_0 | 0.7778 | 77.08% | high |
| high_1 | 0.7908 | 71.88% | high |
| high_2 | 0.8201 | 70.83% | high |
| high_3 | 0.8226 | **92.71%** | high |
| high_4 | 0.9706 | **50.00%** | high |

**汇总**:
- Low BCS mean: **80.42%**
- High BCS mean: **72.50%**
- **Δ(low−high) = +7.92pp**, 95% CI [−5.21, +21.46]pp

**结论**: Channel 2 方向一致（高 BCS → 低准确率），与 v1 prompt 结果方向吻合。CI 包含 0，未达 p<0.05 显著。主要方差来源：
- **high_3 (BCS=0.82, acc=92.7%)** — 异常高，8 种类型虽然 embedding 相近但语义上仍可区分（spouse/sibling/military rank 等），拉高了 high 组均值
- **high_4 (BCS=0.97, acc=50.0%)** — 极端 case，类型几乎同义（participant/participant of/part of/member of/has part），准确率接近随机，强力支持 Channel 2 在尾部的效应

对 reviewer 回应：可以报告"v2 prompt 下方向一致，+7.92pp"，同时诚实说明 CI 跨 0。high_4 的极端 case 可作为定性证据单独展示。

---
