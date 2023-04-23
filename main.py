from SpeechModules.WakeWord import PicoWakeWord
from SpeechModules.Speech2Text import BaiduASR, AzureASR
from SpeechModules.Text2Speech import BaiduTTS, Pyttsx3TTS, AzureTTS
from ChatModules.OpenAIChatModule import OpenaiChatModule
import struct

PICOVOICE_API_KEY = ""  # 你的picovoice key
keyword_path = ''  # 你的唤醒词检测离线文件地址
Baidu_APP_ID = ''  # 你的百度APP_ID
Baidu_API_KEY = ''  # 你的百度API_KEY
Baidu_SECRET_KEY = ''  # 你的百度SECRET_KEY
openai_api_key = ""  # 你的openai api key

AZURE_API_KEY = ""  # 你的azure api key
AZURE_REGION = ""  # 你的azure region

print("初始化中...")
print("请说出唤醒词！")


def run(picowakeword, asr, tts, openai_chat_module):
    while True:  # 需要始终保持对唤醒词的监听
        audio_obj = picowakeword.stream.read(picowakeword.porcupine.frame_length, exception_on_overflow=False)
        audio_obj_unpacked = struct.unpack_from("h" * picowakeword.porcupine.frame_length, audio_obj)
        keyword_idx = picowakeword.porcupine.process(audio_obj_unpacked)
        if keyword_idx >= 0:
            picowakeword.porcupine.delete()
            picowakeword.stream.close()
            picowakeword.myaudio.terminate()  # 需要对取消对麦克风的占用!

            print("嗯,我在,请讲！")
            tts.text_to_speech_and_play("嗯,我在,请讲！")
            while True:  # 进入一次对话session
                q = asr.speech_to_text()
                print(f'[调试]: 通过麦克风识别, 文本={q}')
                res = openai_chat_module.chat_with_origin_model(q)
                print(res)
                tts.text_to_speech_and_play('嗯' + res)


def Orator():
    picowakeword = PicoWakeWord(PICOVOICE_API_KEY, keyword_path)
    asr = AzureASR(AZURE_API_KEY, AZURE_REGION)
    tts = AzureTTS(AZURE_API_KEY, AZURE_REGION)
    openai_chat_module = OpenaiChatModule(openai_api_key)
    try:
        run(picowakeword, asr, tts, openai_chat_module)
    except KeyboardInterrupt:
        if picowakeword.porcupine is not None:
            picowakeword.porcupine.delete()
            print("Deleting porc")
        if picowakeword.stream is not None:
            picowakeword.stream.close()
            print("Closing stream")
        if picowakeword.myaudio is not None:
            picowakeword.myaudio.terminate()
            print("Terminating pa")
            exit(0)
    finally:
        print('本轮对话结束')
        tts.text_to_speech_and_play('嗯' + '主人，我退下啦！')
        if picowakeword.porcupine is not None:
            picowakeword.porcupine.delete()
            print("[调试]: Deleting porc")
        if picowakeword.stream is not None:
            picowakeword.stream.close()
            print("[调试]: Closing stream")
        if picowakeword.myaudio is not None:
            picowakeword.myaudio.terminate()
            print("[调试]: Terminating pa")
        Orator()


if __name__ == '__main__':
    Orator()
