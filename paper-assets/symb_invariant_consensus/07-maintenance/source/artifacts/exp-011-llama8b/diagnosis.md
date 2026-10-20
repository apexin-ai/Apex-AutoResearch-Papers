# exp-011-llama8b 失败诊断

## 失败根因

GPU 显存被已有 vLLM 进程（PID 174585, VLLM::EngineCore, 占用 83548 MiB）霸占，exp-011 启动时仅剩 12.83 GiB 空闲，无法满足 gpu_memory_utilization=0.9 所需的 85.47 GiB。

## 完整 Traceback

```
(EngineCore pid=267167) File "/root/miniconda3/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 118, in __init__
    self.model_executor = executor_class(vllm_config)
  File "/root/miniconda3/lib/python3.12/site-packages/vllm/v1/executor/abstract.py", line 109, in __init__
    self._init_executor()
  File "/root/miniconda3/lib/python3.12/site-packages/vllm/v1/executor/uniproc_executor.py", line 47, in _init_executor
    self.driver_worker.init_device()
  File "/root/miniconda3/lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 283, in init_device
    self.requested_memory = request_memory(init_snapshot, self.cache_config)
  File "/root/miniconda3/lib/python3.12/site-packages/vllm/v1/worker/utils.py", line 413, in request_memory
    raise ValueError(
ValueError: Free memory on device cuda:0 (12.83/94.97 GiB) on startup is less than desired GPU memory utilization (0.9, 85.47 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes.
```

## 环境信息

- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (97887 MiB)
- 占用进程: PID 174585 (VLLM::EngineCore) 使用 83548 MiB
- vLLM 版本: 0.20.2
- 模型路径: /root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct (文件完整，4 shards ~14.9GB)

## 修复建议

1. **立即修复**: 终止占用显存的旧 vLLM 进程
   ```bash
   kill 174585
   ```
   然后重新运行 exp-011。

2. **脚本改进**: 在启动脚本 Step 1 前加入显存检查/清理逻辑：
   ```bash
   # Kill any existing vLLM processes before starting
   pkill -f "vllm.entrypoints" 2>/dev/null || true
   sleep 5
   ```

3. **防御性选项**: 若未来需要与其他进程共存，可降低 `--gpu-memory-utilization` 到 0.15 左右（仅 8B 模型 bf16 约需 16GB），但当前场景应独占 GPU。
