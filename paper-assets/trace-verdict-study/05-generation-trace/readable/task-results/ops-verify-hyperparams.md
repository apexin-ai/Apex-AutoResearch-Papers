# ops verify hyperparams

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_hyperparams_20260516T042920_result.json`
- **Structured JSON:** [`9738f5fb1b77e32ac905.json`](../../sessions/97/9738f5fb1b77e32ac905.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部参数已验证完毕。汇总如下：

---

## 四个冲突参数的真实值

| 参数 | 论文 Appendix | Checklist | **实际值（代码+checkpoint）** | 匹配 |
|------|-------------|-----------|-------------------------------|------|
| Warmup ratio | 0.1 | 0.03 | **0.1** | **Appendix ✓** |
| LR scheduler | linear decay | cosine | **linear** | **Appendix ✓** |
| Gradient accum. | 8 | 1 | **8** | **Appendix ✓** |
| GPU | 1× RTX PRO 6000 (94GB) | 2× consumer GPUs (~48GB) | **2× RTX PRO 6000 Blackwell Server Edition (96GB)，代码 `device_map={"": 0}` 只用 1 块** | **Appendix 接近**，但显存应为 ~96GB 非 94GB |

**结论：4 个冲突全部以 Appendix 为准，Checklist 值全部错误。**

---

## 完整超参数清单

| 参数 | 代码默认值 | 运行时实际值 |
|------|-----------|-------------|
| learning_rate | 2e-4 | 2e-4 |
| lr_scheduler_type | 未设置（default=linear） | **linear** |
| warmup_ratio | 0.1 | 0.1 |
| gradient_accumulation_steps | 8 | 8 |
| per_device_train_batch_size | 4 | 4 |
| num_train_epochs | 3 | 3 |
| max_length | 2048 | 2048 |
| bf16 | True | True |
| fp16 | — | False |
| weight_decay | 0.01 | 0.01 |
| optimizer | 未设置 | **adamw_torch_fused** |
| gradient_checkpointing | False（需显式传入） | **True**（运行时开启） |
| seed | 42 | 42 |
| **lora_r** | 16 | 16 |
| **lora_alpha** | 32 | 32 |
| **lora_dropout** | 0.05 | 0.05 |
| **target_modules** | q/k/v/o/gate/up/down_proj | q/k/v/o/gate/up/down_proj |
| GPU 使用 | `device_map={"": 0}`（单卡） | 1× RTX PRO 6000 (~96GB) |

---
