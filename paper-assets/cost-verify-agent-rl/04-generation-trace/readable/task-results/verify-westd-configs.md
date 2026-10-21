# verify westd configs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_westd_configs_20260521T074057_result.json`
- **Structured JSON:** [`6d8b61886d37dc8d3003.json`](../../sessions/6d/6d8b61886d37dc8d3003.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 磁盘状态

| 分区 | 清理前 | 清理后 | 变化 |
|------|--------|--------|------|
| `/root/autodl-tmp/` (250G) | 184G used / 67G avail (74%) | 129G used / 122G avail (52%) | **释放 55G** |
| `/` (30G) | 14G used / 17G avail (46%) | 14G used / 17G avail (46%) | 无变化 |

清理内容：seed6 三个 checkpoint（5/10/15，共 ~56G）+ pip cache + tmp。

### 配置验证

| 参数 | Seed 5 | Seed 6 |
|------|--------|--------|
| save_freq | **5** ✓ | **5** ✓ |
| optimizer_offload | **false** | **false** |
| seed.train | **456** | **789** |
| 配置路径 | `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed5_episode.yaml` | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed6_episode.yaml` |

### GPU 状态

4× NVIDIA RTX PRO 6000 (96GB each) — **全部空闲**，0MiB 显存占用，0% 利用率。

### Seed 5 残留

无 `/root/autodl-tmp/checkpoints/exp029-seed5/` 目录，无需清理。

---
