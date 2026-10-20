# ProofWriter30 v2 进度报告

**时间**: 2026-05-16 09:20 UTC（实验运行 ~3h）
**状态**: 运行中 (PID 155077)

## 进度

- **已完成**: 16/30 题
- **当前**: [17/30] ProofWriter_RelNoneg-OWA-D5-31_Q12
- **平均耗时**: 668s/题 (≈11.1 min)
- **预估剩余**: 14题 × 668s ≈ 2.6 小时（约 11:50 UTC 完成）
- **无 400 Bad Request 错误**（v1 的 max_tokens 问题已修复）

## 准确率 (16/30)

| 方法 | 正确 | 准确率 |
|------|------|--------|
| **SICA** | 14/16 | **87.5%** |
| **SC** | 15/16 | **93.75%** |

SICA 错误的 2 题：
- **#5** (gold=True): sica_scores={False:0, True:0}，无可用不变量，tie-break 选错。SC 也错（7/12 投 False）
- **#11** (gold=False): sica_scores={False:27, True:38}，SICA 选了高分的 True（错），SC 11/12 投 False（对）

## Multi-candidate Rate

**3/16 = 18.75%** 的题出现多候选答案：

| 题号 | Gold | 候选 | SICA Scores | SICA | SC |
|------|------|------|-------------|------|----|
| #5 | True | 2 | {F:0, T:0} | F ✗ | F ✗ |
| #11 | False | 2 | {F:27, T:38} | T ✗ | F ✓ |
| #14 | False | 3 | {U:0, F:0, T:0} | F ✓ | F ✓ |

关键发现：3 个多候选题中有 2 个不变量得分全为 0（invariant extraction 失败），SICA 退化为随机 tie-break。

## 不变量提取质量

- **"No JSON found" 警告**: 99 次（约 51.6% 的 trace 未产生可解析 JSON）
- **unique_after_dedup = 0 的题**: 3/16（#4, #5, #14），表示完全无可用不变量
- Scorer satisfied_ratio 在有不变量时始终为 1.000

## 问题分析

核心问题：**QwQ-32B 在 ProofWriter D5 上的 invariant extraction 成功率偏低**。当 trace 无法产出结构化 JSON 时，extraction 阶段无法提取不变量，SICA 退化为无信号状态。这是 SC 暂时领先的主要原因——SC 不依赖 extraction 质量，直接用 majority vote。

Problem #11 更值得关注：invariant extraction 成功了（产出了 21 条不变量），但 SICA 选了错误答案（True=38 > False=27）。这说明不变量本身对 True 答案有偏见，可能因为部分不变量来自错误推理链。
