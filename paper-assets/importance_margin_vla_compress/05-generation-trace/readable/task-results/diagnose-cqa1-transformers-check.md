# diagnose cqa1 transformers check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_transformers_check_20260526T061749_result.json`
- **Structured JSON:** [`b947b142ac1a0a374290.json`](../../sessions/b9/b947b142ac1a0a374290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**transformers = 5.5.3** — 确认是不兼容版本（会导致 OpenVLA 产出 0% SR 垃圾数据）。

**但 GPU 2/3 跑的不是 OpenVLA，而是 π0.5 实验**，不受 transformers 版本影响，无需干预：

| GPU | PID | tmux session | 实验 |
|-----|-----|-------------|------|
| 0 | 3728 | `eval_pi05_random_k075_long_seed42_v2` | π0.5 random k=0.75, libero_10 |
| 1 | 3874 | `eval_pi05_attention_k075_long_seed42` | π0.5 attention k=0.75, libero_10 |
| 2 | 77661 | `eval_pi05_l2norm_k05_long_seed42` | π0.5 l2norm k=0.5, libero_10 |
| 3 | 77832 | `eval_pi05_random_k05_long_seed42` | π0.5 random k=0.5, libero_10 |

**处理结论**：四张卡全部在跑 π0.5 eval，没有 OpenVLA 进程。π0.5 不受 transformers 5.5.3 影响，全部让它们继续跑。无需 kill，无需部署新实验。

不过 cqa1 上 transformers 5.5.3 意味着**这台机器不能跑 OpenVLA**，后续如果要在 cqa1 上跑 OpenVLA 必须先降级 transformers。

---
