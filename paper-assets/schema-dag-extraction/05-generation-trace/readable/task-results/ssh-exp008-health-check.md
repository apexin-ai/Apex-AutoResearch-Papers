# ssh exp008 health check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp008-health-check_20260515T094541_result.json`
- **Structured JSON:** [`39c50c0d10527ccf63d8.json`](../../sessions/39/39c50c0d10527ccf63d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：进程卡死

### GPU 状态
- **RTX PRO 6000 Black** (98GB), GPU-Util **0%**, 显存 **669MiB / 97887MiB** (0.7%)
- 唯一 GPU 进程: `VLLM::EngineCore` (PID 241610) 占 660MiB

### 进程状态
| PID | 进程 | 状态 | 说明 |
|-----|-------|------|------|
| 241208 | bash wrapper | S (sleeping) | 等待子进程 |
| 241213 | run_exp008.sh | S (sleeping) | 等待子进程 |
| 241217 | python3 run_sdgd_experiment.py | S (sleeping) | wchan=`do_poll` (等待子进程 IPC) |
| 241610 | VLLM::EngineCore | S (sleeping) | wchan=`futex_wait_queue_me` (死锁) |

### 日志分析
- 日志仅 **31 行**，最后输出时间 **15:45:50**（2 小时前）
- 停在 vLLM v0.20.2 引擎初始化阶段（parallel_state 初始化完成后）
- 模型权重加载 **未开始/未完成** — 32B FP8 模型应占 ~35GB 显存，实际仅 660MiB
- 无任何错误信息

### 结果文件
- `artifacts/exp008/` 仅有 `decomposition.json`（15:45 创建），无实验结果

### 诊断
**卡死**。vLLM EngineCore 在模型加载阶段 futex 死锁，主进程在 poll 等待 EngineCore 响应。2 小时无任何进展，不会自行恢复。

可能原因：vLLM 0.20.2 + Qwen3-32B-FP8 + `enforce_eager=True` 组合在 CUDA 13.1/Driver 590 上的兼容性问题，或模型加载时 NCCL/内存映射卡住。

### 建议操作
需要 kill 进程并重启。可尝试：
1. 去掉 `enforce_eager=True` 让 vLLM 用默认编译模式
2. 或降级到 vLLM 0.19.x 排除版本兼容问题

等 Director 决策。

---
