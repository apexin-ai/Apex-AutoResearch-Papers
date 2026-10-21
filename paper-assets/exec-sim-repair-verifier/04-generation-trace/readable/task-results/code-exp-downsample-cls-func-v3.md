# code exp downsample cls func v3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-downsample-cls-func-v3_20260519T040349_result.json`
- **Structured JSON:** [`95e7e501632784e192d5.json`](../../sessions/95/95e7e501632784e192d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**v2 失败根因**：wandb 启动时进入 online 模式但未配置 API key
```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
EXIT_CODE=1
```
失败点：`trainer.train()` → `on_train_begin` → `wandb.init()` → `_find_or_prompt_for_key`。/root/.netrc 不存在，环境无 WANDB_API_KEY。

**修复方法**：`submit_training_job` 框架自动注入环境变量。v3 进程 `/proc/796729/environ` 显示：
```
HF_HUB_OFFLINE=1
WANDB_MODE=offline    ← 修复关键
CUDA_VISIBLE_DEVICES=1
```

**当前状态**：v3 已在运行（无需重新提交）
- tmux session: `exp-downsample-cls-func-v3`（12:05:35 启动）
- PID 796729 on GPU 1（cuda:1, 16.8 GB）
- 进度：step 36/756 @ 3.35s/iter，预计总时长 ~42 min
- 数据校验：train 8051 行（10 条 prompt 超长被丢弃，保留 8041），val 1896 行 ✓
- log: `/root/runs/exec-sim-repair-verifier/exp-downsample-cls-func-v3.log`

**Registry**：已更新 `exp-downsample-cls-func-v3.notes` 记录诊断与修复细节。

**GPU 1 占用情况**：v3 自身占用（PID 796729）。其他 GPU：0=cwm-8b eval（778334），2=deepseek-cwm eval（734440），3=deepseek-cwm-s123 eval（668680，已运行 1d10h）。

---
