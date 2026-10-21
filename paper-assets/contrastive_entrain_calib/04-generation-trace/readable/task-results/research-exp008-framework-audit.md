# research exp008 framework audit

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp008-framework-audit_20260522T132713_result.json`
- **Structured JSON:** [`9b59690a4b01b3b17b2f.json`](../../sessions/9b/9b59690a4b01b3b17b2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。结果如下：

---

## 核实结果

| 实验 | 脚本文件 | Trainer 类 | reward/loss 计算方式 | num_generations |
|------|----------|-----------|---------------------|----------------|
| **exp-008** | `training/run_exp008_binary_probe_penalty.py` | **自定义训练循环**（手写 PyTorch loop，无 Trainer 类） | `L = L_sft - λ_reward * R3 + λ_reward * λ_probe * S(t)`&lt;br>SFT CE loss + frozen binary probe penalty，R3 为预计算常量仅 monitor | **N/A**（无 generation） |
| **exp-002v3** | `training/run_exp002v3_dcgrpo_scaled_cosine.py` | **DCGRPOTrainer**（继承 `trl.GRPOTrainer`），子类 `Exp002v3Trainer` 加了 reward logging | `DCGRPOConfig` 三路 reward：R1=0.4（cosine × scale=5.0），R2=0.0，R3=0.6（NLI） | **2** |
| **exp-003** | `training/run_exp003_r3only.py` | **DCGRPOTrainer**（继承 `trl.GRPOTrainer`） | R1=0.0, R2=0.0, R3=1.0（纯 NLI reward），`direction_path=""` 触发 R3-only fallback | **2** |
| **exp-014** | **服务器上不存在** | — | — | — |

---

### 关键代码摘录

**exp-008** — 自定义 loop，非 Trainer：
```python
# 手写训练循环核心 (run_exp008_binary_probe_penalty.py)
out = model(input_ids=ids, attention_mask=mask, labels=lab, output_hidden_states=True)
sft_loss = out.loss
# probe score S(t): frozen logistic probe on mean hidden states at reward_layers
s_t = torch.stack(probe_vals).mean()
loss = sft_loss - config.lambda_reward * r3_val + config.lambda_reward * config.lambda_probe * s_t
(loss / config.grad_accum).backward()
```

**exp-002v3** — DCGRPOTrainer (trl.GRPOTrainer 子类)：
```python
config = DCGRPOConfig(
    r1_weight=0.4, r2_weight=0.0, r3_weight=0.6,
    r1_scale_factor=5.0,
    num_generations=2,
    ...
)
trainer = Exp002v3Trainer(model=model_path, args=config, ...)
```

**exp-003** — DCGRPOTrainer, R3-only：
```python
config = DCGRPOConfig(
    direction_path="",  # empty → d_syc=None → R3-only
    r1_weight=0.0, r2_weight=0.0, r3_weight=1.0,
    num_generations=2, beta=0.04, temperature=0.7,
    ...
)
trainer = DCGRPOTrainer(model=MODEL_PATH, args=config, ...)
```

**DCGRPOTrainer 基类** (`/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`): 继承 `trl.GRPOTrainer`，override reward 为 R1(direction alignment) + R2(contrastive consistency) + R3(NLI behavioral)。

---

**核心发现：exp-008 是纯 SFT + probe penalty（手写 loop），不是 GRPO。exp-002v3 和 exp-003 都是 GRPO（通过 DCGRPOTrainer）。exp-014 脚本在服务器上不存在。**

---
