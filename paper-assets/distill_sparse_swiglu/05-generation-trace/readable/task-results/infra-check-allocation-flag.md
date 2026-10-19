# infra check allocation flag

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_allocation_flag_20260517T224921_result.json`
- **Structured JSON:** [`6032fdad6b5a06f097f5.json`](../../sessions/60/6032fdad6b5a06f097f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## 1. `--allocation` 参数

- 参数名：`--allocation`
- 可选值：`global_topk`（默认）、`uniform`
- 含义：`global_topk` = 全局单阈值分配；`uniform` = 每层独立 top-k（等比例）

## 2. 模式控制

通过 `--sparsity_mode` 控制：
- `per_token`：动态 predictor mask
- `teal_global`：静态校准 mask（使用 predictor checkpoint 计算全局 mask）

通过 `--baseline_mode` 控制 training-free baseline（与 `--checkpoint` 互斥）：
- `teal_vanilla`, `teal_greedy`, `wina`, `wina_greedy`, `rsparse`

## 3. 14B KL checkpoint 位置

- **westd-34887** 上存在：`/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt`
- **westd-41718** 上不存在（只有 8B 的 `kl_sparsity30_s42_v3`, `mvp_kl_norm_v2_s42`, `mvp_kl_norm_v2_s123`）

## 4. 正确的命令格式（KL checkpoint + uniform allocation）

在 **westd-34887** 上运行（因为 14B checkpoint 在那里）：

```bash
cd /root/distill_sparse_swiglu && python src/benchmark_eval.py \
  --model_name_or_path /root/autodl-tmp/models/Qwen2.5-14B \
  --checkpoint /root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt \
  --sparsity_mode teal_global \
  --allocation uniform \
  --sparsity_target 0.3 \
  --tasks wikitext2,arc_challenge,mmlu \
  --exp_id qwen14b_kl30_uniform \
  --gpu 0
```

关键点：
- `--sparsity_mode teal_global`（不是 per_token）才会使用 predictor checkpoint 生成静态 mask
- `--allocation uniform` 指定每层等比例分配
- `--checkpoint` 指向 predictor 权重文件
- 如果要跑 `global_topk` 对比，把 `--allocation uniform` 改为 `--allocation global_topk`（或直接省略，默认就是 global_topk）

从日志看之前 8B uniform eval 的实际命令格式验证了：它打印 `Mode: TEAL global mask from predictor (allocation=uniform)`，每层 sparsity 都是 0.500（均匀分配），与上述参数组合一致。

---
