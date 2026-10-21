# code plan006 eval readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-eval-readiness_20260514T102758_result.json`
- **Structured JSON:** [`a70fb822ff12523b44e6.json`](../../sessions/a7/a70fb822ff12523b44e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：eval_sta.py 完全兼容 Prolog，无需任何改动。**

关键发现：

1. **eval_sta.py 已原生支持 `--logic_type prolog`**，包含完整的 Prolog prompt 模板、reward 函数分发、solver 选择
2. **数据格式无障碍** — 脚本只读取 `context`/`question`/`answer`（自然语言字段），不依赖 `fol_premises`/`fol_conclusion`
3. **`prolog_sta_reward`（`src/sta/prolog_reward.py`）已完整实现** — 解析 Prolog clauses+query → 逐条 clause ablation → ISR 计算，返回与 FOL 相同的 reward dict 结构
4. **swipl 已安装**在服务器上（`/usr/lib/swi-prolog/bin/x86_64-linux/swipl`）
5. **指标计算完全通用** — PR, ISR, by_answer_type 等均从 reward dict 泛型计算

报告已保存至 `artifacts/plan006_eval_compatibility.md`，含两个实验的 eval 命令模板，训练完成后可直接使用。

---
