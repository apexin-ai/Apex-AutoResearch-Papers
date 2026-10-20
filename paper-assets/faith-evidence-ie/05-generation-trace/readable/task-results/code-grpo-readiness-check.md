# code grpo readiness check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-readiness-check_20260514T070038_result.json`
- **Structured JSON:** [`629dd067442843bd0964.json`](../../sessions/62/629dd067442843bd0964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the verification report.

---

## GRPO 三路对比验证报告

### 检查清单

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | Stage 切换 (`--stage 1/2/3`) | **PASS** — L309: `choices=[1,2,3]`; L382-402: stage≥2 加 CED/flat_nli，stage 1 只有 format+F1 |
| 2 | SFT adapter 加载 | **PASS** — L375-378: `PeftModel.from_pretrained` → `merge_and_unload()` |
| 3 | tau 调度 | **PASS** with caveat — L147-154 初始化, L156-162 线性插值。**但 total_steps 计算有 bug**（见下） |
| 4 | TRL 1.1.0 兼容 (`processing_class=`) | **PASS** — L438: `processing_class=tokenizer` |
| 5 | SDPA attention | **PASS** — L361: `attn_implementation="sdpa"` |
| 6 | 模型路径 | **PASS** — L303: default `/root/autodl-tmp/models/Qwen3-4B` |
| 7 | DeepSpeed 注释 | **PASS** — L7-8 引用 `deepspeed_zero2.json` |
| 8 | `compute_ced_reward` hard_neg=[] 退化 | **PASS** — `ced_reward.py` L236-237: `p_neg=0.0`，reward = `max(0, p_pos) * I(p_pos>tau)` = `p_pos * I(p_pos>tau)` |
| 9 | `compute_flat_nli_reward` 签名 | **PASS** — L317-332: `(claim, cited_evidence_sents, tau)` → `{"reward", "p_pos"}` |
| 10 | ZeRO-2 配置 | **PASS** — stage 2 + CPU offload optimizer + bf16 |
| 11 | TRL extra columns → reward kwargs | **PASS** — TRL 1.1.0 自动将 dataset 非 `prompt` 列作为 kwargs 传给 reward functions |
| 12 | accelerate_4gpu.yaml | **PASS** with caveat — 4 进程, DEEPSPEED, bf16。但 deepspeed_config_file 路径可能冲突（见下） |

### 发现的问题

#### BUG 1: `total_steps` 缺少 GPU 数量因子（中等严重）

`grpo_trainer.py` L385-387:
```python
steps_per_epoch = math.ceil(
    len(train_dataset) / (args.per_device_batch_size * args.gradient_accumulation_steps)
)
```

4 卡 DDP/DeepSpeed 下，dataset 被分片到 4 个 GPU。实际 steps = `dataset_size / (per_device_bs * num_gpus * grad_accum)`。当前计算结果 **高了 4 倍**。

**影响**：tau 调度进度只走到 ~25%。tau_start=0.3, tau_end=0.5 时，实际只调度到 ~0.35 而非 0.5。

**修复**：
```python
num_gpus = int(os.environ.get("WORLD_SIZE", 1))
steps_per_epoch = math.ceil(
    len(train_dataset) / (args.per_device_batch_size * num_gpus * args.gradient_accumulation_steps)
)
```

#### BUG 2: accelerate config 与 GRPOConfig 的 DeepSpeed 路径可能冲突（低严重）

`accelerate_4gpu.yaml` L3-4:
```yaml
deepspeed_config:
  deepspeed_config_file: configs/deepspeed_zero2.json
```

命令行同时传 `--deepspeed freige/configs/deepspeed_zero2.json` 到 GRPOConfig。两个路径相对于不同位置。GRPOConfig 的 `deepspeed` 参数会覆盖 accelerate config，但 accelerate 初始化时可能先尝试加载自己的路径导致报错。

**修复建议**：从 accelerate config 中删除 `deepspeed_config_file`，只保留 `distributed_type: DEEPSPEED` 和 `zero3_init_flag: false`，让 GRPOConfig 全权管理 deepspeed config。

#### 风险项 3: TRL 1.1.0 reward function 的 completions 格式（需服务器验证）

TRL 不同版本对 completions 参数格式不一致。当前代码假设 `completions: list[str]`。部分 TRL 版本传入 `list[list[dict]]`（chat format）。需在服务器上验证：

```python
python3 -c "import trl; print(trl.__version__)"
```

然后检查 GRPOTrainer 源码中 reward function 的调用方式。

#### 风险项 4: CED 退化 vs flat_nli 不完全等价

当 `hard_negative_sents=[]` 时：
- `compute_ced_reward`: R = `max(0, p_pos - 0) * I(p_pos > tau)` = `p_pos * I(p_pos > tau)`
- `compute_flat_nli_reward`: R = `p_pos * I(p_pos > tau)`

两者等价。Stage 2 (flat_nli mode) 通过 `CEDRewardWrapper` L234 显式调用 `compute_flat_nli_reward`，正确。

### 三组提交命令

CWD = `/root/autodl-tmp/`

**Stage 1: extraction-only (format + F1)**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 1 \
  --output_dir /root/autodl-tmp/grpo_s1 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s1-extraction'
```

**Stage 2: flat-NLI**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 2 \
  --tau_start 0.3 --tau_end 0.5 \
  --output_dir /root/autodl-tmp/grpo_s2 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s2-flatnli'
```

**Stage 3: CED**
```bash
bash -c 'source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export WANDB_API_KEY=[REDACTED] /root/.wandb_key 2>/dev/null) && \
cd /root/autodl-tmp && \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --deepspeed freige/configs/deepspeed_zero2.json \
  --stage 3 \
  --tau_start 0.3 --tau_end 0.5 \
  --output_dir /root/autodl-tmp/grpo_s3 \
  --num_generations 4 \
  --reward_device cpu \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s3-ced'
```

### 待修复后再提交

1. **修复 total_steps 计算**（BUG 1）— 加入 `WORLD_SIZE` 因子，否则 tau 调度不达标
2. **清理 accelerate config 的 deepspeed 路径**（BUG 2）— 防止初始化冲突
3. **服务器验证 TRL completions 格式**（风险项 3）— `pip show trl` 确认版本后检查源码

是否需要我现在修复 BUG 1 和 BUG 2？

---
