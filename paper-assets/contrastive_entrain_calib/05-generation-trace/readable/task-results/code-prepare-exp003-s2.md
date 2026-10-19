# code prepare exp003 s2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp003-s2_20260519T065333_result.json`
- **Structured JSON:** [`4cf112e396e85b515be4.json`](../../sessions/4c/4cf112e396e85b515be4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

**脚本路径**: `/root/contrastive_entrain_calib/training/run_exp003s2_r3only.py` (westd-29046)

**配置摘要** (与 exp-003 仅 seed 和输出目录不同):

| 参数 | exp-003 | exp-003-s2 |
|------|---------|------------|
| seed | 42 | **43** |
| output_dir | `exp003_r3only_seed1` | **`exp003s2_r3only`** |
| r1/r2/r3 | 0.0 / 0.0 / 1.0 | 0.0 / 0.0 / 1.0 |
| r3_model | cross-encoder/nli-deberta-v3-base | cross-encoder/nli-deberta-v3-base |
| data_path | `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` | 同左 |
| LoRA r/alpha | 64/64 | 64/64 |
| max_completion_length | 256 | 256 |
| num_generations | 2 | 2 |
| lr / beta | 5e-5 / 0.04 | 5e-5 / 0.04 |

**数据路径验证**: `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` 存在 (367KB)

**Dry-run**: Syntax OK

注意：westd-28034 上已有的 `run_exp003_r3only_seed2.py` 与原版 exp-003 存在配置差异（r3_model_name、max_completion_length=512、num_generations=4），不是纯 seed 复现。westd-29046 上新建的版本严格只改了 seed 和 output_dir。

---
