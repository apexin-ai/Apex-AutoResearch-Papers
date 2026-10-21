# diagnose depth s1 failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_depth_s1_failure_20260522T072802_result.json`
- **Structured JSON:** [`d2a3a6de7fb006c29002.json`](../../sessions/d2/d2a3a6de7fb006c29002.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告：westd-34685 三实验同时崩溃

### 根因

**数据盘 `/root/autodl-tmp/` 100% 满（350G/350G）。** 三个实验在几乎同一时刻尝试保存 checkpoint 时触发 `No space left on device`。

### 关键错误

三个实验完全相同的错误栈：
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```
- **depth_s0**: 在 step 15000 保存 checkpoint 时崩溃（15:24:39 UTC）
- **depth_s1**: 在 step 15000 保存 checkpoint 时崩溃（15:24:38 UTC）
- **cutoff_s1**: 在 step 2500 保存 checkpoint 时崩溃（15:24:37 UTC）

### 磁盘占用分析（350G 总量）

| 目录 | 大小 | 说明 |
|------|------|------|
| checkpoints/occ_s1_fresh | **149G** | **旧实验残留，主要元凶** |
| checkpoints/depth_s0 | 76G | 7 个 checkpoint（2500~15000） |
| checkpoints/depth_s1 | 80G | 7 个 checkpoint（2500~15000） |
| checkpoints/cutoff_s0 | 15G | 1 个 checkpoint（2500） |
| checkpoints/cutoff_s1 | 11G | 1 个 checkpoint（2500，不完整） |
| models/ | 15G | openvla-7b 基座模型 |
| data/ | 2G | 数据集 |

### 影响范围

| 实验 | 服务器 | 状态 | 当前进度 |
|------|--------|------|----------|
| depth_s0 (cuda:1) | westd-34685 | **已崩溃** | 停在 step 15000 |
| depth_s1 (cuda:2) | westd-34685 | **已崩溃** | 停在 step 15000 |
| cutoff_s1 (cuda:3) | westd-34685 | **已崩溃** | 停在 step 2500 |
| cutoff_s0 (cuda:0) | westd-34685 | **运行中但危险** | step ~2852，将在 step 5000 时崩溃（约30分钟后） |
| depth_s2 | westd-10894 | 正常运行 | step ~1587 |
| depth_s3 | westd-10894 | 正常运行 | step ~1595 |

### cutoff_s0 为什么幸存

它是最后启动的（14:32），在 step 2500 时成功保存了一个 checkpoint（15G），恰好赶在磁盘完全满之前。但**它在 step 5000 时也会崩溃**，大约还有 30 分钟。

### 建议

**紧急**（必须在 cutoff_s0 到达 step 5000 前完成）：
1. **删除 `occ_s1_fresh/`**（149G）——旧实验残留，释放空间最快
2. 如果 occ_s1_fresh 仍然需要，删除 depth_s0/depth_s1 的中间 checkpoint（保留最新的 15000 和 12500 即可），每个实验可释放 ~50G

**重启策略**：
- depth_s0/depth_s1 可从 step 15000 的 checkpoint 恢复（15000 的部分文件已写入，需检查完整性；否则用 12500）
- cutoff_s1 需从头开始（仅跑了 2500 步）
- 考虑只保留最近 2-3 个 checkpoint 以防再次磁盘满

是否需要我帮你清理磁盘并重启实验？

---
