# analysis controlb both

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_controlb_both_20260515T141111_result.json`
- **Structured JSON:** [`ad284cf31aee3331ad55.json`](../../sessions/ad/ad284cf31aee3331ad55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## Control B 结果

| 实验 | Best ρ (shuffled) | Best ρ (real) | 下降 |
|------|-------------------|---------------|------|
| **Trained OpenVLA** | 0.013 | 0.955 | −98.6% |
| **Untrained OpenVLA** | 0.009 | 0.933 | −99.0% |
| DINOv2 (参考) | 0.039 | 0.554 | −93.0% |

**Control B 验证通过。** 打乱标签后所有层 ρ≈0、R²为负、MAE 无改善，确认 trained/untrained OpenVLA probe 学到的是真实 temporal distance 信号。VLA 的 control B ρ（≈0.01）甚至比 DINOv2（0.039）更干净。

报告已注册为 artifact `art_20260515_95b0e2`，两个实验 registry 已更新为 DONE + metrics。

---
