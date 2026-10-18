# fix exp 007 use clean script v3

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp-007-use-clean-script-v3_20260519T174725_result.json`
- **Structured JSON:** [`ad6341d9e08ff4151f82.json`](../../sessions/ad/ad6341d9e08ff4151f82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 步骤 | 状态 |
|------|------|
| 清理 `lm_eval_clean/exp007/` | 已删除 |
| 确认 `run_lmeval_clean.py` 有 `allow_neg_eigval=True` | 确认（第44-46行） |
| 修改 `run_exp007_logsamples.sh` | 已改为调用 `run_lmeval_clean.py`，修正 skip 检查 pattern |
| Dry-run 340M GDN-pure | **acc=0.3753** （通过） |
| 提交批量任务 | tmux session `exp-007`, PID 530432, 日志 `~/runs/entrainment_gated_ft/exp-007.log` |

Dry-run 产生的 GDN-pure 输出已存在，批量脚本会自动跳过它。27个模型中 GDN-pure 340M 已完成，剩余 26 个将依次运行，预计 ~2h。

---
