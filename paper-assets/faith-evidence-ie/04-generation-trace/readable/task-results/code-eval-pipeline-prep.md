# code eval pipeline prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-prep_20260514T073710_result.json`
- **Structured JSON:** [`aed2d39907c1d16f95c9.json`](../../sessions/ae/aed2d39907c1d16f95c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已收集完毕。汇总如下：

---

## 1. SFT Eval 脚本

**需要写新脚本：Yes**

`eval/evaluator.py` 是纯库模块（`DocREDEvaluator` 类），没有 `__main__` 或 argparse CLI 入口。也没有找到 `run_eval`/`infer`/`predict`/`generate` 等任何 runner 脚本。

需要一个 eval runner，负责：
- 加载 checkpoint（base model + LoRA adapter）
- 对 dev.json 每个文档做 inference（生成 JSON 输出）
- 调用 `parse_model_output()` 解析
- 调用 `gold_from_docred()` 转 gold
- 调用 `DocREDEvaluator.from_train_file(train_path).evaluate()` 计算指标
- 输出: F1, Ign-F1, Evi-F1, EDCR, format compliance

---

## 2. 三路 GRPO 完整命令

所有命令的公共前缀（环境变量 + conda）：
```bash
source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp
```

### Stage 3: GRPO+CED（当前在跑）
```bash
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
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
  --wandb_run_name grpo-s3-ced
```

### Stage 2: flat-NLI
```bash
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
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
  --wandb_run_name grpo-s2-flat-nli
```

### Stage 1: extraction-only
```bash
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
  -m freige.training.grpo_trainer \
  --model_name /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --data_dir /root/autodl-tmp/data/docred \
  --stage 1 \
  --output_dir /root/autodl-tmp/grpo_s1 \
  --num_generations 4 \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 16 \
  --num_epochs 1 \
  --learning_rate 5e-5 \
  --seed 42 \
  --wandb_run_name grpo-s1-extraction
```
Stage 1 不需要 `--reward_device`（只用 format + F1 reward，无 NLI 模型），也不需要 `--tau_start/--tau_end`。

---

## 3. GRPO 输出目录

`/root/autodl-tmp/grpo_s3/` 当前为空目录（训练刚开始 7/189 steps）。根据 GRPOConfig：
- `save_strategy="epoch"`, `save_total_limit=2` → 每 epoch 结束保存 checkpoint，最多保留 2 个
- 训练完成后 `trainer.save_model()` + `tokenizer.save_pretrained()` 保存最终模型
- 如果有 WANDB_API_KEY，会上报 wandb

产出文件预期：`adapter_config.json`, `adapter_model.safetensors`, tokenizer 文件, `checkpoint-*` 子目录

---

## 4. 发现的问题

| 项目 | 状态 |
|------|------|
| GRPO CED 运行中 | 正常，7/189 steps，~2min/step，预计 ~6h |
| SFT eval runner | **缺失**，需要新写 |
| NLI cache (`/root/autodl-tmp/nli_cache/`) | 未验证是否被 GRPO 训练引用（`grpo_trainer.py` 的 `CEDRewardWrapper` 没有显式的 `nli_cache` 参数，可能在 `ced_reward.py` 内部处理） |
| `train_nli_cache.json` | 存在于 `/root/autodl-tmp/data/docred/`，38180 样本预计算 cache |
| HF 超时 | 日志显示 NLI 模型下载有 retry（已成功解决） |

**下一步**：需要写一个 `eval/run_eval.py`（或 `scripts/evaluate.py`），做 checkpoint inference + evaluator 调用。

---
