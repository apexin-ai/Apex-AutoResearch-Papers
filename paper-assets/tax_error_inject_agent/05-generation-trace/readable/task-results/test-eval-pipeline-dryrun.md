# test eval pipeline dryrun

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_test_eval-pipeline-dryrun_20260514T111730_result.json`
- **Structured JSON:** [`dd47eb488e9a2c4ea495.json`](../../sessions/dd/dd47eb488e9a2c4ea495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练在跑但还没保存 checkpoint。脚本 ready，训练完成后有 checkpoint 就能自动找到。

---

## 总结

### 1. Eval 流程：**PASS**
- Base Qwen3-8B 在 cuda:3 上跑 3 个 episode 完全通畅
- 模型加载 ~2.5s，每个 episode 1-3 分钟（取决于步数）
- 结果：2/3 OK, success_rate=0.667

### 2. Adapter 加载：**PASS**
- LoRA checkpoint (`mini_taxei_sft/checkpoint-195`) 加载 + `merge_and_unload` 正常
- 推理输出正常，无报错（`libnvJitLink.so.13` warning 无影响）
- 结果：1/2 OK, success_rate=0.5

### 3. Metrics JSON 格式
```json
{
  "model": "...", "eval_split": "valid_unseen", "inject": false,
  "total_episodes": 3, "success_rate": 0.667, "timestamp": "...",
  "by_task_type": { "look_at_obj_in_light": {"total": 3, "success": 2, "rate": 0.667} },
  "episodes": [
    {"task_name": "...", "task_type": "...", "success": true/false, "steps": N, "injected": false, "operator": "none"},
    ...
  ]
}
```
- `episodes[].success` 是 bool，直接可做 McNemar 检验的逐任务二元结果

### 4. Eval 启动脚本
`/root/autodl-tmp/tax_error_inject_agent/scripts/run_v3_eval.sh`

用法：
- `bash scripts/run_v3_eval.sh clean` — 仅 clean eval（3 组并行 cuda:0/1/2）
- `bash scripts/run_v3_eval.sh inject` — 仅 injection eval
- `bash scripts/run_v3_eval.sh both` — 先 clean 再 inject（默认）
- 自动找最新 v3 checkpoint，找不到则报错退出
- 日志写入 `/tmp/eval_v3_*.log`，结果写入 `eval_results/v3_*.json`

**预计 47 tasks 全量 eval 每组 ~90-120 分钟。3 组并行同时完成。**

---
