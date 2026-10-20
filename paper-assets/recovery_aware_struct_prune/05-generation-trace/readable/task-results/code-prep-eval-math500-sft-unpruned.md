# code prep eval math500 sft unpruned

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_eval_math500_sft_unpruned_20260518T064056_result.json`
- **Structured JSON:** [`969765cb29efe83cd72d.json`](../../sessions/96/969765cb29efe83cd72d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 方案

### 1. 模型信息

| 项目 | 值 |
|------|-----|
| **exp_id** | `sft_unpruned_baseline` |
| **模型路径** | `/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline` |
| **所在服务器** | **westd-11672** |
| **基座模型** | DeepSeek-R1-Distill-Qwen-7B (unpruned) |
| **训练配置** | 2 epochs, lr=2e-5, GSM8K train, seed=42 |
| **GSM8K 精度** | 81.27% (N=1319) |

### 2. 是否需要 SCP

**是**，如果要在 westb-23072 上跑。模型仅存在于 westd-11672。

但所有已有 MATH-500 eval 都在 westd 上跑的（`eval_math500_unpruned`、`eval_math500_sft_rasp_20`、`eval_math500_sft_standard_20`），**建议直接在 westd 上跑**，省去 SCP ~14GB 的时间。westd cuda:0-3 均属本项目（C004）。

### 3. Eval 命令

```bash
cd /root/recovery_aware_struct_prune && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline
```

与已有 MATH-500 eval 命令格式一致（参考 `eval_math500_sft_rasp_20` 的 `python src/eval_math500.py --model_path sft_rasp_20_westd`）。用全路径更明确。

### 4. submit_training_job 参数

```
server: westd-11672
account: root
gpu: cuda:0  (或任一空闲 GPU)
command: 上述命令
exp_id: eval_math500_sft_unpruned
tmux_session: eval_math500_sft_unpruned
```

### 5. Registry 注册信息

```
exp_id: eval_math500_sft_unpruned
parent: sft_unpruned_baseline
hypothesis: MATH-500 eval of unpruned SFT model — fills asymmetric baseline gap (W3 review). Completes the comparison: base unpruned (73.6%) vs SFT unpruned (?) vs GRPO unpruned (69%).
spec.checkpoint_source: /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline
spec.data_path: MATH-500
spec.data_count: 500
spec.server: westd-11672
spec.seed: 42
```

### 6. 预计运行时间

~30-45 分钟。GSM8K full eval (1319 samples) 在同模型上耗时 ~65 分钟 (~2.5s/it)，MATH-500 仅 500 题但生成更长，估计 3-5s/it。

### 7. 已有 MATH-500 数据对照

| 模型 | MATH-500 |
|------|----------|
| Unpruned base | 73.6% |
| Unpruned SFT | **待测** |
| Unpruned GRPO | 69.0% |
| Pruned RASP SFT | 24.2% |
| Pruned Standard SFT | 26.0% |

W3 要的就是 "Unpruned SFT" 这一行，补上后 base→SFT→GRPO 三阶段对比完整。

---
