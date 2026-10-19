# code prepare 4suite eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-4suite-eval_20260515T211447_result.json`
- **Structured JSON:** [`e72c2b3496862fb1d6b2.json`](../../sessions/e7/e72c2b3496862fb1d6b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。汇报：

### Suite 参数机制
- `lerobot-eval` 通过 `--env.task=$suite` 指定 suite
- 每个 suite 独立跑，输出到 `$OUTPUT_DIR/$suite/`

### Suite 名称
项目中使用的 4 个 suite（注意：**不是 `libero_long`，而是 `libero_10`**）：

| Suite | 说明 |
|-------|------|
| `libero_spatial` | 空间推理任务 |
| `libero_object` | 物体操作任务 |
| `libero_goal` | 目标导向任务 |
| `libero_10` | 长horizon任务（LIBERO 原始命名为 libero_long） |

### 当前完成状态
- `baseline_std` (v1): 4 suite 全部完成
- `baseline_std_v3`: 只完成 `libero_spatial`，剩余 3 个待跑
- `baseline_plus_v2`: 只完成 `libero_spatial`，剩余 3 个待跑

### 脚本使用
```bash
# baseline_std_v3 补跑（GPU 1）
bash /root/acib/scripts/run_remaining_suites_eval.sh lerobot/smolvla_libero 1 "libero_object libero_goal libero_10" /root/acib/outputs/baseline_std_v3

# baseline_plus_v2 补跑（GPU 0）
bash /root/acib/scripts/run_remaining_suites_eval.sh lerobot/smolvla_libero_plus 0 "libero_object libero_goal libero_10" /root/acib/outputs/baseline_plus_v2
```

脚本已创建于 `/root/acib/scripts/run_remaining_suites_eval.sh`，风格与 `run_eval_std_v3.sh` 一致（含 `--policy.empty_cameras=1`、`--rename_map`）。

---
