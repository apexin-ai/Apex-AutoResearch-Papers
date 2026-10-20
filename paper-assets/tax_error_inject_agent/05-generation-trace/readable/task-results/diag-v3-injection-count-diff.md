# diag v3 injection count diff

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_v3-injection-count-diff_20260514T113154_result.json`
- **Structured JSON:** [`d3a7a38056a9ee4b27d8.json`](../../sessions/d3/d3a7a38056a9ee4b27d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完毕。

---

## 根因：D（不在预设选项中，实为"v3 构建时 TaxEI 注入尚未完成"）

### 时间线

| 时间 (CST) | 事件 |
|-----------|------|
| 18:46 | TaxEI v2 注入启动，开始向 `mini_pipeline_v2/injected_variants.jsonl` 逐条写入 |
| 19:03 | Random 注入**完成**，759 条 / 4,900 步全部落盘 |
| **19:12:28** | **`convert_all_v3.py` 执行，构建 v3 数据** |
| 19:12:30 | TaxEI v2 注入的第 524 条记录写完（= inject_0523） |
| **19:21** | TaxEI v2 注入**完成**，最终 760 条 / 4,671 步 |

### 关键证据

- v3 构建时，TaxEI 注入只写入了**前 524 条记录（3,369 步）**，760 条中剩余 236 条（1,302 步）尚未写完
- Random 注入在 v3 构建前 9 分钟已结束 → 759 条 / 4,900 步完整读入
- Clean 轨迹同理：v3 构建时 337 条（4,176 步），后续追加到 358 条

### 数据验证

| 数据 | v3 构建时（19:12）| 最终版（19:21+）|
|------|-----------------|----------------|
| TaxEI injected | 524 条 / **3,369 步** | 760 条 / 4,671 步 |
| Random injected | 759 条 / **4,900 步** | 759 条 / 4,900 步（不变）|
| Clean | 337 trajs / **4,176 步** | 358 trajs / 4,423 步 |

### 数据来源路径

- TaxEI 注入源：`data/mini_pipeline_v2/injected_variants.jsonl`（760 条，但 v3 只读到 524 条）
- Random 注入源：`data/random_injection/injected_variants.jsonl`（759 条，完整）
- Clean 源：`data/trajectories/successful_trajectories.jsonl`

### 建议

重跑 `convert_all_v3.py` 可消除差异（TaxEI injected 将从 3,369 增加到 4,671，接近 Random 的 4,900）。两组的原始注入记录数几乎相同（760 vs 759），真正的步数差异只有 ~5%（avg 6.15 vs 6.46 steps/record），来自 TaxEI 算子 C1_context_truncation 倾向在较早步骤注入。

---
