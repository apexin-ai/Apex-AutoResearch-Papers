# ops gpu mapping verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_mapping_verify_20260514T043148_result.json`
- **Structured JSON:** [`d5672859450e8167389b.json`](../../sessions/d5/d5672859450e8167389b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. GPU 2 — eval_05B_d100_v5 (PID 266790)

**确认是 eval，不是 SFT。** 命令行为：
```
python evaluate.py --model-path Qwen2.5-0.5B --adapter-path Qwen2.5-0.5B_d100_s42/lora_adapter
  --output-dir eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval
```

当前进度：mmlu 已完成，**GSM8K 726/1319 (55%)**，~17s/it。后面还有 arc_challenge + humaneval。

预计剩余：GSM8K 约 2.8h + arc_challenge + humaneval ≈ **总计还需 4-5 小时**。

### ⚠️ GPU 2 异常：两个 eval 进程共存

| PID | 命令 | 显存 |
|-----|------|------|
| 266790 | evaluate.py ... **d100_s42** | 3658 MiB |
| 266521 | evaluate.py ... **d000_s42** | 3658 MiB |

PID 266521 是另一个实验（Qwen2.5-0.5B_d000_s42 的 eval），两个进程同时跑在 GPU 2 上，互相争抢算力。这是 **C001 违规**的情况，虽然显存够（7330/24564 MiB），但会拖慢双方速度。

### 2. GPU 3 — eval_3B_d000_s123 (PID 242591)

命令确认：`python evaluate.py ... Qwen2.5-3B_d000_s123`

当前在跑 **HumanEval 154/164 (94%)**，这是第 4 个也是最后一个 benchmark。~29s/it，剩余 10 个样本。

**预计 ~5 分钟完成。**

### 3. 全局 GPU 状态

| GPU | 利用率 | 显存 (used/total) | PID |
|-----|--------|-------------------|-----|
| 0 | 9% | 10055/24564 MiB | 251924 |
| 1 | 56% | 12620/24564 MiB | 249294, 255322 |
| 2 | 55% | 7330/24564 MiB | 266521, 266790 |
| 3 | 22% | 13493/24564 MiB | 242591 |
| 4 | 5% | 18547/24564 MiB | 271921 |
| 5 | 10% | 10365/24564 MiB | 250610 |

### 待决策

GPU 2 上 PID 266521（d000_s42 eval）是否为预期内的实验？如果不是，需要 kill 掉以释放算力给 d100_s42。需要确认 266521 对应的 registry 实验 ID。

---
