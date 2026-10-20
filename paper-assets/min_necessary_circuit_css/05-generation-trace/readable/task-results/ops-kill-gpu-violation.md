# ops kill gpu violation

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-gpu-violation_20260513T021204_result.json`
- **Structured JSON:** [`f3feb6dbbc2afc219b7a.json`](../../sessions/f3/f3feb6dbbc2afc219b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 处理报告

### 1. PID 897752 — 已杀死
SIGTERM 成功终止，未需要 SIGKILL。

### 2. cuda:0 — 已清理干净
`nvidia-smi` 确认 cuda:0 显存 0MiB，无任何进程残留。

### 3. 根因分析

**PID 897752 进程已终止，`/proc/897752/cmdline` 无法读取，且服务器无 git 历史，无法精确复原启动命令。** 但根据以下证据推断：

- `mvp_output.log`（最后修改 09:15）记录的是 `run_mvp.py`（IOI 任务），以 HuggingFace 连接错误结束
- `mvp_output_killed.log`（May 12 19:53）显示之前有一次被杀的 MVP 运行
- 当前所有入口脚本（`run_arithmetic.py`, `run_mvp.py`, `run_phase_d_only.py`, `run_circus_fix.py`, `eval_faithfulness.py`）均已有 `CUDA_VISIBLE_DEVICES="5"` 保护
- `run.sh` 也正确设置了 `export CUDA_VISIBLE_DEVICES=5`
- 但 `edge_pruning_l0.py` 和 `ifr_discovery.py` 作为库模块使用 torch 却无 CUDA 保护——如果被直接运行（而非通过入口脚本导入），会默认落到 cuda:0

**最可能的根因**：PID 897752 是在 CUDA_VISIBLE_DEVICES 保护加入代码**之前**启动的旧进程（可能是早期 `run_mvp.py` 运行），或者是某次直接 `python` 交互式启动了某个库模块，未经过入口脚本的 GPU 限制。

### 4. PID 900223（合法实验）状态
- 运行中：`python3 run_arithmetic.py`
- 位于 **cuda:5**，占用 2600MiB，69% 利用率
- 环境变量确认 `CUDA_VISIBLE_DEVICES=5` ✅
- 日志（`/tmp/arithmetic.log`）显示 `mvp_arithmetic_gpt2_k3` 实验正在正常推进

### 5. 防护措施

| 措施 | 状态 |
|------|------|
| `run_arithmetic.py` 文件开头 `os.environ["CUDA_VISIBLE_DEVICES"] = "5"` | ✅ 已存在（无需修改） |
| 所有其他入口脚本均有同样保护 | ✅ 已确认（5个文件 + run.sh） |
| 创建 `/root/min_necessary_circuit_css/gpu_guard.sh` 防护包装脚本 | ✅ 已创建，chmod +x |

**gpu_guard.sh 用法**：`./gpu_guard.sh python3 any_script.py`，确保任何脚本都被限制在 cuda:5。

---
