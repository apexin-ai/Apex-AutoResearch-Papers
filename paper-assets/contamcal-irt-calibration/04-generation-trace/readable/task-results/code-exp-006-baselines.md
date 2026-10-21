# code exp 006 baselines

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-006-baselines_20260514T124156_result.json`
- **Structured JSON:** [`4c826bdca95c23b50984.json`](../../sessions/4c/4c826bdca95c23b50984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码完成。总结：

## exp-006 代码结构（2658 行 / 7 文件）

| 文件 | 行数 | 功能 |
|------|------|------|
| `run_exp006.py` | 371 | 端到端 pipeline: IRT + baselines + evaluation + joint fit ablation |
| `run_irt_calibration.py` | 491 | CmdStanPy 4PL+γ IRT 拟合（per-benchmark 或 matrix 直接输入） |
| `baselines.py` | 447 | 7 baselines 统一接口 (B0-B6)，含 DCR fuzzy inference |
| `evaluate_calibration.py` | 425 | 8 评估指标 + LaTeX/text 表格输出 |
| `joint_fit.py` | 234 | **新增** — 共享全局 γ 的 joint fitting ablation |
| `run_all_baselines.py` | 165 | 独立 baseline runner（含 synthetic data dry-run） |
| `run_irt_stan.py` | 525 | 备选 Stan-only IRT runner |

## 已验证

- Stan model 编译 OK (`contam_irt_4pl_simple.stan`)
- 所有 import 通过
- Baselines dry-run 通过（5/5 non-Stan baselines 输出正常）
- 数据加载：9 models × 4 benchmarks (mmlu/gsm8k/arc_challenge/humaneval)
- Joint concatenation：9 models × 16697 items
- `--help` 参数解析：3 个入口脚本均正常

## 新增内容

1. `joint_fit.py` — concatenate 所有 benchmark items，拟合单个 shared γ（ABLATION）
2. `run_exp006.py --joint-fit` 标志位集成
3. D018 排除规则（3B + GSM8K）
4. `README.md`

---
