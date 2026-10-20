# code ifr proportional binarization

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ifr-proportional-binarization_20260513T075334_result.json`
- **Structured JSON:** [`4bf259a252cda03d0df1.json`](../../sessions/4b/4bf259a252cda03d0df1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

```
=== Proportional Binarization Results — Qwen-2.5 0.5B IOI ===
Total edges: eap_ig=179,388  edge_pruning=179,388  ifr=141,384

| top-p%       | N(eap) N(ep) N(ifr) | 3/3 | 2/3  | 1/3   | J(eap,ep) | J(eap,ifr) | J(ep,ifr) |
|--------------|----------------------|-----|------|-------|-----------|------------|-----------|
| 0.056% (=100)|  100   100     79   |   0 |   70 |   139 |   0.5385  |   0.0000   |   0.0000  |
| 0.1%         |  179   179    141   |   0 |  130 |   239 |   0.5702  |   0.0000   |   0.0000  |
| 0.3%         |  538   538    424   |   0 |  253 |   994 |   0.2425  |   0.0468   |   0.0000  |
| 0.5%         |  897   897    707   |   0 |  305 | 1,891 |   0.1710  |   0.0275   |   0.0000  |
| 1.0%         | 1794  1794   1414   |   0 |  542 | 3,918 |   0.1380  |   0.0345   |   0.0000  |
| 2.0%         | 3588  3588   2828   |   0 | 1163 | 7,678 |   0.0718  |   0.1189   |   0.0000  |
| 3.5%         | 6279  6279   4948   |   1 | 2750 |12,003 |   0.0743  |   0.2015   |   0.0001  |
```

### 关键发现

1. **Proportional binarization 不能修复 IFR 零重叠问题。** CSS 3/3 在 0.056%→2.0% 全程为 0，直到 3.5%（每个方法选 ~5000–6000 条边）才出现第一个 3-way core edge。

2. **EP×IFR 的 Jaccard 极其顽固地为零**，一直到 3.5% 才出现 1 条重叠边（J=0.0001）。而 EAP-IG×IFR 在 0.3% 已经有 43 条重叠（J=0.047）。

3. **根因不是 binarization threshold，而是方法间的系统性分歧。** Layer 分布分析：
   - **EAP-IG** top-0.3%：集中在 layer 0 和 20–23（input→early + late layers）
   - **EP** top-0.3%：集中在 layer 16 和 20–23（mid-late layers）
   - **IFR** top-0.3%：集中在 layer 0–2 和 20–22（early + late，但 early 权重更大）
   
   EP 和 IFR 在 early layers 几乎无交集——EP 不重视 early layers，IFR 很重视。

4. **IFR 的 block-voting 特征依然明显**：top-1 unique score 就有 count=42（14 heads × 3 qkv），说明 IFR proximity scores 在 (src, dst_layer) 粒度上是相同的。

### 结论

问题不是 top-N 太小，而是 **IFR 和 gradient 方法在 Qwen-0.5B IOI 上发现的是结构性不同的 circuit**。EP 重视 mid→late 的路径，IFR 重视 early→mid 的路径。这是方法论层面的分歧，不是超参数能调和的。

---
