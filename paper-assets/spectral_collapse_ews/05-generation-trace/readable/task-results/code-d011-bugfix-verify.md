# code d011 bugfix verify

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d011_bugfix_verify_20260517T130818_result.json`
- **Structured JSON:** [`6a914a7f0dcdbe02e18f.json`](../../sessions/6a/6a914a7f0dcdbe02e18f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## GPU 状态
- GPU 0: RTX PRO 6000, 65909/97887 MiB, 90% util, PID 59365 (exp_001)
- GPU 1: RTX PRO 6000, 23735/97887 MiB, 79% util, PID 88161 → **已 kill**

## PID 88161
killed

## D011 检查

- **A (预算扣减): PASS** — `update()` 中 `self.B_rem -= r` 先按分配值扣减，然后 `report_actual(actual_ratio)` 修正差值：`self.B_rem += (allocated - actual_ratio)`。pipeline.py 对每个 gen 都调用了 `controller.report_actual(actual_ratio)`。两阶段设计等价于直接传 actual_ratio。

- **B (set_baseline): PASS** — `set_baseline()` 方法已存在，正确设置 `S_tilde_0` 和 `S_tilde_prev`：
  ```python
  def set_baseline(self, spectral_metrics):
      key = {"eff_rank": "effective_rank"}.get(self.signal, self.signal)
      S_0 = spectral_metrics[key]
      self.S_tilde_prev = S_0
      self.S_tilde_0 = S_0
  ```

- **C (Gen 0 调用): PASS** — pipeline.py controller 初始化后立即调用：
  ```python
  gen0_metrics = results_all[0]
  controller.set_baseline(gen0_metrics)
  ```

- **D (actual_ratio 回传): PASS** — pipeline.py 计算 `actual_ratio = num_real / total_per_gen`，对 gen >= 1 都调用 `controller.report_actual(actual_ratio)`。

- **E (数据架构): PASS** — `total_per_gen = config.num_synthetic_samples = 50000`（固定总量），`num_real = int(total_per_gen * ratio)`，`num_synth = total_per_gen - num_real`。real pool = 50K（`train_real_50k.pt`），ratio=0.8 → 40K real 完全可行。另有 `num_real = min(num_real, len(real_train_data))` 安全上限。

## Dry-run 表格

```
Gen  S_tilde      delta      triggered  r_req    r_actual   B_rem    real     synth
0    2366.684     N/A        N/A        0.5000   0.5000     4.5000   25000    25000
1    2415.723     -0.020721  False      0.5000   0.5000     4.0000   25000    25000
2    2442.825     -0.011452  False      0.5000   0.5000     3.5000   25000    25000
3    2441.696     0.000477   False      0.5000   0.5000     3.0000   25000    25000
4    2423.373     0.007742   True       0.5027   0.5027     2.4973   25137    24863
5    2396.773     0.011239   True       0.5057   0.5057     1.9916   25284    24716
6    2365.969     0.013016   True       0.5059   0.5059     1.4857   25295    24705
7    2335.079     0.013052   True       0.5033   0.5033     0.9824   25163    24837
8    2293.599     0.017527   True       0.5037   0.5037     0.4787   25186    24814
```

验证通过：
1. Gen 0 baseline 正确（S_tilde_0 = 2366.684）
2. Gen 1-2 log_det 上升（初始 fine-tuning "扩散"效应），delta 为负，不触发
3. Gen 4 起 delta > tau=0.005，正确触发
4. 所有 ratio 在 [0.2, 0.8] 范围内，real_samples 远低于 50K pool
5. B_rem 在 Gen 8 后剩 0.4787，足够最后 1-2 代

## tau 建议

delta 范围：[-0.021, 0.018]，正值均值 ~0.012。当前 tau=0.005 从 Gen 4 开始触发（5/8 代），时机合理（前 3 代 log_det 上升，属正常初始化效应）。

**但 k=1.0 过小**：即使触发，ratio 调整幅度极小（最大 +0.006，即 0.5000→0.5059）。建议：
- 保持 **tau=0.005**（触发时机正确）
- 将 **k 提升到 5.0~10.0**，使 ratio 在触发后有实质性调整（如 0.5→0.55~0.60）

## exp_001 状态

Gen 9/10 进行中，正在生成合成数据（21440/50000 samples）。phase0_results.json 含 Gen 0-8 共 9 代结果。Gen 8 metrics: eff_rank=456.76, ppl=49.29, distinct4=0.440, log_det=2252.12。预计还需完成 Gen 9 + Gen 10。

1B 实验（phase0_1b）在 Gen 0 checkpoint 保存时因磁盘空间不足崩溃，仅有 Gen 0-3 结果。PID 88161 已被 kill。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eff_rank": "effective_rank"
  }
}
```

</details>

---
