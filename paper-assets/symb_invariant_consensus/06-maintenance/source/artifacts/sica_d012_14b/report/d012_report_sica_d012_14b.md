## D012 全量评估报告 — sica_d012_14b

### 总览
- 模型: Qwen2.5-14B-Instruct (vLLM local)
- 数据: ProofWriter-30 + FOLIO-30 (60 题)
- K=12, T=0.7, max_tokens=4096, seed=42
- 总运行时间: 58.3 min (avg 58.3s/problem)
- 运行时间: 2026-05-16 12:05 ~ 13:03

### D012 四项指标

| 指标 | 值 | 阈值 | 判定 |
|------|-----|------|------|
| C0 多候选率 | 53.3% (32/60) | ≥20% | **PASS** |
| C1 约束提取率 | 100.0% (720/720 traces) | ≥50% | **PASS** |
| C2 矛盾检出 | 34 题 (excluded>0) | ≥5 | **PASS** |
| C3 SICA-SC gap | +3.3pp (73.3% vs 70.0%) | ≥+2pp | **PASS** |

Bootstrap p-value: 0.226 (未达 p<0.1 显著性，但 gap 已满足 +2pp 阈值)

### D012 最终判定: **ALL PASS**

---

### 分域统计

| Dataset | N | SICA Acc | SC Acc | Gap | C0 多候选 | C2 矛盾检出 |
|---------|---|----------|--------|-----|-----------|-------------|
| ProofWriter | 30 | 66.7% (20/30) | 66.7% (20/30) | +0.0pp | 60.0% (18/30) | 19 题 |
| FOLIO | 30 | 80.0% (24/30) | 73.3% (22/30) | +6.7pp | 46.7% (14/30) | 15 题 |

**关键观察**: SICA 的优势完全来自 FOLIO 数据集 (+6.7pp)，ProofWriter 上两者持平。

### 约束系统统计

| 指标 | 值 |
|------|-----|
| 总原始约束 | 5,849 |
| 去重后唯一约束 | 1,735 |
| 去重比例 | 29.7% (保留率) |
| 平均每题原始约束 | 97.5 |
| 平均每题唯一约束 | 28.9 |
| MaxSAT 满足数 | 1,690 |
| MaxSAT 排除数 | 45 |
| 排除率 | 2.59% |
| Answer extraction | 100% (720/720 boxed, 0 fallback, 0 none) |
| Truncated traces | 0 |

### 一致性矩阵

| | SC 正确 | SC 错误 |
|---|---|---|
| **SICA 正确** | 41 | 3 |
| **SICA 错误** | 1 | 15 |

Net SICA advantage: +2 题 (3 wins - 1 loss)

### SICA vs SC 差异题详细分析

#### SICA 胜出 (3 题)

| ID | GT | SICA | SC | 机制 |
|----|-----|------|-----|------|
| ProofWriter_RelNeg-OWA-D5-813_Q17 | Unknown | Unknown ✓ | False ✗ | 6:6 tie, 排除1约束后 SICA 选 Unknown |
| folio_012 | False | False ✓ | Unknown ✗ | 6:6 tie, 排除1约束后 SICA 选 False |
| folio_029 | Unknown | Unknown ✓ | False ✗ | 6:6 tie, 排除1约束后 SICA 选 Unknown |

#### SC 胜出 (1 题)

| ID | GT | SICA | SC | 机制 |
|----|-----|------|-----|------|
| ProofWriter_AttNeg-OWA-D5-347_Q11 | True | Unknown ✗ | True ✓ | 6:6 tie, 排除1约束后 SICA 错选 Unknown |

**模式**: 4 题差异全部发生在 6:6 投票平局场景。SICA 通过约束加权打破平局，3/4 次正确。SC 在 tie 时随机选择（取字典序首个或随机），仅 1/4 次碰巧正确。

### 最接近投票的 10 题 (margin ≤ 2)

| ID | GT | SICA | SC | Votes | Excl |
|----|-----|------|-----|-------|------|
| ProofWriter_AttNeg-OWA-D5-347_Q11 | True | Unknown ✗ | True ✓ | T:6 U:6 | 1 |
| ProofWriter_AttNoneg-OWA-D5-20_Q10 | False | False ✓ | False ✓ | T:2 F:5 U:5 | 3 |
| ProofWriter_RelNeg-OWA-D5-813_Q17 | Unknown | Unknown ✓ | False ✗ | F:6 U:6 | 1 |
| folio_012 | False | False ✓ | Unknown ✗ | F:6 U:6 | 1 |
| folio_029 | Unknown | Unknown ✓ | False ✗ | F:6 U:6 | 1 |
| ProofWriter_RelNeg-OWA-D5-498_Q8 | False | True ✗ | True ✗ | T:6 F:1 U:5 | 3 |
| ProofWriter_RelNeg-OWA-D5-173_Q10 | False | False ✓ | False ✓ | F:7 U:5 | 2 |
| ProofWriter_RelNoneg-OWA-D5-251_Q10 | False | Unknown ✗ | Unknown ✗ | F:5 U:7 | 1 |
| ProofWriter_AttNoneg-OWA-D5-500_Q8 | False | False ✓ | False ✓ | F:7 U:5 | 1 |
| ProofWriter_RelNeg-OWA-D5-721_Q8 | False | False ✓ | False ✓ | T:1 F:7 U:4 | 3 |

### 关键发现

1. **SICA 的优势集中在 tie-breaking**: 所有差异题都是 6:6 平局，SICA 用约束权重正确打破了 3/4 次平局。
2. **FOLIO 受益更大**: FOLIO 的自然语言推理更容易产生分歧（Unknown vs False/True 边界模糊），SICA 约束加权在此类场景有效。
3. **ProofWriter 多候选但无 gap**: ProofWriter 虽然 60% 题有多候选（高于 FOLIO 的 46.7%），但 SICA 和 SC 在该域持平，说明多候选不一定导致 accuracy 差异。
4. **约束提取极其可靠**: 100% trace 成功提取约束，表明 14B 模型生成的 CoT 结构化程度高。
5. **排除率适中 (2.59%)**: 既有矛盾检出能力，又不会过度排除导致信息丢失。
6. **统计显著性不足**: bootstrap p=0.226，样本量(60题)下 +2 题的差异难以达到统计显著。需要更大样本或更极端场景来确认 SICA 的可靠优势。
