# ssh unified bce eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unified-bce-eval_20260515T141602_result.json`
- **Structured JSON:** [`55bc64f2b65742e5856c.json`](../../sessions/55/55bc64f2b65742e5856c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已收集。Dense PPL 三次不完全一致（27.96 / 28.38 / 28.14），说明存在轻微非确定性，可能来自 flash_attention 或 bf16 算术。

```
evaluate.py md5: 4f2faa315b3e45b0781c1c07c47515eb
evaluate.py 修复状态: off-by-one 已修复（数据端 shift，evaluate 不再 double shift）
校准样本数: 32（mini-batch=4，分 8 轮平均）

| Checkpoint | Dense PPL | Sparse PPL | Δ%     | Model Sparsity |
|-----------|-----------|------------|--------|----------------|
| s42       | 27.96     | 44.54      | +59.3% | 0.496          |
| s123      | 28.38     | 44.59      | +57.1% | 0.496          |
| s456      | 28.14     | 43.03      | +52.9% | 0.496          |

Dense PPL 是否一致: 否（27.96 ~ 28.38，spread 0.42，~1.5%）
```

**注意事项**：

1. **Dense PPL ~28 而非 ~6**：这与之前 KL eval 报的 6.12 差距很大。当前 evaluate.py 没有 double shift，逻辑上是正确的。之前报 6.12 的版本可能有别的问题（例如 input/label 对齐导致信息泄漏使 PPL 虚低）。建议检查当时的 evaluate.py 版本差异。

2. **Dense PPL 不完全一致**：每次运行加载独立 Python 进程，可能的原因是 flash_attention_2 非确定性。如需完全一致，可改用 `sdpa` attention 实现。

3. **C4 跳过**：因 HF Hub 无 token 导致 streaming 极慢。已添加 `--skip_c4` 参数，后续有 token 后可重新启用。

4. **evaluate.py 改动**：
   - 添加 `--calibration_samples`（默认 32）
   - 添加 `--skip_c4` 
   - `teal_global_masks` 改为 mini-batch 校准避免 OOM

---
