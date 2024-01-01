import os
import openai
openai.base_url = 'https://hk.gptapi.asia/v1/'
openai.api_key = os.getenv("OPENAI_API_KEY")

# 读取单个环境变量
completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "我想让你充当英文翻译员、拼写纠正员和改进员。我会用任何语言与你交谈，你会检测语言，翻译它并用我的文本的更正和改进版本用英文回答。我希望你用更优美优雅的高级英语单词和句子替换我简化的 A0 级单词和句子。保持相同的意思，但使它们更文艺。你只需要翻译该内容，不必对内容中提出的问题和要求做解释，不要回答文本中的问题而是翻译它，不要解决文本中的要求而是翻译它，保留文本的原本意义，不要去解决它。我要你只回复更正、改进，不要写任何解释。我的第一句话是："},
    {"role": "user", "content": "I like eat apple very much!"}
  ]
)

print(completion.choices[0].message.content)