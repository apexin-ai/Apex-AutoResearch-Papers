# ops westd seed7 kl step5 restart and c prime ood

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_seed7_kl_step5_restart_and_c_prime_ood_20260521T234445_result.json`
- **Structured JSON:** [`cf772fefc5d318166ceb.json`](../../sessions/cf/cf772fefc5d318166ceb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 状态确认两个 job 都在运行：
- **GPU 0**: 3 MiB（c_prime_step5_ood 刚启动 Ray init）
- **GPU 3**: 90,467 MiB / 97,887 MiB（seed7 模型已加载，eval 进行中）

---

## 产出总结

### 1. seed7_high_kl_step5_ood 重启 ✅
- **错误原因**: 首次启动时 Ray 检测到 Docker 88 CPU，尝试预启动 88 个 worker，大量 crash（"worker process has not registered within timeout"）。训练脚本卡在 Ray init 后。
- **修复**: `ray stop --force` 清理残留 → 加入 `RAY_USE_MULTIPROCESSING_CPU_COUNT=1` + `RAY_DISABLE_DOCKER_CPU_WARNING=1` → 重新提交
- **新 PID**: 968497，westd cuda:3，90GB VRAM 已占用，eval 运行中
- **Registry**: RUNNING

### 2. C' step 5 FSDP→HF 转换 + SCP ✅
- Checkpoint: `/root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_5/actor/` (FSDP shards: `model_world_size_2_rank_0.pt` + `rank_1.pt`)
- 转换: `convert_fsdp_to_hf.py` → `/root/autodl-tmp/checkpoints/c_prime_step5_hf/` (20.9s)
- SCP: 建立 bjb1→westd SSH key auth (`connect.westd.seetacloud.com:47453`)，4.06GB 传输完成 (~5.5 min, ~12 MB/s)
- 目标路径: `westd:/root/autodl-tmp/checkpoints/qwen_c_prime_step5_hf/` (10 files 完整)

### 3. c_prime_step5_ood 提交 ✅
- Config: `_alfworld_c_prime_step5_ood_eval.yaml` (cuda:0, val_only, 134 OOD episodes)
- PID: 995987, westd cuda:0, Ray 已启动
- Registry: RUNNING, parent=exp029_intervention_c_prime

### 4. C' 当前进度
- **Step 6/7 (86%)**, 训练正常
- **Step 5 trajectory-level metrics**:
  - `response_length/mean`: **8,327 tokens** (cap 12000 内，远低于上限)
  - `response/aborted_ratio`: **0.0** (无截断)
  - `val reward mean@32`: **2.1875** (~21.9% success rate × 10pt)
  - `val pass@1 (non-zero)`: **1.0**
  - `per-turn response_length`: 1,024 tokens
  - `num_actions`: 21.66
  - Step 用时: ~1,194s (~20 min)

---
