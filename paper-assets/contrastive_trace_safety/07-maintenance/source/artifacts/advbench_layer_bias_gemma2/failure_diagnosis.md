# advbench_layer_bias_gemma2 失败诊断

## 根因：代码 bug（已修复）

Phase 1（trace 收集）成功完成（520 traces, 6 JB / 514 safe）。Phase 2（分析）崩溃于 `phase_analyze()` line 417：

```
TypeError: 'NoneType' object is not subscriptable
  "layer": f"L{best_key[0]}", "window": best_key[1],
```

`best_key` 为 None，因为：
1. 仅 6/520 样本为 jailbreak（1.15%），极端类不平衡
2. 原始代码未使用 stratified split（Train+val=416, test=104），可能导致某些 fold 中正样本为 0
3. `evaluate_layer()` 对部分 metric 的所有 layer-window 组合返回 None，`best_key` 未被赋值
4. 代码缺少 None guard 直接下标访问

## 修复状态：已修复

脚本已更新：添加 None guard + stratified split。Phase 2 已单独重跑成功（`/tmp/gemma2_phase2.log`），结果保存于服务器 `artifacts/advbench_layer_bias_gemma2_results.json`。

结论：Divergence = 22.0pp — REPLICATED。
