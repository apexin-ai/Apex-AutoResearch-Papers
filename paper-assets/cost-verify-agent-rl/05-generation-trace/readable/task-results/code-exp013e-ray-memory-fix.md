# code exp013e ray memory fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013e-ray-memory-fix_20260514T085254_result.json`
- **Structured JSON:** [`ffcec092923c0d0772e9.json`](../../sessions/ff/ffcec092923c0d0772e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已清空。

## 产出汇总

### 1. ray.init 调用位置
`/root/cost-verify-agent-rl/RAGEN/train.py:205` — `ray.init(**ray_init_kwargs)`

### 2. 修复方式
**方式 B（直接改代码）** — 已在 `train.py:203` 硬编码：
```python
ray_init_kwargs["object_store_memory"] = 30 * 1024**3
```
此行在 config 的 `ray_kwargs.ray_init` 被解析后、`ray.init()` 调用前强制覆盖，确保无论 config 怎么写都生效。修复已就位，无需额外改动。

### 3. Dry-run 验证结果
日志输出确认：
```
ray init kwargs: {'num_cpus': None, 'runtime_env': {...}, 'object_store_memory': 32212254720}
```
- object_store_memory = **32,212,254,720 bytes (~30GB)** ✅
- 无 SIGKILL/OOM 错误 ✅
- Workers 正常加载模型 ✅

### 4. 最终启动命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR && \
export ALFWORLD_DATA=/root/autodl-tmp/alfworld && \
export CUDA_VISIBLE_DEVICES=0,1 && \
cd /root/cost-verify-agent-rl/RAGEN && \
nohup python train.py --config-name _alfworld_exp013b_dense_reward > /root/autodl-tmp/logs/exp013e.log 2>&1 &
```

---
