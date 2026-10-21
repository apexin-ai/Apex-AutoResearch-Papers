# ops exp025b add preflight

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025b_add_preflight_20260515T074020_result.json`
- **Structured JSON:** [`9dd3f4852cace1daf5e8.json`](../../sessions/9d/9dd3f4852cace1daf5e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。修改前后对比：

**修改前（第3-4行）：**
```bash
set -x
source /root/miniconda3/etc/profile.d/conda.sh
```

**修改后（第3-15行）：**
```bash
set -x

# Pre-flight: 清理残留 Ray 进程
ray stop --force 2>/dev/null
sleep 5
rm -rf /tmp/ray/session_*
pkill -9 -f "ray::" 2>/dev/null
pkill -9 -f raylet 2>/dev/null
pkill -9 -f gcs_server 2>/dev/null
sleep 2
echo "Pre-flight cleanup done"

source /root/miniconda3/etc/profile.d/conda.sh
```

Pre-flight 清理段已正确插入在 `set -x` 之后、`conda activate` 之前。

---
