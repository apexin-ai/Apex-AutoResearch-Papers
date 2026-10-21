# prep mf2 multiseed grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_mf2_multiseed_grpo_20260522T074505_result.json`
- **Structured JSON:** [`e0e4237c3aca43b910fe.json`](../../sessions/e0/e0e4237c3aca43b910fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是完整汇报：

---

```
== SFT Checkpoints ==
RASP α=1.0:
  westd-32935: /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd/ (12G) ✅
  westb-23072: ❌ 不存在（仅有 sft_rasp_rlvr_20, sft_rasp_20_1p5b）
Random:
  westd-32935: /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20/ (12G) ✅
  westb-23072: ❌ 不存在

== Seed 控制 ==
方式: --seed 参数（train_grpo_v5.py L200, default=42）
验证:
  - L61-65: set_seed() 覆盖 random/np/torch/cuda
  - L218:   set_seed(args.seed) 在 main() 开头调用
  - L239:   prepare_dataset(seed=args.seed)
  - L262:   GRPOConfig(seed=args.seed)
  完备 ✅

== Dry-run ==
Status: PASS ✅
  RASP Tokenizer: vocab=151643
  Random Tokenizer: vocab=151643
  Dataset: 7473 samples (GSM8K train)
  Prompt 格式: "Solve the following math problem step by step. Put your final answer in \boxed{}."

== GPU 状态 ==
westd-32935 (4× RTX PRO 6000, 98GB each):
  GPU 0: 19GB/98GB — eval_math500 (grpo_stage2_standard_20_fair), 已跑 4h
  GPU 1: 17GB/98GB — eval_math500 (sft_random_20), 已跑 3.7h
  GPU 2: 16GB/98GB — eval_gsm8k (grpo_rasp_alpha2p0_20), 已跑 30min
  GPU 3: 16GB/98GB — eval_gsm8k (grpo_rasp_alpha0p5_20), 已跑 30min
  每张 GPU 剩余 ~80GB，GRPO 单卡需约 40-50GB，可共存但偏紧

westb-23072 (2× RTX PRO 6000, 98GB each):
  GPU 0: 4.4GB/98GB — 基本空闲
  GPU 1: 0GB/98GB — 完全空闲
  但无 SFT checkpoint，需先 scp 过去
```

## Ready-to-submit commands (westd-32935)

```bash
# RASP seed 123 (GPU 0)
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_seed123 \
  --seed 123 --max_steps 100 --gradient_checkpointing true \
  --run_name grpo_mf2_rasp_seed123 --gpu 0 && \
CUDA_VISIBLE_DEVICES=0 python3 src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_seed123 \
  --output_path results/eval_grpo_mf2_rasp_seed123.json' \
> /tmp/grpo_rasp_seed123.log 2>&1 &

# RASP seed 456 (GPU 1)
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_seed456 \
  --seed 456 --max_steps 100 --gradient_checkpointing true \
  --run_name grpo_mf2_rasp_seed456 --gpu 1 && \
CUDA_VISIBLE_DEVICES=1 python3 src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_seed456 \
  --output_path results/eval_grpo_mf2_rasp_seed456.json' \
> /tmp/grpo_rasp_seed456.log 2>&1 &

# Random seed 123 (GPU 2)
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_seed123 \
  --seed 123 --max_steps 100 --gradient_checkpointing true \
  --run_name grpo_mf2_random_seed123 --gpu 2 && \
CUDA_VISIBLE_DEVICES=2 python3 src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_seed123 \
  --output_path results/eval_grpo_mf2_random_seed123.json' \
> /tmp/grpo_random_seed123.log 2>&1 &

# Random seed 456 (GPU 3)
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_seed456 \
  --seed 456 --max_steps 100 --gradient_checkpointing true \
  --run_name grpo_mf2_random_seed456 --gpu 3 && \
CUDA_VISIBLE_DEVICES=3 python3 src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_seed456 \
  --output_path results/eval_grpo_mf2_random_seed456.json' \
> /tmp/grpo_random_seed456.log 2>&1 &
```

```
== 阻塞项 ==
1. **GPU 白名单冲突**: C005 白名单为 westb-23072 + westd-29022，westd-32935 不在其中。
   如在 westd-32935 跑需确认白名单是否已更新。
2. **GPU 共存风险**: westd-32935 四张 GPU 均有 eval 进程（16-19GB），
   GRPO 单卡需 ~40-50GB（model+ref_model+optimizer+grad），合计 ~60-70GB/卡，
   98GB 应够但建议等 eval 跑完后再启动，避免 OOM。
3. **westb-23072 无 checkpoint**: 若要在 westb 跑需先 scp 过去
   （sft_rasp_20_westd + sft_random_20 各 12GB）。
```

---
