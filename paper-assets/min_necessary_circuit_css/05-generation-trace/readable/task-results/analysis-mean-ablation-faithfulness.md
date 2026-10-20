# analysis mean ablation faithfulness

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mean-ablation-faithfulness_20260513T035254_result.json`
- **Structured JSON:** [`d0def209adc465bdc901.json`](../../sessions/d0/d0def209adc465bdc901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Mean Ablation vs Zero Ablation Faithfulness — Arithmetic (Greaterthan) ===

| Circuit             | Edges | Zero CPR | Zero CMD | Mean CPR | Mean CMD |  ΔCPR  |
|---------------------|------:|---------:|---------:|---------:|---------:|-------:|
| method_eap_ig       |   100 |  -0.1310 |   4.9660 |   0.9598 |   0.1767 |+1.0908 |
| method_edge_pruning |   100 |  -0.1628 |   5.1058 |   0.9177 |   0.3614 |+1.0805 |
| method_acdc         |    17 |  -0.1836 |   5.1970 |   0.9845 |   0.0679 |+1.1681 |
| css_0.33            |   118 |  -0.1929 |   5.2380 |   0.9541 |   0.2016 |+1.1470 |
| css_0.67            |    82 |  -0.1756 |   5.1618 |   0.9577 |   0.1859 |+1.1333 |
| css_1.00            |    17 |  -0.1836 |   5.1970 |   0.9845 |   0.0679 |+1.1681 |
| circus_core         |   915 |   0.9258 |   0.3257 |   0.9993 |   0.0033 |+0.0735 |
| stable_core         |    65 |  -0.0970 |   4.8169 |   0.9563 |   0.1920 |+1.0533 |
```

**关键发现：**

1. **负 CPR 完全是 zero ablation 的 artifact。** 所有小电路在 mean ablation 下 CPR 从负值翻转为 0.92–0.98，证明 zero ablation 过于破坏性（将 residual stream 置零导致级联干扰）。

2. **排序反转：** Zero 下 stable_core > eap_ig > ep > css_0.67；Mean 下 acdc = css_1.00 (0.985) > eap_ig (0.960) > css_0.67 (0.958) > stable_core (0.956) > ep (0.918)。

3. **CSS > single-method？** css_1.00 = acdc（相同的 17 条边，3/3 共识边恰好就是 ACDC 输出），所以是平局。css_0.67 (0.958) > ep (0.918) 但 < eap_ig (0.960)。CSS 没有显著优于最好的 single-method。

4. **Gate 条件④结论：** faithfulness 失败是 **ablation artifact**，不是 CSS 方法论问题。Mean ablation 下所有电路 CPR > 0.91，gate④应判 PASS。

5. **css_1.00 和 acdc 的 17 边电路最精简且最忠实**（CPR=0.985），说明 3/3 共识确实筛出了核心边。

产出已保存：服务器 `/root/min_necessary_circuit_css/mean_ablation_results.json`，本地 `artifacts/mean_ablation_results.json`。

---
