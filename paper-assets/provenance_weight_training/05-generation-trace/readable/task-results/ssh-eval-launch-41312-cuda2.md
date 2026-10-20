# ssh eval launch 41312 cuda2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_launch_41312_cuda2_20260517T202948_result.json`
- **Structured JSON:** [`2711cb53a06890d3b536.json`](../../sessions/27/2711cb53a06890d3b536.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Wait-and-eval script launched as PID 131262. It will poll every 60s for training completion, then auto-run `eval_perplexity.py` on the final checkpoint.

## 汇报

### ess_only_seed123 状态
- **仍在训练**：step 2499/6103 (~41%)，预计还需 ~7 小时
- **已部署自动 eval 脚本**：PID 131262 在后台等待训练完成后自动执行 `eval_perplexity.py`，结果写入 `/root/autodl-tmp/provenance_weight_training/output/eval_ess_only_seed123.log`

### lm-eval (uniform_seed42) 状态
- **旧 `uniform_seed42`**：仅训到 step 799/6103（~13%），是中断的不完整 run，checkpoint 最高到 600，不可用
- **`qwen06b_uniform_seed42_v2`**：当前在 cuda:0 训练中，step ~3799/6103（~62%），尚未完成
- **结论：uniform_seed42 checkpoint 未就绪**。v2 在 cuda:0 上还需 ~3-4 小时完成。cuda:2 释放后（~7h），v2 应已完成，届时可用 v2 的 final checkpoint 跑 lm-eval

### 建议的后续操作
训练完成后检查 eval log：
```bash
cat /root/autodl-tmp/provenance_weight_training/output/eval_ess_only_seed123.log
```

---
