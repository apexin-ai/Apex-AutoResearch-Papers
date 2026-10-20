# ops verify monitor script

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-monitor-script_20260521T103812_result.json`
- **Structured JSON:** [`8f65fdf2a3cb276eb16a.json`](../../sessions/8f/8f65fdf2a3cb276eb16a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-29999 上**不存在** LLaMA-3 eval 监控脚本。搜索结果汇总：

```
脚本路径: 不存在 (无 monitor_llama3_eval.sh 或类似文件)
```

找到的 LLaMA 相关脚本（均非监控脚本）：

| 脚本 | 用途 |
|------|------|
| `exp001/configs/run_llama31_8b_example.sh` | 8B SFT 训练示例模板（非 eval） |
| `scripts/run_llama3b_d000_eval.sh` | 3B d000 单次 eval（mmlu/gsm8k/arc_challenge/humaneval），不是监控循环 |
| `exp002/run_s1_llama_cuda0.sh` | 3B d000+d005 signal 计算（cuda:0） |
| `exp002/run_s1_llama_cuda1.sh` | 3B d025+d100 signal 计算（cuda:1） |

唯一的监控脚本是 `exp001/olmo2_monitor.sh`，用于 OLMo2 eval（轮询 GPU 空闲后启动 olmo2_eval_gpu0/gpu1）。

如果你指的是 LLaMA-3.1-8B 训练完成后自动触发 eval 的监控，需要新建。

---
