# code eval dryrun

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-dryrun_20260515T161034_result.json`
- **Structured JSON:** [`21ad0d4fc6431eeac9b3.json`](../../sessions/21/21ad0d4fc6431eeac9b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 评估结果汇总

### 1. evaluate.py 部署状态: **已部署，有 Bug**

文件存在 (`12KB`)，结构完整，但 **dry-run 失败**:

```
KeyError: 'observation.language.tokens'
```

**根因**: evaluate.py 没有调用 `preprocess_batch()` 来向 batch 添加 `observation.language.tokens` 和 `observation.language.attention_mask`。train.py 的 `preprocess_batch` (line 248) 从 `task` 字段 tokenize 或填充 dummy tokens，但 evaluate.py 的 eval 循环直接把 raw batch 喂给模型。

**影响范围**: baseline 路径和 IMM 路径都受影响:
- Baseline: `model(batch)` at line 195 → SmolVLA forward 访问 `batch["observation.language.tokens"]` 崩溃
- IMM: `model(batch, step=0)` at lines 207/210 → IMM wrapper forward 同样访问 `batch[OBS_LANGUAGE_TOKENS]` 崩溃
- IMM 的 `compute_importance_scores()` 不需要 language tokens，不受影响

### 2. Checkpoint 状态
- **Baseline**: `checkpoints/baseline/step_005000/checkpoint.pt` ✅ (训练当前在 step ~8700, 下一个 save 在 step 10000)
- **IMM**: **不存在** ❌ — `checkpoints/` 下没有 `imm_anchor/` 目录，GPU 1 完全空闲，IMM 训练未启动

### 3. Dry-run 结果
在 GPU 1 上跑了 baseline step-5000 的 dry-run (max_batches=5)，模型加载成功但 eval 循环首个 batch 就 crash。

### 4. 功能覆盖（gate criteria）

evaluate.py 已实现的 metric 计算 **全部覆盖**:
| Gate Criterion | 对应代码 | 状态 |
|---|---|---|
| Δ_k median ≥2x | `compute_margin` + margin_median | ✅ |
| Top-k preservation ≥10pp | `topk_preservation_rate` @ eps=0.01/0.02/0.05 | ✅ |
| Clean success ≤-5pp | `action_loss` per condition | ✅ |
| L·ε/Δ_k ≤-30% | `l_eps_delta_ratio` + empirical Lipschitz | ✅ |

### 5. 需修复的问题

**Bug（必须修复才能运行）**:
- evaluate.py 的 `main()` 或 `evaluate_full()` 需要在 eval 循环前调用 `preprocess_batch(batch, tokenizer, device=device)` （从 train.py import）
- 需要用 `get_tokenizer_from_policy(policy)` 获取 tokenizer

**建议改进（非阻塞）**:
- baseline 路径用 `baseline_forward(policy, batch)` 替代 `model(batch)` 以保持与 train.py 一致
- 缺少 baseline vs IMM 的自动对比脚本（当前需手动比较两个 JSON）

### 6. 评估 Pipeline 就绪状态: **NEEDS_FIX**

- evaluate.py 有一个阻塞性 bug（缺少 `preprocess_batch`）
- IMM 训练未启动（GPU 1 空闲），无 IMM checkpoint
- 修复 bug + 启动 IMM 训练后才能做完整评估

---
