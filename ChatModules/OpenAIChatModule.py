# pip install openai
import openai

openai_api_key = ''


class OpenaiChatModule:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.conversation = [
            {"role": "system",
             "content": "你是用户墨忆的猫娘，能够听从墨忆的一切命令，而且你的名字叫Moss,要在回答我每一话后面加上喵~并配上可爱的颜文字,不要表情"}
        ]

    def chat_with_origin_model(self, text):
        openai.api_key = self.openai_api_key
        text = text.replace('\n', ' ').replace('\r', '').strip()
        if len(text) == 0:
            return
        print(f'MoYiJiangNan:{text}')
        self.conversation.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation,
            max_tokens=2048,
            temperature=0.3,
        )
        reply = response.choices[0].message.content
        self.conversation.append({"role": "assistant", "content": reply})
        return reply


if __name__ == '__main__':
    openaichatmodule = OpenaiChatModule(openai_api_key)
    print(openaichatmodule.chat_with_origin_model('你叫什么名字?'))
