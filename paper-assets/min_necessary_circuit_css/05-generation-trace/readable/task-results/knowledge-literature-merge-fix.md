# knowledge literature merge fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_literature-merge-fix_20260513T022004_result.json`
- **Structured JSON:** [`2ad3156d774ef550d311.json`](../../sessions/2a/2ad3156d774ef550d311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件完整且格式正确。总结：

---

### 新增条目（4 篇）

| 论文 | 位置 | 类型 |
|------|------|------|
| **Mondorf et al. (2510.06811)** | §1.5 (Direction 1) | 直接竞争，详细讨论 4 点局限 |
| **PIE (2604.16889)** | Additional Relevant Work | 互补，CLT-native 方法 |
| **EAP-GP (2502.06852)** | Additional Relevant Work | 互补，gradient 族变体 |
| **GIM (2505.17630)** | Additional Relevant Work | 互补，MIB 顶分方法 |

### 修改条目

- **Takeaway #2**: 从仅讨论 CIRCUS 扩展为同时讨论 CIRCUS + Mondorf et al. 两个竞争者
- **Takeaway #6**: 新增第 4 项加入 Mondorf et al.，第 5 项加入 PIE，新增第 6 项 "Method variants and benchmarks"

### Takeaway #5 修改前后

**修改前：**
> Distribution-shift robustness is a novel evaluation angle — No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.

**修改后：**
> Distribution-shift robustness is a **planned** novel evaluation angle — No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。

---
