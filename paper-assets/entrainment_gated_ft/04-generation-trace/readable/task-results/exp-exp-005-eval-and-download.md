# exp exp 005 eval and download

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp-005-eval-and-download_20260522T162822_result.json`
- **Structured JSON:** [`ca31b12eb460ddd72420.json`](../../sessions/ca/ca31b12eb460ddd72420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已启动并运行中：

- **tmux session**: `exp-005-batch`，PID `902349`
- **后台下载**: DeltaNet pure 正在下载（fetching files）
- **前台评估**: HGRN h3-1 评估已开始（lm_eval 正在初始化）
- GPU 尚未被占用（模型还在加载阶段）

执行流程：
1. **并行下载**（后台）: DeltaNet pure → HGRN pure
2. **串行评估**（前台 GPU）: HGRN h3-1 → GLA pure → （下载完成后）DeltaNet pure → HGRN pure

日志文件: `/root/entrainment_gated_ft/results/exp005_zoo_expansion/eval_download.log`

---
