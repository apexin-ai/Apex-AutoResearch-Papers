# code grpo v2 eval pipeline

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_v2_eval_pipeline_20260513T063837_result.json`
- **Structured JSON:** [`229c784b5eb79b395f4e.json`](../../sessions/22/229c784b5eb79b395f4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建成功，语法检查通过。

**使用方式：**

```bash
cd /root/autodl-tmp/prov_grounded_uie

# 中期 eval（step 50 checkpoint）
bash eval_grpo_v2.sh ./outputs/grpo_v2/checkpoint-50 grpo_v2_step50

# 最终 eval
bash eval_grpo_v2.sh ./outputs/grpo_v2 grpo_v2_final
```

脚本流程：merge LoRA（CPU 上合并，不占 GPU 显存） → `CUDA_VISIBLE_DEVICES=0` 运行 evaluate.py → 打印结果 JSON。每步有时间戳，`set -e` 确保任何步骤失败立即退出。输出目录自动创建在 `./outputs/&lt;output_name>/`。

---
