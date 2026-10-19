# prep plan a eval commands

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan-a-eval-commands_20260521T173642_result.json`
- **Structured JSON:** [`33783dede456df9fefe1.json`](../../sessions/33/33783dede456df9fefe1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**验证结果**：
- eval 脚本是 `src/evaluate.py`（非 `eval_crm.py`），三台服务器均存在
- `--mode acr_vla` 确认可用（= crm_perdof 别名）
- π0.5 必须传 `--model pi05 --obs_dim 2048`（脚本有 ValueError 校验）
- 无 `--cache_dir` 参数

**6 个命令已写入** artifact `pi05_eval_commands.md`，唯一占位符 `&lt;CRM_CKPT>` 待 CRM training 完成后替换。

**部署前注意 3 件事**：
1. bjb2-28827 的 evaluate.py 版本旧（30140 vs 33058 bytes），必须先 `git pull`
2. CRM checkpoint 可能需要 rsync 到 bjb1-32546 和 bjb2-28827
3. 确认 `/root/autodl-tmp/models/pi05_libero_finetuned/` 在各服务器存在

---
