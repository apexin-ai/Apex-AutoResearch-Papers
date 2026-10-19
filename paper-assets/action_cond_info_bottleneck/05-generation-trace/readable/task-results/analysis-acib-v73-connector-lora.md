# analysis acib v73 connector lora

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acib_v73_connector_lora_20260518T020759_result.json`
- **Structured JSON:** [`13e9eda184522a882d23.json`](../../sessions/13/13e9eda184522a882d23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，以下是完整分析。

---

## acib_v73_connector_lora 训练结果分析

### 1. 训练完成状态

| 指标 | 值 |
|------|-----|
| 总步数 | 20000/20000 ✅ |
| 训练时长 | 3.2h |
| EXIT_CODE | 0 |
| 速度 | 1.8 steps/s |
| 可训练参数 | 228,993 / 450M (0.1%) |
| LoRA | connector.modality_projection.proj, rank=8, 105,984 params |
| W&B | 未配置 |

### 2. Final Metrics (Step 20000)

| 指标 | 值 |
|------|-----|
| total loss | 0.2602 |
| task_loss | 0.1472 |
| ib | 0.5411 |
| div | -0.2520 |
| ctr (contrastive) | 1.1907 |
| β | 0.0100 |
| scorer_mean | 0.344 |
| scorer_std | 0.297 |

训练动态正常：contrastive loss 从 11.84 → 1.19 稳步下降；scorer_std 从 0.147 → 0.297 说明 scorer 逐渐学会 selective attention。

### 3. Probe A 结果 (checkpoint-20000)

**固定图像，换 instruction，测 scorer importance map cosine similarity：**

| Pair | v7.3 cos | v7.2 cos | PASS (<0.8)? |
|------|----------|----------|-------------|
| bbq_sauce vs black_bowl_cookie | **0.864** | 0.877 | ❌ |
| bbq_sauce vs black_bowl_cabinet | **0.765** | 0.791 | ✅ |
| black_bowl_cookie vs black_bowl_cabinet | **0.939** | 0.944 | ❌ |

**Pass criterion: cos < 0.8 for at least 2/3 pairs → 1/3 PASS → ❌ FAIL**

v7.3 在所有 pair 上比 v7.2 略优（cos 更低），但改进幅度不足以翻转判定。第三个 pair 的两条 instruction 语义极近（同一动作、不同位置），cos=0.939 符合预期。

### 4. Probe B (natural cross-task)

| Pair | v7.3 cos | v7.2 cos |
|------|----------|----------|
| bbq_sauce vs black_bowl_cookie | **0.603** | 0.670 |
| bbq_sauce vs black_bowl_cabinet | **0.562** | 0.624 |
| black_bowl_cookie vs black_bowl_cabinet | **0.728** | 0.755 |

全部 < 0.8 → importance maps 是 task-dependent 的，不是纯 position prior。v7.3 比 v7.2 更 task-discriminative。

### 5. Checkpoint 路径

```
/root/autodl-tmp/acib_v73_connector_lora_seed42/
├── config.json
├── checkpoint-5000/checkpoint.pt
├── checkpoint-10000/checkpoint.pt
├── checkpoint-15000/checkpoint.pt
└── checkpoint-20000/checkpoint.pt   (867MB)
```

### 6. v7.3 MVP Pass/Fail 初步判定

| Criterion | Status | Notes |
|-----------|--------|-------|
| Probe A cos < 0.8 (≥2/3 pairs) | ❌ **FAIL** | 1/3 pass，与 v7.2 模式一致但略优 |
| α=0.0 = baseline ±1pp | ⏳ 待 eval | |
| α=1.0 4-suite avg ≥ 64.1% | ⏳ 待 eval | |

**结论：Probe A FAIL。** LoRA 结构化方案相比 v7.2 在 language conditioning 上有边际改善（所有 pair cos 下降约 0.01-0.03），但不足以通过 pass criterion。两个 "black bowl" 指令语义高度重叠导致 pair 3 始终 cos>0.9，这可能是 benchmark 本身的局限而非方法问题。

后续需要：
1. 跑 α=0.0 和 α=1.0 的 4-suite eval 验证剩余两个 criterion
2. 考虑是否放宽 Probe A threshold（鉴于 pair 3 语义重叠），或增加更多语义差异大的 task pairs

---
