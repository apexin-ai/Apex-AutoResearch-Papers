# ssh gpu0 v5 resilient

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu0-v5-resilient_20260514T024204_result.json`
- **Structured JSON:** [`58997d05028938b3a05f.json`](../../sessions/58/58997d05028938b3a05f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，运行正常。

### 产出汇总

| 项目 | 状态 |
|------|------|
| **GPU0 残留进程** | 无需清理（唯一进程 PID 558609 在 GPU1 上） |
| **旧 tmux sessions** | 已清理 (plan-001b-gpu0-v4, v4-fix) |
| **lifespan-longest-lived 去重** | 21 → 19 条，有效 episodes: 0-18，**还差 1 个** (ep19) |
| **measure-melting-point** | 目录不存在，从零开始 (20 eps) |
| **episodes.jsonl** | 150GB，无法内存去重，跳过 |
| **新进程** | tmux: `plan-001b-gpu0-v5`，训练 PID: **698985**，脚本 PID: 698971/698974 |
| **GPU 显存** | GPU0: 28013/32607 MiB（vLLM 已加载），GPU1: 28013/32607 MiB |
| **运行状态** | vLLM 推理中，measure-melting-point ep0 正在执行，输出速度 ~97 toks/s |

启动命令：
```
tmux new-session -d -s plan-001b-gpu0-v5 "bash /tmp/run_gpu0_v5.sh 2>&1 | tee ~/runs/simgate-modular-routing/plan-001b-gpu0-v5.log"
```

任务顺序：measure-melting-point (20 eps) → lifespan-longest-lived ep19 (补齐到 20)。

---
