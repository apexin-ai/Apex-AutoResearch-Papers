# C1-C5 指标审计报告

> 审计时间: 2026-05-14  
> 数据来源: `results/mvp_v4_full.json` (83 samples, pipeline PID 29177 仍在运行)  
> 代码 single source of truth: `src/evaluate_mvp.py`  
> 辅助分析: `src/analyze.py`（计算逻辑与 evaluate_mvp.py **不同**）

---

## 1. C1-C5 正式定义（从 evaluate_mvp.py 代码提取）

### C1: disagree_rate（分歧率）
- **公式**: `len(disagree) / len(effective)`
- **分子**: effective 样本中 `agreement_type == "disagree"` 的样本数
- **分母**: effective 样本数（`fol_exec.verdict` 和 `code_exec.verdict` 均不为 `"Error"` 或 `None`）
- **排除**: `fol_exec` 或 `code_exec` 执行出错/缺失的样本
- **代码变量**: `dis_n`, `eff_n`
- **阈值**: ≥10% → PASS

### C2: diagnostic_rate（诊断率）
- **公式**: `diag_n / dis_n`
- **分子**: disagree 样本中 `fol_correct` 或 `code_correct` 至少一个为 True 的样本数
- **分母**: disagree 样本数
- **排除**: dis_n=0 时标记 N/A
- **代码变量**: `diag_n`, `dis_n`
- **阈值**: ≥40% → PASS

### C3: error_types（错误类型数）
- **公式**: `len(set(error_type for r in disagree))`
- **计算范围**: 仅 disagree 样本的 `disagreement.error_type`
- **代码变量**: `etypes`, `c3_count`
- **阈值**: ≥2 → PASS
- **⚠️ 与 analyze.py 的差异**: analyze.py 统计 ALL valid 样本的 error_type（5 种），evaluate_mvp.py 仅统计 disagree 样本（3 种）

### C4: targeted_vs_blind（定向修复 vs 盲目重生成）
- **公式**: `(tgt_rate - bld_rate) × 100` (pp)
- **tgt_rate**: `tgt_ok / tgt_att`，其中 tgt_att = 所有 valid 样本中有 `fol_targeted` 或 `code_targeted` repair rounds 的次数，tgt_ok = 其中至少一轮 `success=True` 的次数
- **bld_rate**: 同理统计 `fol_blind` / `code_blind`
- **注意**: FOL 和 Code 的 targeted/blind 混合计入同一个 rate，不区分方向
- **代码变量**: `tgt_ok`, `tgt_att`, `bld_ok`, `bld_att`, `c4_delta`
- **阈值**: >5pp → PASS

### C5: localization（错误定位准确率）
- **公式**: `loc_correct / loc_total`
- **predicted**: 取自 `disagreement.error_side`，若为空则取 `stability.predicted_error_side`
- **actual**: 根据 `fol_correct`/`code_correct` 判断：fol对code错→"code"，code对fol错→"fol"，都错→"both"，都对→跳过
- **排除**: `agree_correct` 样本；predicted=None；fol_correct 和 code_correct 均为 None
- **代码变量**: `loc_correct`, `loc_total`, `c5_acc`
- **阈值**: ≥60% → PASS
- **⚠️ 严重问题**: evaluate_mvp.py 中 `predicted` 来自 `disagreement.error_side`，而 `actual` 也由同一数据源（`fol_correct`/`code_correct`）在 pipeline 中计算并写入 `error_side`。**predicted 和 actual 来自同源数据**，100% 是同义反复，不是真正的预测准确率。analyze.py 的两层方法（Layer1: exec crash 检测, Layer2: stability 预测）才是有意义的评估。

---

## 2. 实际数值（evaluate_mvp.py 运行结果，83 样本）

