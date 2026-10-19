# scan d139 seed status all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_d139-seed-status-all-servers_20260524T192909_result.json`
- **Structured JSON:** [`f00f34a11e7ac5976432.json`](../../sessions/f0/f00f34a11e7ac5976432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已落盘并注册（artifact id `art_20260524_336b39`，路径 `projects/acr-vla-conformal-refinement/artifacts/_project/report/d139_status_scan.md`）。

## 核心结论

**1. D139 种子扩展（12 实验）→ 100% 完成**
- 6 adaptive + 6 vla_only，跨 object/spatial/goal × s48/s49
- adaptive vs vla_only Δ：object/goal 微负差（-0.005~-0.030），spatial 正差（+0.015, +0.035）
- trigger_rate：object 4%, goal 9%, spatial 20%

**2. τ-sweep（spatial s42）→ 6/6 完成**
| τ | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | 0.35 |
|---|------|------|------|------|------|------|
| SR | 0.790 | 0.805 | 0.810 | 0.795 | 0.805 | 0.800 |
| trig | 0.752 | 0.407 | 0.266 | 0.197 | 0.167 | 0.122 |

SR 平坦，trigger_rate 随 τ 单调下降。

**3. K-sweep**
- K=1 spatial s42 done: SR=0.795, trig=0.1965
- K=5 spatial s42 在 bjb2-40593 GPU 0 进行中，2h33min elapsed，6/10 task 完成

**4. π0.5 CRM 训练（bjb1-18228 GPU 0）**
- Epoch **25/50**，elapsed 8h51m
- Best val_loss = **0.004854 @ epoch 24**（持续小幅下降）
- ETA ~9h，但 timeout 剩余预算 ~3h 不足 — **需决定是否续期**

**5. 空闲 GPU：17 张**
- cqa1-32758: 6 张全空
- bjb1-32546: 5 张
- bjb2-28827: 4 张
- bjb1-18228: 2 张

**注意事项**：bjb1-18228 上 PID 114507（May 23 启动的 pi05 precompute）疑似僵尸，17 GB RES，需要确认后清理。

---
