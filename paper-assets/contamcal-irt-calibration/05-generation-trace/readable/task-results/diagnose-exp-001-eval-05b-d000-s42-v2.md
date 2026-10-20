# diagnose exp 001 eval 05B d000 s42 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_d000_s42_v2_20260514T023825_result.json`
- **Structured JSON:** [`41b68b428e99b1cd9aa8.json`](../../sessions/41/41b68b428e99b1cd9aa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，以下是完整分析。

---

## 诊断结果

### 1. 失败根因：**系统内存压力导致 OOM Kill**（高置信度）

v2 进程在 MMLU 评估 84% (11821/14042) 时被 SIGKILL (EXIT_CODE=137)。证据链：

- **吞吐量持续下降**：从 ~40 it/s（开始）降至 ~22 it/s（被 kill 前），典型内存压力表现
- **6 个 GPU python 进程同时运行**（nvidia-smi 显示 GPU 0/1/3/4/5 均有进程），服务器负载很高
- **`device_map="auto"` 导致模型被放到 GPU 0**（日志 `We will use 90% of the memory on device 0`），而 GPU 0 已有另一个进程 (PID 251924) 占用 10046MiB — 不是目标 GPU 2
- 系统 RAM 总量 1TB，但 buff/cache 占 891GB，实际 free 仅 81GB，在多进程并发下可触发 cgroup 限制

### 2. GPU 显存情况

| GPU | 已用 | 总量 | 占用进程 |
|-----|------|------|---------|
| 0 | 10055MiB | 24564MiB | PID 251924 |
| 1 | 12620MiB | 24564MiB | PID 249294 + 255322 |
| **2** | **0MiB** | **24564MiB** | **空闲（v2 已死）** |
| 3 | 8957MiB | 24564MiB | PID 242591 |
| 4 | 5829MiB | 24564MiB | PID 243300 |
| 5 | 5829MiB | 24564MiB | PID 250610 |

### 3. v1 (前一次运行) 的失败是不同的 bug

v1 (EXIT_CODE=1) 实际**完成了全部 4 个 benchmark**（mmlu + gsm8k + arc_challenge + humaneval pass@1=0.1098），但在**保存结果时崩溃**：

```
FileNotFoundError: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'
```

输出目录存在但为空 — 结果全部丢失。代码 `evaluate.py:565` 有 `output_dir.mkdir(parents=True, exist_ok=True)`，但仍然报错，可能是文件系统瞬时问题或路径解析 bug。

### 4. 修复建议

**核心问题：缺少 `CUDA_VISIBLE_DEVICES` 导致模型抢占 GPU 0。**

重试命令调整：

```bash
CUDA_VISIBLE_DEVICES=2 python evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 \
  --benchmarks mmlu gsm8k arc_challenge humaneval \
  --batch-size 4
```

改动点：
1. **`CUDA_VISIBLE_DEVICES=2`** — 强制使用空闲的 GPU 2，避免与其他进程争抢
2. **`--batch-size 4`**（从默认 8 降低）— 降低 GPU 显存峰值
3. **v1 的 FileNotFoundError** — 需要检查 `evaluate.py` 的保存逻辑，建议在 `open()` 前加一行 `results_file.parent.mkdir(parents=True, exist_ok=True)` 做双重保险，或检查是否存在 Path 对象类型不一致的问题

### 5. 是否需要重试

**需要重试。** v1 完成了评估但结果丢失，v2 在 MMLU 途中被 kill。加 `CUDA_VISIBLE_DEVICES=2` 后应可稳定运行 — 0.5B 模型仅需 ~1-2GB 显存，GPU 2 有 24.5GB 完全空闲。

---
