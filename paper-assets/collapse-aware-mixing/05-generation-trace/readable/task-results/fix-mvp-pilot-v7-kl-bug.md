# fix mvp pilot v7 kl bug

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp_pilot_v7_kl_bug_20260513T174505_result.json`
- **Structured JSON:** [`48b08b3503ae947bb4fe.json`](../../sessions/48/48b08b3503ae947bb4fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

G2 checkpoint-76 评估已开始，正在计算 spectral effective rank。pipeline 正常运行。

总结：

1. **Bug 根因**：`pilot_pipeline.py:50` 用 `tokenizer.vocab_size`（Pythia 返回 50254），但生成的 token ID 可超过这个值（special/padding tokens 达 50276）。`np.bincount(ids, minlength=50254)` 对不同 max token ID 的两代数据产出不同长度的分布向量。

2. **修复**：在 `compute_kl_divergence` 中添加 `effective_vocab = max(arr_a.max()+1, arr_b.max()+1, vocab_size)`，替换函数内所有 `minlength=vocab_size` 为 `minlength=effective_vocab`（包括主计算和 bootstrap 循环共 5 处）。

3. **恢复策略**：G2 训练已完成，写了 `resume_g2_eval.py` 只跑 G2 评估 + leading indicator ranking + MVP verdict，跳过已完成的 G0/G1。

4. **实验状态**：`mvp_pilot_v8_r2` 已在 `cuda:0` 上运行，正在评估 G2 的 6 个 checkpoint。预计每个 checkpoint ~15 分钟，总计 ~1.5 小时。日志在 `/root/autodl-tmp/pilot_v8.log`。

---
