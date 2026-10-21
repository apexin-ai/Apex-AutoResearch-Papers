# Gradient V2 出图脚本就绪报告

**日期**: 2026-05-27

## 结论：就绪，无需修改

`plot_gradient_analysis_v2.py` (380行, 15KB) 已支持 5 条件出图，可直接使用。

## 脚本概况

| 项目 | 详情 |
|------|------|
| 路径 | `/root/occsafe_vla/scripts/plot_gradient_analysis_v2.py` |
| 输入 | `--results_dir` 目录，自动 glob `*_gradient_stats.json` |
| 输出 | `--output` 指定 PDF 路径 |
| 面板 | 4-panel: (a) Action grad norms, (b) OCC grad norms, (c) cosine sim, (d) ratio vs Vanilla |

## 5 条件样式映射（CONDITION_STYLES 已预定义）

| condition_name | 颜色 | 标记 | 线型 | 图例标签 |
|----------------|-------|------|------|----------|
| Vanilla v2 | #607D8B | x | : | Vanilla v2 |
| Full OCC BN v2 | #2196F3 | o | - | Full OCC BN v2 |
| Full OCC LN v2 | #4CAF50 | ^ | - | Full OCC LN v2 |
| Detach BN v2 | #F44336 | s | -- | Detach BN v2 |
| Detach LN v2 | #FF9800 | D | -- | Detach LN v2 |

## 输入输出匹配确认

- `run_gradient_analysis_v2.py` 输出: `{condition_name}_gradient_stats.json`，JSON 内含 `"condition"` 字段
- `plot_gradient_analysis_v2.py` 读取: glob `*_gradient_stats.json`，用 `data["condition"]` 查样式
- **匹配正确，无兼容性问题**

## 使用命令

```bash
# 基本用法（5 条件 JSON 都在 results_dir 下）
python3 /root/occsafe_vla/scripts/plot_gradient_analysis_v2.py \
  --results_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --output /root/occsafe_vla/artifacts/gradient_v2/gradient_analysis_v2_combined.pdf

# 可选: 与 v1 对比
python3 /root/occsafe_vla/scripts/plot_gradient_analysis_v2.py \
  --results_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --v1_results_dir /root/autodl-tmp/analysis/gradient_same_seed/ \
  --output /root/occsafe_vla/artifacts/gradient_v2/gradient_analysis_v2_combined.pdf
```

## 注意事项

1. **condition_name 必须用空格**（如 "Vanilla v2"），不能用下划线（"Vanilla_v2"），否则样式匹配会退化为灰色默认
2. Panel (b)(c) 自动跳过 Vanilla 和 Detach 条件（无 OCC 梯度 / cosine sim），行为正确
3. Panel (d) ratio 以 Vanilla 为 baseline，`find_vanilla()` 按 "vanilla" 关键词匹配
4. `compare_gradient_conditions.py` (11.9KB) 是旧版 3 条件脚本，不需要使用
5. 当前 `artifacts/gradient_v2/` 目录尚不存在，梯度分析运行时会创建
