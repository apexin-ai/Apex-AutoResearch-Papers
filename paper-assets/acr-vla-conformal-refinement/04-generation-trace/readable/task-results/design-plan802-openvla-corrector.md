# design plan802 openvla corrector

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_design_plan802-openvla-corrector_20260517T224214_result.json`
- **Structured JSON:** [`b7fd33e28f4d41770153.json`](../../sessions/b7/b7fd33e28f4d41770153.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/plan802_architecture.md`。

核心设计决策：

1. **Feature extraction**: 用 OpenVLA vision backbone 的 pre-projector output `[256, 2176]` mean-pool 到 `[2176]`，再投影到 512D。选 pre-projector 而非 post-projector(4096D) 是因为前者保留更多空间/几何信息，后者已被 LLM embedding 空间扭曲。

2. **Corrector**: 3 层 MLP，输入 519D (512 obs + 7 action)，输出 7D delta，ε-clipped (默认 0.15)。~1.3M 参数，zero-init 最后一层。

3. **关键 tradeoff**: 丢失所有 conformal 保证（无 K 样本 → 无不确定性估计 → 无覆盖率保证），但 obs_only 本身就是 SmolVLA 实验中最强变体，conformal features 反而引入噪声。

4. **时间线**: 数据收集 ~3h (4×4090 并行 OpenVLA 推理)，训练 <5min，评估 ~6h。总计 5-7 天可完成全流程。

5. **最大风险**: OpenVLA 在 LIBERO-Object 上的 baseline 太弱（如 <5% 成功率），residual correction 无法挽救。需 Day 3 先确认 baseline。

---
