# grounding-prompt-ablation 失败诊断

## 错误类型
**GPU OOM (显存被占用)**

## 根因
GPU 0 上存在残留 vLLM 进程 (PID 165113, `VLLM::EngineCore`)，占用 29508 MiB / 32607 MiB 显存。实验脚本尝试在 GPU 0 上初始化新的 vLLM 引擎时，仅剩 2.04 GiB 可用，远低于所需的 28.22 GiB (gpu_memory_utilization=0.9)，触发 ValueError 后崩溃。

GPU 1 (RTX 5090, 32607 MiB) 完全空闲，未被使用。

## Traceback

```
ValueError: Free memory on device cuda:0 (2.04/31.36 GiB) on startup is less than
desired GPU memory utilization (0.9, 28.22 GiB). Decrease GPU memory utilization or
reduce GPU memory used by other processes.
```

调用链:
```
main() -> run_task() -> run_episode_internal() -> agent.select_action_react()
-> _generate() -> _generate_vllm() -> _load_vllm() -> LLM() -> vllm init_device
-> request_memory() -> ValueError
```

## 部分结果
无可用结果。脚本在第一个 task (chemistry-mix) 的第一个 episode 就失败了，`results/grounding_prompt_ablation/chemistry-mix/` 目录为空。

## 修复建议

1. **Kill 残留进程后重试**: `kill 165113` 释放 GPU 0 显存，然后用原命令重跑
2. **或改用 GPU 1**: 将 `--gpu_id 0` 改为 `--gpu_id 1`，利用空闲的 GPU 1
3. **长期建议**: 在脚本启动前加 GPU 可用显存检查，或在实验 runner 中加入自动清理逻辑
