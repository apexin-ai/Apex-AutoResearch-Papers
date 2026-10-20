# train sft v2 retrain

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft-v2-retrain_20260514T093500_result.json`
- **Structured JSON:** [`b78710d6934ca1e26f26.json`](../../sessions/b7/b78710d6934ca1e26f26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT v2 训练完成。最终结果：

| 指标 | 值 |
|------|-----|
| 训练时间 | 177s (约 3 分钟) |
| 最终 loss | 1.59 (epoch 2.65) → train_loss 均值 2.00 |
| token accuracy | 0.659 |
| 模型保存路径 | `/root/autodl-tmp/diagprobe/checkpoints/sft_v2` |

**汇报总结：**
- **sandbox.py 同步**: 完成，341 行写入服务器
- **快速验证**: 10 样本中 5 个 probe 执行成功（从 0% 修复到 50%+）
- **SFT v2 训练**: 成功完成 3 epochs，模型已保存到 `checkpoints/sft_v2`
- **注意**: eval data 被跳过（`WARNING Skipping eval data without good_probe/probe_rationale fields`），eval 需单独安排
- **GPU 0 已释放**，双卡 eval 可随时启动

---