### 全量模式（All samples, both executed）
| 指标 | 值 | 细节 | 阈值 | 状态 |
|------|-----|------|------|------|
| C1 disagree_rate | 32.1% | 25/78 | ≥10% | PASS |
| C2 diagnostic_rate | 88.0% | 22/25 | ≥40% | PASS |
| C3 error_types | 3 | logic_error, negation_error, quantifier_error | ≥2 | PASS |
| C4 targeted_delta | +21.9pp | T:24/32=75.0% B:17/32=53.1% | >5pp | PASS |
| C5 localization | 100.0% | 35/35 | ≥60% | PASS |

- Total: 83, Valid: 83, Effective (both executed): 78, GT≠Unknown: 53

### 排除 GT=Unknown 模式
| 指标 | 值 | 细节 | 阈值 | 状态 |
|------|-----|------|------|------|
| C1 disagree_rate | 32.7% | 16/49 | ≥10% | PASS |
| C2 diagnostic_rate | 87.5% | 14/16 | ≥40% | PASS |
| C3 error_types | 2 | — | ≥2 | PASS |
| C4 targeted_delta | +9.5pp | T:14/21 B:12/21 | >5pp | PASS |
| C5 localization | 100.0% | 23/23 | ≥60% | PASS |

### analyze.py 报告（同一数据，不同计算逻辑）
| 指标 | analyze.py 值 | evaluate_mvp.py 值 | 差异原因 |
|------|--------------|-------------------|----------|
| C1 | 30.1% (25/83) | 32.1% (25/78) | 分母不同：analyze.py 用 all valid, evaluate_mvp.py 用 effective |
| C3 | 5 types | 3 types | 范围不同：analyze.py 统计 all valid, evaluate_mvp.py 统计 disagree only |
| C4 | +21.9pp | +21.9pp | 一致 |
| C5 | 44.4% (16/36) | 100.0% (35/35) | **算法完全不同**（见下文） |

---

## 3. 三源对比表

### C3 error_types
| 来源 | 值 | 与代码一致性 |
|------|-----|-------------|
| Registry (80样本) | 3 | ✅ 与 evaluate_mvp.py 一致（disagree-only scope） |
| ROADMAP (80样本) | 5 | ✅ 与 analyze.py 一致（all-valid scope） |
| **代码真值** | evaluate_mvp.py=3, analyze.py=5 | 两个脚本计算范围不同 |

**结论**: Registry 引用了 evaluate_mvp.py 的口径（3），ROADMAP 引用了 analyze.py 的口径（5）。两者各自没错，但混用导致矛盾。Gate 评估应以 evaluate_mvp.py 为准→**3 types**。

### C4 targeted_delta
| 来源 | 值 | 与代码一致性 |
|------|-----|-------------|
| Registry (80样本) | 22.6pp | ✅ evaluate_mvp.py 在前 80 样本上确认 = +22.6pp |
| ROADMAP (80样本) | +22.6pp | ✅ 同上 |
| Report.md (79样本) | +36.3pp | ❌ 无法从当前数据复现（见§4分析） |
| **代码真值 (83样本)** | +21.9pp | — |

### C5 localization
| 来源 | 值 | 与代码一致性 |
|------|-----|-------------|
| Registry (80样本) | 1.0 (100%) | ✅ 与 evaluate_mvp.py 一致（但该算法有同义反复问题） |
| ROADMAP (80样本) | 45.8% | ✅ 与 analyze.py 一致（80 样本时 analyze.py = 42.9%，样本边界差异） |
| Report.md (79样本) | 78.3% | ❌ 无法从当前两套代码复现 |
| **代码真值 (83样本)** | evaluate_mvp.py=100%, analyze.py=44.4% | 两套算法差异极大 |

### C3/C4 标签互换问题
Report.md 中 **C3 对应 targeted_delta，C4 对应 localization**，与 evaluate_mvp.py 的定义（C3=error_types, C4=targeted_delta, C5=localization）不一致。Report.md 存在指标编号错位。

---

## 4. targeted delta 骤降分析

### 当前数值（83 样本）
| 方向 | Targeted rate | Blind rate | Delta |
|------|-------------|-----------|-------|
| FOL | 4/8 = 50.0% | 6/8 = 75.0% | **-25.0pp** |
| Code | 20/24 = 83.3% | 11/24 = 45.8% | **+37.5pp** |
| **混合** | **24/32 = 75.0%** | **17/32 = 53.1%** | **+21.9pp** |

