# code exp008 online probe retrain

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-online-probe-retrain_20260518T184944_result.json`
- **Structured JSON:** [`130d60578017305c21e5.json`](../../sessions/13/130d60578017305c21e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，所有验证点通过：

| 检查项 | 结果 |
|--------|------|
| 初始 probe 训练 | acc=0.9945 ✓ |
| Step 1 在线重训练 | acc=0.9945, auroc=1.0000 ✓ |
| Step 2 在线重训练 | acc=1.0000, auroc=1.0000 ✓ |
| S(t) 非零 | step1=0.9997, step2=0.0977 ✓ |
| 无 OOM | 正常完成 ✓ |
| 重训练耗时 | ~37s/次（362 forward passes + 200 epoch probe train） |

现在恢复正式参数。脚本默认值已经是 `max_steps=8000, retrain_interval=500, log_steps=10`，无需额外修改。

**总结**：

修改内容：
1. `TrainConfig` 新增 `retrain_interval: int = 500`
2. `parse_args` 新增 `--retrain_interval` 和 `--log_steps` 参数
3. 新增 `retrain_probe_online()` 函数：用 `torch.no_grad()` 遍历 362 个 calibration samples 提取当前模型 hidden states，重训 200 epoch linear probe，返回 (probe, acc, auroc)
4. 训练循环中每 `retrain_interval` 步触发重训练，替换 probe 并 log 精度

脚本已同步到 westd-28034 和 westd-29046 的 `/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py`。

---
