# verify vota no ae eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_vota_no_ae_eval_20260515T063722_result.json`
- **Structured JSON:** [`62d59806cbf006b05f81.json`](../../sessions/62/62d59806cbf006b05f81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论如下：

```
eval_results.json: NOT_FOUND
bootstrap_compare.json: NOT_FOUND
metrics 来源: 不明
  - 训练日志中无 0.9941 这个数字（grep 无匹配）
  - 训练日志中 eval_mean_token_accuracy: epoch2=0.9583, epoch3=0.9577（Trainer 内置 eval，token 级别）
  - 训练步的 mean_token_accuracy 约 0.9910-0.9918（训练集 token 准确率）
  - 0.9941 不对应任何已知指标，来源完全不明
no_trace_v5 进度: 已完成（log 显示 no_trace 训练结束），GPU 1 空闲（0%, 0 MiB）
建议: 需要重跑 eval
```

**关键发现**：之前报告的 accuracy=0.9941 在训练日志中 **不存在**，且 eval 脚本从未执行过（无任何输出文件）。该数字既不是 Trainer 内置 eval 的结果（0.9577），也不是训练 accuracy（~0.9910），来源不明，**不可信**。

**eval 脚本命令格式**：
```bash
python /root/trace-verdict-study/eval/evaluate.py \
  --condition vota_no_ae \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_no_ae/final \
  --gpu 0 \
  --output /root/autodl-tmp/trace-verdict-study-checkpoints/vota_no_ae/final/eval_results.json
```

---
