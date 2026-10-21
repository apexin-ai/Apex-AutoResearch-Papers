# research plan006 readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan006-readiness_20260514T053844_result.json`
- **Structured JSON:** [`b02983e6e5d3ac3ade77.json`](../../sessions/b0/b02983e6e5d3ac3ade77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan006 Readiness Report

### 1. SWI-Prolog 安装状态
**READY** — 已安装在 `/usr/bin/swipl`（symlink → `/usr/lib/swi-prolog/bin/x86_64-linux/swipl`）。Memory 记录版本 8.4.2。

### 2. Prolog STA 代码状态
**READY** — 完整实现已就位：

| 文件 | 功能 |
|------|------|
| `src/solvers/prolog.py` | PrologSolver 类，封装 swipl subprocess 调用 |
| `src/sta/prolog_reward.py` | Prolog STA reward：O(n) full ablation + O(1) fast ISR |
| `scripts/sta_prolog.py` | 独立测试/评估 CLI，含 5 个内置 test case |
| `src/solvers/factory.py` | 已注册 `"prolog"` solver 类型 |
| `scripts/train_grpo.py` | 完整 Prolog 分支：`build_prolog_dataset()`、`PROLOG_SYSTEM_PROMPT`、`logic_type="prolog"` |

### 3. 训练数据状态
**部分 READY** — `data/train_500_seed42.jsonl`（500 条）包含 `context`/`question`/`answer` 字段（prompt 所需），但 **没有** `prolog_premises`/`prolog_query` 字段（0 条匹配）。

影响分析：`build_prolog_dataset()` 用 `.get()` 取这些字段，缺失时返回空值。**Prompt 构建不受影响**（只用 context+question），**reward 计算不受影响**（只解析模型生成的 Prolog 代码再跑 swipl）。这些字段仅作 metadata 存储。**可以直接开训**。

### 4. 训练配置状态
**READY** — 两份 Prolog 专用 config：
- `configs/grpo_prolog_exec_sta.yaml` — exec+STA (0.5/0.5)，`wandb_run: prolog_exec_sta`
- `configs/grpo_prolog_exec_only.yaml` — exec-only (1.0/0.0)，`wandb_run: prolog_exec_only`

两者均使用 `data/train_500_seed42.jsonl`（符合 C001）、`solver: prolog`、Qwen3-4B、100 steps、`save_total_limit=1`（符合 C003）。注意：`no_wandb: true`，如需 W&B 记录需修改。

### 5. 缺失项清单

| # | 缺失项 | 严重程度 | 说明 |
|---|--------|---------|------|
| 1 | **eval_sta.py 无 Prolog 支持** | **BLOCKER** | `scripts/eval_sta.py` grep "prolog" = 0 匹配。C004 要求跨 run ISR 对比必须用 eval_sta.py 统一评估。训练可以先跑，但出结果后无法合规评估 |
| 2 | **Dry-run 未验证** | MEDIUM | 代码看起来完整但未实际加载验证，需一次 `ssh_execute` dry-run |
| 3 | **sta_prolog.py 测试未跑** | MEDIUM | 5 个内置 test case 需验证 swipl 实际可用 |
| 4 | **W&B 关闭** | LOW | config 设 `no_wandb: true`，需确认是否要开启 |

### 6. 预估准备时间

| 工作项 | 耗时估算 |
|--------|---------|
| 跑 sta_prolog.py 测试 + dry-run | 15 min |
| 给 eval_sta.py 添加 Prolog 支持 | 1-2 hr |
| 修改 config（W&B、输出路径等） | 10 min |
| **总计** | **1.5-2.5 hr**（1 Worker） |

**结论**：代码/数据/环境 90% ready。唯一 blocker 是 eval_sta.py 缺 Prolog 支持（不影响训练启动，但影响结果评估）。可以先提交训练，并行开发 eval_sta.py Prolog 分支。

---
