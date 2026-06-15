**[Voice_Input] -> [faster-whisper for transcription] -> [local Ollama LLM (Qwen3:1B)] -> [qwen3_tts for text_to_speech] -> [voice cloning of VALORANT's agent "Clove"] -> [Voice_Output]**

**[CHALLENGES]:**

Downloading the required packages, libraries, modules, since there were multiple dependency failures due to latest python version, model size, module file size

multiple bugs while importing faster-whisper for voice transcription

Too much time wasted for correct LLM choice decision! since smaller gave bad response, bigger ones took more time! 

finalizing the correct voice transcription model, chose google at first, but required internet, and not very good results! Then decided to go with faster_whisper from openAI

trying multiple voice models :-
1) pyttsx
2) kokoro
3) XTTS-v3
4) coqui_TTS
5) web software "MinimaxAudio", has paid API
6) web software "ElevenLabs", has paid API
7) weight.gg/replay to train my own model locally on CPU, took way too much time, dropped 
8) qwen3_tts (the correct decision) 

qwen3_tts gave me the desired results for the voice cloning for CLove (as she sounds in VALORANT game)

finally training qwen3_TTS on GOOGLE colab for free!

faced multiple dependency failures in colab notebook (such as fast_attn not available) (qwen3_tts) not installed correctly

After voice cloning/training, finally created a web Python API via pyngrok

hosted a local pyngrok server for API integration, which finally led to the completion and success of my handwritten python automation script


**[HELPING RESOURCES]**

1) OpenAI chatGPT, for entire plan execution strategy, crazy project feature suggestions + bug identifications

2) gemini for GOOGLE colab, web python API helping!

3) code generation WAS NOT DONE BY ANY AI, help was taken to find critical bugs, dependency hell fixes, and general issue/suggestions


