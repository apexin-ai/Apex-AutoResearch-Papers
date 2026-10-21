# ssh rsa analysis — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ssh-rsa-analysis.md) · [Structured JSON](../../../sessions/db/dbacf507c9c8a77ba71f.json)

## Before a recorded user message

### Tool result

_source line 389 · 2026-05-15T20:04:23.270Z_

<details><summary>↩ Tool result · `toolu_01Y9ufiKUSUnc2k8dpkNcToy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Config: 10 tasks x 10 demos = 100 trajectories\\nLayers: 33 | CKA: yes\\n\\nLoading actions...\\n  Loaded 100 demos\\nLoading DINO features...\\n  Loaded 100 DINO demos\\n  Common demos: 100\\nPrecomputing ADM and DINO RDM (vectorized)...\\n  Done\\n  Layer  0/32: trained=0.0000  untrained=0.0000  dino=0.3880  [10.8s]\\n  Layer  1/32: trained=0.4117  untrained=0.4641  dino=0.3880  [22.4s]\\n  Layer  2/32: trained=0.4725  untrained=0.4659  dino=0.3880  [15.3s]\\n  Layer  3/32: trained=0.4653  untrained=0.4802  dino=0.3880  [7.4s]\\n  Layer  4/32: trained=0.4599  untrained=0.4751  dino=0.3880  [10.7s]\\n  Layer  5/32: trained=0.4632  untrained=0.4783  dino=0.3880  [18.9s]\\n  Layer  6/32: trained=0.4863  untrained=0.4754  dino=0.3880  [17.6s]\\n  Layer  7/32: trained=0.4534  untrained=0.4790  dino=0.3880  [14.1s]\\n  Layer  8/32: trained=0.4509  untrained=0.4781  dino=0.3880  [10.4s]\\n  Layer  9/32: trained=0.4876  untrained=0.4798  dino=0.3880  [9.9s]\\n  Layer 10/32: trained=0.4647  untrained=0.4831  dino=0.3880  [23.0s]\\n  Layer 11/32: trained=0.4118  untrained=0.4840  dino=0.3880  [15.5s]\\n  Layer 12/32: trained=0.4418  untrained=0.4846  dino=0.3880  [23.8s]\\n  Layer 13/32: trained=0.4677  untrained=0.4844  dino=0.3880  [10.9s]\\n  Layer 14/32: trained=0.4721  untrained=0.4845  dino=0.3880  [13.6s]\\n  Layer 15/32: trained=0.4730  untrained=0.4841  dino=0.3880  [31.6s]\\n  Layer 16/32: trained=0.4637  untrained=0.4845  dino=0.3880  [17.1s]\\n  Layer 17/32: trained=0.4654  untrained=0.4834  dino=0.3880  [11.5s]\\n  Layer 18/32: trained=0.4579  untrained=0.4819  dino=0.3880  [13.7s]\\n  Layer 19/32: trained=0.4569  untrained=0.4843  dino=0.3880  [21.2s]\\n  Layer 20/32: trained=0.4533  untrained=0.4838  dino=0.3880  [29.3s]\\n  Layer 21/32: trained=0.4537  untrained=0.4834  dino=0.3880  [11.9s]\\n  Layer 22/32: trained=0.4409  untrained=0.4825  dino=0.3880  [13.4s]\\n  Layer 23/32: trained=0.4362  untrained=0.4824  dino=0.3880  [25.1s]\\n  Layer 24/32: trained=0.4263  untrained=0.4829  dino=0.3880  [16.0s]\\n  Layer 25/32: trained=0.4319  untrained=0.4837  dino=0.3880  [20.8s]\\n  Layer 26/32: trained=0.4417  untrained=0.4820  dino=0.3880  [17.7s]\\n  Layer 27/32: trained=0.4359  untrained=0.4822  dino=0.3880  [10.5s]\\n  Layer 28/32: trained=0.4137  untrained=0.4810  dino=0.3880  [16.1s]\\n  Layer 29/32: trained=0.4415  untrained=0.4830  dino=0.3880  [22.2s]\\n  Layer 30/32: trained=0.4550  untrained=0.4812  dino=0.3880  [25.0s]\\n  Layer 31/32: trained=0.4626  untrained=0.4817  dino=0.3880  [11.5s]\\n  Layer 32/32: trained=0.4855  untrained=0.4822  dino=0.3880  [7.8s]\\n\\nResults saved to /root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json\\n\\n================================================================================\\nRSA SUMMARY (Spearman corr between representation & action dissimilarity)\\n================================================================================\\n\\n   Layer |    Trained |  Untrained |       DINO |  T-U Delta |   CKA(T,U)\\n--------------------------------------------------------------------\\n       0 |     0.0000 |     0.0000 |     0.3880 |    +0.0000 |     0.0000\\n       1 |     0.4117 |     0.4641 |     0.3880 |    -0.0524 |     0.6869\\n       2 |     0.4725 |     0.4659 |     0.3880 |    +0.0066 |     0.7563\\n       3 |     0.4653 |     0.4802 |     0.3880 |    -0.0149 |     0.7251\\n       4 |     0.4599 |     0.4751 |     0.3880 |    -0.0152 |     0.6990\\n       5 |     0.4632 |     0.4783 |     0.3880 |    -0.0151 |     0.6968\\n       6 |     0.4863 |     0.4754 |     0.3880 |    +0.0109 |     0.7310\\n       7 |     0.4534 |     0.4790 |     0.3880 |    -0.0256 |     0.7959\\n       8 |     0.4509 |     0.4781 |     0.3880 |    -0.0272 |     0.8237\\n       9 |     0.4876 |     0.4798 |     0.3880 |    +0.0078 |     0.8095\\n      10 |     0.4647 |     0.4831 |     0.3880 |    -0.0184 |     0.8177\\n      11 |     0.4118 |     0.4840 |     0.3880 |    -0.0722 |     0.8082\\n      12 |     0.4418 |     0.4846 |     0.3880 |    -0.0428 |     0.8448\\n      13 |     0.4677 |     0.4844 |     0.3880 |    -0.0167 |     0.8536\\n      14 |     0.4721 |     0.4845 |     0.3880 |    -0.0124 |     0.8466\\n      15 |     0.4730 |     0.4841 |     0.3880 |    -0.0111 |     0.8445\\n      16 |     0.4637 |     0.4845 |     0.3880 |    -0.0208 |     0.8457\\n      17 |     0.4654 |     0.4834 |     0.3880 |    -0.0180 |     0.8473\\n      18 |     0.4579 |     0.4819 |     0.3880 |    -0.0240 |     0.8472\\n      19 |     0.4569 |     0.4843 |     0.3880 |    -0.0274 |     0.8503\\n      20 |     0.4533 |     0.4838 |     0.3880 |    -0.0305 |     0.8515\\n      21 |     0.4537 |     0.4834 |     0.3880 |    -0.0297 |     0.8520\\n      22 |     0.4409 |     0.4825 |     0.3880 |    -0.0416 |     0.8521\\n      23 |     0.4362 |     0.4824 |     0.3880 |    -0.0462 |     0.8533\\n      24 |     0.4263 |     0.4829 |     0.3880 |    -0.0566 |     0.8538\\n      25 |     0.4319 |     0.4837 |     0.3880 |    -0.0518 |     0.8555\\n      26 |     0.4417 |     0.4820 |     0.3880 |    -0.0403 |     0.8595\\n      27 |     0.4359 |     0.4822 |     0.3880 |    -0.0463 |     0.8585\\n      28 |     0.4137 |     0.4810 |     0.3880 |    -0.0673 |     0.8545\\n      29 |     0.4415 |     0.4830 |     0.3880 |    -0.0415 |     0.8550\\n      30 |     0.4550 |     0.4812 |     0.3880 |    -0.0262 |     0.8565\\n      31 |     0.4626 |     0.4817 |     0.3880 |    -0.0191 |     0.8555\\n      32 |     0.4855 |     0.4822 |     0.3880 |    +0.0033 |     0.8443\\n\\n   Phase |    Trained |  Untrained |       DINO\\n------------------------------------------------\\n   early |     0.3197 |     0.4148 |     0.4909\\n     mid |     0.5231 |     0.5248 |     0.4132\\n    late |     0.4758 |     0.4592 |     0.2601\\n\\nGates:\\n  G1: peak RSA trained=0.4876 vs untrained=0.4846  delta=+0.0030  FAIL\\n  G2: trained > untrained in 4/33 layers  FAIL\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ec23db3-8ea9-4538-878d-9488493f5f05",
  "uuid": "0f7b116e-0b62-4d9c-8db6-c2227bdb47e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Config: 10 tasks x 10 demos = 100 trajectories\\\\nLayers: 33 | CKA: yes\\\\n\\\\nLoading actions...\\\\n  Loaded 100 demos\\\\nLoading DINO features...\\\\n  Loaded 100 DINO demos\\\\n  Common demos: 100\\\\nPrecomputing ADM and DINO RDM (vectorized)...\\\\n  Done\\\\n  Layer  0/32: trained=0.0000  untrained=0.0000  dino=0.3880  [10.8s]\\\\n  Layer  1/32: trained=0.4117  untrained=0.4641  dino=0.3880  [22.4s]\\\\n  Layer  2/32: trained=0.4725  untrained=0.4659  dino=0.3880  [15.3s]\\\\n  Layer  3/32: trained=0.4653  untrained=0.4802  dino=0.3880  [7.4s]\\\\n  Layer  4/32: trained=0.4599  untrained=0.4751  dino=0.3880  [10.7s]\\\\n  Layer  5/32: trained=0.4632  untrained=0.4783  dino=0.3880  [18.9s]\\\\n  Layer  6/32: trained=0.4863  untrained=0.4754  dino=0.3880  [17.6s]\\\\n  Layer  7/32: trained=0.4534  untrained=0.4790  dino=0.3880  [14.1s]\\\\n  Layer  8/32: trained=0.4509  untrained=0.4781  dino=0.3880  [10.4s]\\\\n  Layer  9/32: trained=0.4876  untrained=0.4798  dino=0.3880  [9.9s]\\\\n  Layer 10/32: trained=0.4647  untrained=0.4831  dino=0.3880  [23.0s]\\\\n  Layer 11/32: trained=0.4118  untrained=0.4840  dino=0.3880  [15.5s]\\\\n  Layer 12/32: trained=0.4418  untrained=0.4846  dino=0.3880  [23.8s]\\\\n  Layer 13/32: trained=0.4677  untrained=0.4844  dino=0.3880  [10.9s]\\\\n  Layer 14/32: trained=0.4721  untrained=0.4845  dino=0.3880  [13.6s]\\\\n  Layer 15/32: trained=0.4730  untrained=0.4841  dino=0.3880  [31.6s]\\\\n  Layer 16/32: trained=0.4637  untrained=0.4845  dino=0.3880  [17.1s]\\\\n  Layer 17/32: trained=0.4654  untrained=0.4834  dino=0.3880  [11.5s]\\\\n  Layer 18/32: trained=0.4579  untrained=0.4819  dino=0.3880  [13.7s]\\\\n  Layer 19/32: trained=0.4569  untrained=0.4843  dino=0.3880  [21.2s]\\\\n  Layer 20/32: trained=0.4533  untrained=0.4838  dino=0.3880  [29.3s]\\\\n  Layer 21/32: trained=0.4537  untrained=0.4834  dino=0.3880  [11.9s]\\\\n  Layer 22/32: trained=0.4409  untrained=0.4825  dino=0.3880  [13.4s]\\\\n  Layer 23/32: trained=0.4362  untrained=0.4824  dino=0.3880  [25.1s]\\\\n  Layer 24/32: trained=0.4263  untrained=0.4829  dino=0.3880  [16.0s]\\\\n  Layer 25/32: trained=0.4319  untrained=0.4837  dino=0.3880  [20.8s]\\\\n  Layer 26/32: trained=0.4417  untrained=0.4820  dino=0.3880  [17.7s]\\\\n  Layer 27/32: trained=0.4359  untrained=0.4822  dino=0.3880  [10.5s]\\\\n  Layer 28/32: trained=0.4137  untrained=0.4810  dino=0.3880  [16.1s]\\\\n  Layer 29/32: trained=0.4415  untrained=0.4830  dino=0.3880  [22.2s]\\\\n  Layer 30/32: trained=0.4550  untrained=0.4812  dino=0.3880  [25.0s]\\\\n  Layer 31/32: trained=0.4626  untrained=0.4817  dino=0.3880  [11.5s]\\\\n  Layer 32/32: trained=0.4855  untrained=0.4822  dino=0.3880  [7.8s]\\\\n\\\\nResults saved to /root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json\\\\n\\\\n================================================================================\\\\nRSA SUMMARY (Spearman corr between representation & action dissimilarity)\\\\n================================================================================\\\\n\\\\n   Layer |    Trained |  Untrained |       DINO |  T-U Delta |   CKA(T,U)\\\\n--------------------------------------------------------------------\\\\n       0 |     0.0000 |     0.0000 |     0.3880 |    +0.0000 |     0.0000\\\\n       1 |     0.4117 |     0.4641 |     0.3880 |    -0.0524 |     0.6869\\\\n       2 |     0.4725 |     0.4659 |     0.3880 |    +0.0066 |     0.7563\\\\n       3 |     0.4653 |     0.4802 |     0.3880 |    -0.0149 |     0.7251\\\\n       4 |     0.4599 |     0.4751 |     0.3880 |    -0.0152 |     0.6990\\\\n       5 |     0.4632 |     0.4783 |     0.3880 |    -0.0151 |     0.6968\\\\n       6 |     0.4863 |     0.4754 |     0.3880 |    +0.0109 |     0.7310\\\\n       7 |     0.4534 |     0.4790 |     0.3880 |    -0.0256 |     0.7959\\\\n       8 |     0.4509 |     0.4781 |     0.3880 |    -0.0272 |     0.8237\\\\n       9 |     0.4876 |     0.4798 |     0.3880 |    +0.0078 |     0.8095\\\\n      10 |     0.4647 |     0.4831 |     0.3880 |    -0.0184 |     0.8177\\\\n      11 |     0.4118 |     0.4840 |     0.3880 |    -0.0722 |     0.8082\\\\n      12 |     0.4418 |     0.4846 |     0.3880 |    -0.0428 |     0.8448\\\\n      13 |     0.4677 |     0.4844 |     0.3880 |    -0.0167 |     0.8536\\\\n      14 |     0.4721 |     0.4845 |     0.3880 |    -0.0124 |     0.8466\\\\n      15 |     0.4730 |     0.4841 |     0.3880 |    -0.0111 |     0.8445\\\\n      16 |     0.4637 |     0.4845 |     0.3880 |    -0.0208 |     0.8457\\\\n      17 |     0.4654 |     0.4834 |     0.3880 |    -0.0180 |     0.8473\\\\n      18 |     0.4579 |     0.4819 |     0.3880 |    -0.0240 |     0.8472\\\\n      19 |     0.4569 |     0.4843 |     0.3880 |    -0.0274 |     0.8503\\\\n      20 |     0.4533 |     0.4838 |     0.3880 |    -0.0305 |     0.8515\\\\n      21 |     0.4537 |     0.4834 |     0.3880 |    -0.0297 |     0.8520\\\\n      22 |     0.4409 |     0.4825 |     0.3880 |    -0.0416 |     0.8521\\\\n      23 |     0.4362 |     0.4824 |     0.3880 |    -0.0462 |     0.8533\\\\n      24 |     0.4263 |     0.4829 |     0.3880 |    -0.0566 |     0.8538\\\\n      25 |     0.4319 |     0.4837 |     0.3880 |    -0.0518 |     0.8555\\\\n      26 |     0.4417 |     0.4820 |     0.3880 |    -0.0403 |     0.8595\\\\n      27 |     0.4359 |     0.4822 |     0.3880 |    -0.0463 |     0.8585\\\\n      28 |     0.4137 |     0.4810 |     0.3880 |    -0.0673 |     0.8545\\\\n      29 |     0.4415 |     0.4830 |     0.3880 |    -0.0415 |     0.8550\\\\n      30 |     0.4550 |     0.4812 |     0.3880 |    -0.0262 |     0.8565\\\\n      31 |     0.4626 |     0.4817 |     0.3880 |    -0.0191 |     0.8555\\\\n      32 |     0.4855 |     0.4822 |     0.3880 |    +0.0033 |     0.8443\\\\n\\\\n   Phase |    Trained |  Untrained |       DINO\\\\n------------------------------------------------\\\\n   early |     0.3197 |     0.4148 |     0.4909\\\\n     mid |     0.5231 |     0.5248 |     0.4132\\\\n    late |     0.4758 |     0.4592 |     0.2601\\\\n\\\\nGates:\\\\n  G1: peak RSA trained=0.4876 vs untrained=0.4846  delta=+0.0030  FAIL\\\\n  G2: trained > untrained in 4/33 layers  FAIL\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Config: 10 tasks x 10 demos = 100 trajectories\\nLayers: 33 | CKA: yes\\n\\nLoading actions...\\n  Loaded 100 demos\\nLoading DINO features...\\n  Loaded 100 DINO demos\\n  Common demos: 100\\nPrecomputing ADM and DINO RDM (vectorized)...\\n  Done\\n  Layer  0/32: trained=0.0000  untrained=0.0000  dino=0.3880  [10.8s]\\n  Layer  1/32: trained=0.4117  untrained=0.4641  dino=0.3880  [22.4s]\\n  Layer  2/32: trained=0.4725  untrained=0.4659  dino=0.3880  [15.3s]\\n  Layer  3/32: trained=0.4653  untrained=0.4802  dino=0.3880  [7.4s]\\n  Layer  4/32: trained=0.4599  untrained=0.4751  dino=0.3880  [10.7s]\\n  Layer  5/32: trained=0.4632  untrained=0.4783  dino=0.3880  [18.9s]\\n  Layer  6/32: trained=0.4863  untrained=0.4754  dino=0.3880  [17.6s]\\n  Layer  7/32: trained=0.4534  untrained=0.4790  dino=0.3880  [14.1s]\\n  Layer  8/32: trained=0.4509  untrained=0.4781  dino=0.3880  [10.4s]\\n  Layer  9/32: trained=0.4876  untrained=0.4798  dino=0.3880  [9.9s]\\n  Layer 10/32: trained=0.4647  untrained=0.4831  dino=0.3880  [23.0s]\\n  Layer 11/32: trained=0.4118  untrained=0.4840  dino=0.3880  [15.5s]\\n  Layer 12/32: trained=0.4418  untrained=0.4846  dino=0.3880  [23.8s]\\n  Layer 13/32: trained=0.4677  untrained=0.4844  dino=0.3880  [10.9s]\\n  Layer 14/32: trained=0.4721  untrained=0.4845  dino=0.3880  [13.6s]\\n  Layer 15/32: trained=0.4730  untrained=0.4841  dino=0.3880  [31.6s]\\n  Layer 16/32: trained=0.4637  untrained=0.4845  dino=0.3880  [17.1s]\\n  Layer 17/32: trained=0.4654  untrained=0.4834  dino=0.3880  [11.5s]\\n  Layer 18/32: trained=0.4579  untrained=0.4819  dino=0.3880  [13.7s]\\n  Layer 19/32: trained=0.4569  untrained=0.4843  dino=0.3880  [21.2s]\\n  Layer 20/32: trained=0.4533  untrained=0.4838  dino=0.3880  [29.3s]\\n  Layer 21/32: trained=0.4537  untrained=0.4834  dino=0.3880  [11.9s]\\n  Layer 22/32: trained=0.4409  untrained=0.4825  dino=0.3880  [13.4s]\\n  Layer 23/32: trained=0.4362  untrained=0.4824  dino=0.3880  [25.1s]\\n  Layer 24/32: trained=0.4263  untrained=0.4829  dino=0.3880  [16.0s]\\n  Layer 25/32: trained=0.4319  untrained=0.4837  dino=0.3880  [20.8s]\\n  Layer 26/32: trained=0.4417  untrained=0.4820  dino=0.3880  [17.7s]\\n  Layer 27/32: trained=0.4359  untrained=0.4822  dino=0.3880  [10.5s]\\n  Layer 28/32: trained=0.4137  untrained=0.4810  dino=0.3880  [16.1s]\\n  Layer 29/32: trained=0.4415  untrained=0.4830  dino=0.3880  [22.2s]\\n  Layer 30/32: trained=0.4550  untrained=0.4812  dino=0.3880  [25.0s]\\n  Layer 31/32: trained=0.4626  untrained=0.4817  dino=0.3880  [11.5s]\\n  Layer 32/32: trained=0.4855  untrained=0.4822  dino=0.3880  [7.8s]\\n\\nResults saved to /root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json\\n\\n================================================================================\\nRSA SUMMARY (Spearman corr between representation & action dissimilarity)\\n================================================================================\\n\\n   Layer |    Trained |  Untrained |       DINO |  T-U Delta |   CKA(T,U)\\n--------------------------------------------------------------------\\n       0 |     0.0000 |     0.0000 |     0.3880 |    +0.0000 |     0.0000\\n       1 |     0.4117 |     0.4641 |     0.3880 |    -0.0524 |     0.6869\\n       2 |     0.4725 |     0.4659 |     0.3880 |    +0.0066 |     0.7563\\n       3 |     0.4653 |     0.4802 |     0.3880 |    -0.0149 |     0.7251\\n       4 |     0.4599 |     0.4751 |     0.3880 |    -0.0152 |     0.6990\\n       5 |     0.4632 |     0.4783 |     0.3880 |    -0.0151 |     0.6968\\n       6 |     0.4863 |     0.4754 |     0.3880 |    +0.0109 |     0.7310\\n       7 |     0.4534 |     0.4790 |     0.3880 |    -0.0256 |     0.7959\\n       8 |     0.4509 |     0.4781 |     0.3880 |    -0.0272 |     0.8237\\n       9 |     0.4876 |     0.4798 |     0.3880 |    +0.0078 |     0.8095\\n      10 |     0.4647 |     0.4831 |     0.3880 |    -0.0184 |     0.8177\\n      11 |     0.4118 |     0.4840 |     0.3880 |    -0.0722 |     0.8082\\n      12 |     0.4418 |     0.4846 |     0.3880 |    -0.0428 |     0.8448\\n      13 |     0.4677 |     0.4844 |     0.3880 |    -0.0167 |     0.8536\\n      14 |     0.4721 |     0.4845 |     0.3880 |    -0.0124 |     0.8466\\n      15 |     0.4730 |     0.4841 |     0.3880 |    -0.0111 |     0.8445\\n      16 |     0.4637 |     0.4845 |     0.3880 |    -0.0208 |     0.8457\\n      17 |     0.4654 |     0.4834 |     0.3880 |    -0.0180 |     0.8473\\n      18 |     0.4579 |     0.4819 |     0.3880 |    -0.0240 |     0.8472\\n      19 |     0.4569 |     0.4843 |     0.3880 |    -0.0274 |     0.8503\\n      20 |     0.4533 |     0.4838 |     0.3880 |    -0.0305 |     0.8515\\n      21 |     0.4537 |     0.4834 |     0.3880 |    -0.0297 |     0.8520\\n      22 |     0.4409 |     0.4825 |     0.3880 |    -0.0416 |     0.8521\\n      23 |     0.4362 |     0.4824 |     0.3880 |    -0.0462 |     0.8533\\n      24 |     0.4263 |     0.4829 |     0.3880 |    -0.0566 |     0.8538\\n      25 |     0.4319 |     0.4837 |     0.3880 |    -0.0518 |     0.8555\\n      26 |     0.4417 |     0.4820 |     0.3880 |    -0.0403 |     0.8595\\n      27 |     0.4359 |     0.4822 |     0.3880 |    -0.0463 |     0.8585\\n      28 |     0.4137 |     0.4810 |     0.3880 |    -0.0673 |     0.8545\\n      29 |     0.4415 |     0.4830 |     0.3880 |    -0.0415 |     0.8550\\n      30 |     0.4550 |     0.4812 |     0.3880 |    -0.0262 |     0.8565\\n      31 |     0.4626 |     0.4817 |     0.3880 |    -0.0191 |     0.8555\\n      32 |     0.4855 |     0.4822 |     0.3880 |    +0.0033 |     0.8443\\n\\n   Phase |    Trained |  Untrained |       DINO\\n------------------------------------------------\\n   early |     0.3197 |     0.4148 |     0.4909\\n     mid |     0.5231 |     0.5248 |     0.4132\\n    late |     0.4758 |     0.4592 |     0.2601\\n\\nGates:\\n  G1: peak RSA trained=0.4876 vs untrained=0.4846  delta=+0.0030  FAIL\\n  G2: trained > untrained in 4/33 layers  FAIL\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 390_

全量运行完成。结果已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json`。

