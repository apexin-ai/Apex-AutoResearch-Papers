# diag grpo speed crisis

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grpo-speed-crisis_20260515T031634_result.json`
- **Structured JSON:** [`9d242fe620e4a851bea8.json`](../../sessions/9d/9d242fe620e4a851bea8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No checkpoints saved yet (only `completions/` dir), so we can reuse the same output directories.

---

## 当前进度
- **RASP**: step 1/500, 1h51m/step, 已运行 2h7m, ETA 922h (38.4天)
- **Standard**: step 1/500, 1h52m/step, 已运行 2h7m, ETA 932h (38.8天)
- GPU: 两块都 100% 利用率, ~52GB/98GB

## 代码分析
| 参数 | 当前值 | 来源 |
|------|--------|------|
| `num_generations` | **4** | 默认值（未显式传参） |
| `per_device_train_batch_size` | **1** | 默认值 |
| `gradient_accumulation_steps` | **4** | 默认值 |
| `max_completion_length` | **4096** | 显式传参 |
| `max_samples` | **2000** | 显式传参 |
| vLLM | **未启用** | GRPOConfig 中无 `use_vllm`；且非均匀剪枝模型 intermediate_size=[8128,18944] 不兼容 vLLM |
| 总 steps | **500** | 2000/(1×4) |

## 瓶颈分析

**主因：`max_completion_length=4096` + `num_generations=4`**

每个 training step 需要生成 4 micro-batches × 4 completions = 16 个序列。TRL 的 batched generation 等待最长序列完成。即使 99% EOS rate @~180 tokens，16 个序列中至少一个不停止的概率 ~15%，此时该序列跑满 4096 tokens，拖慢整个 batch。

vLLM 不可用（非均匀剪枝架构 + 版本不兼容 0.18.1 vs 支持的 0.11-0.17.1），只能优化参数。

## 重启方案

**建议：Kill 两个进程，重启。** 无 checkpoint 可 resume，且参数需要改。

### 参数变更

| 参数 | 旧值 | 新值 | 理由 |
|------|------|------|------|
| `max_completion_length` | 4096 | **384** | SFT avg ~180 tokens, 2.1x 安全余量，封死 worst-case |
| `num_generations` | 4 | **2** | GRPO 最小值，generation 开销减半 |
| `max_samples` | 2000 | **1000** | 步数 500→250，总时间减半 |
| `save_steps` | 100 | **50** | 适配 250 steps (保存于 50,100,150,200,250) |
| 其他 | 不变 | 不变 | lr, grad_accum, batch_size, patience 保持 |

### RASP 命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20 \
  --gpu 0 \
  --max_completion_length 384 \
  --num_generations 2 \
  --num_train_epochs 1 \
  --max_samples 1000 \
  --learning_rate 1e-6 \
  --save_total_limit 3 \
  --save_steps 50 \
  --reward_desert_patience 50 \
  --run_name grpo_stage2_rasp_20_v2
```

### Standard 命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/train_grpo.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20 \
  --gpu 1 \
  --max_completion_length 384 \
  --num_generations 2 \
  --num_train_epochs 1 \
  --max_samples 1000 \
  --learning_rate 1e-6 \
  --save_total_limit 3 \
  --save_steps 50 \
  --reward_desert_patience 50 \
  --run_name grpo_stage2_standard_20_v2
```

### 预估时间

| 指标 | 保守估计 | 乐观估计 |
|------|----------|----------|
| Step 时间 | ~12 min | ~5 min |
| 250 steps 总时间 | ~50h | ~21h |
| 加速比 | ~9x | ~22x |

保守估计基于 worst-case generation 从 4096→384 (~10.7x) 和 num_generations 4→2 (2x) 的折衷。第一个 step 通常有 warmup 开销，后续会更快。

**建议**：重启后观察前 3 个 step 的平均时间。如果 >15 min/step，可进一步将 `max_samples` 降到 500（125 steps，~31h 保守估计）。

### 执行步骤
1. `kill 263888 263966`
2. 清理旧 output dir 的 `completions/` 子目录
3. 启动两个新实验（nohup + 日志重定向）
4. 等 step 1 完成后检查速度

是否执行 kill 和重启？

---
