# code mvp experiment

**eco alpha beta diversity** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_experiment_20260521T130416_result.json`
- **Structured JSON:** [`d1af00729ae36f10c124.json`](../../sessions/d1/d1af00729ae36f10c124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MVP 代码完成，dry-run 全流程通过。

**文件清单** (`artifacts/` 下):

| 文件 | 功能 |
|------|------|
| `run_mvp.py` | 主入口，串联全部 11 步分析 |
| `data_loader.py` | Dryad 数据下载/解析 + 合成数据生成 |
| `diversity.py` | Hill numbers、Jost 乘法分区、Baselga 分解、覆盖率估计 |
| `flat_metrics.py` | TF-IDF cosine similarity + FAIL test 2 |
| `analysis.py` | Bootstrap CI、rarefaction 敏感性检验、Pass/Fail 判定 |
| `visualization.py` | 4 张图：Hill 对比、Baselga 分解、cosine 热力图、rarefaction |
| `requirements.txt` | 依赖列表 |

**合成数据 dry-run 结果验证**:
- alpha↑：AI 条件下个体多样性显著高于 no-AI（q=0/1/2 全部 CI 不重叠）
- beta↓：AI 条件下群体 beta 显著低于 no-AI（q=0 下 CI 不重叠）
- Baselga 两组分 CI 不重叠（可区分 turnover vs nestedness）
- Cosine r=0.445, p≈0（flat metrics 能检测条件差异）
- FAIL test 2 未触发（TF-IDF 恢复误差 21-34%，>10% 阈值）
- 4 张图全部正常生成

**部署命令**:
```bash
pip install -r requirements.txt
python run_mvp.py                  # 下载真实数据并运行
python run_mvp.py --synthetic      # 合成数据测试
python run_mvp.py --nboot 200      # 设置 bootstrap 迭代数
```

---
