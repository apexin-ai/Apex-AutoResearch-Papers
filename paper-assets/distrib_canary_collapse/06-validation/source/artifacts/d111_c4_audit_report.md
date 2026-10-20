# D111 Direction Check Audit — C4 Experiments

审计日期: 2026-05-19
服务器: westd-17855

---

## c4_a050_s42_fp32

- **5method_leadlag.json 存在？** 否（仅有 analysis_results.json）
- **naive_xcorr direction-checked？** 否

### peak_lag 原始值

| Pair | naive_lag | diff_lag | naive_fwd? | diff_fwd? |
|------|-----------|----------|------------|-----------|
| entropy→d1 | -5 | -1 | NO | NO |
| entropy→d2 | 4 | -1 | YES | NO |
| entropy→d3 | -1 | -1 | NO | NO |
| entropy→mauve | -1 | -1 | NO | NO |
| ece→d1 | -5 | -1 | NO | NO |
| ece→d2 | 5 | -1 | YES | NO |
| ece→d3 | 4 | -1 | YES | NO |
| ece→mauve | 5 | -1 | YES | NO |

### 方向修正前后对比

| Metric | Registry (未修正) | 修正后 (peak_lag>0) |
|--------|-------------------|---------------------|
| naive_xcorr | 8/8 | **4/8** |
| diff_xcorr | 8/8 | **0/8** |
| PermG_fwd | 8/8 | 8/8 (不受影响) |
| PermG_rev | 7/8 | 7/8 (不受影响) |
| threshold_onset | 8/8 | 8/8 (不受影响) |
| TY_granger | 4/8 | 4/8 (不受影响) |
| K≥3 | 8/8 | **6/8** |
| K≥4 | 8/8 | **2/8** |

### K≥3/K≥4 修正明细

| Pair | 原 votes | 修正 votes | 修正后方法 |
|------|----------|------------|------------|
| entropy→d1 | 4 (naive,diff,thresh,pg_fwd) | **2** (thresh,pg_fwd) | K≥3:NO |
| entropy→d2 | 4 (naive,diff,thresh,pg_fwd) | **3** (naive,thresh,pg_fwd) | K≥3:YES |
| entropy→d3 | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| entropy→mauve | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| ece→d1 | 4 (naive,diff,thresh,pg_fwd) | **2** (thresh,pg_fwd) | K≥3:NO |
| ece→d2 | 4 (naive,diff,thresh,pg_fwd) | **3** (naive,thresh,pg_fwd) | K≥3:YES |
| ece→d3 | 5 (naive,diff,thresh,pg_fwd,ty) | **4** (naive,thresh,pg_fwd,ty) | K≥4:YES |
| ece→mauve | 5 (naive,diff,thresh,pg_fwd,ty) | **4** (naive,thresh,pg_fwd,ty) | K≥4:YES |

---

## c4_a075_s42_fp32

- **5method_leadlag.json 存在？** 否（仅有 analysis_results.json）
- **naive_xcorr direction-checked？** 否

### peak_lag 原始值

| Pair | naive_lag | diff_lag | naive_fwd? | diff_fwd? |
|------|-----------|----------|------------|-----------|
| entropy→d1 | -1 | -1 | NO | NO |
| entropy→d2 | -1 | -2 | NO | NO |
| entropy→d3 | -2 | -2 | NO | NO |
| entropy→mauve | -1 | -1 | NO | NO |
| ece→d1 | -5 | -1 | NO | NO |
| ece→d2 | -1 | -1 | NO | NO |
| ece→d3 | -1 | -2 | NO | NO |
| ece→mauve | -1 | -1 | NO | NO |

### 方向修正前后对比

| Metric | Registry (未修正) | 修正后 (peak_lag>0) |
|--------|-------------------|---------------------|
| naive_xcorr | 8/8 | **0/8** |
| diff_xcorr | 8/8 | **0/8** |
| PermG_fwd | 8/8 | 8/8 (不受影响) |
| PermG_rev | 0/8 | 0/8 (不受影响) |
| threshold_onset | 8/8 | 8/8 (不受影响) |
| TY_granger | 6/8 | 6/8 (不受影响) |
| K≥3 | 8/8 | **6/8** |
| K≥4 | 8/8 | **0/8** |

### K≥3/K≥4 修正明细

| Pair | 原 votes | 修正 votes | 修正后方法 |
|------|----------|------------|------------|
| entropy→d1 | 4 (naive,diff,thresh,pg_fwd) | **2** (thresh,pg_fwd) | K≥3:NO |
| entropy→d2 | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| entropy→d3 | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| entropy→mauve | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| ece→d1 | 4 (naive,diff,thresh,pg_fwd) | **2** (thresh,pg_fwd) | K≥3:NO |
| ece→d2 | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| ece→d3 | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |
| ece→mauve | 5 (naive,diff,thresh,pg_fwd,ty) | **3** (thresh,pg_fwd,ty) | K≥3:YES |

