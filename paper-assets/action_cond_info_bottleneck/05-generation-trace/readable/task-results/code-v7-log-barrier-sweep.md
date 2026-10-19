# code v7 log barrier sweep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v7-log-barrier-sweep_20260516T105158_result.json`
- **Structured JSON:** [`e0e4f38f867b4aeabc38.json`](../../sessions/e0/e0e4f38f867b4aeabc38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

## 1. losses.py 修改确认

```python
# 旧: cos_sim.mean() — 平坦梯度
# 新: -log(1 - cos_sim + eps).mean() — log-barrier，cos→1时梯度发散
```

## 2. 单元测试

| 场景 | loss 值 |
|------|---------|
| near-identical (w1 ≈ w2) | **9.72** |
| different (w1 vs random) | **-0.08** |
| exactly-same (w1 vs w1) | **13.78** (≈-log(eps)) |

## 3. 训练指标演化

### Lambda=0.01

| Step | total_loss | task_loss | ctr_loss | scorer_mean | scorer_std |
|------|-----------|-----------|----------|-------------|------------|
| 100 | 0.1324 | 0.0621 | **8.81** | 0.398 | 0.240 |
| 200 | 0.1309 | 0.0915 | **6.36** | 0.480 | 0.287 |
| 300 | 0.1377 | 0.1049 | **5.85** | 0.459 | 0.295 |
| 400 | 0.0855 | 0.0501 | **5.69** | 0.426 | 0.303 |
| 500 | 0.1277 | 0.0950 | **5.49** | 0.420 | 0.299 |

### Lambda=0.1

| Step | total_loss | task_loss | ctr_loss | scorer_mean | scorer_std |
|------|-----------|-----------|----------|-------------|------------|
| 100 | 0.4704 | 0.1163 | **3.64** | 0.318 | 0.268 |
| 200 | 0.3419 | 0.1289 | **2.25** | 0.271 | 0.316 |
| 300 | 0.3387 | 0.1119 | **2.26** | 0.190 | 0.281 |
| 400 | 0.2935 | 0.1096 | **1.92** | 0.208 | 0.299 |
| 500 | 0.2765 | 0.1207 | **1.69** | 0.289 | 0.334 |

ctr_loss 趋势：log-barrier 两档都在持续下降（cos_sim 在远离 1），λ=0.1 下降更快更低。

## 4. Probe A 结果（关键判据）

| | Lambda=0.01 | Lambda=0.1 |
|---|---|---|
| Probe A cos range | **[0.9977, 0.9999]** | **[0.7043, 0.9514]** |
| Verdict | scorer barely depends on language | **scorer is language-condition-dependent** |
| Probe B cos range | [0.9026, 0.9335] | **[0.5320, 0.7058]** |
| Probe B verdict | position prior + mild variation | **task-dependent importance maps** |

## 5. 推荐

**Lambda=0.1** 是明确的赢家：
- Probe A cos 降到 0.70~0.95，scorer 已经开始对 language instruction 产生不同 importance map
- Probe B cos 降到 0.53~0.71，importance map 开始 task-dependent（不再是纯 position prior）
- task_loss（0.12）仍在合理范围，没有被 contrastive loss 压垮

Lambda=0.01 的 ctr_loss 虽然在下降，但 500 steps 后 Probe A cos 仍 >0.997，效果不足。

完整训练建议用 **lambda=0.1**，可以跑更长（如 5k~10k steps）观察 Probe A cos 是否继续下探到 <0.8。

---
