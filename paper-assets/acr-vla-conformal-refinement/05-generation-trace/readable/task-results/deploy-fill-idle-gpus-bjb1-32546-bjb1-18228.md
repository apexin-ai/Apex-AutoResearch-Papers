# deploy fill idle gpus bjb1 32546 bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill-idle-gpus-bjb1-32546-bjb1-18228_20260525T080319_result.json`
- **Structured JSON:** [`775584414203b02324db.json`](../../sessions/77/775584414203b02324db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署结果

### ✅ 任务 1: bjb1-32546 cuda:3 — eval-smolvla-crm-goal-seed44
- PID 70782，GPU 显存占用 5609 MiB
- 日志显示已加载 SmolVLA + CRM checkpoint，10 个 Goal 任务已加载，进入 rollout 阶段
- Registry 已转为 RUNNING（PENDING → QUEUED → RUNNING）

### ⚠️ 任务 2: bjb1-18228 cuda:2 — **未部署（重复实验，已 kill）**

**关键发现**：`eval-pi05-vla-only-goal-s43` 在 registry 中已是 **DONE** 状态：
- 完成时间：2026-05-25 00:37（约 7.5 小时前）
- 执行服务器：bjb1-32546 cuda:4
- 结果：**overall_success_rate = 0.97**（200 rollouts / 10 tasks）
- 同 seed、同 benchmark、同模型 → 重复运行结果一致，纯属浪费 GPU

已 kill bjb1-18228 上刚启动的 pi05 进程（PID 518504），GPU 2 已释放至 1 MiB used。

**建议**：如需在 bjb1-18228 cuda:2 填充 idle GPU，请改派其他未完成的实验（例如其他 seed 的 π0.5 评估、或 CRM 相关变体）。Director 可能下发任务时未检查 registry DONE 状态。

---
