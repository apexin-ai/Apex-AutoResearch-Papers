# infra audit all servers deploy spatial adapt s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_audit-all-servers-deploy-spatial-adapt-s45_20260523T231720_result.json`
- **Structured JSON:** [`e55db63ca946a454d121.json`](../../sessions/e5/e55db63ca946a454d121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Spec 已更新。registry 状态机限制，DEPLOYED 无法回到 RUNNING，但关键信息（server=cqa1-32758, cuda:4, PID=502821）已记录，cron 也已存在。

---

## 审计结果

### 1. GPU 利用率

| 服务器 | GPU | Util | Mem | 实验/任务 |
|--------|-----|------|-----|-----------|
| **bjb1-32546** | 0 | 0% | 2/24564 MiB | **空闲** |
| | 1 | 22% | 2322 MiB | eval-long-vla-s45 |
| | 2 | 23% | 2329 MiB | eval-long-adapt-s45 |
| | 3 | 29% | 2423 MiB | eval-long-crm-s45 |
| | 4 | 34% | 3083 MiB | eval-long-reconvla-s45 |
| | 5 | 31% | 4764 MiB | eval-reconvla-obj-s45 |
| **bjb2-28827** | 0-5 | 18-25% | 3.4-5.6 GB | 6 goal-s46 + long-k2mean-s45 |
| **bjb2-40593** | 0 | 13% | 5942 MiB | eval-spatial-k2mean-s45 |
| **cqa1-32758** | 0-5 | 14-29% | 3.1-5.4 GB | 5 spatial/obj-s45 + goal-k2mean-s45 + **spatial-adapt-s45 (cuda:4)** |
| **bjb1-18228** | 0-3 | 21-25% | ~9.9 GB ea | 4× π0.5 precompute (obj/spatial/goal/long) |

### 2. Spatial Adapt s45

**不需要重新部署。** 实验已在 cqa1-32758 cuda:4 上运行（PID 502821, tmux: `eval-supp-spatial-adapt-tau025-s45`），产出正常（95-100% success rate）。之前在 bjb2-40593 被 killed 后已有人在 cqa1-32758 上重启。Registry spec 已更新为新位置，cron 已存在。

### 3. Cron 注册（8/8 成功）

| 实验 | 服务器 | tmux session |
|------|--------|-------------|
| eval-supp-goal-adapt-tau025-s46 | bjb2-28827 | eval-goal-adapt-s46 |
| eval-supp-goal-crm-norm005-s46 | bjb2-28827 | eval-goal-crm-s46 |
| eval-supp-goal-reconvla-s46 | bjb2-28827 | eval-supp-goal-reconvla-s46 |
| eval-supp-goal-k2mean-s46 | bjb2-28827 | eval-goal-k2mean-s46 |
| eval-supp-goal-vla-only-s46 | bjb2-28827 | eval-supp-goal-vla-only-s46 |
| eval-supp-obj-k2mean-s45 | cqa1-32758 | eval-obj-k2mean-s45 |
| eval-supp-reconvla-obj-s45 | bjb1-32546 | eval-reconvla-obj-s45 |
| eval-supp-spatial-k2mean-s45 | bjb2-40593 | eval-spatial-k2mean-s45 |

### 4. 空闲 GPU

仅 **bjb1-32546 cuda:0**（0% util, 2 MiB）。其余 22 个 GPU 全部在用（17 eval + 4 precompute + 1 spatial-k2mean on bjb2-40593）。

### 5. 注意事项
- `eval-supp-spatial-adapt-tau025-s45` registry 状态卡在 DEPLOYED（状态机不允许 DONE→RUNNING），conclusion 仍为 "killed"，但 spec 已更新为 cqa1-32758 实际位置。当实验完成时 cron 应能正确检测并更新。
- bjb1-18228 的 4 个 π0.5 precompute 使用 nohup 而非 tmux，无 tmux session。

---
