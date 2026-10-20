# Eval Result: MATH-500 — SFT CKA-only 20% (fixed eval v2)

## 总准确率

| Metric | Value |
|--------|-------|
| Accuracy | **27.4%** (137/500) |
| Stderr | ±1.99% |
| 95% CI | [23.4%, 31.4%] |

## EOS 统计

| Metric | Value |
|--------|-------|
| Natural EOS | 384 (76.8%) |
| Truncated | 116 (23.2%) |
| Avg response length | 673.3 tokens |

## 错误/异常

- 运行正常，EXIT_CODE=0，无报错
- HuggingFace Hub 网络不可达（AutoDL 限制），自动回退到本地缓存数据集，不影响结果
- 23.2% 的回复被截断（达到 max_length=2048），可能略压低准确率

## 与 buggy 版本对比

| Version | Accuracy | 差异 |
|---------|----------|------|
| v1 (buggy eval) | 26.8% (134/500) | — |
| **v2 (fixed eval)** | **27.4% (137/500)** | +0.6pp |

差异仅 +0.6pp（3 题），在 stderr (±2.0%) 范围内，统计上无显著差异。说明之前的 eval bug 对 CKA-only 模型影响极小。

## 结论

**Status: SUCCESS（评估成功运行）/ NEGATIVE（结果本身偏低）**

- 27.4% 的 MATH-500 准确率确认了 CKA-only 剪枝策略的数学推理能力较弱
- 修复后的 eval 脚本验证了之前 26.8% 的结果基本可靠，非 bug 导致的异常低分
- 此结果可直接填入 tab_math500.tex 的 CKA-only SFT 行
