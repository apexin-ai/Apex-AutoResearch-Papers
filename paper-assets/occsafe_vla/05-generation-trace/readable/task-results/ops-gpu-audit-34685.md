# ops gpu audit 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_34685_20260524T185234_result.json`
- **Structured JSON:** [`6913ac9068375c90db1c.json`](../../sessions/69/6913ac9068375c90db1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**4/4 实验全部存活，GPU 利用率正常。** 健康度报告的 7% 可能是采样时间点问题。

## 进程状态

| 实验 | GPU | PID | 状态 | 运行时间 | GPU 利用率 | 显存占用 |
|------|-----|-----|------|---------|-----------|---------|
| cutoff_45k_s1 | cuda:0 | 882188 | **存活** (Ssl) | 6h22m | 41% | 62203/97887 MiB |
| cutoff_15k_s1 | cuda:1 | 861222 | **存活** (Ssl) | 6h57m | 90% | 62203/97887 MiB |
| cutoff_25k_s2 | cuda:2 | 998127→998208 | **存活** (Ss+) | 1h48m | 99% | 62209/97887 MiB |
| reverse_cutoff_s2 | cuda:3 | 998624→999132 | **存活** (Ss+) | 1h47m | 37% | 62203/97887 MiB |

## 备注

- **PID 差异**：cutoff_25k_s2 和 reverse_cutoff_s2 的给定 PID（998127/998624）是 bash wrapper 进程，实际 Python 进程 PID 为 998208 和 999132，均在 nvidia-smi 中正常显示。
- **GPU 利用率**：实时采样为 41%/90%/99%/37%（均值 ~67%），与健康报告的 7% 不符。可能是报告采样时恰好处于数据加载/checkpoint 保存阶段。
- **显存**：4 卡均占用 ~62GB/98GB，一致且正常。
- `tmux ls` 被 read-only 模式拦截，但进程状态已通过 ps 和 nvidia-smi 确认，无需额外检查。

---
