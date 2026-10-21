# code multiseed config diff

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multiseed_config_diff_20260522T090747_result.json`
- **Structured JSON:** [`9ed38457b681bfea22ac.json`](../../sessions/9e/9ed38457b681bfea22ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是完整配置表。

---

## 共享超参（5 条件完全一致）

| 参数 | 值 | 来源 |
|------|-----|------|
| model | Qwen2.5-7B-Instruct (`/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`) | config.py MODEL_NAME |
| lr | 2e-4 | config.py LEARNING_RATE (v7 未显式传，用默认值) |
| batch_size | 1 | config.py BATCH_SIZE (v7 未显式传，用默认值) |
| grad_accum | 8 (effective batch = 8) | config.py GRADIENT_ACCUMULATION |
| epochs | 3 | train_phase2.py argparse default |
| max_seq_len | 2048 | v7 命令显式传 |
| optimizer | AdamW | train_phase2.py:190 硬编码 |
| weight_decay | 0.01 | train_phase2.py:190 硬编码 |
| lr_scheduler | cosine_with_warmup | train_phase2.py:197 硬编码 |
| warmup_steps | max(1, total_steps // 10) ≈ 10% | train_phase2.py:199 硬编码 |
| LoRA rank (r) | 16 | config.py LORA_RANK |
| LoRA alpha | 32 | train_phase2.py:141 硬编码 |
| LoRA dropout | 0.05 | train_phase2.py:143 硬编码 |
| LoRA target_modules | ["q_proj", "v_proj"] | train_phase2.py:142 硬编码 |
| LoRA bias | "none" | 硬编码 |
| precision | bf16 (torch.bfloat16) | threadgate.py:81 硬编码 |
| gradient_checkpointing | enabled | train_phase2.py:148 硬编码 |
| grad_clip_norm | 1.0 | train_phase2.py ~L278 硬编码 |
| attn_implementation | "eager" | train_phase2.py:151-154 硬编码 |
| gar_epsilon | 0.001 | config.py GAR_EPSILON |
| data | ultrachat_8k (全量，无 train/eval split) | --data-dir 默认值 |
| seeds | [42, 123, 7] (3 seeds) | D048 协议 |

## 条件差异（仅列不同项）

| 参数 | Base | TG | LO | UG | SS |
|------|------|----|----|----|----|
| **训练脚本** | train_phase2.py | train_phase2.py | train_phase2.py | train_phase2.py | **train_phase2_v8b.py** |
| **gate-type** | none | threadgate | none | uniform | threadgate |
| **lambda-gar** | **0** | 1.0 | 1.0 | 1.0 | 1.0 |
| **lambda-gate-div** | 0 (自动，code 检查 gate_type≠none) | 1.0 | 0 (自动，gate_type=none) | 1.0 | 1.0 |
| **init-bias** | N/A (无 gate) | 1.5 | N/A (无 gate) | 1.5 | 1.5 |
| **gate-lr-multiplier** | N/A (无 gate) | 10 | N/A (无 gate) | 10 | 10 |
| **min-gate-std** | N/A | 0.05 | N/A | 0.05 | 0.05 |
| **gar-loss-mode** | N/A (λ=0) | mse_target | mse_target | mse_target | mse_target |
| **gar-target** | N/A (λ=0) | 0.5 | 0.5 | 0.5 | 0.5 |
| **scheduled-sampling** | No | No | No | No | **Yes** |
| **ss-max-ratio** | — | — | — | — | **0.3** |
| **ss-warmup-steps** | — | — | — | — | 0 |
| **ss-gen-max-tokens** | — | — | — | — | 128 |
| **ss-gen-temperature** | — | — | — | — | 0.7 |

## 完整运行命令模板

**Base** (纯 LoRA SFT):
```bash
python src/train_phase2.py \
  --gate-type none --lambda-gar 0 \
  --max-seq-len 2048 --seed {SEED} --epochs 3 \
  --output-dir runs/d048_base_s{SEED} \
  --data-dir data/ultrachat_8k
```

**TG** (= v7 配置):
```bash
python src/train_phase2.py \
  --gate-type threadgate \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 \
  --min-gate-std 0.05 --init-bias 1.5 \
  --gate-lr-multiplier 10 --max-seq-len 2048 \
  --seed {SEED} --epochs 3 \
  --output-dir runs/d048_tg_s{SEED} \
  --data-dir data/ultrachat_8k
