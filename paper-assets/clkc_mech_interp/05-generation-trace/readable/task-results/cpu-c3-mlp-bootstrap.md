# cpu c3 mlp bootstrap

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_c3-mlp-bootstrap_20260522T080853_result.json`
- **Structured JSON:** [`fd7ff8e0d41c20485eea.json`](../../sessions/fd/fd7ff8e0d41c20485eea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程在 20 分钟内完成了 ~400/1000 iterations（第一个 condition），服务器严重负载（其他 train_probe.py 占用 550% CPU）。

**当前状态**：
- 脚本 `src/bootstrap_mlp_delta.py` 在 westd-41302 后台运行 (PID 464607)
- 日志: `logs/c3_mlp_bootstrap.log`
- 结果会写入: `data/c3_mlp_bootstrap_results.json`（每个 condition 完成后增量保存）
- 预估总运行时间: **~2-3 小时**（服务器负载高）

**已有中间结果** (qwen3_conflict, 400 iterations):
- mean delta = **+0.039** (MLP bal_acc - Linear bal_acc)
- Linear EN→ZH: ~0.600, MLP EN→ZH: ~0.639
- Delta 非常稳定，一直为正值

从趋势看，conflict 的 CI 应该会清楚地排除 0（MLP gain 显著）。XNLI 的结果需要等脚本跑完。

4 个 conditions 配置:

| Condition | Peak Layer | EN Train | ZH Test |
|-----------|-----------|----------|---------|
| qwen3_conflict | 23 | 798 | 168 |
| llama31_conflict | 5 | 1096 | 272 |
| qwen3_xnli | 22 | 800 | 200 |
| llama31_xnli | 17 | 800 | 200 |

进程已经在后台稳定运行，完成后 `data/c3_mlp_bootstrap_results.json` 会包含所有 4 个 condition 的 95% CI。可以后续用 `cat data/c3_mlp_bootstrap_results.json` 查看最终结果。

---
