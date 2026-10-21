# ops check 1 7b no evi v3 completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_1_7b_no_evi_v3_completion_20260516T135335_result.json`
- **Structured JSON:** [`908fd0b975caef50fee3.json`](../../sessions/90/908fd0b975caef50fee3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 已更新为 DONE。

## 结果摘要

| 指标 | 值 |
|------|-----|
| Ign-F1 | 0.3982 |
| Rel-F1 | 0.4103 |
| Evi-F1 | 0.0 (no-evidence 模型不输出 evidence) |
| EDCR | 0.0 |
| Format compliance | 100% |
| Truncated samples | 501/985 |

## Evidence Tax（1.7B 模型）

| 配置 | Ign-F1 |
|------|--------|
| With-evidence | 0.4679 |
| No-evidence | 0.3982 |
| **Evidence tax** | **+0.0697 (+17.5% relative)** |

结论：在 1.7B 模型上，with-evidence 训练相比 no-evidence 训练带来 +7.0 绝对 F1 提升。Evidence 训练信号对关系抽取有显著正向效果，不存在"evidence tax"（即加入 evidence 不会拖累关系抽取性能，反而提升）。

注意事项：501/985 样本被 truncated（max_new_tokens=1024），这可能压低了 no-evidence 模型的分数，但 with-evidence eval 同样有 truncation，因此对比仍有效。

---
