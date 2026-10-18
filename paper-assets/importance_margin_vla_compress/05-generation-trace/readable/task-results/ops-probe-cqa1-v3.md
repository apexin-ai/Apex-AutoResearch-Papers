# ops probe cqa1 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_probe_cqa1_v3_20260522T060209_result.json`
- **Structured JSON:** [`32612f2205df30413c87.json`](../../sessions/32/32612f2205df30413c87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集。结果如下：

```
hostname: autodl-container-61bb4e82b9-0e2cbbac (确认是 cqa1-33015，非 westd-27271)
GPU 数量: 4 × 24GB

| GPU | 利用率 | 显存        | 实验                                          | PID  | 状态    |
|-----|--------|-------------|-----------------------------------------------|------|---------|
| 0   | 18%    | 10367/24564 | eval_pi05_pruning random k=0.925 spatial s43   | 5786 | RUNNING |
| 1   | 27%    | 10363/24564 | eval_pi05_pruning random k=0.9 spatial s43     | 5866 | RUNNING |
| 2   | 14%    | 10373/24564 | eval_pi05_pruning l2norm k=0.95 spatial s43    | 5943 | RUNNING |
| 3   | 17%    | 10363/24564 | eval_pi05_pruning l2norm k=0.9 spatial s43     | 6087 | RUNNING |

空闲 GPU: 无（4/4 全部占用）
```

**与 Registry 不一致**：Registry 记录的两个实验（`eval_smolvla_official_l2norm_k090_object_seed42` GPU 0、`eval_smart_compress_m32_official` GPU 3）与实际运行的进程完全不同。实际跑的是 4 个 Pi0.5 pruning 评估（random/l2norm × 不同 keep_ratio），全部在 libero_spatial、seed 43。Registry 需要更新。

---
