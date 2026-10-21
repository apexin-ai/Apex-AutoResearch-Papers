# check bootstrap final status and collect

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_final_status_and_collect_20260523T003901_result.json`
- **Structured JSON:** [`4b4a1f4117dcf1b493b7.json`](../../sessions/4b/4b4a1f4117dcf1b493b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Bootstrap 状态汇总

### 总体进度：**17/20 完成，3 条件待完成**

| GPU | 脚本 | 状态 |
|-----|-------|------|
| cuda:0 | openvla×4suites + nora×{goal,spatial} = 12条件 | **全部完成** (08:26:35) |
| cuda:1 | tracvla×4suites = 8条件 | 5/8完成，1个运行中 |

**GPU 状态**: GPU0 空闲 (0%), GPU1 在用 (691 MiB) — 正在跑 `tracvla/object/untrained`（RidgeCV fitting 阶段）

### 缺失条件 (3个)
1. `tracvla_object/untrained` — **正在运行**，extraction 已完成，在 fitting 阶段
2. `tracvla_long/trained` — 排队中
3. `tracvla_long/untrained` — 排队中

---

### 全部 17 个已完成结果 JSON

#### 1. openvla / goal / trained
```json
arch: openvla, suite: goal, condition: trained
peak_r2: 0.4164 @ L1, exit_r2: 0.2826 @ L31
delta: 0.1339, delta_ci_95: [0.0, 0.0742]
bootstrap_deltas: mean=0.0165, std=0.0216, median=0.0082
per_layer_r2: L0=0.3404, L1=0.4164, L2=0.2169, L3=0.1178, L4=0.3157, L5=0.3061, L6=0.2861, L7=0.2507, L8=0.2143, L9=0.1941, L10=0.1912, L11=0.3643, L12=0.3474, L13=0.3383, L14=0.3237, L15=0.3227, L16=0.2946, L17=0.2817, L18=0.2642, L19=0.2548, L20=0.257, L21=0.2328, L22=0.2289, L23=0.234, L24=0.2454, L25=0.2317, L26=0.364, L27=0.364, L28=0.374, L29=0.371, L30=0.3597, L31=0.2826
n_demos=100, n_total_samples=5000, n_bootstrap=1000
```

#### 2. openvla / goal / untrained
```json
arch: openvla, suite: goal, condition: untrained
peak_r2: 0.4026 @ L10, exit_r2: 0.3039 @ L31
delta: 0.0988, delta_ci_95: [0.0, 0.0484]
bootstrap_deltas: mean=0.012, std=0.015, median=0.007
per_layer_r2: L0=0.3323, L1=0.3882, L2=0.3454, L3=0.2745, L4=0.3489, L5=0.324, L6=0.3306, L7=0.3119, L8=0.3096, L9=0.3002, L10=0.4026, L11=0.3777, L12=0.3529, L13=0.3492, L14=0.3443, L15=0.322, L16=0.3101, L17=0.297, L18=0.2855, L19=0.2884, L20=0.3019, L21=0.2648, L22=0.2524, L23=0.3763, L24=0.3628, L25=0.3491, L26=0.3369, L27=0.3302, L28=0.3196, L29=0.3102, L30=0.3113, L31=0.3039
```

#### 3. openvla / spatial / trained
```json
arch: openvla, suite: spatial, condition: trained
peak_r2: 0.5452 @ L24, exit_r2: 0.4963 @ L31
delta: 0.0489, delta_ci_95: [0.0, 0.0444]
bootstrap_deltas: mean=0.0081, std=0.0118, median=0.0031
per_layer_r2: L0=0.3498, L1=0.5034, L2=0.5077, L3=0.5419, L4=0.5275, L5=0.5183, L6=0.5084, L7=0.4886, L8=0.5286, L9=0.5248, L10=0.518, L11=0.5277, L12=0.5209, L13=0.5166, L14=0.5194, L15=0.5094, L16=0.5096, L17=0.499, L18=0.4958, L19=0.4815, L20=0.5309, L21=0.535, L22=0.5376, L23=0.5433, L24=0.5452, L25=0.5448, L26=0.5402, L27=0.5355, L28=0.5362, L29=0.5215, L30=0.5089, L31=0.4963
```

#### 4. openvla / spatial / untrained
```json
arch: openvla, suite: spatial, condition: untrained
peak_r2: 0.5339 @ L4, exit_r2: 0.518 @ L31
delta: 0.016, delta_ci_95: [0.0, 0.0362]
bootstrap_deltas: mean=0.0123, std=0.01, median=0.0114
per_layer_r2: L0=0.3252, L1=0.4626, L2=0.5271, L3=0.4993, L4=0.5339, L5=0.5285, L6=0.5066, L7=0.4998, L8=0.4763, L9=0.4676, L10=0.515, L11=0.5156, L12=0.5165, L13=0.5188, L14=0.528, L15=0.5221, L16=0.5139, L17=0.5115, L18=0.4947, L19=0.4974, L20=0.4968, L21=0.4869, L22=0.4732, L23=0.4513, L24=0.5032, L25=0.5149, L26=0.5219, L27=0.515, L28=0.5106, L29=0.5105, L30=0.5144, L31=0.518
```

#### 5. openvla / object / trained
```json
arch: openvla, suite: object, condition: trained
peak_r2: 0.5752 @ L21, exit_r2: 0.5509 @ L31
delta: 0.0242, delta_ci_95: [0.0, 0.0269]
bootstrap_deltas: mean=0.0064, std=0.0078, median=0.0041
per_layer_r2: L0=0.4284, L1=0.5301, L2=0.5411, L3=0.5614, L4=0.5664, L5=0.5503, L6=0.523, L7=0.4921, L8=0.5513, L9=0.549, L10=0.5461, L11=0.5461, L12=0.5522, L13=0.5397, L14=0.5411, L15=0.5344, L16=0.5325, L17=0.5249, L18=0.5088, L19=0.5153, L20=0.5221, L21=0.5752, L22=0.5742, L23=0.5712, L24=0.5653, L25=0.5567, L26=0.5562, L27=0.5607, L28=0.5588, L29=0.5511, L30=0.5554, L31=0.5509
```

#### 6. openvla / object / untrained
```json
arch: openvla, suite: object, condition: untrained
peak_r2: 0.5932 @ L14, exit_r2: 0.5407 @ L31
delta: 0.0525, delta_ci_95: [0.0, 0.0575]
bootstrap_deltas: mean=0.0143, std=0.0169, median=0.0085
per_layer_r2: L0=0.4295, L1=0.5338, L2=0.5526, L3=0.5828, L4=0.5854, L5=0.5698, L6=0.5598, L7=0.5579, L8=0.5486, L9=0.57, L10=0.5771, L11=0.586, L12=0.5824, L13=0.5826, L14=0.5932, L15=0.5869, L16=0.5882, L17=0.5683, L18=0.5769, L19=0.5744, L20=0.5639, L21=0.5603, L22=0.5814, L23=0.5809, L24=0.5794, L25=0.5811, L26=0.5766, L27=0.5812, L28=0.5761, L29=0.5701, L30=0.5643, L31=0.5407
```

#### 7. openvla / long / trained
```json
arch: openvla, suite: long, condition: trained
peak_r2: 0.5121 @ L25, exit_r2: 0.4691 @ L31
delta: 0.043, delta_ci_95: [0.0, 0.0591]
bootstrap_deltas: mean=0.0141, std=0.0175, median=0.0084
per_layer_r2: L0=0.3842, L1=0.4677, L2=0.4239, L3=0.375, L4=0.4581, L5=0.4635, L6=0.4413, L7=0.4168, L8=0.4025, L9=0.3918, L10=0.4724, L11=0.477, L12=0.4764, L13=0.4746, L14=0.4731, L15=0.4547, L16=0.4534, L17=0.4646, L18=0.4654, L19=0.444, L20=0.4312, L21=0.4255, L22=0.5105, L23=0.5096, L24=0.5029, L25=0.5121, L26=0.5041, L27=0.4981, L28=0.4945, L29=0.4961, L30=0.496, L31=0.4691
```

#### 8. openvla / long / untrained
```json
arch: openvla, suite: long, condition: untrained
peak_r2: 0.5341 @ L24, exit_r2: 0.508 @ L31
delta: 0.0261, delta_ci_95: [0.0, 0.0692]
bootstrap_deltas: mean=0.0179, std=0.02, median=0.013
per_layer_r2: L0=0.3945, L1=0.4894, L2=0.4866, L3=0.4463, L4=0.5094, L5=0.5076, L6=0.4995, L7=0.4812, L8=0.4595, L9=0.4482, L10=0.412, L11=0.5114, L12=0.5013, L13=0.5008, L14=0.5092, L15=0.5117, L16=0.4898, L17=0.4933, L18=0.4844, L19=0.4798, L20=0.4686, L21=0.4575, L22=0.454, L23=0.4428, L24=0.5341, L25=0.5239, L26=0.5277, L27=0.5292, L28=0.5301, L29=0.5272, L30=0.5336, L31=0.508
```

#### 9. tracvla / goal / trained
```json
arch: tracvla, suite: goal, condition: trained
peak_r2: 0.5399 @ L13, exit_r2: 0.2065 @ L31
delta: 0.3334, delta_ci_95: [0.0924, 0.3545]  ← CI 不包含 0，显著!
bootstrap_deltas: mean=0.1909, std=0.0697, median=0.1788
per_layer_r2: L0=0.455, L1=0.5002, L2=0.5105, L3=0.5059, L4=0.4393, L5=0.4509, L6=0.4767, L7=0.4736, L8=0.439, L9=0.5085, L10=0.5063, L11=0.4576, L12=0.4935, L13=0.5399, L14=0.5241, L15=0.4993, L16=0.4998, L17=0.4547, L18=0.4685, L19=0.4149, L20=0.4452, L21=0.4244, L22=0.3947, L23=0.3503, L24=0.2975, L25=0.2535, L26=0.2392, L27=0.1033, L28=-0.0845, L29=-0.1402, L30=-0.4649, L31=0.2065
```

#### 10. tracvla / goal / untrained
```json
arch: tracvla, suite: goal, condition: untrained
peak_r2: 0.5048 @ L11, exit_r2: 0.4403 @ L31
delta: 0.0645, delta_ci_95: [0.0, 0.0776]
bootstrap_deltas: mean=0.0227, std=0.0231, median=0.0187
per_layer_r2: L0=0.4305, L1=0.4554, L2=0.4816, L3=0.4982, L4=0.4775, L5=0.4805, L6=0.4699, L7=0.4394, L8=0.4493, L9=0.4916, L10=0.487, L11=0.5048, L12=0.4626, L13=0.4641, L14=0.4141, L15=0.4814, L16=0.4519, L17=0.4284, L18=0.411, L19=0.4034, L20=0.3982, L21=0.495, L22=0.4841, L23=0.4803, L24=0.4708, L25=0.4671, L26=0.4537, L27=0.4209, L28=0.3699, L29=0.3528, L30=0.47, L31=0.4403
```

#### 11. tracvla / spatial / trained
```json
arch: tracvla, suite: spatial, condition: trained
peak_r2: 0.6871 @ L13, exit_r2: 0.5315 @ L31
delta: 0.1557, delta_ci_95: [0.0487, 0.1619]  ← 显著!
bootstrap_deltas: mean=0.0986, std=0.0298, median=0.0957
per_layer_r2: L0=0.6202, L1=0.6686, L2=0.6849, L3=0.6854, L4=0.6354, L5=0.6311, L6=0.63, L7=0.6476, L8=0.6192, L9=0.6687, L10=0.6692, L11=0.6507, L12=0.6452, L13=0.6871, L14=0.6828, L15=0.6791, L16=0.6633, L17=0.642, L18=0.6088, L19=0.6356, L20=0.6106, L21=0.5751, L22=0.5589, L23=0.5351, L24=0.5018, L25=0.5208, L26=0.3911, L27=0.3774, L28=0.3316, L29=0.2408, L30=0.1795, L31=0.5315
```

#### 12. tracvla / spatial / untrained
```json
arch: tracvla, suite: spatial, condition: untrained
peak_r2: 0.612 @ L4, exit_r2: 0.5643 @ L31
delta: 0.0477, delta_ci_95: [0.0, 0.0464]
bootstrap_deltas: mean=0.0128, std=0.0137, median=0.0095
per_layer_r2: L0=0.451, L1=0.514, L2=0.5829, L3=0.5938, L4=0.612, L5=0.5916, L6=0.582, L7=0.57, L8=0.5058, L9=0.5669, L10=0.57, L11=0.5818, L12=0.5717, L13=0.5476, L14=0.5432, L15=0.5854, L16=0.5861, L17=0.5713, L18=0.5836, L19=0.5654, L20=0.546, L21=0.543, L22=0.5975, L23=0.5931, L24=0.5894, L25=0.5812, L26=0.5736, L27=0.5668, L28=0.5449, L29=0.542, L30=0.5748, L31=0.5643
```

#### 13. tracvla / object / trained
```json
arch: tracvla, suite: object, condition: trained
peak_r2: 0.6315 @ L13, exit_r2: 0.2692 @ L31
delta: 0.3623, delta_ci_95: [0.0735, 0.3719]  ← 显著!
bootstrap_deltas: mean=0.195, std=0.077, median=0.1858
per_layer_r2: L0=0.5904, L1=0.6108, L2=0.6149, L3=0.6016, L4=0.5578, L5=0.5939, L6=0.5886, L7=0.597, L8=0.5636, L9=0.623, L10=0.6194, L11=0.6067, L12=0.5676, L13=0.6315, L14=0.6257, L15=0.6093, L16=0.6218, L17=0.6047, L18=0.6161, L19=0.5991, L20=0.5623, L21=0.5424, L22=0.5124, L23=0.5102, L24=0.4937, L25=0.4675, L26=0.3802, L27=0.2803, L28=0.2306, L29=0.1797, L30=0.0148, L31=0.2692
```

#### 14. nora / goal / trained
```json
arch: nora, suite: goal, condition: trained  (36 layers, L0-L35)
peak_r2: 0.4489 @ L8, exit_r2: -0.0062 @ L35
delta: 0.4551, delta_ci_95: [1.0253, 1.8867]  ← 注意: CI远大于delta本身，bootstrap可能有异常
bootstrap_deltas: mean=1.3777, std=0.2108, median=1.3484
per_layer_r2: L0=0.3683 ... L8=0.4489(peak) ... L30=0.2892 ... L35=-0.0062
```

#### 15. nora / goal / untrained
```json
arch: nora, suite: goal, condition: untrained  (36 layers)
peak_r2: 0.4203 @ L5, exit_r2: 0.3397 @ L35
delta: 0.0806, delta_ci_95: [0.0046, 0.1076]  ← 显著!
bootstrap_deltas: mean=0.0517, std=0.0477, median=0.0481
per_layer_r2: L0=0.3856 ... L5=0.4203(peak) ... L22=0.4085 ... L35=0.3397
```

#### 16. nora / spatial / trained
```json
arch: nora, suite: spatial, condition: trained  (36 layers)
peak_r2: 0.5763 @ L20, exit_r2: 0.2683 @ L35
delta: 0.308, delta_ci_95: [0.1097, 0.4715]  ← 显著!
bootstrap_deltas: mean=0.2663, std=0.0957, median=0.2569
per_layer_r2: L0=0.4823 ... L20=0.5763(peak) ... L33=0.2703 ... L35=0.2683
```

#### 17. nora / spatial / untrained
```json
arch: nora, suite: spatial, condition: untrained  (36 layers)
peak_r2: 0.5125 @ L4, exit_r2: 0.424 @ L35
delta: 0.0885, delta_ci_95: [0.0002, 0.0873]  ← 勉强显著
bootstrap_deltas: mean=0.0381, std=0.0221, median=0.036
per_layer_r2: L0=0.4837 ... L4=0.5125(peak) ... L18=0.5109 ... L35=0.424
```

---

### 显著性速查表（CI 不包含 0 = 显著）

| # | Arch | Suite | Cond | Peak R² | Exit R² | Delta | CI_95 | 显著? |
|---|------|-------|------|---------|---------|-------|-------|-------|
| 1 | openvla | goal | trained | 0.416@L1 | 0.283@L31 | 0.134 | [0, 0.074] | No |
| 2 | openvla | goal | untrained | 0.403@L10 | 0.304@L31 | 0.099 | [0, 0.048] | No |
| 3 | openvla | spatial | trained | 0.545@L24 | 0.496@L31 | 0.049 | [0, 0.044] | No |
| 4 | openvla | spatial | untrained | 0.534@L4 | 0.518@L31 | 0.016 | [0, 0.036] | No |
| 5 | openvla | object | trained | 0.575@L21 | 0.551@L31 | 0.024 | [0, 0.027] | No |
| 6 | openvla | object | untrained | 0.593@L14 | 0.541@L31 | 0.053 | [0, 0.058] | No |
| 7 | openvla | long | trained | 0.512@L25 | 0.469@L31 | 0.043 | [0, 0.059] | No |
| 8 | openvla | long | untrained | 0.534@L24 | 0.508@L31 | 0.026 | [0, 0.069] | No |
| 9 | **tracvla** | **goal** | **trained** | **0.540@L13** | **0.207@L31** | **0.333** | **[0.092, 0.355]** | **Yes** |
| 10 | tracvla | goal | untrained | 0.505@L11 | 0.440@L31 | 0.065 | [0, 0.078] | No |
| 11 | **tracvla** | **spatial** | **trained** | **0.687@L13** | **0.532@L31** | **0.156** | **[0.049, 0.162]** | **Yes** |
| 12 | tracvla | spatial | untrained | 0.612@L4 | 0.564@L31 | 0.048 | [0, 0.046] | No |
| 13 | **tracvla** | **object** | **trained** | **0.632@L13** | **0.269@L31** | **0.362** | **[0.074, 0.372]** | **Yes** |
| 14 | **nora** | **goal** | **trained** | **0.449@L8** | **-0.006@L35** | **0.455** | **[1.025, 1.887]** | **Yes*** |
| 15 | **nora** | **goal** | **untrained** | **0.420@L5** | **0.340@L35** | **0.081** | **[0.005, 0.108]** | **Yes** |
| 16 | **nora** | **spatial** | **trained** | **0.576@L20** | **0.268@L35** | **0.308** | **[0.110, 0.472]** | **Yes** |
| 17 | nora | spatial | untrained | 0.513@L4 | 0.424@L35 | 0.089 | [0.000, 0.087] | Marginal |

*nora/goal/trained 的 bootstrap CI [1.025, 1.887] 远超 canonical delta 0.455，bootstrap 分布可能有问题（variance 极大或 exit layer 不稳定）。

### 日志无错误。cuda1 预计还需 1-2 小时完成剩余 3 个条件。

---
