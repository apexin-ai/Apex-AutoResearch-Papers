# code eval pipeline prep

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json`
- **Structured JSON:** [`5206002c297ac70e97d7.json`](../../sessions/52/5206002c297ac70e97d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 评估脚本列表

| 脚本 | 位置 | 用途 |
|------|------|------|
| `run_libero_eval.py` | `/root/afford_invar/openvla-oft/experiments/robot/libero/` | Standard LIBERO 4 suites SR 评估（原仓库自带） |
| `run_heatmap_eval.py` | `/root/afford_invar/scripts/evaluation/` | Heatmap 质量评估（**已实现模型加载**） |
| `eval_pride.py` | `/root/afford_invar/scripts/evaluation/` | PRIDE metric 计算（新建） |
| `launch_eval.sh` | `/root/afford_invar/scripts/evaluation/` | 一键评估启动模板（新建） |

### 2. 缺失依赖（LIBERO 仿真评估需要，heatmap 评估不需要）

```bash
pip install robosuite==1.4.1 mujoco imageio[ffmpeg] bddl easydict cloudpickle gym
```

已安装：`libero` ✓, `h5py` ✓, `scipy` ✓, `torch` ✓, `transformers` ✓

### 3. LIBERO-Para 数据状态

- ✓ `paraphrases.json` 已在 `/root/afford_invar/data/`（覆盖全部 5 suites, 共 130 tasks × 5 paraphrases）
- ✓ HDF5 demo 数据已在 `/root/autodl-tmp/LIBERO-datasets/`（spatial/object/goal/10/90 全部有）

### 4. Heatmap eval 与 checkpoint 对接方案

Checkpoint 结构（`/root/afford_invar/runs/&lt;run>/checkpoint-{step}/`）：
- VLA LoRA weights (HF pretrained format)
- `action_head--{step}_checkpoint.pt`
- `afford_decoder--{step}_checkpoint.pt`
- `dataset_statistics.json`

`run_heatmap_eval.py` 中新增 `AffordanceHeatmapGenerator` 类：
- `get_vla()` → 加载 VLA + LoRA
- `AffordanceDecoder(hidden_dim=4096, output_size=128, mid_dim=256)` → 加载 decoder checkpoint
- Forward: image → processor → VLA(output_hidden_states=True) → layer 18 patch features → AffordanceDecoder → 128×128 heatmap

### 5. 评估启动命令模板

**Heatmap（训练完成后立即可跑，不需要 robosuite）：**
```bash
CKPT=/root/afford_invar/runs/libero_goal_no_noops+afford+b2+lr0.0005+a0.1/checkpoint-XXXXX

python /root/afford_invar/scripts/evaluation/run_heatmap_eval.py \
    --checkpoint-dir $CKPT \
    --suite libero_goal \
    --max-demos 5 \
    --device cuda:1 \
    --output-dir /root/afford_invar/results/heatmap_eval
```

**Standard LIBERO SR（需先安装 robosuite）：**
```bash
cd /root/afford_invar/openvla-oft
CUDA_VISIBLE_DEVICES=1 python experiments/robot/libero/run_libero_eval.py \
    --pretrained_checkpoint $CKPT \
    --task_suite_name libero_goal \
    --num_trials_per_task 20 \
    --use_l1_regression True \
    --lora_rank 32 \
    --num_images_in_input 1 \
    --use_proprio False \
    --center_crop True
```

**PRIDE（需两轮 LIBERO SR 评估结果）：**
```bash
python /root/afford_invar/scripts/evaluation/eval_pride.py \
    --original-log &lt;original_eval.txt> \
    --paraphrase-log &lt;paraphrase_eval.txt> \
    --output /root/afford_invar/results/pride.json
```

---
