# diagnose behavioral pilot w4

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_behavioral_pilot_w4_20260518T103243_result.json`
- **Structured JSON:** [`4e87ccae4038cd6f3935.json`](../../sessions/4e/4e87ccae4038cd6f3935.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/behavioral_pilot_w4_diagnosis.md`。

核心结论：

- **失败原因**：SSH 连接断开导致级联终止（SIGHUP→SIGTERM），不是 OOM 或脚本 bug
- **进度**：仅完成 6/60 episodes (10%)，Task 0 baseline ep 0-5 全部 fail (R=0.000)
- **无 W&B**：脚本本身没有 wandb 集成，只写 JSON
- **可直接重跑**：环境完整，GPU 空闲
- **关键风险**：baseline 成功率为 0，重跑前建议先排查 `unnorm_key="bridge_orig"` 是否正确匹配 LIBERO 的 action space，否则 85 分钟跑完也拿不到有意义的对比数据

---
