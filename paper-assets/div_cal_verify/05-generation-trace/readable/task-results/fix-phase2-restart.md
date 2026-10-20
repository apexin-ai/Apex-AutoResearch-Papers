# fix phase2 restart

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_phase2_restart_20260513T034010_result.json`
- **Structured JSON:** [`57b7646e1a2aa6f99ccd.json`](../../sessions/57/57b7646e1a2aa6f99ccd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总结果：

---

## 执行结果

### 1. 进程 kill ✓
PID 138068/138072/138073/138083 全部终止，无残留进程。tmux session `phase2_3method_selfit` 已清除。

### 2. run_phase2.sh 修复 ✓
在 `set -e` 后插入两行：
```bash
source /root/div_cal_verify/env.sh
export TRANSFORMERS_OFFLINE=1
```

### 3. results_phase2/ 状态 ✓
残留的 `uncurated/` 目录已删除，目录现在为空。

### 4. GPU 状态 ✓
- GPU 0: RTX PRO 6000 Black, 49175MiB/97887MiB, 0% util（有其他占用）
- **GPU 1: RTX PRO 6000 Black, 0MiB/97887MiB, 0% util — 完全空闲，可用**

### 5. 启动命令
请用 `submit_training_job` 提交：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/div_cal_verify/run_phase2.sh 1"
```

---
