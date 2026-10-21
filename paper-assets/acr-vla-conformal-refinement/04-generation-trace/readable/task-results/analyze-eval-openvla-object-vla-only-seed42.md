# analyze eval openvla object vla only seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-openvla-object-vla-only-seed42_20260517T180313_result.json`
- **Structured JSON:** [`18ca0132a4b74a217c9d.json`](../../sessions/18/18ca0132a4b74a217c9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析完成

**结果：OpenVLA VLA-only 在 LIBERO-Object 上 0.0% 成功率（0/100 episodes）。**

### 关键发现

| Method | Success Rate |
|--------|-------------|
| SmolVLA VLA-only (K=1) | 10.8% |
| **OpenVLA VLA-only (K=1)** | **0.0%** |
| SmolVLA + obs_only CRM | 17.5% |

所有 10 个 task 均为 0/10。实验本身运行正常（无 crash，EXIT_CODE=0，推理速度稳定 178ms/step），模型在产生 action 但全部无效。

### 需要关注的问题

0% 结果异常低。OpenVLA 是 7B 模型，理论上应优于 0.4B 的 SmolVLA。可能原因：
1. 该 fine-tuned checkpoint 训练不充分或未收敛
2. Action unnormalization 配置问题（虽然 `unnorm_key=libero_object` 已设置）
3. OpenVLA 原论文在 LIBERO 上有正面结果，需要核查差异来源

### 建议下一步

在 OpenVLA 上构建 CRM 之前，先验证 checkpoint 质量（查看训练日志/loss 曲线）。如果 checkpoint 确认有效，则 0% baseline 反而是 CRM 的极端测试场景。

---
