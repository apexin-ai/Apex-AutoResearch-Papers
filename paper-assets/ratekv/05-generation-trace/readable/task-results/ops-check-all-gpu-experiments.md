# ops check all gpu experiments

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_gpu_experiments_20260516T061239_result.json`
- **Structured JSON:** [`86320d1b38aaa57665fc.json`](../../sessions/86/86320d1b38aaa57665fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 实验状态

| 实验 | GPU | 状态 | 详情 |
|------|-----|------|------|
| `llama_multi_seed_ppl` | GPU 0 (99%, 16.5GB) | **运行中** | Seed 42 profiling 220/256 heads |
| `mistral_multi_seed_ppl_v2` | GPU 1 (100%, 41.3GB) | **运行中** | Seed 42 profiling 180/256 heads |
| `yi_8k_eval` | — | **完成 ✓** | 已关闭，结果已入 registry |

### Yi 8K Eval 结果 (negative — 符合预期)

| Method | 8K PPL | vs BF16 |
|--------|--------|---------|
| BF16 baseline | 5.2619 | — |
| Uniform 4-bit | 5.5032 | +4.6% |
| Constrained MCKP | 5.5648 | +5.8% |

MCKP 比 uniform **差** 0.0616 PPL。Spike 形状模型 (c=0.71) 在 8K 上无 MCKP 收益，符合 "Spread-specific long-context amplification" 假设的对照预期。

### 运行中实验进度估算

两个实验都刚完成 baseline + uniform eval，进入 seed 42 的 head profiling：
- **Llama**: 220/256 heads done → seed 42 剩 ~20min profiling + ~15min eval，之后还有 seed 123/456 各 ~2.5h → **预计还需 ~5.5h**
- **Mistral**: 180/256 heads done → seed 42 剩 ~45min + ~15min eval，之后 seed 123/456 → **预计还需 ~6.5h**

### GPU 空闲情况与建议

- **0 个 GPU 空闲**，两块 RTX PRO 6000 (98GB) 满载
- Yi 8K eval 的 tmux session 已退出，不占 GPU
- 预计今晚 ~20:00-21:00 UTC 两个实验陆续完成，届时可调度新任务

---
