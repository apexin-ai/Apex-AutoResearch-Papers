# code p2b skip logic and eval prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p2b_skip_logic_and_eval_prep_20260512T131844_result.json`
- **Structured JSON:** [`9aa99c6982b03c3c1989.json`](../../sessions/9a/9aa99c6982b03c3c1989.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

skip 逻辑正确：`$OUT_DIR` 不再有反斜杠。全部任务完成，汇总：

### 产出

| # | 任务 | 状态 |
|---|------|------|
| 1 | `scripts/run_p2b_all.sh` skip 逻辑 | ✓ 已添加（L34-38），检查 `$OUT_DIR/final/model.pt` 或 `$OUT_DIR/model.pt` |
| 2 | `scripts/run_eval_all.sh` 批量 eval | ✓ 已创建，使用 `--ckpt-dir`（匹配 eval_p2b.py 实际参数），自动提取 JSON 指标 + 聚合表格 |
| 3 | `batch_extract.py` 路径归一化 | ✓ 已确认包含 `normalize_path` + `_common_suffix_length`（L43+），无需修改 |
| 4 | `scripts/run_m1_extraction.sh` M1 提取 | ✓ 已创建，参数匹配 batch_extract.py（`--metadata/--output-dir/--repos-dir/--workers/--timeout/--python-only/--skip-log`） |
| 5 | run 1 checkpoint 状态 | ✓ `p2b_random_s42` 完整：4 个子目录（checkpoint-200/400/600 + final），`final/model.pt` 6.2GB，含 tokenizer + training_config.json |

当前 checkpoints 目录只有 `p2b_random_s42`，其余 8 个 run 尚未完成。重启 `run_p2b_all.sh` 时会自动 skip 这个已完成的 run。

---
