# exp pythia seed43 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pythia_seed43_001_20260518T130548_result.json`
- **Structured JSON:** [`6c7a061ba029cc9ce00e.json`](../../sessions/6c/6c7a061ba029cc9ce00e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 运行正常。Step 1 LoRA 训练 depth_0 进行中，12% (122/939 steps)，~3.5 it/s。

实验已提交，汇总：

| 项目 | 值 |
|------|------|
| exp_id | `pythia_seed43_001` |
| 脚本 | `scripts/run_pythia_seed43.sh` |
| 模型 | Pythia-1.4B (local: `/root/autodl-tmp/models/pythia-1.4b`) |
| seed | 43 |
| samples/depth | 5000 |
| depths | d0-d3 (4-class) |
| GPU | cuda:1 (CUDA_VISIBLE_DEVICES=1) |
| tmux session | `pythia_seed43_001` |
| 输出目录 | `results/pythia_seed43/` |
| registry 状态 | RUNNING |

全流程 8 步：LoRA d0 → gen d1 → LoRA d1 → gen d2 → LoRA d2 → gen d3 → feature extraction → RF eval。`eval_second_seed.py` 已内置 `np.clip(X, -1e10, 1e10)` 防护。预计 2-3h 完成。

---
