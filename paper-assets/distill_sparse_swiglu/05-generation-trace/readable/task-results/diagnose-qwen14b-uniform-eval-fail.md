# diagnose qwen14b uniform eval fail

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen14b_uniform_eval_fail_20260518T003449_result.json`
- **Structured JSON:** [`dc1eafc900344f7f5d92.json`](../../sessions/dc/dc1eafc900344f7f5d92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

### 1. 原始 5-task 运行失败原因

**失败 task**: GSM8K (`generate_until`)

**失败模式**: 进程在 GSM8K 生成阶段被直接 kill（无 Python traceback），疑似 OOM：
- KL30: 死在 369/1319 (28%), 运行 1h08m
- TEAL30: 死在 225/1319 (17%), 运行 57m

autoregressive generation 比 loglikelihood forward pass 需要更多显存，14B 模型在生成 2048 tokens 时 OOM 合理。

### 2. 4-task 重跑也失败了

两个 `_4task` 日志（08:35）显示 WikiText-2 PPL 成功，但 lm-eval 阶段崩溃：

```
RuntimeError: Cannot send a request, as the client has been closed.
```

崩在 `datasets.load_dataset` 下载 arc_challenge 时。原始 5-task 跑通是因为有 `HF_HUB_OFFLINE=1` + 缓存，4-task 重跑没设 offline mode 或缓存路径不对。

### 3. 已完成的指标

| Model | WikiText-2 PPL | ARC/Winogrande/MMLU |
|-------|---------------|---------------------|
| KL30 uniform | **7.6318** | 未完成 |
| TEAL30 uniform | **8.0054** | 未完成 |

### 4. 判断

**不能直接用旧结果，必须重跑。** 原因：
- 5-task 运行虽然完成了 loglikelihood 阶段，但脚本在 GSM8K OOM 死后没有输出任何结果
- 4-task 重跑只拿到了 WikiText-2 PPL（可用），lm-eval 部分因 HF Hub 连接失败

### 5. 修复建议

重跑时需要：
1. 去掉 GSM8K（D053 已决定）
2. 设置 `HF_HUB_OFFLINE=1` 环境变量（或 `HF_DATASETS_OFFLINE=1`）
3. 确认 `--cache_dir /root/autodl-tmp/.hf_cache` 指向已有缓存
4. 5-task 运行时数据集确实被缓存过（日志里有 "Using the latest cached version"），缓存在 `/root/autodl-tmp/.hf_cache/datasets/`

---
