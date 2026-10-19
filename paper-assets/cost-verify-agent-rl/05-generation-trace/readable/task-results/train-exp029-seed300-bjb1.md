# train exp029 seed300 bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_exp029_seed300_bjb1_20260522T151637_result.json`
- **Structured JSON:** [`75ba84f4c0f5af2274d1.json`](../../sessions/75/75ba84f4c0f5af2274d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 状态报告

### Pre-flight checklist (C002) ✅
| 项目 | 状态 |
|------|------|
| 入口点 | `python train.py --config-name` — 与 seed42 一致 |
| 磁盘 | `/root/autodl-tmp` 57GB 可用 (78%) |
| Config | `_alfworld_exp029_seed300_episode.yaml` 已创建并验证 |
| SFT checkpoint | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` → `exp021_ragen_sft_v4/final` 存在 |
| 输出目录 | `/root/autodl-tmp/checkpoints/exp029-seed300/` 已创建 |

### Config 变更（相对 seed42）
- `seed.train`: 42 → **300**
- `experiment_name`: `exp029-seed300-episode-level`
- `local_log_dir` / `default_local_dir`: `exp029-seed300/`
- 其余参数完全一致

### ⚠️ 冲突：GPU 0 被 seed4 OOD eval 占用
- **进程**: PID 427167, `_alfworld_exp029_seed4_ood_step15`
- **GPU 占用**: 8124 MiB on cuda:0
- **启动时间**: ~5 分钟前，模型刚初始化完毕，实际 episode rollout 尚未开始
- **预估耗时**: 30-60+ 分钟（341 OOD environments, single GPU）
- **按指令不 kill**，等 eval 完成后即可启动

### 待执行的启动命令（GPU 释放后直接运行）
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 RAY_ADDRESS="" RAY_TMPDIR=/tmp/ray_seed300 VLLM_WORKER_MULTIPROC_METHOD=spawn python train.py --config-name _alfworld_exp029_seed300_episode' > /root/autodl-tmp/logs/seed300_episode_grpo.log 2>&1 &
```

需要我轮询等待 eval 完成后自动启动，还是你另行安排？

---
