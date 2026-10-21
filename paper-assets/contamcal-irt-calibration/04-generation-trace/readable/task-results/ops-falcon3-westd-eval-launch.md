# ops falcon3 westd eval launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-westd-eval-launch_20260522T110144_result.json`
- **Structured JSON:** [`5d38188b7a5143e96ba7.json`](../../sessions/5d/5d38188b7a5143e96ba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. GPU 状态
| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 0 / 97887 MiB | 0% | 空闲 → eval d000 |
| cuda:1 | 0 / 97887 MiB | 0% | 空闲 → eval d005 |
| cuda:2 | 0 / 97887 MiB | 0% | 空闲 → eval d025 |
| cuda:3 | 55019 / 97887 MiB | 99% | d050 训练中 |

### 2. 训练结果
| Dosage | 状态 | Steps | Train Loss | Epoch | lora_alpha |
|--------|------|-------|-----------|-------|------------|
| d000 | **成功** | 3125 | 1.057 | 1.0 | 32 ✓ |
| d005 | **成功** | 3177 | 1.060 | 1.0 | 32 ✓ |
| d025 | **成功** | 3384 | 1.062 | 1.0 | 32 ✓ |

三个 adapter 均有 `adapter_model.safetensors` (169MB)，训练时长均约 2h50m。

### 3. Eval 提交
| exp_id | GPU | PID | tmux session |
|--------|-----|-----|-------------|
| eval_falcon3_d000_s42 | cuda:0 | 618603 | eval_falcon3_d000_s42 |
| eval_falcon3_d005_s42 | cuda:1 | 618759 | eval_falcon3_d005_s42 |
| eval_falcon3_d025_s42 | cuda:2 | 618913 | eval_falcon3_d025_s42 |

### 4. d050 进度
- **3073/3642 steps (84%)**, epoch 0.79, elapsed 3h11m
- 预计剩余 ~40min（~3.6s/step × 569 steps）
- loss=1.056, lr=5.77e-6（仍在余弦衰减中段）

### 5. C009 注意
evaluate.py 当前 37775 bytes，reference 为 37591 bytes。版本不一致，请确认是否为已知更新。

---
