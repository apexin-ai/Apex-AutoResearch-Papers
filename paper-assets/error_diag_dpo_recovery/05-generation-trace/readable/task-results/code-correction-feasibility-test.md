# code correction feasibility test

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_correction-feasibility-test_20260512T131344_result.json`
- **Structured JSON:** [`4991c56a599e659d4faa.json`](../../sessions/49/4991c56a599e659d4faa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- `--help` 正常
- 导入成功，函数正确导出
- `select_tasks` 正确选择 diverse task types
- `create_env` 创建的 env 正确返回指定 game_files（3/3 match=True）
- env.reset() 按顺序返回选定任务，obs 正常

**脚本文件**: `/root/autodl-tmp/error_diag_dpo_recovery/src/test_correction_feasibility.py` (313行)

**已备份被覆盖的 replay-then-correct 版本**: `test_correction_feasibility_replay.py`

**ALFWorld 重复 reset 可行性**: textworld gym env 不支持对同一 game 重复 reset，但通过 `create_env` 只注册选定的 game_files 子集，每轮创建新 env 即可重复尝试同一批任务。验证确认 game_file 匹配正确。

**运行示例**:
```bash
# 8B 模型
python src/test_correction_feasibility.py --gpu 0 --num_tasks 10 --max_attempts 10

# 14B-AWQ，从失败轨迹选任务
python src/test_correction_feasibility.py \
  --trajectory_file data/trajectories/train_part0.jsonl \
  --model_name /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ \
  --gpu 1 --num_tasks 10 --max_attempts 10 \
  --output_path data/feasibility_14b.json
```

---
