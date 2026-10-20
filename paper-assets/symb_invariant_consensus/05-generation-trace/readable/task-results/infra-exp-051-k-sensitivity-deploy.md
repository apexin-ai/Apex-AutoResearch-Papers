# infra exp 051 k sensitivity deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp-051-k-sensitivity-deploy_20260518T225859_result.json`
- **Structured JSON:** [`9a9503c55e1f2d970fbc.json`](../../sessions/9a/9a9503c55e1f2d970fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`exp051` session 运行中。脚本设计为先等 120s 加载 vLLM，之后串行跑 K=4/8/16/20。

**部署总结：**
- GPU 0 已清空，Mistral-7B vLLM 正在启动（port 8000）
- tmux session: `exp051`
- 串行 4 组 K 值（4→8→16→20），每组 204 题 FOLIO
- 输出: `results/exp051_mistral_k_sensitivity/k{4,8,16,20}/`
- Registry: `exp-051-mistral-k-sensitivity` → RUNNING
- 预估总时长 ~3h

---
