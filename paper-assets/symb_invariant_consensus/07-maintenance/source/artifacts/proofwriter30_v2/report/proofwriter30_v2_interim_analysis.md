# ProofWriter30 v2 中间分析 (16/30)

> 数据来源: `proofwriter_30_v2.json` (westd-32608), 截至 2026-05-16 09:17
> 当前进度: 完成 16/30，正在运行 #17 (RelNoneg-OWA-D5-31_Q12)

## D012 指标预估

- **C0 (多候选率)**: 3/16 = 18.75% — 仅 3 题出现 trace 间答案分歧 (T/F/U 不一致)
- **C1 (约束提取率)**: trace 级 93/192 = 48.4%；problem 级 13/16 = 81.25%（3 题完全提取失败）
- **C2 (矛盾检出)**: 0 题 — 所有 problem 的 satisfied_ratio=1.000，excluded=0，**未检测到任何跨路径矛盾**
- **C3 (SICA vs SC)**: SICA=14/16 (87.5%), SC=15/16 (93.75%), **gap = −6.25pp (SICA 落后)**

## "No JSON found" 警告分析

共 99 次 "No JSON found in response for trace" 警告。这是 **约束提取阶段**（constraint extraction）的失败，不是答案提取失败。所有 192 条 trace 均成功提取了答案（per_trace 中每条都有 answer 字段），但其中 99 条未能从 trace 中提取出 FOL 约束的 JSON 结构。

验证: traces_with_constraints 合计 = 93，失败 = 192 − 93 = 99，与警告数完全吻合。

## 每题详情表

| # | problem_id | gold | SICA | SC | SC votes | multi_candidate | twc/12 | constraints (te→ud) | sat/exc | sica_scores |
|---|-----------|------|------|-----|----------|-----------------|--------|---------------------|---------|-------------|
| 1 | AttNeg-D5-979_Q9 | True | True ✓ | True ✓ | 12/0/0 | No | 4 | 64→29 | 29/0 | {T:64} |
| 2 | RelNoneg-D5-1036_Q11 | True | True ✓ | True ✓ | 12/0/0 | No | 1 | 13→13 | 13/0 | {T:13} |
| 3 | AttNeg-D5-891_Q1 | True | True ✓ | True ✓ | 12/0/0 | No | 12 | 180→27 | 27/0 | {T:180} |
| 4 | AttNeg-D5-347_Q11 | True | True ✓ | True ✓ | 12/0/0 | No | **0** | 0→0 | 0/0 | {T:0} |
| **5** | **RelNoneg-D5-616_Q7** | **True** | **False ✗** | **False ✗** | **5/7/0** | **Yes** | **0** | **0→0** | **0/0** | **{T:0,F:0}** |
| 6 | AttNeg-D5-399_Q3 | True | True ✓ | True ✓ | 12/0/0 | No | 12 | 196→27 | 27/0 | {T:196} |
| 7 | RelNoneg-D5-173_Q11 | True | True ✓ | True ✓ | 12/0/0 | No | 3 | 36→12 | 12/0 | {T:36} |
| 8 | AttNoneg-D5-971_Q5 | True | True ✓ | True ✓ | 12/0/0 | No | 8 | 40→5 | 5/0 | {T:40} |
| 9 | AttNoneg-D5-702_Q1 | True | True ✓ | True ✓ | 12/0/0 | No | 12 | 55→25 | 25/0 | {T:55} |
| 10 | AttNoneg-D5-844_Q1 | True | True ✓ | True ✓ | 12/0/0 | No | 12 | 177→22 | 22/0 | {T:177} |
| **11** | **RelNeg-D5-498_Q8** | **False** | **True ✗** | **False ✓** | **0/11/1** | **Yes** | **4** | **41→21** | **21/0** | **{F:27,T:38}** |
| 12 | AttNoneg-D5-20_Q10 | False | False ✓ | False ✓ | 0/12/0 | No | 10 | 230→25 | 25/0 | {F:230} |
| 13 | RelNeg-D5-173_Q10 | False | False ✓ | False ✓ | 0/12/0 | No | 1 | 9→9 | 9/0 | {F:9} |
| **14** | **RelNoneg-D5-251_Q10** | **False** | **False ✓** | **False ✓** | **0/7/2+3U** | **Yes (3-way)** | **0** | **0→0** | **0/0** | **{U:0,F:0,T:0}** |
| 15 | RelNeg-D5-721_Q8 | False | False ✓ | False ✓ | 0/12/0 | No | 2 | 30→15 | 15/0 | {F:30} |
| 16 | AttNoneg-D5-500_Q8 | False | False ✓ | False ✓ | 0/12/0 | No | 12 | 115→26 | 26/0 | {F:115} |

> SC votes 列格式: True/False/Unknown。sica_scores 中 T=True, F=False, U=Unknown。

## 关键发现

### 1. SICA 反向翻转 (Problem #11)
**最严重问题。** SC 以 11:1 的压倒性多数正确投票 False，但 SICA 的约束加权评分将答案翻转为 True（F:27 vs T:38）。这说明从少数错误 trace 中提取的约束权重反而更高，导致 SICA 覆盖了 SC 的正确判断。

### 2. 约束提取完全失败导致 SICA 退化为 SC
Problem #4、#5、#14 约束提取率为 0（twc=0/12），SICA 完全退化为 SC 投票。其中 #5 和 #14 恰好是多候选题：
- **#5**: 7F:5T 分裂投票，无约束可用，SICA 跟随 SC 选了 False（错误）
- **#14**: 7F:2T:3U 三方分裂，无约束可用，SICA 跟随 SC 选了 False（正确但纯靠运气）

### 3. 零矛盾检出
16 题中没有检测到任何跨路径约束矛盾（satisfied_ratio 全为 1.000，excluded 全为 0）。这意味着 MaxSAT 求解器从未需要排除任何约束——要么约束太弱/太一致，要么矛盾检测的阈值需要调整。

### 4. 约束提取率两极分化
- 12/12（满分）: #3, #6, #9, #10, #16 — 5 题
- 0/12（完全失败）: #4, #5, #14 — 3 题
- 中间: 其余 8 题

## 风险评估

### D012 各标准 PASS 预测

| 标准 | 当前状态 | 30 题预测 | 风险 |
|------|---------|----------|------|
| C0 多候选率 | 3/16 = 18.75% | 预计 5-6/30 ≈ 17-20% | ⚠️ 偏低，多数题 unanimous |
| C1 约束提取率 | trace 级 48.4% | 预计维持 45-55% | ⚠️ 过半 trace 提取失败 |
| C2 矛盾检出 | 0/16 | 预计 0-1/30 | 🔴 **高风险 FAIL** |
| C3 SICA vs SC gap | −6.25pp | 预计 −3 ~ −6pp | 🔴 **高风险 FAIL — SICA 劣于 SC** |

### 核心问题

**SICA 在 16 题样本中严格劣于 SC**：SC 答对了 SICA 答错的题（#11），但 SICA 没有答对任何 SC 答错的题。唯一两者都错的题（#5）是因为模型本身在该题上就倾向错误答案。

根本原因：约束加权机制在少数有分歧的题上反而放大了错误——当少数 trace 的错误答案恰好伴随更多/更强的 FOL 约束时，SICA 会被误导。而在多数一致的题上，SICA 只是复制 SC 的结果。

**如果剩余 14 题保持类似分布，最终 SICA accuracy ≈ 87%，SC accuracy ≈ 93%，gap 约 −5pp。D012 C3 标准（SICA ≥ SC）极可能 FAIL。**
