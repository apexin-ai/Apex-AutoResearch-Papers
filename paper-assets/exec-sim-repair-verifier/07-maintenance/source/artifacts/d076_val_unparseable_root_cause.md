# D076: Val Set Unparseable Root Cause Analysis

## 结论

**Val unparseable 100% 由 prompt 截断引起。** 两个 problem_id 的 git diff 超过 2048 token 限制：

| Problem ID | 样本数 | Code 字符 | Tokens | @2048 | @4096 |
|---|---|---|---|---|---|
| sympy__sympy-14248 | 1406 | 18003-18007 | ~4947 | 截断→不可解析 | 截断→不可解析 |
| pytest-dev__pytest-5787 | 477 | 9808-9828 | ~2352 | 截断→不可解析 | 可容纳 |

**1406 + 477 = 1883 = 20.2% = 不可解析数量（精确匹配）。**

在 4096 限制下，只有 sympy 仍被截断：**1406 = 15.1%（精确匹配）。**

## 为什么 Test 不受影响

- Val/Test 的 problem_id **完全不重叠**（0 个共同 ID）
- Test 最长的 problem（pydata__xarray-6992, 2322 个样本）tokenize 后为 **2034-2047 tokens** — 刚好低于 2048 限制 1-14 个 token
- Test 只有 484 个样本被截断（4.9%），其中 132 个（1.35%）生成不含 "pass"/"fail" 的文本

## 截断机制

```
截断 prompt → 模型看到不完整 diff → 继续补全代码而非回答 "pass/fail" → parse_prediction 找不到关键词 → 标记为 unparseable
```

即使 "截断但可解析" 的样本也是垃圾预测（test 中准确率仅 35.8%）— 生成的代码片段碰巧包含 "fail" 一词。

## 数据详情

### Val 长度分布

```
code 字符直方图:
     0-   500:  2119 (22.7%)
   500-  1000:  1061 (11.4%)
  1000-  2000:  2844 (30.5%)
  2000-  3000:   473 (5.1%)
  3000-  5000:   171 (1.8%)
  5000-  8000:   784 (8.4%)   ← django-13344, 1268 tokens, 不截断
  8000- 10000:   477 (5.1%)   ← pytest-5787, 2352 tokens, 截断@2048
 18000- 20000:  1406 (15.1%)  ← sympy-14248, 4947 tokens, 始终截断
```

### Tokenization 校准

| Code 字符 | Tokens | 字符/Token |
|---|---|---|
| 403 | 206 | 2.23 |
| 992 | 404 | 2.48 |
| 5084 | 1271 | 4.06 |
| 9808 | 2350 | 4.22 |
| 18003 | 4864 | 3.74 |

### Val problem_id 全览（22 个，按 code 长度降序）

```
sympy__sympy-14248:        n=1406, code=18003-18007, labels={0:488, 1:918}
pytest-dev__pytest-5787:   n=477,  code=9808-9828,   labels={1:268, 0:209}
django__django-13344:      n=784,  code=5084-5088,   labels={1:782, 0:2}
scikit-learn-14496:        n=171,  code=3809,         labels={1:171}
django__django-15732:      n=429,  code=2828-2834,    labels={0:143, 1:286}
... 17 more, all < 2600 chars ...
```

### 训练影响

训练脚本 (`train_repo_verifier.py`) 也用 `max_seq_length=2048`。截断的训练样本 labels 全为 -100（masked），**模型从截断样本学不到任何东西**。Train 有 ~3.2% 的 code >= 8000 字符，这些训练样本相当于被浪费了。

## 修复方案

### 推荐：增大 eval max_seq_length 到 5120

```bash
python eval_repo_cls.py \
  --checkpoint_dir <ckpt> \
  --split val \
  --max_seq_length 5120 \
  --batch_size 8
```

- Val 最长样本 = 4947 tokens，5120 可容纳全部
- Qwen3-4B bf16 ≈ 8GB model + ~3GB KV cache @5120 → 5090 可行
- 无数据损失，无代码改动（仅 CLI 参数）
- batch_size 可能需要从 16 降到 8 以适应更长序列

### 备选 1：过滤长样本

从 val 中移除 sympy-14248 和 pytest-5787：
- 损失 1883/9335 = 20.2% 的 val 样本
- 剩余 7452 样本 0% truncation/unparseable
- 缺点：改变 val 集分布，可能引入选择偏差

### 备选 2：训练+评估都增大 max_seq_length

如果重新训练：
- 训练 max_seq_length=5120，让模型学习全部样本
- 评估也用 5120
- 最彻底，但需要重新训练

## Checkpoint Selection 可行性

使用推荐修复（max_seq_length=5120）后：
- Val 0% unparseable
- Val 可靠用于 checkpoint selection（D063 要求达成）
- 无需额外改动
