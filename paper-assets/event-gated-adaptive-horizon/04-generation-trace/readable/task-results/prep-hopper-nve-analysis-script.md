# prep hopper nve analysis script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_hopper_nve_analysis_script_20260527T030533_result.json`
- **Structured JSON:** [`81a1efb97f73c11da9ff.json`](../../sessions/81/81a1efb97f73c11da9ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本工作正常。

**产出：**
- 脚本路径：`/root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_hopper_nve.py`
- Tensorboard tag 名称：实际使用 `metrics.jsonl` 格式（与项目已有脚本一致），关键字段为 `eval_return` 和 `value_mean`
- Dry-run：`--help` 通过，实际运行对已有的 baseline 和 trained_s0 正确输出 NVE trajectory，缺失的 3 个实验优雅跳过

**用法：**
```bash
python scripts/analyze_hopper_nve.py              # 全部 5 个实验
python scripts/analyze_hopper_nve.py --json        # JSON 输出
python scripts/analyze_hopper_nve.py --threshold 2.0 --sustained 3  # 自定义阈值
```

---
