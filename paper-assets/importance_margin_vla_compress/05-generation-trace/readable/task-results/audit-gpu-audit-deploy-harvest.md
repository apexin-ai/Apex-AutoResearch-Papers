# audit gpu audit deploy harvest

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_audit_deploy_harvest_20260527T072330_result.json`
- **Structured JSON:** [`61b6bb9b1ae81a61a05e.json`](../../sessions/61/61b6bb9b1ae81a61a05e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 π0.5 实验启动正常（模型加载中）。现在整理完整报告。

---

## Part 1: 全局 GPU 状态表

### westd-27271 (2 GPU)
| GPU | Util | VRAM | PID | 实验 | 进度 |
|-----|------|------|-----|------|------|
| 0 | 73% | 16.0/95.6G | 728571 | eval_openvla_attn_k095_goal_seed42_v2 | Task 5/10 |
| 1 | 71% | 16.0/95.6G | 735728 | eval_openvla_l2norm_k085_object_seed42 | Task 3/10 |

### westd-38929 (4 GPU)
| GPU | Util | VRAM | PID | 实验 | 进度 |
|-----|------|------|-----|------|------|
| 0 | 67% | 16.2/95.6G | 112587 | OV Random k=0.95 Long v2 | Task 2/10 |
| 1 | 67% | 16.0/95.6G | 949447 | eval_openvla_l2norm_k095_long_seed42 | 运行中 |
| 2 | 67% | 16.4/95.6G | 968309 | eval_openvla_l2norm_k075_long_seed42_v2 | 运行中 |
| 3 | 69% | 16.0/95.6G | 950007 | eval_openvla_attn_k095_long_seed42 | 运行中 |

### westd-41074 (4 GPU)
| GPU | Util | VRAM | PID | 实验 | 进度 |
|-----|------|------|-----|------|------|
| 0 | 72% | 16.2/95.6G | 32184 | eval_openvla_random_k095_long_seed42 | Task 7/10 |
| 1 | 39% | 10.7/95.6G | 177597 | eval_pi05_random_k075_long_seed42_strict | Task 6/10 |
| 2 | 🆕 | loading | 262128 | **eval_pi05_random_k095_long_seed42_strict** | 启动中 |
| 3 | 🆕 | loading | 262464 | **eval_pi05_l2norm_k095_long_seed42_strict** | 启动中 |

### cqa1-33015 (4 GPU, 24G each)
| GPU | Util | VRAM | PID | 实验 | 进度 |
|-----|------|------|-----|------|------|
| 0 | 84% | 15.7/24.0G | 896333 | eval_openvla_random_k095_goal_seed42_v2 | Task 10/10 (即将完成) |
| 1 | 51% | 15.7/24.0G | 11249 | OV Attn k=0.95 Goal v2 backup | 未注册备份 |
| 2 | 21% | 10.2/24.0G | 938642 | eval_pi05_attn_k095_long_seed42_strict | 运行中 |
| 3 | 69% | 15.7/24.0G | 897100 | eval_openvla_attn_k05_goal_seed42_v3 | 运行中 |

**总计: 16/16 GPU 全部在用（含 2 个刚部署）**

---

## Part 2: Registry vs 实际差异

| # | 差异 | 详情 |
|---|------|------|
| 1 | **eval_openvla_l2norm_k095_object_seed42** — Registry=RUNNING，实际=进程已死 | 无进程、无 exit 文件。首次运行已成功 SR=70.6% (200 ep)。陈旧 RUNNING 条目，需标记。 |
| 2 | **westd-38929 GPU0** — 有进程但不在 registry | `eval_openvla_random_k095_long_seed42_v2` (pid 112587, Task 2/10)，ROADMAP 标记的备份实验未注册。 |
| 3 | **cqa1 GPU1** — 未注册备份 | OV Attn k=0.95 Goal v2 的第二实例（westd-27271 已有主实例），双保险但未独立追踪。 |
| 4 | **cqa1 GPU0/1 原 π0.5 实验** — 已完成 | 用户提到的 π0.5 Random k=0.5/0.7 strict 已结束，GPU 被 OV Goal 实验接管。 |

---

## Part 3: 收割结果

**eval_openvla_l2norm_k095_object_seed42**: 无新完成实验可收割（进程死但无新结果）。已有首次运行数据 SR=70.6% (200 ep)。建议直接采用此结果标记 DONE。

其余 11 个 RUNNING 实验均有活进程在跑，尚未完成。cqa1 GPU0 的 `eval_openvla_random_k095_goal_seed42_v2` 在 Task 10/10，预计 1-2h 内完成。

---

## Part 4: westd-41074 GPU2/3 部署结果

原计划 OV Goal backup **失败** — `openvla-libero-goal` 缺少 `model-00001-of-00004.safetensors`（shards 2-4 存在，shard 1 缺失）。

替代部署成功：
| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| 2 | eval_pi05_random_k095_long_seed42_strict | 262128 | π0.5 Random k=0.95 strict，补全 curve 顶端 |
| 3 | eval_pi05_l2norm_k095_long_seed42_strict | 262464 | π0.5 L2norm k=0.95 strict，首个 L2norm strict 实验 |

两个实验均已确认启动成功（模型加载中）。预计运行 4-5h。

---

## Part 5: 发现 & 建议

1. **westd-41074 Goal 模型不完整** — 如果后续需要在 westd-41074 跑 Goal 实验，需补下载 `model-00001-of-00004.safetensors`（~5GB）。
2. **westd-38929 GPU0 备份未注册** — `eval_openvla_random_k095_long_seed42_v2` 应补注册到 registry。
3. **cqa1 GPU0 即将释放** — `eval_openvla_random_k095_goal_seed42_v2` 在 Task 10/10，完成后 GPU0 可复用。
4. **无空闲 GPU** — 所有 16 张卡均已填满。

---
