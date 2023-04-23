### ChatGPT 智能音箱

1.打开`main.py`文件，修改以下参数

```python
PICOVOICE_API_KEY = ""  # 你的picovoice key
# 你的唤醒词检测离线文件地址,该项目唤醒词是hi siri
keyword_path = './SpeechModules/SpeechModulesFile/hi-siri_en_windows_v2_2_0.ppn'  # 你的唤醒词检测离线文件地址
Baidu_APP_ID = ''  # 你的百度APP_ID
Baidu_API_KEY = ''  # 你的百度API_KEY
Baidu_SECRET_KEY = ''  # 你的百度SECRET_KEY
openai_api_key = ""

AZURE_API_KEY = "" # 你的Azure API Key
AZURE_REGION = "" # 你的Azure Region
```

2.打开`OpenAiChatModule.py`文件，修改以下参数

```python
openai_api_key = "" # 请替换为自己的API KEY
```

3.打开`WakeWord.py`修改以下参数

```python
PICOVOICE_API_KEY = ""  # 请替换为自己的API KEY
keyword_path = './SpeechModulesFile/hi-siri_en_windows_v2_2_0.ppn' # 请替换为自己的唤醒词路径
```

4.打开`Text2Speech.py`修改以下参数

```python
# 百度TTS的语音服务
result = self.client.synthesis(text, 'zh', 1, {
            'spd': 5, # 语速
            'vol': 5, # 音量大小
            'per': 4  # 发声人 百度丫丫
        })  # 得到音频的二进制文件

# Azure TTS的语音服务
self.speech_config.speech_synthesis_voice_name = "zh-CN-XiaoyouNeural"

# 百度ASR的语音服务
APP_ID = '' # 你的百度APP_ID
API_KEY = '' # 你的百度API_KEY
SECRET_KEY = '' # 你的百度SECRET_KEY

# Azure ASR的语音服务
AZURE_API_KEY = "" # 你的Azure API Key
AZURE_REGION = ""# 你的Azure Region
```

5.打开`Speech2Text.py`修改以下参数
```python
if __name__ == '__main__':
    APP_ID = '' # 你的百度APP_ID
    API_KEY = '' # 你的百度API_KEY
    SECRET_KEY = '' # 你的百度SECRET_KEY
    baiduasr = BaiduASR(APP_ID, API_KEY, SECRET_KEY)
    result = baiduasr.speech_to_text()
    print(result)

    AZURE_API_KEY = "" # 你的Azure API Key
    AZURE_REGION = "" # 你的Azure Region
    azureasr = AzureASR(AZURE_API_KEY, AZURE_REGION)
    azureasr.speech_to_text()
```