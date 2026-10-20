# ssh server status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_server-status-check_20260514T062135_result.json`
- **Structured JSON:** [`98fa23a5af69de962f8f.json`](../../sessions/98/98fa23a5af69de962f8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### GPU 状态
| GPU | 显存使用 | 利用率 | 负载 |
|-----|---------|--------|------|
| 0 | 60178/97887 MiB | 91% | s020 + s030 (两个实验共享) |
| 1 | 21047/97887 MiB | 75% | bf16_ds_rand_s015 (新) |
| 2 | 21047/97887 MiB | 71% | bf16_ds_rand_s020 (新) |
| 3 | 21047/97887 MiB | 76% | bf16_ds_rand_s025 (新) |

### 5 个原始实验状态

```
GPU 1→done: bf16_importance_s015  DONE  EXIT_CODE=0  II[high]=-0.15, II[mid]=+0.45, II[low]=+2.41  PASS
GPU 3→done: bf16_importance_s025  DONE  EXIT_CODE=0  II[high]=+0.30, II[mid]=+5.73, II[low]=+25.85 PASS
GPU 2→done: v6_random_s030_r3    DONE  EXIT_CODE=0  II[high]=+9.24, II[mid]=-230.76, II[low]=-7.41 PASS (noisy)
GPU 0:      bf16_importance_s020  RUNNING 42/50  ~10-15min remaining
GPU 0:      bf16_importance_s030  RUNNING 38/50  ~15-25min remaining
```

### profiling_results.json 状态
| 实验 | 文件 | 大小 | per_problem_ii |
|------|------|------|---------------|
| bf16_imp_s015 | EXISTS | 1.99MB | 50 problems ✓ |
| bf16_imp_s020 | NOT FOUND | - | 尚未生成 |
| bf16_imp_s025 | EXISTS | 1.99MB | 50 problems ✓ |
| bf16_imp_s030 | NOT FOUND | - | 尚未生成 |
| v6_random_s030_r3 | EXISTS | 1.99MB | 50 problems ✓ |

### 新发现的 3 个实验
tmux 里还有 3 个新启动的 random masking 实验（bf16_ds_rand_s015/s020/s025），均在 11/50，分别占 GPU 1/2/3。

### 关键发现

1. **GPU 0 资源竞争**：s020 和 s030 共享 GPU 0（60GB 显存，91% 利用率），可能互相拖慢。

2. **Importance masking II 随 sparsity 单调增长**：
   - s015: low_II=2.41, mid_II=0.45
   - s025: low_II=25.85, mid_II=5.73（约 10x 增幅）
   - 预计 s020/s030 会填补中间值

3. **Random masking (s030) 极度不稳定**：mid_sparsity mean=-230.76 但 median=+2.43，被极端 outlier 主导。CI 宽度 656，结果不可靠。

4. **PPL 降解加速**：s025 importance low_both_PPL=63.67（dense 仅 1.23），s030 random 更是 88.94。

已将完整 metrics 保存到 `memory.md`。

---
