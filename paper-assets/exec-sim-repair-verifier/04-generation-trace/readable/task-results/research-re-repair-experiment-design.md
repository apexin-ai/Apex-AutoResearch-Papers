# research re repair experiment design

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_re-repair-experiment-design_20260516T051324_result.json`
- **Structured JSON:** [`f78866049701b6cba8b8.json`](../../sessions/f7/f78866049701b6cba8b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个产出已就绪：

**实验方案** (`artifacts/re_repair_experiment_design.md`):
- **4 conditions**: control（无诊断）、cls-diag（CLS 预测的 per-test fail）、oracle-diag（ground truth 上界）、random-diag（噪声基线，排除"看到 test name 本身就有用"的混淆）
- **数据**: SWE-bench Verified T≥2 实例 ~155 个，每个 ≥5 个 incorrect patches（公开 agent 提交 + 合成变异），总计 ~775 paired observations
- **统计**: McNemar test（paired binary）+ instance-clustered bootstrap 95% CI，n=775 对 Δ=5pp 有 power≥0.80
- **CLS 误差处理**: 分层分析（CLS 高/低准确度实例对比）+ accuracy-utility frontier（向 oracle 注入不同比例噪声，画出诊断准确度 vs 修复成功率曲线）
- **计算**: ~84h GPU（CLS 推理 + 修复生成），Docker 验证 48-96h wall-clock；Phase 0 快速可行性检查（10 实例，4h）可做 go/no-go
- **风险**: cls-diag 可能劣于 control 时有 oracle 兜底；修复 LLM 太弱时切 API 模型

**框架代码** (`re_repair_eval.py`):
- 4-phase CLI: `prepare` → `generate` → `verify` → `analyze`
- CLS 推理（LoRA 加载 + per-test 预测）、vLLM batch 修复生成、Docker 验证 placeholder、McNemar + clustered bootstrap 分析、resolve rate 图表生成
- 遵循项目既有模式（`load_jsonl`、chat template、argparse）

关键设计决策需确认：
1. **修复 LLM**：用 Qwen3-8B（本地，便宜但可能太弱）还是 API（更贵但修复能力更强）？建议 Phase 0 先用 Qwen3-8B 试 10 个实例看 resolve rate 是否 >0
2. **Docker 环境**：westd 服务器是否有 Docker？如果没有需要另开机器跑验证

---
