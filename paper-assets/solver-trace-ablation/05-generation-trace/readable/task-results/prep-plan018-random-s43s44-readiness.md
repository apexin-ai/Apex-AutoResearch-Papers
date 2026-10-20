# prep plan018 random s43s44 readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan018-random-s43s44-readiness_20260514T091756_result.json`
- **Structured JSON:** [`34965bb2b0e8920f9190.json`](../../sessions/34/34965bb2b0e8920f9190.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇总：

**已创建**: 服务器上 `configs/plan018_random_b01_s43.yaml` 和 `s44.yaml`

**全部验证通过**:
- 数据文件 `train_500_seed42.jsonl` 存在
- 模型路径存在
- Output 目录不存在（无覆盖风险）
- 磁盘 112G 可用
- `save_total_limit=1`、`log_completions=False` 已在脚本中硬编码

**关键发现**: `train_grpo.py` 的 config 加载有 bug——argparse 默认值非 None 时 YAML 不会覆盖。因此提交命令必须显式传 `--beta 0.1 --num_steps 500 --seed 43/44`，不能只靠 YAML config。

**提交命令已写入** `artifacts/plan018/random_s43s44_readiness.md`，等 GPU 空闲后替换 `N`/`M` 为实际 GPU 编号即可执行。当前两张 GPU 都被占用（~80G/98G）。

---
