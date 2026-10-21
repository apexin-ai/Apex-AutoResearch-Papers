# code xor fix eval s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_xor-fix-eval-s43_20260521T105436_result.json`
- **Structured JSON:** [`c8cad1d64711d2112612.json`](../../sessions/c8/c8cad1d64711d2112612.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正在初始化（vLLM 警告是正常的）。三件事完成，汇总如下：

---

## 产出

### 1. d165-s42 eval 结果

| 指标 | 值 |
|------|-----|
| **PR** | 0.14 (14/100) |
| **ISR*** (proved-only mean) | 0.5467 |
| **TS% (H7)** | 0.0% (0/14) |
| **CE% (H1)** | 14.3% (2/14) |
| **PG% (H8)** | 0.0% (0/14) |
| **CI% (H9)** | 14.3% (2/14) |
| **Genuine%** | 85.7% (12/14) |

**by_answer_type:**
| type | count | proved | PR |
|------|-------|--------|----|
| true | 34 | 14 | 41.2% |
| false | 25 | 0 | 0.0% |
| unknown | 41 | 0 | 0.0% |

注：只有 answer=true 的问题被 proved，false/unknown 全部 PR=0。

### 2. XOR bug 修复

**文件**: `/root/solver-trace-ablation/src/solvers/prover9.py`
- **Line 42**: `raise ValueError("No left operand for ⊕")` → `return formula`
- **Line 77**: `raise ValueError("No right operand for ⊕")` → `return formula`

效果：malformed XOR 公式不再抛异常，而是保留原始字符串传给 Prover9，Prover9 因语法错误返回 `proved=False` → reward=0。正常 XOR 展开不受影响（已验证 `A ⊕ B` → `((A ∨ B) ∧ ¬(A ∧ B))`）。

### 3. s43 训练已提交

- **PID**: 871391
- **tmux session**: `d165-llama-exec-s43`
- **GPU**: cuda:0
- **log**: `/tmp/d165_llama_exec_s43_r2.log`

---
