# analysis action divergence run

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action_divergence_run_20260517T102711_result.json`
- **Structured JSON:** [`976739c92b86d6dda41d.json`](../../sessions/97/976739c92b86d6dda41d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动成功。**

- **tmux session**: `action_divergence`
- **PID**: 422618
- **GPU**: CUDA_VISIBLE_DEVICES=1
- **进度**: Task 0 已跑完 3/5 episodes，每 episode ~8 秒
- **配置**: 3 tasks × 5 episodes × 280 steps = 15 episodes 总计
- **预计运行时间**: ~2-3 分钟（15 episodes × ~8s/ep ≈ 120s + 模型加载 + 图表生成）

早期数据：Task 0 ("pick up alphabet soup → basket") 的 final L2 divergence 在 1.67–1.90 范围，说明 pruned 模型在 episode 末尾与 baseline 有显著 action 偏移。

---
