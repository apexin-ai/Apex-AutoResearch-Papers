# check cka script verify

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cka_script_verify_20260525T144509_result.json`
- **Structured JSON:** [`00663ef2eae1d58425e5.json`](../../sessions/00/00663ef2eae1d58425e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果汇总：

### 1. run_command.sh — 存在且完整
- 激活 `conda activate occsafe` 环境
- checkpoint 搜索模式：`${CKPT_DIR}/*50000_chkpt`，其中 `CKPT_DIR` = `/root/autodl-tmp/checkpoints/ablation_occ_detach_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3`
- 使用 `CUDA_VISIBLE_DEVICES=3`，`--gpu 0`
- 输出到 `/root/autodl-tmp/analysis/cka_s3_verification/`

### 2. cka_analysis.py — JSON summary 确认
- L8: `import json`
- L216: 构建 `cka_results["summary"]`
- L227: 写入 `cka_results.json`
- L229: `json.dump(cka_results, f, indent=2)`

输出格式正确。

### 3. checkpoint 路径匹配
当前 s3 checkpoint 目录下有：
- 训练中目录（无 `_chkpt` 后缀）
- `10000_chkpt`（已保存）

50K checkpoint 保存后文件名将是 `...--50000_chkpt`，与 `run_command.sh` 中 `*50000_chkpt` glob 模式**匹配**。无需修改。

### 4. pretrained baseline 模型
`/root/autodl-tmp/models/openvla-7b/` 存在，包含完整模型文件（3 个 safetensors 分片 + tokenizer + config）。

### 结论
脚本有效，路径全部匹配，无需修改。s3 训练到 50K step 后直接执行 `bash /root/autodl-tmp/analysis/cka_s3_verification/run_command.sh` 即可。

---
