# ops llama3 eval pipeline setup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-eval-pipeline-setup_20260521T105708_result.json`
- **Structured JSON:** [`8f5b9f026ae7c679fdd0.json`](../../sessions/8f/8f5b9f026ae7c679fdd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，无需重新部署。

```
PID 512753/512754/512755 状态: alive — /tmp/monitor_llama3_eval.sh
  512753: d000 → GPU 1
  512754: d025 → GPU 0
  512755: d100 → GPU 3

训练状态: 进行中，无 .done 文件
  d000: 1020/3125 (33%), ETA ~1h42m
  d100: 1051/4159 (25%), ETA ~2h21m
  GPU 2 空闲

eval 脚本: /tmp/monitor_llama3_eval.sh（已存在，功能完整）
  - C006 检查 (lora_alpha=32) ✓
  - C004 CUDA_VISIBLE_DEVICES 显式设置 ✓
  - evaluate.py 37775 bytes 版本校验 ✓
  - 无 GSM8K ✓

monitor 进程: 已运行，PIDs 512753/512754/512755

eval 参数:
  benchmarks: mmlu (5-shot), arc_challenge (25-shot)
  batch-size: 2
  model: /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B
  adapter: checkpoint dir 自动探测 (lora_adapter/ 或根目录)
  output: /root/contamcal-irt-calibration/results/{mmlu,arc}_eval/llama3_8b/{dosage}_s0/
```

---
