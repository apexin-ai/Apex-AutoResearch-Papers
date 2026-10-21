# code mmlu gsm8k eval prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mmlu-gsm8k-eval-prep_20260523T125251_result.json`
- **Structured JSON:** [`9928b75ad9732d93899d.json`](../../sessions/99/9928b75ad9732d93899d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 产出

### 1. lm-eval 安装状态
**未安装**。安装命令：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
pip install lm-eval
```

### 2. 模型路径

| 模型 | 路径 | 状态 |
|------|------|------|
| Vanilla Qwen3-8B | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` | OK |
| ACT best s1 ckpt-8000 | `exp004_act_baseline/checkpoint-8000` | **不在 29046 上** |
| ACT s2 ckpt-8000 | `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-8000` | OK (可替代) |
| R3-only s1 ckpt-6500 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-6500` | OK |
| Heldout ckpt-500 | `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp004_heldout/checkpoint-500` | OK (备用) |

**问题**：ACT s1 全量训练 ckpt-8000 不在 29046。`outputs/` 下只有 `exp-004-act-baseline-s2`（seed 2）。需要决定：用 s2 代替，还是从其他服务器迁移 s1。

两个 adapter 都以 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` 为 base model。ACT s2 的 LoRA config: r=64, alpha=128, targets=q/k/v/o/gate/up/down_proj；R3-only s1: r=64, alpha=64, targets=q/k/v/o_proj。

### 3. eval 脚本
已写入 29046: `/root/contrastive_entrain_calib/eval/run_lm_eval.sh`
本地副本: `eval/run_lm_eval.sh`

### 4. 运行命令

```bash
# 先安装 lm-eval
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
pip install lm-eval

# 1. Vanilla Qwen3-8B
CUDA_VISIBLE_DEVICES=0 nohup bash /root/contrastive_entrain_calib/eval/run_lm_eval.sh \
  /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  none \
  /root/eval_results/lm_eval/vanilla \
  > /tmp/eval_vanilla.log 2>&1 &

# 2. ACT best (暂用 s2 ckpt-8000，待确认 s1)
CUDA_VISIBLE_DEVICES=1 nohup bash /root/contrastive_entrain_calib/eval/run_lm_eval.sh \
  /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  /root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-8000 \
  /root/eval_results/lm_eval/act_best \
  > /tmp/eval_act.log 2>&1 &

# 3. R3-only best (s1 ckpt-6500)
# 等前面两个跑完后用 GPU 0 或 1
CUDA_VISIBLE_DEVICES=0 nohup bash /root/contrastive_entrain_calib/eval/run_lm_eval.sh \
  /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
  /root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-6500 \
  /root/eval_results/lm_eval/r3only_best \
  > /tmp/eval_r3only.log 2>&1 &
```

2 个 GPU (RTX PRO 6000 96GB)，可同时跑 2 个 eval。Qwen3-8B bf16 约 16GB 显存。

### 5. 预计运行时间

| 任务 | 单模型耗时 (hf backend, 8B) | 说明 |
|------|---------------------------|------|
| MMLU (5-shot) | ~2 小时 | 14k 多选题，loglikelihood |
| GSM8K (5-shot) | ~5-10 分钟 | 1.3k 题，generate_until |
| **单模型总计** | ~2 小时 | |
| **3 模型总计** | ~4-5 小时 | 2 GPU 并行跑前 2 个，第 3 个排队 |

如果想加速，可以装 vllm 用 `--model vllm` 后端（MMLU 降到 ~15-20 分钟），但 vllm + PEFT 配置更复杂，建议先用 hf 后端跑通。

---

**待决策**：ACT s1 ckpt-8000 需要从其他服务器迁移，还是用 s2 替代？论文主表如果报的是 s1 结果，eval 也应该用 s1 保持一致。

---
