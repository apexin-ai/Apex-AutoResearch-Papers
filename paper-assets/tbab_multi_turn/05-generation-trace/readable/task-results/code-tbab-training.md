# code tbab training

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tbab-training_20260518T064913_result.json`
- **Structured JSON:** [`ec50587df68656e850d8.json`](../../sessions/ec/ec50587df68656e850d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。验证结果汇总：

| Condition | 配置 | train_loss (5 steps) | 运行时间 | 状态 |
|---|---|---|---|---|
| C1: LoRA-only | bridge=F, reset=F | 0.7314 | 66.5s | OK |
| C2: Position-reset | bridge=F, reset=T | 2.244 | 59.5s | OK |
| C3: Bridge+standard | bridge=T, reset=F | 0.7321 | 61.9s | OK |
| C4: Full TBAB | bridge=T, reset=T | 2.244 | 62.1s | OK |

关键验证点：
- **Position reset**: 在每个 turn boundary 处 position 正确重置为 0，bridge tokens 占 pos=[0,1,2,3]，内容从 pos=4 开始
- **Bridge tokens**: IDs [32000-32003] 正确插入在 `&lt;/s>` 之后，labels=-100
- **4D causal mask**: C2/C4 使用 4D mask (`needs_4d_mask=True`)，C1/C3 使用 2D mask
- **Trainable params**: C1/C2 = 83.9M (1.15%)，C3/C4 = 346M (4.72%) — bridge embedding 行可训练
- **Loss 合理**: C1/C3（无 position reset）~0.73，C2/C4（有 position reset）~2.24 — position reset 改变了注意力模式，初始 loss 更高符合预期

代码部署在 `westd-29046:/root/tbab_multi_turn/scripts/`，4 个 YAML config 在 `configs/` 子目录。正式训练命令示例：
```bash
CUDA_VISIBLE_DEVICES=0,1 python3 train.py --config configs/condition4_full_tbab.yaml --seed 42
```

---
