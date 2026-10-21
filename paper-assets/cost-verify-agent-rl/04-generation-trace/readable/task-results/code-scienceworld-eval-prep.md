# code scienceworld eval prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld-eval-prep_20260519T151636_result.json`
- **Structured JSON:** [`63cab823f3edc21d99ec.json`](../../sessions/63/63cab823f3edc21d99ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本验证通过。总结：

**已完成：**
1. **依赖安装** — bjb1 上安装了 `scienceworld==1.2.3`、`py4j`、`openjdk-11`
2. **创建 `eval_scienceworld.py`** — 位于 `/root/cost-verify-agent-rl/eval_scienceworld.py`
3. **Dry-run 通过** — base model 跑 1 个 boil episode（10 步，0% success 符合预期）

**脚本功能：**
- 基于 vLLM 推理，user turn 格式完全匹配 SFT 训练数据
- 30 个 task type 的 per-task-type breakdown
- 支持 `--temperature`（0.0/0.4）、`--eval_split`（dev/test）、`--task_names`（指定 task）
- 输出 JSON 含 success_rate、avg_score、valid_action_rate、format_rate

**用法示例（SFT 训练完成后）：**
```bash
# 先把 westd checkpoint 传到 bjb1，然后：
CUDA_VISIBLE_DEVICES=0,1 python3 eval_scienceworld.py \
  --checkpoint /path/to/scienceworld_sft_hf \
  --temperature 0.0 \
  --eval_split dev \
  --output /tmp/sw_sft_eval_t0.json
```

**待确认：** westd SFT 训练完成后，checkpoint 在 `/root/autodl-tmp/checkpoints/scienceworld_sft` 下（包含 `hf_model` 子目录），需 scp 到 bjb1。

---
