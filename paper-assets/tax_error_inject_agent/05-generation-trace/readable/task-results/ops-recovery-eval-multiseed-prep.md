# ops recovery eval multiseed prep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recovery-eval-multiseed-prep_20260516T023021_result.json`
- **Structured JSON:** [`8bf1955a2c8ee76008a7.json`](../../sessions/8b/8bf1955a2c8ee76008a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the report:

---

## Recovery Eval Multi-seed 准备工作报告

### 1. Recovery Eval 脚本

**位置**: `/root/autodl-tmp/tax_error_inject_agent/eval/recovery.py`

**参数列表**:
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--model_path` | None | LoRA adapter checkpoint 路径 |
| `--base_model` | Qwen3-8B 路径 | 基座模型 |
| `--task_list` | None | 任务列表 JSON（使用 `eval/eval_tasks_47.json`） |
| `--num_episodes` | 134 | 不指定 task_list 时的 episode 数 |
| `--inject` / `--no_inject` | False | 是否注入错误 |
| `--inject_mode` | "action" | 注入模式 |
| `--inject_step` | "auto" | 注入步骤 |
| `--output` | eval_results/results.json | 输出路径 |
| `--device` | cuda:0 | GPU |
| `--seed` | 42 | eval 随机种子（固定为 42） |

**运行命令格式**（从已有结果反推）:
```bash
CUDA_VISIBLE_DEVICES=X python eval/recovery.py \
    --model_path &lt;checkpoint> \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
    --inject \
    --task_list eval/eval_tasks_47.json \
    --output eval_results/&lt;name>.json \
    --device cuda:0
```

### 2. Checkpoint 清单 — 全部 15 个存在

所有 checkpoint 在 `/root/autodl-tmp/tax_error_inject_agent/checkpoints/`:

| Condition | seed=42 | seed=0 | seed=123 | seed=1 | seed=7 |
|-----------|---------|--------|----------|--------|--------|
| **Vanilla** | `mini_vanilla_sft_v4` | `..._seed0` | `..._seed123` | `..._seed1` | `..._seed7` |
| **TaxEI** | `mini_taxei_sft_v4` | `..._seed0` | `..._seed123` | `..._seed1` | `..._seed7` |
| **Random** | `mini_random_sft_v4` | `..._seed0` | `..._seed123` | `..._seed1` | `..._seed7` |

**无需重训任何 checkpoint。**

### 3. Recovery Eval 完成状态

| Condition | seed=42 | seed=0 | seed=123 | seed=1 | seed=7 |
|-----------|---------|--------|----------|--------|--------|
| **Vanilla** | ✅ 61.7% | ✅ 68.1% | ✅ 66.0% | ❌ | ❌ |
| **TaxEI** | ✅ 59.6% | ✅ 46.8% | ✅ 61.7% | ❌ | ❌ |
| **Random** | ✅ 63.8% | ❌ | ❌ | ❌ | ❌ |

**已完成 7/15，剩余 8 个**：
- Vanilla: seed=1, seed=7
- TaxEI: seed=1, seed=7
- Random: seed=0, seed=123, seed=1, seed=7

### 4. 批量 Recovery Eval 脚本框架

用 4 张 GPU 并行，两轮跑完：

```bash
cd /root/autodl-tmp/tax_error_inject_agent
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
BASEM=/root/autodl-tmp/models/Qwen/Qwen3-8B

find_final_ckpt() {
    ls -dt "$1"/v*-*/ 2>/dev/null | head -1 | xargs -I{} sh -c 'ls -d {}checkpoint-* | sort -V | tail -1'
}

# === Round 1: 4 jobs on 4 GPUs ===
CUDA_VISIBLE_DEVICES=0 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_vanilla_sft_v4_seed1) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_vanilla_recovery_eval_s1.json --device cuda:0 &
CUDA_VISIBLE_DEVICES=1 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_taxei_sft_v4_seed1) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_taxei_recovery_eval_s1.json --device cuda:0 &
CUDA_VISIBLE_DEVICES=2 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_random_sft_v4_seed0) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_random_recovery_eval_s0.json --device cuda:0 &
CUDA_VISIBLE_DEVICES=3 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_random_sft_v4_seed123) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_random_recovery_eval_s123.json --device cuda:0 &
wait

# === Round 2: 4 jobs on 4 GPUs ===
CUDA_VISIBLE_DEVICES=0 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_vanilla_sft_v4_seed7) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_vanilla_recovery_eval_s7.json --device cuda:0 &
CUDA_VISIBLE_DEVICES=1 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_taxei_sft_v4_seed7) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_taxei_recovery_eval_s7.json --device cuda:0 &
CUDA_VISIBLE_DEVICES=2 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_random_sft_v4_seed1) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_random_recovery_eval_s1.json --device cuda:0 &
CUDA_VISIBLE_DEVICES=3 python eval/recovery.py --model_path $(find_final_ckpt checkpoints/mini_random_sft_v4_seed7) --base_model $BASEM --inject --task_list eval/eval_tasks_47.json --output eval_results/v4_random_recovery_eval_s7.json --device cuda:0 &
wait
```

### 5. GPU 时间预估

- 从已有结果时间戳推断：每个 recovery eval（47 episodes）约 **1 小时**
- 8 个剩余 eval，4 GPU 并行 → **2 轮 × ~1h = ~2 小时**
- 如果顺序跑则 ~8 小时

---
