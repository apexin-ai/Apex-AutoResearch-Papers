# eval c1 s42 results and c1s137 eval

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_c1-s42-results-and-c1s137-eval_20260518T150444_result.json`
- **Structured JSON:** [`68c1b039db23d15b4369.json`](../../sessions/68/68c1b039db23d15b4369.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "All data collected. Here are the results:\n\n---\n\n## C1_s42 Eval 结果\n\n**P̄ = 7.69% (7/91)**\n\n| 指标 | 值 |\n|------|-----|\n| P̄ | 0.0769 |\n| A90 | 0.0 |\n| U10_90 | 0.353 |\n| 通过 | 7 / 91 |\n\n### Per-source 分布\n\n| 来源 | 总数 | 通过 | 通过率 |\n|------|------|------|--------|\n| sharded-HumanEval | 36 | 5 | 13.9% |\n| sharded-livecodebench | 55 | 2 | 3.6% |\n\n### 通过的 7 个 sample\n\n| task_id | turns | shards |\n|---------|-------|--------|\n| HumanEval/7 | 1 | 5 |\n| HumanEval/25 | 1 | 6 |\n| HumanEval/43 | 2 | 6 |\n| HumanEval/8 | 2 | 6 |\n| HumanEval/124 | 8 | 9 |\n| livecodebench/2727 | 5 | 10 |\n| livecodebench/2876 | 2 | 8 |\n\n通过的 sample 集中在 low-turn (1-2 turns) 的简单题。livecodebench 通过率远低于 HumanEval。\n\n---\n\n## GPU 状态\n\n**0MiB / 97,887MiB** — 完全空闲，足够启动 eval。\n\n---\n\n## C1_s137 Eval 命令\n\n已验证：checkpoint 存在，base model 路径正确，参数与 C1_s42 一致。注意 `run_eval.py` 没有 `--temperature` / `--seed` 参数，实际参数是 `--condition` 和 `--n_repeats`。\n\n```bash\ncd /root/tbab_multi_turn/eval && \\\nOPENROUTER_API_KEY=[REDACTED]"tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8\" \\\nOPENROUTER_BASE_URL=\"http://47.94.22.126/v1\" \\\npython3 run_eval.py \\\n  --model_path /root/tbab_multi_turn/checkpoints/c1_lora_only_seed137 \\\n  --base_model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.1 \\\n  --condition lora_only \\\n  --tasks code \\\n  --n_repeats 1 \\\n  --output_dir /root/tbab_multi_turn/eval/results/c1_s137_code_n1\n```\n\n没有 `submit_training_job` 工具可用。eval 预计耗时 ~2.5 小时（参考 C1_s42: 18:54→21:35）。ssh_execute 会超时，需要你决定如何提交。"
}

---
