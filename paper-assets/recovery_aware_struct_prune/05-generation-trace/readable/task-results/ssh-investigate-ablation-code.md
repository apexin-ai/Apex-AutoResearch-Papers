# ssh investigate ablation code

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_investigate_ablation_code_20260523T055725_result.json`
- **Structured JSON:** [`9b43e990c053c4cd8051.json`](../../sessions/9b/9b43e990c053c4cd8051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕。以下是全部结果。

---

## 1. Floor 参数

**文件**: `src/prune.py:307-308`
```python
min_keep_intermediate = int(intermediate_size * 0.4)
```

- **硬编码 0.4 (40%)**，无命令行参数控制
- 要跑 floor 消融，需修改 `prune.py` 添加 `--floor_ratio` 参数

## 2. κ 参数

代码里叫 **`--alpha`**，不叫 kappa。

**文件**: `src/prune.py:166`
```python
parser.add_argument("--alpha", type=float, default=1.0, help="RASP alpha parameter")
```

**已可通过命令行控制。** 公式：
- RASP: `S(h) = I(h) * (1 - F(h))^alpha` (行 210-213)
- RASP-RLVR: `S(h) = I(h) * F(h)^alpha` (行 218-221)
- cka_only: 不使用 alpha，`score = 1 - overlap` (行 223-228)

## 3. 1.5B 模型

- **westd-32935**: 不存在，只有 7B (`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`)
- **westb-23072**: 存在
  - `/root/autodl-tmp/recovery_aware_struct_prune/models/DeepSeek-R1-Distill-Qwen-1.5B`
  - `/root/autodl-tmp/.hf_cache/hub/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-1.5B`

## 4. SFT 超参数 (`train_sft_warmup.py`)

| 参数 | 值 |
|---|---|
| lr | 2e-5 |
| epochs | 1 |
| batch_size | 2 |
| gradient_accumulation | 8 (eff=16) |
| max_seq_length | 2048 |
| lr_scheduler | 默认 (linear) |
| precision | bf16 |
| optimizer | 默认 AdamW |
| save_strategy | epoch |

## 5. GRPO 超参数 (`train_grpo_v5.py`)

| 参数 | 值 |
|---|---|
| lr | 1e-6 |
| epochs | 3 |
| batch_size | 2 |
| gradient_accumulation | 8 (eff=16) |
| max_completion_length | 512 |
| temperature | 0.4 |
| repetition_penalty | 1.15 |
| num_generations | 4 |
| beta (KL) | 0.01 |
| loss_type | dapo |
| format_reward_weight | 0.1 |
| optimizer | adamw_8bit |
| gradient_checkpointing | true |
| report_to | wandb |

## 6. 完整脚本列表

29 个 Python 文件在 `src/`，关键文件：
- `prune.py` — 剪枝主脚本 (modes: standard, rasp, rasp-rlvr, cka_only, random)
- `train_sft_warmup.py` — SFT 恢复
- `train_grpo_v5.py` — GRPO 恢复 (最新版)
- `sft_recovery.py` — 另一个 SFT 脚本 (lr=2e-5, epochs=2, batch=1, grad_accum=8)
- `eval_gsm8k.py` / `eval_math500.py` / `eval_humaneval.py` / `eval_mbpp.py` — 评估
- `compute_layer_cka.py` — CKA 计算
- `importance_score.py` — 重要性分数
- `model_utils.py` — 加载非均匀剪枝模型

## 7. Pipeline 自动化

已有 `scripts/run_alpha_ablation.sh` 可作为模板，流程：prune → eval (无 SFT/GRPO)。完整 pipeline (prune → SFT → GRPO → eval) 需要自行编排，但各阶段脚本都齐全。

---

**消融实验改动需求**：
- **α 消融 (4 个)**：参数已可命令行控制，零代码修改
- **Floor 消融 (3 个)**：需改 `prune.py` 第 308 行，把 `0.4` 抽成 `--floor_ratio` 参数

---
