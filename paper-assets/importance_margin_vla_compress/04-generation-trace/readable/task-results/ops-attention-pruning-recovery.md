# ops attention pruning recovery

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_attention_pruning_recovery_20260522T124955_result.json`
- **Structured JSON:** [`f5402b39fc0dedd34efa.json`](../../sessions/f5/f5402b39fc0dedd34efa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 状态汇报

### 两台 dry-run 均已完成

| 模型 | 服务器 | Suite | Prune | k | SR | 耗时 |
|------|--------|-------|-------|---|----|----|
| **OpenVLA** | westd-38929 | libero_object | attention | 0.5 | **40.0%** (8/20) | 11.1 min |
| **π0.5** | westd-41074 | libero_object | attention | 0.5 | **45.0%** (9/20) | 4.2 min |

### Per-task SR

| Task | OpenVLA | π0.5 |
|------|---------|------|
| alphabet soup | 50% | 100% |
| cream cheese | 0% | 50% |
| salad dressing | 50% | 50% |
| bbq sauce | 50% | 0% |
| ketchup | 100% | 50% |
| tomato sauce | 0% | 0% |
| butter | 50% | 100% |
| milk | 50% | 50% |
| chocolate pudding | 50% | 0% |
| orange juice | 0% | 50% |

### 实现概要

**OpenVLA** (`eval_openvla_l2norm_libero.py:164`, `AttentionPruningHook`):
- Hook 在 `vla.projector` 输出后执行
- 取 LLM (Llama) 前 2 层，对 vision-only tokens 做 self-attention
- importance = avg attention weight column sum（被其他 token 关注的总量）
- 选 top-k 保留

**π0.5** (`eval_pi05_pruning_libero.py:80`, `compute_attention_importance_probe`):
- 拼接 vision + language embeddings，送入 LLM (Gemma) 前 2 层
- importance = avg attention from language tokens → each vision token
- 选 top-k 保留

### 发现的 Bug

1. **OpenVLA 文件名错误**: `attention_prune` 模式的结果保存为 `openvla_l2norm_prune_k05_object.json`，因为 output path 的 `else` 分支没有区分 attention_prune 和 l2norm_prune（第 ~385 行）
2. **OpenVLA k_ratio: null**: JSON 中 `k_ratio` 字段只对 `random_prune` 非 null，attention_prune 时也应该记录
3. **π0.5 config 记录错误**: JSON 中 `n_keep_per_image: 256` 应为 128（日志确认实际 keep=128/256）
4. **实现差异**: OpenVLA 只用 vision token 间的 self-attention，π0.5 用 language→vision cross-attention。两种策略不同，可能影响可比性。

### 服务器上其他运行中的进程

- **westd-38929**: 2 个 π0.5 baseline eval 正在跑（libero_goal + libero_10，seed42，50ep）
- **westd-41074**: OpenVLA smart compress 训练在跑（m64 config，v6）

### SmolVLA

未在任一服务器上找到 SmolVLA attention pruning dry-run。

---
