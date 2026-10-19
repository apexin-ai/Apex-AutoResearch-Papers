# code pool sensitivity prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pool_sensitivity_prep_20260516T075945_result.json`
- **Structured JSON:** [`f425940d00403f4c2bd7.json`](../../sessions/f4/f425940d00403f4c2bd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. evaluate_pool50.py 修改
已添加 `--max-queries` 参数（4 处改动），用于 dry-run 限制 query 数量。`--pool-size` 参数原本就支持，无需修改核心逻辑。

### 2. 脚本路径
`/root/structfuse/scripts/run_pool_sensitivity.sh`

### 3. Pool size 可行性分析

| Pool | 全局候选池 | 每 sample 自带 neg | 补齐来源 | 可行性 |
|------|-----------|-------------------|---------|--------|
| 50 | 50318 | max=50, median=50 | 多数不需补齐 | ✓ 完全可行 |
| 100 | 50318 | max=50 | 从全局池补 ~50 | ✓ 完全可行 |
| 200 | 50318 | max=50 | 从全局池补 ~150 | ✓ 完全可行 |
| 500 | 50318 | max=50 | 从全局池补 ~450 | ✓ 完全可行 |

所有 pool size 下全部 2476 test 样本均可参与评估（全局池 50318 远大于 500）。

**注意**：pool>50 时，额外候选来自其他 repo 的全局池（随机采样），不是同一 repo 内的文件。这意味着更大 pool 的"难度"取决于跨 repo 候选的迷惑性。

### 4. 执行命令模板

```bash
# 标准运行（GPU 空闲后执行）
DEVICE=cuda:1 bash /root/structfuse/scripts/run_pool_sensitivity.sh

# Dry-run（5 queries 验证）
DEVICE=cuda:1 MAX_QUERIES=5 bash /root/structfuse/scripts/run_pool_sensitivity.sh

# 全 seed 运行
DEVICE=cuda:1 SEEDS="42 43 44" bash /root/structfuse/scripts/run_pool_sensitivity.sh
```

### 5. 预估 GPU 时间（A6000, test set 2476 samples）

| Pool | 每 query 前向次数 | 预估单 checkpoint | 3 strategies × 1 seed |
|------|-----------------|------------------|----------------------|
| 50 | ~5 | ~12 min | ~36 min |
| 100 | ~8 | ~18 min | ~54 min |
| 200 | ~14 | ~30 min | ~90 min |
| 500 | ~33 | ~70 min | ~210 min |
| **合计** | | | **~6.5 hrs** |

3 strategies × 3 seeds × 4 pool sizes ≈ 19.5 hrs。建议先跑 seed=43 单 seed 验证排名趋势。

---
