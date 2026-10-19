# code ablation ladder prep v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_ladder_prep_v2_20260516T031026_result.json`
- **Structured JSON:** [`9676b181c5d687cd8670.json`](../../sessions/96/9676b181c5d687cd8670.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇报如下：

---

## Ablation Ladder 就绪度报告

### 1. 每个配置就绪状态

| # | 配置 | routing_mode | 代码 | Checkpoint | 状态 |
|---|------|-------------|------|------------|------|
| (a) | Frozen pi0 | `none` | ✅ | 不需要 | ✅ **就绪** |
| (b) | Universal r16 | `universal` | ✅ | `lora_universal_r16/final/` ✅ | ✅ **就绪**（需将同一 dir 传入 3 个 expert 参数） |
| (b2) | Universal r48 | `universal` | ✅ | `lora_universal_r48/` — 无 `final/`，仅有 step_1000~7000 | ❌ **训练未完成** |
| (c) | Random routing | `random` | ✅ | visual ❌ / spatial ✅ / physical ✅ | ⚠️ **等 visual final** |
| (d) | Meta-Brain | `par` | ✅ | router ✅ / visual ❌ / spatial ✅ / physical ✅ | ⚠️ **等 visual final** |
| (e) | Oracle | `oracle` | ✅ | 同 (c)(d) | ⚠️ **等 visual final** |

### 2. Checkpoint 路径模式

训练代码保存路径：`{output_dir}/{run_name}/step_{N}/` + 训练结束时 `final/`

```
checkpoints/
├── phase1/par_router/best_router.pt          ✅ PAR router (F1=0.9963)
├── phase1/visual/best/                       ✅ 旧版 visual expert (epoch-based)
├── lora_visual_r16/step_{1k-7k}/             ⚠️ 新版 visual — 无 final/，训练中
├── lora_spatial_r16/final/                   ✅ spatial expert (r16, alpha=32)
├── lora_physical_r16/final/                  ✅ physical expert (r16, alpha=32)
├── lora_universal_r16/final/                 ✅ universal r16
└── lora_universal_r48/step_{1k-7k}/          ⚠️ universal r48 — 无 final/，训练中
```

**两个 visual checkpoint 需要决策**：`phase1/visual/best/` 是旧训练产物，`lora_visual_r16/` 是新训练。如果新训练不出 `final/`，可用旧的或 `step_7000` 作为 fallback。

### 3. 评测环境

- LIBERO-Plus：`task_classification.json` ✅
- `evaluate_libero_plus.py`：完整支持 7 种 perturbation type + oracle label 自动设置（line 367）
- `ablation_ladder.py`：5 种 routing mode 全部实现，含 dry-run + 绘图 + LaTeX 输出

### 4. 代码层面的问题

**`compute_merged_deltas` 硬编码 `EXPERT_NAMES = ["visual", "spatial", "physical"]`**：universal 模式必须将同一 checkpoint 复制到 3 个 expert 槽（数学上等价：1/3·A + 1/3·A + 1/3·A = A）。`ablation_ladder.py` 没有 `--lora_universal_dir` 快捷参数，需手动传 3 次。

**r16 vs r48 无内建区分**：代码只有 1 个 `universal` config，需跑两次并指向不同路径。

### 5. 阻塞清单

| 优先级 | 阻塞项 | 影响 | 预估 |
|--------|--------|------|------|
| P0 | visual_r16 训练完成（产出 `final/`） | 阻塞 (c)(d)(e) | 训练中，step_7000 已保存 |
| P0 | universal_r48 训练完成（产出 `final/`） | 阻塞 (b2) | 训练中，step_7000 已保存 |
| P1 | 释放 GPU（4卡全部被训练占用） | 阻塞所有评测 | 等训练结束 |
| P2 | 决策用哪个 visual checkpoint | 影响结果一致性 | 建议用新的 `lora_visual_r16/final/` |

**无需额外实现的代码**：ablation_ladder.py + evaluate_libero_plus.py + meta_brain_assembly.py 已完备覆盖全部 6 种配置。

### 6. GPU-hours 估算

| 场景 | 配置 | 参数 | 估算 |
|------|------|------|------|
| 完整评测 | 6 configs | 7 ptype × 50 ep × 5 seed | ~144 GPU-hours (~24h/config) |
| 精简评测 | 6 configs | 7 ptype × 20 ep × 3 seed | ~50 GPU-hours (~8h/config) |
| Smoke test | 6 configs | 7 ptype × 5 ep × 1 seed | ~3 GPU-hours (~30min/config) |

建议先跑 smoke test 验证 pipeline 端到端通，再跑精简版出数据。

---
