# deploy spatial s47 5gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_spatial-s47-5gpu_20260524T104342_result.json`
- **Structured JSON:** [`5651be71deccdc7ec461.json`](../../sessions/56/5651be71deccdc7ec461.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验启动成功，python 进程都在运行（高 CPU 占用 = 模型加载/推理中）。

## 启动确认

| Method | 服务器 | GPU | tmux session | Python PID |
|--------|--------|-----|--------------|------------|
| vla-only | cqa1-32758 | cuda:0 | spatial-vla-s47 | 844299 |
| crm | cqa1-32758 | cuda:1 | spatial-crm-s47 | 844581 |
| adapt | cqa1-32758 | cuda:2 | spatial-adapt-s47 | 844595 |
| k2mean | cqa1-32758 | cuda:3 | spatial-k2mean-s47 | 845121 |
| reconvla | bjb2-40593 | cuda:0 | spatial-reconvla-s47 | 261844 |

日志位置：
- cqa1-32758: `/tmp/eval_spatial_{vla,crm,adapt,k2mean}_s47.log`
- bjb2-40593: `/tmp/eval_spatial_reconvla_s47.log`

注：首次启动因为 tmux session 内 PATH 没有 conda，5 个进程立即退出（`python: command not found`）；已用 `bash -lc 'source conda.sh && conda activate base && ...'` 重启成功。所有进程都已通过 args 解析阶段进入模型加载。

---