### 80 样本时的数值
| 方向 | Targeted rate | Blind rate | Delta |
|------|-------------|-----------|-------|
| FOL | 4/8 = 50.0% | 6/8 = 75.0% | -25.0pp |
| Code | 19/23 = 82.6% | 10/23 = 43.5% | +39.1pp |
| **混合** | **23/31 = 74.2%** | **16/31 = 51.6%** | **+22.6pp** |

### 36.3pp 来源分析

Report.md 的 +36.3pp **无法从当前数据的任何切片复现**：
- 全量混合 delta: +21.9pp (83) / +22.6pp (80)
- Code-only delta: +37.5pp (83) / +39.1pp (80)
- FOL-only delta: -25.0pp

最可能的解释：
1. **36.3pp 来自 Report.md 的一个历史版本**，对应当时的数据快照（可能是 pipeline 中间状态，repair 数据不完整时的计算结果）
2. 或者是 **code-only delta 在某个中间快照的值**（code-only 在 37-39pp 范围内，36.3pp 接近但不精确匹配）
3. Report.md 同时存在 C3/C4/C5 编号错位问题，不排除数值也被错位复制

### FOL targeted < FOL blind 的原因

FOL targeted repair rate (50%) 低于 FOL blind (75%)，原因分析：
- FOL 修复样本量很小（仅 8 次 attempt），统计波动大
- FOL 侧在 disagree 中几乎总是"正确方"（9:1 不对称），targeted repair 主要针对 code 侧
- FOL targeted repair 的 8 次 attempt 可能针对的是 FOL 确实有错的少数困难样本，修复难度本身更高
- FOL blind（无诊断信息的重新生成）反而能靠"换个方式写"偶然修好简单的语法/格式问题

**这说明 C4 的 PASS (+21.9pp) 主要由 Code 修复的巨大优势 (+37.5pp) 驱动，FOL 方向实际上是负贡献。** 论文中应按方向分别报告，而非仅报混合 delta。

---

## 5. C5 同义反复问题（关键审计发现）

evaluate_mvp.py 的 C5 逻辑：
```python
predicted = dis_info.get("error_side")  # 从 disagreement 数据中读取
# ... 
if fol_c and not code_c: actual = "code"  # 也从 disagreement 数据推导
```

`error_side` 字段是 pipeline 在生成 disagreement 数据时，根据 `fol_correct`/`code_correct` 的值**直接计算并写入**的。因此 `predicted == actual` 是必然成立的——它们是同一个计算的两种表述。这就是 C5=100% 的原因。

analyze.py 的 C5 使用了不同方法：
- Layer 1: exec crash 检测（4/4 correct）
- Layer 2: stability-based prediction vs actual error_side（12/25 correct）
- 总计: 16/36 = 44.4%

**结论**: evaluate_mvp.py 的 C5=100% 不具备评估意义。如果要诚实评估 localization 能力，应使用 analyze.py 的两层方法，此时 C5=44.4% < 60% 阈值，**C5 实际 FAIL**。

---

## 6. 审计结论

| 指标 | evaluate_mvp.py 报告 | 实际可信度 | 建议 |
|------|---------------------|-----------|------|
| C1 | 32.1% PASS | ✅ 可信 | — |
| C2 | 88.0% PASS | ✅ 可信 | — |
| C3 | 3 types PASS | ✅ 可信（scope 是 disagree-only） | 统一口径，明确说明是 disagree 子集 |
| C4 | +21.9pp PASS | ⚠️ 需拆分报告 | FOL=-25pp, Code=+37.5pp，混合值掩盖了方向差异 |
| C5 | 100% PASS | ❌ 同义反复，不可信 | 应改用 analyze.py 逻辑，实际 44.4% FAIL |

**MVP 真实状态**: 如果修正 C5 定义，结果为 **4/5 PASS**（C5 FAIL），而非 5/5 PASS。

---

