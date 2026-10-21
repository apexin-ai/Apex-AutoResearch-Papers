# diagnose bjb2 readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb2-readiness_20260515T014512_result.json`
- **Structured JSON:** [`a8419811e9eebb5eeca4.json`](../../sessions/a8/a8419811e9eebb5eeca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是结果：

---

## bjb2-40593 Eval 可用性检查结果

### 1. GPU 状态
- **空闲**: RTX 4090 D, 显存 0/24564 MiB, 利用率 0%, 无 GPU 进程

### 2. evaluate.py 一致性
- **一致**: `src/evaluate.py` 两台服务器均为 14489 bytes
- 核心模块 (crm.py, aci.py, cgs.py, utils.py, train_crm.py) 字节数完全相同
- **差异**:
  - bjb2 多了: `src/gated_crm.py`, `src/compute_norm_stats.py`
  - bjb1 多了: `src/sanity_check_reset.py`, `run_eval_gpu.py`, `diagnose_crm_scale.py`
  - **注意**: bjb1 有 `run_eval_gpu.py`（根目录），bjb2 没有。如果 eval 用的是这个脚本，需要同步过去

### 3. Cache 路径
- bjb2: `/root/autodl-tmp/crm_cache/spatial/` — **2402 samples**
- bjb1: `/root/autodl-tmp/crm_cache_v5/spatial/` — **12167 samples**
- bjb2 上 **不存在** `crm_cache_v5`
- `train_crm.py` 默认 `--cache_dir` 硬编码为 `/root/autodl-tmp/crm_cache/`
- **但**: `evaluate.py` 是 LIBERO rollout 脚本，**不读 precompute cache**，只加载 CRM checkpoint + SmolVLA 模型在仿真环境中跑。cache 不兼容只影响训练，不影响 eval

### 4. CRM v3-norm Checkpoints
- **存在**: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt` (1.3MB, 2026-05-15 创建)

### 5. Python 环境
- Python 3.12.3 (miniconda3)
- 依赖包列表未能通过 read_only 获取（pip 被 allowlist 拦截），需另外确认 torch/transformers/lerobot/robosuite 是否安装

---

### 结论

**不能立即启动，需要先做准备工作：**

1. **必须**: 确认 robosuite / lerobot / transformers / torch 等依赖已安装（需用 `ssh_execute` 跑 `pip list`）
2. **必须**: 同步 `run_eval_gpu.py` 到 bjb2（如果 eval 依赖这个入口脚本）
3. **无需处理**: cache 路径差异不影响 eval（evaluate.py 不读 cache）
4. **已就绪**: GPU 空闲、CRM checkpoint 存在、核心代码一致

---
