# diagnose m32 m64 seed44 completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m32_m64_seed44_completion_20260519T081438_result.json`
- **Structured JSON:** [`e5d35f681e6b2ab49c7d.json`](../../sessions/e5/e5d35f681e6b2ab49c7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**训练状态（全部完成）：**
| 实验 | 最终 step | 最终 loss | checkpoint |
|---|---|---|---|
| M=32 seed44 | 99999/100000 | 0.0415 | ✅ 1.59GB |
| M=64 seed44 | 100000/100000 | 0.0310 | ✅ 1.59GB |
| M=96 seed44 | 已确认完成 | — | ✅ 1.59GB |

**Registry 更新：** M=32/M=64 → ANALYZING，cron 已删除。

**Eval 启动（全部正常运行）：**
| eval | GPU | PID | 状态 |
|---|---|---|---|
| eval_smart_compress_m32_seed44 | cuda:0 | 762596 | ✅ 已在跑 episodes |
| eval_smart_compress_m64_seed44 | cuda:1 | 763351 | ✅ 已在跑 episodes |
| eval_smart_compress_m96_seed44 | cuda:2 | 764777 | ✅ 已在跑 episodes |

参数：`eval_smart_compress_libero.py --n_queries {M} --suite libero_object --num_episodes 500 --seed 44`。注意 eval 脚本用 `--n_queries` 和 `--checkpoint_path`（不是任务描述中的 `--checkpoint`）。500 episodes 预计需要约 3-4 小时。

---
