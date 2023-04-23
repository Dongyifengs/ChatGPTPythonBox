from aip import AipSpeech
import pygame
import pyttsx3
import azure.cognitiveservices.speech as speechsdk


class BaiduTTS:  # 百度语音合成
    def __init__(self, APP_ID, API_KEY, SECRET_KEY):
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def text_to_speech_and_play(self, text=""):  # 语音合成并播放
        result = self.client.synthesis(text, 'zh', 1, {
            'spd': 5,  # 语速
            'vol': 5,  # 音量大小
            'per': 4  # 发声人 百度丫丫
        })  # 得到音频的二进制文件

        if not isinstance(result, dict):  # 如果不是字典类型，说明合成成功
            with open("./audio.mp3", "wb") as f:
                f.write(result)
        else:  # 否则合成失败
            print("[调试]: 语音合成失败", result)
        # playsound('./audio.wav')
        self.play_audip_with_pygame('./audio.mp3')  # 使用pygame播放音频

    def play_audip_with_pygame(self, audio_file_path):  # 使用pygame播放音频
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(20)
        pygame.mixer.quit()


class Pyttsx3TTS:  # pyttsx3语音合成(备选)
    def __init__(self):
        pass

    def text_to_speech_and_play(self, text=""):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


class AzureTTS:
    def __init__(self, AZURE_API_KEY, AZURE_REGION):
        self.AZURE_API_KEY = AZURE_API_KEY
        self.AZURE_REGION = AZURE_REGION
        self.speech_config = speechsdk.SpeechConfig(subscription=AZURE_API_KEY, region=AZURE_REGION)
        self.speech_config = speechsdk.SpeechConfig(subscription=AZURE_API_KEY, region=AZURE_REGION)
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        # The language of the voice that speaks.
        self.speech_config.speech_synthesis_voice_name = "zh-CN-XiaoyouNeural"
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config,
                                                              audio_config=self.audio_config)

    def text_to_speech_and_play(self, text):
        # Get text from the console and synthesize to the default speaker.
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("[调试]: 文本语音合成 [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("[调试]: 取消语音合成:{}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("[调试]: 错误 :{}".format(cancellation_details.error_details))
                    print("[调试]: 您是否设置了语音资源键和区域值?")


if __name__ == '__main__':
    APP_ID = ''
    API_KEY = ''
    SECRET_KEY = ''

    baidutts = BaiduTTS(APP_ID, API_KEY, SECRET_KEY)
    baidutts.text_to_speech_and_play('春天来了，每天的天气都很好！')

    # pyttsx3tts = BaiduTTS(APP_ID, API_KEY, SECRET_KEY)
    # pyttsx3tts.text_to_speech_and_play('春天来了，每天的天气都很好！')

    AZURE_API_KEY = ""
    AZURE_REGION = ""
    azuretts = AzureTTS(AZURE_API_KEY, AZURE_REGION)
    azuretts.text_to_speech_and_play("嗯，你好，我是你的智能小伙伴，我的名字叫Murphy，你可以和我畅所欲言，我是很会聊天的哦！")
