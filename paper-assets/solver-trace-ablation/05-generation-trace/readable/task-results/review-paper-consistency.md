# review paper consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper-consistency_20260515T041641_result.json`
- **Structured JSON:** [`b5747e2f6be03c0f8bf3.json`](../../sessions/b5/b5747e2f6be03c0f8bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。结果：

- **124 个定量声明已检查**
- **116 个一致**，0 个关键错误
- **1 个轻微不一致**："200× collapse" 实际应为 ~214× (0.6423/0.003)
- **7 个无法仅从 registry 验证**（需要 eval 输出文件），包括 random β=0.1 s43 的 ISR*=0.058、500 步组件数 6.58、1000 步 94.8% ISR=0 等

所有主表（Table 1、Table 2）、附录详细表、3-seed 聚合统计（mean±std）、关键叙事数据点（64.5% vs 0%、1.06×、99.5% 退化、σ=±47pp）均与 registry 一致。D051/C006 等约束全部满足。

报告已写入 `artifacts/paper_consistency_audit.md` 并注册。

---
