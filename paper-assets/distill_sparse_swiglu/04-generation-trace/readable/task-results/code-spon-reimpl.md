# code spon reimpl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_spon_reimpl_20260515T171100_result.json`
- **Structured JSON:** [`b6dcd7c95706d34256ed.json`](../../sessions/b6/b6dcd7c95706d34256ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. SPON 论文关键细节

| 项目 | 细节 |
|------|------|
| **注入位置** | MLP down_proj 前的 intermediate 激活（ablation 表明 down_proj 效果最好） |
| **公式** | `Y = W · S(X) + W · α`，其中 S(X) 是稀疏化激活，W 是 down_proj，α 是 learnable bias |
| **Loss** | `L(A) = E[D_KL(σ(z(u)) ‖ σ(ž(u;A)))]` — dense vs sparse+bias 的输出分布匹配 |
| **超参** | lr=1e-5, batch_size=8, block_size=128, epochs=10, WikiText-raw-v2 |
| **吸收** | `b_W_l = W_l @ α_l` → 零推理开销（bias fused into FMA） |
| **每层参数** | 1 个 spontaneous neuron（dim=intermediate_size），single vector per layer |
| **无公开代码** | GitHub `hxu105/SPON` 搜索未找到公开仓库 |

### 2. 文件清单

| 文件 | 状态 | 说明 |
|------|------|------|
| `src/spon.py` | 已有 | `SPONBiasVectors` + `SPONPatcher`（3 模式：dense/sparse/sparse_spon）+ `fold_into_model()` |
| `src/train_spon.py` | 已有 | 独立训练脚本，冻结模型+predictor，只训 SPON biases |
| `src/evaluate.py` | **已修改** | 新增 `--spon_checkpoint` 参数 + `spon_biases` 支持 + TEAL+SPON 评估段 |
| `src/compensation.py` | 已有 | Mean activation compensation（互补方法，非 SPON） |

### 3. SPON 参数量

- Llama-3.1-8B: 32 层 × 14,336 intermediate_size = **458,752 params**
- 占模型总参数 0.0057%
- 注意：任务描述中的 128K（基于 hidden_dim=4096）是误估，SPON bias 维度是 **intermediate_size** 不是 hidden_size

### 4. Dry-run 结果

- **Import**: `SPONBiasVectors`, `SPONPatcher` 导入正常
- **2-step 训练**: loss=2.17→2.22, mean_bias_norm=0.0012→0.0017, checkpoint 保存正常
- **fold_into_model**: down_proj.bias 从 None → shape [4096]，数学正确

### 5. 使用方法

**训练 SPON:**
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_spon.py \
  --predictor_checkpoint checkpoints/predictor_kl.pt \
  --num_steps 1000 --batch_size 8 --seq_len 128 --lr 1e-5 \
  --dataset wikitext-103 --gpu 0
```

**评估（含 SPON）:**
```bash
CUDA_VISIBLE_DEVICES=0 python src/evaluate.py \
  --checkpoint checkpoints/predictor_kl.pt \
  --spon_checkpoint checkpoints/spon_biases.pt \
  --gpu 0
```

### 6. plan_005 组合接口设计

SPON 提供静态偏移 `c_s = α_l`（input-independent），plan_005 的 contextual predictor 提供动态偏移 `c_θ(x)`。组合方式：

```python
# plan_005: c = c_s + c_theta(x)
intermediate = sparse_mlp(x) + spon_bias[l] + contextual_predictor(x)
```

`SPONBiasVectors` 的 `forward(layer_idx, intermediate)` 接口已支持叠加 —— contextual predictor 只需在 SPON 之后再加一个 additive term。`SPONPatcher` 可扩展为 4 模式（增加 `sparse_spon_contextual`）。

---
