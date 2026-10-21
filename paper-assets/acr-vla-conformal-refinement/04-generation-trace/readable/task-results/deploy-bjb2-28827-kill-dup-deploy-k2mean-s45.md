# deploy bjb2 28827 kill dup deploy k2mean s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-kill-dup-deploy-k2mean-s45_20260523T201852_result.json`
- **Structured JSON:** [`08093eda3dc0bac74dbe.json`](../../sessions/08/08093eda3dc0bac74dbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**1. Kill 确认 + GPU 释放**
- PID 849946 force killed，tmux session `eval-supp-long-vla-only-s43` 已清理
- cuda:4 释放至 1 MiB → 部署后占用 3304 MiB

**2. evaluate.py 文件名机制**
- 默认模板：`logs/eval_{benchmark}_{mode}{model_tag}{norm_tag}{adaptive_tag}_seed{seed}.json`
- K2mean 用 `--mode vla_only`，默认生成 `eval_long_vla_only_seed45.json`，与 VLA-only 完全相同
- 解决：evaluate.py L96 有 `--output_file` 参数，直接指定 `logs/eval_long_k2mean_seed45.json`

**3. 实际部署命令**
```
CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
  --benchmark long --mode vla_only --baseline_mode mean --K 2 \
  --seed 45 --n_rollouts 20 \
  --output_file logs/eval_long_k2mean_seed45.json
```

**4. 新进程**
- PID: 924226，tmux session: `eval-long-k2mean-s45`
- 模型加载完成，LIBERO long 环境初始化中

**5. Registry**
- `eval-supp-long-vla-only-s43`: status=DONE, conclusion=killed
- `eval-supp-long-k2mean-s45`: status=RUNNING, spec 已填充

---
