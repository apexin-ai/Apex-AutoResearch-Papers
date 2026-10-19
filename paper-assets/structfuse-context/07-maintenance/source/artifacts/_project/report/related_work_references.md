# StructFuse Related Work Literature Collection

> Collected: 2026-05-16 | Total: 21 papers across 3 directions

---

## Direction 1: Code Retrieval 中的 Negative Mining 策略

### 1.1 CoCoHaNeRe (direct-competitor)

Code search framework with differentiable hard negative retrieval from a searchable memory bank. Average MRR exceeds CodeBERT/GraphCodeBERT/UniXcoder by 11.25%/8.13%/7.38%. **与 StructFuse 最直接的竞品——同样关注 code search 中 hard negative 的挖掘策略。**

```bibtex
@article{fan2025cocohanere,
  title={Effective Hard Negative Mining for Contrastive Learning-Based Code Search},
  author={Fan, Ye and Li, Chao and Ge, Jing and Huang, Liang and Luo, Bin},
  journal={ACM Transactions on Software Engineering and Methodology},
  volume={34},
  number={3},
  pages={1--35},
  year={2025},
  doi={10.1145/3695994}
}
```

### 1.2 CodeSearchNet (evaluation)

Code search benchmark with 6M functions across 6 languages and expert relevance annotations. **StructFuse 使用的评估数据集的来源基准。**

```bibtex
@article{husain2019codesearchnet,
  title={CodeSearchNet Challenge: Evaluating the State of Semantic Code Search},
  author={Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},
  journal={arXiv preprint arXiv:1909.09436},
  year={2019}
}
```

### 1.3 CodeBERT (background)

First bimodal pre-trained model for programming language and natural language, trained with replaced token detection. **Code retrieval 领域的基线模型。**

```bibtex
@inproceedings{feng2020codebert,
  title={CodeBERT: A Pre-Trained Model for Programming and Natural Languages},
  author={Feng, Zhangyin and Guo, Daya and Tang, Duyu and Duan, Nan and Feng, Xiaocheng and Gong, Ming and Shou, Linjun and Qin, Bing and Liu, Ting and Jiang, Daxin and Zhou, Ming},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2020},
  pages={1536--1547},
  year={2020}
}
```

### 1.4 GraphCodeBERT (method-component)

First pre-trained model incorporating code structure (data flow) for code representations. Uses semantic-level structure rather than AST. **展示了结构化代码表示对检索的提升，StructFuse 的 structure-aware embedding 思路的先驱。**

```bibtex
@inproceedings{guo2021graphcodebert,
  title={GraphCodeBERT: Pre-training Code Representations with Data Flow},
  author={Guo, Daya and Ren, Shuo and Lu, Shuai and Feng, Zhangyin and Tang, Duyu and Liu, Shujie and Zhou, Long and Duan, Nan and Svyatkovskiy, Alexey and Fu, Shengyu and Tufano, Michele and Deng, Shao Kun and Clement, Colin and Drain, Dawn and Sundaresan, Neel and Yin, Jian and Jiang, Daxin and Zhou, Ming},
  booktitle={International Conference on Learning Representations},
  year={2021}
}
```

### 1.5 UniXcoder (background)

Unified cross-modal pre-training leveraging AST and code comments via contrastive learning. **StructFuse 的 backbone encoder 之一，也展示了 AST 结构对代码表示的增益。**

```bibtex
@inproceedings{guo2022unixcoder,
  title={UniXcoder: Unified Cross-Modal Pre-training for Code Representation},
  author={Guo, Daya and Lu, Shuai and Duan, Nan and Wang, Yanlin and Zhou, Ming and Yin, Jian},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={7212--7225},
  year={2022}
}
```

### 1.6 CodeRetriever (direct-competitor)

Large-scale contrastive pre-training with both unimodal (code-code) and bimodal (code-text) learning for code search. **与 StructFuse 类似的 contrastive learning 框架，但没有显式的 hard negative 策略。**

```bibtex
@inproceedings{li2022coderetriever,
  title={CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search},
  author={Li, Xiaonan and Gong, Yeyun and Shen, Yelong and Qiu, Xipeng and Zhang, Hang and Yao, Bolun and Qi, Weizhen and Jiang, Daxin and Chen, Weizhu and Duan, Nan},
  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
  pages={2898--2910},
  year={2022}
}
```

### 1.7 CoCoSoDa (direct-competitor)

Contrastive code search with soft data augmentation and momentum-based negative enrichment. Exceeds CodeBERT/GraphCodeBERT/UniXcoder by 13.3%/10.5%/5.9% MRR. **在 negative sample enrichment 方面与 StructFuse 互补——CoCoSoDa 用 momentum queue 增加 negative 数量，StructFuse 关注 negative difficulty。**

