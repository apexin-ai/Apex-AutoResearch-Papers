\section{Limitations}
\label{sec:limitations}

Our analysis has three main limitations in scope.
First, the probing and steering experiments focus primarily on the English--Chinese language pair, with German serving only as supplementary evidence for cross-lingual transfer; whether the detection--decision dissociation and transfer asymmetry patterns hold for typologically distant pairs (e.g., English--Japanese, English--Arabic) remains to be verified.
Second, we evaluate two model families (Llama-3.1-8B-Instruct and Qwen3-8B), which limits the generality of architectural conclusions; in particular, the causal steering intervention succeeded only in Llama at layer~13, and we cannot confirm whether the mid-layer causal node exists at comparable depth in Qwen or other architectures.
Third, our conflict dataset is constructed from entity-centric factual statements following \citet{zhao2026when}, and the findings may not extend to other conflict types such as opinion-based or temporally contingent contradictions.
