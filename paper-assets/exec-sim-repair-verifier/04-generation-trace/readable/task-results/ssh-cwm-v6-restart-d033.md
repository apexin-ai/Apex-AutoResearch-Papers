# ssh cwm v6 restart d033

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-v6-restart-d033_20260512T203346_result.json`
- **Structured JSON:** [`8bd3c033172753591665.json`](../../sessions/8b/8bd3c033172753591665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 旧进程 kill
PID 84887 已成功终止。

### 2. train_repo_cwm.py 参数检查与修改
文件中原有参数：
- `eval_strategy`: "steps" ✓
- `save_strategy`: "steps" ✓
- `save_steps`: 500 ✓
- `save_total_limit`: 3 ✓
- **`eval_steps`: 缺失** — 未显式设置，fallback 到 `logging_steps=50`，这就是 eval 每 50 步触发的根因

**修复**：在第 266 行添加了 `"eval_steps": 500`。

### 3. 命令行覆盖检查
- `/root/.bash_history` 不存在
- tmux capture-pane 不可用（旧 session 已被 kill）
- 无发现命令行覆盖参数

### 4. 新 PID
- Python 进程 PID: **89516**
- tmux wrapper PID: 89511
- GPU: cuda:2, 显存占用 8429 MiB

### 5. Step 50 eval 验证 — 成功
- `grep -i eval` 在完整日志中**零匹配**
- 日志显示 step 50 → 51 直接过渡，无 "Running evaluation" 或 eval_loss 输出
- **确认 eval_steps=500 修复生效**

### 6. Loss 趋势
由于 stdout 被重定向到文件时 `\r` 覆盖机制，HuggingFace Trainer 的 loss 日志值（在 logging_steps=50 时输出）被 tqdm 进度条重绘覆盖，无法从文件中提取单独的 loss 数值。训练速度稳定在 ~8s/step，ETA ~14h50m（对比旧配置 42h 大幅改善），step 55+ 正常推进。

---
