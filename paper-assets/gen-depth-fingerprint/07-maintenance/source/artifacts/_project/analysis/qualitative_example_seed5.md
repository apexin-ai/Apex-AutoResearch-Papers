## Seed 5, Pythia-2.8B, Continuation

### Gen-0 (Wikipedia seed: Abraham Lincoln)

Abraham Lincoln ( ; February 12, 1809 -- April 15, 1865) was an American lawyer, politician, and statesman who served as the 16th president of the United States from 1861 until his assassination in 1865. Lincoln led the Union through the American Civil War to defend the nation as a constitutional union and succeeded in defeating the insurgent Confederacy, abolishing slavery, expanding the power of the federal government, and modernizing the U.S. economy.

Lincoln was born into poverty in a log cabin in Kentucky and was raised on the frontier, primarily in Indiana. He was self-educated and became a lawyer, Whig Party leader, Illinois state legislator, and U.S. congressman from Illinois. In 1849, he returned to his successful law practice in Springfield, Illinois. In 1854, he was angered by t

### Gen-1

, and he was defeated in the 1864 presidential election by Democrat Andrew Johnson.

Lincoln's death in 1865, the end of the war, and the election of Republican Abraham Lincoln's successor, Republican Ulysses S. Grant, were all met with celebration in the North.

The Civil War

In the 1860 presidential election, Lincoln was opposed by former Democrat Stephen A. Douglas, who had been a leader of the pro-slavery Democratic Party and a supporter of the Fugitive Slave Act of 1850. Lincoln had been a strong supporter of the Fugitive Slave Act, and was a strong supporter of the Kansas--Nebraska Act, which had been passed by the Kansas Legislature and was signed by President James Buchanan in 1854. The Fugitive Slave Act of 1850 allowed for the return of slaves who had escaped from their owners to

### Gen-2

's support of Douglas was a key factor in the split in the Republican Party.

Douglas was the first prominent politician to recognize the growing anti-slavery movement and to advocate for its repeal. In 1854, he wrote a series of letters to the editor of the New York Times, urging that the Fugitive Slave Law be repealed. He also wrote to the editor of the Chicago Tribune, urging that the law be repealed and that all of the laws passed by the Lincoln administration be rescinded. Douglas was a strong opponent of the Kansas--Nebraska Act, which was supported by Lincoln. He was also opposed to the Compromise of 1850, which Lincoln supported.

Douglas's opposition to the Fugitive Slave Law of 1850 and to the Kansas--Nebraska Act of 1854 made him a controversial figure in Illinois. He was a suppor

### Gen-3

member of the Illinois House of Representatives in 1851, and he was a delegate to the Republican National Convention in 1856. He was elected to the United States Senate in 1858, and he was reelected in 1860. Douglas was the only Republican to hold the office of Vice President of the United States from 1861 until March 4, 1865, when Abraham Lincoln was assassinated. He was the last Republican to hold the office of Vice President, and he was the only Republican to be elected to the office of Vice President until the election of Chester A. Arthur in 1876. Douglas was the first Republican to be elected to the office of Vice President since Andrew Johnson in 1868.

Douglas was the leader of the Republican Party in Illinois from 1860 to 1872, and he was a member of the Republican National Commi

### Gen-4

defeated by Democrat Winfield Scott Hancock. Douglas was the chairman of the Republican National Committee from 1876 to 1879. Douglas was the Republican candidate for President in 1884, but he was defeated by Democrat Grover Cleveland. Douglas was the Republican nominee for President in 1888, but he was defeated by Democrat Benjamin Harrison. Douglas was the Republican nominee for President in 1892, and he was defeated by Democrat Grover Cleveland. Douglas was the Republican nominee for President in 1896, but he was defeated by Democrat William McKinley. Douglas was the Republican nominee for President in 1900, and he was defeated by Democrat William Jennings Bryan. Douglas was the Republican nominee for President in 1908, but he was defeated by Democrat William Howard Taft. Douglas was t

### Feature Values (features_all_models.csv)

| Feature | Gen-0 | Gen-1 | Gen-2 | Gen-3 | Gen-4 |
| --- | --- | --- | --- | --- | --- |
| entropy_mean | 2.358 | 2.638 | 2.792 | 2.021 | 1.185 |
| entropy_std | 1.516 | 1.745 | 1.808 | 1.268 | 1.358 |
| entropy_min | 0.002 | 0.002 | 0.001 | 0.002 | 0.002 |
| entropy_max | 7.000 | 6.996 | 8.047 | 7.691 | 6.180 |
| tail_decay | -0.00231 | -0.00243 | -0.00225 | -0.00277 | -0.00272 |
| ttr | 0.660 | 0.522 | 0.467 | 0.350 | 0.260 |
| hapax_ratio | 0.555 | 0.373 | 0.317 | 0.200 | 0.178 |

### Observations

- **TTR collapse**: Type-token ratio drops monotonically from 0.660 (gen-0) to 0.260 (gen-4), a 60% reduction. Vocabulary diversity collapses across generations.
- **Hapax ratio decline**: Proportion of words used exactly once drops from 0.555 to 0.178, indicating increasing repetition of the same words.
- **Entropy non-monotone**: entropy_mean rises slightly from gen-0 to gen-2 then drops sharply at gen-3/4, consistent with transition from diverse text to repetitive loops.
- **Content degeneration visible in text**: By gen-3/4, the model produces factually absurd repetitive lists ("Douglas was the Republican nominee for President in 1884/1888/1892/1896/1900/1908...").
- **tail_decay** stays relatively stable across depths, suggesting token-rank distribution shape is less sensitive to iterative generation than vocabulary diversity metrics.
