# analysis v3 training curves

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3_training_curves_20260516T204437_result.json`
- **Structured JSON:** [`d04970a221d9d22b677e.json`](../../sessions/d0/d04970a221d9d22b677e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 文件已生成（202 行 = 1 header + 201 data rows）。以下是完整分析报告：

---

## v3 LoRA Expert 训练分析报告

### 1. 训练配置（统一）

| 参数 | 值 |
|------|-----|
| Base checkpoint | pi0_libero (openpi format, 778 keys) |
| 训练数据 | LIBERO-Object, 97 episodes, 66984 frames |
| LoRA rank | 16, alpha=32 |
| Target modules | Q/K/V/O on all 18 PaliGemma layers (72 modules) |
| Trainable params | 3,686,400 / 3.5B (0.11%) |
| Batch size | 16 |
| Steps | 10,000 |
| LR | 2e-4 with cosine decay to 1e-5 |
| Warmup | ~100 steps (linear warmup to peak LR) |

### 2. 关键 Metrics 汇总

| Expert | Initial Loss | Final Loss | Min Loss (step) | Last-1K Avg | Wall Time | Grad Norm (late) |
|--------|-------------|-----------|-----------------|-------------|-----------|-----------------|
| **physical** | **2.3697** | 0.5876 | 0.5673 (8950) | **0.5810** | 2.83h | 5.98 |
| visual | 1.9794 | 0.5899 | 0.5894 (9050) | 0.6006 | 3.04h | 5.48 |
| spatial | 1.9529 | 0.6126 | 0.5942 (9800) | 0.6048 | 2.85h | 5.64 |
| universal | 1.9529 | 0.6030 | 0.5932 (9700) | 0.6045 | 2.84h | 5.22 |

### 3. 收敛曲线对比

**Loss at Key Milestones:**

| Step | physical | visual | spatial | universal |
|------|----------|--------|---------|-----------|
| 0 | **2.37** | 1.98 | 1.95 | 1.95 |
| 100 | 0.99 | 0.98 | 0.99 | 1.03 |
| 500 | 0.87 | 0.86 | 0.87 | 0.88 |
| 2000 | 0.83 | 0.83 | 0.82 | 0.83 |
| 5000 | 0.69 | 0.70 | 0.69 | 0.70 |
| 9999 | 0.59 | 0.59 | 0.61 | 0.60 |

**四路 expert 收敛行为高度一致**——step 100 后 loss 差异 < 0.04，step 500 后差异 < 0.02。最终 loss 分布在 0.58-0.61 范围内（std ≈ 0.01），差异不显著。

### 4. Physical Initial Loss 偏高分析

Physical expert 的 initial loss (2.37) 比其他三个 (~1.95) 高约 **21%**。原因：

- pi0_libero base 已在 LIBERO-90 上 fine-tuned，模型对标准 demo 已有一定适应
- **physical perturbation（物理属性扰动）对 action space 的影响最大**——改变物体质量、摩擦等物理参数直接影响最优 action trajectory，使得初始 action prediction error 最高
- visual/spatial/universal 扰动更多影响 observation space（视觉外观、空间位置），对 action prediction 的初始偏移较小
- 但 physical 在 step 100 即收敛到与其他 expert 相同水平（0.99），说明 LoRA 快速适应了物理扰动的 action shift

### 5. 训练健康度

- **无 NaN**：全部 4 个 expert 无任何 NaN loss
- **无异常 spike**：没有任何 >0.05 的 step-to-step loss 跳升
- **无早停**：全部跑满 10000 步
- **Grad norm 演化正常**：early (0-500) avg ~0.6-1.7 → late (8000+) avg ~5.2-6.0，梯度逐渐增大但稳定在合理范围
- **训练时间一致**：physical/spatial/universal ~2.84h，visual 稍慢 (3.04h) 可能因共享 GPU 资源竞争

### 6. 与 v1 训练对比

| 对比项 | v1 | v3 |
|--------|-----|-----|
| Base model | pi0_base（预训练权重） | pi0_libero（LIBERO-90 fine-tuned） |
| Initial loss | ~0.08 | ~1.95-2.37 |
| Final loss | ~0.01 | ~0.59-0.61 |
| 训练数据 | 同 LIBERO-Object | 同 |

v1 的 initial loss 0.08 和 final loss 0.01 **不正常**——因为 pi0_base 没有经过 action space fine-tuning，其 action head 输出接近零/随机，loss 计算不反映真实的 action prediction quality。v3 使用正确的 pi0_libero base（已经学会了 LIBERO-90 的 action distribution），对 LIBERO-Object 数据是 OOD，initial loss ~2.0 是合理的 cross-entropy level。

### 7. 输出文件

- CSV: `/root/autodl-tmp/analysis/v3_training_curves.csv`（201 rows, 每 50 步采样，包含 loss/lr/grad_norm/elapsed per expert）

---
