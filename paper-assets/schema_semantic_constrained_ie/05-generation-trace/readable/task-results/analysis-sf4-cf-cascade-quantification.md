# analysis sf4 cf cascade quantification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf4-cf-cascade-quantification_20260523T094407_result.json`
- **Structured JSON:** [`a2921378fd358918cd90.json`](../../sessions/a2/a2921378fd358918cd90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

---

### Qwen ZS SciERC S1 (245 unique CF entities, 248 violations, 167/551 docs)

| 分类 | 数量 | 占比 | 含义 |
|---|---|---|---|
| **no_gold_match** | 144 | 58.1% | 实体不在 gold 中（幻觉实体） |
| **correct_lock** | 45 | 18.1% | first-seen 正确，约束阻止了错误类型 |
| **both_wrong** | 41 | 16.5% | 两个类型都不匹配 gold |
| **cascade_error** | 18 | 7.3% | first-seen 错误，阻止了正确类型 |

Generic 参与度：Specific→Generic 占 51.2%（主导模式），模型在具体类型锁定后尝试退化为 Generic。

### Qwen FT SciERC S1 (21 unique CF entities, 22 violations)

- **cascade_error = 0** — FT 完全消除了级联错误
- correct_lock = 14 (63.6%) — 剩余的 CF 大多是约束在帮忙

### 关键结论

1. **只有 7.3% 的 ZS CF violations 是真正的级联错误**（first-seen 锁错 → 阻止正确类型）
2. **correct_lock (18.1%) 是 cascade_error (7.3%) 的 2.5 倍** — first-seen 锁定更多时候是在帮忙
3. **58.1% 涉及幻觉实体** — CF 的根因是 ZS 模型能力不足，不是约束机制本身
4. **FT 完全消除 cascade errors** (0/22)，fine-tuning 解决了这个问题

脚本：`scripts/analyze_cf_cascade.py`
报告：`outputs/cf_cascade_analysis_qwen_zs_scierc_s1.json` / `..._ft_...json`

---
