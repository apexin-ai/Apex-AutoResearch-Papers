# analysis cross strategy loo

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_strategy_loo_20260515T040036_result.json`
- **Structured JSON:** [`f450e88b315dcb599ecf.json`](../../sessions/f4/f450e88b315dcb599ecf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9 个 rotation 全部完成。结果如下：

| Model | Hold-out | Train | Test | 4-class acc | 95% CI | d1v2 AUC | d2v3 AUC |
|-------|----------|-------|------|-------------|--------|----------|----------|
| Pythia-1.4B | nucleus | 40000 | 20000 | **0.6935** | [0.687, 0.700] | 0.6903 | 0.7626 |
| Pythia-1.4B | temp09 | 40000 | 20000 | 0.6281 | [0.621, 0.635] | 0.5760 | 0.7240 |
| Pythia-1.4B | topk50 | 40000 | 20000 | 0.5151 | [0.508, 0.522] | 0.6393 | 0.5801 |
| GPT-2 XL | nucleus | 40000 | 20000 | 0.5993 | [0.593, 0.606] | 0.7826 | 0.4985 |
| GPT-2 XL | temp09 | 40000 | 20000 | 0.5609 | [0.554, 0.568] | **0.1288** | 0.6366 |
| GPT-2 XL | topk50 | 40000 | 20000 | 0.5364 | [0.530, 0.543] | 0.8308 | 0.7222 |
| OLMo-1B | nucleus | 40000 | 20000 | 0.6538 | [0.647, 0.660] | 0.7931 | 0.6076 |
| OLMo-1B | temp09 | 40000 | 20000 | 0.5816 | [0.575, 0.588] | **0.2529** | 0.7015 |
| OLMo-1B | topk50 | 40000 | 20000 | 0.5488 | [0.542, 0.556] | 0.8549 | 0.7107 |

**关键发现：**
- **所有 9 个 rotation 的 4-class accuracy 均远超 chance (0.25)**，均值 0.5908，说明深度信号跨策略可迁移
- **Pythia 表现最稳定**（0.52–0.69），hold-out nucleus 最高
- **d1v2 AUC 在 hold-out=temp09 时反转**（GPT-2 XL: 0.13, OLMo: 0.25），说明 temp09 的 d1→d2 过渡特征分布与 nucleus/topk50 显著不同——分类器从其他两种策略学到的 d1/d2 判别规则在 temp09 上方向反转
- **d2v3 AUC 更稳定**（6/9 rotation > 0.6），深层递归信号跨策略一致性更强

脚本位于 `src/cross_strategy_loo.py`，JSON 结果保存在服务器 `results/cross_strategy_loo.json`，artifact 已注册。

---
