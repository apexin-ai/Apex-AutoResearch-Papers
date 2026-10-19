# diagnose eval perdof object norm03 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-perdof-object-norm03-seed44-r2_20260517T115319_result.json`
- **Structured JSON:** [`01926eb3c56f78e929ab.json`](../../sessions/01/01926eb3c56f78e929ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总全部证据：

**实验 `eval-perdof-object-norm03-seed44-r2` 确认为真正失败。**

证据链：
1. **输出文件不存在** — `eval_object_perdof_norm03_seed44_r2.json` 在 `/root/acr-vla-conformal-refinement/logs/` 和 `/root/autodl-tmp/` 下均不存在
2. **无运行日志** — `~/runs/` 目录下无对应 tmux 日志，无 exit sentinel (`/tmp/agent-ml-exit/`)，无 `nohup.out`
3. **无 tmux session** — 当前只有 `eval-dc-r2` 和 `eval-perdof-object-norm01-seed46` 两个 session
4. **PID 421086 已退出**，EXIT_CODE=129 (SIGHUP)
5. **存在的非 `_r2` 日志 `eval_object_perdof_norm03_seed44.log`** 是另一个独立实验（args 显示 `output_file` 不含 `_r2`），仅跑了 task 1 的 4/10 rollouts 就停止，也未完成
6. 非 `_r2` 实验同样没有输出 JSON（`eval_object_perdof_norm03_seed44.json` 不存在）

根因：实验以 nohup 启动但未正确设置日志重定向，进程收到 SIGHUP (信号1) 被杀。28 分钟的运行时间不足以完成 10 tasks × 10 rollouts。stdout/stderr 因缺少重定向而丢失。

```json
{"status": "truly_failed", "evidence": "输出文件 eval_object_perdof_norm03_seed44_r2.json 不存在；无日志/sentinel/tmux session；EXIT_CODE=129 (SIGHUP)；非 _r2 日志显示同参数实验也只跑了 4/100 rollouts 即终止", "metrics": null, "root_cause": "nohup 进程收到 SIGHUP 被杀，未设置日志重定向导致输出丢失。同参数的非 _r2 实验也未完成，可能存在环境/资源竞争问题", "fix_steps": ["用 tmux session 或显式日志重定向重新启动实验", "确保 GPU 0 无冲突进程", "命令示例: cd /root/acr-vla-conformal-refinement && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44_r2.json' > logs/eval_object_perdof_norm03_seed44_r2.log 2>&1 &"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "truly_failed",
    "evidence": "输出文件 eval_object_perdof_norm03_seed44_r2.json 不存在；无日志/sentinel/tmux session；EXIT_CODE=129 (SIGHUP)；非 _r2 日志显示同参数实验也只跑了 4/100 rollouts 即终止",
    "metrics": null,
    "root_cause": "nohup 进程收到 SIGHUP 被杀，未设置日志重定向导致输出丢失。同参数的非 _r2 实验也未完成，可能存在环境/资源竞争问题",
    "fix_steps": [
      "用 tmux session 或显式日志重定向重新启动实验",
      "确保 GPU 0 无冲突进程",
      "命令示例: cd /root/acr-vla-conformal-refinement && nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44_r2.json' > logs/eval_object_perdof_norm03_seed44_r2.log 2>&1 &"
    ]
  }
}
```

</details>

---
