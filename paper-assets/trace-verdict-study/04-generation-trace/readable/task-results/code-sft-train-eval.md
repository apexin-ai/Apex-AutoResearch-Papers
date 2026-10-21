# code sft train eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft-train-eval_20260514T164002_result.json`
- **Structured JSON:** [`bdc2d768b8d89caa6c26.json`](../../sessions/bd/bdc2d768b8d89caa6c26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已部署到 westd-11235 的三个脚本：**

| 脚本 | 路径 | 状态 |
|------|------|------|
| 数据格式化 | `/root/trace-verdict-study/data/format_training_data.py` | mock 数据测试通过 |
| LoRA SFT 训练 | `/root/trace-verdict-study/train/train_sft.py` | `--help` 通过 |
| 评估 | `/root/trace-verdict-study/eval/evaluate.py` | `--help` 通过 |

**数据格式化** mock 测试结果：5 条样本 → 3 train / 2 test，三组条件（no_trace / vota / full_trace）各生成 train + test 文件，VOTA 压缩和 FullTrace 格式化均正常工作，null trace 正确处理为 `[No trace available]`。

**等数据到位后的启动命令：**
```bash
# 1. 格式化
python /root/trace-verdict-study/data/format_training_data.py

# 2. 训练（三个条件分别跑，可用不同 GPU）
python /root/trace-verdict-study/train/train_sft.py --condition no_trace --gpu 0
python /root/trace-verdict-study/train/train_sft.py --condition vota --gpu 1
python /root/trace-verdict-study/train/train_sft.py --condition full_trace --gpu 0

# 3. 评估
python /root/trace-verdict-study/eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota/final
```

`raw_traces.jsonl` 尚未生成，等另一个 Worker 完成数据生成即可启动流程。

---
