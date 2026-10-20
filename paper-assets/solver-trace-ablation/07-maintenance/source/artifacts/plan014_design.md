# Plan014: Downstream Validation — 打破 ISR 循环论证

> 更新: 2026-05-14 | Dream M2/W4 必修 | DDL: 2026-05-25

## 问题

我们用 ISR 训练模型，又用 ISR 评估 → 循环论证。需要**独立于 ISR 的外部标准**证明高 ISR formalization 确实更好。

---

## 方案 A: NLI Label Accuracy（推荐，代码已就绪）

### 原理
用生成的 FOL 做 3-way 蕴含分类（true/false/unknown），与 gold label 对比。NLI 准确率完全独立于 ISR。

### 核心论证
ISR 衡量 "每个 premise 是否 necessary"；Label accuracy 衡量 "formalization 是否正确捕获语义"。两者正交。若高 ISR → 高 label accuracy，则 ISR 是 genuine quality proxy。

### 代码状态
**`scripts/eval_downstream.py` 已完整实现**，包含：
- Phase 1: 加载 checkpoint，生成 K 个 formalizations（temperature sampling）
- Phase 2: 3-way 分类：prove(premises→conclusion) + prove(premises→¬conclusion)
- Phase 3: Full STA ISR 计算（per formalization）
- Aggregation: ISR bucket 分组（high>0.7, mid 0.3-0.7, low<0.3）+ ISR quartile 分组
- Best-of-N: oracle / ISR-best / random / prove-first 四策略对比
- 按 gold label 类型分组统计

**待补充**（~20 行）：
1. `scipy.stats.spearmanr(ISR, correct)` — ISR 与 NLI 正确性的秩相关系数
2. `scipy.stats.mannwhitneyu` — ISR quartile 间 accuracy 差异显著性检验
3. Bootstrap 95% CI for BoN accuracy differences

### 输入
- Checkpoint: exec-only / exec+STA / random-reward（各 500 步训练后的 checkpoint）
- 测试集: `data/test_held_out.jsonl`（100 条，symlink → test_100.jsonl）
- K=8 generations per sample, temperature=0.7, top_p=0.9

### 运行命令
```bash
python scripts/eval_downstream.py \
    --checkpoint_path outputs/plan001-exec-only-s42/checkpoint-500 \
    --data_path data/test_held_out.jsonl \
    --output_path results/plan014_downstream_exec_only.json \
    --num_generations 8 --workers 4
```

### 评估指标（全部独立于 ISR）
| Metric | 定义 | 预期 |
|--------|------|------|
| Spearman ρ(ISR, correct) | ISR 与 label correctness 秩相关 | ρ > 0.3, p < 0.05 |
| BoN(ISR-best) | ISR-best 选择的 label accuracy | > Random |
| Δ accuracy (Q4 − Q1) | ISR top vs bottom quartile accuracy 差 | > 0, p < 0.05 |
| Overall NLI accuracy | 全部 generations 的 label accuracy | — |

### 预期结果解读
- **ISR 有效**: ρ≥0.3 + BoN(ISR) > BoN(Random) by ≥5pp → ISR captures genuine quality
- **弱信号**: ρ∈(0.15,0.3) → ISR provides modest quality signal beyond provability
- **ISR 无效**: ρ≤0.15 → ISR 只反映 solver 内部结构，不预测语义正确性

### 资源
- GPU: ~1.5h/checkpoint × 3 checkpoints = ~4.5h（inference 阶段）
- CPU: ~30min/checkpoint（solver eval，可 multiprocess 并行）
- 代码改动: ~20 行添加统计检验

---

## 方案 B: Cross-Solver Agreement（零 GPU 成本补充）

### 原理
同一 FOL formalization 用 Prover9 和 Z3 分别验证。高 ISR formalization 若在两个 solver 上都一致，说明不是 solver-specific artifact。

### 核心假设
- 高 ISR formalization 跨 solver agreement 更高
- 低 ISR formalization 可能在 Prover9 上 provable 但在 Z3 上 fail（偶然正确）

### 代码状态
- Prover9 和 Z3 solver **已实现**（`src/solvers/prover9.py`, `src/solvers/z3_solver.py`）
- Z3Solver 有完整的 FOL parser（支持 ProofWriter 语法：∀/∃/→/∧/∨/¬）
- Z3Solver 额外有 `check_consistency()` 方法
- **需新建**: `scripts/eval_cross_solver.py`（~150 行）

### 输入
复用方案 A 的 formalization 输出 JSON（无需额外 GPU inference）

### 评估指标
| Metric | 定义 |
|--------|------|
| Cross-solver agreement | Prover9 与 Z3 判定一致的比例 |
| Agreement by ISR bucket | 高/中/低 ISR 的 agreement 分组对比 |
| Unanimous prove rate | 两个 solver 同时 prove 的比例 |

