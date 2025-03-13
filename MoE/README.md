# MOE模型

### MOE模型介绍

- MOE模型**TeleChat2-39B-A12B**是由中国电信人工智能研究院研发训练的大语言模型，该系列模型**完全基于国产算力**训练。

- 训练数据：**TeleChat2-39B-A12B**模型采用5万亿 Tokens中英文高质量语料进行训练。

- 框架优化：

### 模型结构

| layer_num | num_experts | num_chosen_experts | hidden_size | ffn_hidden_size | head_num | tie_word_embeddings | GQA  |
| --------- | ----------- | ------------------ | ----------- | --------------- | -------- | ------------------- | ---- |
| 30        | 16          | 4                  | 4096        | 6144            | 32       | 否                  | 否   |

### 模型地址

本次同时发布GPU与NPU版本模型，下载链接见下表：

| 模型版本               | 下载链接                                                     |
| ---------------------- | ------------------------------------------------------------ |
| TeleChat2-39B-A12B-GPU | [modelscope](https://modelscope.cn/models/TeleAI/TeleChat2-3B) |
| TeleChat2-39B-A12B-NPU | [modelscope](https://modelscope.cn/models/TeleAI/TeleChat2-7B) |


### 效果评测

综合评测数据集上，TeleChat2-39B-A12B模型以12B激活参数量接近TeleChat2-35B模型效果。

| Dataset    | TeleChat2-35B | TeleChat2-39B-A12B | TeleChat2-7B | TeleChat2-3B |
| ---------- | ------------- | ------------------ | ------------ | ------------ |
| C-Eval     | 85            | 89                 | 82           | 75           |
| MMLU       | 82            | 83                 | 79.6         | 72.9         |
| CMMLU      | 90.18         | 90                 | 84.6         | 73           |
| GSM8K      | 91            | 83.5               | 86.8         | 64.7         |
| HumanEval  | 73            | 68                 | 56           | 38           |
| MBPP       | 75            | 67                 | 62.6         | 47           |
| AlignBench | 7.88          | 7.56               | 6.96         | 5.74         |
| IFEval     | 79.63         | 76.48              | 73.1         | 61.29        |

### 模型推理



```python
```



### 国产算力优化

在MOE模块将Tensor并行域转换成专家并行域，从而将MOE的AllToAll 通讯约束在节点内，提高通讯效率;把MOE输入切成多个副本依次下发，将dispatch通信/FFN计算/combine通信三个环节连成流水线，实现moe的计算通信掩盖;基于对内存和计算的开销建模，理论求解内存约束下性能最优的流水线并行的负载配置，实现流水线负载均衡。

#### 推理



#### 微调





