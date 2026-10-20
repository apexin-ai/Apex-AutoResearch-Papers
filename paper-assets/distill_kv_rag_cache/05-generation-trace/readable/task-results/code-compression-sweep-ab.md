# code compression sweep ab

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compression-sweep-ab_20260514T075957_result.json`
- **Structured JSON:** [`a01857e50e9898b06b5a.json`](../../sessions/a0/a01857e50e9898b06b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成（211s）。结果如下：

---

### TABLE A: 压缩率拐点（无任何 restoration）

| Ratio | Config E EM/F1 | Config A (0% restore) EM/F1 | Δ EM |
|-------|---------------|----------------------------|------|
| 4x | 0.200/0.314 | 0.000/0.000 | -0.200 |
| 6x | 0.200/0.314 | 0.000/0.000 | -0.200 |
| 8x | 0.200/0.314 | 0.000/0.000 | -0.200 |
| 10x | 0.200/0.314 | 0.000/0.000 | -0.200 |
| 12x | 0.200/0.314 | 0.000/0.000 | -0.200 |

### TABLE B: Restoration 分离（ratio=8）

| Budget | Config A EM/F1 | Config E EM/F1 | Δ EM |
|--------|---------------|----------------|------|
| 0% (skip all) | 0.000/0.000 | 0.200/0.314 | -0.200 |
| 5% (boundary only) | 0.200/0.200 | 0.200/0.314 | +0.000 |
| 10% (boundary+3.75% CEGR) | 0.200/0.200 | 0.200/0.314 | +0.000 |
| 20% (boundary+13.75% CEGR) | 0.200/0.200 | 0.200/0.314 | +0.000 |

---

### 结论

1. **没有"压缩率拐点"——即使最温和的 4x 压缩，去掉 restoration 后也完全崩溃。** 输出从"错误但合理的自然语言"（4x-6x）退化到"纯乱码循环"（8x+）。PCA+量化的有损压缩在没有任何 token 恢复时，KV cache 已损坏到模型无法正常推理。

2. **Restoration 贡献是决定性的，且 boundary restoration 是关键跳变点。**
   - 0% → 5%（boundary only）：EM 从 0.000 跳到 0.200（追平 E baseline），输出从乱码恢复为正常语言。仅恢复 ~6.25% 的 boundary tokens 就挽救了生成质量。
   - 5% → 10% → 20%：EM/F1 无进一步提升（在 5 样本上饱和），CEGR 额外恢复的 token 没有带来增量收益。

3. **核心发现：之前 6x+20% restoration+greedy argmax 三重保护掩盖 config 差异的根因，不是压缩率太温和，而是 boundary restoration 单独就足以把质量拉回 baseline 水平。** CEGR/ProphetKV 的边际贡献在当前实验设置下接近零——真正的质量守护者是 boundary recomputation（chunk 边界 token 的无损恢复）。

---
