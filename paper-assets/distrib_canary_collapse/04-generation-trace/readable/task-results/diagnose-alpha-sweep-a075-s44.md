# diagnose alpha sweep a075 s44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha_sweep_a075_s44_20260516T141402_result.json`
- **Structured JSON:** [`66e1d76146cf1e1bc586.json`](../../sessions/66/66e1d76146cf1e1bc586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：实验实际上**成功完成**，未失败

| 项目 | 结果 |
|------|------|
| **EXIT_CODE** | **0**（成功），不是 1 |
| **完成度** | 全部 11 代（gen_0 ~ gen_10）完成，与 config 的 `num_generations: 10` 一致 |
| **运行时长** | ~4h14m（17:58 → 22:12） |
| **metrics** | `all_metrics.json` 包含完整 11 代指标 |
| **Error/Traceback** | 日志中**无任何 error、traceback、exception** |
| **磁盘** | 57G/250G（23%），正常 |
| **W&B** | 日志中**零 wandb 引用** — 该实验脚本未配置 W&B 日志记录 |

### 关于"无有效 W&B metrics"

config.json 中没有 wandb 相关配置，脚本运行时也未初始化 wandb。所以不是 W&B 上报失败，而是**这个实验从未打算上报 W&B**。metrics 全部保存在本地 `all_metrics.json`。

### 末代指标（gen_10）

```
perplexity=76.35, token_entropy=2.336, eff_rank=77.8, mauve=0.029
distinct_1=0.067, distinct_2=0.309, distinct_3=0.508, ece=0.206
```

可以看到随代际递增的 collapse 趋势：perplexity 从 26.9（gen_0）涨到 76.4（gen_10），distinct_1/2/3 持续下降，mauve 始终很低（~0.03）。数据本身是符合预期的 canary collapse pattern。

**结论：无需重跑，也无需修代码。** 如果需要 W&B 记录，需在启动脚本中添加 wandb 初始化。

---
