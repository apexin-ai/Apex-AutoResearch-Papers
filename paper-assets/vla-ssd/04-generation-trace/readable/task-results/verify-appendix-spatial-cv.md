# verify appendix spatial cv

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_appendix_spatial_cv_20260523T184704_result.json`
- **Structured JSON:** [`02159f0a3620e378e602.json`](../../sessions/02/02159f0a3620e378e602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Spatial 表 CV 列：4 个值全部不一致

| Condition | Paper d | Pipeline d | Paper CV | Pipeline CV | 差异 |
|-----------|---------|------------|----------|-------------|------|
| Empty | 1.173 | 1.181 | **0.185** | **0.087** | ❌ 偏差 +0.098 |
| Wrong | 0.885 | 0.915 | **0.093** | **0.272** | ❌ 偏差 -0.179 |
| Shuffled | 0.979 | 0.994 | **0.166** | **0.162** | ❌ 偏差 +0.004 |
| Paraphrased | 0.807 | 0.816 | **0.128** | **0.179** | ❌ 偏差 -0.051 |

Cohen's d 列使用的是全局 d（与 ranking 一致，无误），但 CV 列与管线 `cross_task_variance.cohens_d.cv` 严重不符。

Empty 和 Wrong 的 CV 看起来可能被**互换**了（paper Empty=0.185 ≈ pipeline Paraphrased=0.179；paper Wrong=0.093 ≈ pipeline Empty=0.087），但即使考虑互换也无法完全对齐。

**正确值**（来自管线 JSON，population std）：

```
Empty:       CV = 0.087
Wrong:       CV = 0.272
Shuffled:    CV = 0.162
Paraphrased: CV = 0.179
```

### Goal 表

Goal 表 (`tab:counterfactual_goal_detail`) 没有 CV 列，无需核查。管线中 Goal 的 CV 值为：empty=0.073, wrong=0.087, shuffled=0.042, paraphrased=0.104。

---
