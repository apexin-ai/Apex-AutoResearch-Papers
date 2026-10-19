# check server process audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-process-audit_20260521T165332_result.json`
- **Structured JSON:** [`7797f1b047b9dba8a649.json`](../../sessions/77/7797f1b047b9dba8a649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是汇总。

---

## bjb1-32546 (6 GPU × 4090)
- **GPU 使用**: 全部 6 卡满载，9 个进程共享 6 卡
  - GPU 0,2,3: ~19.3GB/24.6GB（各 2 进程共享）— 99%, 99%, 90% 利用率
  - GPU 1,4,5: ~9.7GB/24.6GB（各 1 进程）— 25-27% 利用率
- **Python 进程**: 9 个 Object precompute（shard 1-9，num_shards=10）
  - s5: 5200/7251 (72%), ~66min 剩余
  - s8: 5400/7250 (74%), ~58min 剩余
  - s1: 4400/7251 (61%), ~102min 剩余
  - s6: 5300/7251 (73%), ~61min 剩余
  - s2,3,4,7,9: 类似进度
- **Cache**: 398MB in `object/`

## bjb2-28827 (6 GPU × 4090)
- **GPU 使用**: 全部 6 卡在用，每卡 ~9.7GB, 20-22% 利用率
- **Python 进程**: 6 个 Spatial precompute（shard 0-5，num_shards=7）
  - s0: 5000/8608 (58%), ~136min 剩余
  - s3: 5000/8607 (58%), ~137min 剩余
- **Cache**: 268MB in `spatial/`

## bjb1-18228 (4 GPU × 4090)
- **GPU 使用**: 仅 GPU 3 在用（9.7GB, 24%），**GPU 0,1,2 完全空闲**
- **Python 进程**: 1 个 Spatial precompute（shard 6，num_shards=7）
  - s6: 6000/8607 (70%), ~82min 剩余
- **Pipeline monitor**: `crm-pipeline-auto` 在运行，但其远程 SSH 监控失效（所有远程服务器都报 0 进程）
- **Cache**: spatial/ 55MB, object/ 256MB（旧数据残留）

## bjb2-40593 (1 GPU × 4090 D)
- **GPU 使用**: GPU 0 在用，9.8GB, 14% 利用率
- **Python 进程**: 1 个 Object+Spatial precompute（shard 0，num_shards=10）
  - `--benchmark object spatial`（先跑 object 再跑 spatial）
  - s0 object: 4900/7251 (68%), ~131min 剩余，3.35s/sample（最慢）
- **Cache**: 54MB in `object/`

---

## 总结
- **实际在跑的 precompute 进程数**: 17（9 + 6 + 1 + 1）
- **空闲 GPU 数**: 3（bjb1-18228 的 GPU 0,1,2）
- **状态**: **(a) 全部还在跑**，未完成也未停止
- **预计完成时间**: 最慢的是 bjb2-28827 spatial shards（~2.3hr）和 bjb2-40593 object shard 0（~2.2hr，且之后还要跑 spatial）

| Benchmark | Shards | 进度范围 | 预计完成 |
|-----------|--------|----------|----------|
| Object 0 (bjb2-40593) | 1/10 | 68% | ~2.2hr |
| Object 1-9 (bjb1-32546) | 9/10 | 61-74% | ~1-1.7hr |
| Spatial 0-5 (bjb2-28827) | 6/7 | ~58% | ~2.3hr |
| Spatial 6 (bjb1-18228) | 1/7 | 70% | ~1.4hr |

**关键问题**:
1. bjb1-32546 上 9 进程挤 6 GPU，3 卡双进程共享，可能互相拖慢
2. bjb1-18228 有 3 GPU 完全闲置，浪费资源
3. `crm-pipeline-auto` 的远程监控失效（SSH 不通），后续 rsync+merge 阶段可能也会失败
4. bjb2-40593 的 shard 0 跑的是 `object spatial` 双 benchmark 合并模式，其他服务器是分开跑的——sharding 方案不一致（object 用 10 shards，但 spatial 在其他机器用 7 shards）
5. Registry 显示 0 RUNNING 是因为这些进程通过 tmux/nohup 直接启动，没注册到 experiment registry

---
