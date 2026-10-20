# code fix filters v2

**pgpf collapse filter** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_filters_v2_20260513T114021_result.json`
- **Structured JSON:** [`d93ca75185a751282311.json`](../../sessions/d9/d93ca75185a751282311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。以下是完整产出：

---

## 1. 修改前 PGPFStaticFilter 原始代码

```python
class PGPFStaticFilter(BaseFilter):
    """Property-guided filtering: keep samples passing ALL three property thresholds.

    Thresholds are percentile-based, computed from the score distribution.
    If fewer samples pass than retention_rate allows, return all passing samples.
    If more pass, randomly subsample to retention_rate.

    For lexical_conformity: higher = more conforming → keep above threshold.
    For quality (PPL): lower is better → keep below threshold.
    For semantic_novelty: higher means more novel → keep above threshold.
    """

    def __init__(self, retention_rate=0.5, lexical_conformity_percentile=50.0,
                 semantic_novelty_percentile=50.0, quality_percentile=50.0):
        super().__init__(retention_rate)
        self.lc_pct = lexical_conformity_percentile
        self.sn_pct = semantic_novelty_percentile
        self.q_pct = quality_percentile

    def filter(self, samples, scores):
        n = len(samples)
        k = self._target_count(n)
        lc_vals = np.array([s.get("lexical_conformity", 0.0) for s in scores])
        sn_vals = np.array([s.get("semantic_novelty", 0.0) for s in scores])
        q_vals = np.array([s.get("quality", float("inf")) for s in scores])
        lc_thresh = np.percentile(lc_vals, self.lc_pct)
        sn_thresh = np.percentile(sn_vals, self.sn_pct)
        q_thresh = np.percentile(q_vals, self.q_pct)
        passing_indices = []
        for i in range(n):
            if lc_vals[i] >= lc_thresh and sn_vals[i] >= sn_thresh and q_vals[i] <= q_thresh:
                passing_indices.append(i)
        if len(passing_indices) > k:
            passing_indices = random.sample(passing_indices, k)
        return [samples[i] for i in passing_indices]
```

**问题**：(1) 用 `quality` (PPL) 而非 `confidence`；(2) percentile threshold 交集可能返回少于 k 个样本。

## 2. 修改后完整 filters.py

已在上方验证输出中贴出完整内容。核心变化：
- `PGPFStaticFilter` 改为 rank-based：对 `lc`/`sn`/`confidence` 分别 rank 归一化后加权求和，取 top-k
- `lc` 反转（越低越好），`sn` 和 `confidence` 正向
- 总是返回恰好 k 个样本
- `build_filter` 中 `pgpf_static` 分支不再传 percentile 参数
- 顶部添加 `from scipy.stats import rankdata`

## 3. config.py 修改

- 注释 `# PGPF thresholds (percentile-based, applied to gen-0 distribution)` → `# PGPF property thresholds (LC + SN + Confidence; rank-based in PGPFStaticFilter)`
- 字段 `quality_percentile` → `confidence_percentile`

## 4. recursive_loop.py 检查结果

**无需修改。** 训练集构建逻辑 `current_train_data = filtered + real_subset` 本身正确，`n_real` 基于 `len(filtered)` 计算。旧的问题是 PGPFStaticFilter 可能返回少于 k 条（threshold 交集过严时），新实现总是返回恰好 k 条，与 RandomFilter/ConfidenceFilter 一致。

## 5. Import 测试

```
import OK
```

## 6. Dry-run 测试

```
Expected k = 2500
RandomFilter: 2500
ConfidenceFilter: 2500
PGPFStaticFilter: 2500
ALL EQUAL: True
```

---
