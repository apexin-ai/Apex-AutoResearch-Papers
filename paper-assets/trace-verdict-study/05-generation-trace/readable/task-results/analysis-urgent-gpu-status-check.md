# analysis urgent gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_gpu_status_check_20260518T221438_result.json`
- **Structured JSON:** [`443f59beb30eb47ad318.json`](../../sessions/44/443f59beb30eb47ad318.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Q1 nvidia-smi:
  cuda:0 — PID: 无活跃进程, 显存: 49.2G/97.9G, 利用率: 0%  ⚠️ 显存未释放但无进程
  cuda:1 — PID: 466403, 显存: 47.0G/97.9G, 利用率: 100%

Q2 qwen15b_exception_only_seed456:
  状态: 评估阶段报错（训练已完成，eval 脚本崩溃）
  错误: ValueError: Can't find 'adapter_config.json' at
        '/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed456/final'
  原因: checkpoint 目录缺少 adapter_config.json，PeftModel.from_pretrained 加载失败
  ⚠️ cuda:0 的 49G 显存可能是该崩溃进程残留，需手动释放

Q3 registry seed456:
  未找到条目（count=0），registry 中无 qwen15b_exception_only_seed456 记录

Q4 codellama13b_full_trace_tail512_seed123:
  进度: step 333/444 (75%), ~13.4s/step
  已运行: 1h19m
  剩余: 111 steps × 13.4s ≈ 25min
  预计完成: ~06:40 (服务器时间)
```

**需要处理的问题：**

1. **seed456 eval 失败**：checkpoint 路径 `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed456/final` 下缺少 `adapter_config.json`。需要检查该目录实际内容，确认训练是否正常保存了 LoRA adapter。
2. **cuda:0 显存泄漏**：49G 显存被占用但无活跃进程，需要确认是否有僵尸进程并释放。

需要我排查这两个问题吗？

---
