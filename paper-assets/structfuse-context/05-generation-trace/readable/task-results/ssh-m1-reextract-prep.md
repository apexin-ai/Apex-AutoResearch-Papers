# ssh m1 reextract prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m1_reextract_prep_20260513T192555_result.json`
- **Structured JSON:** [`87e3cb3dfcbd76f8fc8b.json`](../../sessions/87/87e3cb3dfcbd76f8fc8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇报如下：

---

## M1 重提取准备报告

### 1. 磁盘空间

| 项目 | 大小 |
|------|------|
| /root/autodl-tmp/ 总容量 | 250GB |
| 已用 | 124GB (50%) |
| **可用** | **127GB** |
| full_m1_data/ | 16GB（含 repos 3.2GB） |
| structfuse/ 总计 | 107GB |

重跑预计额外空间：CodeQL DB 临时占用 ~2-5GB（每组完成后自动清理），最终结果文件替换现有 error JSON 文件不会增加净用量。**127GB 剩余空间充足**。

### 2. 失败 instances 统计

- **总 instances**: 44,173
- **成功**: 15,897 (36%)
- **失败**: 28,276 (64%)，全部 `buggy_file_not_found`
- **涉及 repos**: 82 个（总共 123 repos）
- **错误分布**: 从 pylint-dev/astroid (1,749 err) 到 alanjds/drf-nested-routers (1 err)，集中在大 repo
- 所有 82 repos 都有部分成功、部分失败，确认瞬态故障而非系统性问题

### 3. 重跑脚本

**位置**:
- 准备脚本: `/root/structfuse/scripts/prepare_m1_rerun.py`
- 重跑脚本: `/root/structfuse/scripts/rerun_m1_failed.sh`

**执行流程**:
```bash
# Step 1: 准备（删除 error JSON + 生成 metadata）
python3 /root/structfuse/scripts/prepare_m1_rerun.py

# Step 2: 启动重跑（nohup 后台）
nohup bash /root/structfuse/scripts/rerun_m1_failed.sh &
```

**关键设计**:
- 3 workers（原 8，降低磁盘压力）
- 仅重跑 28,276 个失败 instances（metadata 已过滤，resume 跳过已有成功文件）
- CodeQL DB 每组完成后自动清理（batch_extract.py 已有此逻辑）
- 磁盘监控：每 5 分钟检查，<10GB 自动 kill
- 完成后自动重建 all.jsonl（旧文件备份为 .bak）
- 日志: `/root/runs/structfuse-context/m1_rerun.log`

### 4. 预估运行时间

- 成功 instances 平均提取时间: **24.82s**（median 22.57s, P90 33.94s）
- 82 个 repo group 的 CodeQL DB 创建: ~120s/group
- **3 workers**: 28,276 × 25s / 3 + 82 × 120s / 3 ≈ **~66 小时**
- **4 workers**: ≈ **~50 小时**（可在脚本中改 WORKERS=4）

### 5. 状态

**脚本已准备好，未启动。** GPU 未触碰。

---