```

**LO** (GAR loss only, 无 gate):
```bash
python src/train_phase2.py \
  --gate-type none \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 \
  --max-seq-len 2048 --seed {SEED} --epochs 3 \
  --output-dir runs/d048_lo_s{SEED} \
  --data-dir data/ultrachat_8k
```

**UG** (uniform gate):
```bash
python src/train_phase2.py \
  --gate-type uniform \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 \
  --min-gate-std 0.05 --init-bias 1.5 \
  --gate-lr-multiplier 10 --max-seq-len 2048 \
  --seed {SEED} --epochs 3 \
  --output-dir runs/d048_ug_s{SEED} \
  --data-dir data/ultrachat_8k
```

**SS** (scheduled sampling):
```bash
python src/train_phase2_v8b.py \
  --gate-type threadgate \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 \
  --min-gate-std 0.05 --init-bias 1.5 \
  --gate-lr-multiplier 10 --max-seq-len 2048 \
  --scheduled-sampling --ss-max-ratio 0.3 \
  --ss-warmup-steps 0 --ss-gen-max-tokens 128 --ss-gen-temperature 0.7 \
  --seed {SEED} --epochs 3 \
  --output-dir runs/d048_ss_s{SEED} \
  --data-dir data/ultrachat_8k
```

## 待确认问题

### 1. Base 关闭 GAR loss — `--lambda-gar 0` 可行

代码 L274: `loss = l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div`。`lambda_gar=0` 使 GAR 项归零。同时 `gate_type=none` 使 `l_gate_div` 也自动为 0（代码 L263-267 检查 `gate_type != "none"`）。最终 loss = l_ntp，纯 LoRA SFT。**无需代码改动。** 唯一副作用：`compute_gar_loss` 仍被调用（浪费少量计算），但不影响训练结果。

### 2. ⚠️ UG gate alpha 不是固定 0.5 — 是可学习的

任务描述说 UG "alpha=0.5 固定"，但代码中 `--gate-type uniform` 使用的是 `UniformGateNetwork`（threadgate.py:57-69），这是一个**可学习**的网络：`sigmoid(fc2(relu(fc1(cat(down_proj(h), constant_vector)))))`。它和 threadgate 的区别仅在于用 constant_vector 替代 turn_embedding，即**不感知 turn 结构**，但 gate 值仍然是动态计算并可学习的。

- 初始 gate ≈ sigmoid(init_bias=1.5) ≈ 0.82，不是 0.5
- 如果需要 alpha 恒定为 0.5，需要**修改代码**：新增一个不含可学习参数的 FixedGateNetwork，直接返回 0.5

**建议**：当前 UniformGateNetwork 的消融意义是"去掉 turn-aware 信息但保留可学习 gate"，这已经是有效的消融。如果改为固定 0.5，消融意义变为"完全去掉 gate 的自适应能力"。请 Director 确认需要哪种。

### 3. SS 使用 train_phase2_v8b.py

SS 条件必须用 `train_phase2_v8b.py`，因为 `--scheduled-sampling` 参数只在 v8b 中存在。v8b 的基础超参（LoRA、optimizer、warmup）与 train_phase2.py 完全一致，已验证。

### 4. config.py 默认 vs v7 实际值差异

| 参数 | config.py 默认 | v7 实际 | D048 应使用 |
|------|---------------|---------|------------|
| lambda_gar (GAR_LAMBDA) | **2.0** | 1.0 | 1.0 |
| init_bias (INIT_BIAS) | **2.0** | 1.5 | 1.5 |
| gate_lr_multiplier | **1.0** | 10 | 10 |
| gar_target (GAR_TARGET) | **0.3** | 0.5 | 0.5 |

上表中 D048 采用 v7 实际值。如果直接不传这些参数，会用 config.py 默认值，与 v7 不一致。**所有条件必须显式传这些参数。**

### 5. 无 eval split

数据集 `ultrachat_8k` 只有单个 split（data-00000-of-00001.arrow），训练时全量使用，无 train/eval 划分。如需 eval，需另行处理。

---
