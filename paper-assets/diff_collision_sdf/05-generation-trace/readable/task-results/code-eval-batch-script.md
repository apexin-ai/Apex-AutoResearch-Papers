# code eval batch script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_batch_script_20260520T120802_result.json`
- **Structured JSON:** [`2caa1e877bb1655184f9.json`](../../sessions/2c/2caa1e877bb1655184f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。`/root/colliforce-vla/scripts/eval_batch.sh`：

- **三层循环** method × scene × seed，自动推导 checkpoint 路径（取最大数值 step 子目录）
- **method 映射**：baseline → `--model_type baseline`，a1 → `--model_type a1 --sdf_checkpoint ...`，a3 → `--model_type a3 --sdf_gt_path ...`，a3_no_refine → `--model_type a3 --no_refine`
- **scene 映射**：spatial_* → safelibero_spatial + Level II，object_* → safelibero_object + Level I
- **结果提取**：从 eval 输出 JSON 解析 TSR/CAR/ETS/avg_smoothness，追加到 CSV
- **额外支持**：`--step` 指定 step、`--dry_run` 只打印命令不执行
- dry run 验证路径推导正确：baseline 取到 step 12000，a1 取到 8000 并带 sdf_decoder.pt

---
