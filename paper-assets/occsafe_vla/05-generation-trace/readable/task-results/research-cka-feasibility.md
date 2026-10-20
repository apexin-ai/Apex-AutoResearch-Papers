# research cka feasibility

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cka_feasibility_20260523T233317_result.json`
- **Structured JSON:** [`206971d3f5590a7a2ce1.json`](../../sessions/20/206971d3f5590a7a2ce1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CKA 分析已完成。结果如下：

## CKA 结果总结

| Condition | DINOv2 mean | DINOv2 min | SigLIP mean | SigLIP min |
|-----------|-------------|------------|-------------|------------|
| **Vanilla** | 0.968 | 0.899 | 0.953 | 0.843 |
| **Full OCC** | 0.964 | 0.842 | 0.960 | 0.880 |
| **Detach OCC** | **0.539** | **0.448** | **0.312** | **0.223** |

## 核心发现

**Detach OCC 的 encoder 表征发生了灾难性偏移：**

1. **Vanilla & Full OCC** 的 CKA 均在 0.84-0.99 范围，说明 fine-tuning 后 encoder 表征与 pretrained 高度一致——LoRA 微调正确地保留了预训练特征。

2. **Detach OCC** 的 CKA 断崖式下降：
   - DINOv2：mean 0.539（vs Vanilla 0.968），最低 block 14 仅 0.448
   - SigLIP：mean 0.312（vs Vanilla 0.953），最低 block 14 仅 0.223
   - SigLIP 退化比 DINOv2 更严重（0.31 vs 0.54）

3. **SigLIP 中层（block 10-16）退化最严重**，CKA 跌至 0.22-0.26，几乎完全丧失与 pretrained 的对齐。

## 论文意义

这直接与梯度分析互相印证：
- 梯度分析显示 Detach OCC 的 encoder 梯度只有 Vanilla 的 1-13%
- CKA 分析显示 Detach OCC 的 encoder 表征偏离 pretrained 达 0.45-0.78（1 - CKA）

解释机制：当 OCC head 的梯度被 detach 后，encoder 失去了来自辅助任务的梯度信号，但 action head 的梯度仍在更新 encoder——只是这个信号太弱（LoRA 低秩约束），导致 encoder 向一个退化方向漂移，而非保持在 pretrained 的良好初始化附近。Full OCC 提供了额外的梯度约束（occupancy prediction），相当于正则化，帮助 encoder 保持在 pretrained 附近。

产出文件：
- 服务器：`westd-34685:/root/autodl-tmp/analysis/cka/` (cka_results.json, cka_analysis.pdf, cka_analysis.png)
- 本地：`artifacts/cka_results.json`, `artifacts/cka_analysis.py`

---
