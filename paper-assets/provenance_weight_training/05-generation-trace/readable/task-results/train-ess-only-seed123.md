# train ess only seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ess_only_seed123_20260517T150800_result.json`
- **Structured JSON:** [`d8e385b85bbd876e7363.json`](../../sessions/d8/d8e385b85bbd876e7363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练任务已成功提交，正在等待 cuda:1 上的 lm_eval（HellaSwag）完成释放显存后自动启动。

总结：
- **已创建** `scripts/run_ess_only_seed123.sh` 和 `scripts/run_ess_only_seed456.sh`
- **已提交** `ess_only_seed123` 到 westd-41312 cuda:1（tmux session: `ess_only_seed123`）
- 参数：`--weighting_method ess_only`，`--n_min 2`，`--seed 123`，`--save_steps 200`，`--num_train_tokens 200000000`（= 6103 steps）
- 脚本内置了 GPU 等待逻辑，lm_eval 结束后自动开始训练
- seed456 脚本已就绪，本次未提交

---
