# diag fewrel 80rel sighup

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_fewrel_80rel_sighup_20260515T134010_result.json`
- **Structured JSON:** [`183abcf2309203a734db.json`](../../sessions/18/183abcf2309203a734db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败原因：**不是真正的失败**

主日志 `exp_fewrel_formal_80rel.log` 末尾显示：
```
===== 80-rel ALL DONE =====
EXIT_CODE=129
```

实验**实际已跑完全部 batch**（count_1 到 count_80，exp1 + exp2），所有结果都已打印。EXIT_CODE=129 (SIGHUP) 是在主计算完成后才被记录的——SIGHUP 到达时实验已经做完了，只是 wrapper 脚本捕获到了非零退出码。

另外 `/tmp/fewrel_80rel_exp1.log` 记录了一次**更早的失败尝试**：vLLM 启动时 GPU 显存不足（仅 2.42/94.97 GiB 可用），那次是因为其他进程占了 GPU。这不是当前产出对应的运行。

### 2. Partial output → **实际是完整产出**

| 文件 | 大小 | 说明 |
|------|------|------|
| predictions_exp1.json | 22MB | exp1 预测结果 |
| predictions_exp2.json | 5.5MB | exp2 预测结果 |
| eval_exp1.json | 175KB | exp1 评估 |
| eval_exp2.json | 101KB | exp2 评估 |
| preprocess_exp1/exp2.json | ~280KB each | 预处理配置 |
| relation_sim_matrix.pt | 29KB | 相似度矩阵 |

exp1 和 exp2 的 predictions + eval 都在，**数据应保留，无需重跑**。

### 3. GPU 状态：**完全空闲**

```
NVIDIA RTX PRO 6000 Blackwell, 0 MiB / 97887 MiB, 0% utilization
```

### 4. 残留进程：**无**

GPU 显存 0 MiB，无 vLLM 或实验进程在运行。无需清理。

### 结论

实验数据完整，EXIT_CODE=129 只是 SIGHUP 在实验完成后到达 wrapper 脚本导致的虚假失败。可以直接用现有产出继续下游分析。

---
