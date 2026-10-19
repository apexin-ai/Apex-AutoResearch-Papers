# code v8 film impl sweep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8-film-impl-sweep_20260516T105359_result.json`
- **Structured JSON:** [`c1941d58a28efd25b438.json`](../../sessions/c1/c1941d58a28efd25b438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Probe A complete. Let me compile the full results.

---

## 产出汇总

### 1. 代码 diff

**config.py** — 新增 `conditioning_mode` 字段:
```python
conditioning_mode: Literal["concat", "film"] = "film"
```

**scorer.py** — 新增 `FiLMGenerator` + 修改 `ACIBScorer`:
- `FiLMGenerator`: 2层MLP (condition_dim → feature_dim → feature_dim*2)，最后一层零初始化
- `ACIBScorer.forward`: FiLM 模式下 `modulated = (1 + gamma) * vis + beta`，只用 `visual_dim` 输入 MLP（不 concat condition）
- 向后兼容：`conditioning_mode="concat"` 保留原逻辑

**train_acib.py** — 新增 `--conditioning_mode` 参数，传入 ACIBConfig

**cross_task_probe.py** — 从 config.json 读取 `conditioning_mode`

### 2. 单元测试
```
Scorer params: 2,829,249 (vs concat模式 ~2M)
weights shape: [2, 64] ✅
Identity init cos(diff_cond): 1.000000 ✅
net[2] grad norm: 42.09 (梯度流通) ✅
Concat mode backward compat: ✅
```

### 3. Step 100-500 指标演化

| Step | total_loss | task_loss | ib_loss | div_loss | scorer_mean | scorer_std | steps/s |
|------|-----------|-----------|---------|----------|-------------|-----------|---------|
| 100  | 0.0739    | 0.0852    | 0.0315  | -0.2520  | 0.703       | 0.256     | 1.7     |
| 200  | 0.0598    | 0.0839    | 0.0577  | -0.2949  | 0.656       | 0.297     | 1.3     |
| 300  | 0.0336    | 0.0601    | 0.0794  | -0.3047  | 0.633       | 0.307     | 1.1     |
| 400  | 0.0189    | 0.0398    | 0.0809  | -0.3047  | 0.629       | 0.309     | 1.0     |
| 500  | 0.0849    | 0.1065    | 0.0729  | -0.3125  | 0.641       | 0.314     | 1.0     |

注：β=0.0 全程（beta_warmup=1000 > 500步），IB 惩罚未生效。速度降至1.0 steps/s 因 GPU 1 与另一个 v7 进程共享。

### 4. Probe A cos 值

```
Probe A: bit_identical=False, cos∈[0.9997, 1.0000]
→ scorer barely depends on language

Probe B: cos∈[0.9048, 0.9496]
→ moderately similar, mostly position prior with mild task variation
```

### 5. 验证标准

| 标准 | 目标 | 实际 | 结果 |
|------|------|------|------|
| Probe A cos | < 0.95 | 0.9997-1.0000 | ❌ FAIL |
| scorer_std | > 0.1 | 0.314 | ✅ PASS |
| task_loss | < 0.15 | 0.1065 | ✅ PASS |

### 分析

FiLM 在 500 步内没有打破 shortcut — `bit_identical=False` 说明 FiLM 确实在产生微弱调制（vs v5-v7 的 bit_identical=True），但调制量极小（cos≈0.9997）。原因：

1. **零初始化 + β warmup** → FiLM 前 500 步几乎是 identity，没有足够的训练步数让 FiLM 层学到有意义的语言依赖调制
2. **无直接语言区分 loss** → task loss 不要求 FiLM 对不同语言产生不同 modulation；diversity/IB loss 不直接作用于 FiLM 的条件依赖性
3. **β=0 全程** → IB 约束未生效，scorer 没有信息瓶颈压力

### 6. 完整训练推荐配置

```bash
MUJOCO_GL=egl python3 -u scripts/train_acib.py \
    --model_id lerobot/smolvla_libero \
    --dataset_id lerobot/libero \
    --data_root /root/autodl-tmp/libero_dataset \
    --hidden_dim 64 \
    --alpha 0.01 \
    --beta 0.01 \
    --beta_warmup_steps 200     # 更短的 warmup 让 IB 更早生效
    --mode soft \
    --condition_source language \
    --conditioning_mode film \
    --lambda_contrastive 0.0 \
    --diversity_lambda 0.1 \
    --lambda_ent 0.0 \
    --steps 5000                # 至少 5000 步让 FiLM 有足够学习时间
    --batch_size 64 \
    --lr 3e-4                   # 更高 lr 加速 FiLM 收敛
    --warmup_steps 200 \
    --grad_clip 1.0 \
    --save_freq 1000 \
    --dtype bfloat16 \
    --gpu 1 \
    --output_dir /root/acib/outputs/acib_v8_film_5k \
    --seed 42
```

关键改进建议：
- **缩短 beta_warmup** 到 200 步，让 IB 惩罚更早介入
- **增加 lr** 到 3e-4，加速 FiLM 层从零初始化的学习
- **5000+ 步训练** — 500 步不够 FiLM 从 identity init 发展出有意义的语言依赖调制
- 若 5k 步 Probe A 仍 >0.95，考虑**恢复 contrastive loss**（lambda_contrastive=0.01）迫使 FiLM 产生条件依赖输出

---
