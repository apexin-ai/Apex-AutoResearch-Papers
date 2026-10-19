# ApexTune × AIF360 — 完整战役归档 (v1 – v6.1)

统一保存 aif360 基准上 apextune-fml 全部六代诊断实验的**代码与结果**。
本目录是 2026-09-16 从三个分散存放点(vast 4090 实例、平台工作区、S3)
归并而成,去除了此前"v5 之后仅存于租用实例"的单点风险。

## 口径声明

- 模型 `gpt-5.6-sol`(官方口径为 `gpt-5.4`),复现 checkout → 全部运行标记
  **`comparable: false` / 非 leaderboard-eligible / diagnostic**。
- 指标:绝对平均几率差 `abs_aod_mean`,**越低越好**;准确率为硬约束。
- 归一化分:`max(0, 0.23986259586405548 − abs_aod)`。

## 目录结构

```
aif360-campaign-archive/
├── README.md                  ← 本文件
├── SHA256SUMS                 ← 全树校验和
├── code-v1-v4/                ← 权威归档(v1–v4),含索引/APT 轨迹/SHA256SUMS
│   ├── code-v1/round-{1,2}/
│   ├── code-v2/round-1/
│   ├── code-v3/round-1/
│   ├── code-v4/round-{1,2,3}/ + three_rounds_qd_v4.json
│   ├── ARCHITECTURE_QD_V4.md
│   ├── COLLECTION_MANIFEST.json
│   └── SHA256SUMS
├── code-v5/                   ← 三轮(QD 搜索最优配置)
├── code-v6/                   ← 一轮(recombine 等四组件)
├── code-v61/                  ← 一轮(修 bug 后重试,family_pessimistic 首次实测翻车)
└── early-20260905/            ← 9/5 早期运行(无终测分)
```

每个 `<run>/` 目录含:`summary.json`、`.apextune_fml_state.json`、
`run_manifest.json`、`seed_code.json`、`step_snapshots/`(100 步代码)、
`final_test/`;v5–v6.1 另附派生的 `README.md` 与 `APEXTUNE_RUN_LABEL.json`
(**派生视图,原始 json 为权威**)。

## 成绩总表(诊断口径)

| 代际 | 轮 | best val abs_aod | final test abs_aod | 归一化分 |
|---|---|---|---|---|
| v1 | r1 | 0.03094 | 0.01260 | 0.22726 |
| v1 | r2 | 0.00125 | 0.01112 | 0.22874 |
| v2 | r1 | 0.02754 | 0.02105 | 0.21881 |
| v3 | r1 | 0.04088 | 0.05288 | 0.18698 |
| v4 | r1 | 0.00125 | 0.01112 | 0.22874 |
| v4 | r2 | 0.04088 | 0.05288 | 0.18698 |
| v4 | r3 | 0.03094 | 0.01260 | 0.22726 |
| **v5** | r1 | 0.00125 | 0.01112 | 0.22874 |
| **v5** | r2 | 0.02000 | 0.01145 | 0.22841 |
| **v5** | r3 | 0.01088 | 0.01954 | 0.22032 |
| v6 | r1 | 0.04088 | 0.05288 | 0.18698 |
| v6.1 | r1 | 0.02671 | 0.06818 | 0.17168 |
| early | r1 | 0.01421 | (无) | (无) |

- **v5 三轮**:归一化分 mean **0.2258** ± 0.0048(样本 std)→ 收官配置。
- v4 三轮:0.2143 ± 0.0237。
- v6/v6.1 四组件(重组臂/家族悲观终选/反思层/分辨率门控)全部回退为默认关闭,
  仅保留"失败批零奖励记账"修复。详见 `code-v61/README` 与提交历史。

## 来源与校验

| 槽位 | 归并自 |
|---|---|
| code-v1-v4 | 本地 `task-165/aif360-apextune-structure-history-20260912/`(与 S3 副本哈希一致) |
| code-v5 | 4090 `/root/apextune-results/.../aif360-gpt56sol-qd-v5-r{1,2,3}-*` |
| code-v6 | 4090 `.../aif360-gpt56sol-qd-v6-r1-20260914` |
| code-v61 | 4090 `.../aif360-gpt56sol-qd-v61-r1-20260915` |
| early-20260905 | 4090 `.../aif360-r1-restart-20260905` |

- `code-v1-v4/SHA256SUMS` 为原归档校验;`code-v5`/`v6`/`v61`/`early-*` 的
  `SHA256SUMS` 为本次归档时生成,**逐一校验通过**。
- 顶层 `SHA256SUMS` 覆盖全树,可离线验证字节完整性。

## 状态

- 代码 + 结果 + 终测产物:**六代全齐,无遗失**。
- 本归档即本地与 S3 的权威副本(S3 路径见镜像说明)。
