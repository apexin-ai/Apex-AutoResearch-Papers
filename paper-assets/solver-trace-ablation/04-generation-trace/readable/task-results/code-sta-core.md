# code sta core

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sta-core_20260513T173855_result.json`
- **Structured JSON:** [`c98c90861456869b8a9e.json`](../../sessions/c9/c98c90861456869b8a9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 import 通过，decompose_fol 工作正常。

文件清单：
- `src/__init__.py` — 空
- `src/solvers/__init__.py` — 空
- `src/solvers/base.py` — SolverResult + FOLSolver 抽象类
- `src/solvers/prover9.py` — Prover9 CLI 后端
- `src/solvers/z3_solver.py` — Z3 Python API 后端 + FOL 解析器
- `src/solvers/factory.py` — 工厂函数，prover9 → z3 fallback
- `src/sta/__init__.py` — 空
- `src/sta/components.py` — FOL 组件分解
- `src/sta/ablation.py` — STA ablation 核心逻辑
- `src/sta/isr.py` — ISR 计算 + 批量统计
- `src/sta/reward.py` — GRPO reward 函数（含 formalization 解析器）
- `scripts/phase0_baseline.py` — Phase 0 baseline 脚本

---
