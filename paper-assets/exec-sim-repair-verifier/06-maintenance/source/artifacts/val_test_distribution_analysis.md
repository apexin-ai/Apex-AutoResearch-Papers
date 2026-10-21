# Val/Test 分布差异分析报告

## 概要结论

**Root cause: 多维度严重分布偏移，核心是 mutation type 组成 + per-problem 难度异质性。**

Val 和 Test 来自**完全不同的 SWE-bench 问题实例**（22 vs 25 个 problem_id，零重叠），导致 repo 组成、mutation type 分布、per-problem label rate 全部偏移。Checkpoint selection 在 val 上优化的 pattern 不迁移到 test 的不同信号分布上，造成 ranking reversal。

---

## 1. 基本统计

| 指标 | Val | Test | 差异 |
|------|-----|------|------|
| 样本数 | 9,335 | 9,784 | +4.8% |
| 唯一 problem_id | 22 | 25 | — |
| **PID 重叠** | **0** | **0** | **完全不同** |
| 唯一 repo | 8 | 9 | — |
| label=1 (正例) | 7,083 (75.88%) | 7,138 (72.96%) | -2.92pp |
| label=0 (负例) | 2,252 (24.12%) | 2,646 (27.04%) | +2.92pp |
| Majority baseline | 75.88% | 72.96% | -2.92pp |

## 2. Mutation Type 分布（最关键差异）

| Mutation Type | Val | Val% | Test | Test% | 偏移 |
|---------------|-----|------|------|-------|------|
| gold | 4,223 | 45.2% | 4,633 | 47.4% | +2.2pp |
| **operator_swap** | **1,783** | **19.1%** | **3,357** | **34.3%** | **+15.2pp** |
| boundary_removal | 1,401 | 15.0% | 1,049 | 10.7% | -4.3pp |
| **off_by_one** | **929** | **10.0%** | **183** | **1.9%** | **-8.1pp** |
| return_value | 999 | 10.7% | 562 | 5.7% | -5.0pp |

**关键**: operator_swap 从 19.1% → 34.3%（接近翻倍），off_by_one 从 10.0% → 1.9%（缩减 5 倍）。不同 mutation type 的检测签名完全不同，模型在 val 上学到的 off_by_one 检测能力在 test 上几乎无用。

### 每种 Mutation 的 label=0 (被检出) 率

| Mutation Type | Val label=0 率 | Test label=0 率 | 差异 |
|---------------|---------------|----------------|------|
| boundary_removal | 40.8% | 58.3% | +17.5pp |
| off_by_one | 16.5% | 29.5% | +13.0pp |
| operator_swap | 44.3% | 49.6% | +5.3pp |
| return_value | 73.9% | 56.2% | -17.7pp |

return_value 在 val 中最容易检出（73.9%），但在 test 中检出率下降 17.7pp 且样本量骤减。operator_swap 在 test 中占主导且检出率略高。

## 3. Repo 组成

| Repo | Val% | Test% | 差异 |
|------|------|-------|------|
| django/django | 29.7% | 36.5% | +6.8pp |
| **pydata/xarray** | **0%** | **23.7%** | **Test-only** |
| matplotlib/matplotlib | 18.9% | 16.1% | -2.8pp |
| **pylint-dev/pylint** | **12.1%** | **0%** | **Val-only** |
| astropy/astropy | 7.3% | 10.9% | +3.6pp |
| sympy/sympy | 19.1% | 1.1% | -18.0pp |
| scikit-learn/scikit-learn | 6.3% | 0.5% | -5.8pp |
| **psf/requests** | **0%** | **4.5%** | **Test-only** |
| pytest-dev/pytest | 5.1% | 5.3% | ≈ |
| sphinx-doc/sphinx | 1.6% | 1.3% | ≈ |

- xarray 占 test 的 23.7% 但 val 中完全没有
- pylint 占 val 的 12.1% 但 test 中完全没有
- sympy 从 val 19.1% 骤降到 test 1.1%

### 同 repo 跨 split label=0 率剧变

| Repo | Val label=0 率 | Test label=0 率 | 原因 |
|------|---------------|----------------|------|
| **matplotlib** | **2.9%** | **50.0%** | Val: boundary_removal(几乎全存活); Test: operator_swap(50%被检出) |
| **astropy** | **0.0%** | **40.8%** | Val: 纯 gold 无 mutation; Test: 有 boundary+operator_swap |
| sympy | 40.4% | 51.4% | 不同 problem instance |
| django | 24.6% | 32.6% | 不同 problem instance + mutation mix |

matplotlib 在 val 中几乎是 "免费准确率"（97.1% label=1），在 test 中变成 50/50 的难题。

## 4. Test Type (f2p vs p2p)

| Test Type | Val | Val% | Test | Test% |
|-----------|-----|------|------|-------|
| f2p | 2,968 | 31.8% | 2,320 | 23.7% |
| p2p | 6,367 | 68.2% | 7,464 | 76.3% |

Test 比 Val 多 ~8pp 的 p2p 样本。

## 5. 输入长度分布（字符数）

