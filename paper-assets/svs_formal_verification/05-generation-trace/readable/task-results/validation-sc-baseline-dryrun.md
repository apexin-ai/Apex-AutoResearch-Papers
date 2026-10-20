# validation sc baseline dryrun

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_sc_baseline_dryrun_20260514T113843_result.json`
- **Structured JSON:** [`3a868b349f4b90f57b2a.json`](../../sessions/3a/3a868b349f4b90f57b2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SC Baseline dry-run 完成，管线跑通。汇报：

---

## gpu-5090-4x-4 状态 & SC Baseline Dry-Run 结果

### GPU 状态（4x RTX 5090, 各 32GB）
| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| 0 | 99% | 31459/32607 MiB | 忙 |
| 1 | 99% | 31459/32607 MiB | 忙 |
| 2 | 0% | 31401/32607 MiB | 显存被占但空闲 |
| 3 | 0% | 31401/32607 MiB | 显存被占但空闲 |

### 代码部署
- `/root/autodl-tmp/svs_formal_verification/` ✓ 已存在
- `svs_pipeline/` 完整（data loader, evaluation/metrics, generation, formalization, verification）
- ProofWriter 本地缓存 ✓ 可用
- Python 3.12.3 (conda base) ✓
- HuggingFace 网络不通（需 `source /etc/network_turbo`），但本地缓存回退正常

### SC Baseline 管线验证 ✓ 跑通
- **10 题 ProofWriter depth-5**，每题 8 条 mock chain（60% 正确率）
- **Majority voting + evaluate_results() + format_report()** 全部正常
- Mock 场景下 SC accuracy = 100%（60% correct rate + 8 chains 足够让正确答案成为多数）
- 输出文件：`outputs_dryrun/sc_baseline_dryrun.json`
- 管线组件验证：数据加载 ✓ → Chain 生成 ✓ → Majority Vote ✓ → Metrics 计算 ✓ → 报告输出 ✓

### Blocker
- **GPU 0-3 显存全被占**（即便 GPU 2-3 利用率 0%），如果要跑真实 LLM 推理需要先释放显存
- HF Hub 网络不通，正式实验前需 `source /etc/network_turbo`

---
