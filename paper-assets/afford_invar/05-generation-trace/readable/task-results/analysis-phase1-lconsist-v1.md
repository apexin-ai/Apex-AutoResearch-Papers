# analysis phase1 lconsist v1

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase1_lconsist_v1_20260519T225345_result.json`
- **Structured JSON:** [`0581357b44529c7da454.json`](../../sessions/05/0581357b44529c7da454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练仍在运行**（PID 110222，当前约 step 521/20000），并未完成。但 500-step 梯度监控数据已足够做分叉判断。

## 分析结果

### 1. 训练状态
- **未完成**：当前 step ~521/20000（2.6%），进程活跃（PID 110222）
- 仅保存了 `checkpoint-500`
- W&B 已禁用，无远程指标可查
- 无 NaN/OOM/异常

### 2. Loss 收敛

| 指标 | Step 0 | Step 500 | 趋势 |
|------|--------|----------|------|
| L_action | 0.6562 | ~0.45 | 正常下降 |
| L_consist | 0.3492 | 0.0005 | 快速崩塌至近零 |
| L_total | 0.6912 | ~0.45 | 基本等于 L_action |
| H_entropy | -8.01 | -7.29 | 略升（heatmap 仍近均匀） |

### 3. 梯度监控 — **Path B 确认**

| Step | L_consist | consist_grad_norm | total_grad_norm | **grad_ratio** |
|------|-----------|-------------------|-----------------|----------------|
| 0 | 0.3492 | 2.3588 | 38.1050 | **6.19%** |
| 100 | 0.0024 | 0.0046 | 19.1103 | **0.02%** |
| 200 | 0.0014 | 0.0064 | 15.1939 | **0.04%** |
| 300 | 0.0008 | 0.0021 | 20.8426 | **0.01%** |
| 400 | 0.0008 | 0.0018 | 18.6487 | **0.01%** |
| 500 | 0.0005 | 0.0017 | 20.2325 | **0.01%** |

grad_ratio 在 step 0 后立即崩塌到 **< 0.1%**，远低于 1% 阈值。L_consist 梯度对模型参数更新基本无贡献。

### 4. Heatmap 质量

- `hm_mean` ≈ 0.000061（恒定，= 1/16384，即均匀分布值）
- `hm_max` ≈ 0.003（极小峰值）
- `hm_std` ≈ 0.0003（几乎无空间变化）
- `hm_ent` ≈ 7.2-7.3（接近 log2(256)=8.0 的均匀分布熵）

**Heatmap 本质上是均匀分布，没有学到空间结构。**

### 5. 结论

**Path B 确认：L_consist 作为正则项失效。** 

原因分析：
- alpha=0.1 将 L_consist 缩放后量级太小（step 0 时 L_con × alpha ≈ 0.035 vs L_act ≈ 0.66）
- L_consist 在前 100 步内从 0.35 降到 0.002，decoder 找到了"均匀分布"这个 trivial solution（所有 paraphrase 输出相同的均匀 heatmap，MSE ≈ 0）
- 没有 entropy 惩罚（lambda_H=0），无力阻止坍缩

### 6. 建议下一步

按实验 hypothesis 中的分叉路径：
- **Path B 方案**：kill 当前训练，切到 L_transfer-only（用预训练 affordance label 直接监督 decoder，而非用 consistency 间接约束）
- 或者尝试调参救 L_consist：增大 alpha（如 1.0）+ 加入 entropy 正则（lambda_H > 0）防止 trivial solution

是否需要我 kill 当前进程并准备 Path B 实验？

---
