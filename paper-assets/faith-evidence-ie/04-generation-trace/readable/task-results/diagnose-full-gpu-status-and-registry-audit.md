# diagnose full gpu status and registry audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_gpu_status_and_registry_audit_20260519T031518_result.json`
- **Structured JSON:** [`2e3dcee441e38cb88672.json`](../../sessions/2e/2e3dcee441e38cb88672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry fixed. Here's the full report:

---

## GPU 全卡状态

| GPU | 显存 | PID | 实验 | Registry |
|-----|------|-----|------|----------|
| **0** | **0 MiB (空闲)** | — | — | — |
| 1 | 27524 / 32607 MiB (84%), util 99% | 602749 | `plan019_1_7b_rsft_s44` — 1.7B RSFT s44 训练 | ✅ RUNNING |
| 2 | 29110 / 32607 MiB (89%), util 69% | 601718 | `plan019_1_7b_rsft_s43` — 1.7B RSFT s43 训练 | ✅ RUNNING |
| 3 | 18882 / 32607 MiB (58%), util 69% | 598911 | `plan019_8b_rsft_s44_eval` — 8B RSFT s44 eval | ✅ RUNNING |
| CPU | 无 GPU 占用 | 603844 | `d112_rsft_s44_ced_score` — D112 step 2 CED scoring | ❌ 无条目 + **卡死** |

## Registry 审计结果

| 条目 | 问题 | 修复 |
|------|------|------|
| `d112_rsft_s44_gen_shard3` (PID 590568) | 进程不存在，registry 仍 RUNNING | ✅ 已更新为 DONE (success) |
| `d112_rsft_s44_ced_score` (PID 603844) | 有进程无 registry | ⏸️ 暂不创建——进程已卡死需重启 |
| 其余 3 个 RUNNING 条目 | PID/GPU 均匹配 | ✅ 无需修复 |

## cuda:1 状态

**Director 报告有误：cuda:1 不空闲。** PID 602749 (1.7B RSFT s44) 正在 cuda:1 上跑，27524 MiB，GPU 利用率 99%。

**cuda:0 才是空闲卡。**

## D112 Step 2 — 严重阻塞

PID 603844 (`d112_rsft_s44_ced_score`) **卡死**：
- 加载 NLI 模型 `cross-encoder/nli-deberta-v3-base` 时尝试连接 HuggingFace，网络不可达
- 5 次重试全部失败，log 从 11:13:58 起冻结（3+ 分钟无输出）
- 无 GPU 显存占用，输出目录为空

**模型已缓存在本地** `/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/`，但脚本未设离线模式。

**修复方案：** kill PID 603844，在脚本中加 `export HF_HUB_OFFLINE=1` 后重新启动，强制使用本地缓存。是否执行？

---
