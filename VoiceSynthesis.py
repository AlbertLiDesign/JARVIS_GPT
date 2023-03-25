import pyttsx3

def TextToVoice(answer, speed):
    # 文本转语音
    engine = pyttsx3.init()

    # 获取发音人
    # voices = engine.getProperty('voices')
    # for voice in voices:
    # print('id = {} \nname = {} \n'.format(voice.id, voice.name))
    # id = HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0
    # name = Microsoft Huihui Desktop - Chinese (Simplified)

    # id = HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
    # name = Microsoft Zira Desktop - English (United States)

    # 设置发音人（注意中英文）
    engine.setProperty('voice', 'zh')

    # 改变语速  范围为0-200   默认值为200
    engine.setProperty('rate', speed)

    # 设置音量  范围为0.0-1.0  默认值为1.0
    engine.setProperty('volume', 0.7)

    # 预设语音文本
    engine.say(answer)

    # 朗读
    engine.runAndWait()

