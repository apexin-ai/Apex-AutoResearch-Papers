# compute_cka.py 验证报告

## 验证日期
2026-05-21

## 脚本
`code/compute_cka.py` — Linear CKA (Kornblith et al. 2019) 计算脚本

## 验证数据
- MVP_001 (Qwen2.5-7B) 激活：`/root/xling_calib_direction/activations/`
- 8 层 × 5 语言，n=14042 parallel samples per pair
- 层：0, 4, 8, 12, 16, 20, 24, 27
- 语言：zh, ar, hi, sw, ko (ref: en)

## 与已有结果对比

已有结果：`results/cka_results.csv`（列名: layer, language, cka）

| layer | lang | existing | new      | diff     |
|-------|------|----------|----------|----------|
| 0     | zh   | 0.912057 | 0.912092 | +0.000035|
| 0     | ar   | 0.901368 | 0.901320 | -0.000048|
| 0     | hi   | 0.536453 | 0.536285 | -0.000168|
| 0     | sw   | 0.439737 | 0.439818 | +0.000081|
| 0     | ko   | 0.686871 | 0.686777 | -0.000094|
| 16    | zh   | 0.885897 | 0.885929 | +0.000032|
| 16    | ar   | 0.882861 | 0.882928 | +0.000067|
| 27    | sw   | 0.084145 | 0.084149 | +0.000004|

**所有 40 组数值偏差 < 0.0004**，属于浮点精度差异（float32 累积误差），算法实现正确。

## Summary 统计

### Per-language mean CKA
- zh: 0.7388 (最高)
- ar: 0.6934
- ko: 0.6542
- hi: 0.4359
- sw: 0.4159 (最低)

### Per-layer mean CKA
- layer 16: 0.7604 (peak)
- layer 12: 0.7354
- layer 0: 0.6953
- layer 8: 0.6945
- layer 4: 0.5826
- layer 20: 0.5735
- layer 24: 0.4153
- layer 27: 0.2440 (最低)

## 结论
脚本验证通过。CKA 在中间层（12-16）最高，顶层急剧下降——与 correctness direction 跨语言迁移在顶层退化的发现一致。
