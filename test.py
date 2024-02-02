from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def get_similar_words(word):
    # 拆分输入文本并将其编码
    input_ids = tokenizer.encode(word, return_tensors='pt')
    with torch.no_grad():
        embeddings = model(input_ids)[0]
    # 计算标记之间的余弦相似度
    cosine_similarities = torch.nn.functional.cosine_similarity(embeddings, embeddings)
    # 获取相似度最高的标记
    similar_word_idx = cosine_similarities.argsort().numpy()[0][-2]
    similar_word = tokenizer.decode([similar_word_idx])
    return similar_word