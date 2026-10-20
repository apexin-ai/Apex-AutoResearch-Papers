# eval cls8b s42 resume val sweep gpu1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-resume-val-sweep-gpu1_20260515T184643_result.json`
- **Structured JSON:** [`efd94a9340879eb684cf.json`](../../sessions/ef/efd94a9340879eb684cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **GPU 1 sweep 已启动**（exp_id: `cls8b-s42-resume-val-sweep-gpu1`，PID 405526）
- 评估范围：checkpoint 4000→5800（10 个，step=200）
- GPU 0 当前在 checkpoint-2200（3/21），将继续跑 1800→3800
- 两个 sweep 输出到同一目录 `/root/autodl-tmp/eval_results/cls_8b_s42_resume_val/`，按 step 子目录分开，不会冲突
- 参数完全一致：seq_length=8192, batch_size=1, val split (n=9335)
- Log: `~/runs/exec-sim-repair-verifier/cls8b-s42-resume-val-sweep-gpu1.log`

---
