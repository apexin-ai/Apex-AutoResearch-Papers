# gpu check and deploy supp

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_check-and-deploy-supp_20260528T155015_result.json`
- **Structured JSON:** [`6fb8856ac269263ef99c.json`](../../sessions/6f/6fb8856ac269263ef99c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| 服务器 | GPU 数 | 状态 | 备注 |
|--------|--------|------|------|
| bjb1-18228 | 1× RTX 4090 | **空闲** (0 MiB / 24564 MiB, 0%) | 无残留 python 进程 |
| bjb1-32546 | 6× GPU | **连接失败** | `Unable to connect to port 32546` |
| bjb2-28827 | 6× GPU | **连接失败** | `Unable to connect to port 28827` |
| cqa1-32758 | 6× GPU | **连接失败** | `Unable to connect to port 32758` |

**严重问题：3/4 服务器不可达，22 GPU 中只有 1 GPU 可用。** AutoDL 实例可能已关机或端口已变。需要去 AutoDL 控制台确认实例状态并获取新端口。

此外 bjb1-18228 只显示 1 块 GPU（配置说 cuda:0-3 共 4 卡），可能也已重建。

Registry 确认 RUNNING 实验数为 0，所有实验已清理。

---

## 数据缺口（来自 supplementary_summary.md Section F）

| 类型 | 缺口描述 | 优先级 |
|------|----------|--------|
| Bonus seeds / long / adaptive_conformal | **无有效 SR**（s42/s45/s46 均为 None） | **P0** — 主方法 long 无补充数据 |
| Bonus seeds / object / adaptive_conformal | 仅 1 个有效 seed (s42) | **P0** — 主方法 object 补充不足 |
| Bonus seeds / object / crm_obs_only | 仅 1 个有效 seed (s46) | P1 |
| Bonus seeds / long / crm_obs_only | 仅 1 个有效 seed (s46) | P1 |
| Bonus seeds / goal / reconvla | 仅 2 个有效 seed (s46, s47) | P1 |
| Bonus seeds / long / reconvla | 仅 2 个有效 seed (s45, s46) | P1 |
| Pi05 / long / crm_obs_only | 仅 1 个 seed (s44) | P2 |
| Pi05 tau-sweep | 多为单 seed (s42)，multi-seed 覆盖仅 tau=0.25 | P2 |
| CRM always-on / smolvla / long s45 | SR 为 None | P2 |

---

## 部署建议

**当前只有 bjb1-18228 的 1 块 GPU 可用。** DDL 20:00 BJ，每个实验约 30-40 分钟，最多再跑 ~10-12 个实验。

如果只有 1 GPU 可用，建议优先级排序：

| 优先级 | 实验 | 服务器:GPU | 预估时长 |
|--------|------|-----------|----------|
| 1 | eval-supp-long-adapt-tau025-s43 | bjb1-18228:0 | ~35min |
| 2 | eval-supp-long-adapt-tau025-s44 | bjb1-18228:0 | ~35min |
| 3 | eval-supp-obj-adapt-tau025-s43 | bjb1-18228:0 | ~35min |
| 4 | eval-supp-obj-adapt-tau025-s44 | bjb1-18228:0 | ~35min |
| ... | 后续按 P1 缺口排 | — | — |

**但真正的瓶颈是服务器不可达。** 建议：
1. **立即去 AutoDL 控制台检查 bjb1-32546 / bjb2-28827 / cqa1-32758 实例状态**，如果已关机则开机，如果端口变了请更新 `~/.ssh/config`
2. 恢复后 22 GPU 全开可在 DDL 前批量补齐上述缺口
3. bjb1-18228 如果确实只有 1 卡，立即开始跑 P0 缺口实验（long/adaptive 和 object/adaptive）

等待指示。

---
