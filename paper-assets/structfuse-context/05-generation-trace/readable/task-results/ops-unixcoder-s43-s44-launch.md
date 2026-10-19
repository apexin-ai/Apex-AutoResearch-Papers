# ops unixcoder s43 s44 launch

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_unixcoder_s43_s44_launch_20260516T093158_result.json`
- **Structured JSON:** [`ee686a6cbddfda4d6a6a.json`](../../sessions/ee/ee686a6cbddfda4d6a6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动并验证。

**总结：**

| 项目 | 值 |
|------|-----|
| 脚本 | `/root/structfuse/scripts/run_unixcoder_s43_s44_chain.sh` |
| Seeds | 43 → 44（顺序执行） |
| Patience | 2（两个脚本均确认） |
| Strategies | random, embedding_distance, dataflow_aware |
| 输出目录 | `/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/{strategy}_s{43,44}/` |
| GPU | cuda:0，当前 UniXcoder 进程 ~16 GiB × 2（两个 GPU 各一个） |
| tmux session | `unixcoder-3strat-s43` |
| 日志 | `~/runs/structfuse-context/unixcoder-3strat-s43.log` |
| 超时 | 12h |

GPU 进程已确认：cuda:0 上有 PID 164287 占用 16044 MiB（UniXcoder s43 第一个 strategy 已开始训练）。Qwen 主链（~50 GiB）共存无冲突。

---
