# check gpu5090x4 pid investigation

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu5090x4_pid_investigation_20260514T115801_result.json`
- **Structured JSON:** [`82c6e90fa3c63d351a12.json`](../../sessions/82/82c6e90fa3c63d351a12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

四张卡被 **两个 vLLM 推理服务** 占满，都是 root 用户启动：

| GPU | PID | 进程 | 模型 | 端口 | 运行时间 | GPU利用率 |
|-----|-----|------|------|------|----------|-----------|
| 0, 1 | 33642, 33643 | vLLM (TP=2) | **DeepSeek-R1-Distill-Qwen-14B** | 8001 | 2h33m | 99% |
| 2, 3 | 41815, 41816 | vLLM (TP=2) | **Qwen2.5-14B-Instruct** | 8002 | 1h19m | 0% |

两个实例都设置了 `--gpu-memory-utilization 0.90`，所以显存预分配近满。

GPU 0+1 利用率 99% 是因为有一个 **`svs_pipeline.run_mvp`** 进程（PID 37622，运行 ~2h）正在调用 port 8001 的 DeepSeek 模型做推理。

GPU 2+3 利用率 0% 是因为 Qwen2.5 服务虽然启动了但当前无请求，显存被预占但 GPU 空闲。

两个 vLLM 服务都是本项目 `svs_formal_verification` 的工作进程。

---