```bibtex
@inproceedings{shi2023cocosoda,
  title={CoCoSoDa: Effective Contrastive Learning for Code Search},
  author={Shi, Ensheng and Wang, Yanlin and Gu, Wenchao and Du, Lun and Zhang, Hongyu and Han, Shi and Zhang, Dongmei and Sun, Hongbin},
  booktitle={2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE)},
  pages={2198--2210},
  year={2023}
}
```

---

## Direction 2: Contrastive Learning 中 Hard Negative 的 Overfitting 问题

### 2.1 CPC / InfoNCE (background)

Introduces InfoNCE loss: contrastive predictive coding for unsupervised representation learning. **Contrastive learning 的基础损失函数，StructFuse 训练目标的理论根基。**

```bibtex
@article{oord2018representation,
  title={Representation Learning with Contrastive Predictive Coding},
  author={van den Oord, Aaron and Li, Yazhe and Vinyals, Oriol},
  journal={arXiv preprint arXiv:1807.03748},
  year={2018}
}
```

### 2.2 HCL (method-component)

Develops controllable hard negative sampling for contrastive learning, showing harder negatives accelerate and improve learning. **理论上证明了 hard negative 的价值，但也暗示了过度 hard 会导致问题——StructFuse difficulty analysis 的理论起点。**

```bibtex
@inproceedings{robinson2021contrastive,
  title={Contrastive Learning with Hard Negative Samples},
  author={Robinson, Joshua David and Chuang, Ching-Yao and Sra, Suvrit and Jegelka, Stefanie},
  booktitle={International Conference on Learning Representations},
  year={2021}
}
```

### 2.3 DCL (method-component)

Debiased contrastive objective correcting for false negatives (same-class samples treated as negatives). **False negative 是 hard negative 过拟合的重要来源之一，DCL 提供了理论框架。**

```bibtex
@inproceedings{chuang2020debiased,
  title={Debiased Contrastive Learning},
  author={Chuang, Ching-Yao and Robinson, Joshua and Lin, Yen-Chen and Torralba, Antonio and Jegelka, Stefanie},
  booktitle={Advances in Neural Information Processing Systems},
  volume={33},
  pages={8765--8775},
  year={2020}
}
```

### 2.4 MoCHi (method-component)

Hard negative mixing at feature level with minimal overhead; shows harder negatives facilitate faster learning. **Feature-level hard negative 合成方法，与 StructFuse 的 structure-based negative mining 形成对比。**

```bibtex
@inproceedings{kalantidis2020hard,
  title={Hard Negative Mixing for Contrastive Learning},
  author={Kalantidis, Yannis and Sariyildiz, Mert Bulent and Pion, No{\'e} and Weinzaepfel, Philippe and Larlus, Diane},
  booktitle={Advances in Neural Information Processing Systems},
  volume={33},
  pages={21798--21809},
  year={2020}
}
```

### 2.5 Understanding Hard Negatives in NCE (background)

Theoretical analysis: using model distribution as negative distribution reduces gradient bias. **为 hard negative 的作用提供了理论解释——StructFuse 的 difficulty-overfitting 分析可引用此理论框架。**

```bibtex
@inproceedings{zhang2021understanding,
  title={Understanding Hard Negatives in Noise Contrastive Estimation},
  author={Zhang, Wenzheng and Stratos, Karl},
  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages={1090--1101},
  year={2021}
}
```

### 2.6 ProGCL (method-component)

Shows hard negatives in graph CL are often false negatives; proposes probability-based hardness that accounts for true/false negative distinction. **揭示了 hard negative = false negative 的陷阱，与 StructFuse 发现的 difficulty-overfitting 现象呼应。**

```bibtex
@inproceedings{xia2022progcl,
  title={ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning},
  author={Xia, Jun and Wu, Lirong and Wang, Ge and Chen, Jintao and Li, Stan Z.},
  booktitle={Proceedings of the 39th International Conference on Machine Learning},
  pages={24332--24346},
  year={2022}
}
```

### 2.7 WCL (method-component)

Difficulty-based sampling exploiting a bias-amplifying encoder to find informative hard negatives while avoiding false negatives. **用 difficulty 分层采样来 debias，与 StructFuse 的 difficulty stratification 思路最接近。**

```bibtex
@inproceedings{jang2023difficulty,
  title={Difficulty-Based Sampling for Debiased Contrastive Representation Learning},
  author={Jang, Taeuk and Wang, Xiaoqian},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={24039--24048},
  year={2023}
}
```

