# ssh olmo temp09 001 check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_olmo_temp09_001_check_20260514T225434_result.json`
- **Structured JSON:** [`fbb40c614af37ab39e34.json`](../../sessions/fb/fbb40c614af37ab39e34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## olmo_temp09_001 实验结果

**状态：FAILED**

| Step | 内容 | 状态 |
|------|------|------|
| 1 | LoRA finetune depth-0 | ✅ 完成, final loss=2.2684, 939/939 steps |
| 2 | Generate depth-1 | ✅ 完成, 5000 samples |
| 3 | LoRA finetune depth-1 | ❌ 在 ~626/939 步 (67%) 被 kill |
| 4-7 | depth-2/3 生成 + 特征提取 + 分类 | 未执行 |

**失败原因：** 进程在 Step 3 finetune 中途被 kill，日志无 traceback/error，大概率是 AutoDL 实例关机或 OOM。日志最后修改时间 06:56 CST，pipeline 启动于 06:23，总运行 ~33 分钟。

**残留产出：**
- `data/olmo_temp09/depth_0.jsonl` (symlink) + `depth_1.jsonl` (5000 lines)
- `checkpoints/olmo_temp09/lora_depth_0/` (完整) + `lora_depth_1/checkpoint-626` (中间 checkpoint)

需要重跑 pipeline，可以考虑从 Step 3 断点恢复（利用已有的 depth_1.jsonl 和 lora_depth_0）。

---
