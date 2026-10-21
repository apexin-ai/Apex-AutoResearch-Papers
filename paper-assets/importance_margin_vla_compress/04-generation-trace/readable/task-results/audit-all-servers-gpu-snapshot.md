# audit all servers gpu snapshot

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_all_servers_gpu_snapshot_20260524T234946_result.json`
- **Structured JSON:** [`1cc94592728375d0f6db.json`](../../sessions/1c/1cc94592728375d0f6db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总结果：

---

## 交叉对比结果

### Registry RUNNING 实验（13 个）

| # | 实验 | 服务器 | GPU | Registry PID |
|---|------|--------|-----|-------------|
| 1 | eval_openvla_l2norm_k09_goal_seed42 | westd-27271 | 0 | 81901 |
| 2 | eval_openvla_l2norm_k09_spatial_seed42 | westd-27271 | 1 | 79033 |
| 3 | eval_openvla_random_k09_goal_seed42 | westd-38929 | 0 | 936679 |
| 4 | eval_openvla_random_k09_spatial_seed42 | westd-38929 | 1 | 937064 |
| 5 | eval_openvla_attn_k085_goal_seed42 | westd-38929 | 2 | 860471 |
| 6 | eval_openvla_attn_k085_spatial_seed42 | westd-38929 | 3 | 861122 |
| 7 | eval_openvla_attn_k09_long_seed42 | westd-41074 | 0 | **无** |
| 8 | eval_openvla_attn_k085_long_seed42 | westd-41074 | 1 | 912556 |
| 9 | eval_pi05_random_k085_goal_seed43_postfix | westd-41074 | 2 | 10015 |
| 10 | eval_openvla_l2norm_k09_long_seed42 | westd-41074 | 3 | 53116 |
| 11 | eval_pi05_random_k085_object_seed43_postfix | cqa1-33015 | 0 | 733129 |
| 12 | eval_pi05_random_k085_spatial_seed43_postfix | cqa1-33015 | 1 | 788482 |
| 13 | eval_pi05_l2norm_k085_spatial_seed43_postfix | cqa1-33015 | 3 | 792816 |

### 4 台服务器 × GPU 状态矩阵

#### westd-27271（2 GPU）
| GPU | 显存占用 | 利用率 | GPU PID | Registry 匹配 | 状态 |
|-----|---------|--------|---------|---------------|------|
| 0 | 16.0/95.6 GB | 71% | 81911 | eval_openvla_l2norm_k09_goal_seed42 | ✅ 一致 |
| 1 | 15.7/95.6 GB | 69% | 79044 | eval_openvla_l2norm_k09_spatial_seed42 | ✅ 一致 |

#### westd-38929（4 GPU）
| GPU | 显存占用 | 利用率 | GPU PID | Registry 匹配 | 状态 |
|-----|---------|--------|---------|---------------|------|
| 0 | 15.6/95.6 GB | 66% | 936689 | eval_openvla_random_k09_goal_seed42 | ✅ 一致 |
| 1 | 15.7/95.6 GB | 84% | 937175 | eval_openvla_random_k09_spatial_seed42 | ✅ 一致 |
| 2 | 15.6/95.6 GB | 71% | 860477 | eval_openvla_attn_k085_goal_seed42 | ✅ 一致 |
| 3 | 15.7/95.6 GB | 67% | 861128 | eval_openvla_attn_k085_spatial_seed42 | ✅ 一致 |

#### westd-41074（4 GPU）
| GPU | 显存占用 | 利用率 | GPU PID | Registry 匹配 | 状态 |
|-----|---------|--------|---------|---------------|------|
| 0 | 15.8/95.6 GB | 71% | 982884 | eval_openvla_attn_k09_long_seed42 | ⚠️ 进程在跑但 registry 缺 PID |
| 1 | 15.4/95.6 GB | 66% | 912562 | eval_openvla_attn_k085_long_seed42 | ✅ 一致 |
| 2 | 10.3/95.6 GB | 21% | 10020 | eval_pi05_random_k085_goal_seed43_postfix | ✅ 一致 |
| 3 | 15.8/95.6 GB | 86% | 53125 | eval_openvla_l2norm_k09_long_seed42 | ✅ 一致 |

#### cqa1-33015（4 GPU）
| GPU | 显存占用 | 利用率 | GPU PID | Registry 匹配 | 状态 |
|-----|---------|--------|---------|---------------|------|
| 0 | 10.0/24.0 GB | 23% | 733134 | eval_pi05_random_k085_object_seed43_postfix | ✅ 一致 |
| 1 | 10.1/24.0 GB | 24% | 788487 | eval_pi05_random_k085_spatial_seed43_postfix | ✅ 一致 |
| 2 | 10.3/24.0 GB | 0% | 860112 | **无** | ❌ **有进程无注册** |
| 3 | 10.1/24.0 GB | 69% | 792821 | eval_pi05_l2norm_k085_spatial_seed43_postfix | ✅ 一致 |

---

### 不一致项

| 类型 | 服务器 | GPU | PID | 实验 | 详情 |
|------|--------|-----|-----|------|------|
| ❌ 有进程无注册 | cqa1-33015 | 2 | 860112 | π0.5 Random k=0.85 **Long** seed43 | `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85 --suite libero_10 --seed 43`，占用 10.5GB 显存但 registry 无记录 |
| ⚠️ Registry 缺 PID | westd-41074 | 0 | 982884 | eval_openvla_attn_k09_long_seed42 | 进程正常运行，但 registry 的 spec 中无 PID 字段（命令行已确认匹配） |

**总结**：13 个 RUNNING 实验全部有对应进程在跑（无"有注册无进程"情况）。有 1 个未注册的 GPU 进程（cqa1-33015 GPU2），1 个 registry 条目缺 PID 记录。

---
