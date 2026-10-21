# analysis precompute v4 shard01

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_precompute-v4-shard01_20260513T200541_result.json`
- **Structured JSON:** [`37d2c346215ee61b6744.json`](../../sessions/37/37d2c346215ee61b6744.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### Shard 完成情况

| Shard | 状态 | 样本进度 | EXIT_CODE | Error |
|-------|------|---------|-----------|-------|
| shard0 | **完成** | object 4857/4857 | 0 | 无 |
| shard1 | **完成** | object 4857/4857 | 0 | 无 |
| shard2 | **运行中** | object 4600/4856 | — | 无 |

- shard0/shard1 均正常退出，无 error/traceback
- 两者完成后各自尝试 merge，发现 shard2 未完成，跳过了 merge 步骤
- shard2 剩余 256 样本 × 0.48s/sample ≈ **~2 分钟内完成**（从最后一条日志算起，可能已经完成了）

### Cache 文件

**总大小：190MB**

| 目录 | 文件数 | 说明 |
|------|--------|------|
| spatial/ | 33 | 3 shard × 9 partial + 已合并的 obs_features.pt(46.7MB) / k_samples.pt(14.6MB) / expert_actions.pt(1.4MB) / manifest.json |
| object/ | 29 | 3 shard 的 partial 文件（shard0 10个 ✓, shard1 10个 ✓, shard2 9个，缺最后一块 4500-4856） |

- **spatial 已完成 merge**（合并文件已生成）
- **object 未 merge**，等 shard2 完成后由其触发合并

### Eval 进度

| Eval | 状态 |
|------|------|
| eval-spatial-v5-full | 运行中，第 1/10 个任务完成，success rate 90% (9/10) |
| eval-object-v4-full | 日志文件不存在，**未启动** |

### 结论

**shard0/shard1 可标记 DONE(success)**。shard2 预计已完成或即将完成，完成后会触发 object cache 的 merge。spatial 的 precompute+merge 已全部就绪。eval-spatial 刚开始跑第一个任务，eval-object 尚未启动。

---
