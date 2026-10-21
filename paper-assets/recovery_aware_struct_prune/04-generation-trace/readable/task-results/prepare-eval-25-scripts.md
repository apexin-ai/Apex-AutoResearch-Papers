# prepare eval 25 scripts

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_eval_25_scripts_20260514T183630_result.json`
- **Structured JSON:** [`3526fb457a523d7bcc34.json`](../../sessions/35/3526fb457a523d7bcc34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **pruned_standard_25** 和 **pruned_rasp_25** 均存在且完整（config.json 确认）
- 无之前的部分 25% eval 结果
- `src/run_eval_25.sh` 已创建并通过语法检查
- 参数与 20% eval 一致：`--max_samples 100`、`--max_new_tokens 4096`、输出到 `results/` 目录
- 修正了任务描述中的 `--output_file` → `--output_path`

GPU 释放后执行：
```bash
bash src/run_eval_25.sh 1
```

---
