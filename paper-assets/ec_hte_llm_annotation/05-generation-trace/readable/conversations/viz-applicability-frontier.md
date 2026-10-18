# viz applicability frontier

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_viz_applicability-frontier_20260521T131949.jsonl`
- **Structured JSON:** [`c0f577d3e414a5ca5e29.json`](../../sessions/c0/c0f577d3e414a5ca5e29.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-21T13:24:51.184821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp001_hb_results_v2.csv",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp001_hb_results_v2.csv",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T13:24:51.185460+00:00_

1	regime,n_expert,k_subgroups,subgroup,method,bias_z0,rmse_z0,coverage_z0,bias_z1,rmse_z1,coverage_z1,bias_z0_se,rmse_z0_se,bias_z1_se,rmse_z1_se
2	extreme,50,2,A,global_corrected,0.0419069214759441,0.0948316868974548,0.9,-0.0447841536140324,0.1009053812158317,0.92,0.0085069728882993,0.006277615116952,0.0090422760096045,0.0069082006871354
3	extreme,50,2,A,hb_dirichlet,-0.0407358153033897,0.2008839065231489,0.87,0.0333561830322693,0.195896670721699,0.89,0.0196710287609899,0.0324946122374873,0.0193035930990485,0.0316347921085781
4	extreme,50,2,A,mle_laplace,-0.0447999748980635,0.2207981209191847,0.9,0.0374912741848124,0.2160219183134855,0.89,0.021620539412923,0.0436122660693167,0.0212743680403995,0.043197850384468
5	extreme,50,2,A,naive,0.0975680337471985,0.1162336137316838,0.68,-0.0999931570178252,0.1203757891595256,0.67,0.006317223877489,0.0058499455732945,0.0067020139998265,0.0066216950480105
6	extreme,50,2,A,oracle,-0.0020416673648791,0.0604751419272658,0.96,-0.0014788365306621,0.068121871796001,0.93,0.0060440668307805,0.0037509642077601,0.0068105818103201,0.0046896446168449
7	extreme,50,2,B,global_corrected,-0.0914251725138643,0.1270187653535856,0.83,0.0737899889594724,0.1122252688462482,0.85,0.0088177120517509,0.0081659040031459,0.0084555002790926,0.0074712492224381
8	extreme,50,2,B,hb_dirichlet,-0.0376479364723482,0.0764595245844048,0.96,0.0271758092225553,0.0799411041606548,0.96,0.0066548416803461,0.0050203704100773,0.0075180153814181,0.0067427042818766
9	extreme,50,2,B,mle_laplace,-0.0444907218062021,0.0799775582711805,0.94,0.0333961068331738,0.0822359803009619,0.93,0.0066460405507213,0.0049903203216076,0.0075149560906551,0.006950286866694
10	extreme,50,2,B,naive,0.0085372707084391,0.0579205496215187,0.99,-0.0254487911537092,0.0655762525078565,0.95,0.0057287913885126,0.0033635837160605,0.0060436776235906,0.0043159557642836
11	extreme,50,2,B,oracle,-0.0115136967464799,0.0589578879380852,0.98,-0.0049187208168962,0.0615249584745558,0.97,0.0057822723365039,0.0036
…[truncated 3667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T13:24:51.185844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp003_phase_a_v3.csv",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp003_phase_a_v3.csv",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T13:24:51.186184+00:00_

1	regime,n_expert,method,level,bias_z0,rmse_z0,coverage_z0,bias_z0_se,bias_z1,rmse_z1,coverage_z1,bias_z1_se
2	extreme,50,global_corrected,S0,-0.03534275798748018,0.08669415582453324,0.85,0.007956171679749314,0.1109579049798617,0.23880726096469368,0.68,0.021252985818025778
3	extreme,50,global_corrected,S1,-0.010995916308599965,0.07096789353413342,0.93,0.0070464058731637925,0.03647024734618422,0.17207582669405067,0.84,0.016901380970099914
4	extreme,50,global_corrected,S2,0.005520613231890927,0.13154348415342343,0.94,0.013208969654021732,0.03427524031496108,0.20088244613780795,0.96,0.01989339392601387
5	extreme,50,global_corrected,S3,-0.014176385921270927,0.12149057939752252,0.95,0.012126850984221097,-0.03190769617318731,0.19085087085472155,0.94,0.01891126376745014
6	extreme,50,global_corrected,marginal,-0.017437837426638843,0.058008911924762006,0.91,0.00556046260027524,0.051288292663250544,0.15396963474260936,0.75,0.014590767614502573
7	extreme,50,hb_ec_hte,S0,-0.02970663489512883,0.09050712357318057,0.84,0.008592371094008714,0.11911647366545963,0.32845359291020476,0.62,0.030763521031143694
8	extreme,50,hb_ec_hte,S1,-0.020073471552115918,0.09221900994171853,0.89,0.009046122856345288,0.12990991590970163,0.3823485115258341,0.73,0.03614138873843922
9	extreme,50,hb_ec_hte,S2,-0.06684253203133939,0.4985044041466665,0.9,0.04964914444472895,0.3212975675295203,1.7684613825326716,0.85,0.17477903899151576
10	extreme,50,hb_ec_hte,S3,-0.027587183962024073,0.5859992889097478,0.95,0.05882984485183233,0.048069915114084844,1.0941176428277426,0.95,0.10985678002404362
11	extreme,50,hb_ec_hte,marginal,-0.029900621291044194,0.10698806671556138,0.86,0.01032423806269409,0.13869477420774726,0.330049728098338,0.79,0.030100267226782645
12	extreme,50,naive,S0,0.001597104674733294,0.06250147548418125,0.94,0.0062795834758266654,-0.03683922218111064,0.09388294906918818,0.89,0.00867882587309717
13	extreme,50,naive,S1,0.012847783140188742,0.05700075054929507,0.92,0.005581372366234139,-0.0575942765
…[truncated 2829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T13:24:51.186498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp013_boundary_condition.csv",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp013_boundary_condition.csv",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T13:24:51.186781+00:00_

1	mc_run,subgroup,method,z_level,tau_corrected,tau_true,se_corrected,coverage
2	0,A,naive,z0,0.22073268690751013,0.1,0.08984202940975,1
3	0,A,naive,z1,0.2683053383446192,0.5,0.09033248413389942,0
4	0,A,global_corrected,z0,0.20976944213188006,0.1,0.11248938389872705,1
5	0,A,global_corrected,z1,0.28103053317347554,0.5,0.11699036933459982,1
6	0,A,mle_laplace,z0,0.16995803008521093,0.1,0.20926401786411933,1
7	0,A,mle_laplace,z1,0.3155120463091352,0.5,0.20084105038948402,1
8	0,A,hb_eb,z0,0.17865042171701187,0.1,0.18722403393225637,1
9	0,A,hb_eb,z1,0.3068665990914543,0.5,0.17903398967004214,1
10	0,B,naive,z0,0.2352368098929284,0.1,0.08588659839646512,1
11	0,B,naive,z1,0.3677201509119956,0.5,0.08518781149961989,1
12	0,B,global_corrected,z0,0.2047056695757771,0.1,0.10748739662892469,1
13	0,B,global_corrected,z1,0.4031580816372604,0.5,0.11039168900895656,1
14	0,B,mle_laplace,z0,0.1854140149797748,0.1,0.12245090645960595,1
15	0,B,mle_laplace,z1,0.41459887158028097,0.5,0.11926807937941808,1
16	0,B,hb_eb,z0,0.20285206664312866,0.1,0.10889069469927921,1
17	0,B,hb_eb,z1,0.39335386127592736,0.5,0.10301961699781596,1
18	0,C,naive,z0,0.04564792276018892,0.1,0.0940288122019198,1
19	0,C,naive,z1,0.29316917513103036,0.5,0.09285132174639095,0
20	0,C,global_corrected,z0,-0.011394011942556436,0.1,0.11766008403198622,1
21	0,C,global_corrected,z1,0.3593785636252883,0.5,0.12034574249501821,1
22	0,C,mle_laplace,z0,-0.06043261397017171,0.1,0.14009720123942346,1
23	0,C,mle_laplace,z1,0.4699700696816314,0.5,0.17276339978214977,1
24	0,C,hb_eb,z0,0.0019244787888440939,0.1,0.11184769208230066,1
25	0,C,hb_eb,z1,0.42342612774006116,0.5,0.15010438341181867,1
26	0,D,naive,z0,0.08461805819815305,0.1,0.08286341470218091,1
27	0,D,naive,z1,0.6195163488816202,0.5,0.09011172328740204,1
28	0,D,global_corrected,z0,-0.03865068368774886,0.1,0.10405281709296582,1
29	0,D,global_corrected,z1,0.7625961385706134,0.5,0.11634652638102957,0
30	0,D,mle_laplace,z0,0.011643185910816454,0.1,0.09496735474748315,1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T13:24:51.187087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp015_semi_real_raw.csv",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/results/exp015_semi_real_raw.csv",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T13:24:51.187392+00:00_

1	seed,n_expert,subgroup,z_level,method,cate,oracle_cate,bias,ci_lo,ci_hi,coverage,abs_bias,squared_error
2	0,100,S0,0,oracle,0.33211949803961804,0.3,0.032119498039618055,0.23700081702768586,0.42723817905155026,1,0.032119498039618055,0.0010316621543170282
3	0,100,S0,0,naive,0.4113280584737231,0.3,0.11132805847372312,0.3173424234985137,0.5053136934489325,0,0.11132805847372312,0.012393936603528714
4	0,100,S0,0,global_corrected,0.39198224175685276,0.3,0.09198224175685277,0.2709785141857287,0.5129859693279768,1,0.09198224175685277,0.00846073279861611
5	0,100,S0,0,hb_ec_hte,0.36263353892272837,0.3,0.06263353892272838,0.25824644765630367,0.4670206301891531,1,0.06263353892272838,0.003922960197984931
6	0,100,S0,1,oracle,0.7829024613727693,0.8,-0.017097538627230735,0.5711618894555494,0.9946430332899893,1,0.017097538627230735,0.00029232582710964707
7	0,100,S0,1,naive,0.41102730517293806,0.8,-0.388972694827062,0.1677017616546872,0.6543528486911889,0,0.388972694827062,0.15129975732102668
8	0,100,S0,1,global_corrected,0.540300204904407,0.8,-0.25969979509559304,-0.22401900596851887,1.3046194157773328,1,0.25969979509559304,0.06744398357269302
9	0,100,S0,1,hb_ec_hte,0.7762082747131791,0.8,-0.02379172528682094,0.22714348501027004,1.3252730644160882,1,0.02379172528682094,0.000566046192123555
10	0,100,S1,0,oracle,0.3702897642519276,0.4,-0.02971023574807241,0.2421188188285098,0.4984607096753454,1,0.02971023574807241,0.0008826981082060398
11	0,100,S1,0,naive,0.35066903136637606,0.4,-0.04933096863362396,0.21800014487437575,0.4833379178583764,1,0.04933096863362396,0.002433544466331591
12	0,100,S1,0,global_corrected,0.31478271758077336,0.4,-0.08521728241922666,0.15164421100959866,0.47792122415194804,1,0.08521728241922666,0.007261985222918237
13	0,100,S1,0,hb_ec_hte,0.35721476650728673,0.4,-0.04278523349271329,0.19800315933228313,0.5164263736822903,1,0.04278523349271329,0.0018305762050259953
14	0,100,S1,1,oracle,0.3811641876065166,0.65,-0.2688358123934834,0.09459067486319084,0.6677377003498
…[truncated 2528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T13:24:51.187757+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\n\n# exp-001\ndf1 = pd.read_csv('results/exp001_hb_results_v2.csv')\nprint('=== EXP-001 ===')\nprint('regimes:', df1['regime'].unique())\nprint('n_expert:', sorted(df1['n_expert'].unique()))\nprint('k_subgroups:', sorted(df1['k_subgroups'].unique()))\nprint('methods:', df1['method'].unique())\nprint('subgroups:', df1['subgroup'].unique())\nprint()\n\n# exp-003\ndf3 = pd.read_csv('results/exp003_phase_a_v3.csv')\nprint('=== EXP-003 ===')\nprint('regimes:', df3['regime'].unique())\nprint('n_expert:', sorted(df3['n_expert'].unique()))\nprint('methods:', df3['method'].unique())\nprint('levels:', df3['level'].unique())\nprint()\n\n# exp-013\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\nprint('=== EXP-013 ===')\nprint('n_expert (unique):', sorted(df13.groupby(['mc_run'])['subgroup'].first().index[:5].tolist()))\nprint('subgroups:', df13['subgroup'].unique())\nprint('methods:', df13['method'].unique())\nprint('z_levels:', df13['z_level'].unique())\nprint('rows:', len(df13))\nprint()\n\n# exp-015\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nprint('=== EXP-015 ===')\nprint('n_expert:', sorted(df15['n_expert'].unique()))\nprint('subgroups:', df15['subgroup'].unique())\nprint('methods:', df15['method'].unique())\nprint('z_levels:', df15['z_level'].unique())\nprint('rows:', len(df15))\n\"\n",
  "description": "Explore structure of all 4 experiment CSVs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\n\n# exp-001\ndf1 = pd.read_csv('results/exp001_hb_results_v2.csv')\nprint('=== EXP-001 ===')\nprint('regimes:', df1['regime'].unique())\nprint('n_expert:', sorted(df1['n_expert'].unique()))\nprint('k_subgroups:', sorted(df1['k_subgroups'].unique()))\nprint('methods:', df1['method'].unique())\nprint('subgroups:', df1['subgroup'].unique())\nprint()\n\n# exp-003\ndf3 = pd.read_csv('results/exp003_phase_a_v3.csv')\nprint('=== EXP-003 ===')\nprint('regimes:', df3['regime'].unique())\nprint('n_expert:', sorted(df3['n_expert'].unique()))\nprint('methods:', df3['method'].unique())\nprint('levels:', df3['level'].unique())\nprint()\n\n# exp-013\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\nprint('=== EXP-013 ===')\nprint('n_expert (unique):', sorted(df13.groupby(['mc_run'])['subgroup'].first().index[:5].tolist()))\nprint('subgroups:', df13['subgroup'].unique())\nprint('methods:', df13['method'].unique())\nprint('z_levels:', df13['z_level'].unique())\nprint('rows:', len(df13))\nprint()\n\n# exp-015\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nprint('=== EXP-015 ===')\nprint('n_expert:', sorted(df15['n_expert'].unique()))\nprint('subgroups:', df15['subgroup'].unique())\nprint('methods:', df15['method'].unique())\nprint('z_levels:', df15['z_level'].unique())\nprint('rows:', len(df15))\n\"\n",
    "description": "Explore structure of all 4 experiment CSVs"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T13:24:51.188092+00:00_

=== EXP-001 ===
regimes: &lt;ArrowStringArray>
['extreme', 'homogeneous', 'moderate']
Length: 3, dtype: str
n_expert: [np.int64(50), np.int64(100), np.int64(250), np.int64(500), np.int64(1000), np.int64(2000)]
k_subgroups: [np.int64(2), np.int64(4)]
methods: &lt;ArrowStringArray>
['global_corrected',     'hb_dirichlet',      'mle_laplace',
            'naive',           'oracle', 'hb_dirichlet_reg',
  'mle_laplace_reg']
Length: 7, dtype: str
subgroups: &lt;ArrowStringArray>
['A', 'B', 'C', 'D']
Length: 4, dtype: str

=== EXP-003 ===
regimes: &lt;ArrowStringArray>
['extreme', 'homogeneous', 'moderate']
Length: 3, dtype: str
n_expert: [np.int64(50), np.int64(100), np.int64(250), np.int64(500)]
methods: &lt;ArrowStringArray>
['global_corrected', 'hb_ec_hte', 'naive', 'oracle', 'stratified_mle']
Length: 5, dtype: str
levels: &lt;ArrowStringArray>
['S0', 'S1', 'S2', 'S3', 'marginal']
Length: 5, dtype: str

=== EXP-013 ===
n_expert (unique): [0, 1, 2, 3, 4]
subgroups: &lt;ArrowStringArray>
['A', 'B', 'C', 'D']
Length: 4, dtype: str
methods: &lt;ArrowStringArray>
['naive', 'global_corrected', 'mle_laplace', 'hb_eb']
Length: 4, dtype: str
z_levels: &lt;ArrowStringArray>
['z0', 'z1']
Length: 2, dtype: str
rows: 3200

=== EXP-015 ===
n_expert: [np.int64(100), np.int64(250), np.int64(500)]
subgroups: &lt;ArrowStringArray>
['S0', 'S1', 'S2', 'S3']
Length: 4, dtype: str
methods: &lt;ArrowStringArray>
['oracle', 'naive', 'global_corrected', 'hb_ec_hte']
Length: 4, dtype: str
z_levels: [0 1]
rows: 9600

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T13:24:51.188387+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-001: Compute worst-subgroup RMSE for HB vs Global at each (regime, K, n_expert) ===\ndf1 = pd.read_csv('results/exp001_hb_results_v2.csv')\ndf1 = df1[df1['regime'] == 'extreme']\n\n# avg RMSE across z0/z1\ndf1['avg_rmse'] = (df1['rmse_z0'] + df1['rmse_z1']) / 2\n\nfor method in ['hb_dirichlet', 'global_corrected']:\n    for k in [2, 4]:\n        sub = df1[(df1['method'] == method) & (df1['k_subgroups'] == k)]\n        # worst subgroup RMSE per n_expert\n        worst = sub.groupby('n_expert')['avg_rmse'].max().reset_index()\n        worst.columns = ['n_expert', 'worst_rmse']\n        worst['n_expert_per_K'] = worst['n_expert'] / k\n        print(f'exp001 {method} K={k}:')\n        print(worst[['n_expert', 'n_expert_per_K', 'worst_rmse']].to_string(index=False))\n        print()\n\"\n",
  "description": "Extract exp-001 worst-subgroup RMSE for HB vs Global"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-001: Compute worst-subgroup RMSE for HB vs Global at each (regime, K, n_expert) ===\ndf1 = pd.read_csv('results/exp001_hb_results_v2.csv')\ndf1 = df1[df1['regime'] == 'extreme']\n\n# avg RMSE across z0/z1\ndf1['avg_rmse'] = (df1['rmse_z0'] + df1['rmse_z1']) / 2\n\nfor method in ['hb_dirichlet', 'global_corrected']:\n    for k in [2, 4]:\n        sub = df1[(df1['method'] == method) & (df1['k_subgroups'] == k)]\n        # worst subgroup RMSE per n_expert\n        worst = sub.groupby('n_expert')['avg_rmse'].max().reset_index()\n        worst.columns = ['n_expert', 'worst_rmse']\n        worst['n_expert_per_K'] = worst['n_expert'] / k\n        print(f'exp001 {method} K={k}:')\n        print(worst[['n_expert', 'n_expert_per_K', 'worst_rmse']].to_string(index=False))\n        print()\n\"\n",
    "description": "Extract exp-001 worst-subgroup RMSE for HB vs Global"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T13:24:51.188667+00:00_

exp001 hb_dirichlet K=2:
 n_expert  n_expert_per_K  worst_rmse
       50            25.0    0.198390
      100            50.0    0.133503
      250           125.0    0.121386
      500           250.0    0.111458
     1000           500.0    0.106101
     2000          1000.0    0.102716

exp001 hb_dirichlet K=4:
 n_expert  n_expert_per_K  worst_rmse
       50            12.5  509.933807
      100            25.0   11.560158
      250            62.5    0.208470
      500           125.0    0.183985
     1000           250.0    0.179505
     2000           500.0    0.174650

exp001 global_corrected K=2:
 n_expert  n_expert_per_K  worst_rmse
       50            25.0    0.119622
      100            50.0    0.108357
      250           125.0    0.100703
      500           250.0    0.097596
     1000           500.0    0.097507
     2000          1000.0    0.096993

exp001 global_corrected K=4:
 n_expert  n_expert_per_K  worst_rmse
       50            12.5    0.161445
      100            25.0    0.146808
      250            62.5    0.140566
      500           125.0    0.140507
     1000           250.0    0.140681
     2000           500.0    0.140674

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T13:24:51.188978+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-003: worst-subgroup RMSE for HB vs Global (extreme regime) ===\ndf3 = pd.read_csv('results/exp003_phase_a_v3.csv')\ndf3 = df3[(df3['regime'] == 'extreme') & (df3['level'] != 'marginal')]\n\n# avg RMSE across z0/z1\ndf3['avg_rmse'] = (df3['rmse_z0'] + df3['rmse_z1']) / 2\n\nK_003 = 4  # 4 subgroups (S0-S3)\nfor method in ['hb_ec_hte', 'global_corrected']:\n    sub = df3[df3['method'] == method]\n    worst = sub.groupby('n_expert')['avg_rmse'].max().reset_index()\n    worst.columns = ['n_expert', 'worst_rmse']\n    worst['n_expert_per_K'] = worst['n_expert'] / K_003\n    print(f'exp003 {method}:')\n    print(worst[['n_expert', 'n_expert_per_K', 'worst_rmse']].to_string(index=False))\n    print()\n\n# === EXP-013: worst-subgroup RMSE for HB vs Global ===\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\n# avg over MC runs\ndf13['rmse'] = np.sqrt(df13['squared_error'])  # wait, no squared_error is per-row\n# Actually let's compute mean squared error then RMSE\nagg = df13.groupby(['subgroup', 'z_level', 'method']).agg(\n    mean_se=('squared_error', 'mean')\n).reset_index()\nagg['rmse'] = np.sqrt(agg['mean_se'])\n\n# avg RMSE across z0/z1\npivot = agg.groupby(['subgroup', 'method'])['rmse'].mean().reset_index()\nfor method in ['hb_eb', 'global_corrected', 'naive']:\n    sub = pivot[pivot['method'] == method]\n    print(f'exp013 {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\nprint()\n\n# === EXP-015: worst-subgroup RMSE for HB vs Global ===\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nagg15 = df15.groupby(['n_expert', 'subgroup', 'z_level', 'method']).agg(\n    mean_se=('squared_error', 'mean')\n).reset_index()\nagg15['rmse'] = np.sqrt(agg15['mean_se'])\n\npivot15 = agg15.groupby(['n_expert', 'subgroup', 'method'])['rmse'].mean().reset_index()\nfor n in sorted(df15['n_expert'].unique()):\n    for method in ['hb_ec_hte', 'global_corrected', 'naive']:\n        sub = pivot15[(pivot15['n_expert'] == n) & (pivot15['method'] == method)]\n        print(f'exp015 n={n} {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\n    print()\n\"\n",
  "description": "Extract exp-003/013/015 worst-subgroup RMSE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-003: worst-subgroup RMSE for HB vs Global (extreme regime) ===\ndf3 = pd.read_csv('results/exp003_phase_a_v3.csv')\ndf3 = df3[(df3['regime'] == 'extreme') & (df3['level'] != 'marginal')]\n\n# avg RMSE across z0/z1\ndf3['avg_rmse'] = (df3['rmse_z0'] + df3['rmse_z1']) / 2\n\nK_003 = 4  # 4 subgroups (S0-S3)\nfor method in ['hb_ec_hte', 'global_corrected']:\n    sub = df3[df3['method'] == method]\n    worst = sub.groupby('n_expert')['avg_rmse'].max().reset_index()\n    worst.columns = ['n_expert', 'worst_rmse']\n    worst['n_expert_per_K'] = worst['n_expert'] / K_003\n    print(f'exp003 {method}:')\n    print(worst[['n_expert', 'n_expert_per_K', 'worst_rmse']].to_string(index=False))\n    print()\n\n# === EXP-013: worst-subgroup RMSE for HB vs Global ===\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\n# avg over MC runs\ndf13['rmse'] = np.sqrt(df13['squared_error'])  # wait, no squared_error is per-row\n# Actually let's compute mean squared error then RMSE\nagg = df13.groupby(['subgroup', 'z_level', 'method']).agg(\n    mean_se=('squared_error', 'mean')\n).reset_index()\nagg['rmse'] = np.sqrt(agg['mean_se'])\n\n# avg RMSE across z0/z1\npivot = agg.groupby(['subgroup', 'method'])['rmse'].mean().reset_index()\nfor method in ['hb_eb', 'global_corrected', 'naive']:\n    sub = pivot[pivot['method'] == method]\n    print(f'exp013 {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\nprint()\n\n# === EXP-015: worst-subgroup RMSE for HB vs Global ===\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nagg15 = df15.groupby(['n_expert', 'subgroup', 'z_level', 'method']).agg(\n    mean_se=('squared_error', 'mean')\n).reset_index()\nagg15['rmse'] = np.sqrt(agg15['mean_se'])\n\npivot15 = agg15.groupby(['n_expert', 'subgroup', 'method'])['rmse'].mean().reset_index()\nfor n in sorted(df15['n_expert'].unique()):\n    for method in ['hb_ec_hte', 'global_corrected', 'naive']:\n        sub = pivot15[(pivot15['n_expert'] == n) & (pivot15['method'] == method)]\n        print(f'exp015 n={n} {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\n    print()\n\"\n",
    "description": "Extract exp-003/013/015 worst-subgroup RMSE"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T13:24:51.189272+00:00_

Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.local/lib/python3.14/site-packages/pandas/core/indexes/base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'squared_error'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "&lt;string>", line 25, in &lt;module>
    df13['rmse'] = np.sqrt(df13['squared_error'])  # wait, no squared_error is per-row
                           ~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.local/lib/python3.14/site-packages/pandas/core/frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/ubuntu/.local/lib/python3.14/site-packages/pandas/core/indexes/base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'squared_error'
exp003 hb_ec_hte:
 n_expert  n_expert_per_K  worst_rmse
       50            12.5    1.133483
      100            25.0    0.433222
      250            62.5    0.480219
      500           125.0    0.269703

exp003 global_corrected:
 n_expert  n_expert_per_K  worst_rmse
       50            12.5    0.166213
      100            25.0    0.157832
      250            62.5    0.152308
      500           125.0    0.149104

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T13:24:51.189565+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\nprint('exp013 columns:', list(df13.columns))\nprint()\n\n# Compute RMSE from tau_corrected and tau_true\ndf13['sq_err'] = (df13['tau_corrected'] - df13['tau_true'])**2\nagg = df13.groupby(['subgroup', 'z_level', 'method']).agg(\n    mean_se=('sq_err', 'mean')\n).reset_index()\nagg['rmse'] = np.sqrt(agg['mean_se'])\n\npivot = agg.groupby(['subgroup', 'method'])['rmse'].mean().reset_index()\nfor method in ['hb_eb', 'global_corrected', 'naive']:\n    sub = pivot[pivot['method'] == method]\n    print(f'exp013 {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\nprint()\n\n# exp-015\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nprint('exp015 columns:', list(df15.columns))\ndf15['sq_err'] = (df15['cate'] - df15['oracle_cate'])**2\nagg15 = df15.groupby(['n_expert', 'subgroup', 'z_level', 'method']).agg(\n    mean_se=('sq_err', 'mean')\n).reset_index()\nagg15['rmse'] = np.sqrt(agg15['mean_se'])\n\npivot15 = agg15.groupby(['n_expert', 'subgroup', 'method'])['rmse'].mean().reset_index()\nfor n in sorted(df15['n_expert'].unique()):\n    for method in ['hb_ec_hte', 'global_corrected', 'naive']:\n        sub = pivot15[(pivot15['n_expert'] == n) & (pivot15['method'] == method)]\n        if len(sub) > 0:\n            print(f'exp015 n={n} {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\n    print()\n\"\n",
  "description": "Extract exp-013 and exp-015 RMSE data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\nprint('exp013 columns:', list(df13.columns))\nprint()\n\n# Compute RMSE from tau_corrected and tau_true\ndf13['sq_err'] = (df13['tau_corrected'] - df13['tau_true'])**2\nagg = df13.groupby(['subgroup', 'z_level', 'method']).agg(\n    mean_se=('sq_err', 'mean')\n).reset_index()\nagg['rmse'] = np.sqrt(agg['mean_se'])\n\npivot = agg.groupby(['subgroup', 'method'])['rmse'].mean().reset_index()\nfor method in ['hb_eb', 'global_corrected', 'naive']:\n    sub = pivot[pivot['method'] == method]\n    print(f'exp013 {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\nprint()\n\n# exp-015\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nprint('exp015 columns:', list(df15.columns))\ndf15['sq_err'] = (df15['cate'] - df15['oracle_cate'])**2\nagg15 = df15.groupby(['n_expert', 'subgroup', 'z_level', 'method']).agg(\n    mean_se=('sq_err', 'mean')\n).reset_index()\nagg15['rmse'] = np.sqrt(agg15['mean_se'])\n\npivot15 = agg15.groupby(['n_expert', 'subgroup', 'method'])['rmse'].mean().reset_index()\nfor n in sorted(df15['n_expert'].unique()):\n    for method in ['hb_ec_hte', 'global_corrected', 'naive']:\n        sub = pivot15[(pivot15['n_expert'] == n) & (pivot15['method'] == method)]\n        if len(sub) > 0:\n            print(f'exp015 n={n} {method}: worst subgroup RMSE = {sub[\\\"rmse\\\"].max():.4f} (subgroup={sub.loc[sub[\\\"rmse\\\"].idxmax(), \\\"subgroup\\\"]})')\n    print()\n\"\n",
    "description": "Extract exp-013 and exp-015 RMSE data"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T13:24:51.189878+00:00_

exp013 columns: ['mc_run', 'subgroup', 'method', 'z_level', 'tau_corrected', 'tau_true', 'se_corrected', 'coverage']

exp013 hb_eb: worst subgroup RMSE = 0.6131 (subgroup=A)
exp013 global_corrected: worst subgroup RMSE = 0.1614 (subgroup=D)
exp013 naive: worst subgroup RMSE = 0.1523 (subgroup=A)

exp015 columns: ['seed', 'n_expert', 'subgroup', 'z_level', 'method', 'cate', 'oracle_cate', 'bias', 'ci_lo', 'ci_hi', 'coverage', 'abs_bias', 'squared_error']
exp015 n=100 hb_ec_hte: worst subgroup RMSE = 0.9151 (subgroup=S1)
exp015 n=100 global_corrected: worst subgroup RMSE = 0.3108 (subgroup=S2)
exp015 n=100 naive: worst subgroup RMSE = 0.1410 (subgroup=S0)

exp015 n=250 hb_ec_hte: worst subgroup RMSE = 0.5897 (subgroup=S2)
exp015 n=250 global_corrected: worst subgroup RMSE = 0.2755 (subgroup=S2)
exp015 n=250 naive: worst subgroup RMSE = 0.1410 (subgroup=S0)

exp015 n=500 hb_ec_hte: worst subgroup RMSE = 0.3643 (subgroup=S2)
exp015 n=500 global_corrected: worst subgroup RMSE = 0.2351 (subgroup=S2)
exp015 n=500 naive: worst subgroup RMSE = 0.1410 (subgroup=S0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T13:24:51.190228+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "extreme.*misclass|misclass.*extreme|MISCLASS_RATES|misclass_rate",
  "-i": "True",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Grep",
  "tool_args": {
    "pattern": "extreme.*misclass|misclass.*extreme|MISCLASS_RATES|misclass_rate",
    "-i": "True",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T13:24:51.190488+00:00_

Found 18 files
results/exp004_confusion_matrices.csv
results/exp008_multi_llm_comparison.csv
exp004_hate_speech.py
exp008_multi_llm.py
results/exp013_boundary_analysis.md
results/pilot_gpt41_run.log
pilot_gemini_annotation.py
exp007_ppci_dsl.py
results/exp003_hb_rerun.log
exp011_causal_forest.py
exp003_tweeteval.py
exp005_diagnostic_criterion.py
results/ucb_hate_speech_exploration.md
exp001_hb_synthetic.py
results/exp003_v2_run.log
results/exp003_run.log
mvp_simulation.py
results/mvp_v2_100mc_log.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T13:24:51.190743+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "extreme|misclass|REGIMES",
  "path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "output_mode": "content",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Grep",
  "tool_args": {
    "pattern": "extreme|misclass|REGIMES",
    "path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "output_mode": "content",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T13:24:51.191082+00:00_

3-exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4-
5-Compares confusion matrix estimators for CATE correction under heterogeneous
6:misclassification across subgroups:
7-  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8-
9-Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
--
33-N = 5000
34-SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35-
36:REGIMES = {
37-    2: {
38:        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39:        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40:        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41-    },
42-    4: {
43:        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44:        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45:        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46-    },
47-}
48-
--
63-    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64-    mc_rates = np.zeros(N)
65-    for i, s in enumerate(labels):
66:        mc_rates[S == s] = regime_params['misclass'][i]
67-    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68-    idx = rng.choice(N, min(n_expert, N), replace=False)
69-    expert_mask = np.zeros(N, dtype=bool)
--
529-    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530-    for k in sorted(df_agg['k_subgroups'].unique()):
531-        print(f"\n  K = {int(k)} subgroups")
532:        for regime in ['extreme', 'moderate', 'homogeneous']:
533-            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534-            if sub.empty:
535-                continue
--
557-def run_sweep(regime_names, n_experts, k_list, n_mc,
558-              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559-    all_rows, all_diag = [], []
560:    total = sum(1 f
…[truncated 981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T13:24:51.191468+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-001: Compute AVERAGE RMSE across all subgroups for HB vs Global ===\ndf1 = pd.read_csv('results/exp001_hb_results_v2.csv')\ndf1 = df1[df1['regime'] == 'extreme']\ndf1['avg_rmse'] = (df1['rmse_z0'] + df1['rmse_z1']) / 2\n\nfor k in [2, 4]:\n    print(f'=== K={k} extreme ===')\n    for method in ['hb_dirichlet', 'global_corrected', 'naive']:\n        sub = df1[(df1['method'] == method) & (df1['k_subgroups'] == k)]\n        # Mean RMSE across all subgroups (not worst)\n        avg_by_n = sub.groupby('n_expert')['avg_rmse'].mean().reset_index()\n        avg_by_n.columns = ['n_expert', 'mean_rmse']\n        avg_by_n['n_per_K'] = avg_by_n['n_expert'] / k\n        print(f'  {method}:')\n        for _, r in avg_by_n.iterrows():\n            print(f'    n/K={r[\\\"n_per_K\\\"]:>8.1f}  avg_rmse={r[\\\"mean_rmse\\\"]:.4f}')\n    print()\n\n# Also compute HB/Global ratio to find crossover\nfor k in [2, 4]:\n    hb = df1[(df1['method'] == 'hb_dirichlet') & (df1['k_subgroups'] == k)]\n    gl = df1[(df1['method'] == 'global_corrected') & (df1['k_subgroups'] == k)]\n    hb_avg = hb.groupby('n_expert')['avg_rmse'].mean()\n    gl_avg = gl.groupby('n_expert')['avg_rmse'].mean()\n    ratio = hb_avg / gl_avg\n    print(f'K={k} HB/Global ratio:')\n    for n, r in ratio.items():\n        print(f'  n/K={n/k:>8.1f}  ratio={r:.3f} {\\\"<-- HB wins\\\" if r < 1 else \\\"\\\"}')\n    print()\n\"\n",
  "description": "Compute avg RMSE and crossover for exp-001"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-001: Compute AVERAGE RMSE across all subgroups for HB vs Global ===\ndf1 = pd.read_csv('results/exp001_hb_results_v2.csv')\ndf1 = df1[df1['regime'] == 'extreme']\ndf1['avg_rmse'] = (df1['rmse_z0'] + df1['rmse_z1']) / 2\n\nfor k in [2, 4]:\n    print(f'=== K={k} extreme ===')\n    for method in ['hb_dirichlet', 'global_corrected', 'naive']:\n        sub = df1[(df1['method'] == method) & (df1['k_subgroups'] == k)]\n        # Mean RMSE across all subgroups (not worst)\n        avg_by_n = sub.groupby('n_expert')['avg_rmse'].mean().reset_index()\n        avg_by_n.columns = ['n_expert', 'mean_rmse']\n        avg_by_n['n_per_K'] = avg_by_n['n_expert'] / k\n        print(f'  {method}:')\n        for _, r in avg_by_n.iterrows():\n            print(f'    n/K={r[\\\"n_per_K\\\"]:>8.1f}  avg_rmse={r[\\\"mean_rmse\\\"]:.4f}')\n    print()\n\n# Also compute HB/Global ratio to find crossover\nfor k in [2, 4]:\n    hb = df1[(df1['method'] == 'hb_dirichlet') & (df1['k_subgroups'] == k)]\n    gl = df1[(df1['method'] == 'global_corrected') & (df1['k_subgroups'] == k)]\n    hb_avg = hb.groupby('n_expert')['avg_rmse'].mean()\n    gl_avg = gl.groupby('n_expert')['avg_rmse'].mean()\n    ratio = hb_avg / gl_avg\n    print(f'K={k} HB/Global ratio:')\n    for n, r in ratio.items():\n        print(f'  n/K={n/k:>8.1f}  ratio={r:.3f} {\\\"<-- HB wins\\\" if r < 1 else \\\"\\\"}')\n    print()\n\"\n",
    "description": "Compute avg RMSE and crossover for exp-001"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T13:24:51.191778+00:00_

=== K=2 extreme ===
  hb_dirichlet:
    n/K=    25.0  avg_rmse=0.1383
    n/K=    50.0  avg_rmse=0.1026
    n/K=   125.0  avg_rmse=0.0934
    n/K=   250.0  avg_rmse=0.0878
    n/K=   500.0  avg_rmse=0.0850
    n/K=  1000.0  avg_rmse=0.0832
  global_corrected:
    n/K=    25.0  avg_rmse=0.1087
    n/K=    50.0  avg_rmse=0.1029
    n/K=   125.0  avg_rmse=0.0994
    n/K=   250.0  avg_rmse=0.0972
    n/K=   500.0  avg_rmse=0.0968
    n/K=  1000.0  avg_rmse=0.0964
  naive:
    n/K=    25.0  avg_rmse=0.0900
    n/K=    50.0  avg_rmse=0.0900
    n/K=   125.0  avg_rmse=0.0900
    n/K=   250.0  avg_rmse=0.0900
    n/K=   500.0  avg_rmse=0.0900
    n/K=  1000.0  avg_rmse=0.0900

=== K=4 extreme ===
  hb_dirichlet:
    n/K=    12.5  avg_rmse=128.3390
    n/K=    25.0  avg_rmse=3.0000
    n/K=    62.5  avg_rmse=0.1352
    n/K=   125.0  avg_rmse=0.1266
    n/K=   250.0  avg_rmse=0.1228
    n/K=   500.0  avg_rmse=0.1210
  global_corrected:
    n/K=    12.5  avg_rmse=0.1394
    n/K=    25.0  avg_rmse=0.1318
    n/K=    62.5  avg_rmse=0.1274
    n/K=   125.0  avg_rmse=0.1253
    n/K=   250.0  avg_rmse=0.1249
    n/K=   500.0  avg_rmse=0.1245
  naive:
    n/K=    12.5  avg_rmse=0.1126
    n/K=    25.0  avg_rmse=0.1126
    n/K=    62.5  avg_rmse=0.1126
    n/K=   125.0  avg_rmse=0.1126
    n/K=   250.0  avg_rmse=0.1126
    n/K=   500.0  avg_rmse=0.1126

K=2 HB/Global ratio:
  n/K=    25.0  ratio=1.272 
  n/K=    50.0  ratio=0.997 <-- HB wins
  n/K=   125.0  ratio=0.939 <-- HB wins
  n/K=   250.0  ratio=0.903 <-- HB wins
  n/K=   500.0  ratio=0.878 <-- HB wins
  n/K=  1000.0  ratio=0.863 <-- HB wins

K=4 HB/Global ratio:
  n/K=    12.5  ratio=920.707 
  n/K=    25.0  ratio=22.763 
  n/K=    62.5  ratio=1.061 
  n/K=   125.0  ratio=1.010 
  n/K=   250.0  ratio=0.983 <-- HB wins
  n/K=   500.0  ratio=0.972 <-- HB wins

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T13:24:51.192152+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-003: HB vs Global avg RMSE ===\ndf3 = pd.read_csv('results/exp003_phase_a_v3.csv')\ndf3 = df3[(df3['regime'] == 'extreme') & (df3['level'] != 'marginal')]\ndf3['avg_rmse'] = (df3['rmse_z0'] + df3['rmse_z1']) / 2\n\nK = 4\nfor method in ['hb_ec_hte', 'global_corrected', 'naive']:\n    sub = df3[df3['method'] == method]\n    avg_by_n = sub.groupby('n_expert')['avg_rmse'].mean().reset_index()\n    avg_by_n.columns = ['n_expert', 'mean_rmse']\n    avg_by_n['n_per_K'] = avg_by_n['n_expert'] / K\n    print(f'exp003 {method}:')\n    for _, r in avg_by_n.iterrows():\n        print(f'  n/K={r[\\\"n_per_K\\\"]:>8.1f}  avg_rmse={r[\\\"mean_rmse\\\"]:.4f}')\n    print()\n\nhb = df3[df3['method'] == 'hb_ec_hte'].groupby('n_expert')[['avg_rmse']].mean()\ngl = df3[df3['method'] == 'global_corrected'].groupby('n_expert')[['avg_rmse']].mean()\nratio = hb['avg_rmse'] / gl['avg_rmse']\nprint('exp003 HB/Global ratio:')\nfor n, r in ratio.items():\n    print(f'  n/K={n/K:>8.1f}  ratio={r:.3f} {\\\"<-- HB wins\\\" if r < 1 else \\\"\\\"}')\nprint()\n\n# === EXP-013: HB vs Global ===\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\ndf13['sq_err'] = (df13['tau_corrected'] - df13['tau_true'])**2\nagg = df13.groupby(['subgroup', 'z_level', 'method']).agg(mean_se=('sq_err', 'mean')).reset_index()\nagg['rmse'] = np.sqrt(agg['mean_se'])\npivot = agg.groupby(['method'])['rmse'].mean().reset_index()\nprint('exp013 avg RMSE across subgroups (n=50, K=4, n/K=12.5):')\nfor _, r in pivot.iterrows():\n    print(f'  {r[\\\"method\\\"]}: {r[\\\"rmse\\\"]:.4f}')\nprint()\n\n# === EXP-015: HB vs Global ===\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nagg15 = df15.groupby(['n_expert', 'subgroup', 'z_level', 'method']).agg(\n    mean_se=('squared_error', 'mean')\n).reset_index()\nagg15['rmse'] = np.sqrt(agg15['mean_se'])\npivot15 = agg15.groupby(['n_expert', 'method'])['rmse'].mean().reset_index()\nprint('exp015 avg RMSE (K=4):')\nfor n in sorted(df15['n_expert'].unique()):\n    for method in ['hb_ec_hte', 'global_corrected', 'naive']:\n        sub = pivot15[(pivot15['n_expert'] == n) & (pivot15['method'] == method)]\n        if len(sub) > 0:\n            print(f'  n={n} n/K={n/4:.1f} {method}: {sub[\\\"rmse\\\"].values[0]:.4f}')\n    print()\n\"\n",
  "description": "Compute HB/Global ratios for exp-003, 013, 015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# === EXP-003: HB vs Global avg RMSE ===\ndf3 = pd.read_csv('results/exp003_phase_a_v3.csv')\ndf3 = df3[(df3['regime'] == 'extreme') & (df3['level'] != 'marginal')]\ndf3['avg_rmse'] = (df3['rmse_z0'] + df3['rmse_z1']) / 2\n\nK = 4\nfor method in ['hb_ec_hte', 'global_corrected', 'naive']:\n    sub = df3[df3['method'] == method]\n    avg_by_n = sub.groupby('n_expert')['avg_rmse'].mean().reset_index()\n    avg_by_n.columns = ['n_expert', 'mean_rmse']\n    avg_by_n['n_per_K'] = avg_by_n['n_expert'] / K\n    print(f'exp003 {method}:')\n    for _, r in avg_by_n.iterrows():\n        print(f'  n/K={r[\\\"n_per_K\\\"]:>8.1f}  avg_rmse={r[\\\"mean_rmse\\\"]:.4f}')\n    print()\n\nhb = df3[df3['method'] == 'hb_ec_hte'].groupby('n_expert')[['avg_rmse']].mean()\ngl = df3[df3['method'] == 'global_corrected'].groupby('n_expert')[['avg_rmse']].mean()\nratio = hb['avg_rmse'] / gl['avg_rmse']\nprint('exp003 HB/Global ratio:')\nfor n, r in ratio.items():\n    print(f'  n/K={n/K:>8.1f}  ratio={r:.3f} {\\\"<-- HB wins\\\" if r < 1 else \\\"\\\"}')\nprint()\n\n# === EXP-013: HB vs Global ===\ndf13 = pd.read_csv('results/exp013_boundary_condition.csv')\ndf13['sq_err'] = (df13['tau_corrected'] - df13['tau_true'])**2\nagg = df13.groupby(['subgroup', 'z_level', 'method']).agg(mean_se=('sq_err', 'mean')).reset_index()\nagg['rmse'] = np.sqrt(agg['mean_se'])\npivot = agg.groupby(['method'])['rmse'].mean().reset_index()\nprint('exp013 avg RMSE across subgroups (n=50, K=4, n/K=12.5):')\nfor _, r in pivot.iterrows():\n    print(f'  {r[\\\"method\\\"]}: {r[\\\"rmse\\\"]:.4f}')\nprint()\n\n# === EXP-015: HB vs Global ===\ndf15 = pd.read_csv('results/exp015_semi_real_raw.csv')\nagg15 = df15.groupby(['n_expert', 'subgroup', 'z_level', 'method']).agg(\n    mean_se=('squared_error', 'mean')\n).reset_index()\nagg15['rmse'] = np.sqrt(agg15['mean_se'])\npivot15 = agg15.groupby(['n_expert', 'method'])['rmse'].mean().reset_index()\nprint('exp015 avg RMSE (K=4):')\nfor n in sorted(df15['n_expert'].unique()):\n    for method in ['hb_ec_hte', 'global_corrected', 'naive']:\n        sub = pivot15[(pivot15['n_expert'] == n) & (pivot15['method'] == method)]\n        if len(sub) > 0:\n            print(f'  n={n} n/K={n/4:.1f} {method}: {sub[\\\"rmse\\\"].values[0]:.4f}')\n    print()\n\"\n",
    "description": "Compute HB/Global ratios for exp-003, 013, 015"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T13:24:51.192483+00:00_

exp003 hb_ec_hte:
  n/K=    12.5  avg_rmse=0.6051
  n/K=    25.0  avg_rmse=0.2822
  n/K=    62.5  avg_rmse=0.2251
  n/K=   125.0  avg_rmse=0.1589

exp003 global_corrected:
  n/K=    12.5  avg_rmse=0.1517
  n/K=    25.0  avg_rmse=0.1340
  n/K=    62.5  avg_rmse=0.1245
  n/K=   125.0  avg_rmse=0.1196

exp003 naive:
  n/K=    12.5  avg_rmse=0.1030
  n/K=    25.0  avg_rmse=0.1030
  n/K=    62.5  avg_rmse=0.1030
  n/K=   125.0  avg_rmse=0.1030

exp003 HB/Global ratio:
  n/K=    12.5  ratio=3.990 
  n/K=    25.0  ratio=2.106 
  n/K=    62.5  ratio=1.807 
  n/K=   125.0  ratio=1.329 

exp013 avg RMSE across subgroups (n=50, K=4, n/K=12.5):
  global_corrected: 0.1394
  hb_eb: 0.2953
  mle_laplace: 0.2813
  naive: 0.1126

exp015 avg RMSE (K=4):
  n=100 n/K=25.0 hb_ec_hte: 0.7842
  n=100 n/K=25.0 global_corrected: 0.2631
  n=100 n/K=25.0 naive: 0.1230

  n=250 n/K=62.5 hb_ec_hte: 0.4113
  n=250 n/K=62.5 global_corrected: 0.2318
  n=250 n/K=62.5 naive: 0.1230

  n=500 n/K=125.0 hb_ec_hte: 0.2599
  n=500 n/K=125.0 global_corrected: 0.1963
  n=500 n/K=125.0 naive: 0.1230

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T13:24:51.192847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/ec_hte_llm_annotation/artifacts/figures",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/ec_hte_llm_annotation/artifacts/figures",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T13:24:51.193107+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T13:24:51.193415+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
  "content": "\"\"\"\nApplicability Frontier: When does EC-HTE help?\nCombines data from exp-001, exp-003, exp-013, exp-015.\n\"\"\"\n\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.lines import Line2D\nimport warnings\nwarnings.filterwarnings('ignore')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['Times New Roman', 'DejaVu Serif'],\n    'mathtext.fontset': 'dejavuserif',\n    'font.size': 10,\n    'axes.labelsize': 12,\n    'axes.titlesize': 13,\n    'legend.fontsize': 8.5,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 9,\n    'figure.dpi': 150,\n})\n\n# ── Data extraction ──────────────────────────────────────────────────────\n\ndef load_exp001():\n    df = pd.read_csv('results/exp001_hb_results_v2.csv')\n    df = df[df['regime'] == 'extreme']\n    df['avg_rmse'] = (df['rmse_z0'] + df['rmse_z1']) / 2\n\n    rows = []\n    for k in [2, 4]:\n        worst_misclass = {2: 0.25, 4: 0.30}[k]\n        hb = df[(df['method'] == 'hb_dirichlet') & (df['k_subgroups'] == k)]\n        gl = df[(df['method'] == 'global_corrected') & (df['k_subgroups'] == k)]\n        hb_avg = hb.groupby('n_expert')['avg_rmse'].mean()\n        gl_avg = gl.groupby('n_expert')['avg_rmse'].mean()\n        for n in hb_avg.index:\n            ratio = hb_avg[n] / gl_avg[n]\n            rows.append({\n                'exp': f'exp-001 (K={k})',\n                'n_per_K': n / k,\n                'worst_misclass': worst_misclass,\n                'hb_rmse': hb_avg[n],\n                'gl_rmse': gl_avg[n],\n                'ratio': ratio,\n            })\n    return pd.DataFrame(rows)\n\n\ndef load_exp003():\n    df = pd.read_csv('results/exp003_phase_a_v3.csv')\n    df = df[(df['regime'] == 'extreme') & (df['level'] != 'marginal')]\n    df['avg_rmse'] = (df['rmse_z0'] + df['rmse_z1']) / 2\n\n    K = 4\n    worst_misclass = 0.25\n    hb = df[df['method'] == 'hb_ec_hte'].groupby('n_expert')['avg_rmse'].mean()\n    gl = df[df['method'] == 'global_corrected'].groupby('n_expert')['avg_rmse'].mean()\n\n    rows = []\n    for n in hb.index:\n        ratio = hb[n] / gl[n]\n        rows.append({\n            'exp': 'exp-003',\n            'n_per_K': n / K,\n            'worst_misclass': worst_misclass,\n            'hb_rmse': hb[n],\n            'gl_rmse': gl[n],\n            'ratio': ratio,\n        })\n    return pd.DataFrame(rows)\n\n\ndef load_exp013():\n    df = pd.read_csv('results/exp013_boundary_condition.csv')\n    df['sq_err'] = (df['tau_corrected'] - df['tau_true'])**2\n    agg = df.groupby(['method']).agg(mean_se=('sq_err', 'mean')).reset_index()\n    agg['rmse'] = np.sqrt(agg['mean_se'])\n\n    hb_rmse = agg.loc[agg['method'] == 'hb_eb', 'rmse'].values[0]\n    gl_rmse = agg.loc[agg['method'] == 'global_corrected', 'rmse'].values[0]\n\n    return pd.DataFrame([{\n        'exp': 'exp-013',\n        'n_per_K': 12.5,\n        'worst_misclass': 0.30,\n        'hb_rmse': hb_rmse,\n        'gl_rmse': gl_rmse,\n        'ratio': hb_rmse / gl_rmse,\n    }])\n\n\ndef load_exp015():\n    df = pd.read_csv('results/exp015_semi_real_raw.csv')\n    agg = df.groupby(['n_expert', 'method']).agg(mean_se=('squared_error', 'mean')).reset_index()\n    agg['rmse'] = np.sqrt(agg['mean_se'])\n\n    K = 4\n    worst_fnr = 0.526\n    rows = []\n    for n in sorted(df['n_expert'].unique()):\n        hb_rmse = agg.loc[(agg['n_expert'] == n) & (agg['method'] == 'hb_ec_hte'), 'rmse'].values[0]\n        gl_rmse = agg.loc[(agg['n_expert'] == n) & (agg['method'] == 'global_corrected'), 'rmse'].values[0]\n        rows.append({\n            'exp': 'exp-015',\n            'n_per_K': n / K,\n            'worst_misclass': worst_fnr,\n            'hb_rmse': hb_rmse,\n            'gl_rmse': gl_rmse,\n            'ratio': hb_rmse / gl_rmse,\n        })\n    return pd.DataFrame(rows)\n\n\n# ── Classify outcome ─────────────────────────────────────────────────────\n\ndef classify(ratio):\n    if ratio < 0.95:\n        return 'green'\n    elif ratio <= 1.05:\n        return 'yellow'\n    else:\n        return 'red'\n\n\n# ── Load all data ────────────────────────────────────────────────────────\n\ndata = pd.concat([load_exp001(), load_exp003(), load_exp013(), load_exp015()], ignore_index=True)\ndata['outcome'] = data['ratio'].apply(classify)\n\n# ── Plot ─────────────────────────────────────────────────────────────────\n\nfig, ax = plt.subplots(figsize=(8, 5.5))\n\n# Background shading for regions\nx_range = np.array([5, 2000])\n\n# Red zone: high FNR (>0.5) — always fails\nax.axhspan(0.45, 0.60, color='#FFCCCC', alpha=0.35, zorder=0)\nax.axhspan(0.32, 0.45, color='#FFF3CD', alpha=0.25, zorder=0)\n\n# Green zone approximation: low misclass + high budget\n# Fill a polygon for the \"safe\" region\ngreen_x = [80, 2000, 2000, 150]\ngreen_y = [0.18, 0.18, 0.32, 0.32]\nax.fill(green_x, green_y, color='#C8E6C9', alpha=0.35, zorder=0)\n\n# Additional green for very high budget\ngreen_x2 = [40, 80, 150, 2000, 2000, 40]\ngreen_y2 = [0.18, 0.18, 0.32, 0.32, 0.18, 0.18]\n\n# Marker styles per experiment\nmarker_map = {\n    'exp-001 (K=2)': ('o', 55),\n    'exp-001 (K=4)': ('s', 55),\n    'exp-003': ('^', 60),\n    'exp-013': ('X', 80),\n    'exp-015': ('D', 55),\n}\n\ncolor_map = {\n    'green': '#2E7D32',\n    'yellow': '#F9A825',\n    'red': '#C62828',\n}\n\n# Plot each experiment's points\nfor exp_name, (marker, ms) in marker_map.items():\n    sub = data[data['exp'] == exp_name]\n    for _, row in sub.iterrows():\n        c = color_map[row['outcome']]\n        edgecolor = 'black' if row['outcome'] != 'red' else '#8B0000'\n        ax.scatter(row['n_per_K'], row['worst_misclass'], marker=marker,\n                   s=ms, c=c, edgecolors=edgecolor, linewidths=0.8, zorder=5)\n\n# Threshold lines\nax.axvline(x=25, color='#555555', linestyle='--', linewidth=1.0, alpha=0.7, zorder=2)\nax.axhline(y=0.50, color='#555555', linestyle=':', linewidth=1.0, alpha=0.7, zorder=2)\n\n# Threshold annotations\nax.annotate(r'$n_{\\mathrm{expert}}/K = 25$' + '\\n(budget threshold)',\n            xy=(25, 0.195), fontsize=7.5, color='#333333', ha='right',\n            fontstyle='italic', va='top',\n            rotation=90)\nax.annotate('worst FNR = 0.5\\n(classifier quality\\n threshold)',\n            xy=(1500, 0.505), fontsize=7.5, color='#333333', ha='right',\n            va='bottom', fontstyle='italic')\n\n# Annotate specific crossover points for exp-001\nax.annotate('K=2 crossover\\n' + r'($n/K \\approx 50$)',\n            xy=(50, 0.25), xytext=(15, 0.21),\n            fontsize=7, color='#2E7D32', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=0.8))\n\nax.annotate('K=4 crossover\\n' + r'($n/K \\approx 250$)',\n            xy=(250, 0.30), xytext=(600, 0.355),\n            fontsize=7, color='#2E7D32', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=0.8))\n\n# Annotate exp-013 failure\nax.annotate('exp-013: 2.1× worse\\n(boundary failure)',\n            xy=(12.5, 0.30), xytext=(8, 0.38),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))\n\n# Annotate exp-015 failures\nax.annotate('exp-015: real GPT-4.1\\n(poor classifier quality)',\n            xy=(62.5, 0.526), xytext=(200, 0.555),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))\n\n# Region labels\nax.text(500, 0.22, 'EC-HTE\\nbeneficial', fontsize=9, color='#1B5E20',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.7)\nax.text(30, 0.545, 'EC-HTE\\nfails', fontsize=9, color='#B71C1C',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.6)\n\n# Axes\nax.set_xscale('log')\nax.set_xlabel(r'Expert budget per subgroup ($n_{\\mathrm{expert}} / K$)')\nax.set_ylabel('Worst-subgroup misclassification rate (or FNR)')\nax.set_title('Applicability Frontier: When Does EC-HTE Help?', fontweight='bold', pad=12)\nax.set_xlim(8, 1500)\nax.set_ylim(0.17, 0.58)\n\n# Light grid\nax.grid(True, which='major', color='#E0E0E0', linewidth=0.5, zorder=0)\nax.grid(True, which='minor', color='#F0F0F0', linewidth=0.3, zorder=0, alpha=0.5)\nax.set_axisbelow(True)\n\n# Custom x-tick labels\nax.set_xticks([10, 25, 50, 100, 250, 500, 1000])\nax.set_xticklabels(['10', '25', '50', '100', '250', '500', '1000'])\n\n# Legend\nlegend_elements = [\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',\n           markersize=7, markeredgecolor='black', label='exp-001 (K=2, synthetic)'),\n    Line2D([0], [0], marker='s', color='w', markerfacecolor='gray',\n           markersize=7, markeredgecolor='black', label='exp-001 (K=4, synthetic)'),\n    Line2D([0], [0], marker='^', color='w', markerfacecolor='gray',\n           markersize=7, markeredgecolor='black', label='exp-003 (TweetEval semi-synth.)'),\n    Line2D([0], [0], marker='X', color='w', markerfacecolor='gray',\n           markersize=8, markeredgecolor='black', label='exp-013 (boundary, K=4, n=50)'),\n    Line2D([0], [0], marker='D', color='w', markerfacecolor='gray',\n           markersize=6, markeredgecolor='black', label='exp-015 (real GPT-4.1 CM)'),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#2E7D32',\n           markersize=7, markeredgecolor='black', label='HB wins (ratio < 0.95)'),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#F9A825',\n           markersize=7, markeredgecolor='black', label='Comparable (0.95–1.05)'),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#C62828',\n           markersize=7, markeredgecolor='#8B0000', label='HB worse (ratio > 1.05)'),\n]\n\nax.legend(handles=legend_elements, loc='lower right', framealpha=0.9,\n          edgecolor='#CCCCCC', ncol=2, columnspacing=1.0, handletextpad=0.5)\n\nfig.tight_layout()\n\n# Save\nfig.savefig('artifacts/figures/applicability_frontier.pdf', bbox_inches='tight')\nfig.savefig('artifacts/figures/applicability_frontier.png', bbox_inches='tight', dpi=300)\nprint('Saved to artifacts/figures/applicability_frontier.{pdf,png}')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
    "content": "\"\"\"\nApplicability Frontier: When does EC-HTE help?\nCombines data from exp-001, exp-003, exp-013, exp-015.\n\"\"\"\n\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.lines import Line2D\nimport warnings\nwarnings.filterwarnings('ignore')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['Times New Roman', 'DejaVu Serif'],\n    'mathtext.fontset': 'dejavuserif',\n    'font.size': 10,\n    'axes.labelsize': 12,\n    'axes.titlesize': 13,\n    'legend.fontsize': 8.5,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 9,\n    'figure.dpi': 150,\n})\n\n# ── Data extraction ──────────────────────────────────────────────────────\n\ndef load_exp001():\n    df = pd.read_csv('results/exp001_hb_results_v2.csv')\n    df = df[df['regime'] == 'extreme']\n    df['avg_rmse'] = (df['rmse_z0'] + df['rmse_z1']) / 2\n\n    rows = []\n    for k in [2, 4]:\n        worst_misclass = {2: 0.25, 4: 0.30}[k]\n        hb = df[(df['method'] == 'hb_dirichlet') & (df['k_subgroups'] == k)]\n        gl = df[(df['method'] == 'global_corrected') & (df['k_subgroups'] == k)]\n        hb_avg = hb.groupby('n_expert')['avg_rmse'].mean()\n        gl_avg = gl.groupby('n_expert')['avg_rmse'].mean()\n        for n in hb_avg.index:\n            ratio = hb_avg[n] / gl_avg[n]\n            rows.append({\n                'exp': f'exp-001 (K={k})',\n                'n_per_K': n / k,\n                'worst_misclass': worst_misclass,\n                'hb_rmse': hb_avg[n],\n                'gl_rmse': gl_avg[n],\n                'ratio': ratio,\n            })\n    return pd.DataFrame(rows)\n\n\ndef load_exp003():\n    df = pd.read_csv('results/exp003_phase_a_v3.csv')\n    df = df[(df['regime'] == 'extreme') & (df['level'] != 'marginal')]\n    df['avg_rmse'] = (df['rmse_z0'] + df['rmse_z1']) / 2\n\n    K = 4\n    worst_misclass = 0.25\n    hb = df[df['method'] == 'hb_ec_hte'].groupby('n_expert')['avg_rmse'].mean()\n    gl = df[df['method'] == 'global_corrected'].groupby('n_expert')['avg_rmse'].mean()\n\n    rows = []\n    for n in hb.index:\n        ratio = hb[n] / gl[n]\n        rows.append({\n            'exp': 'exp-003',\n            'n_per_K': n / K,\n            'worst_misclass': worst_misclass,\n            'hb_rmse': hb[n],\n            'gl_rmse': gl[n],\n            'ratio': ratio,\n        })\n    return pd.DataFrame(rows)\n\n\ndef load_exp013():\n    df = pd.read_csv('results/exp013_boundary_condition.csv')\n    df['sq_err'] = (df['tau_corrected'] - df['tau_true'])**2\n    agg = df.groupby(['method']).agg(mean_se=('sq_err', 'mean')).reset_index()\n    agg['rmse'] = np.sqrt(agg['mean_se'])\n\n    hb_rmse = agg.loc[agg['method'] == 'hb_eb', 'rmse'].values[0]\n    gl_rmse = agg.loc[agg['method'] == 'global_corrected', 'rmse'].values[0]\n\n    return pd.DataFrame([{\n        'exp': 'exp-013',\n        'n_per_K': 12.5,\n        'worst_misclass': 0.30,\n        'hb_rmse': hb_rmse,\n        'gl_rmse': gl_rmse,\n        'ratio': hb_rmse / gl_rmse,\n    }])\n\n\ndef load_exp015():\n    df = pd.read_csv('results/exp015_semi_real_raw.csv')\n    agg = df.groupby(['n_expert', 'method']).agg(mean_se=('squared_error', 'mean')).reset_index()\n    agg['rmse'] = np.sqrt(agg['mean_se'])\n\n    K = 4\n    worst_fnr = 0.526\n    rows = []\n    for n in sorted(df['n_expert'].unique()):\n        hb_rmse = agg.loc[(agg['n_expert'] == n) & (agg['method'] == 'hb_ec_hte'), 'rmse'].values[0]\n        gl_rmse = agg.loc[(agg['n_expert'] == n) & (agg['method'] == 'global_corrected'), 'rmse'].values[0]\n        rows.append({\n            'exp': 'exp-015',\n            'n_per_K': n / K,\n            'worst_misclass': worst_fnr,\n            'hb_rmse': hb_rmse,\n            'gl_rmse': gl_rmse,\n            'ratio': hb_rmse / gl_rmse,\n        })\n    return pd.DataFrame(rows)\n\n\n# ── Classify outcome ─────────────────────────────────────────────────────\n\ndef classify(ratio):\n    if ratio < 0.95:\n        return 'green'\n    elif ratio <= 1.05:\n        return 'yellow'\n    else:\n        return 'red'\n\n\n# ── Load all data ────────────────────────────────────────────────────────\n\ndata = pd.concat([load_exp001(), load_exp003(), load_exp013(), load_exp015()], ignore_index=True)\ndata['outcome'] = data['ratio'].apply(classify)\n\n# ── Plot ─────────────────────────────────────────────────────────────────\n\nfig, ax = plt.subplots(figsize=(8, 5.5))\n\n# Background shading for regions\nx_range = np.array([5, 2000])\n\n# Red zone: high FNR (>0.5) — always fails\nax.axhspan(0.45, 0.60, color='#FFCCCC', alpha=0.35, zorder=0)\nax.axhspan(0.32, 0.45, color='#FFF3CD', alpha=0.25, zorder=0)\n\n# Green zone approximation: low misclass + high budget\n# Fill a polygon for the \"safe\" region\ngreen_x = [80, 2000, 2000, 150]\ngreen_y = [0.18, 0.18, 0.32, 0.32]\nax.fill(green_x, green_y, color='#C8E6C9', alpha=0.35, zorder=0)\n\n# Additional green for very high budget\ngreen_x2 = [40, 80, 150, 2000, 2000, 40]\ngreen_y2 = [0.18, 0.18, 0.32, 0.32, 0.18, 0.18]\n\n# Marker styles per experiment\nmarker_map = {\n    'exp-001 (K=2)': ('o', 55),\n    'exp-001 (K=4)': ('s', 55),\n    'exp-003': ('^', 60),\n    'exp-013': ('X', 80),\n    'exp-015': ('D', 55),\n}\n\ncolor_map = {\n    'green': '#2E7D32',\n    'yellow': '#F9A825',\n    'red': '#C62828',\n}\n\n# Plot each experiment's points\nfor exp_name, (marker, ms) in marker_map.items():\n    sub = data[data['exp'] == exp_name]\n    for _, row in sub.iterrows():\n        c = color_map[row['outcome']]\n        edgecolor = 'black' if row['outcome'] != 'red' else '#8B0000'\n        ax.scatter(row['n_per_K'], row['worst_misclass'], marker=marker,\n                   s=ms, c=c, edgecolors=edgecolor, linewidths=0.8, zorder=5)\n\n# Threshold lines\nax.axvline(x=25, color='#555555', linestyle='--', linewidth=1.0, alpha=0.7, zorder=2)\nax.axhline(y=0.50, color='#555555', linestyle=':', linewidth=1.0, alpha=0.7, zorder=2)\n\n# Threshold annotations\nax.annotate(r'$n_{\\mathrm{expert}}/K = 25$' + '\\n(budget threshold)',\n            xy=(25, 0.195), fontsize=7.5, color='#333333', ha='right',\n            fontstyle='italic', va='top',\n            rotation=90)\nax.annotate('worst FNR = 0.5\\n(classifier quality\\n threshold)',\n            xy=(1500, 0.505), fontsize=7.5, color='#333333', ha='right',\n            va='bottom', fontstyle='italic')\n\n# Annotate specific crossover points for exp-001\nax.annotate('K=2 crossover\\n' + r'($n/K \\approx 50$)',\n            xy=(50, 0.25), xytext=(15, 0.21),\n            fontsize=7, color='#2E7D32', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=0.8))\n\nax.annotate('K=4 crossover\\n' + r'($n/K \\approx 250$)',\n            xy=(250, 0.30), xytext=(600, 0.355),\n            fontsize=7, color='#2E7D32', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=0.8))\n\n# Annotate exp-013 failure\nax.annotate('exp-013: 2.1× worse\\n(boundary failure)',\n            xy=(12.5, 0.30), xytext=(8, 0.38),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))\n\n# Annotate exp-015 failures\nax.annotate('exp-015: real GPT-4.1\\n(poor classifier quality)',\n            xy=(62.5, 0.526), xytext=(200, 0.555),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))\n\n# Region labels\nax.text(500, 0.22, 'EC-HTE\\nbeneficial', fontsize=9, color='#1B5E20',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.7)\nax.text(30, 0.545, 'EC-HTE\\nfails', fontsize=9, color='#B71C1C',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.6)\n\n# Axes\nax.set_xscale('log')\nax.set_xlabel(r'Expert budget per subgroup ($n_{\\mathrm{expert}} / K$)')\nax.set_ylabel('Worst-subgroup misclassification rate (or FNR)')\nax.set_title('Applicability Frontier: When Does EC-HTE Help?', fontweight='bold', pad=12)\nax.set_xlim(8, 1500)\nax.set_ylim(0.17, 0.58)\n\n# Light grid\nax.grid(True, which='major', color='#E0E0E0', linewidth=0.5, zorder=0)\nax.grid(True, which='minor', color='#F0F0F0', linewidth=0.3, zorder=0, alpha=0.5)\nax.set_axisbelow(True)\n\n# Custom x-tick labels\nax.set_xticks([10, 25, 50, 100, 250, 500, 1000])\nax.set_xticklabels(['10', '25', '50', '100', '250', '500', '1000'])\n\n# Legend\nlegend_elements = [\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',\n           markersize=7, markeredgecolor='black', label='exp-001 (K=2, synthetic)'),\n    Line2D([0], [0], marker='s', color='w', markerfacecolor='gray',\n           markersize=7, markeredgecolor='black', label='exp-001 (K=4, synthetic)'),\n    Line2D([0], [0], marker='^', color='w', markerfacecolor='gray',\n           markersize=7, markeredgecolor='black', label='exp-003 (TweetEval semi-synth.)'),\n    Line2D([0], [0], marker='X', color='w', markerfacecolor='gray',\n           markersize=8, markeredgecolor='black', label='exp-013 (boundary, K=4, n=50)'),\n    Line2D([0], [0], marker='D', color='w', markerfacecolor='gray',\n           markersize=6, markeredgecolor='black', label='exp-015 (real GPT-4.1 CM)'),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#2E7D32',\n           markersize=7, markeredgecolor='black', label='HB wins (ratio < 0.95)'),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#F9A825',\n           markersize=7, markeredgecolor='black', label='Comparable (0.95–1.05)'),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#C62828',\n           markersize=7, markeredgecolor='#8B0000', label='HB worse (ratio > 1.05)'),\n]\n\nax.legend(handles=legend_elements, loc='lower right', framealpha=0.9,\n          edgecolor='#CCCCCC', ncol=2, columnspacing=1.0, handletextpad=0.5)\n\nfig.tight_layout()\n\n# Save\nfig.savefig('artifacts/figures/applicability_frontier.pdf', bbox_inches='tight')\nfig.savefig('artifacts/figures/applicability_frontier.png', bbox_inches='tight', dpi=300)\nprint('Saved to artifacts/figures/applicability_frontier.{pdf,png}')\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T13:24:51.193951+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T13:24:51.194217+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 scripts/plot_applicability_frontier.py",
  "description": "Run the plotting script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 scripts/plot_applicability_frontier.py",
    "description": "Run the plotting script"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T13:24:51.194484+00:00_

Saved to artifacts/figures/applicability_frontier.{pdf,png}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T13:24:51.194729+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la artifacts/figures/applicability_frontier.*",
  "description": "Verify output files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la artifacts/figures/applicability_frontier.*",
    "description": "Verify output files exist"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T13:24:51.195000+00:00_

-rw-r--r-- 1 ubuntu ubuntu  52171 May 21 13:23 artifacts/figures/applicability_frontier.pdf
-rw-r--r-- 1 ubuntu ubuntu 350506 May 21 13:23 artifacts/figures/applicability_frontier.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T13:24:51.195242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/figures/applicability_frontier.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/figures/applicability_frontier.png"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T13:24:51.196773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T13:24:51.197184+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
  "old_string": "# Annotate exp-013 failure\nax.annotate('exp-013: 2.1× worse\\n(boundary failure)',\n            xy=(12.5, 0.30), xytext=(8, 0.38),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))",
  "new_string": "# Annotate exp-013 failure\nax.annotate('exp-013: 2.6× worse\\nthan naive (n/K=12.5)',\n            xy=(12.5, 0.30), xytext=(8, 0.40),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
    "old_string": "# Annotate exp-013 failure\nax.annotate('exp-013: 2.1× worse\\n(boundary failure)',\n            xy=(12.5, 0.30), xytext=(8, 0.38),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))",
    "new_string": "# Annotate exp-013 failure\nax.annotate('exp-013: 2.6× worse\\nthan naive (n/K=12.5)',\n            xy=(12.5, 0.30), xytext=(8, 0.40),\n            fontsize=7, color='#C62828', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#C62828', lw=0.8))"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T13:24:51.197538+00:00_

The file /home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T13:24:51.197821+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
  "old_string": "ax.annotate(r'$n_{\\mathrm{expert}}/K = 25$' + '\\n(budget threshold)',\n            xy=(25, 0.195), fontsize=7.5, color='#333333', ha='right',\n            fontstyle='italic', va='top',\n            rotation=90)",
  "new_string": "ax.annotate(r'$n_{\\mathrm{expert}}/K = 25$',\n            xy=(25, 0.185), fontsize=7.5, color='#555555', ha='right',\n            fontstyle='italic', va='top',\n            rotation=90)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
    "old_string": "ax.annotate(r'$n_{\\mathrm{expert}}/K = 25$' + '\\n(budget threshold)',\n            xy=(25, 0.195), fontsize=7.5, color='#333333', ha='right',\n            fontstyle='italic', va='top',\n            rotation=90)",
    "new_string": "ax.annotate(r'$n_{\\mathrm{expert}}/K = 25$',\n            xy=(25, 0.185), fontsize=7.5, color='#555555', ha='right',\n            fontstyle='italic', va='top',\n            rotation=90)"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T13:24:51.198176+00:00_

The file /home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T13:24:51.198437+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
  "old_string": "ax.annotate('worst FNR = 0.5\\n(classifier quality\\n threshold)',\n            xy=(1500, 0.505), fontsize=7.5, color='#333333', ha='right',\n            va='bottom', fontstyle='italic')",
  "new_string": "ax.annotate('worst FNR = 0.5',\n            xy=(1200, 0.505), fontsize=7.5, color='#555555', ha='right',\n            va='bottom', fontstyle='italic')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
    "old_string": "ax.annotate('worst FNR = 0.5\\n(classifier quality\\n threshold)',\n            xy=(1500, 0.505), fontsize=7.5, color='#333333', ha='right',\n            va='bottom', fontstyle='italic')",
    "new_string": "ax.annotate('worst FNR = 0.5',\n            xy=(1200, 0.505), fontsize=7.5, color='#555555', ha='right',\n            va='bottom', fontstyle='italic')"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T13:24:51.198762+00:00_

The file /home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T13:24:51.199050+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
  "old_string": "ax.text(30, 0.545, 'EC-HTE\\nfails', fontsize=9, color='#B71C1C',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.6)",
  "new_string": "ax.text(600, 0.545, 'EC-HTE fails', fontsize=9, color='#B71C1C',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
    "old_string": "ax.text(30, 0.545, 'EC-HTE\\nfails', fontsize=9, color='#B71C1C',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.6)",
    "new_string": "ax.text(600, 0.545, 'EC-HTE fails', fontsize=9, color='#B71C1C',\n        ha='center', va='center', fontstyle='italic', fontweight='bold', alpha=0.6)"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T13:24:51.199372+00:00_

The file /home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T13:24:51.199665+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
  "old_string": "# Red zone: high FNR (>0.5) — always fails\nax.axhspan(0.45, 0.60, color='#FFCCCC', alpha=0.35, zorder=0)\nax.axhspan(0.32, 0.45, color='#FFF3CD', alpha=0.25, zorder=0)\n\n# Green zone approximation: low misclass + high budget\n# Fill a polygon for the \"safe\" region\ngreen_x = [80, 2000, 2000, 150]\ngreen_y = [0.18, 0.18, 0.32, 0.32]\nax.fill(green_x, green_y, color='#C8E6C9', alpha=0.35, zorder=0)\n\n# Additional green for very high budget\ngreen_x2 = [40, 80, 150, 2000, 2000, 40]\ngreen_y2 = [0.18, 0.18, 0.32, 0.32, 0.18, 0.18]",
  "new_string": "# Red zone: high FNR (>0.5) — always fails\nax.axhspan(0.45, 0.60, color='#FFCCCC', alpha=0.30, zorder=0)\n\n# Yellow/transitional zone\nyellow_x = [25, 1500, 1500, 100]\nyellow_y = [0.17, 0.17, 0.45, 0.45]\nax.fill(yellow_x, yellow_y, color='#FFF9C4', alpha=0.20, zorder=0)\n\n# Green zone: moderate misclass + high budget\ngreen_x = [50, 1500, 1500, 200]\ngreen_y = [0.17, 0.17, 0.32, 0.32]\nax.fill(green_x, green_y, color='#C8E6C9', alpha=0.35, zorder=0)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py",
    "old_string": "# Red zone: high FNR (>0.5) — always fails\nax.axhspan(0.45, 0.60, color='#FFCCCC', alpha=0.35, zorder=0)\nax.axhspan(0.32, 0.45, color='#FFF3CD', alpha=0.25, zorder=0)\n\n# Green zone approximation: low misclass + high budget\n# Fill a polygon for the \"safe\" region\ngreen_x = [80, 2000, 2000, 150]\ngreen_y = [0.18, 0.18, 0.32, 0.32]\nax.fill(green_x, green_y, color='#C8E6C9', alpha=0.35, zorder=0)\n\n# Additional green for very high budget\ngreen_x2 = [40, 80, 150, 2000, 2000, 40]\ngreen_y2 = [0.18, 0.18, 0.32, 0.32, 0.18, 0.18]",
    "new_string": "# Red zone: high FNR (>0.5) — always fails\nax.axhspan(0.45, 0.60, color='#FFCCCC', alpha=0.30, zorder=0)\n\n# Yellow/transitional zone\nyellow_x = [25, 1500, 1500, 100]\nyellow_y = [0.17, 0.17, 0.45, 0.45]\nax.fill(yellow_x, yellow_y, color='#FFF9C4', alpha=0.20, zorder=0)\n\n# Green zone: moderate misclass + high budget\ngreen_x = [50, 1500, 1500, 200]\ngreen_y = [0.17, 0.17, 0.32, 0.32]\nax.fill(green_x, green_y, color='#C8E6C9', alpha=0.35, zorder=0)"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T13:24:51.200075+00:00_

The file /home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T13:24:51.200339+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 scripts/plot_applicability_frontier.py",
  "description": "Regenerate plot with fixes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 scripts/plot_applicability_frontier.py",
    "description": "Regenerate plot with fixes"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T13:24:51.200605+00:00_

Saved to artifacts/figures/applicability_frontier.{pdf,png}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T13:24:51.200869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/figures/applicability_frontier.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/figures/applicability_frontier.png"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T13:24:51.202385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_viz_applicability-frontier_20260521T131949",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-21T13:24:51.202750+00:00_

The plot looks good. The key story is clear:

- **Green zone** (bottom-right): EC-HTE benefits when budget per subgroup is high (n/K > ~50–250) and classifier quality is decent (worst misclass < 0.30)
- **Red zone** (top-left): EC-HTE fails with poor classifiers (FNR > 0.5, exp-015) or insufficient budget (n/K = 12.5, exp-013)
- **Yellow zone**: transitional region where HB and Global are comparable

Key thresholds annotated:
- `n_expert/K = 25` vertical dashed line (budget threshold from exp-013)
- `worst FNR = 0.5` horizontal dotted line (classifier quality threshold from exp-015)
- Crossover points: K=2 at n/K ≈ 50, K=4 at n/K ≈ 250

Output saved to `artifacts/figures/applicability_frontier.{pdf,png}` (300 dpi PNG, 350 KB).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_viz_applicability-frontier_20260521T131949"
}
```

</details>

---
