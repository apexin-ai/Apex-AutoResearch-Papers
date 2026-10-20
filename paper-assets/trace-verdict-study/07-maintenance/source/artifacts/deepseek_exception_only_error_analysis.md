# DeepSeek Exception-Only 额外错误分析

## 错误总览

| ID | Problem | Label | Pred | Exception Type | 错误类型 |
|----|---------|-------|------|----------------|----------|
| 540 | MBPP/113 | pass | fail | ValueError (caught) | DeepSeek-only |
| 541 | MBPP/113 | pass | fail | ValueError (caught) | DeepSeek-only |
| 542 | MBPP/113 | pass | fail | ValueError (caught) | DeepSeek-only |
| 543 | MBPP/113 | pass | fail | ValueError (caught) | DeepSeek-only |
| 548 | MBPP/113 | pass | fail | ValueError (caught) | DeepSeek-only |
| 549 | MBPP/113 | pass | fail | ValueError (caught) | DeepSeek-only |
| 901 | HumanEval/95 | pass | fail | GeneratorExit (internal) | Irreducible (all models) |
| 905 | HumanEval/95 | pass | fail | GeneratorExit (internal) | Irreducible (all models) |

**所有 8 个错误模式相同**：label=pass 被预测为 fail。即模型看到 `[ERROR]` 就倾向于判定失败。

## 额外错误根因分析

### MBPP/113 (6个额外错误)

代码：
```python
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
```

Trace: `[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python' | locals: s='python'`

**根因**：这是一个经典的 "caught exception" 模式。`ValueError` 被 `except` 显式捕获，是正常控制流的一部分。代码完全正确，通过所有测试。但 DeepSeek 看到 `[ERROR]` 标记就判定 fail。

6 个样本是同一个 solution 的 6 份副本（MD5 hash 一致），对应 MBPP/113 的 try/except 实现。同一 problem 还有 4 个不同 solution（使用 `.isdigit()`），trace 显示 `[No exception data in trace]`，DeepSeek 全部正确。

### HumanEval/95 (2个共享错误)

代码使用 `all(isinstance(k, str) and k.islower() for k in keys)` — Python 内部在 `all()` 短路时对 generator 触发 `GeneratorExit`。这不是用户代码的 bug，是 Python 运行时实现细节。

**比 MBPP/113 更难**：代码中没有显式 try/except，GeneratorExit 是隐式的 Python 内部机制。

## 跨 Seed 一致性

| 模型 | seed42 | seed123 | seed456 | 结论 |
|------|--------|---------|---------|------|
| DeepSeek MBPP/113 (6) | 6/6 fail | 6/6 fail | 6/6 fail | **100% 一致失败** |
| DeepSeek HumanEval/95 (2) | 2/2 fail | 0/2 fail | 2/2 fail | 2/3 seeds 失败 |
| Qwen MBPP/113 (6) | 0/6 fail | 0/6 fail | 0/6 fail | **100% 一致正确** |
| Qwen HumanEval/95 (2) | 2/2 fail | 2/2 fail | 2/2 fail | **100% 一致失败** |

## 训练数据分析

训练集（4720 样本）中 `[ERROR]` + label=pass 的"caught exception"样本：**仅 14 个 (0.30%)**

| Exception 类型 | 训练样本数 | 测试样本数 |
|---------------|-----------|-----------|
| GeneratorExit | 10 | 2 |
| ValueError | 3 | 6 |
| StopIteration | 1 | 0 |

极端类别不平衡（14/4720 = 0.3%）使得 `[ERROR] → fail` 成为压倒性主导模式。

## Qwen vs DeepSeek 对比

| 维度 | Qwen-7B | DeepSeek-6.7B |
|------|---------|---------------|
| 总错误数 | 2 | 8 |
| Accuracy | 99.83% | 99.33% |
| ValueError caught | ✅ 正确 | ❌ 全错 |
| GeneratorExit | ❌ 全错 | ❌ 全错 |
| 训练参数 | 3ep, lr=2e-4, bs=4 | 相同 |
| Token 膨胀率 | 1.0x (基准) | 1.21-1.32x |

## 结论

1. **根因是 "caught exception" 模式识别能力差异**，不是 tokenizer 长度问题（输入仅 128/103 tokens，远未截断）
2. **DeepSeek 对 `[ERROR]` 有更强的 fail bias**：即使 try/except 清晰可见，仍判 fail。Qwen 能从训练集中仅 3 个 ValueError 样本学到"try/except 捕获 = pass"的规则
3. **GeneratorExit 对所有模型都是 irreducible error**：Python 内部机制太隐晦，无法仅从 exception trace 推断
4. **训练数据的 0.3% caught-exception 比例是根本瓶颈**：如需改善，应增加 caught-exception 训练样本
5. **6 个"额外错误"实质上是 1 个独特错误的 6 份重复**（同一 problem 同一 solution 的数据集重复）