---

## Direction 3: Representation Geometry / Similarity Saturation

### 3.1 SimCLR (background)

Simple contrastive framework showing the importance of data augmentation, projection head, and batch size. **Contrastive learning 的经典方法论，StructFuse 实验设计的参考。**

```bibtex
@inproceedings{chen2020simple,
  title={A Simple Framework for Contrastive Learning of Visual Representations},
  author={Chen, Ting and Kornblith, Simon and Norouzi, Mohammad and Hinton, Geoffrey},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={1597--1607},
  year={2020}
}
```

### 3.2 Alignment & Uniformity (method-component)

Identifies two key properties of contrastive loss: alignment of positive pairs and uniformity on hypersphere; proves contrastive loss optimizes both asymptotically. **StructFuse 分析 embedding space 质量的理论工具——可用 alignment/uniformity 指标量化 structure-aware embedding 的改进。**

```bibtex
@inproceedings{wang2020understanding,
  title={Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere},
  author={Wang, Tongzhou and Isola, Phillip},
  booktitle={Proceedings of the 37th International Conference on Machine Learning},
  pages={9929--9939},
  year={2020}
}
```

### 3.3 Representation Degeneration (background)

Shows pre-trained LM embeddings degenerate into a narrow cone, limiting representation power; proposes regularization. **Embedding 退化的理论根源——StructFuse 观察到的 similarity saturation 可追溯到此现象。**

```bibtex
@inproceedings{gao2019representation,
  title={Representation Degeneration Problem in Training Natural Language Generation Models},
  author={Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
  booktitle={International Conference on Learning Representations},
  year={2019}
}
```

### 3.4 Anisotropy of Contextualized Representations (background)

Discovers that BERT/ELMo/GPT-2 representations occupy a narrow cone (anisotropy) across all layers. **实证发现 pre-trained model 的各向异性问题，StructFuse 使用的 code encoder 继承了此问题。**

```bibtex
@inproceedings{ethayarajh2019contextual,
  title={How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings},
  author={Ethayarajh, Kawin},
  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
  pages={55--65},
  year={2019}
}
```

### 3.5 BERT-flow (method-component)

Shows BERT sentence embeddings are anisotropic; proposes normalizing flows to transform to isotropic Gaussian. **Anisotropy 矫正方法的代表，与 StructFuse 的 whitening/normalization 策略形成对比。**

```bibtex
@inproceedings{li2020sentence,
  title={On the Sentence Embeddings from Pre-trained Language Models},
  author={Li, Bohan and Zhou, Hao and He, Junxian and Wang, Mingxuan and Yang, Yiming and Li, Lei},
  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
  pages={9119--9130},
  year={2020}
}
```

### 3.6 SimCSE (method-component)

Contrastive learning regularizes anisotropic embedding space to be more uniform; uses dropout as minimal augmentation. Spectral analysis shows contrastive loss flattens singular spectrum. **直接证明 contrastive learning 改善 anisotropy——StructFuse 可引用其 uniformity 分析框架。**

```bibtex
@inproceedings{gao2021simcse,
  title={SimCSE: Simple Contrastive Learning of Sentence Embeddings},
  author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},
  booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
  pages={6894--6910},
  year={2021}
}
```

### 3.7 Whitening for Sentence Representations (method-component)

Whitening operation enhances isotropy and reduces dimensionality of sentence representations. **针对 anisotropy 的简洁解法，与 StructFuse 中 embedding post-processing 的讨论相关。**

```bibtex
@article{su2021whitening,
  title={Whitening Sentence Representations for Better Semantics and Faster Retrieval},
  author={Su, Jianlin and Cao, Jiarun and Liu, Weijie and Ou, Yangyiwen},
  journal={arXiv preprint arXiv:2103.15316},
  year={2021}
}
```

---

## Summary

| Direction | Papers | Key insight for StructFuse |
|-----------|--------|---------------------------|
| 1. Code retrieval negative mining | 7 | StructFuse fills the gap between structure-aware encoding (GraphCodeBERT) and hard negative mining (CoCoHaNeRe) by using structural similarity for difficulty-aware negative selection |
| 2. Hard negative overfitting | 7 | Existing work (HCL, DCL, ProGCL, WCL) shows hard negatives help but can cause overfitting/false-negative problems; StructFuse's difficulty stratification addresses this in code domain |
| 3. Representation geometry | 7 | Pre-trained code encoders inherit anisotropy (Ethayarajh, Gao 2019); contrastive learning improves uniformity (SimCSE, Wang & Isola) but similarity saturation in high-similarity regions remains; StructFuse's structure-aware negatives target this specific region |
