# ops multiseed ht acc zscore

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_multiseed-ht-acc-zscore_20260523T005932_result.json`
- **Structured JSON:** [`de6e9ff83363cfda9e06.json`](../../sessions/de/de6e9ff83363cfda9e06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果：

```
HT Cohen's |d|:        15%        25%        50%
s1 (seed42):         9.4791    11.1560    20.9703
s2 (seed123):        9.7305    11.6196    16.1837
s3 (seed456):        9.4854    15.2285    17.3188
Mean:                9.5650    12.6680    18.1576
SD:                  0.1434     2.2295     2.5011

Acc z Cohen's |d|:     15%        25%        50%
s1 (seed42):        34.9312    41.1183    56.7022
s2 (seed123):       39.0715    44.1420    58.4234
s3 (seed456):       37.5363    42.3743    58.1443
Mean:               37.1797    42.5449    57.7567
SD:                  2.0930     1.5191     0.9238
```

Clean baseline (n=10): HT mean=-0.0330 (SD=0.0030), Acc mean=0.6775 (SD=0.0015).

两点观察：
- Accuracy z-score 的 Cohen's d 极大（35-58），因为 clean seeds 的 accuracy SD 极小（0.0015），微小的 accuracy 差异就产生巨大 effect size。这说明 accuracy 作为污染检测指标灵敏度极高但也意味着它对任何系统性差异都很敏感。
- HT Cohen's d 也很大（9.5-18.2），且随污染水平单调递增，cross-seed 一致性较好（15% 的 SD 仅 0.14）。

结果已保存至 `/root/autodl-tmp/ctrl_contam_pilot/results/cohens_d_ht_acc.json`。

---
