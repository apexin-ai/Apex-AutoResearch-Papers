# prep swebench eval readiness

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_swebench_eval_readiness_20260514T080045_result.json`
- **Structured JSON:** [`2a5abc6caca1792767e0.json`](../../sessions/2a/2a5abc6caca1792767e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/swebench_eval_readiness.md`。

**总结**: 11 项检查中 10 项通过，唯一缺失项是 `dataflow_aware_s42` checkpoint（等 M2 训练完成）。pipeline 其余部分完全就绪：

- 数据（300 test instances）和 HF 缓存就绪，12/12 repos 已 clone
- 评估脚本、所有 Python 依赖、基座模型、random_s42 checkpoint 均到位
- 2× RTX PRO 6000 Blackwell (98GB)，磁盘余 90GB，资源充足
- 预估评估耗时 2.5-5 小时（300 instances, 含 repo checkout + batch encoding）
- 可立即用 random_s42 跑 baseline，或先 `--dry-run` 验证 pipeline 逻辑

---
