# ops cqa1 path fix and k08 collect

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-path-fix-and-k08-collect_20260521T131336_result.json`
- **Structured JSON:** [`a04b2233a5ad3c52ffc3.json`](../../sessions/a0/a04b2233a5ad3c52ffc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry updates done. Here's the complete report:

---

## 产出

### 1. 移动的文件

4 files moved from `/root/eval_results/` → correct path (wrong path now empty):

| 文件 | 内容 | SR |
|------|------|-----|
| `xvla_prune_k08_libero_object_seed43.json` | L2norm k=0.8 seed43 | 88.4% |
| `xvla_prune_k08_libero_object_seed44.json` | L2norm k=0.8 seed44 | 89.8% |
| `xvla_l2_norm_k0.7_libero_object_seed44.json` | L2norm k=0.7 seed44 | 56.4% |
| `xvla_random_k0.3_libero_object_seed44.json` | Random k=0.3 seed44 | 63.0% |

### 2. X-VLA k=0.8 多种子 SR

**L2norm k=0.8**: seed42=88.8%, seed43=88.4%, seed44=89.8% → **mean 89.0%** (极低方差)

Random k=0.8: seed42=89.4% (仅1种子, 来自 `xvla_prune_k0.8_libero_object.json`)

### 3. k=0.85 SR

**L2norm k=0.85**: seed42=68.0%, seed43=67.6%, seed44=68.2% → **mean 67.9%**

**Random k=0.85**: seed42=63.6%, seed43 仍在运行 (PID 358390)

注意：k=0.8→0.85 出现 **cliff drop** (L2norm 89.0% → 67.9%, 下降 21pp)

### 4. 运行中实验 cwd

**两个 GPU 进程 cwd 都是 `/root/`（错误！）**：
- PID 358232: L2norm k=0.85 seed43 — 这是重复运行，旧结果已存在(67.6%)
- PID 358390: Random k=0.85 seed43 — 仍在收集，完成后结果会写到 `/root/eval_results/`

### 5. 脚本输出路径逻辑

Line 303: `f"eval_results/xvla_{args.mode}_k{args.keep_ratio}_{args.suite}_seed{args.seed}.json"`

**使用相对路径**。结果写到 `{cwd}/eval_results/`。从 `/root/` 启动就写到 `/root/eval_results/`。

### 6. Registry 更新

6 个实验 RUNNING → DONE（含 metrics）：
- L2norm k=0.7: seed43=59.0%, seed44=56.4%
- Random k=0.7: seed44=65.0%
- Random k=0.3: seed43=66.2%, seed44=63.0%
- L2norm k=0.3: seed43=21.0%

### Random k=0.3 seed44

SR = **63.0%**（seed42=62.8%, seed43=66.2%, mean≈63.7%）

---

**需要 Director 决定**：
1. PID 358232 (L2norm k=0.85 seed43 重复运行) 是否 kill？旧结果已有 67.6%
2. PID 358390 (Random k=0.85 seed43) 完成后需手动从 `/root/eval_results/` 取结果
3. 后续实验应确保从正确目录 `cd /root/autodl-tmp/importance_margin_vla_compress` 启动

---
