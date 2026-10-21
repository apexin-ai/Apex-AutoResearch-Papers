# Silent Logic Error Analysis (N3 fix)

## 数据集统计
- Total test samples: 1190
- Pass: 851 (71.5%)
- Fail: 339 (28.5%)

## Fail 样本分类

按 exception 来源将 fail 样本分为三类：

| 类别 | 数量 | 占比 | 说明 |
|------|------|------|------|
| AssertionError (silent logic error) | 188 | 55.5% | 代码本身正常运行，但输出错误，测试 assert 失败 |
| Code crash (TypeError/NameError/...) | 81 | 23.9% | 代码执行时抛出异常 (TypeError 53, NameError 21, AttributeError 5, StopIteration 2) |
| No trace available | 70 | 20.6% | trace 收集失败 |

**关键发现**：超过半数 (55.5%) 的 fail 样本是 silent logic error，代码不崩溃但产生错误结果。

## 各 condition 对 silent error 的预测 recall

| Condition | AssertionError (n=188) | Code crash (n=81) | Gap |
|-----------|----------------------|-------------------|-----|
| no_trace | 62.8% | 98.8% | +36.0pp |
| exception_only | 100.0% | 100.0% | 0.0pp |
| ae_only | 100.0% | 100.0% | 0.0pp |
| loop_only | 67.6% | 100.0% | +32.4pp |
| full_trace | 50.0% | 88.9% | +38.9pp |
| vota | 100.0% | 100.0% | 0.0pp |

## 分析

1. **Silent logic error 是最难的 fail 子类**：no_trace 和 loop_only 对 code crash 接近 100% recall，但对 silent error 仅 ~63-68%。full_trace 更差，仅 50%。

2. **exception_only 对 silent error 有效**：尽管名为 "exception_only"，该 condition 对 188 个 AssertionError 样本 recall 100%。原因是 exception_only 提供了 `[ERROR] AssertionError at line N: | locals: ...` 信息，虽然代码本身没 crash，但测试框架的 AssertionError 被 trace 系统捕获并展示给模型。

3. **full_trace 在 silent error 上最弱 (50%)**：full_trace 提供完整变量快照但不标注 `[ERROR]`，模型需要从变量值推断输出是否正确，这比直接看 error tag 困难得多。

4. **no_trace 对 code crash 的高 recall (98.8%)** 说明：代码结构特征已足以预测大多数 crash 类型错误（如类型不匹配的操作），但无法预测 silent 逻辑错误。

## 对 Reviewer N3 的回应要点

- 数据集中 55.5% 的 fail 是 silent logic error（代码运行无异常，输出错误）
- exception_only 之所以对这类样本有效，是因为 trace 系统捕获了测试框架的 AssertionError（测试级异常，非代码级异常）
- 真正无任何异常信息的 condition（no_trace, loop_only）对 silent error 的 recall 显著低于 code crash（差距 32-38pp），证实了 silent logic error 确实更难判定
- full_trace 在 silent error 上的 50% recall 说明：仅提供变量快照而不标注错误，模型难以正确判断
