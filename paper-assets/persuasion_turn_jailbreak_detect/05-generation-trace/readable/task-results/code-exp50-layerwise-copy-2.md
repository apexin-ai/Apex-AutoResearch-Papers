# code exp50 layerwise

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp50_layerwise_20260522T092001_result.json`
- **Structured JSON:** [`5f997f855d3f67d658b0.json`](../../sessions/5f/5f997f855d3f67d658b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp50 结果汇报

实验已完成，脚本和结果均已在服务器上。

### 产出文件
- `results/exp50_layerwise_results.json`
- `figures/paper/fig_layerwise_pr_fisher.pdf`

### 关键发现 — **强支持 hypothesis**

**Participation Ratio (PR):**

| Layer | vanilla | 9-class | scrambled | JB-MLM |
|-------|---------|---------|-----------|--------|
| 0-8   | ~1-10   | ~1-9    | ~1-9      | ~1-9   |
| **9** | **6.68** | **2.88** | **2.79** | 7.09 |
| **10** | **9.70** | **1.47** | **1.87** | 8.95 |
| 11-12 | 1.4-1.5 | 1.8-2.0 | 1.5-1.7  | 1.4-1.7 |

- Layers 0-8: 四个变体 PR 相似（无显著差异）
- **Layers 9-10: 9-class 和 scrambled 的 PR 急剧下降**（从 ~3-9 降到 1.5-2.9），而 vanilla 和 JB-MLM 维持高 PR（7-10）
- 分类训练引发的 **dimensional compression 集中在 layer 9-10** ✓

**Fisher Ratio:**

| Layer | vanilla | 9-class | scrambled | JB-MLM |
|-------|---------|---------|-----------|--------|
| 0-5   | 0-0.78  | 0-0.84  | 0-0.81    | 0.3-0.85 |
| 6-7   | 1.1-1.5 | 1.5-2.0 | 1.3-1.7   | 1.1-1.5 |
| **8** | 1.47    | **3.20** | **2.50**  | 1.40 |
| **9** | 1.04    | **4.03** | **3.76**  | 1.07 |
| **10** | 0.73   | **10.92**| **5.93**  | 0.93 |
| **11** | 2.28   | **9.10** | **7.37**  | 3.33 |
| **12** | 2.83   | **6.53** | **7.91**  | 2.61 |

- Layers 0-7: 判别力弱且变体间相似
- **Layer 8 开始分叉，9-class 在 layer 10 达到峰值 Fisher=10.92（vanilla 同层仅 0.73，相差 15 倍）**
- scrambled 峰值在 layer 12（Fisher=7.91 vs vanilla 2.83）
- **JB-MLM 全程跟踪 vanilla**，确认 MLM 不产生判别性压缩

### 结论

1. **Discriminative compression 是后期层现象** — PR 在 layer 9-10 对分类变体急剧下降，与 Maennel 2020 的"早期层统计量标签无关"机制形成区分 ✓
2. **判别力集中在 layers 8-12** — 9-class 的 Fisher ratio 在 layer 10 达到 10.92，是 vanilla 的 15 倍 ✓
3. **MLM 不产生此效应** — JB-MLM 全程与 vanilla 趋势一致，说明 compression 是分类监督的特有产物 ✓
4. **scrambled 也展现后期层 compression**（虽然幅度略低于 9-class）— 说明任何分类信号（即使标签被打乱）都足以引发后期层结构重组

---
