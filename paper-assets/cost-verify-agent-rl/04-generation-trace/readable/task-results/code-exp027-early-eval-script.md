# code exp027 early eval script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp027_early_eval_script_20260515T151920_result.json`
- **Structured JSON:** [`88cefbe5f69265a76280.json`](../../sessions/88/88cefbe5f69265a76280.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No checkpoints yet (empty dir). Both scripts validated:

**脚本路径:**
- Wrapper: `/root/cost-verify-agent-rl/scripts/eval_checkpoint.sh`
- Python: `/root/cost-verify-agent-rl/scripts/eval_checkpoint.py`（已修复 3 个问题）

**使用方法:**
```bash
bash scripts/eval_checkpoint.sh /root/autodl-tmp/checkpoints/exp027/global_step_5
# 或指定 GPU:
bash scripts/eval_checkpoint.sh /root/autodl-tmp/checkpoints/exp027/global_step_5 1
```

**对 .py 的修复:**
1. `ALFWORLD_DATA`: `~/.cache/alfworld` → `setdefault("/root/autodl-tmp/alfworld")`
2. `gpu_memory_utilization`: 0.85 → 0.35
3. `max_model_len`: 32768 → 8192

**Dry-run 结果:** shell 语法检查 OK，Python `--help` 正常输出。

**GPU 共享方案:** 训练用 vLLM `gpu_memory_utilization=0.4`（~38GB/GPU），eval 用 0.35（~33GB）。单 GPU 总计 71GB < 96GB（RTX PRO 6000），理论上可并行。如果 OOM，需等训练 val 间隙（每 5 step 有一次 val phase）再跑。

**当前状态:** exp027 checkpoint 目录为空，step 5 checkpoint 尚未生成。

---
