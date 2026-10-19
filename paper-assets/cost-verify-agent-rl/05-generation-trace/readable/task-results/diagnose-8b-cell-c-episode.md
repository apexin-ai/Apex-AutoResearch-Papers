# diagnose 8b cell c episode

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b_cell_c_episode_20260519T114351_result.json`
- **Structured JSON:** [`b12a233acf24ad1649c7.json`](../../sessions/b1/b12a233acf24ad1649c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/diagnose_8b_cell_c_oom.md`。

**核心结论**:

- **OOM 触发点**: 第一个 training step 的 `loss.backward()`（`dp_actor.py:468`），不是 rollout 也不是 eval
- **根因**: `use_dynamic_bsz=False` + `context_window_mode=full`。micro-batch 按样本数切分（每批 1 个样本），但单个 full-context episode 可达 17K tokens。8B 模型在 FSDP backward 时需要聚合全量参数（~16 GB）+ 梯度（~16 GB）+ 激活重计算，单卡峰值 ~88 GiB，只剩 6.47 GiB 不够 8.76 GiB 的分配请求
- **1.7B 没问题的原因**: 参数量仅 1.7B（vs 8B），backward 峰值 ~15-20 GB，远低于 GPU 容量

**推荐修复**: 启用 `use_dynamic_bsz: True` + 降低 `ppo_max_token_len_per_gpu` 到 16384。这是最小改动且最可能解决的方案。

---
