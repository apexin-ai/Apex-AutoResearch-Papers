# diag exp 068 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-068-status-check_20260519T114110_result.json`
- **Structured JSON:** [`a3b273c4918386529986.json`](../../sessions/a3/a3b273c4918386529986.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**exp-068 正在运行中**，resource tracking 未检测到是因为实验脚本本身是 CPU 进程（通过 HTTP 调用 vLLM API），不直接占用 GPU。

### 运行状态
- **进度**: 49/200 完成，正在处理第 50 题 (logiqa_049)
- **ETA**: 约 87 分钟（日志显示 151 remaining）
- **当前准确率**: SICA 81.63%, SC 81.63% (前 49 题)
- **启动时间**: 19:13 (vLLM 19:08 启动)

### GPU 使用
| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | **空闲** | 0MiB | 0% |
| 1 | vLLM EngineCore (PID 142896) | 88278MiB | 79% |
| 2 | vLLM EngineCore (PID 125544) | 88246MiB | 96% |
| 3 | vLLM EngineCore (PID 76474) | 88254MiB | 96% |

注意：GPU 0 未被使用。exp-068 的 vLLM 在 GPU 1 上（port 8001, serving Qwen3-14B）。GPU 2-3 上的 vLLM 进程属于其他实验。

### tmux sessions (共 6 个)
| Session | 创建时间 |
|---------|----------|
| exp048_vllm | 10:19 |
| exp048_run | 10:20 |
| exp064_vllm | 16:44 |
| exp064_run | 16:56 |
| **exp068_vllm** | **19:08** |
| **exp068_run** | **19:13** |

### vLLM 服务
- `localhost:8001` — Qwen3-14B (`/root/autodl-tmp/models/Qwen3-14B`)，max_model_len=40960

### 结论
exp-068 正常运行中，registry 标记 RUNNING 是正确的。resource tracking 没检测到是因为它只追踪了 GPU 0，而 vLLM 实际部署在 GPU 1 上。预计约 87 分钟后完成全部 200 题。

---
