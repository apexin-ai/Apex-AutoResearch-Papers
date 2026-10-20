# code libero object resume

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_object_resume_20260521T002750_result.json`
- **Structured JSON:** [`1bcd344b1bbae2cd2201.json`](../../sessions/1b/1bcd344b1bbae2cd2201.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正式启动，配置正确：10 tasks × 10 demos × 50 timesteps × 15 seeds。

总结：
- **Checkpoint**: openvla-7b-finetuned-libero-object 已下载完成（16GB）
- **Data**: 10 个 LIBERO-Object hdf5 文件齐全
- **Script**: `libero_object_full_pipeline.py` 已修复 4 个问题：
  1. `global N_IMG_TOKENS` 声明位置（SyntaxError）
  2. `PrismaticProcessor` 加载（AutoProcessor 兼容性）
  3. pixel_values dtype 转 bfloat16
  4. 小样本 probing/classification 边界检查
- **新增 RSA 模块**: Phase 5，within-task Spearman(cosine_rep, euclidean_act)
- **Dry-run**: 6 个 phase 全部通过
- **正式实验**: `libero_object_full_pipeline` 已提交到 cuda:0，tmux session 运行中
- **输出**: `/root/autodl-tmp/vla-ssd/results/libero_object/` → 5 个 JSON + pipeline.log

---
