# ops verify baseline norm stats

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_baseline_norm_stats_20260522T111400_result.json`
- **Structured JSON:** [`e7de22671762b7f3e97f.json`](../../sessions/e7/e7de22671762b7f3e97f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process 396303 is already dead — no need to kill it.

## 结论

**baseline eval 的 norm_stats 加载没有被破坏。** 具体发现：

1. **norm_stats 完全一致** — `baseline_object_pudding_eval/best/assets/` 和 `baseline_object_pudding/baseline_object_pudding_seed0/best/assets/` 下的 `norm_stats.json` 内容完全相同。v11 的手动加载路径正确。

2. **displacement 差异是采样方差，不是代码 bug** — v10 eval 跑了 50 个 episode，前 3 个的 displacement 分别是 `[0.000, 0.000, 0.196]`，均值 0.065m。v11 dry-run 只跑了 3 个 episode 得到 0.0076m，完全在正常波动范围内。这个指标的 per-episode 方差极大（0 到 0.29m）。

3. **v10_bak 不是 v10 eval 实际使用的代码** — v10 eval 日志里有 `[EVAL CONFIG]` 输出行，v10_bak 里没有这行。实际的 v10 eval 代码更接近 v11（使用 `pi0_libero_low_mem_finetune` config + `_dc.replace` override）。

4. **必须使用 `gemma_2b_lora` config** — 用 `gemma_2b`（非 LoRA）加载这个 checkpoint 会产生全零 action，机器人完全不动。v11 的 config 选择是正确的。

5. **`extra_delta_transform=False` override 是必要的** — `pi0_libero_low_mem_finetune` 默认是 `True`，v11 的 `_dc.replace` 覆盖为 `False` 是正确的。

6. **文件已恢复为 v11 版本**，无永久性改动。v10like 测试进程已自然结束。

**如果需要公平对比 v10 和 v11 的 baseline 性能，应该用 v11 代码跑完整 50 个 episode。** 3 个 episode 的结果不具备统计意义。

---
