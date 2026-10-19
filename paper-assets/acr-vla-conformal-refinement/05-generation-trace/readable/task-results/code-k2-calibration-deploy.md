# code k2 calibration deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_k2-calibration-deploy_20260519T202852_result.json`
- **Structured JSON:** [`2e1bc19ff67adff64bb5.json`](../../sessions/2e/2e1bc19ff67adff64bb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已启动并注册。

**修改内容**：在 `compute_k10_variance()` 中利用已有的 K=10 samples 计算所有 C(10,2)=45 对的 L2 距离均值（向量化实现），存入 `k2_l2` 字段，最后输出 3 组 Spearman ρ：
- ρ(FMVD, K10_var) — 原有
- ρ(K2_L2, K10_var) — 核心 go/no-go 指标
- ρ(K2_L2, FMVD) — 两信号间关系

**运行状态**：模型已加载，10 tasks 就绪，正在 bjb2-28827 cuda:1 上跑。PID=995735，日志在 `/tmp/k2_l2_calibration.log`，结果输出到 `logs/k2_l2_calibration.json`。

---
