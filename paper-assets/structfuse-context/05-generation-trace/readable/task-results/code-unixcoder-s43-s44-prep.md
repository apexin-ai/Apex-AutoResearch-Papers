# code unixcoder s43 s44 prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unixcoder_s43_s44_prep_20260516T075817_result.json`
- **Structured JSON:** [`cc9990ce6115c3c42e22.json`](../../sessions/cc/cc9990ce6115c3c42e22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出总结

**脚本路径**：
- `/root/structfuse/scripts/run_unixcoder_3strategies_s43.sh`
- `/root/structfuse/scripts/run_unixcoder_3strategies_s44.sh`

**与 s42 的差异**：
- `SEED=43` / `SEED=44`
- `--early-stopping-patience 2`（s42 是 3，按统一 regime 调整）

**训练数据**：全部就绪，6 个 train + 6 个 val 文件均存在于 `/root/autodl-tmp/structfuse/full_m2_training_data/`。

**输出目录**：`/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/{strategy}_s{43,44}/`，无冲突。

**提交命令**：
```bash
# s43 和 s44 可以分配到不同 GPU 并行跑
bash /root/structfuse/scripts/run_unixcoder_3strategies_s43.sh 0
bash /root/structfuse/scripts/run_unixcoder_3strategies_s44.sh 1
```

**预估 GPU 时间**：每个 seed 3 个 strategy 串行，约 2-3h/seed。两个 seed 并行跑总共 ~3h。

---
