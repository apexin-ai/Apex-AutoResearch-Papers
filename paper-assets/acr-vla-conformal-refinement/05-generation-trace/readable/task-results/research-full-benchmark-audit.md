# research full benchmark audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_full-benchmark-audit_20260520T071731_result.json`
- **Structured JSON:** [`7f5c589381d62b9f5762.json`](../../sessions/7f/7f5c589381d62b9f5762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存到 `artifacts/benchmark_data_audit.md` 并注册 (`art_20260520_8e3ba4`)。

核心结论：

- **0 个数值不匹配** — 所有 script 与 registry 共有的 seed，SR 值完全一致
- **9/15 组数据完美匹配**（含 Long-CRM、Goal-VLA、Object-K5、Object-VLA、Argmin 等）
- **8 个 seed 的 registry 状态异常**（数据有效但 status 不是 DONE+success）：
  - VLA-Spatial seed48/49: conclusion=failed（数据来自 Director 指令）
  - VLA-Long seed49: status=PREPARING，无 SR（**最高风险，数据不可验证**）
  - CRM-Goal seed47: status=PREPARING，SR=0.69 已在 metrics 中
  - 4 个 Adaptive-K: status=ALLOCATED 应为 DONE
  - Object norm01 seed42: status=DEPLOYED 应为 DONE
- **1 个被排除的 registry seed**: Object CRM norm02 K=10 seed42 (SR=0.22 是离群值)

**建议优先处理**: VLA-Long seed49（无法验证）和 VLA-Spatial seed48/49（registry 标记为 failed）。

---
