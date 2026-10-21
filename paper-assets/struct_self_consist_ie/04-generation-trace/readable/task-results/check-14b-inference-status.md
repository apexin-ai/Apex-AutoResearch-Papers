# check 14b inference status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_14b-inference-status_20260520T143619_result.json`
- **Structured JSON:** [`cda20de6f7b317030c96.json`](../../sessions/cd/cda20de6f7b317030c96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/14b_inference_status_check.md`。

## 状态总结

**进程运行情况**（与预期不同，实际是 shell 脚本循环 N∈{1,2,4,8,16}）：

| 任务 | GPU | 当前 N | 进度 | 预估剩余 |
|------|-----|--------|------|---------|
| **SciERC** | 3 (99%) | N=16 | 63% | 即将全部完成 |
| **CoNLL** | 1 (12%) | N=2 | 21% | ~2-3h 完成全部 N |
| **FewNERD** | 0 (98%) | N=1 | 13% (4886/37648) | 20-30h+ |

**已出结果 — 情况很差**：

- **SciERC** (N=1~8 已完): greedy F1 = **0.41%**，99%+ 样本 F1=0，全部 FAIL
- **CoNLL** (N=1 完): greedy F1 = **4.6%**，95% 样本 F1=0，FAIL
- Consistency signal (Fleiss/SJ) 与 F1 **负相关**（方向反了）
- 所有 report 建议降温到 T=0.7

核心问题：14B 模型在 FewNERD 上训练后，**跨数据集泛化几乎为零**。SciERC/CoNLL 的 F1 接近 0 说明模型输出格式可能与这两个数据集的 gold 不兼容，或者模型根本无法识别非 FewNERD 的实体类型。需要等 FewNERD 自身结果出来后对比确认。

---