---

## c4_a025_s42_fp32 (参考，已修正)

- **5method_leadlag.json 存在？** 否（仅有 analysis_results.json）
- **Registry 已有 D111 修正记录**: naive 8/8→3/8, diff 8/8→0/8, K3 8/8→0/8, K4 3/8→0/8

### 验证 peak_lag 值

| Pair | naive_lag | diff_lag | naive_fwd? | diff_fwd? |
|------|-----------|----------|------------|-----------|
| entropy→d1 | -2 | -3 | NO | NO |
| entropy→d2 | 1 | -3 | YES | NO |
| entropy→d3 | 3 | -1 | YES | NO |
| entropy→mauve | -1 | -1 | NO | NO |
| ece→d1 | -2 | -3 | NO | NO |
| ece→d2 | 0 | -3 | NO | NO |
| ece→d3 | 2 | -1 | YES | NO |
| ece→mauve | -1 | -1 | NO | NO |

naive forward: 3/8 ✓ 与 registry 一致
diff forward: 0/8 ✓ 与 registry 一致

---

## 分析脚本状态

### batch_analysis.py

- **路径**: `/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py`
- **输出文件**: `analysis_results.json`
- **D111 方向检查**: ❌ **缺失**

**Bug 位置 1 — summary 计数（~L445-446）**:
```python
# 当前代码（错误）：只检查 significant，不检查 peak_lag
naive_fwd = sum(1 for p in all_pairs if p["results"].get("naive_xcorr", {}).get("significant", False))
diff_fwd = sum(1 for p in all_pairs if p["results"].get("diff_xcorr", {}).get("significant_fdr", ...))

# 修正：加 peak_lag > 0 过滤
naive_fwd = sum(1 for p in all_pairs
    if p["results"].get("naive_xcorr", {}).get("significant", False)
    and (p["results"].get("naive_xcorr", {}).get("peak_lag") or 0) > 0)
diff_fwd = sum(1 for p in all_pairs
    if p["results"].get("diff_xcorr", {}).get("significant_fdr",
        p["results"].get("diff_xcorr", {}).get("significant", False))
    and (p["results"].get("diff_xcorr", {}).get("peak_lag") or 0) > 0)
```

**Bug 位置 2 — compute_consensus（L372-385）**:
```python
# 当前代码（错误）：
if r["naive_xcorr"].get("significant", False):
    votes += 1; methods_sig.append("naive")
if r["diff_xcorr"].get("significant_fdr", r["diff_xcorr"].get("significant", False)):
    votes += 1; methods_sig.append("diff")

# 修正：加 peak_lag > 0
if r["naive_xcorr"].get("significant", False) and (r["naive_xcorr"].get("peak_lag") or 0) > 0:
    votes += 1; methods_sig.append("naive")
if (r["diff_xcorr"].get("significant_fdr", r["diff_xcorr"].get("significant", False))
        and (r["diff_xcorr"].get("peak_lag") or 0) > 0):
    votes += 1; methods_sig.append("diff")
```

### run_5method_s43.py

- **路径**: `/root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py`
- **输出文件**: `5method_leadlag.json`
- **D111 方向检查**: ❌ **缺失**（无 direction 相关代码）

---

## 总结

| 实验 | naive 修正 | diff 修正 | K≥3 修正 | K≥4 修正 | 需更新 registry |
|------|-----------|-----------|----------|----------|----------------|
| c4_a025 | 8/8→3/8 ✓ | 8/8→0/8 ✓ | 8/8→0/8 ✓ | 3/8→0/8 ✓ | 否（已修正） |
| c4_a050 | 8/8→**4/8** | 8/8→**0/8** | 8/8→**6/8** | 8/8→**2/8** | **是** |
| c4_a075 | 8/8→**0/8** | 8/8→**0/8** | 8/8→**6/8** | 8/8→**0/8** | **是** |

### 关键发现

1. **c4_a075 影响最严重**：naive 和 diff 全部 peak_lag ≤ 0（全为负 lag），方向完全错误。K≥4 从 8/8 直接归零。但 PermG(8/8) + threshold(8/8) + TY(6/8) 仍支撑 K≥3=6/8。

2. **c4_a050 中度影响**：diff 全部 lag=-1，naive 仅 4/8 有正 lag。K≥4 从 8/8 降至 2/8（仅 ece→d3 和 ece→mauve 保留）。

3. **两个分析脚本均未内置 D111 方向检查**：batch_analysis.py 和 run_5method_s43.py 都只检查 significance，不过滤 peak_lag 方向。需在 compute_consensus 和 summary 计数处修复。

4. **c4 实验 diff_xcorr 系统性反向**：三个 C4 实验中，diff_xcorr 的 peak_lag 全部 ≤ 0（绝大多数为 -1），说明 C4 数据集上差分互相关一致检测到下游→canary 方向，而非 canary→下游。这是 C4 vs WikiText 的一个显著差异。
