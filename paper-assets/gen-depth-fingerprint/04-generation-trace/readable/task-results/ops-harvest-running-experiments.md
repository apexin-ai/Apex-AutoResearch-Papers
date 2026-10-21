# ops harvest running experiments

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-running-experiments_20260515T221121_result.json`
- **Structured JSON:** [`4490b3e92209e838e500.json`](../../sessions/44/4490b3e92209e838e500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总报告：

---

## 实验状态汇总

### 1. plan-007-cross-model — ✅ DONE (已入库)
- PIDs 241978/242205 已退出
- 3class F1=0.8089, binary F1=0.7635
- 无需操作

### 2. plan-008-multi-domain — ✅ DONE (刚收割)
- PID 234066 已退出，全 pipeline 跑完
- **Per-domain 3-class F1 (in-domain LOGO)**:

| Domain | 3-class F1 | Binary F1 |
|--------|-----------|-----------|
| wikipedia | **0.7928** | 0.8224 |
| scientific | 0.7049 | 0.7701 |
| creative | 0.6275 | 0.7310 |
| news | 0.5742 | 0.6266 |

- **跨域 pooled**: 3class=0.478, binary=0.674
- **Wiki→other transfer**: 极差（0.22-0.34），分类器不跨域泛化
- ⚠️ **dedup 未执行**——`--phase all` 直接跑完了 generate→extract→evaluate，跳过了之前要求的 dedup 步骤。前 ~45 seeds 可能有重复。如需论文级精确数字，需补跑 `dedup_generations.py → re-extract → re-evaluate`
- Registry 已更新为 DONE/success

### 3. plan-006-paraphrastic — ⏳ 仍在运行
- PID 246021 在 cuda:1，运行 ~41min
- **Generate 阶段 ~44%**：2111/~4975 条（当前 seed_id ~438/995）
- 速率 ~10s/seed，剩余 ~557 seeds ≈ 93min
- **ETA**：generate 完成 ~1.5h，加 extract+evaluate 总计 ~2h
- 无 results 文件产出

### 4. GPU 状态

| GPU | 利用率 | 显存 | 状态 |
|-----|-------|------|------|
| 0 | 65% | 6193/32607 MiB | 残留显存（plan-008 进程已退出，CUDA 未释放） |
| 1 | 63% | 6197/32607 MiB | plan-006 活跃（PID 246026） |
| 2 | 0% | 3 MiB | **空闲** |
| 3 | 0% | 3 MiB | **空闲** |

### 待决事项
1. **plan-008 dedup**：是否需要补跑 dedup→re-extract→re-evaluate 获取干净结果？GPU 0/2/3 空闲可用
2. **plan-006**：~2h 后可收割，到时需提取 paraphrastic vs continuation 对比数据

---
