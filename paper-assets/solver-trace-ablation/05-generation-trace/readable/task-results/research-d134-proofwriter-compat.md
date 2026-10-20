# research d134 proofwriter compat

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d134-proofwriter-compat_20260518T105841_result.json`
- **Structured JSON:** [`af4ac353db9611a45493.json`](../../sessions/af/af4ac353db9611a45493.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have complete understanding of the pipeline and both datasets. Here's the assessment:

---

```
=== 现有 Pipeline 总结 ===

数据格式: JSONL，字段 {id, context, question, answer, fol_premises, fol_conclusion, depth}
数据来源: FOLIO 数据集 (ID: folio_xxx)
FOL 语法: Unicode 符号 (∀, ∃, →, ¬, ∧, ∨, ↔, ⊕) + predicate-argument 语法
Pipeline 流程:
  1. 模型接收 NL context+question → 生成 FOL formalization
  2. _parse_formalization() 解析生成的 FOL 为 premises+conclusion
  3. Prover9Solver._normalize_fol() 将 Unicode → Prover9 ASCII (all/exists/-/&/|/->)
  4. decompose_fol() 将 FOL 拆解为可消融的 FOLComponent
  5. run_sta() 逐个移除 component → Prover9 重证 → 计算 ISR

关键发现: eval_sta.py 的 ISR 计算不依赖 gold FOL 字段。
模型从 NL 生成 FOL，STA 对模型输出做消融。
因此新数据集只需提供 NL context + question + answer 即可跑 ISR diagnostic eval。
Gold FOL 字段仅在 GRPO 训练时间接有用（模型自己生成 FOL 计算 reward）。


=== ProofWriter ===

数据格式: 控制英语的 facts/rules + query，无原生 FOL 标注
  - Facts: "The cat is young." / "The cow is round."
  - Rules: "If something is young then it is nice."
  - Query: "The cat is nice." + label (True/False/Unknown)
  原始 JSON: 非标准格式 "$answer$ ; $proof$ ; $question$ = ... ; $context$ = sent1: ... sent2: ..."

FOL 语法: 原始数据无 FOL。
  衍生数据集 ProofFOL 有 GPT-4o 生成的 Prover9 格式 FOL（经 Prover9 验证），
  但 ProofFOL 仓库 (github.com/RamyaKeerthy/ProofFOL) 返回 404，公开可用性存疑。

与 Prover9 兼容: 是（如果有 FOL 翻译）
  ProofWriter 的 NL 是 Datalog 风格的控制语言，语法高度规则化。
  模型生成的 FOL 经 _normalize_fol() 转 Prover9 语法后可直接使用。
  问题复杂度低于 FOLIO（大多为简单一元/二元谓词 + 链式推理）。

与 decompose_fol 兼容: 是
  ProofWriter 的 FOL 结构（∀x(P(x)→Q(x))、P(a)、链式蕴含）
  完全在 decompose_fol 的解析能力范围内。

适配工作量: 4-8 小时
  1. 下载 ProofWriter 数据 (HuggingFace/AllenAI): ~30min
  2. 格式转换脚本 (→ JSONL {id, context, question, answer}): ~2h
  3. 验证 eval_sta.py 能跑通: ~1h
  4. [可选] 如需 gold FOL 用于训练，需 GPT-4o 翻译 + Prover9 验证: ~1天
  
推荐: 可用（eval-only 半天内可完成；如需训练数据含 gold FOL 则需额外 1 天）


=== PrOntoQA ===

数据格式: 合成 QA，基于 ontology 树生成
  - NL: "Rex is a cat." / "Every cat is a mammal." / "True or false: Rex is a mammal."
  - 内部有完整 FOL 表示（TPTP 格式）

FOL 语法: TPTP 格式
  - 量词: ![X]: (全称), ?[X]: (存在)
  - 连接词: & (合取), | (析取), ~ (否定), => (蕴含), <=> (等价)
  - 谓词: cat(rex), mammal(X) — 大多为一元谓词
  示例: ![X]: (cat(X) => mammal(X))

与 Prover9 兼容: 需简单转换
  TPTP → Prover9 映射完全确定:
    ![X]: → all X    ?[X]: → exists X
    ~      → -        =>    → ->
    &      → &        |     → |
  转换器 ~50 行 Python。

与 decompose_fol 兼容: 是
  PrOntoQA 结构非常简单：
  - premises: 一元谓词事实 + 全称蕴含规则
  - conclusion: 一元谓词断言
  - 推理链: 线性（1-5 hop），无分支
  decompose_fol 完全可处理。

适配工作量: 3-6 小时
  1. 用 PrOntoQA 生成器生成数据 (pip install + run_experiment.py): ~1h
  2. 提取 NL + FOL 字段，格式转换为 JSONL: ~2h
  3. TPTP→Unicode 转换器（如需 gold FOL）: ~1h
  4. 验证 eval_sta.py 跑通: ~1h

推荐: 可用（最容易适配的候选。FOL 原生可用，结构简单，生成器可控制复杂度）


=== 总结建议 ===

                    ProofWriter         PrOntoQA
原生 FOL            ✗ (需翻译)          ✓ (TPTP 格式)
Prover9 兼容        ✓ (翻译后)          ✓ (简单映射)
decompose_fol 兼容  ✓                   ✓
推理复杂度          depth 0-5, Datalog  1-5 hop, 线性链
谓词复杂度          简单                极简（一元为主）
eval-only 适配      4-8h                3-6h
含 gold FOL 适配    +1天                +1h
代码改动            无（仅数据格式）    无（仅数据格式）

优先级建议:
1. PrOntoQA 优先：有原生 FOL、生成器可控、结构最简单、适配最快
2. ProofWriter 次之：NL-only 需要 FOL 翻译步骤，但问题域更贴近 FOLIO

两个数据集都不需要改 STA pipeline 代码，只需写数据格式转换脚本。
用现有 checkpoint 做 ISR diagnostic eval 预计每个数据集 100 样本 ~30-60 分钟（含推理+Prover9 消融）。
```

---
