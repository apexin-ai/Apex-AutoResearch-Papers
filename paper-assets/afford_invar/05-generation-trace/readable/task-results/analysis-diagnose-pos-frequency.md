# analysis diagnose pos frequency

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnose-pos-frequency_20260520T001840_result.json`
- **Structured JSON:** [`2c2f6bc0016b17f2f717.json`](../../sessions/2c/2c2f6bc0016b17f2f717.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因找到了。**

## 诊断结果

10 条 LIBERO-Goal instructions 全部在 pair_index 中，但它们之间只有 **1 对** 正样本：

```
push the plate to the front of the stove <-> put the cream cheese in the bowl (sim=0.888)
```

其余 44 对 LIBERO-Goal 指令之间的 SigLIP similarity 全部 < 0.8，无法形成正样本。

### pos_count 推算

- 只有 2/10 的 instructions（上述这对的两端）有机会在 queue 中找到正样本
- batch_size=2 随机采样，anchor 命中这 2 条 instruction 的概率 ≈ 20%
- 期望 pos_count ≈ 0.4/step → 实际观测 0.27/step ✓（考虑采样方差，吻合）

### 这不是 transfer_proj 的 bug

pos_count **完全由 instruction matching 决定**，和 feature 提取方式（spatial_normalize vs transfer_proj）无关。`is_positive_pair` 只看 `instr_to_idx` 查表，不用 feature similarity。

### v1 的 1.55/step 从哪来？

最可能的解释：**v1 用了不同的 dataset**。config 默认是 `libero_spatial_no_noops`（10 个 "pick up the black bowl from X" 任务），而 v2 切换到了 `libero_goal_no_noops`。LIBERO-Spatial 的 10 条指令结构高度相似，会产生大量正样本对。

我在服务器上没找到 `phase1_transfer_v1.log`，无法直接确认 v1 的 dataset。你能确认 v1 用的是哪个 dataset 吗？

### 建议

1. **不需要 kill 当前训练**——代码没有 bug，transfer_proj 工作正常
2. 如果希望 LIBERO-Goal 上也有足够的正样本，需要以下之一：
   - **降低 sim_threshold**（比如 0.70），增加 intra-goal positive pairs
   - **启用 paraphrase augmentation**：训练时随机用 paraphrases 替换原始 instruction，这样 queue 里会出现同一 task 的 paraphrases，它们之间 similarity 很高
   - **扩大 pair_index 构建时的 instruction 集**：把 LIBERO-Goal instructions 的 paraphrases 也加入训练数据流

---
