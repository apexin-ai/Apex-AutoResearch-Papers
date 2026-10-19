# code dpo pipeline prep

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-pipeline-prep_20260512T160444_result.json`
- **Structured JSON:** [`4aa894456e2cf8280be6.json`](../../sessions/4a/4aa894456e2cf8280be6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 数据格式

| 数据源 | 格式 | 关键字段 | 对话格式 |
|--------|------|----------|----------|
| `alfworld_sft.json` (expert, 3119条) | JSON array | `id`, `game_file` (相对路径), `conversations` | `{from: "human"/"gpt", value}` |
| `trajectories_v3/train.jsonl` (21条) | JSONL | `task_id` (int), `game_file` (绝对路径+`/game.tw-pddl`), `reward`, `steps` | `{role: "user"/"assistant", content}` |
| `classified/classified_errors.jsonl` (88条) | JSONL | 同上 + `error_type`, `failure_step`, `correction_horizon`, `conversations` | 同 trajectory |

Task 匹配通过 `game_file` 归一化：提取最后两级路径 `&lt;task_dir>/&lt;trial_dir>`。

### CLI 接口

**`src/measure_correction_span.py`** (P1 gate)
```bash
python src/measure_correction_span.py \
  --classified data/classified/classified_errors.jsonl \
  --expert eto_repo/data/alfworld_sft.json \
  --output data/correction_span_results.jsonl  # 可选
```

**`src/build_dpo_pairs.py`**
```bash
python src/build_dpo_pairs.py \
  --classified data/classified/classified_errors.jsonl \
  --expert eto_repo/data/alfworld_sft.json \
  --trajectory_dir data/trajectories_v3  # 可选，classified 已含 conversations \
  --output data/dpo_pairs_v2.jsonl
```

### Dry-run 结果

**Correction span** (82/88 matched, 6 expert 未匹配):
- action: N=5, mean=1.20
- verification: N=4, mean=1.00
- planning: N=73, mean=5.32
- **Kruskal-Wallis: H=16.839, p=0.0002 (\*\*\*) — 三类 error type 的 correction span 差异高度显著**

**DPO pairs**: 67/88 成功构建 (15 build_failed, 6 no_expert_match)

### 注意事项
- **数据盘 100% 满**（169G，structfuse 占 107G）。DPO 输出需写到 root 分区 (`/tmp/` 或 `/root/`) 或先清理空间。
- 当前 88 条 classified 数据中，verification 类仅 4 条且均未生成 DPO pair（failure_step ≈ expert_steps，无有效 chosen continuation）。等更多轨迹数据收集完成后会改善。

---
