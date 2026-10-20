# code recovery eval dev

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery-eval-dev_20260514T173802_result.json`
- **Structured JSON:** [`6dac57dd929d3e21139d.json`](../../sessions/6d/6dac57dd929d3e21139d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

**`eval/injected_eval.py`** (463 行) — Injected Recovery Evaluation 脚本
- 在 eval 时注入错误 action：在指定步骤替换模型的 action 为随机错误 action，发送给环境
- 根据 `--model_variant` 插入训练格式匹配的 error tag：
  - taxei → `[Error Type: P1_StepOrderSwap]` 等
  - random → `[Error occurred]`
  - vanilla → 无标签
- 输出 JSON：per-task recovery 结果 + aggregate recovery_rate / by_operator / by_task_type
- 内置 `--compare_with` 统计检验（McNemar + bootstrap CI）

**`scripts/run_injected_eval.sh`** — 3 个变体的启动脚本
- `bash scripts/run_injected_eval.sh all` 并行跑 3 个模型 + 自动对比
- 支持单独跑 `taxei`/`random`/`vanilla`/`compare`

**Dry-run 验证通过**: Vanilla checkpoint, 1 task, cuda:3 — 注入 `take bowl 1 from desk 1`（原本 `go to desk 2`），模型 13 步 RECOVERED。

---
