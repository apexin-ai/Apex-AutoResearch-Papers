# ops verify grpo random 20 gpu

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_grpo_random_20_gpu_20260517T133942_result.json`
- **Structured JSON:** [`ad7e7bef9d3107d22a95.json`](../../sessions/ad/ad7e7bef9d3107d22a95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. nvidia-smi（21:43:05）

| GPU | PID | 进程 | 显存 |
|-----|-----|------|------|
| 1 | 715803 | eval_gsm8k (pruned_cka_only_20) | 12994 MiB |
| 1 | 719684 | **grpo_random_20** | 12374 MiB |

- 总显存占用：25382 MiB / 97887 MiB（26%）
- GPU 利用率：78-81%
- cuda:0 空闲

### 2. 启动状态：正常，无致命错误

日志时间线：
```
21:39:32  Loading pruned model from sft_random_20
21:39:33  Non-uniform MLP detected: intermediate_size range [10832, 17592]
21:41:17  Preparing GSM8K training dataset...
21:42:38  [WARNING] Network unreachable → retry 1/5
21:42:39  Fell back to cached dataset ✓
21:42:39  Training on 7473 samples
21:42:39  Loading pruned ref_model from sft_random_20
```

- 唯一问题：HuggingFace 网络不可达，但自动 fallback 到本地缓存，无影响
- ref_model 正在加载中，预计还需 ~1-2 分钟

### 3. 第一个 step metrics

尚未输出——ref_model 仍在加载。GRPO 完整初始化（policy + ref + first generation batch）预计总共 ~5-8 分钟。

### 注意事项

cuda:1 上同时跑着 eval_gsm8k（PID 715803，pruned_cka_only_20, 200 samples），已运行 75 分钟。两者共用 25GB/97GB 显存，空间充裕。当 GRPO 进入训练（显存可能涨到 ~50GB），加上 eval 的 13GB ≈ 63GB，仍在 97GB 安全范围内。

---
