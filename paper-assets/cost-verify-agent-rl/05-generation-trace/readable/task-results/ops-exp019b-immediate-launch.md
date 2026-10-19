# ops exp019b immediate launch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp019b-immediate-launch_20260514T201913_result.json`
- **Structured JSON:** [`6e4fa48e51ca33e19798.json`](../../sessions/6e/6e4fa48e51ca33e19798.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认脚本在处理完全部 3553 个 game 后才写 jsonl。以下是状态报告：

---

## 状态报告

### 1. 进程状态：**运行中（即将完成）**
- PID 368343, `augment_admissible_v2.py`, 已运行 3h14m
- 进度 **3500/3553**（98.5%），剩余 53 个 game
- 预计 5-10 分钟内完成

### 2. 数据文件：**尚未生成**
- `/root/autodl-tmp/expert_sft_v3/` 目录已创建但为空
- 脚本逻辑：**处理完所有 game 后一次性写入** train/val jsonl
- 预期产出：~2669 条有效 SFT 样本（当前 valid_sft=2669），95/5 split → ~2536 train / ~133 val

### 3. 数据质量（从日志推断）
- `ok`: 3154, `too_long`: 250, `not_won`: 346, `invalid_action`: 235
- **move actions: 2948, admissible_move: 8487** ✓
- put actions: 0, admissible_put: 0（符合预期，v3 只处理 move 类任务）

### 4. 训练脚本：**就绪**
- 路径: `/root/cost-verify-agent-rl/scripts/run_exp019b.sh` ✓
- 入口点: `scripts/sft_train_v2.py` ✓（文件存在）
- 配置: `lr=5e-6, epochs=2, batch=4, grad_accum=4, max_seq=4096, CUDA_VISIBLE_DEVICES=0`
- Base checkpoint: `exp008_sft/final/model.safetensors` ✓

### 5. GPU 状态：**完全空闲**
- GPU 0: 0 MiB, 0% utilization
- GPU 1: 0 MiB, 0% utilization

### 6. 磁盘：165GB 可用（35% used）✓

### 结论：**不可立即启动，预计 5-10 分钟后就绪**

数据收集进程即将完成。文件写入后需要验证数据格式（admissible/move 字段），然后可通过 `run_exp019b.sh` 启动训练。建议等进程结束后再检查一次确认 jsonl 已生成。

---
