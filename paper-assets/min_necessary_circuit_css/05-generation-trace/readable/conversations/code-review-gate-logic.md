# code review gate logic

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 0
- **Tool calls:** 1
- **Original source:** `logs/chats/worker_code_review_gate_logic_20260512T225814.jsonl`
- **Structured JSON:** [`03034c5223f6318d0c45.json`](../../sessions/03/03034c5223f6318d0c45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

3 recorded events

### Tool call

_source line 1 · 2026-05-12T23:00:47.662086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_review_gate_logic_20260512T225814",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/analyze_mvp_results.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T23:00:47.662798+00:00_

1	"""MVP 结果自动分析：Phase C/D/E 汇总。
2	
3	读取 v3 三方法 circuit 数据，计算 CSS matrix、off-diagonal 比率、
4	按 ACDC threshold 敏感性分析，生成可视化，输出 pass/fail 判定。
5	
6	Usage:
7	    python analyze_mvp_results.py [--results-dir /root/structfuse-context] [--output-dir ./analysis]
8	    python analyze_mvp_results.py --dry-run   # mock data 验证
9	"""
10	
11	import argparse
12	import itertools
13	import json
14	import sys
15	from collections import Counter
16	from pathlib import Path
17	from typing import Any, Dict, List, Optional, Set, Tuple
18	
19	import numpy as np
20	
21	
22	# ---------------------------------------------------------------------------
23	# Data loading
24	# ---------------------------------------------------------------------------
25	
26	def _find_cache_files(results_dir: Path) -> Dict[str, Path]:
27	    """Auto-detect per-method cache files under results_dir.
28	
29	    Searches for:
30	      1. cache_&lt;method>.json  (old MVP flat layout)
31	      2. cache/&lt;model_slug>/&lt;task>/&lt;method>_*.json  (run_circus.py structured cache)
32	      3. Keys inside mvp_results.json that embed raw scores
33	    """
34	    found: Dict[str, Path] = {}
35	    method_names = ["eap_ig", "edge_pruning", "acdc", "ifr"]
36	
37	    for m in method_names:
38	        flat = results_dir / f"cache_{m}.json"
39	        if flat.exists():
40	            found[m] = flat
41	
42	    cache_dir = results_dir / "cache"
43	    if cache_dir.is_dir():
44	        for p in cache_dir.rglob("*.json"):
45	            for m in method_names:
46	                if p.stem.startswith(m):
47	                    found.setdefault(m, p)
48	
49	    return found
50	
51	
52	def _load_scores_from_file(path: Path) -> Dict[str, float]:
53	    """Load edge scores from a cache JSON (handles both flat and structured)."""
54	    with open(path) as f:
55	        data = json.load(f)
56	
57	    if isinstance(data, dict) and "scores" in data:
58	        return {str(k): float(v) for k, v in data["scores"].items()}
59	    if isinstance(data, dict) 
…[truncated 22451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_review_gate_logic_20260512T225814",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 3 · 2026-05-12T23:00:47.663186+00:00_

## 审核结果

### 1. Off-diagonal 计算 — **PASS**

代码有两层 off-diagonal 计算：

**2^K cross-tabulation** (`compute_css_matrix_full`, L171-201):
- `all_edges` = 所有 circuit 的 union，因此不存在 `(0,0,0)` cell → `total_with_any == len(all_edges)` ✓
- `off_diagonal = total_with_any - agree_in` = 非全部方法一致的边数 ✓
- `off_diagonal_pct = off_diagonal / total_with_any` = 相对于 union 的比例 ✓

**CIRCUS-core x CSS cross-table** (`compute_cross_table`, L226-267):
- 每条边的 `css_score = (包含该边的方法数) / K`，高 CSS 阈值 0.67（K=3 时需 ≥2/3 方法） ✓
- 四象限分类正确：`stable_core`(core+高CSS)、`method_specific`(core+低CSS)、`cross_unstable`(非core+高CSS)、`noise` ✓
- `off_diagonal_pct = method_specific / (stable_core + method_specific)` = core 中方法特异性比例 ✓

**潜在风险**（非阻塞）：L232 `all_edges = set(tiers.keys()) | union(circuits)` 包含所有评分边（未二值化的）。`compute_circus_tiers` 中 `core_thr=1.0` 意味着仅高于 90.91 百分位的边为 core（约占总边数 9%）。当总评分边 >2200 且 `top_n=200` 时，部分 core-tier 边不在任何 circuit 中，会被错误归为 `method_specific`，抬高 `off_diagonal_pct`。对典型 transformer 规模（~1000-2000 边）不构成问题。

### 2. Gate 标准对齐 — **PASS**

L313-334 阈值完全匹配：

| 代码 | 标准 | 对齐 |
|------|------|------|
| `pct >= 10` → PASS_MAIN | ≥10% → Main track | ✓ |
| `pct >= 5` → PASS_FINDINGS | 5-10% → Findings + Arithmetic | ✓ |
| `pct >= 2` → MARGINAL | 2-5% → Findings 确认 | ✓ |
| `pct < 2` → KILL | <2% + 连续两组 + ΔF 无差异 | ✓* |

\*KILL 的"连续两组"和"ΔF 无统计差异"条件未在代码中自动检查，但 action 字符串中标注了 ΔF 前置条件（L334: `"if ΔF 无统计差异"`）。对于单次运行分析脚本，连续组检查需跨 run 比较，合理地留给人工判断。

### 3. 输出完整性 — **PASS (缺置信区间)**

| 要求 | 状态 | 位置 |
|------|------|------|
| off-diagonal 绝对边数 | ✓ | L533 |
| off-diagonal 百分比 | ✓ | L533 (相对 total_union) + L554 (相对 core_total) |
| 基数说明 | ✓ | 两种基数均输出 |
| 2^K cell 分布 | ✓ | L536-538，含边数和百分比 |
| 置信区间 | ✗ | 未实现 |

置信区间未计算。如果需要，可用 bootstrap 对 top-N 二值化重采样计算 off-diagonal 的 CI。当前不影响 gate 判定逻辑的正确性。

### 4. Critical fix 验证 — **PASS**

- **Critical 1** (L565): `gate = gate_judgment(xtab["off_diagonal_pct"])` — 使用 CIRCUS-core off-diagonal，非 2^K cell off-diagonal。L564 注释明确标注。 ✓
- **Critical 2** (L541): `primary = "eap_ig"` — 硬编码，非 `sorted(methods)[0]`（后者会得到 "acdc"）。 ✓

---

**结论**：gate 逻辑与 D001-D003 标准对齐，两个 critical fix 已正确应用，可用于 v3 结果判定。唯一缺项是置信区间，以及当边数规模 >2200 时 `compute_cross_table` 的 `all_edges` 可能引入膨胀（建议将 L232 改为仅取 circuit union：`all_edges = set(); for c in circuits.values(): all_edges |= c`，不包含未二值化的 tiers 键）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_review_gate_logic_20260512T225814"
}
```

</details>

---
