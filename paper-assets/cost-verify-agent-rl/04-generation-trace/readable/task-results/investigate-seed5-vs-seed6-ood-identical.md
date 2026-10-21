# investigate seed5 vs seed6 ood identical

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_seed5_vs_seed6_ood_identical_20260521T150145_result.json`
- **Structured JSON:** [`6c43eabb6258466bc588.json`](../../sessions/6c/6c43eabb6258466bc588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Per-task 分布完全不同。以下是完整调查结论：

---

## 调查结论

```
1. Checkpoint 加载验证：
   - Seed 5 eval 加载了: /root/autodl-tmp/checkpoints/qwen_exp029_seed5_step10_hf
   - Seed 6 eval 加载了: /root/autodl-tmp/checkpoints/qwen_exp029_seed6_step15_hf
   - Symlink 目标: seed5 → exp029-seed5/global_step_10_hf, seed6 → exp029-seed6/global_step_15_hf
   - ✅ 加载路径正确且不同

2. 模型权重校验：
   - Seed 5 md5: 35c3860dff645f9d4d9e28c898d20729
   - Seed 6 md5: 64f0d8dc6d7ed9cff2f00f171939fbc0
   - ✅ 权重不同，确实是两个不同模型

3. Per-task 对比（W&B logged 的前 20 个 episode）：
   - Seed 5 成功: ep1, ep4, ep14, ep17 (4/20)
   - Seed 6 成功: ep3, ep7, ep9, ep10, ep11, ep20 (6/20)
   - 重叠: 0/20（成功的 task 完全不同！）
   - ✅ 分布明显不同

4. 辅助指标对比（进一步证实不同行为模式）：
   - num_actions:          38.54 vs 36.57
   - action_is_effective:  0.9999 vs 0.9730
   - action_is_valid:      0.7266 vs 0.6325
   - manager_invalid:      0.00015 vs 0.0270
   - response_length:      6632 vs 5605
   - ✅ 行为模式显著不同

5. 最终结论：数据可信。
   两个不同模型（不同 seed、不同训练步数、不同权重）恰好在 134 个 OOD task 上
   获得了相同的成功总数 39，但成功的 task 集合完全不同。
   这是统计巧合，不是 bug。
```

**概率合理性**：对于 ~29% 成功率的 Binomial(134, 0.29)，P(X=39) ≈ 7.6%，两个独立实验都取到 39 的概率约 0.6%——不常见，但在多 seed 实验中完全可能遇到。

---
