# code profiling script prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_profiling_script_prep_20260525T154407_result.json`
- **Structured JSON:** [`b4adc16c33810fa09507.json`](../../sessions/b4/b4adc16c33810fa09507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**`profile_openvla_efficiency.py`** — 远程路径 `/root/autodl-tmp/importance_margin_vla_compress/profile_openvla_efficiency.py`，artifact id `art_20260525_c795b0`。

**关键设计**
- `k_ratios` 默认 `[1.0, 0.9, 0.7, 0.5, 0.3]`；`k=1.0` 不挂任何 prune hook → 真 baseline
- Hook 链顺序：`obs_hook` 先注册 → 记录 `tokens_original`；prune hook 后注册 → 记录 `tokens_kept`（PyTorch forward hook 按注册顺序串联，后注册的 hook 看到前一个 hook 的输出）。修复了初版"main + probe 各装一次 prune hook 导致重复剪枝 + n_original 失真"的 bug
- 每个 k：3 warmup → reset_peak_memory_stats → 10 次 timed forward，每次 `cuda.synchronize()` 包夹 `time.perf_counter()`
- 三种模式 `l2norm_prune` / `random_prune` / `attention_prune` 直接复用 `eval_openvla_l2norm_libero.py` 中的 hook 类
- 输出 CSV 列：`mode, k_ratio, latency_ms_{median,p10,p90}, peak_mem_mb, tokens_original, tokens_kept`

**验证（未占用 GPU）**
- `py_compile` 通过
- `--help` 输出正常
- `CUDA_VISIBLE_DEVICES=""` 完整 import（torch / hf prismatic / transformers llama / 自身模块）成功
- Hook factories 三种实例化均 OK

**未执行**：实际 forward pass。两块 GPU 都在跑实验（GPU0 70%/15.6GB，GPU1 56%/15.7GB）；OpenVLA-7B bf16 ≈ 14GB，挤上去会冲击在跑的实验，遵循任务约束跳过。

---
