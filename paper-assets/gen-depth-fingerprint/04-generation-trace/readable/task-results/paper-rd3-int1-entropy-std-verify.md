# paper rd3 int1 entropy std verify

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rd3-int1-entropy-std-verify_20260516T051818_result.json`
- **Structured JSON:** [`1f01a756a20019dde126.json`](../../sessions/1f/1f01a756a20019dde126.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Generator | entropy_std ρ | p-value | entropy_mean ρ | tail_decay ρ |
|-----------|--------------|---------|----------------|-------------|
| olmo-2-1b | **-0.2958** | <1e-6 | -0.6386 | -0.1411 |
| pythia-1b | **-0.2414** | <1e-6 | -0.7120 | +0.0904 |
| pythia-2.8b | -0.1530 | <1e-6 | -0.6754 | +0.0633 |
| qwen3-0.6b | **-0.2294** | <1e-6 | -0.5656 | -0.0902 |
| qwen3-1.7b | -0.1882 | <1e-6 | -0.6022 | -0.0698 |
| qwen3-8b | -0.0755 | <1e-6 | -0.4754 | -0.0894 |

### 判断

**entropy_std 的 "near-stationary" 分类需要加 caveat。** 3/6 generator 的 |ρ| > 0.2：

- 最大偏离：**olmo-2-1b** (ρ = -0.296)
- 其次：pythia-1b (-0.241)、qwen3-0.6b (-0.229)

所有 generator 的 entropy_std ρ 都是**负值**，说明 entropy_std 随 depth 系统性下降（方差收缩），只是幅度因模型而异。Overall |ρ| = 0.076 之所以小，并非因为各模型都接近零，而是小模型（1B 级）有较强负相关，大模型（qwen3-8b）接近零，混合后被稀释。

对比特征：entropy_mean 全部 |ρ| > 0.47（强 depth-sensitive），tail_decay 全部 |ρ| < 0.15（真正 near-stationary）。

结果已保存到服务器 `results/rd3_int1_entropy_std_pergen.json` 和本地 artifacts，并注册为 `art_20260516_8edcf5`。

---
