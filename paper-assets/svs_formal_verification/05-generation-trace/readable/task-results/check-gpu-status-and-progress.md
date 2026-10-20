# check gpu status and progress

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_and_progress_20260514T113729_result.json`
- **Structured JSON:** [`a03d49d2256f3cee5248.json`](../../sessions/a0/a03d49d2256f3cee5248.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**1. GPU 状态**
```
0, 99 %, 31459 MiB, 32607 MiB
1, 99 %, 31459 MiB, 32607 MiB
2, 0 %, 31401 MiB, 32607 MiB
3, 0 %, 31401 MiB, 32607 MiB
```

**2. mvp_003 进度（gold_label 计数）**
```
19
```

**3. vLLM 进程**
```
# DeepSeek-R1-Distill-Qwen-14B (GPU 0,1, port 8001)
PID 33091  2.5%CPU  python -m vllm.entrypoints.openai.api_server --model .../DeepSeek-R1-Distill-Qwen-14B --tensor-parallel-size 2 --port 8001 --dtype float16 --gpu-memory-utilization 0.90
PID 33642  96.1%CPU  VLLM::Worker_TP0
PID 33643  49.1%CPU  VLLM::Worker_TP1

# Qwen2.5-14B-Instruct (GPU 2,3, port 8002)
PID 41281  1.1%CPU  python -m vllm.entrypoints.openai.api_server --model .../Qwen2___5-14B-Instruct --tensor-parallel-size 2 --port 8002 --max-model-len 4096 --dtype auto --gpu-memory-utilization 0.90
PID 41815  16.8%CPU  VLLM::Worker_TP0
PID 41816  10.8%CPU  VLLM::Worker_TP1
```

**4. mvp_003 进程**
```
 37622    01:46:31  0.7  0.0
```

---
