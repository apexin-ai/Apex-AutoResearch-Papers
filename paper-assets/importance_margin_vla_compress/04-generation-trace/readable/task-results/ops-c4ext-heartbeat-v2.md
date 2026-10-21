# ops c4ext heartbeat v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4ext_heartbeat_v2_20260519T204639_result.json`
- **Structured JSON:** [`3bce1d7f34966a66600f.json`](../../sessions/3b/3bce1d7f34966a66600f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 心跳汇报

### westd-41074 (4× H800 97GB)

| GPU | 利用率 | VRAM | PID | 实验 | 状态 |
|-----|--------|------|-----|------|------|
| 0 | 99% | 30.1/97.9 GB | 26118 | ? | **异常** — 无匹配活跃日志 |
| 1 | 99% | 48.1/97.9 GB | 43111 | ? | **异常** — 无匹配活跃日志 |
| 2 | 0% | 0 GB | — | — | 空闲 |
| 3 | 0% | 0 GB | — | — | 空闲 |

**问题**：GPU 0/1 满载运行，但最近的日志：
- `train_openvla_vtc_m128_seed42.log` 停在 02:28 "Computing action statistics..."（2h+ 无更新）
- `train_openvla_sc_m128_lora_seed42.log` 被 SIGTERM 终止于 step 1183 (03:27)

日志和进程不匹配，可能训练输出到了 stdout/nohup.out 而不是 log 文件，或者是新启动的未知进程。

---

### westd-27271 (2× H800 97GB)

| GPU | 利用率 | VRAM | PID | 实验 | 状态 |
|-----|--------|------|-----|------|------|
| 0 | 5% | 32.3/97.9 GB | 841334 | ? | **可疑** — 5% 利用率 + 32GB VRAM |
| 1 | 0% | 0 GB | — | — | 空闲 |

**问题**：GPU 0 占了 32GB 显存但利用率仅 5%。今天没有新日志，昨天最新的是 `eval_mlp_adapter_control.log` (May 19 20:33)。可能是个闲置/卡死的进程。

---

### cqa1-33015 (4× RTX 4090 24GB)

| GPU | 利用率 | VRAM | PID | 实验 | Step | Loss | 状态 |
|-----|--------|------|-----|------|------|------|------|
| 0 | 40% | 2.8/24.6 GB | 678106 | m128_seed43 | 77800/100k | 0.038 | 正常 |
| 1 | 0% | 2.9/24.6 GB | 649697 | m16_seed43 | 77450/100k | 0.038 | 正常 |
| 2 | 18% | 2.8/24.6 GB | 649845 | m16_seed44_v3 | 54000/100k | 0.066 | 正常 |
| 3 | 0% | 3.0/24.6 GB | 685415 | eval m32_seed44 | Ep 380/500 | — | 正常 |

全部健康，空闲 GPU：无。

---

### 总结

- **cqa1-33015**：4/4 GPU 全部正常运行，无异常
- **westd-41074**：GPU 0/1 有活跃进程但日志不匹配，需确认实际在跑什么；GPU 2/3 空闲
- **westd-27271**：GPU 0 疑似卡死进程（5% util, 32GB VRAM, 无今日日志）；GPU 1 空闲

---
