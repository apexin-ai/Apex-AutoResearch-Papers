# code plan a nmin scaling

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_a_nmin_scaling_20260516T095014_result.json`
- **Structured JSON:** [`844a0169730c4881a5b9.json`](../../sessions/84/844a0169730c4881a5b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功验证，日志输出：

```
n_min: 4
```

自动计算 `max(2, 8//2) = 4` 正确生效。训练在 step 0 因为某些原因报错（可能是 `/tmp` 磁盘或 checkpoint 路径问题），但参数解析和逻辑完全正确。

## 总结

1. **代码无需修改** — `pretrain_weighted.py:310-311` 已有自动 n_min 逻辑：`max(2, batch_size // 2)`
2. **之前 bs8 实验失败原因**：`run_batchsize8_seed42.sh` 显式传了 `--n_min 2`，覆盖了自动值
3. **验证脚本已创建**：`/root/provenance_weight_training/scripts/run_bs8_auto_nmin_seed42.sh`
   - 不传 `--n_min`，自动生效 n_min=4
   - 包含 `--tau 0.8`、`--eval_data_path`、`--eval_steps 500` 等完整参数
4. **Dry-run 确认**：日志打印 `n_min: 4`，参数传递正确

可以直接启动正式训练。是否现在运行？

---
