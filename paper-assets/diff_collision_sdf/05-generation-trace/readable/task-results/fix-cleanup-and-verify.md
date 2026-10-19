# fix cleanup and verify

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cleanup_and_verify_20260527T201257_result.json`
- **Structured JSON:** [`14fb20ebcd97de0f2bec.json`](../../sessions/14/14fb20ebcd97de0f2bec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务结果汇报：

---

### 任务 1：旧 checkpoint 重命名 — ✅ 完成

`a1_sdf_pi05_object_pudding_seed2_l01` → `a1_sdf_pi05_object_pudding_seed2_l01_OLD`

- PID 425058 仍在运行（seed2 lambda=0.1, 30K steps），确认其对该目录无任何打开的文件句柄（`lsof` 验证）
- 旧目录内容：`30000/model.safetensors`（7.5GB, May 26 16:40），来自前一次训练
- 新训练完成后会自动创建新的 `seed2_l01/` 目录

---

### 任务 2：per-task fingerprint 图 — ⚠️ PNG 正确，PDF 缺失

图文件位置：本地 `artifacts/fig_pertask_car_fingerprint.png`

**数据验证通过：**
- LoRA-only 使用了 3-seed 数据：s0={CP:74, Milk:66, OJ:68, BBQ:20}, s1={CP:68, Milk:72, OJ:54, BBQ:16}, s2={CP:76, Milk:62, OJ:56, BBQ:26} ✅
- LoRA-only bar 上显示 3 个 seed dots ✅
- 脚注写的是 "LoRA-only: 3-seed mean (dots = seeds)" ✅
- s2 数据匹配预期值（OJ=56, CP=76, Milk=62, BBQ=26）✅

**问题：PDF 不存在。** 脚本 (`fig_pertask_car_fingerprint.py`) 输出路径为 `/root/autodl-tmp/artifacts/`，该目录在 westd-45947 上不存在，两台服务器和本地均未找到 PDF 版本。

---

### 任务 3：appendix per-task table — ❌ appendix.tex 尚未创建

- 两台服务器和本地均无 `appendix.tex` 文件
- `fig_pertask_car_fingerprint.py` 第 23 行引用了 "Table 8 (appendix.tex, tab:per_task_car)"，但该表格/文件从未被创建
- 现有 `experiments.tex` 全是 TODO 占位符，无实际数据
- `reeval_comparison.tex` 仅包含旧的 2-seed LoRA 数据（s0, s1），无 s2 行
- LoRA s2 的 per-task CAR 数据存在于图生成脚本中，但尚未写入任何 tex 表格

---