## RSA 结果摘要

### Per-layer RSA (Spearman corr: representation dissimilarity vs action dissimilarity)

| 趋势 | 数值 |
|------|------|
| Trained peak RSA | 0.4876 (layer 9) |
| Untrained peak RSA | 0.4846 (layer 12) |
| DINO RSA (constant) | 0.3880 |
| Trained > Untrained | 仅 4/33 层 (layers 2, 6, 9, 32) |
| T-U Delta 范围 | -0.0722 ~ +0.0109 |

### Per-phase RSA (均值跨层)

| Phase | Trained | Untrained | DINO |
|-------|---------|-----------|------|
| early | 0.3197 | **0.4148** | 0.4909 |
| mid | 0.5231 | **0.5248** | 0.4132 |
| late | **0.4758** | 0.4592 | 0.2601 |

### CKA (Trained vs Untrained)
CKA 从 layer 1 的 0.687 持续上升到 layer 26 的 0.860，表明 trained 和 untrained 的表征在深层高度相似。

### Gates
- **G1 FAIL**: peak delta = +0.003 (阈值 0.05)
- **G2 FAIL**: trained > untrained 仅 4/33 层

### 关键发现
1. **VLA training 并未改善 action-relevant 表征结构**——在绝大多数层中 untrained RSA 反而略高于 trained。
2. **Untrained VLA 的 RSA 非常稳定**（~0.48 跨所有层），而 trained VLA 的 RSA 在深层（20-28）明显下降（~0.41-0.44），提示 training 可能引入了 action 无关的变异。
3. **Temporal phase 差异**：trained 在 late phase 优于 untrained（0.4758 vs 0.4592），但在 early phase 远逊（0.3197 vs 0.4148）。
4. **DINO 在 early phase 最强**（0.4909），在 late phase 最弱（0.2601），与 VLA 互补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ec23db3-8ea9-4538-878d-9488493f5f05",
  "uuid": "b4634571-bae4-4197-979d-65991a8271f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mc2pgtXqEkfFcTqdQQUpDq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3121,
      "cache_read_input_tokens": 121503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3121
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 391_

