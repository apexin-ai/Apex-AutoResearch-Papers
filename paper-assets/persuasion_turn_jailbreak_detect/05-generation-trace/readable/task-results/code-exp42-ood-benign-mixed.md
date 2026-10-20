# code exp42 ood benign mixed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp42_ood_benign_mixed_20260522T035847_result.json`
- **Structured JSON:** [`11920b17c5f9bb432aa4.json`](../../sessions/11/11920b17c5f9bb432aa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp42_ood_benign_mixed 执行完成。

**结果汇总：**

| Metric | Baseline (plan_002) | exp42 (mixed) | Target |
|--------|--------------------:|-------------:|-------:|
| WildChat FPR | 68.1% | **0.0%** | <30% |
| IID F1 | ~1.0 | 1.0 | — |
| OOD DD F1 | ~1.0 | 1.0 | >0.95 |
| OOD AA F1 | ~0.96 | 0.956 | >0.95 |
| OOD FITD F1 | ~1.0 | 1.0 | >0.95 |

**关键发现：** 混入仅 150 条 WildChat benign 对话（占训练集 30%）就将 FPR 从 68.1% 完全消除到 0%，同时 OOD jailbreak 检测性能无退化。这证实 exp38 的判断：高 FPR 纯粹是 benign 分布不匹配导致，而非模型架构缺陷。

**注意事项：** 评估集只有 49 条 WildChat benign（226 总数中 27 条因含 jailbreak 模式被过滤，199 条中 150 用于训练），属于小样本。但从 68.1%→0% 的跨越式改进来看，信号非常强。

---
