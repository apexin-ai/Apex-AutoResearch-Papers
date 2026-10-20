# infra disk audit cleanup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-audit-cleanup_20260518T003456_result.json`
- **Structured JSON:** [`cb0174d63a12f3a0f91f.json`](../../sessions/cb/cb0174d63a12f3a0f91f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘诊断报告

### 清理前/后状态
| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 总容量 | 879G | 879G |
| 已用 | 398G | 398G |
| **可用** | **436G** | **436G** |

磁盘当前 436GB 可用，**远超 100GB 目标**。告警中提到的 66GB 可用状态已不存在，可能是训练进程临时文件释放或之前已有清理。

### 已删除
| 目录 | 大小 | 原因 |
|------|------|------|
| `checkpoints_deepseek_cls_repo/` | 195M | 原始 v1 CLS checkpoint，已被 v4 替代 |

### 规则中的 v2/v3 目录不存在
- `checkpoints_deepseek_cls_repo_v2/` — 不存在
- `checkpoints_deepseek_cls_repo_v3/` — 不存在

### 当前 Top 5 空间占用
| 目录 | 大小 | 备注 |
|------|------|------|
| `/root/autodl-tmp/models/` | 102G | 模型权重，不可删 |
| `/root/.cache/huggingface/` | 23G | Qwen 模型缓存 |
| `checkpoints_backup_cwm_8b/` | 11G | CWM 8B 备份，59 个中间 checkpoint |
| `checkpoints_backup_cls_8b_seed123/` | 5.5G | CLS 8B s123 备份，32 个中间 checkpoint |
| `checkpoints_repo_cls_8b_s42_resume/` | 5.4G | CLS 8B s42 resume 训练，33 个中间 checkpoint |

### 需要你确认的潜在清理项
上述 3 个 backup/resume 目录合计 **21.9G**，都包含大量中间 checkpoint（每 100-200 步一个）。如果这些备份不再需要，删除后可释放到约 458GB 可用。是否清理？

---
