# infra wait bootstrap100 bash

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_wait_bootstrap100_bash_20260521T230652_result.json`
- **Structured JSON:** [`71ec02f04e4f6f4501cf.json`](../../sessions/71/71ec02f04e4f6f4501cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap 完成。注意：**n_bootstrap=20/方向**（不是 100/方向 — 可能是 100 次总迭代分配到 4+个方向）。

## Bootstrap 结果 (n=20/方向)

### Llama 3.1

| Direction | Bal Acc (mean±std) | F1 (mean±std) |
|-----------|-------------------|---------------|
| EN→EN | **0.773 ± 0.010** | 0.770 ± 0.011 |
| ZH→ZH | 0.709 ± 0.013 | 0.710 ± 0.015 |
| ZH→EN | 0.710 ± 0.027 | 0.734 ± 0.024 |
| EN→ZH | 0.644 ± 0.022 | 0.691 ± 0.031 |

### Qwen 3

| Direction | Bal Acc (mean±std) | F1 (mean±std) |
|-----------|-------------------|---------------|
| EN→EN | **0.754 ± 0.019** | 0.751 ± 0.019 |
| ZH→EN | 0.731 ± 0.025 | 0.724 ± 0.041 |
| ZH→ZH | 0.717 ± 0.021 | 0.723 ± 0.027 |
| EN→ZH | 0.657 ± 0.026 | 0.656 ± 0.047 |

### COMET 进度

- **Qwen**: ~340/798 back-translated (~43%)
- **Llama**: ~320/1096 back-translated (~29%)
- 两个都还在 back-translate 阶段，EXIT_CODE=124（timeout，COMET 进程仍在运行）
- 无 validated 文件

### 关键发现

1. **同语言 probe 最强**：EN→EN 两模型都是最高（Llama 0.773, Qwen 0.754）
2. **跨语言不对称**：ZH→EN 明显优于 EN→ZH（两模型一致），说明中文表示更容易迁移到英文方向
3. **EN→ZH 最弱**：~0.65，跨语言方向中最困难
4. **Llama EN→EN 略优于 Qwen**（0.773 vs 0.754），但 Qwen ZH→ZH 略优（0.717 vs 0.709）
5. **std 合理**：同语言 ~0.01-0.02，跨语言 ~0.02-0.03，bootstrap 估计稳定

---