## 附录: evaluate_mvp.py 完整源码

```python
#!/usr/bin/env python3
"""MVP Gate Evaluation — compute 5 criteria, two sample groups."""

import json
import sys


def load_results(path):
    with open(path) as f:
        return json.load(f)


def evaluate(results, exclude_unknown=False):
    valid = [r for r in results if "disagreement" in r]
    if exclude_unknown:
        valid = [r for r in valid if r.get("ground_truth") != "Unknown"]

    total = len(valid)

    effective = [
        r for r in valid
        if r.get("fol_exec", {}).get("verdict") not in ("Error", None)
        and r.get("code_exec", {}).get("verdict") not in ("Error", None)
    ]
    eff_n = len(effective)

    # C1: disagree_rate among effective samples
    disagree = [r for r in effective if r["disagreement"]["agreement_type"] == "disagree"]
    dis_n = len(disagree)
    c1_rate = dis_n / eff_n if eff_n else 0

    # C2: diagnostic rate — at least one side correct among disagree
    if dis_n > 0:
        diag_n = sum(
            1 for r in disagree
            if r["disagreement"].get("fol_correct") or r["disagreement"].get("code_correct")
        )
        c2_rate = diag_n / dis_n
    else:
        diag_n = 0
        c2_rate = 0

    # C3: distinct error types among disagree
    etypes = set()
    for r in disagree:
        et = r["disagreement"].get("error_type")
        if et:
            etypes.add(et)
    c3_count = len(etypes)

    # C4: targeted vs blind repair
    tgt_att = tgt_ok = bld_att = bld_ok = 0
    for r in valid:
        rep = r.get("repair", {})
        for key in ("fol_targeted", "code_targeted"):
            rounds = rep.get(key, [])
            if rounds:
                tgt_att += 1
                if any(rd.get("success", False) for rd in rounds):
                    tgt_ok += 1
        for key in ("fol_blind", "code_blind"):
            rounds = rep.get(key, [])
            if rounds:
                bld_att += 1
                if any(rd.get("success", False) for rd in rounds):
                    bld_ok += 1

    has_repair = tgt_att > 0 or bld_att > 0
    tgt_rate = tgt_ok / tgt_att if tgt_att else 0
    bld_rate = bld_ok / bld_att if bld_att else 0
    c4_delta = (tgt_rate - bld_rate) * 100

    # C5: localization accuracy
    loc_correct = 0
    loc_total = 0
    for r in valid:
        dis_info = r["disagreement"]
        at = dis_info["agreement_type"]
        if at == "agree_correct":
            continue

        fol_c = dis_info.get("fol_correct")
        code_c = dis_info.get("code_correct")
        predicted = dis_info.get("error_side")

        if not predicted:
            stab = r.get("stability", {})
            predicted = stab.get("predicted_error_side") if isinstance(stab, dict) else None

        if predicted is None:
            continue
        if fol_c is None and code_c is None:
            continue

        if fol_c and not code_c:
            actual = "code"
        elif code_c and not fol_c:
            actual = "fol"
        elif not fol_c and not code_c:
            actual = "both"
        else:
            continue

        loc_total += 1
        if predicted == actual:
            loc_correct += 1

    has_loc = loc_total > 0
    c5_acc = loc_correct / loc_total if loc_total else 0

    return {
        "total": total,
        "effective": eff_n,
        "c1": {"rate": c1_rate, "num": dis_n, "den": eff_n, "pass": c1_rate >= 0.10},
        "c2": {"rate": c2_rate, "num": diag_n, "den": dis_n,
               "pass": c2_rate >= 0.40, "na": dis_n == 0},
        "c3": {"count": c3_count, "types": sorted(etypes), "pass": c3_count >= 2},
        "c4": {"tgt_rate": tgt_rate, "bld_rate": bld_rate, "delta": c4_delta,
               "tgt_ok": tgt_ok, "tgt_att": tgt_att, "bld_ok": bld_ok, "bld_att": bld_att,
               "pass": c4_delta > 5, "pending": not has_repair},
        "c5": {"acc": c5_acc, "correct": loc_correct, "total": loc_total,
               "pass": c5_acc >= 0.60, "pending": not has_loc},
    }


def print_section(title, ev):
    print(f"\n--- {title} ---")

    c1 = ev["c1"]
    c1_s = f"{c1['rate']*100:.1f}% ({c1['num']}/{c1['den']})"
    print(f"C1 disagree_rate:      {c1_s:28s} [>=10%]  {'PASS' if c1['pass'] else 'FAIL'}")

    c2 = ev["c2"]
    if c2["na"]:
        print(f"C2 diagnostic_rate:    {'N/A (0 disagree)':28s} [>=40%]  N/A")
    else:
        c2_s = f"{c2['rate']*100:.1f}% ({c2['num']}/{c2['den']})"
        print(f"C2 diagnostic_rate:    {c2_s:28s} [>=40%]  {'PASS' if c2['pass'] else 'FAIL'}")

    c3 = ev["c3"]
    c3_s = f"{c3['count']} types"
    print(f"C3 error_types:        {c3_s:28s} [>=2  ]  {'PASS' if c3['pass'] else 'FAIL'}")

    c4 = ev["c4"]
    if c4["pending"]:
        print(f"C4 targeted_vs_blind:  {'PENDING (no repair data)':28s} [>5pp ]  PENDING")
    else:
        c4_s = f"{c4['delta']:+.1f}pp (T:{c4['tgt_ok']}/{c4['tgt_att']} B:{c4['bld_ok']}/{c4['bld_att']})"
        print(f"C4 targeted_vs_blind:  {c4_s:28s} [>5pp ]  {'PASS' if c4['pass'] else 'FAIL'}")

    c5 = ev["c5"]
    if c5["pending"]:
        print(f"C5 localization:       {'PENDING (no data)':28s} [>=60%]  PENDING")
    else:
        c5_s = f"{c5['acc']*100:.1f}% ({c5['correct']}/{c5['total']})"
        print(f"C5 localization:       {c5_s:28s} [>=60%]  {'PASS' if c5['pass'] else 'FAIL'}")

    criteria = [
        c1["pass"],
        c2["pass"] if not c2["na"] else None,
        c3["pass"],
        c4["pass"] if not c4["pending"] else None,
        c5["pass"] if not c5["pending"] else None,
    ]
    passed = sum(1 for c in criteria if c is True)
    evaluated = sum(1 for c in criteria if c is not None)
    pending = sum(1 for c in criteria if c is None)
    return passed, evaluated, pending


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <results.json>")
        sys.exit(1)

    path = sys.argv[1]
    results = load_results(path)

    all_valid = [r for r in results if "disagreement" in r]
    non_unknown = [r for r in all_valid if r.get("ground_truth") != "Unknown"]
    effective = [
        r for r in all_valid
        if r.get("fol_exec", {}).get("verdict") not in ("Error", None)
        and r.get("code_exec", {}).get("verdict") not in ("Error", None)
    ]

    print("=" * 70)
    print("MVP Gate Evaluation")
    print("=" * 70)
    print(f"Results file: {path}")
    print(f"Total samples: {len(results)} | Valid: {len(all_valid)} | "
          f"Effective (both executed): {len(effective)} | GT!=Unknown: {len(non_unknown)}")

    ev_all = evaluate(results, exclude_unknown=False)
    p1, e1, pend1 = print_section("All samples (both executed)", ev_all)

    ev_no_unk = evaluate(results, exclude_unknown=True)
    p2, e2, pend2 = print_section("Excluding GT=Unknown", ev_no_unk)

    print()
    print("=" * 70)
    if pend1 > 0:
        print(f"MVP RESULT: {p1}/{e1} PASS, {pend1} PENDING")
    elif p1 == e1:
        print(f"MVP RESULT: {p1}/{e1} PASS -> PROCEED")
    else:
        print(f"MVP RESULT: {p1}/{e1} PASS -> BLOCKED")
    print("=" * 70)


if __name__ == "__main__":
    main()
```
