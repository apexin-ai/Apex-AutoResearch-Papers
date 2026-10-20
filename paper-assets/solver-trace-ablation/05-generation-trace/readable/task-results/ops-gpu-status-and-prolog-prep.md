# ops gpu status and prolog prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-prolog-prep_20260514T115711_result.json`
- **Structured JSON:** [`4c1b0cf5a4dd1069a66f.json`](../../sessions/4c/4c1b0cf5a4dd1069a66f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. nvidia-smi

| GPU | 型号 | 显存占用 | GPU-Util | PID | 进程 |
|-----|------|---------|----------|-----|------|
| 0 | RTX PRO 6000 Black (98GB) | 80223 / 97887 MiB | 89% | 564905 | plan018-additive-random-b01-s44 |
| 1 | RTX PRO 6000 Black (98GB) | 55903 / 97887 MiB | 94% | 572609 | plan009-sft-baseline-s42-r4 |

### 2. plan018-s44 进度
**Step 105/500 (21%)**，~8-13s/step，预计还需 ~55-85 min。GPU 0。

### 3. plan009-sft-r4 进度
**Step 400/500 (80%)**，~1.2 it/s，预计还需 ~1-2 min。GPU 1。

### 4. Prolog s43/s44 数据阻塞：**否**
- `train_500_seed42.jsonl` 存在，500 行，484KB
- `grpo_prolog_exec_only.yaml` 配置正常，已指向正确数据文件
- seed 只控制模型初始化/采样随机性，数据文件不变（C001）
- ROADMAP 标注"阻塞于数据"是错误的，数据已就绪

### 5. 提交命令

GPU 1 即将空闲（plan009-sft-r4 ~1-2 min 完成），GPU 0 约 1h 后空闲。

**plan006-prolog-exec-s43（GPU 1，可立即排队）：**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43"
```

**plan006-prolog-exec-s44（GPU 0，需等 plan018-s44 完成）：**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44"
```

### 6. 磁盘空间：**足够**

| 项目 | 大小 |
|------|------|
| 总容量 | 250G |
| 已用 | 90G (36%) |
| 可用 | **161G** |
| 两个 Prolog 实验需要 | ~62G (每个 ~31G，参考 plan006_prolog_exec_s42) |
| 预期剩余 | ~99G |

主要占用：plan009_sft_baseline_s42 (38G)、plan006_prolog_exec_s42 (31G)、plan018_additive_random_b01_s44 (15G，仍在增长)。

---