| 字段 | Split | Mean | Median | P5 | P95 | Max |
|------|-------|------|--------|-----|-----|-----|
| code | Val | 4,435 | 1,354 | 404 | 18,007 | 18,007 |
| code | Test | 3,533 | 1,552 | 558 | 8,857 | 8,857 |
| test | Val | 161 | 76 | 36 | 506 | 11,345 |
| test | Test | 92 | 70 | 52 | 121 | 1,264 |
| total | Val | 6,542 | 3,208 | 2,460 | 20,472 | 31,352 |
| total | Test | 5,591 | 3,454 | 2,609 | 10,967 | 11,759 |

- Val 的 code 字段方差更大（p95=18,007 vs 8,857），长尾更重
- Val 的 test 字段也有更大方差（max=11,345 vs 1,264）
- **4B seed123 的 val@5120 vs test@2048 截断差异在长尾样本上影响显著**（val p95=20,472 远超 5120 token，大量内容被截断）

## 6. Per-Problem 集中度

### Val 头部问题
| Problem | Repo | 占比 | label=0 率 | Mutation |
|---------|------|------|-----------|----------|
| matplotlib-23314 | matplotlib | 18.9% | 3% | boundary_removal |
| sympy-14248 | sympy | 15.1% | 35% | operator_swap + off_by_one |
| pylint-4604 | pylint | 12.1% | 35% | boundary_removal + operator_swap |
| django-16938 | django | 10.3% | 50% | return_value |
| django-13344 | django | 8.4% | 0% | operator_swap(全存活) |

Top-5 占 val 的 64.8%。

### Test 头部问题
| Problem | Repo | 占比 | label=0 率 | Mutation |
|---------|------|------|-----------|----------|
| xarray-6992 | xarray | 23.7% | 0% | operator_swap(全存活) |
| matplotlib-24177 | matplotlib | 16.1% | 50% | operator_swap |
| astropy-7336 | astropy | 10.9% | 41% | boundary_removal + operator_swap |
| django-12325 | django | 7.3% | 67% | operator_swap + boundary_removal |
| django-14315 | django | 6.1% | 58% | return_value + operator_swap |

Top-5 占 test 的 64.1%。

**关键对比**: 
- Val 最大问题 matplotlib-23314 (18.9%) 几乎全正确（3% label=0）→ 模型在此问题上 predict-all-1 即可
- Test 最大问题 xarray-6992 (23.7%) 也是全正确（0% label=0）→ 但模型从未见过 xarray
- Test 第二大 matplotlib-24177 (16.1%) 是 50/50 → 与 val 中同 repo 的难度天差地别

## 7. "免费准确率" 问题（label=0 = 0%，predict-all-1 即正确）

| Split | 这类问题占比 | 涉及的 repo |
|-------|------------|------------|
| Val | ~22% | astropy(7.3%), django(多个小问题), scikit-learn(3.2%), sympy(0.5%) |
| Test | ~32% | xarray(23.7%), django(多个小问题) |

Test 有更多 "免费" 样本（32% vs 22%），但这些集中在模型从未见过的 xarray repo。

---

## 8. Reversal 机制分析

### 为什么 val-best ≠ test-best

1. **Mutation specialization**: Val 奖励 off_by_one (10%) 和 return_value (10.7%) 检测能力，Test 奖励 operator_swap (34.3%) 检测能力。不同 checkpoint 可能对不同 mutation type 有不同学习进度，导致 ranking 反转。

2. **Repo overfitting**: Val-best checkpoint 可能 overfit 到 pylint/sympy 的 pattern（合计 31.2% of val），这些 repo 在 test 中几乎不存在。反之，test 需要 xarray (23.7%) 泛化能力，val 完全无法选择。

3. **Per-problem difficulty shift**: 同名 repo（如 matplotlib）在 val/test 中用了完全不同的 problem instance + mutation type 组合，导致 "matplotlib 上的表现" 含义完全不同。

4. **Class balance shift**: Val 24.1% vs Test 27.0% label=0，3pp 差异。模型在 val 上学到的 threshold 在 test 上偏高。

5. **（4B s123 confound）**: seq_len 5120→2048 导致 val 长尾样本（code p95=18007）被截断更多，改变了难度分布。8B s42 的 8192→8192 是 clean comparison，但仍有上述 1-4 的分布偏移。

### 可验证预测

如果 root cause 正确，以下应成立：
- 在 test 上按 mutation_type 拆分准确率，val-best 和 test-best checkpoint 在 operator_swap 子集上差异最大
- 在 test 上按 repo 拆分，xarray 子集的表现差异最显著（因为 val 选择完全无法考虑 xarray）
- 8B s42 (clean seq_len) 的 reversal 幅度应小于 4B s123（有 seq_len confound）

---

## 9. 建议（如需改进 checkpoint selection）

1. **Stratified val set**: 重新划分 val/test，确保 repo、mutation type、problem instance 有重叠
2. **Per-mutation-type early stopping**: 不用整体 val accuracy 选 checkpoint，而是分 mutation type 看 calibration
3. **Cross-validation**: 在完整数据上做 k-fold，避免单一 val split 的 selection bias
