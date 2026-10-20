# code plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-prolog-readiness_20260514T072132_result.json`
- **Structured JSON:** [`1b54bc6682adb2eee4d2.json`](../../sessions/1b/1b54bc6682adb2eee4d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan006 Prolog GRPO 就绪检查报告

### 1. warmup_ratio 代码 — **PASS**

`warmup_ratio` 直接传入 `GRPOConfig`（L342 定义, L424 传入），无自定义计算。HuggingFace Trainer 内部处理 `warmup_steps = ceil(warmup_ratio * max_steps)`，短步数下（如 3 步 × 0.1 = ceil(0.3) = 1 步 warmup）行为正确。无 bug。

### 2. Prolog 配置文件 — **PASS**

两个配置均已存在：

| 文件 | K | warmup_ratio | 关键参数 |
|------|---|---|---|
| `grpo_prolog_exec_only.yaml` | 8 | 0.0 | logic_type=prolog, solver=prolog, data_path=data/train_500_seed42.jsonl (C001✓) |
| `grpo_prolog_exec_only_k16_warmup.yaml` | 16 | 0.1 | 同上 + K=16 |

### 3. Prolog 数据 — **PASS**

`data/train_500_seed42.jsonl` 存在，500 条。NL premises/conclusion 作为输入，`logic_type=prolog` 切换 prompt 模板让模型生成 Prolog formalization（非 FOL）。数据格式兼容。

### 4/5. Dry-run & K=16 smoke test — **BLOCKED（GPU 满载）**

两张卡均被占用（各 80346 MiB）。

### CRITICAL BLOCKER: swipl 未安装

**`swipl`（SWI-Prolog）在服务器上不存在。** `find / -name "swipl"` 返回空。PrologSolver 依赖 swipl 二进制执行 reward 计算，缺少它训练会在第一步 reward 计算时失败。

**需要操作**：在 dry-run 前安装 SWI-Prolog：
```bash
apt-get update && apt-get install -y swi-prolog
```

是否现在安装 swipl？

---
