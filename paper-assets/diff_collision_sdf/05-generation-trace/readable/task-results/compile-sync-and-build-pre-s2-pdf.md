# compile sync and build pre s2 pdf

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compile_sync_and_build_pre_s2_pdf_20260528T013407_result.json`
- **Structured JSON:** [`cbda65afab8119ee202b.json`](../../sessions/cb/cbda65afab8119ee202b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

### 编译状态
- **成功**，本地编译（远程无 pdflatex）
- **16 页，576 KB**
- 无未解析引用，无 fatal errors
- PDF 位置：本地 `docs/paper/main.pdf`，已上传到 `westd-45947:/root/colliforce-vla/docs/paper/main.pdf`

### paper_switch.py --verify
- **23/23 通过**（Scenario B: 11/11, Scenario C: 12/12）

### 本地 vs 远程 appendix.tex 差异摘要

**远程旧版**（254 行）结构完全不同：
- 以 `\appendix` 开头
- 独立的 per-condition CAR 表（tab:pertask_lora, tab:pertask_l005, tab:pertask_l01）
- 独立的 baseline 表（tab:pertask_baseline）
- 独立的 null distribution 表（tab:null_dist）
- 额外 sections：SDF Ground Truth Pipeline, Training Hyperparameters, Evaluation Protocol and Metrics
- 缺少：Displacement Distribution/Threshold sections, Per-Task TSR 表, Per-Task CAR consolidated 表, SSR 表, Oracle Analysis, Oracle Details

**本地新版**（270 行）包含所有 3 项修改：
1. LoRA s0 CAR 级联修正（dfCAR 56.5, SSR 54.67, null 54.58）
2. Per-task TSR 表（tab:per_task_tsr）— 3-seed mean
3. Baseline per-task TSR 71.5%（reeval 替代旧 74.7%）

### 同步操作
- 用 scp 将本地 appendix.tex 覆盖远程文件（旧版结构已被新版替换）
- abstract.tex, claim3.tex, discussion.tex **未动**（远程版是 paper_switch.py 期望的 pre-switch 状态，与本地有微小差异属正常）

### 注意
- 远程路径是 `/root/colliforce-vla/docs/paper/`，**不是** `paper/sections/`（之前的 Worker 报告路径有误）
- westd-35807 上没有任何 .tex 文件，paper 仅在 westd-45947 上

---
