# ssh critical eval verification

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_critical-eval-verification_20260517T162024_result.json`
- **Structured JSON:** [`156e556b79cc015589f2.json`](../../sessions/15/156e556b79cc015589f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证数据已齐全。汇报如下：

---

## 验证结果

### 验证 1: Action Expert 权重 — **PASS**
| 模块 | 检查数 | max_diff | 状态 |
|------|--------|----------|------|
| lm_expert | 145 | 0.0 | PASS (bit-identical) |
| text_model | 146 | 0.0 | PASS (bit-identical) |
| vision_model | 197 | 0.0 | PASS (bit-identical) |
| other (state_proj 等) | 11 | 0.0 | PASS (bit-identical) |
| connector | 1 | 1.38e-2 | FAIL (expected, trainable) |

Freeze 完全有效。所有冻结参数与 baseline 完全一致（0 差异）。

**重要发现**: `/root/autodl-tmp/models/smolvla_libero/model.safetensors` 和 HF cache 版本**不同**（max_diff=6.3e-3）。之前的 "0.4% L2=0.32/norm=71.8" 是正确的，但如果有人用 local copy 做对比会得到错误的巨大差异。

### 验证 2: Hook 执行路径 — **PASS (无 bug)**
- `alpha=0.0` → `effective = 1 - 0 + 0 * weights = 1.0`
- 数值验证：`max|output*effective - output| = 0.0`（精确恒等）
- 代码无 bypass 遗漏：hook 仍运行 scorer 并 cache logits，但返回值是原始 output

**但**: connector 权重已修改（rel=0.4%），所以 hook 收到的 `output` 本身就和 baseline 不同。

### 验证 3: Connector Output 分布 — 放大效应量化
```
Weight space:
  base norm=71.7609, v72 norm=71.7612
  L2=0.2890, cos=1.00003, rel=0.4028%

Output space (500 normalized inputs):
  cos: mean=0.99999, min=0.99996
  L2:  mean=0.0026, max=0.0053
  rel: mean=0.3974%, max=0.8391%

SVD:
  Diff top SV=0.178, Base top SV=6.83
  Diff/Base ratio=2.6%
  Effective rank=960 (full rank, diffuse drift)
```

0.4% weight-space shift → ~0.4% output-space shift（近线性放大，无爆炸）。

### 当前 eval 进度参考 (libero_spatial)

| 配置 | pc_success |
|------|-----------|
| v7.2 alpha=0.0 | 59.4% |
| v7.2 alpha=1.0 | 61.0% |
| v7 scorer_only | 58.4% |

alpha=0.0 实际上**高于** v7 的 58.4%，没有回退。

### 结论

**不是 bug。** alpha=0.0 "回退"的根本原因是 v7.2 checkpoint 包含训练后的 connector 权重。alpha=0.0 绕过了 scorer reweighting，但无法绕过 connector 本身的漂移。这是 connector_scorer freeze mode 的预期行为：

- alpha=0.0 = baseline + connector drift（无 scorer）
- alpha=X>0 = baseline + connector drift + scorer reweighting

如果需要真正的 baseline 对比，应使用 `eval_baseline.py` 或 `--disable_scoring` 配合原始 baseline 模型（而非 v7.2 checkpoint）。

---
