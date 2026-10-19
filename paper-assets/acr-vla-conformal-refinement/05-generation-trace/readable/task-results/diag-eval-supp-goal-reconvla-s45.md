# diag eval supp goal reconvla s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-supp-goal-reconvla-s45_20260523T225731_result.json`
- **Structured JSON:** [`786eabd3a6ae02fe5c73.json`](../../sessions/78/786eabd3a6ae02fe5c73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：假警报，实验已正常完成。**

- **根因**：eval 脚本将结果写入本地 JSON 文件而非 W&B，cron 监控以 W&B metrics 作为成功信号，因此误报失败
- **实际结果**：SR = 85.5%（171/200），所有 10 个 task 全部跑完，无任何 error/OOM/磁盘问题
- **Registry 状态**：已标记为 DONE，conclusion=success
- **无需重跑**

诊断报告已写入 `artifacts/diag-eval-supp-goal-reconvla-s45.md` 并注册。建议后续更新 cron 监控逻辑，增加对本地 JSON 输出的检测作为备用成功信号。

---
