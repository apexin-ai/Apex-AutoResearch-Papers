# code ste baseline

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ste_baseline_20260515T183635_result.json`
- **Structured JSON:** [`4bc50d6cf55170757f8c.json`](../../sessions/4b/4bc50d6cf55170757f8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 dry-run 都通过了。

### 结果对比

| | STE (`--relaxation ste`) | Gumbel (`--relaxation gumbel`) |
|---|---|---|
| mask 类型 | `STEMask` (hard threshold + STE gradient) | `GumbelSigmoidMask` (soft mask + noise) |
| tau | `0.000` (无 annealing) | `0.820` (正常 annealing) |
| kl_raw step 1 | 4.531 | 0.773 |
| sparsity step 1 | 0.541 | 0.398 |
| lambda | 正常工作 | 正常工作 |

KL 差异符合预期：STE 用 hard mask 直接零化神经元，信息损失更大；Gumbel 用 soft mask 保留了梯度信息。

### 修改文件总结

**`src/predictor.py`**:
- 新增 `STEMask(nn.Module)` 类（line 77），forward 用 `hard - sigmoid.detach() + sigmoid` 实现 STE trick

**`src/train.py`**（6 处修改）:
- 新增 `--relaxation` 参数（choices: `gumbel`/`ste`，默认 `gumbel`）
- import 添加 `STEMask`
- `main()`: 当 `--relaxation ste` 时替换 `wrapper.gumbel_mask` 为 `STEMask()`
- `train_kl()`: STE 模式下跳过 tau annealing
- `train_kl_normalized()`: 同上

---
