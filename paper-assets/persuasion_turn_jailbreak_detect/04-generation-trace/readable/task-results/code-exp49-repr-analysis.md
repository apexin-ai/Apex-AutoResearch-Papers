# code exp49 repr analysis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp49_repr_analysis_20260522T071133_result.json`
- **Structured JSON:** [`fcb15ebe5960f7dc9b37.json`](../../sessions/fc/fcb15ebe5960f7dc9b37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总如下：

## exp49 完整结果

### A1: Weight Distance from Pretrained

| Variant | Overall L2 | Relative Norm |
|---------|-----------|---------------|
| vanilla | 0.0000 | 0.000000 |
| wiki-MLM | 2.9236 | 0.002214 |
| binary | 3.1603 | 0.002393 |
| JB-MLM | 3.3750 | 0.002556 |
| scrambled | 3.7398 | 0.002832 |
| 9-class | 3.9984 | 0.003028 |
| **topic** | **4.8941** | **0.003706** |

所有变体的 weight distance 量级相近 (relative norm ~0.002-0.004)，分类变体略大于 MLM 变体。

### A2: SVD Geometry (Representation Collapse)

| Variant | PR (有效维度) | Top10 Var% | Eff Dim 90% |
|---------|-------------|-----------|-------------|
| **vanilla** | **31.93** | 94.31% | **13** |
| wiki-MLM | 25.00 | 96.67% | 7 |
| JB-MLM | 24.56 | 96.35% | 7 |
| topic | 14.46 | 98.97% | 4 |
| 9-class | 9.37 | 99.59% | 3 |
| scrambled | 7.82 | 99.63% | 2 |
| **binary** | **3.73** | **99.90%** | **1** |

**关键发现**: 分类变体 PR 远低于 MLM/vanilla，符合预期排序：
- 分类 DAPT 大幅压缩表征空间 (PR: 3.73-14.46)
- MLM DAPT 保留更多结构 (PR: 24-25)
- Vanilla 最丰富 (PR: 31.93)

### A3: Clustering (Fisher Ratio)

| Variant | JB Intra | Benign Intra | Inter Dist | Fisher Ratio |
|---------|---------|-------------|-----------|-------------|
| vanilla | 0.000437 | 0.000183 | 0.000207 | **0.000069** |
| wiki-MLM | 0.002103 | 0.001166 | 0.000964 | 0.000284 |
| JB-MLM | 0.000439 | 0.000200 | 0.000727 | 0.000829 |
| topic | 0.413848 | 0.522339 | 0.107958 | 0.012449 |
| scrambled | 0.254468 | 0.002486 | 0.817798 | 2.602778 |
| 9-class | 0.397623 | 0.002132 | 1.336193 | 4.466274 |
| **binary** | **0.112958** | **0.005028** | **1.525593** | **19.726283** |

**关键发现**:
- **分类变体 Fisher ratio 比 MLM/vanilla 高 3-5 个数量级**
- Binary 最强 (19.73) > 9-class (4.47) > scrambled (2.60) >> topic (0.01) >> MLM/vanilla (~0)
- MLM 和 vanilla 的 inter-class distance 接近 0，表明 Stage-1 MLM 几乎不编码 jailbreak/benign 区分

### 对 "Optimization Regularization" Claim 的启示

这些结果**强有力支持** optimization regularization 假说：

1. **分类 DAPT 产生 representation collapse** (PR 大幅下降)，将高维表征压缩到少数几个方向，而 MLM DAPT 保持接近 vanilla 的丰富结构
2. **分类 DAPT 的 Fisher ratio 极高**，说明表征空间被分类目标"雕刻"出类别结构；scrambled 也有高 Fisher ratio (2.60) 是因为虽然标签被打乱，但分类训练本身仍然迫使模型学习某种判别结构
3. **Weight distance 相近但 representation 差异巨大**——所有变体改动权重的幅度类似 (~0.2-0.4% relative)，但分类 DAPT 把表征空间压缩到 1-4 维有效维度，而 MLM 保持 7 维，vanilla 13 维

---
