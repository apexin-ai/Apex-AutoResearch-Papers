# analysis actor entropy plan031

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_actor-entropy-plan031_20260514T110759_result.json`
- **Structured JSON:** [`4878681ae21b76b3ec75.json`](../../sessions/48/4878681ae21b76b3ec75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

1. **原始假设需修正** — collapsed 配置的 actor entropy 并非上升，而是**下降更慢**（008d 在 25K 步比 008c 高 3.11 nats）
2. **唯一 entropy 上升实例**：fixed_dt2 在 65K 步 entropy 从 -5.17 微升至 -5.12，恰好是 eval_return 从 360 崩塌至 133 的时刻
3. **最强诊断信号是 V/E ratio**，不是 entropy：008d 在 55K 步 V/E=1.67，fixed_dt2 在 65K 步 V/E=2.72，而所有 healthy 配置始终 < 0.6
4. **建议 C2 claim 修改为**：delusional critic 延缓 actor entropy 收敛，但 entropy 最终仍会下降——actor 变得确定性强但收敛到错误策略。V/E ratio 作为主指标，entropy delay 作为辅助证据

报告已注册为 artifact `analysis_actor_entropy_plan031`。

---
