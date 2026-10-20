# research val test distribution analysis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_val-test-distribution-analysis_20260514T223007_result.json`
- **Structured JSON:** [`671f6138b17e1992f154.json`](../../sessions/67/671f6138b17e1992f154.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。以下是完整分析。

---

## 1. Label Balance

| | Val (9335) | Test (9784) | Δ |
|---|---|---|---|
| Pass (1) | 7083 (75.88%) | 7138 (72.96%) | -2.9pp |
| Fail (0) | 2252 (24.12%) | 2646 (27.04%) | +2.9pp |

Test 的 fail 比例高 2.9pp。影响 majority baseline（val 75.9% vs test 73.0%），但不足以解释 reversal。

---

## 2. Mutation Type Distribution — 显著差异

| Mutation Type | Val | Val% | Test | Test% | Δ |
|---|---|---|---|---|---|
| gold | 4223 | 45.2% | 4633 | 47.4% | +2.2pp |
| **operator_swap** | **1783** | **19.1%** | **3357** | **34.3%** | **+15.2pp** |
| boundary_removal | 1401 | 15.0% | 1049 | 10.7% | -4.3pp |
| return_value | 999 | 10.7% | 562 | 5.7% | -5.0pp |
| **off_by_one** | **929** | **10.0%** | **183** | **1.9%** | **-8.1pp** |

Test 被 operator_swap 主导（34.3%），val 的 mutation 分布更均匀。

### 各 Mutation Type 的 Pass Rate 差异

| Mutation Type | Val Pass% | Test Pass% | Δ |
|---|---|---|---|
| gold | 100.0% | 100.0% | 0 |
| boundary_removal | 59.2% | 41.7% | -17.5pp |
| off_by_one | 83.5% | 70.5% | -13.0pp |
| operator_swap | 55.7% | 50.4% | -5.3pp |
| return_value | 26.1% | 43.8% | +17.7pp |

同一 mutation type 的 pass rate 在 val/test 间也差异很大，说明底层 repo 构成不同导致 mutation 存活率不同。

---

## 3. Repo Composition — **根因**

| Repo | Val | Val% | Test | Test% | 状态 |
|---|---|---|---|---|---|
| django | 2770 | 29.7% | 3572 | 36.5% | 两边都有 |
| **sympy** | **1780** | **19.1%** | **105** | **1.1%** | val 独占 |
| matplotlib | 1760 | 18.9% | 1572 | 16.1% | 两边都有 |
| **pylint** | **1134** | **12.1%** | **0** | **0.0%** | **val-exclusive** |
| astropy | 680 | 7.3% | 1071 | 10.9% | 两边都有 |
| **scikit-learn** | **585** | **6.3%** | **46** | **0.5%** | val 独占 |
| pytest | 477 | 5.1% | 522 | 5.3% | 两边都有 |
| sphinx | 149 | 1.6% | 132 | 1.3% | 两边都有 |
| **xarray** | **0** | **0.0%** | **2322** | **23.7%** | **test-exclusive** |
| **requests** | **0** | **0.0%** | **442** | **4.5%** | **test-exclusive** |

关键数字：
- Val 中 37.5% 的样本来自 test 中几乎不存在的 repo（sympy 19.1% + pylint 12.1% + sklearn 6.3%）
- Test 中 28.2% 的样本来自 val 中完全不存在的 repo（xarray 23.7% + requests 4.5%）

---

## 4. Test Type (f2p vs p2p)

| | Val | Val% | Test | Test% |
|---|---|---|---|---|
| f2p | 2968 | 31.8% | 2320 | 23.7% |
| p2p | 6367 | 68.2% | 7464 | 76.3% |

Val 的 f2p 比例高 8.1pp。f2p 测试（fail-to-pass）是检测 patch 正确性的关键信号，p2p 更容易预测（mutation 通常不影响 pass-to-pass 测试）。

---

## 5. Sequence Length Estimate

从文件大小粗略估算：
- Val: 67MB / 9335 ≈ **7,184 bytes/sample**
- Test: 61MB / 9784 ≈ **6,202 bytes/sample**

Val 样本平均大 16%。这与 repo 构成有关——sympy/pylint 的 patch 可能更长。在不同 max_seq_length 下，truncation 比例会不同。

---

## 6. Reversal 根因诊断

### Split 策略的结构性缺陷

`split_swebench_data.py` 按 `instance_id` 做 stratified 80/10/10 split，**但仅按 majority label 分层，未按 repo 分层**。由于不同 repo 的 instance 数量差异大且随机 shuffle 不充分，导致 val 和 test 的 repo 构成严重不平衡。

### Reversal 机制

**8B s42（clean comparison, val@8192 vs test@8192）：**
- ckpt-600 在训练更多 step 后，更深地拟合了 training set 的 repo 分布
- Val 与 training set 共享大量 repo（sympy 19%, pylint 12%, sklearn 6%），所以过拟合 → val 指标上升
- Test 包含 28% 未见过的 repo（xarray 24%, requests 5%），ckpt-600 的 repo-specific 特征反而损害泛化
- ckpt-400 泛化更好 → test 上赢

**4B seed123（confounded, val@5120 vs test@2048）：**
- 除了上述 repo 分布问题外，还叠加了 seq_len confound
- val@5120 保留更多 context → 人为抬高 val 指标
- test@2048 截断更多信息 → 压低 test 指标
- 这使得 val 与 test 的可比性更差

### 最可能导致 reversal 的因素（按影响力排序）

1. **Repo 分布不匹配（主因）**：37.5% val 样本 → test 没有；28.2% test 样本 → val 没有。模型在 repo-specific pattern 上的学习在 val 上被奖励，在 test 上被惩罚。
2. **Mutation type 分布不匹配（派生因素）**：operator_swap 在 test 中占比翻倍（34% vs 19%），而 off_by_one 从 10% 降到 2%。这是 repo 分布差异的下游效应。
3. **对 4B 实验：seq_len confound（加剧因素）**：val@5120 vs test@2048 使比较不公平。

### 建议

如果要消除 reversal，**需要按 repo 分层的 stratified split**——确保每个 repo 在 train/val/test 中按比例分配，而不仅仅按 label 分层。

---
