# code verify exp008 signal survival

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_exp008_signal_survival_20260514T135151_result.json`
- **Structured JSON:** [`6b1403ff79782731b70b.json`](../../sessions/6b/6b1403ff79782731b70b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-006 和 exp-008 互不依赖，各自独立消费 exp-002 signals。审查完成。

---

## exp-008 Signal Survival Analysis 代码就绪度报告

### 状态：**needs-fix → FIXED**

### 修复内容

**`run_exp008.sh` 中 `--adapter-path` bug**（已修复）
- `compute_signals.py` 没有 `--adapter-path` 参数，但 shell 脚本试图传入它 → 运行必崩
- 修复：adapter 路径直接作为 `--model-path` 传入（signal 模块自动检测 `adapter_config.json` 并加载 LoRA）

### 已验证通过

| 检查项 | 状态 |
|--------|------|
| v3 `signal_survival.py --dry-run` (4 regime, 3 benchmark, cliff detection) | ✓ |
| v2 `run_signal_survival.py --dry-run --regime-names base SFT RL DPO` | ✓ |
| `--help` 参数解析 | ✓ |
| 4 regime 模型/adapter 路径存在 | ✓ |
| Labels 格式 + 转换逻辑 | ✓ |
| `compute_signals.py` 接口兼容性 | ✓（修复后）|
| 统计测试完整性 (Cohen's d, Spearman, Wilcoxon, AUC) | ✓ |

### 4 Regime 定义 & 数据就绪度

| Regime | 模型路径 | 存在 | exp-002 signals |
|--------|----------|------|-----------------|
| base | Qwen2.5-0.5B | ✓ | **需计算** |
| sft_clean | d000 LoRA adapter | ✓ | ✓ 已有 |
| sft_contam | d005 LoRA adapter | ✓ | ✓ 已有 |
| rl_aligned | Qwen2.5-0.5B-Instruct | ✓ | **需计算** |

### 缺失/阻塞项

1. **base 和 rl_aligned 的 signal 数据尚未计算** — `run_exp008.sh` Step 1 会处理，不阻塞代码就绪
2. **ConStat 信号被 shell 脚本排除**（`SIGNALS="embedding minkpp selfcritique"`）— 需要 original vs paraphrased eval results，如果数据不存在则合理排除
3. **Shell 脚本 Step 2 用 v2 而非 v3** — v3 `signal_survival.py` 有 cliff detection 和 cross-benchmark aggregation，对 paper C2 claim 更有价值。建议 Step 2 改用 v3 或追加 Step 3

### 预估启动时间

exp-002 完成 + GPU 空闲后：
- **已有 sft_clean/sft_contam signals 可复用** → 只需计算 base + rl_aligned（2 regime × 3 benchmark × 3 signal = 18 次 inference）
- Signal 计算: **~1-2 小时 GPU 时间**
- Survival 分析: **< 1 分钟**
- 端到端含所有 regime: **~2-4 小时**

---
