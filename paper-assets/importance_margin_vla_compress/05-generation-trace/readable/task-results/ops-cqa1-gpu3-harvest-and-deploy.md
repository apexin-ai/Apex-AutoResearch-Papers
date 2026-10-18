# ops cqa1 gpu3 harvest and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-gpu3-harvest-and-deploy_20260527T140859_result.json`
- **Structured JSON:** [`4a9db7292e816444c8ce.json`](../../sessions/4a/4a9db7292e816444c8ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型还在 CPU 上加载（pi05 加载需要几分钟），GPU3 显存尚未上升，属正常。PID=386857 进程已确认运行中。

---

**收割结果：L2norm k=0.9 seed42 strict**
| 指标 | 值 |
|------|-----|
| Overall SR | **80.0%** (400/500) |
| T0 alphabet_soup_tomato | 96% |
| T1 cream_cheese_butter | 96% |
| T2 stove_moka | 94% |
| T3 black_bowl_drawer | 100% |
| T4 mugs_plates | 82% |
| T5 book_caddy | 96% |
| T6 mug_plate_pudding | 6% |
| T7 alphabet_soup_cream_cheese | 92% |
| T8 two_moka_pots | 44% |
| T9 mug_microwave | 94% |
| Elapsed | 209.7 min |

对比 lenient 版本（80.2%, 401/500），strict 仅下降 0.2pp（1 fewer success），差异极小。

**新实验部署：L2norm k=0.9 seed43 strict**
- Server: cqa1-33015 GPU3
- PID: 386857
- Log: `logs/eval_pi05_l2norm_k09_long_seed43_strict_cqa1.log`
- Registry: `eval_pi05_l2norm_k09_long_seed43_strict_cqa1` → RUNNING
- 预计完成：~3.5h（约 01:45 UTC）

---
