# diagnose 1 7b rsft failures

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_1_7b_rsft_failures_20260519T035424_result.json`
- **Structured JSON:** [`0e240f1ca889130fc3fe.json`](../../sessions/0e/0e240f1ca889130fc3fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。GPU 1 和 GPU 2 空闲，可以并行提交两个训练。

```json
{
  "root_cause": "两个独立问题：(1) RSFT 脚本的 --sft_adapter 路径都指向 s42 的 SFT adapter (/root/autodl-tmp/sft_output_qwen3_1_7b_bf16)，而非各自的 seed-specific adapter (seed43/seed44)。训练实际完成但结果科学上无效。(2) 监控误报：WANDB_API_KEY 未设置导致 W&B 未上报，rsft_trainer.py 也无 sentinel file，监控系统检测到进程结束但无成功标志，自动标记失败。",
  "error_type": "data",
  "fix_applied": "修正 train_1_7b_s43.sh 的 --sft_adapter 为 sft_output_qwen3_1_7b_bf16_seed43，train_1_7b_s44.sh 的 --sft_adapter 为 sft_output_qwen3_1_7b_bf16_seed44。删除了无效输出目录。",
  "fix_steps": [
    "sed 修复 s43 脚本 sft_adapter 路径 → sft_output_qwen3_1_7b_bf16_seed43",
    "sed 修复 s44 脚本 sft_adapter 路径 → sft_output_qwen3_1_7b_bf16_seed44",
    "rm -rf 删除两个无效输出目录",
    "dry-run 验证 import 正常",
    "确认两个 seed-specific SFT adapter 文件完整（278MB）",
    "确认 RSFT 训练数据存在（3021 行）"
  ],
  "ready_to_resubmit": true,
  "resubmit_commands": {
    "s43": "CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/freige/scripts/seed_expansion/train_1_7b_s43.sh",
    "s44": "CUDA_VISIBLE_DEVICES=2 bash /root/autodl-tmp/freige/scripts/seed_expansion/train_1_7b_s44.sh"
  },
  "gpu_status": "GPU 1 (0 MiB used), GPU 2 (0 MiB used) 均空闲可用"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "两个独立问题：(1) RSFT 脚本的 --sft_adapter 路径都指向 s42 的 SFT adapter (/root/autodl-tmp/sft_output_qwen3_1_7b_bf16)，而非各自的 seed-specific adapter (seed43/seed44)。训练实际完成但结果科学上无效。(2) 监控误报：WANDB_API_KEY 未设置导致 W&B 未上报，rsft_trainer.py 也无 sentinel file，监控系统检测到进程结束但无成功标志，自动标记失败。",
    "error_type": "data",
    "fix_applied": "修正 train_1_7b_s43.sh 的 --sft_adapter 为 sft_output_qwen3_1_7b_bf16_seed43，train_1_7b_s44.sh 的 --sft_adapter 为 sft_output_qwen3_1_7b_bf16_seed44。删除了无效输出目录。",
    "fix_steps": [
      "sed 修复 s43 脚本 sft_adapter 路径 → sft_output_qwen3_1_7b_bf16_seed43",
      "sed 修复 s44 脚本 sft_adapter 路径 → sft_output_qwen3_1_7b_bf16_seed44",
      "rm -rf 删除两个无效输出目录",
      "dry-run 验证 import 正常",
      "确认两个 seed-specific SFT adapter 文件完整（278MB）",
      "确认 RSFT 训练数据存在（3021 行）"
    ],
    "ready_to_resubmit": true,
    "resubmit_commands": {
      "s43": "CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/freige/scripts/seed_expansion/train_1_7b_s43.sh",
      "s44": "CUDA_VISIBLE_DEVICES=2 bash /root/autodl-tmp/freige/scripts/seed_expansion/train_1_7b_s44.sh"
    },
    "gpu_status": "GPU 1 (0 MiB used), GPU 2 (0 MiB used) 均空闲可用"
  }
}
```

</details>

---
