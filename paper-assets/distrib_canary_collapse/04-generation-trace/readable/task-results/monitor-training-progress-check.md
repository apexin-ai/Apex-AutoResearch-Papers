# monitor training progress check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_check_20260516T012122_result.json`
- **Structured JSON:** [`79cd790e81950cfc6fca.json`](../../sessions/79/79cd790e81950cfc6fca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Here's the summary:

```
实验: gen_wiki_gpt2m_a025_s42
PID: 149202 状态: running (已运行 2h59m)
进度: 3/10 gen (Gen 3 训练中, step 4100/5000 = 82%)
最新输出: {'loss': 1.9139, 'grad_norm': 1.194, 'learning_rate': 1.001e-05, 'epoch': 6.56}
速度: 2.06 it/s (~40min/gen 训练 + 生成开销 ≈ 47min/cycle)
预估剩余: ~5.5h (finish gen3 ~8min + gen4-9 × ~47min)

实验: alpha_sweep_a025_s44
PID: 147811 状态: running (已运行 3h17m)
进度: 8/10 gen (Gen 8 训练完成, 正在生成 Gen 9 合成数据)
最新输出: {'train_loss': 2.2696, 'train_runtime': 314.95s, 'epoch': 1.0} (gen8 训练结束)
速度: 15.9 it/s (~5min/gen 训练, ~22min/cycle 含生成)
预估剩余: ~45min (gen9 + gen10 各 ~22min, 但 gen9 生成阶段已开始)
```

alpha_sweep 快完成了；GPT-2m 因为模型更大 (medium vs Pythia-410m)，训练速度慢 ~8x，还需要较长时间。

---