### 注意事项
- Z3 的 FOL parser 是 ProofWriter 子集，可能对模型生成的 FOL 有 parse error → 需报告 parse error rate 作为 confound
- SWI-Prolog 需要 Prolog 语法（非 FOL），仅在 Prolog-trained checkpoint 上可用，本次暂不纳入

### 实施步骤
```
1. 读取方案 A 输出的 JSON（含 parsed premises + conclusion）
2. 对每个 formalization 调 Z3Solver.prove(premises, conclusion)
3. 比较 Prover9 result vs Z3 result
4. 按 ISR bucket 分组输出 agreement 统计
```

### 资源
- GPU: **0**（纯 CPU solver 调用）
- CPU: ~1h（100 × 8 × Z3 prove，每个 <1s）
- 代码: ~150 行新脚本
- **依赖**: 方案 A 已运行

---

## 方案 C: Perturbation Sensitivity（高复杂度，DDL 风险）

### 原理
对 NL premise 做语义扰动（删除关键 premise / 添加无关 premise），重新生成 formalization。好的 formalization 应对关键扰动敏感、对噪声鲁棒。

### 扰动类型
1. **Premise deletion**: 随机删除 context 中一条 NL 句子，重新生成 FOL
2. **Irrelevant insertion**: 添加一条与主题无关的 NL 句子，重新生成 FOL

### 评估指标
| Metric | 定义 | 预期（高 ISR） |
|--------|------|--------------|
| Δ prove_rate (deletion) | 删 premise 后 prove_rate 下降 | 下降更大（premise 必需） |
| Δ ISR (insertion) | 加噪声后 ISR 变化 | 下降更小（鲁棒） |

### 风险
- GPU 时间大: ~3h/checkpoint × 2 扰动类型 × 3 checkpoints = ~18h
- 设计复杂: 需精心选择哪些 premise 是"关键"的（circular：需要 STA 本身来判断）
- 模型对扰动后 context 的生成质量下降可能掩盖信号
- **结论: DDL 11 天内风险过高，不推荐**

---

## 推荐方案: A + B 组合

### 理由
1. **方案 A**: 代码 80% 就绪（eval_downstream.py 已完整实现），改动 ~20 行，直接回应审稿人
2. **方案 B**: 零 GPU 成本，复用方案 A 输出，补充 solver-independence 证据
3. **两者互补**: A 证明语义正确性，B 证明非 solver artifact
4. **方案 C** GPU 预算过大（18h），设计复杂，DDL 风险高

### Timeline（DDL: 2026-05-25）

| 日期 | 任务 | 依赖 | GPU |
|------|------|------|-----|
| 5/14 | eval_downstream.py 添加 Spearman + Mann-Whitney | — | 0 |
| 5/15 | 跑方案 A: exec-only checkpoint | checkpoint 就绪 | 1.5h |
| 5/16 | 跑方案 A: exec+STA + random-reward | checkpoint 就绪 | 3h |
| 5/16 | 编写 eval_cross_solver.py | — | 0 |
| 5/17 | 跑方案 B: cross-solver eval | 方案 A 输出 | 0 |
| 5/18 | 分析结果 + 图表 | A+B 完成 | 0 |

**总 GPU 成本**: ~4.5h（仅 inference）
**总 CPU 时间**: ~4h（solver eval）
**代码改动**: ~170 行（20 行修改 + 150 行新脚本）

### 输出文件
```
results/plan014_downstream_exec_only.json
results/plan014_downstream_exec_sta.json
results/plan014_downstream_random.json
results/plan014_cross_solver.json
artifacts/plan014_isr_nli_correlation.pdf
```

### 论文写法
- Section: "External Validation of ISR" 或 "Does ISR Predict Formalization Quality?"
- Table: ISR bucket × NLI accuracy × checkpoint type
- Figure: ISR vs NLI accuracy scatter + regression line
- Key claim: *"Formalizations with higher ISR achieve X% higher NLI accuracy (Spearman ρ=Y, p<0.001), demonstrating that ISR captures genuine formalization quality beyond proof success."*
- Cross-solver: *"High-ISR formalizations show Z% higher cross-solver agreement, confirming that ISR reflects solver-independent structural quality."*

---

## 关键依赖

| 依赖 | 状态 | 备选 |
|------|------|------|
| exec-only checkpoint (plan001-s42) | 训练中/失败修复中 | 用 r5 的 100-step checkpoint |
| exec+STA checkpoint (plan002) | 待 plan005 确定权重 | 用 plan005 的 checkpoint |
| random-reward checkpoint (plan013) | 训练中 | 延后运行 |
| scipy (spearmanr, mannwhitneyu) | 需确认已安装 | pip install scipy |
