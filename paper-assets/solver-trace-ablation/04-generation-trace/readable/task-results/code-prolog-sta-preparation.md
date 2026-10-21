# code prolog sta preparation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prolog-sta-preparation_20260513T230710_result.json`
- **Structured JSON:** [`1bd024d6a4e4da69c799.json`](../../sessions/1b/1bd024d6a4e4da69c799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出总结：

### 新建文件
| 文件 | 说明 |
|------|------|
| `src/solvers/prolog.py` | PrologSolver — 通过 swipl CLI 执行 Prolog 查询，exit code 0=proved / 1=failed / 2=syntax error，subprocess timeout 处理 |
| `src/sta/prolog_reward.py` | Prolog STA reward — 解析 Prolog formalization、逐条 ablation、ISR 计算、fast O(1) 近似 |
| `scripts/sta_prolog.py` | 独立测试 CLI，5 个内置测试用例，支持 `--test` / `--file` / `--fast` |
| `configs/grpo_prolog_exec_only.yaml` | execution-only GRPO 配置 |
| `configs/grpo_prolog_exec_sta.yaml` | execution+STA GRPO 配置 |

### 修改文件
| 文件 | 改动 |
|------|------|
| `src/solvers/factory.py` | 注册 `"prolog"` / `"swipl"` → PrologSolver |
| `scripts/train_grpo.py` | 新增 `--logic_type prolog`，Prolog system prompt/user template，`build_prolog_dataset()`，reward dispatch 根据 logic_type 切换 FOL/Prolog reward 函数 |

### 测试结果
- Full STA: **5/5 通过**（grandparent、redundant fact、missing fact、simple query、chain reasoning）
- Fast STA: **5/5 通过**
- train_grpo.py 语法检查 + import 检查 + config 解析：全部通过
- FOL 路径向后兼容：不受影响

### Prolog JSONL 数据格式
```json
{
  "id": "prolog_001",
  "context": "Tom is Bob's parent. Bob is Ann's parent...",
  "question": "Is Tom Ann's grandparent?",
  "answer": "true",
  "prolog_premises": ["parent(tom, bob).", "parent(bob, ann).", "grandparent(X,Y) :- parent(X,Z), parent(Z,Y)."],
  "prolog_query": "grandparent(tom, ann)"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "id": "prolog_001",
    "context": "Tom is Bob's parent. Bob is Ann's parent...",
    "question": "Is Tom Ann's grandparent?",
    "answer": "true",
    "prolog_premises": [
      "parent(tom, bob).",
      "parent(bob, ann).",
      "grandparent(X,Y) :- parent(X,Z), parent(Z,Y)."
    ],
    "prolog_query": "grandparent(tom, ann)"
  }
}
```

</details>

---