全量运行完成。结果已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json`。

## RSA 结果摘要

### Per-layer RSA (Spearman corr: representation dissimilarity vs action dissimilarity)

| 趋势 | 数值 |
|------|------|
| Trained peak RSA | 0.4876 (layer 9) |
| Untrained peak RSA | 0.4846 (layer 12) |
| DINO RSA (constant) | 0.3880 |
| Trained > Untrained | 仅 4/33 层 (layers 2, 6, 9, 32) |
| T-U Delta 范围 | -0.0722 ~ +0.0109 |

### Per-phase RSA (均值跨层)

| Phase | Trained | Untrained | DINO |
|-------|---------|-----------|------|
| early | 0.3197 | **0.4148** | 0.4909 |
| mid | 0.5231 | **0.5248** | 0.4132 |
| late | **0.4758** | 0.4592 | 0.2601 |

### CKA (Trained vs Untrained)
CKA 从 layer 1 的 0.687 持续上升到 layer 26 的 0.860，表明 trained 和 untrained 的表征在深层高度相似。

### Gates
- **G1 FAIL**: peak delta = +0.003 (阈值 0.05)
- **G2 FAIL**: trained > untrained 仅 4/33 层

### 关键发现
1. **VLA training 并未改善 action-relevant 表征结构**——在绝大多数层中 untrained RSA 反而略高于 trained。
2. **Untrained VLA 的 RSA 非常稳定**（~0.48 跨所有层），而 trained VLA 的 RSA 在深层（20-28）明显下降（~0.41-0.44），提示 training 可能引入了 action 无关的变异。
3. **Temporal phase 差异**：trained 在 late phase 优于 untrained（0.4758 vs 0.4592），但在 early phase 远逊（0.3197 vs 0.4148）。
4. **DINO 在 early phase 最强**（0.4909），在 late phase 最弱（0.2601），与 VLA 互补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1083273,
  "duration_api_ms": 941517,
  "num_turns": 171,
  "stop_reason": "end_turn",
  "session_id": "9ec23db3-8ea9-4538-878d-9488493f5f05",
  "total_cost_usd": 9.28750725,
  "usage": {
    "input_tokens": 168,
    "cache_creation_input_tokens": 112783,
    "cache_read_input_tokens": 14940473,
    "output_tokens": 44351,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112783,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 689,
        "cache_read_input_tokens": 121503,
        "cache_creation_input_tokens": 3121,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3121
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2672,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0027619999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 168,
      "outputTokens": 44351,
      "cacheReadInputTokens": 14940473,
      "cacheCreationInputTokens": 112783,
      "webSearchRequests": 0,
      "costUSD": 9.28474525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f580321f-9f2c-4772-a78f-ba1ed2d2cda8"
}
```

</details>

---
