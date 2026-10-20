# ssh verify gate3 script

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-gate3-script_20260514T162618_result.json`
- **Structured JSON:** [`2ee3f744a5393fe9bb91.json`](../../sessions/2e/2ee3f744a5393fe9bb91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

### 结论

**analyze_gate3.py 与 v4 eval 输出格式完全兼容，无需修复。**

- v4_vanilla_eval.json 的结构（`episodes` 数组，含 `task_name`/`success`/`task_type` 字段）与脚本 `build_outcome_vectors()` 和 `per_task_type_breakdown()` 的期望完全一致
- Self-test 运行成功：diff=0.0pp, p=1.0, discordant=0，符合预期
- `run_v4_eval.sh` 中 taxei/random eval 的输出路径已确认为 `eval_results/v4_taxei_eval.json` 和 `eval_results/v4_random_eval.json`
- 依赖（scipy）已安装

### eval 完成后直接执行：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/tax_error_inject_agent && \
python3 scripts/analyze_gate3.py \
  --vanilla eval_results/v4_vanilla_eval.json \
  --taxei eval_results/v4_taxei_eval.json \
  --random eval_results/v4_random_eval.json
```

---
