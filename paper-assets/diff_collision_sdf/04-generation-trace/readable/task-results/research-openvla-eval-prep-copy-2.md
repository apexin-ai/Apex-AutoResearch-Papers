# research openvla eval prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla_eval_prep_20260523T051238_result.json`
- **Structured JSON:** [`bf24023a5ea65b076424.json`](../../sessions/bf/bf24023a5ea65b076424.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项产出完成：

1. **调研报告**: `artifacts/openvla_eval_prep.md` — OpenVLA 模型信息、LIBERO 兼容性分析、预期结果
2. **Eval 脚本**: `artifacts/eval_openvla_safelibero.py` — 完整框架，与现有 displacement pipeline 对齐，新增 `fake_safe_rate` 和 `mean_action_magnitude` 指标，7 处 `TODO: adapt` 标注
3. **Memory 更新**: `memory.md` 记录了调研结论和适配要点

**核心判断**: OpenVLA zero-shot 是验证 fake safety 的理想选择。LIBERO 不在其训练数据中 → TSR≈0%，但 action collapse 会导致 CAR 虚高至 80-100%，frozen_rate 60-90%。这与 Pi0.5 和 baseline 的 fake safety 现象一致，为论文 claim 提供第三个独立模型的证据。

**适配工作量约半天**：主要是 action rotation 格式转换 (roll/pitch/yaw → axis-angle)、图像方向确认、action scaling，都不难。

---
