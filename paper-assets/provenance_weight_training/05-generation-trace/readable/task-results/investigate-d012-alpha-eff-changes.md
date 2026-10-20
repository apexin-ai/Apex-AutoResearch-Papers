# investigate d012 alpha eff changes

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_d012_alpha_eff_changes_20260514T171247_result.json`
- **Structured JSON:** [`eb01a7954895e919dabf.json`](../../sessions/eb/eb01a7954895e919dabf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因找到了。**

## 完整报告

### 1. D012 对 `alpha_eff.py` 的变更

**零改动。** 文件完全未修改。服务器上存在 `pretrain_weighted.py.v1_backup`，diff 确认 `alpha_eff.py` 从始至终未被触碰。

### 2. Early return 逻辑

`if alpha_0 >= tau: return 0.0` **从最初版本就存在**，不是 D012 引入的。Reviewer 的怀疑不成立。

### 3. D012 实际改动 (`pretrain_weighted.py` diff)

| 变更 | 旧版 | 新版 | 影响 |
|------|------|------|------|
| **n_min 默认值** | `max(1, int(batch_size*0.75))` = **3** | `max(2, batch_size//2)` = **2** | 唯一实质性改动 |
| unweighted_loss | 不记录 | 新增记录 | 仅日志 |
| gradient_checkpointing | 支持 | 移除，改为 resume_from_checkpoint 重构 | 无关 |
| W&B 指标 | 无 weighted/unweighted 分离 | 新增 | 仅日志 |
| **EMA 平滑 b*** | 不存在 | **也不存在** | D012 描述了 EMA 但最终未实现 |

### 4. b=0 比例 1.7% → 78% 的根因

**是数据分析错误，不是代码问题。**

```
adaptive_fix_seed42 step_metrics.jsonl 总览:
  Training 条目: 6,130 → b=0 = 138 (2.3%)
  Eval 条目:    25,431 → b=0 = 25,419 (100.0%)
  混合计算:     31,521 → b=0 = 25,554 (81.1%) ← 报告的 ~78%
```

- 旧版 adaptive 的 step_metrics **没有 eval 条目**（24,412 = 6103×4，纯训练数据）
- 新版 adaptive_fix 的 step_metrics **混入了 25,431 条 eval 数据**（eval 数据集几乎全是 human 样本，alpha_0 ≈ 1.0 >> tau=0.8，100% 触发 early return → b=0）
- **仅看 training 条目：b=0 rate 从 1.9% → 2.3%，本质无差异**

D015 已经警告过这个问题：「step_metrics 混入 eval 数据需在分析代码中过滤」。

### 5. 结论

D012 **只改了 n_min 默认值**（3→2），没有其他算法改动。EMA 未实现，alpha_eff.py 未修改。78% b=0 是 eval 数据污染 step_metrics 的分析 artifact。

---
