# ssh check gpu0 v3 progress

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu0-v3-progress_20260514T015751_result.json`
- **Structured JSON:** [`766d214fdfe559f495bc.json`](../../sessions/76/766d214fdfe559f495bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度报告

### 结论：v3 尚未启动，v2 在 09:47 崩溃

**v2 崩溃点**：跑到第 4 个 task `lifespan-longest-lived` 的 episode 15 时，VLLM EngineCore 进程意外死亡（`EngineDeadError`）。v2 是一个覆盖 7 个 task 的大 run，依次完成了 find-animal、identify-life-stages-1、lifespan-longest-lived-then-shortest-lived 后，在 lifespan-longest-lived 崩溃。

**v3 状态**：`run_gpu0_v3.sh` 脚本已存在但**从未被启动**（`/root/runs/` 下无 v3 log 文件）。

### plan_c 数据产出

| Task | 状态 | episodes.jsonl |
|------|------|----------------|
| lifespan-longest-lived | v2 部分完成 | 16 行（5 reuse + 11 collected，缺 ep 16-19） |
| measure-melting-point-unknown-substance | 未开始 | 不存在 |
| freeze | 未开始 | 不存在 |
| chemistry-mix | 未开始 | 不存在 |

### GPU 状态

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| GPU0 (RTX 5090) | 28013 / 32607 MiB | 0% | 僵尸 VLLM::EngineCore (PID 544942)，v2 崩溃残留 |
| GPU1 (RTX 5090) | 0 / 32607 MiB | 0% | 空闲 |

### 对拆分决策的建议

4 个 task 全部未完成，可以自由分配。GPU0 上的僵尸 VLLM 进程需要先 kill 掉才能重启。GPU1 完全空闲，可以立即使用。

---
