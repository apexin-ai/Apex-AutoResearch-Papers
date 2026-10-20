# ops fix sync rerun g2

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_sync_rerun_g2_20260513T174750_result.json`
- **Structured JSON:** [`f5f4d4c2c0de2f6cc602.json`](../../sessions/f5/f5f4d4c2c0de2f6cc602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`resume_g2_eval.py` 使用 `from metrics import compute_checkpoint_metrics`——即修复后的 metrics.py。KL 计算不会再 crash。

## 总结

| Step | 状态 |
|------|------|
| **Step 1: 文件同步** | 完成。3 个缺失文件（rerun_g2_eval.py, test_kl_divergence.py, compare_eff_rank_vs_ngram.py）已通过 ssh_execute+base64 写入。其余文件已存在。 |
| **Step 2: 验证** | 通过。metrics.py 已有 `effective_vocab` 修复。 |
| **Step 3: Unit test** | **3/3 全部通过**：OOV tokens (kl=7.78)、same distribution (kl≈0)、bootstrap CI。 |
| **Step 4: v7 进程** | v7 (PID 60104) 已结束（KL crash: shapes (50277,) vs (50254,)）。 |
| **Step 5: G2 eval rerun** | **已在运行**。另一个 worker 已提交 `resume_g2_eval.py` 作为 mvp_pilot_v8，正在评估 checkpoint 1/6（spectral-rank 79%）。使用修复后的 metrics.py，KL 不会再 crash。 |

**注意事项**：
- 有两个重复的 v8 job（mvp_pilot_v8 和 mvp_pilot_v8_r2）同时在 GPU 0 上运行，可能导致 GPU 争用和变慢
- G2 共 6 个 checkpoints：checkpoint-76, 152, 228, 304, 305, final_model
- G1 synth data 加载成功（10M tokens），KL divergence 将正常计算
- 结果将写入 `/root/autodl-tmp/output_v7/G2/metrics/metrics.jsonl`

无需再手动启动 rerun——等 v8 job 完成后读取结果即可。

---
