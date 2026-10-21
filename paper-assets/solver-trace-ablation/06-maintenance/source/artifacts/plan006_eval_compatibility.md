# plan006 Prolog 实验 eval_sta.py 兼容性报告

**日期**: 2026-05-14
**结论**: 完全兼容，无需任何代码改动

## 兼容性分析

### 1. 数据加载 — 兼容
- `load_data()` 是通用 JSONL loader，无格式假设
- main 循环只读取 `context`、`question`、`answer`（自然语言字段），均存在于 `train_500_seed42.jsonl`
- FOL 专有字段（`fol_premises`、`fol_conclusion`）eval_sta.py 从未访问

### 2. Logic Type 分发 — 已实现
`--logic_type prolog` 选择 `LOGIC_CONFIG["prolog"]`，包含：
- `PROLOG_SYSTEM_PROMPT` / `PROLOG_USER_TEMPLATE` — Prolog 专用 prompt
- `prolog_sta_reward` — Prolog STA reward 函数（来自 `src/sta/prolog_reward.py`）
- `"prolog"` — 默认 solver 名

### 3. Prolog STA Reward — 完整实现
`prolog_sta_reward` 流程：
1. `parse_prolog_formalization()` — 从模型输出解析 Prolog clauses + query（支持 `?-` 和 `Query:` 两种格式）
2. `prolog_sta_ablation()` — 逐条移除 clause，检查 query 是否失败（rule ablation）
3. `prolog_isr()` = necessary_clauses / total_clauses
4. 返回与 FOL 相同的 dict 结构：`execution_reward`, `sta_reward`, `combined_reward`, `details`

### 4. Solver — 已安装
- `PrologSolver` 调用 `swipl` 二进制
- swipl 已安装：`/usr/lib/swi-prolog/bin/x86_64-linux/swipl`
- `get_solver("prolog")` 正确返回 `PrologSolver`

### 5. 指标计算 — 通用
PR, mean_isr, isr_std, median_isr, isr_pr_ratio, proved_only_mean_isr, by_answer_type — 全部从 reward dict 通用计算，无 logic-type 依赖

## Prolog 数据格式样本（train_500_seed42.jsonl 前 2 条）

```json
{"id": "folio_473", "context": "Belgium, France, and Germany are European countries.\nParis is the capital of France.\n...", "question": "If John goes to Europe, he will see the Eiffel Tower.", "answer": "unknown", "fol_premises": ["EuropeanCountry(belgium) ..."], "fol_conclusion": "GoTo(john, europe) -> See(john, eiffelTower)", "depth": 3}

{"id": "folio_1181", "context": "Some employees in James's town who work in business analysis are good at math...", "question": "Leif is good at math.", "answer": "unknown", "fol_premises": ["..."], "fol_conclusion": "...", "depth": 2}
```

注意：数据中的 `fol_premises` / `fol_conclusion` 是 FOL 标注，eval_sta.py 不使用它们。Prolog 模式下模型根据 `context` + `question` 自行生成 Prolog formalization。

## 建议的 eval 命令模板

### plan006-prolog-exec-s42（exec_only 模型）
```bash
export CUDA_VISIBLE_DEVICES=<空闲GPU>
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation

python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/grpo_prolog_exec_only/checkpoint-<STEP> \
  --data_path data/test_100.jsonl \
  --logic_type prolog \
  --output_path results/plan006_prolog_exec_s42_eval.json
```

### plan006-prolog-sta-s42（exec+sta 模型）
```bash
export CUDA_VISIBLE_DEVICES=<空闲GPU>
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation

python scripts/eval_sta.py \
  --model_path /root/autodl-tmp/outputs/grpo_prolog_exec_sta/checkpoint-<STEP> \
  --data_path data/test_100.jsonl \
  --logic_type prolog \
  --output_path results/plan006_prolog_sta_s42_eval.json
```

### 注意事项
- 替换 `<空闲GPU>` 为实际可用 GPU 编号（遵守 C002/C005）
- 替换 `<STEP>` 为最终 checkpoint step 编号
- 评估数据用 `test_100.jsonl`（与 FOL 实验一致）
- 如需限制样本数用 `--max_samples N`
