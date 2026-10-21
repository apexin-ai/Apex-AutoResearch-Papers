# ops diagnose seed123 vs v5 config

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-seed123-vs-v5-config_20260513T204513_result.json`
- **Structured JSON:** [`33b1c756e3da9dd075f5.json`](../../sessions/33/33b1c756e3da9dd075f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整对比结果：

---

## 对比总结

### 1. 训练代码
**完全一致** — `train_repo_verifier.py` md5 = `9799cc4bb8a1c896f792e74178f45aeb`

### 2. 训练超参

| 参数 | home (CLS v5) | westd (seed123) |
|------|:---:|:---:|
| learning_rate | 5e-05 | 5e-05 |
| weight_decay | 0.01 | 0.01 |
| warmup_ratio | 0.05 | 0.05 |
| batch_size | 2 | 2 |
| grad_accum | 16 | 16 |
| bf16 | True | True |
| seed | **42** | **123** |

超参**完全一致**（除 seed）。lr 都是 5e-5，不是 2e-4。

### 3. Python / transformers 版本

| | home | westd |
|---|:---:|:---:|
| Python | 3.10.12 | 3.10.12 |
| **transformers** | **4.57.6** | **5.8.0** |

### 4. 数据文件
- 行数：均 70748
- **md5 不同**：home `e25e2c88...` vs westd `be5814c9...`
- keys 相同，但行顺序不同（不同 shuffle）

### 5. Base Model 路径
- home: `Qwen/Qwen3-4B`（hub 引用）
- westd: `/root/.cache/huggingface/hub/Qwen/Qwen3-4B`（本地 cache，offline 模式）

### 6. 训练曲线对比

**home (seed=42)** — 当前 step 4200/6633 (epoch 1.90)：
| step | eval_loss |
|------|-----------|
| 200 | 0.1258 |
| 400 | 0.0761 |
| **600** | **0.0642** ← best |
| 800 | 0.2045 |
| 1000+ | 0.12~0.33（严重过拟合） |

**westd (seed=123)** — 当前 step 3200/6633 (epoch 1.45)，仍在运行：
| step | eval_loss |
|------|-----------|
| **200** | **0.0808** ← best |
| 400 | 0.0902 |
| 600 | 0.1147 |
| 800 | 0.1473 |
| 1000+ | 0.19~0.36（更严重的过拟合） |

---

## 22pp Gap 最可能原因

**三个差异叠加导致：**

1. **transformers 4.57.6 vs 5.8.0（主因）** — 跨大版本（4→5），tokenizer 行为、attention 实现、训练循环细节均可能变化。westd 的模型从 step 200 之后就持续恶化，而 home 在 step 600 才达到 best 后开始恶化，说明 transformers 5.x 下模型的训练动态有显著不同。

2. **数据文件内容/顺序不同** — 两边数据 md5 不一致。在两者都严重过拟合的情况下，early steps 看到的数据顺序对 best checkpoint 质量影响极大。

3. **两者都严重过拟合，best checkpoint 都很早** — home best 在 step 600（epoch 0.27），westd best 在 step 200（epoch 0.09）。两者 eval_loss 差距其实不大（0.0642 vs 0.0808），但这种微小 loss 差距在分类 accuracy 上可以放大为 22pp。

**建议**：在 westd 上将 transformers 降级到 4.57.6，用与 home 相同的数据文件重跑，排除这两个变量。

---
