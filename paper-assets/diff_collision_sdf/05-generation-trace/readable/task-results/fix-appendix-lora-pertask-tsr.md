# fix appendix lora pertask tsr

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_appendix_lora_pertask_tsr_20260528T011106_result.json`
- **Structured JSON:** [`806423d84bc3f32a9b3b.json`](../../sessions/80/806423d84bc3f32a9b3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

远程 appendix.tex 没有 `tab:per_task_tsr` 表——远程文件结构不同（使用的是按条件拆分的 CAR 表，没有合并的 per-task TSR 表）。

**本地修改已完成**，5 处变更全部正确：
1. Caption: "LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol)"
2. 表头: `LoRA-only` (无 dagger)，`(3 seeds)`
3. 数据: OJ=30.0, CP=70.7, Milk=44.7, BBQ=60.7
4. Mean: 51.5
5. 脚注已删除

**远程文件无需修改** — westd-45947 的 `/root/colliforce-vla/docs/paper/appendix.tex` 没有 `tab:per_task_tsr` 表，结构与本地不同。远程文件的 appendix 仅包含按条件拆分的 per-task CAR 表和 baseline 表，不存在需要更新的 per-task TSR 表。

需要我把本地版本的 per-task TSR 表同步到远程文件吗？

---
