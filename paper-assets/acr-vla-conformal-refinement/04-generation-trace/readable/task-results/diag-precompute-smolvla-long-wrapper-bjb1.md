# diag precompute smolvla long wrapper bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_precompute-smolvla-long-wrapper-bjb1_20260522T185039_result.json`
- **Structured JSON:** [`2b2e18f7629beac7e7f4.json`](../../sessions/2b/2b2e18f7629beac7e7f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：误报（False Positive）

**任务实际已成功完成。**

**根因**：监控系统日志路径不匹配。
- 监控期望的日志路径：`~/runs/.../precompute-smolvla-long-wrapper-bjb1.log`（不存在）
- 实际日志路径：`/root/autodl-tmp/logs/precompute_long_k10.log`
- 监控找不到日志、sentinel、W&B 三样证据，5 次检测后自动判定失败

**实际运行结果**：
- 54,059 samples 全部处理完成（200 trajectories, 51.8 分钟）
- 12 项验证全部 PASS（shape、NaN、Inf、diversity）
- 产出路径 `/root/autodl-tmp/crm_cache_smolvla_k10/long/`，15GB，含 `obs_features.pt` + `k_samples.pt` + `expert_actions.pt` + `manifest.json`

**建议**：无需重跑，将实验状态改为 completed。后续提交任务时确保日志路径与监控路径一致。

---
